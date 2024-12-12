from __future__ import division
import numpy as np
import os
import rasterio
from rasterio.features import shapes
import geopandas as gpd
from datetime import datetime, timedelta, date
import sys
import pandas as pd
import glob
import os
from calendar import monthrange

#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        ArgYearInt ArgMonthInt 
#ArgNum   1          2          

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

#ClimDivShpFile = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS_EPSG4326.shp'
ClimDivShpFile = '/discover/nobackup/syatheen/NIDIS/Data/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS_EPSG4326.shp'

mask = None

ArgYearInt = int(round(float(sys.argv[1])))
ArgMonthInt = int(round(float(sys.argv[2])))

cmd = 'mkdir -p /discover/nobackup/projects/nca/syatheen/ESA_CCI_Npzs/'
os.system(cmd)

ArrayFileName = '/discover/nobackup/projects/nca/syatheen/ESA_CCI_Npzs/ESA_CCI_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '_ClimDivs.npz'

SourceFileBasePath = '/discover/nobackup/projects/nca/syatheen/'

ESA_CCI_LowerLimit = 0.

#######END ANY EDITS REQUIRED#########

#BEGIN GETTING CLIMDIV SHAPEFILE DATA
ClimDivShp = gpd.read_file(ClimDivShpFile)
CLIMDIV_SortedList_FrmShpFile = sorted(ClimDivShp.CLIMDIV.values.tolist())
#END GETTING CLIMDIV SHAPEFILE DATA

NumDaysInMonth = int(round(float(monthrange(ArgYearInt, ArgMonthInt)[1]))) 

YYYYMMDD_Of_RefArrayForPrcntl = np.empty((NumDaysInMonth, 1), dtype=np.int32)
YYYYMMDD_Of_RefArrayForPrcntl[:] = -9999
RefArrayForPrcntl = np.empty((NumDaysInMonth, len(CLIMDIV_SortedList_FrmShpFile)))
RefArrayForPrcntl[:] = np.NaN

for WhichDayInMonth in range(1, NumDaysInMonth+1):

  YYYYMMDD_Of_RefArrayForPrcntl[WhichDayInMonth-1] = 10000*ArgYearInt + 100*ArgMonthInt + WhichDayInMonth 
  SourceFile = SourceFileBasePath + 'ESA_CCI/ESA_CCI_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + format(WhichDayInMonth,'02') + '.tif'

  IfTifFileExists = os.path.exists(SourceFile)
  if IfTifFileExists:
    with rasterio.Env():
      with rasterio.open(SourceFile) as SrcInfo:
        ImageInfo = SrcInfo.read()
        results = ( {'properties': {'raster_val': vv}, 'geometry': ss}
                   for ii, (ss, vv) in enumerate( shapes(ImageInfo, mask = mask,
                                                         transform = SrcInfo.transform)))
        geoms = list(results)
        gpd_polygonized_raster  = gpd.GeoDataFrame.from_features(geoms)
        gpd_polygonized_raster.crs = SrcInfo.crs
  
        Intrsct = gpd.overlay(df1 = gpd_polygonized_raster, df2 = ClimDivShp)
  
        for iClimDiv in range(len(CLIMDIV_SortedList_FrmShpFile)):
  
          Sel_Intrsct = Intrsct.loc[ (Intrsct.CLIMDIV == CLIMDIV_SortedList_FrmShpFile[iClimDiv]) &
                                     ( ~(Intrsct.geometry.is_empty | Intrsct.geometry.isna()) ) &
                                     ( ~(Intrsct.raster_val.isnull()) ) &
                                     ~np.isnan( Intrsct.raster_val ) &
                                     ( Intrsct.raster_val >= ESA_CCI_LowerLimit  ) &
                                     (Intrsct.geometry.area > 0) ]
          if len(Sel_Intrsct.index) > 0:
            RefArrayForPrcntl[WhichDayInMonth-1, iClimDiv] = (Sel_Intrsct.raster_val*Sel_Intrsct.geometry.area).sum()/Sel_Intrsct.geometry.area.sum()
  
        #end of for iClimDiv in range(len(CLIMDIV_SortedList_FrmShpFile))
      #end of with rasterio.open(SourceFile) as SrcInfo
    #with rasterio.Env()
  #end of if IfTifFileExists

#end of for WhichDayInMonth in range(1, NumDaysInMonth+1)

print("YYYYMMDD_Of_RefArrayForPrcntl.shape is ",YYYYMMDD_Of_RefArrayForPrcntl.shape)
print("YYYYMMDD_Of_RefArrayForPrcntl is ",YYYYMMDD_Of_RefArrayForPrcntl)
print("RefArrayForPrcntl.shape is ",RefArrayForPrcntl.shape)
print("RefArrayForPrcntl is ",RefArrayForPrcntl)
print("np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)))
print("np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)))
print("np.amin(np.isnan(RefArrayForPrcntl).sum(axis=1)) is ",np.amin(np.isnan(RefArrayForPrcntl).sum(axis=1)))
print("np.amax(np.isnan(RefArrayForPrcntl).sum(axis=1)) is ",np.amax(np.isnan(RefArrayForPrcntl).sum(axis=1)))
print('overall min is ',np.nanmin(RefArrayForPrcntl),', overall max is ',np.nanmax(RefArrayForPrcntl))

np.savez_compressed(ArrayFileName, YYYYMMDD_Of_RefArrayForPrcntl = YYYYMMDD_Of_RefArrayForPrcntl, RefArrayForPrcntl = RefArrayForPrcntl)

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")


