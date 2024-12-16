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
#        BaseFileName ThisClimDivsPortion
#ArgNum   1            2 

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

#ClimDivShp = gpd.read_file('/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS_EPSG4326.shp')
ClimDivShp = gpd.read_file('/discover/nobackup/syatheen/NIDIS/Data/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS_EPSG4326.shp')

BaseFileName = sys.argv[1]
ThisClimDivsPortion = sys.argv[2] # Value is '1st' or '2nd'

ThisYear = int(round(float(BaseFileName[13:17])))
ThisWeek = int(round(float(BaseFileName[17:20])))

RefDateVecList = [ ThisYear-1, 12, 31, 0, 0, 0]

RefDate = date(RefDateVecList[0], RefDateVecList[1], RefDateVecList[2])
ThisDate = RefDate + timedelta(days=ThisWeek*7)
ThisMonth = ThisDate.month
ThisDayOfMonth = ThisDate.day

ArrayFileName = '/discover/nobackup/projects/nca/syatheen/BlendedVHP_Npzs/' + BaseFileName[-6:] + '_' + format(ThisYear,'04')+format(ThisMonth,'02')+format(ThisDayOfMonth,'02') + '_' + ThisClimDivsPortion + 'ClimDivsPortion.npz'

BlendedVHP_LowerLimit = -9998

SourceFilePath = '/discover/nobackup/projects/nca/syatheen/BlendedVHP_RenamedTifs/'

#######END ANY EDITS REQUIRED#########

#BEGIN GETTING CLIMDIV SHAPEFILE DATA
CLIMDIV_SortedList_FrmShpFile = sorted(ClimDivShp.CLIMDIV.values.tolist())
#END GETTING CLIMDIV SHAPEFILE DATA

YYYYMMDD_Of_InfoArrayForPrcntl = np.empty((1, 1), dtype=np.int32)
YYYYMMDD_Of_InfoArrayForPrcntl[:] = -9999
if ThisClimDivsPortion == '1st':
  InfoArrayForPrcntl = np.empty((1, int(round(float(len(CLIMDIV_SortedList_FrmShpFile)/2)))))
elif ThisClimDivsPortion == '2nd':
  InfoArrayForPrcntl = np.empty((1, len(CLIMDIV_SortedList_FrmShpFile) - int(round(float(len(CLIMDIV_SortedList_FrmShpFile)/2)))))
InfoArrayForPrcntl[:] = np.NaN

YYYYMMDD_Of_InfoArrayForPrcntl[0] = 10000*ThisYear + 100*ThisMonth + ThisDayOfMonth

BaseFileNameWithPath = SourceFilePath + BaseFileName 
#BaseFileName = 

IfTifFileExists = os.path.exists('{}.tif'.format(BaseFileNameWithPath))
if IfTifFileExists:

  cmd = 'mkdir -p /discover/nobackup/projects/nca/syatheen/BlendedVHP_RenamedTifs/TempCreatedFiles'
  os.system(cmd)

  inDs = gdal.Open('{}.tif'.format(BaseFileNameWithPath))
  if ThisClimDivsPortion == '1st':
    outDs = gdal.Translate('/discover/nobackup/projects/nca/syatheen/BlendedVHP_RenamedTifs/TempCreatedFiles/{}_1stClimDivsPortion.xyz'.format(BaseFileName), inDs, format='XYZ', creationOptions=["ADD_HEADER_LINE=YES"])
  elif ThisClimDivsPortion == '2nd':
    outDs = gdal.Translate('/discover/nobackup/projects/nca/syatheen/BlendedVHP_RenamedTifs/TempCreatedFiles/{}_2ndClimDivsPortion.xyz'.format(BaseFileName), inDs, format='XYZ', creationOptions=["ADD_HEADER_LINE=YES"])
  outDs = None
  try:
    if ThisClimDivsPortion == '1st':
      os.remove('/discover/nobackup/projects/nca/syatheen/BlendedVHP_RenamedTifs/TempCreatedFiles/{}_1stClimDivsPortion.csv'.format(BaseFileName))
    elif ThisClimDivsPortion == '2nd':
      os.remove('/discover/nobackup/projects/nca/syatheen/BlendedVHP_RenamedTifs/TempCreatedFiles/{}_2ndClimDivsPortion.csv'.format(BaseFileName))
  except OSError:
    pass
  if ThisClimDivsPortion == '1st':
    os.rename('/discover/nobackup/projects/nca/syatheen/BlendedVHP_RenamedTifs/TempCreatedFiles/{}_1stClimDivsPortion.xyz'.format(BaseFileName), '/discover/nobackup/projects/nca/syatheen/BlendedVHP_RenamedTifs/TempCreatedFiles/{}_1stClimDivsPortion.csv'.format(BaseFileName))
  elif ThisClimDivsPortion == '2nd':
    os.rename('/discover/nobackup/projects/nca/syatheen/BlendedVHP_RenamedTifs/TempCreatedFiles/{}_2ndClimDivsPortion.xyz'.format(BaseFileName), '/discover/nobackup/projects/nca/syatheen/BlendedVHP_RenamedTifs/TempCreatedFiles/{}_2ndClimDivsPortion.csv'.format(BaseFileName))
  if ThisClimDivsPortion == '1st':
    GridPoints_XYZ_df = pd.read_csv('/discover/nobackup/projects/nca/syatheen/BlendedVHP_RenamedTifs/TempCreatedFiles/{}_1stClimDivsPortion.csv'.format(BaseFileName), sep = ' ', header = 0, dtype = 'float64')
  elif ThisClimDivsPortion == '2nd':
    GridPoints_XYZ_df = pd.read_csv('/discover/nobackup/projects/nca/syatheen/BlendedVHP_RenamedTifs/TempCreatedFiles/{}_2ndClimDivsPortion.csv'.format(BaseFileName), sep = ' ', header = 0, dtype = 'float64')
  try:
    if ThisClimDivsPortion == '1st':
      os.remove('/discover/nobackup/projects/nca/syatheen/BlendedVHP_RenamedTifs/TempCreatedFiles/{}_1stClimDivsPortion.csv'.format(BaseFileName))
    elif ThisClimDivsPortion == '2nd':
      os.remove('/discover/nobackup/projects/nca/syatheen/BlendedVHP_RenamedTifs/TempCreatedFiles/{}_2ndClimDivsPortion.csv'.format(BaseFileName))
  except OSError:
    pass

  #Valid_GridPoints_XYZ_df = GridPoints_XYZ_df.loc[(GridPoints_XYZ_df.Z >= BlendedVHP_LowerLimit) & (GridPoints_XYZ_df.Z <= BlendedVHP_UpperLimit)]
  Valid_GridPoints_XYZ_df = GridPoints_XYZ_df.loc[(GridPoints_XYZ_df.Z >= BlendedVHP_LowerLimit)]
  Valid_GridPoints_XYZ_df.reset_index(drop=True, inplace=True)
  GridPoints_gdf = gpd.GeoDataFrame(Valid_GridPoints_XYZ_df, geometry=gpd.points_from_xy(Valid_GridPoints_XYZ_df.X, Valid_GridPoints_XYZ_df.Y))

  if ThisClimDivsPortion == '1st':
    NumClimDivs = int(round(float(len(CLIMDIV_SortedList_FrmShpFile)/2)))   
  elif ThisClimDivsPortion == '2nd':
    NumClimDivs = len(CLIMDIV_SortedList_FrmShpFile) - int(round(float(len(CLIMDIV_SortedList_FrmShpFile)/2)))

  for iClimDiv in range(NumClimDivs):

    if ThisClimDivsPortion == '1st':
      Sel_ClimDivShp = ClimDivShp.loc[ ClimDivShp.CLIMDIV == CLIMDIV_SortedList_FrmShpFile[ iClimDiv ] ]
    elif ThisClimDivsPortion == '2nd':
      Sel_ClimDivShp = ClimDivShp.loc[ ClimDivShp.CLIMDIV == CLIMDIV_SortedList_FrmShpFile[ iClimDiv + int(round(float(len(CLIMDIV_SortedList_FrmShpFile)/2))) ] ]
    Sel_ClimDivShp.reset_index(drop=True, inplace=True)
    GridPoints_gdf_mask = GridPoints_gdf.intersects(Sel_ClimDivShp.loc[0, 'geometry'])
    GridPoints_gdf_Sel = GridPoints_gdf.loc[GridPoints_gdf_mask]
    if len(GridPoints_gdf_Sel) > 0:
      InfoArrayForPrcntl[0, iClimDiv] = GridPoints_gdf_Sel['Z'].mean()
  
  #end of for iClimDiv in range(NumClimDivs)

#end of if IfTifFileExists

print("YYYYMMDD_Of_InfoArrayForPrcntl.shape is ",YYYYMMDD_Of_InfoArrayForPrcntl.shape)
print("YYYYMMDD_Of_InfoArrayForPrcntl is ",YYYYMMDD_Of_InfoArrayForPrcntl)
print("InfoArrayForPrcntl.shape is ",InfoArrayForPrcntl.shape)
print("InfoArrayForPrcntl is ",InfoArrayForPrcntl)
print("np.amin(np.isnan(InfoArrayForPrcntl).sum(axis=0)) is ",np.amin(np.isnan(InfoArrayForPrcntl).sum(axis=0)))
print("np.amax(np.isnan(InfoArrayForPrcntl).sum(axis=0)) is ",np.amax(np.isnan(InfoArrayForPrcntl).sum(axis=0)))
print("np.amin(np.isnan(InfoArrayForPrcntl).sum(axis=1)) is ",np.amin(np.isnan(InfoArrayForPrcntl).sum(axis=1)))
print("np.amax(np.isnan(InfoArrayForPrcntl).sum(axis=1)) is ",np.amax(np.isnan(InfoArrayForPrcntl).sum(axis=1)))
print('overall min is ',np.nanmin(InfoArrayForPrcntl),', overall max is ',np.nanmax(InfoArrayForPrcntl))

np.savez_compressed(ArrayFileName, YYYYMMDD_Of_InfoArrayForPrcntl = YYYYMMDD_Of_InfoArrayForPrcntl, InfoArrayForPrcntl = InfoArrayForPrcntl)

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")


