#!/usr/bin/env python
from __future__ import division
import numpy as np
import os
import rasterio
import geopandas as gpd
from datetime import datetime, timedelta, date
import sys
from osgeo import gdal
import glob
import shapely.speedups
import fiona

shapely.speedups.enable()

#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        BaseFileName 
#ArgNum   1            

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

SourceFilePath = '/discover/nobackup/projects/nca/syatheen/BlendedVHP_RenamedTifs/'

ClimGrid1DShpFile = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/nClimGrid_as_poly_NoNans.shp'

BaseFileName = sys.argv[1]

ThisYear = int(round(float(BaseFileName[13:17])))
ThisWeek = int(round(float(BaseFileName[17:20])))

RefDateVecList = [ ThisYear-1, 12, 31, 0, 0, 0]

RefDate = date(RefDateVecList[0], RefDateVecList[1], RefDateVecList[2])
ThisDate = RefDate + timedelta(days=ThisWeek*7)
ThisMonth = ThisDate.month
ThisDayOfMonth = ThisDate.day

ArrayFileName = '/discover/nobackup/projects/nca/syatheen/BlendedVHP_Npzs/' + BaseFileName[-6:] + '_' + format(ThisYear,'04')+format(ThisMonth,'02')+format(ThisDayOfMonth,'02') + '_ClimGrid1D.npz'

xres=0.125000000000/3
yres=0.125000000000/3
resample_alg = 'near'
Width = 1385
Height = 596
output_bounds = [-124 - 17*xres, 24 + 13*yres, -67, 49 + 9*yres]

BlendedVHP_LowerLimit = -9998

#######END ANY EDITS REQUIRED#########

#BEGIN GETTING PxlRowCol SHAPEFILE DATA
ClimGrid1DShp = gpd.read_file(ClimGrid1DShpFile)
PxlRowCol_SortedList_FrmShpFile = sorted(ClimGrid1DShp.PxlRowCol.values.tolist())
PxlRowCol_SortedArr_FrmShpFile = np.array(PxlRowCol_SortedList_FrmShpFile)
PxlRow_SortedArr_FrmShpFile = (np.around(PxlRowCol_SortedArr_FrmShpFile // 10000)).astype(int)
PxlCol_SortedArr_FrmShpFile = (np.around(PxlRowCol_SortedArr_FrmShpFile % 10000)).astype(int)
#END GETTING PxlRowCol SHAPEFILE DATA

YYYYMMDD_Of_InfoArrayForPrcntl = np.empty((1, 1), dtype=np.int32)
YYYYMMDD_Of_InfoArrayForPrcntl[:] = -9999
InfoArrayForPrcntl = np.empty(( 1, len(PxlRowCol_SortedList_FrmShpFile) ))
InfoArrayForPrcntl[:] = np.NaN

YYYYMMDD_Of_InfoArrayForPrcntl[0] = 10000*ThisYear + 100*ThisMonth + ThisDayOfMonth

BaseFileNameWithPath = SourceFilePath + BaseFileName 

IfTifFileExists = os.path.exists('{}.tif'.format(BaseFileNameWithPath))
if IfTifFileExists:

  cmd = 'mkdir -p /discover/nobackup/projects/nca/syatheen/BlendedVHP_RenamedTifs/TempCreatedFiles'
  os.system(cmd)

  FileName_SNODAS = '{}.tif'.format(BaseFileNameWithPath)

  outfn = '/discover/nobackup/projects/nca/syatheen/SNODAS/TempCreatedFiles/' + BaseFileName + '_downsampTo_nCG.tif'

  try:
    os.remove(outfn)
  except OSError:
    pass

  ds = gdal.Warp(outfn, FileName_SNODAS, options = gdal.WarpOptions(resampleAlg=resample_alg, width=Width, height=Height, outputBounds=output_bounds, dstNodata = np.NaN))
  ds = None

  with rasterio.Env():
    with rasterio.open(outfn) as SrcInfo:

      ImageInfo = SrcInfo.read()

      ImageInfo = np.flip(ImageInfo, axis = 1)

      InfoArrayForPrcntl[0, :] = ImageInfo[0, PxlRow_SortedArr_FrmShpFile, PxlCol_SortedArr_FrmShpFile]

    #end of with rasterio.open(..
  #end of with rasterio.Env()

  try:
    os.remove(outfn)
  except OSError:
    pass

#end of if IfTifFileExists

WhichIdxs = np.where( ~np.isnan(InfoArrayForPrcntl) &
                      ( InfoArrayForPrcntl < BlendedVHP_LowerLimit ) )  
InfoArrayForPrcntl[WhichIdxs] = np.NaN

print("YYYYMMDD_Of_InfoArrayForPrcntl.shape is ",YYYYMMDD_Of_InfoArrayForPrcntl.shape)
print("YYYYMMDD_Of_InfoArrayForPrcntl is ",YYYYMMDD_Of_InfoArrayForPrcntl)
print("InfoArrayForPrcntl.shape is ",InfoArrayForPrcntl.shape)
print("InfoArrayForPrcntl is ",InfoArrayForPrcntl)
print("np.amin(np.isnan(InfoArrayForPrcntl).sum(axis=0)) is ",np.amin(np.isnan(InfoArrayForPrcntl).sum(axis=0)))
print("np.amax(np.isnan(InfoArrayForPrcntl).sum(axis=0)) is ",np.amax(np.isnan(InfoArrayForPrcntl).sum(axis=0)))
print("np.amin(np.isnan(InfoArrayForPrcntl).sum(axis=1)) is ",np.amin(np.isnan(InfoArrayForPrcntl).sum(axis=1)))
print("np.amax(np.isnan(InfoArrayForPrcntl).sum(axis=1)) is ",np.amax(np.isnan(InfoArrayForPrcntl).sum(axis=1)))
print('overall min is ',np.nanmin(InfoArrayForPrcntl),', overall max is ',np.nanmax(InfoArrayForPrcntl))

np.savez_compressed(ArrayFileName, 
                    YYYYMMDD_Of_InfoArrayForPrcntl = YYYYMMDD_Of_InfoArrayForPrcntl, 
                    InfoArrayForPrcntl = InfoArrayForPrcntl)

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")


