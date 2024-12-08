from __future__ import division
import numpy as np
import os
import geopandas as gpd
from datetime import datetime, timedelta, date
import sys
from osgeo import gdal
import pandas as pd
import glob
import shapely.speedups

shapely.speedups.enable()

#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        ThisYear ThisWeek
#ArgNum   1        2     

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

#ClimDivShpFile = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS_EPSG2163.shp'
ClimDivShpFile = '/discover/nobackup/syatheen/NIDIS/Data/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS_EPSG2163.shp'

ThisYear = int(round(float(sys.argv[1])))
ThisWeek = int(round(float(sys.argv[2])))

RefDateVecList = [ ThisYear-1, 12, 31, 0, 0, 0]

RefDate = date(RefDateVecList[0], RefDateVecList[1], RefDateVecList[2])
ThisDate = RefDate + timedelta(days=ThisWeek*7)
ThisMonth = ThisDate.month
ThisDoM = ThisDate.day

ArrayFileName = 'InfoArrsWeekly/'+format(ThisYear,'04')+format(ThisMonth,'02')+format(ThisDoM,'02')+'.npz'

QuickDRI_LowerLimit = -200
QuickDRI_UpperLimit = 200

SourceFilePath = 'Data/'

#######END ANY EDITS REQUIRED#########

#BEGIN GETTING CLIMDIV SHAPEFILE DATA
ClimDivShp = gpd.read_file(ClimDivShpFile)
CLIMDIV_SortedList_FrmShpFile = sorted(ClimDivShp.CLIMDIV.values.tolist())
#END GETTING CLIMDIV SHAPEFILE DATA

YYYYMMDD_Of_RefArrayForPrcntl = np.empty((1,1), dtype=np.int32)
YYYYMMDD_Of_RefArrayForPrcntl[:] = -9999
RefArrayForPrcntl = np.empty((1,len(CLIMDIV_SortedList_FrmShpFile)))
RefArrayForPrcntl[:] = np.NaN

YYYYMMDD_Of_RefArrayForPrcntl[0] = 10000*ThisYear + 100*ThisMonth + ThisDoM

FileNames_QuickDRI=glob.glob(SourceFilePath+'qdri_'+format(ThisYear,'04')+'wk'+format(ThisWeek,'02')+'.tif')

if (len(FileNames_QuickDRI) == 1):

  BaseFileNameWithPath = SourceFilePath+'qdri_'+format(ThisYear,'04')+'wk'+format(ThisWeek,'02')
  BaseFileName = 'qdri_'+format(ThisYear,'04')+'wk'+format(ThisWeek,'02')
  
  IfTifFileExists = os.path.exists('{}.tif'.format(BaseFileNameWithPath))
  if IfTifFileExists:
    inDs = gdal.Open('{}.tif'.format(BaseFileNameWithPath))
    outDs = gdal.Translate('TempCreatedFiles/{}.xyz'.format(BaseFileName), inDs, format='XYZ', creationOptions=["ADD_HEADER_LINE=YES"])
    outDs = None
    try:
      os.remove('TempCreatedFiles/{}.csv'.format(BaseFileName))
    except OSError:
      pass
    os.rename('TempCreatedFiles/{}.xyz'.format(BaseFileName), 'TempCreatedFiles/{}.csv'.format(BaseFileName))
    GridPoints_XYZ_df = pd.read_csv('TempCreatedFiles/{}.csv'.format(BaseFileName), sep = ' ', header = 0, dtype = 'float64')
    try:
      os.remove('TempCreatedFiles/{}.csv'.format(BaseFileName))
    except OSError:
      pass

    Valid_GridPoints_XYZ_df = GridPoints_XYZ_df.loc[(GridPoints_XYZ_df.Z >= QuickDRI_LowerLimit) & (GridPoints_XYZ_df.Z <= QuickDRI_UpperLimit)]
    Valid_GridPoints_XYZ_df.reset_index(drop=True, inplace=True)
    GridPoints_gdf = gpd.GeoDataFrame(Valid_GridPoints_XYZ_df, geometry=gpd.points_from_xy(Valid_GridPoints_XYZ_df.X, Valid_GridPoints_XYZ_df.Y))

    for iClimDiv in range(len(CLIMDIV_SortedList_FrmShpFile)):

      Sel_ClimDivShp = ClimDivShp.loc[ ClimDivShp.CLIMDIV == CLIMDIV_SortedList_FrmShpFile[iClimDiv] ]
      Sel_ClimDivShp.reset_index(drop=True, inplace=True)
      GridPoints_gdf_mask = GridPoints_gdf.intersects(Sel_ClimDivShp.loc[0, 'geometry'])
      GridPoints_gdf_Sel = GridPoints_gdf.loc[GridPoints_gdf_mask]
      if len(GridPoints_gdf_Sel) > 0:
        RefArrayForPrcntl[0, iClimDiv] = GridPoints_gdf_Sel['Z'].mean()
    
    #end of for iClimDiv in range(len(CLIMDIV_SortedList_FrmShpFile))

  #end of if IfTifFileExists

#end of if (len(FileNames_QuickDRI) == 1)

print("YYYYMMDD_Of_RefArrayForPrcntl.shape is ",YYYYMMDD_Of_RefArrayForPrcntl.shape)
print("YYYYMMDD_Of_RefArrayForPrcntl is ",YYYYMMDD_Of_RefArrayForPrcntl)
print("RefArrayForPrcntl.shape is ",RefArrayForPrcntl.shape)
print("RefArrayForPrcntl is ",RefArrayForPrcntl)
print("np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)))
print("np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)))
print('overall min is ',np.nanmin(RefArrayForPrcntl),', overall max is ',np.nanmax(RefArrayForPrcntl))

np.savez_compressed(ArrayFileName, YYYYMMDD_Of_RefArrayForPrcntl = YYYYMMDD_Of_RefArrayForPrcntl, RefArrayForPrcntl = RefArrayForPrcntl)

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")


