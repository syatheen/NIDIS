#!/usr/bin/env python
# Coded by Soni Yatheendradas
#         on Nov 18, 2024
# NOTE: This is a non-multiprocessing & original style copy of InfoArrays_gdalWarp_ClimGrid1D_DailyCollToMonthly_Indicators_113.py (GlobSnow3) existing at Gitbub path nidis/nidis/model/nclimgrid/spatial_resolution/ 
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
from osgeo import gdal
import shapely.speedups
import fiona
import copy

shapely.speedups.enable()

# NOTE: sys.argv indices start at 1, not 0
# Python arguments to this program will be (for now):
#        ArgIndicator ArgYearInt ArgMonthInt ArgBeginDoM_Int ArgEndDoM_Int   
# ArgNum  1            2          3           4               5
  
ssstart_Overall = datetime.now()
  
#######BEGIN ANY EDITS REQUIRED#######
  
ArgIndicator = sys.argv[1] 
ArgYearInt = int(round(float(sys.argv[2])))
ArgMonthInt = int(round(float(sys.argv[3])))
ArgBeginDoM_Int = int(round(float(sys.argv[4])))
ArgEndDoM_Int = int(round(float(sys.argv[5])))

if ArgIndicator == 'GlobSnow3': 
    ClimGrid1DShpFile = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/nClmGrd_as_ply_NoNns_wGlbSnw3RwCl.shp'
#end of if ArgIndicator == 'GlobSnow3'
 
NameKeys_PathToSaveDataValues = ( (('GlobSnow3',), '/discover/nobackup/projects/nca/syatheen/GlobSnow3_Npzs'),  )
Dict_of_Name_PathToSaveData_Pairs = { key : value for keys, value in NameKeys_PathToSaveDataValues for key in keys } 
os.makedirs(Dict_of_Name_PathToSaveData_Pairs[ArgIndicator], exist_ok=True)
 
if ArgIndicator == 'GlobSnow3': 

    ArrayFileName = os.path.join(
        Dict_of_Name_PathToSaveData_Pairs[ArgIndicator], ArgIndicator + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '_ClimGrid1D.npz')

    SourceFileBasePath = '/discover/nobackup/projects/nca/syatheen/' + ArgIndicator
  
    LowerLimit = 0.
  
#end of if ArgIndicator == 'GlobSnow3'
      
#######END ANY EDITS REQUIRED#########
  
#BEGIN GETTING PxlRowCol ETC SHAPEFILE DATA
ClimGrid1DShp = gpd.read_file(ClimGrid1DShpFile)
PxlRowCol_Arr_FrmShpFile = ClimGrid1DShp.PxlRowCol.values
SortingIdxs = np.argsort(PxlRowCol_Arr_FrmShpFile)
#END GETTING PxlRowCol ETC SHAPEFILE DATA
  
#BEGIN GETTING PxlRowCol ETC OF GLOBSNOW3 GRID
IndicatorGridRowCol_Arr_FrmShpFile = ClimGrid1DShp.grid_code.values
IndicatorGridRowCol_SortedArr_FrmShpFile = IndicatorGridRowCol_Arr_FrmShpFile[SortingIdxs]
IndicatorGridRow_SortedArr_FrmShpFile = (np.around(IndicatorGridRowCol_SortedArr_FrmShpFile // 1000)).astype(int)
IndicatorGridCol_SortedArr_FrmShpFile = (np.around(IndicatorGridRowCol_SortedArr_FrmShpFile % 1000)).astype(int)
del IndicatorGridRowCol_SortedArr_FrmShpFile
#END GETTING PxlRowCol ETC SHAPEFILE DATA OF GLOBSNOW3 GRID

NumDaysInMonth = int(round(float(monthrange(ArgYearInt, ArgMonthInt)[1]))) 
if ArgBeginDoM_Int < 0:
    BeginningDayInMonth = 1
else:
    BeginningDayInMonth = ArgBeginDoM_Int
#end of if ArgBeginDoM_Int < 0
if ArgEndDoM_Int < 0:
    EndingDayInMonth = NumDaysInMonth
else:
    EndingDayInMonth = ArgEndDoM_Int
#end of if ArgEndDoM_Int < 0
  
YYYYMMDD_Of_InfoArray = np.empty((EndingDayInMonth - BeginningDayInMonth + 1, 1), dtype=np.int32)
YYYYMMDD_Of_InfoArray[:] = -9999
InfoArray = np.empty((EndingDayInMonth - BeginningDayInMonth + 1, PxlRowCol_Arr_FrmShpFile.size))
InfoArray[:] = np.NaN

del PxlRowCol_Arr_FrmShpFile
  
for WhichDayInMonth in range(BeginningDayInMonth, EndingDayInMonth + 1):
  
    YYYYMMDD_Of_InfoArray[WhichDayInMonth - BeginningDayInMonth] = 10000 * ArgYearInt + 100 * ArgMonthInt + WhichDayInMonth # SY: NOTE [WhichDayInMonth - BeginningDayInMonth] instead of [WhichDayInMonth - 1]  
    if ArgIndicator == 'GlobSnow3': 
        SourceFile = os.path.join(SourceFileBasePath, ArgIndicator + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + format(WhichDayInMonth,'02') + '.tif')
    #end of if ArgIndicator == 'ESA_CCI'

    IfTifFileExists = os.path.exists(SourceFile)
    if IfTifFileExists:

        with rasterio.Env():
            with rasterio.open(SourceFile) as SrcInfo:
    
                ImageInfo = SrcInfo.read()
      
#                ImageInfo = np.flip(ImageInfo, axis = 1)
      
                InfoArray[WhichDayInMonth - BeginningDayInMonth, :] = ImageInfo[0, IndicatorGridRow_SortedArr_FrmShpFile, IndicatorGridCol_SortedArr_FrmShpFile] # SY: NOTE [WhichDayInMonth - BeginningDayInMonth] instead of [WhichDayInMonth - 1] 
        
            #end of with rasterio.open(..
        #end of with rasterio.Env()
  
    #end of if IfTifFileExists
  
#end of for WhichDayInMonth in range(BeginningDayInMonth, EndingDayInMonth + 1)
 
if ArgIndicator == 'GlobSnow3': 
    Idxs =  np.where(InfoArray < LowerLimit)
    InfoArray[Idxs] = np.nan
#end of if ArgIndicator == 'GlobSnow3'
 
print("YYYYMMDD_Of_InfoArray.shape is ",YYYYMMDD_Of_InfoArray.shape)
print("YYYYMMDD_Of_InfoArray is ",YYYYMMDD_Of_InfoArray)
print("InfoArray.shape is ",InfoArray.shape)
print("InfoArray is ",InfoArray)
print("np.amin(np.isnan(InfoArray).sum(axis=0)) is ",np.amin(np.isnan(InfoArray).sum(axis=0)))
print("np.amax(np.isnan(InfoArray).sum(axis=0)) is ",np.amax(np.isnan(InfoArray).sum(axis=0)))
print("np.amin(np.isnan(InfoArray).sum(axis=1)) is ",np.amin(np.isnan(InfoArray).sum(axis=1)))
print("np.amax(np.isnan(InfoArray).sum(axis=1)) is ",np.amax(np.isnan(InfoArray).sum(axis=1)))
print('overall min is ',np.nanmin(InfoArray),', overall max is ',np.nanmax(InfoArray))
  
np.savez_compressed(ArrayFileName,
                    YYYYMMDD_Of_InfoArray = YYYYMMDD_Of_InfoArray,
                    InfoArray = InfoArray)
  
eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")
  
