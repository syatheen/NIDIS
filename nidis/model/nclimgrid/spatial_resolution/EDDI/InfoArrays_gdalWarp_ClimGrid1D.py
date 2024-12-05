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
import rasterio
from rasterio.features import shapes
import fiona

shapely.speedups.enable()

#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        BeginYear BeginMonth BeginDoM EndYear EndMonth EndDoM WhichAggregation
#ArgNum   1         2          3        4       5        6      7

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

ClimGrid1DShpFile = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/nClimGrid_as_poly_NoNans.shp'

LowerLimit = -9998

BeginYear = int(round(float(sys.argv[1])))
BeginMonth = int(round(float(sys.argv[2])))
BeginDoM = int(round(float(sys.argv[3])))
EndYear = int(round(float(sys.argv[4])))
EndMonth = int(round(float(sys.argv[5])))
EndDoM = int(round(float(sys.argv[6])))
WhichAggregation = sys.argv[7]
SourceFilePath = '/discover/nobackup/projects/nca/syatheen/EDDI/'
ArrayFileName = '/discover/nobackup/projects/nca/syatheen/EDDI_Npzs/' + format(BeginYear,'04') + format(BeginMonth,'02') + format(BeginDoM,'02') + 'To' + format(EndYear,'04') + format(EndMonth,'02') + format(EndDoM,'02') + '_' + WhichAggregation + '.npz'   

xres=0.125000000000/3
yres=0.125000000000/3
resample_alg = 'near'
Width = 1385
Height = 596
output_bounds = [-124 - 17*xres, 24 + 13*yres, -67, 49 + 9*yres]

BeginDateVecList = [ BeginYear, BeginMonth, BeginDoM, 0, 0, 0]
EndDateVecList = [ EndYear, EndMonth, EndDoM, 0, 0, 0]

#######END ANY EDITS REQUIRED#########

#BEGIN GETTING PxlRowCol ETC SHAPEFILE DATA
ClimGrid1DShp = gpd.read_file(ClimGrid1DShpFile)
PxlRowCol_SortedList_FrmShpFile = sorted(ClimGrid1DShp.PxlRowCol.values.tolist())
PxlRowCol_SortedArr_FrmShpFile = np.array(PxlRowCol_SortedList_FrmShpFile)
PxlRow_SortedArr_FrmShpFile = (np.around(PxlRowCol_SortedArr_FrmShpFile // 10000)).astype(int)
PxlCol_SortedArr_FrmShpFile = (np.around(PxlRowCol_SortedArr_FrmShpFile % 10000)).astype(int)
#END GETTING PxlRowCol ETC SHAPEFILE DATA

BeginDate = date(BeginDateVecList[0], BeginDateVecList[1], BeginDateVecList[2])
EndDate = date(EndDateVecList[0], EndDateVecList[1], EndDateVecList[2])
if BeginDate > EndDate:
  print('BeginDate should not be later than EndDate!!!')
  sys.exit(0)

TotalNumDaysDiff = abs(EndDate-BeginDate).days # Calculating the number of days elapsed from the beginning date vector to the ending one
print('TotalNumDaysDiff is ', TotalNumDaysDiff)

YYYYMMDD_Of_RefArrayForPrcntl = np.empty((TotalNumDaysDiff+1,1), dtype=np.int32)
YYYYMMDD_Of_RefArrayForPrcntl[:] = -9999
RefArrayForPrcntl = np.empty((TotalNumDaysDiff+1,len(PxlRowCol_SortedList_FrmShpFile)))
RefArrayForPrcntl[:] = np.NaN

for NumDaysDiff in range(0,TotalNumDaysDiff+1):

  IntermediateDate = BeginDate + timedelta(days=NumDaysDiff)

  ThisYear = IntermediateDate.year
  ThisMonth = IntermediateDate.month
  ThisDoM = IntermediateDate.day

  YYYYMMDD_Of_RefArrayForPrcntl[NumDaysDiff] = 10000*ThisYear + 100*ThisMonth + ThisDoM
  
  FileNames_EDDI=glob.glob(SourceFilePath + WhichAggregation + '/' + format(ThisYear,'04') + '/EDDI_ETrs_' + WhichAggregation + '_' + format(ThisYear,'04') + format(ThisMonth,'02') + format(ThisDoM,'02') + '.asc')
  
  if (len(FileNames_EDDI) == 1):
  
    BaseFileName = 'EDDI_ETrs_' + WhichAggregation + '_' + format(ThisYear,'04') + format(ThisMonth,'02') + format(ThisDoM,'02')

    infn = SourceFilePath  + WhichAggregation + '/' + format(ThisYear,'04') + '/' + BaseFileName + '.asc'
    outfn = SourceFilePath + 'TempCreatedFiles/' + BaseFileName + '_upsampTo_nCG.tif'

    try:
        os.remove('/discover/nobackup/projects/nca/syatheen/EDDI/TempCreatedFiles/{}_upsampTo_nCG.tif'.format(BaseFileName))
    except OSError:
        pass

#    ds = gdal.Warp(outfn, infn, options = gdal.WarpOptions(xRes=xres, yRes=yres, resampleAlg=resample_alg))
#    ds = gdal.Warp(outfn, infn, options = gdal.WarpOptions(resampleAlg=resample_alg, width=Width, height=Height, outputBounds=output_bounds))
    ds = gdal.Warp(outfn, infn, options = gdal.WarpOptions(resampleAlg=resample_alg, width=Width, height=Height, outputBounds=output_bounds, dstNodata = np.NaN))
    ds = None

    IfTifFileExists = os.path.exists('/discover/nobackup/projects/nca/syatheen/EDDI/TempCreatedFiles/{}_upsampTo_nCG.tif'.format(BaseFileName))
    if IfTifFileExists:
      with rasterio.Env():
        with rasterio.open('/discover/nobackup/projects/nca/syatheen/EDDI/TempCreatedFiles/{}_upsampTo_nCG.tif'.format(BaseFileName)) as SrcInfo:
    
          ImageInfo = SrcInfo.read()
   
          ImageInfo = np.flip(ImageInfo, axis = 1)
 
          RefArrayForPrcntl[NumDaysDiff, :] = ImageInfo[0, PxlRow_SortedArr_FrmShpFile, PxlCol_SortedArr_FrmShpFile]
    
          #end of for iPxlRowCol in range(len(PxlRowCol_SortedList_FrmShpFile))
        #with rasterio.open('/discover/nobackup/projects/nca/syatheen/EDDI/TempCreatedFiles/{}_upsampTo_nCG.tif'.format(BaseFileName)) as SrcInfo
      #with rasterio.Env()
    #end of if IfTifFileExists
    
    try:
        os.remove('/discover/nobackup/projects/nca/syatheen/EDDI/TempCreatedFiles/{}_upsampTo_nCG.tif'.format(BaseFileName))
    except OSError:
        pass
  
  #end of if (len(FileNames_EDDI) == 1)

#end of for NumDaysDiff in range(0,TotalNumDaysDiff+1)

Idxs =  np.where(RefArrayForPrcntl <= LowerLimit)
RefArrayForPrcntl[Idxs] = np.nan

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


