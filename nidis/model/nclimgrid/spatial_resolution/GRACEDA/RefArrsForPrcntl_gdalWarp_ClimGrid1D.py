#!/usr/bin/env python
from __future__ import division
import numpy as np
import sys
import os
import rasterio
from rasterio.features import shapes
import geopandas as gpd
from datetime import datetime, timedelta
import glob
import time
from osgeo import gdal
import shapely.speedups
import fiona

shapely.speedups.enable()

#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        WhichVar ArgYear
#ArgNum   1        2

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

SourceFilePath = '/discover/nobackup/projects/nca/syatheen/GRACE/'
ClimGrid1DShpFile = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/nClimGrid_as_poly_NoNans.shp'
#LowerLimit = 0.0
#UpperLimit =  100.0
WhichVar = sys.argv[1] # choices are gws_inst, rtzsm_inst and sfsm_inst
ArgYear = int(round(float(sys.argv[2]))) 
ArrayFileName = 'RefPctlArrsWeekly/'+sys.argv[2]+'_'+WhichVar+'_ClimGrid1D.npz'

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

if ArgYear == 2002: 
  BeginDateVecList = [ 2002, 4, 1, 0, 0, 0]
elif ArgYear == 2003: 
  BeginDateVecList = [ 2003, 1, 6, 0, 0, 0]
elif ArgYear == 2004: 
  BeginDateVecList = [ 2004, 1, 5, 0, 0, 0]
elif ArgYear == 2005: 
  BeginDateVecList = [ 2005, 1, 3, 0, 0, 0]
elif ArgYear == 2006: 
  BeginDateVecList = [ 2006, 1, 2, 0, 0, 0]
elif ArgYear == 2007: 
  BeginDateVecList = [ 2007, 1, 1, 0, 0, 0]
elif ArgYear == 2008: 
  BeginDateVecList = [ 2008, 1, 7, 0, 0, 0]
elif ArgYear == 2009: 
  BeginDateVecList = [ 2009, 1, 5, 0, 0, 0]
elif ArgYear == 2010: 
  BeginDateVecList = [ 2010, 1, 4, 0, 0, 0]
elif ArgYear == 2011: 
  BeginDateVecList = [ 2011, 1, 3, 0, 0, 0]
elif ArgYear == 2012: 
  BeginDateVecList = [ 2012, 1, 2, 0, 0, 0]
elif ArgYear == 2013: 
  BeginDateVecList = [ 2013, 1, 7, 0, 0, 0]
elif ArgYear == 2014: 
  BeginDateVecList = [ 2014, 1, 6, 0, 0, 0]
elif ArgYear == 2015: 
  BeginDateVecList = [ 2015, 1, 5, 0, 0, 0]
elif ArgYear == 2016: 
  BeginDateVecList = [ 2016, 1, 4, 0, 0, 0]
elif ArgYear == 2017: 
  BeginDateVecList = [ 2017, 1, 2, 0, 0, 0]
elif ArgYear == 2018: 
  BeginDateVecList = [ 2018, 1, 1, 0, 0, 0]
elif ArgYear == 2019: 
  BeginDateVecList = [ 2019, 1, 7, 0, 0, 0]
elif ArgYear == 2020: 
  BeginDateVecList = [ 2020, 1, 6, 0, 0, 0]
else:
  sys.exit("Invalid ArgYear Choice!!!")

if ArgYear == 2002: 
  EndDateVecList = [ 2002, 12, 30, 0, 0, 0]
elif ArgYear == 2003: 
  EndDateVecList = [ 2003, 12, 29, 0, 0, 0]
elif ArgYear == 2004: 
  EndDateVecList = [ 2004, 12, 27, 0, 0, 0]
elif ArgYear == 2005: 
  EndDateVecList = [ 2005, 12, 26, 0, 0, 0]
elif ArgYear == 2006: 
  EndDateVecList = [ 2006, 12, 25, 0, 0, 0]
elif ArgYear == 2007: 
  EndDateVecList = [ 2007, 12, 31, 0, 0, 0]
elif ArgYear == 2008: 
  EndDateVecList = [ 2008, 12, 29, 0, 0, 0]
elif ArgYear == 2009: 
  EndDateVecList = [ 2009, 12, 28, 0, 0, 0]
elif ArgYear == 2010: 
  EndDateVecList = [ 2010, 12, 27, 0, 0, 0]
elif ArgYear == 2011: 
  EndDateVecList = [ 2011, 12, 26, 0, 0, 0]
elif ArgYear == 2012: 
  EndDateVecList = [ 2012, 12, 31, 0, 0, 0]
elif ArgYear == 2013: 
  EndDateVecList = [ 2013, 12, 30, 0, 0, 0]
elif ArgYear == 2014: 
  EndDateVecList = [ 2014, 12, 29, 0, 0, 0]
elif ArgYear == 2015: 
  EndDateVecList = [ 2015, 12, 28, 0, 0, 0]
elif ArgYear == 2016: 
  EndDateVecList = [ 2016, 12, 26, 0, 0, 0]
elif ArgYear == 2017: 
  EndDateVecList = [ 2017, 12, 25, 0, 0, 0]
elif ArgYear == 2018: 
  EndDateVecList = [ 2018, 12, 31, 0, 0, 0]
elif ArgYear == 2019: 
  EndDateVecList = [ 2019, 12, 30, 0, 0, 0]
elif ArgYear == 2020: 
  EndDateVecList = [ 2020, 10, 26, 0, 0, 0]
else:
  sys.exit("Invalid ArgYear Choice!!!")

BeginDateTime = datetime(BeginDateVecList[0], BeginDateVecList[1], BeginDateVecList[2], BeginDateVecList[3], BeginDateVecList[4], BeginDateVecList[5])
EndDateTime = datetime(EndDateVecList[0], EndDateVecList[1], EndDateVecList[2], EndDateVecList[3], EndDateVecList[4], EndDateVecList[5])
DiffTimee = EndDateTime - BeginDateTime
NumWeeks = int(round(DiffTimee.total_seconds()/(3600*24*7)) + 1)
print('NumWeeks = ',NumWeeks)

YYYYMMDD_Of_RefArrayForPrcntl = np.empty((NumWeeks,1), dtype=np.int32)
YYYYMMDD_Of_RefArrayForPrcntl[:] = np.NaN
RefArrayForPrcntl = np.empty((NumWeeks,len(PxlRowCol_SortedList_FrmShpFile)))
RefArrayForPrcntl[:] = np.NaN

for WhichWeek in range(NumWeeks):

  ThisDateTime = BeginDateTime + timedelta(days=(WhichWeek*7))
  ThisYear = ThisDateTime.year
  ThisMonth = ThisDateTime.month
  ThisDoM = ThisDateTime.day
  YYYYMMDD_Of_RefArrayForPrcntl[WhichWeek] = 10000*ThisYear + 100*ThisMonth + ThisDoM

  FileNames_GRACE=glob.glob(SourceFilePath+'TifFiles/v040/'+WhichVar+'/GRACEDADM_CLSM0125US_7D.A'+format(ThisYear,'04')+format(ThisMonth,'02')+format(ThisDoM,'02')+'.040.tif')

  if (len(FileNames_GRACE) == 1):
    FileName_GRACE = FileNames_GRACE[0]

    IfTifFileExists = os.path.exists(FileName_GRACE)
    if IfTifFileExists:

      BaseFileName = WhichVar + format(ThisYear,'04') + format(ThisMonth,'02') + format(ThisDoM,'02')
  
      outfn = SourceFilePath + 'TempCreatedFiles/' + BaseFileName + '_upsampTo_nCG.tif' 
  
      try:
          os.remove(SourceFilePath + 'TempCreatedFiles/{}_upsampTo_nCG.tif'.format(BaseFileName))
      except OSError:
          pass
  
      ds = gdal.Warp(outfn, FileName_GRACE, options = gdal.WarpOptions(resampleAlg=resample_alg, width=Width, height=Height, outputBounds=output_bounds, dstNodata = np.NaN))
      ds = None
  
      with rasterio.Env():
        with rasterio.open(SourceFilePath + 'TempCreatedFiles/{}_upsampTo_nCG.tif'.format(BaseFileName)) as SrcInfo:
  
          ImageInfo = SrcInfo.read()
  
          ImageInfo = np.flip(ImageInfo, axis = 1)
  
          RefArrayForPrcntl[WhichWeek, :] = ImageInfo[0, PxlRow_SortedArr_FrmShpFile, PxlCol_SortedArr_FrmShpFile]
  
        #end of with rasterio.open(..
      #end of with rasterio.Env()

    #end of if IfTifFileExists

  #end of if (len(FileNames_GRACE) == 1)

#end of for WhichWeek in range(NumWeeks)

print("YYYYMMDD_Of_RefArrayForPrcntl.shape is ",YYYYMMDD_Of_RefArrayForPrcntl.shape)
print("YYYYMMDD_Of_RefArrayForPrcntl is ",YYYYMMDD_Of_RefArrayForPrcntl)
print("RefArrayForPrcntl.shape is ",RefArrayForPrcntl.shape)
print("RefArrayForPrcntl is ",RefArrayForPrcntl)
print("np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)))
print("np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)))
print("np.amin(np.isnan(RefArrayForPrcntl).sum(axis=1)) is ",np.amin(np.isnan(RefArrayForPrcntl).sum(axis=1)))
print("np.amax(np.isnan(RefArrayForPrcntl).sum(axis=1)) is ",np.amax(np.isnan(RefArrayForPrcntl).sum(axis=1)))
print('overall min is ',np.nanmin(RefArrayForPrcntl),', overall max is ',np.nanmax(RefArrayForPrcntl))

np.savez_compressed(ArrayFileName, 
                    YYYYMMDD_Of_RefArrayForPrcntl = YYYYMMDD_Of_RefArrayForPrcntl, 
                    RefArrayForPrcntl = RefArrayForPrcntl)

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")


