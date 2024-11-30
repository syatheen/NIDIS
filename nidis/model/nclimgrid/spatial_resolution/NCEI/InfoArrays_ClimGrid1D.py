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
import fiona

#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        ArgVariable ArgYearInt ArgMonthInt
#ArgNum   1           2          3     

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

cmd = 'mkdir -p /discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/'
os.system(cmd)

ClimGrid1DShpFile = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/nClimGrid_as_poly_NoNans.shp'

mask = None

ArgVariable = sys.argv[1] # Choices are: spei-gamma-01, spei-gamma-02, spei-gamma-03,
                          #              spei-gamma-06, spei-gamma-09, spei-gamma-12,
                          #              spei-gamma-24, spei-gamma-36, spei-gamma-48,
                          #              spei-gamma-60, spei-gamma-72,
                          #              spei-pearson-01, spei-pearson-02, spei-pearson-03,
                          #              spei-pearson-06, spei-pearson-09, spei-pearson-12,
                          #              spei-pearson-24, spei-pearson-36, spei-pearson-48,
                          #              spei-pearson-60, spei-pearson-72,
                          #              spi-gamma-01, spi-gamma-02, spi-gamma-03,
                          #              spi-gamma-06, spi-gamma-09, spi-gamma-12,
                          #              spi-gamma-24, spi-gamma-36, spi-gamma-48,
                          #              spi-gamma-60, spi-gamma-72,
                          #              spi-pearson-01, spi-pearson-02, spi-pearson-03,
                          #              spi-pearson-06, spi-pearson-09, spi-pearson-12,
                          #              spi-pearson-24, spi-pearson-36, spi-pearson-48,
                          #              spi-pearson-60, spi-pearson-72,
                          #              pet,
                          #              prcp, tavg, tmax
ArgYearInt = int(round(float(sys.argv[2])))
ArgMonthInt = int(round(float(sys.argv[3])))

ArrayFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/' + ArgVariable+'_'+format(ArgYearInt,'04')+format(ArgMonthInt,'02')+'_1DClimGrid.npz'

if ( (ArgVariable[0:10] == 'spei-gamma') or
     (ArgVariable[0:12] == 'spei-pearson') or
     (ArgVariable[0:9] == 'spi-gamma') or
     (ArgVariable[0:11] == 'spi-pearson') ):
  Variable_LowerLimit = -3.09
  Variable_UpperLimit = 3.09
elif (ArgVariable == 'pet'):
  Variable_LowerLimit = 0
  Variable_UpperLimit = 3.402823466385289e+38
elif ( (ArgVariable == 'tavg') or
       (ArgVariable == 'tmax') ):
  Variable_LowerLimit = -100
  Variable_UpperLimit = 100
elif (ArgVariable == 'prcp'):
  Variable_LowerLimit = 0
  Variable_UpperLimit = 2000
#end of if ( (ArgVariable[0:10] == 'spei-gamma') or...

SourceFile = '/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_monthly/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif'

#######END ANY EDITS REQUIRED#########

#BEGIN GETTING CLIMGRID1D SHAPEFILE DATA
ClimGrid1DShp = gpd.read_file(ClimGrid1DShpFile)
PxlRowCol_SortedList_FrmShpFile = sorted(ClimGrid1DShp.PxlRowCol.values.tolist())
PxlRowCol_SortedArr_FrmShpFile = np.array(PxlRowCol_SortedList_FrmShpFile)
PxlRow_SortedArr_FrmShpFile = (np.around(PxlRowCol_SortedArr_FrmShpFile // 10000)).astype(int)
PxlCol_SortedArr_FrmShpFile = (np.around(PxlRowCol_SortedArr_FrmShpFile % 10000)).astype(int)
#END GETTING CLIMGRID1D SHAPEFILE DATA

del PxlRowCol_SortedArr_FrmShpFile

YYYYMMDD_Of_InfoArray = np.empty((1,1), dtype=np.int32)
YYYYMMDD_Of_InfoArray[:] = -9999
InfoArray = np.empty((1,len(PxlRowCol_SortedList_FrmShpFile)))
del PxlRowCol_SortedList_FrmShpFile
InfoArray[:] = np.NaN

YYYYMMDD_Of_InfoArray[0] = 100 * ArgYearInt + ArgMonthInt

IfTifFileExists = os.path.exists(SourceFile)
if IfTifFileExists:
  with rasterio.Env():
    with rasterio.open(SourceFile) as SrcInfo:

      ImageInfo = SrcInfo.read()

      InfoArray[0, :] = ImageInfo[0, PxlRow_SortedArr_FrmShpFile, PxlCol_SortedArr_FrmShpFile] 

    #with rasterio.open(SourceFile) as SrcInfo
  #with rasterio.Env()
#end of if IfTifFileExists
del PxlRow_SortedArr_FrmShpFile 
del PxlCol_SortedArr_FrmShpFile

Idxs =  np.where( (InfoArray < Variable_LowerLimit) | (InfoArray > Variable_UpperLimit)  )
InfoArray[Idxs] = np.nan

print("YYYYMMDD_Of_InfoArray.shape is ",YYYYMMDD_Of_InfoArray.shape)
print("YYYYMMDD_Of_InfoArray is ",YYYYMMDD_Of_InfoArray)
print("InfoArray.shape is ",InfoArray.shape)
print("InfoArray is ",InfoArray)
print("np.amin(np.isnan(InfoArray).sum(axis=0)) is ",np.amin(np.isnan(InfoArray).sum(axis=0)))
print("np.amax(np.isnan(InfoArray).sum(axis=0)) is ",np.amax(np.isnan(InfoArray).sum(axis=0)))
print("np.amin(np.isnan(InfoArray).sum(axis=1)) is ",np.amin(np.isnan(InfoArray).sum(axis=1)))
print("np.amax(np.isnan(InfoArray).sum(axis=1)) is ",np.amax(np.isnan(InfoArray).sum(axis=1)))
print('overall min is ',np.nanmin(InfoArray),', overall max is ',np.nanmax(InfoArray))

np.savez_compressed(ArrayFileName, YYYYMMDD_Of_InfoArray = YYYYMMDD_Of_InfoArray, InfoArray = InfoArray)

del YYYYMMDD_Of_InfoArray 
del InfoArray

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")


