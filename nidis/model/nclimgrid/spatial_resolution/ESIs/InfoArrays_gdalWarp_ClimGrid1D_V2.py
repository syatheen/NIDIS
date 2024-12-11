#!/usr/bin/env python
from __future__ import division
import numpy as np
import sys
import os
import rasterio
from rasterio.features import shapes
import geopandas as gpd
from datetime import date, datetime, timedelta
import glob
import time
from calendar import monthrange
from osgeo import gdal
#import shapely.speedups # SY
#import fiona # SY

#shapely.speedups.enable() # SY

#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        ThisYear ThisMonth InitialNumDaysOfMonthToProcess
#ArgNum   1        2         3

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

#SourceFilePath = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/ESI/DailyInfoTiffs/'
#SourceFilePath = './DailyInfoTiffs/'
SourceFilePath = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/OriginalData/ESI/'

ClimGrid1DShpFile = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/nClimGrid_as_poly_NoNans.shp'

ThisYear = int(round(float(sys.argv[1])))
ThisMonth = int(round(float(sys.argv[2])))
InitialNumDaysOfMonthToProcess = int(round(float(sys.argv[3]))) # if -ve number like -9999, then processes all days of the month

cmd = 'mkdir -p /discover/nobackup/projects/nca/syatheen/ESI_Npzs/TempCreatedFiles/'
os.system(cmd)

ArrayFileName = '/discover/nobackup/projects/nca/syatheen/ESI_Npzs/'+format(ThisYear,'04')+format(ThisMonth,'02')+'_ClimGrid1D.npz'

xres=0.125000000000/3
yres=0.125000000000/3
resample_alg = 'near'
Width = 1385
Height = 596
output_bounds = [-124 - 17*xres, 24 + 13*yres, -67, 49 + 9*yres]

#######END ANY EDITS REQUIRED#########

#BEGIN GETTING PxlRowCol ETC SHAPEFILE DATA
ClimGrid1DShp = gpd.read_file(ClimGrid1DShpFile)
PxlRowCol_SortedList_FrmShpFile = sorted(ClimGrid1DShp.PxlRowCol.values.tolist())
PxlRowCol_SortedArr_FrmShpFile = np.array(PxlRowCol_SortedList_FrmShpFile)
PxlRow_SortedArr_FrmShpFile = (np.around(PxlRowCol_SortedArr_FrmShpFile // 10000)).astype(int)
PxlCol_SortedArr_FrmShpFile = (np.around(PxlRowCol_SortedArr_FrmShpFile % 10000)).astype(int)
#END GETTING PxlRowCol ETC SHAPEFILE DATA

if InitialNumDaysOfMonthToProcess <= 0:
    days_in_month = monthrange(ThisYear, ThisMonth)[1] 
else:
    days_in_month = InitialNumDaysOfMonthToProcess

BeginDateVecList = [ ThisYear, ThisMonth, 1, 0, 0, 0]

BeginDate = date(BeginDateVecList[0], BeginDateVecList[1], BeginDateVecList[2])

YYYYMMDD_Of_RefArrayForPrcntl = np.empty((days_in_month,1), dtype=np.int32)
YYYYMMDD_Of_RefArrayForPrcntl[:] = -9999
RefArrayForPrcntl = np.empty((days_in_month,len(PxlRowCol_SortedList_FrmShpFile)))
RefArrayForPrcntl[:] = np.NaN

for WhichDayFromStart in range(days_in_month):

    IntermediateDate = BeginDate + timedelta(days=WhichDayFromStart)
  
    ThisDoM = IntermediateDate.day
  
    YYYYMMDD_Of_RefArrayForPrcntl[WhichDayFromStart] = 10000*ThisYear + 100*ThisMonth + ThisDoM
    
    FileNames_ESI=glob.glob(SourceFilePath+format(ThisYear,'04')+format(ThisMonth,'02')+format(ThisDoM,'02')+'.tif')
    
    if (len(FileNames_ESI) == 1):
      FileName_ESI = FileNames_ESI[0]
    
      IfTifFileExists = os.path.exists(FileName_ESI)
      if IfTifFileExists:

          BaseFileName = format(ThisYear,'04') + format(ThisMonth,'02') + format(ThisDoM,'02') 

          outfn = '/discover/nobackup/projects/nca/syatheen/ESI_Npzs/TempCreatedFiles/' + BaseFileName + '_upsampTo_nCG.tif'

          try:
              os.remove('/discover/nobackup/projects/nca/syatheen/ESI_Npzs/TempCreatedFiles/{}_upsampTo_nCG.tif'.format(BaseFileName))
          except OSError:
              pass

          ds = gdal.Warp(outfn, FileName_ESI, options = gdal.WarpOptions(resampleAlg=resample_alg, width=Width, height=Height, outputBounds=output_bounds, dstNodata = np.NaN))
          ds = None

          with rasterio.Env():

              with rasterio.open('/discover/nobackup/projects/nca/syatheen/ESI_Npzs/TempCreatedFiles/{}_upsampTo_nCG.tif'.format(BaseFileName)) as SrcInfo:
        
                  ImageInfo = SrcInfo.read()
          
                  ImageInfo = np.flip(ImageInfo, axis = 1)
          
                  RefArrayForPrcntl[WhichDayFromStart, :] = ImageInfo[0, PxlRow_SortedArr_FrmShpFile, PxlCol_SortedArr_FrmShpFile]
        
              #end of with rasterio.open(..

          #with rasterio.Env()

      #end of if IfTifFileExists

      try:
          os.remove('/discover/nobackup/projects/nca/syatheen/ESI_Npzs/TempCreatedFiles/{}_upsampTo_nCG.tif'.format(BaseFileName))
      except OSError:
          pass
    
    #end of if (len(FileNames_ESI) == 1)

#end of for WhichDayFromStart in range(days_in_month)

print("YYYYMMDD_Of_RefArrayForPrcntl.shape is ",YYYYMMDD_Of_RefArrayForPrcntl.shape)
print("YYYYMMDD_Of_RefArrayForPrcntl is ",YYYYMMDD_Of_RefArrayForPrcntl)
print("RefArrayForPrcntl.shape is ",RefArrayForPrcntl.shape)
print("RefArrayForPrcntl is ",RefArrayForPrcntl)
print("np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)))
print("np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)))
print('overall min is ',np.nanmin(RefArrayForPrcntl),', overall max is ',np.nanmax(RefArrayForPrcntl))

np.savez_compressed(ArrayFileName, YYYYMMDD_Of_RefPrcntlArray = YYYYMMDD_Of_RefArrayForPrcntl, RefPrcntlArray = RefArrayForPrcntl)

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")


