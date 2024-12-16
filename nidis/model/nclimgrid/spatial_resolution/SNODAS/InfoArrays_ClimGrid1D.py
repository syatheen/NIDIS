#!/usr/bin/env python
from __future__ import division
import numpy as np
import sys
import os
import rasterio
import geopandas as gpd
from datetime import datetime, timedelta
import glob
from osgeo import gdal
import shapely.speedups
import fiona

shapely.speedups.enable()

#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        ThisYear ThisMonth ThisDayOfMonth 
#ArgNum   1        2         3              

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

SourceFilePath = '/discover/nobackup/projects/nca/syatheen/SNODAS/'

ClimGrid1DShpFile = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/nClimGrid_as_poly_NoNans.shp'

SNODAS1DShpFile = r'/discover/nobackup/projects/nca/syatheen/SNODAS_Shapefile/snodas20031030_points_w_nClimGridRowCol.shp' 

ThisYear = int(round(float(sys.argv[1])))
ThisMonth = int(round(float(sys.argv[2])))
ThisDayOfMonth = int(round(float(sys.argv[3]))) 

ArrayFileName = '/discover/nobackup/projects/nca/syatheen/SNODAS_Npzs/New/SNODAS_' + format(ThisYear, '04') + format(ThisMonth, '02') + format(ThisDayOfMonth, '02') + '_ClimGrid1D.npz'

SNODAS_LowerLimit = 0.0
SNODAS_UpperLimit = 32000.0 # To discard 32767.0 values

#######END ANY EDITS REQUIRED#########

#BEGIN GETTING PxlRowCol SHAPEFILE DATA
ClimGrid1DShp = gpd.read_file(ClimGrid1DShpFile)
PxlRowCol_SortedList_FrmShpFile = sorted(ClimGrid1DShp.PxlRowCol.values.tolist())
PxlRowCol_SortedArr_FrmShpFile = np.array(PxlRowCol_SortedList_FrmShpFile)
del ClimGrid1DShp
#END GETTING PxlRowCol SHAPEFILE DATA

#BEGIN GETTING PxlRowCol ETC SHAPEFILE DATA of VegDRI
SNODAS1DShp = gpd.read_file(SNODAS1DShpFile)
SnodasPxlRowCol_Arr_FrmSNODASShpFile = SNODAS1DShp.grid_code.values
SnodasPxlRow_Arr_FrmSNODASShpFile = (np.around(SnodasPxlRowCol_Arr_FrmSNODASShpFile // 10000)).astype(int)
SnodasPxlCol_Arr_FrmSNODASShpFile = (np.around(SnodasPxlRowCol_Arr_FrmSNODASShpFile % 10000)).astype(int)
del SnodasPxlRowCol_Arr_FrmSNODASShpFile
nClimGridPxlRowCol_Arr_FrmSNODASShpFile = SNODAS1DShp.PxlRowCol.values
del SNODAS1DShp
#END GETTING PxlRowCol ETC SHAPEFILE DATA of VegDRI

YYYYMMDD_Of_InfoArrayForPrcntl = np.empty((1, 1), dtype=np.int32)
YYYYMMDD_Of_InfoArrayForPrcntl[:] = -9999
InfoArrayForPrcntl = np.empty(( 1, len(PxlRowCol_SortedList_FrmShpFile) ))
InfoArrayForPrcntl[:] = np.nan

del PxlRowCol_SortedList_FrmShpFile

YYYYMMDD_Of_InfoArrayForPrcntl[0] = 10000*ThisYear + 100*ThisMonth + ThisDayOfMonth

BaseFileNameWithPath = SourceFilePath + 'SNODAS' + format(ThisYear, '04') + format(ThisMonth, '02') + format(ThisDayOfMonth, '02')

IfTifFileExists = os.path.exists('{}.tif'.format(BaseFileNameWithPath))
if IfTifFileExists:

  FileName_SNODAS = '{}.tif'.format(BaseFileNameWithPath)

  with rasterio.Env():
    with rasterio.open(FileName_SNODAS) as SrcInfo:

      ImageInfo = SrcInfo.read()

      SNODAS1DArrInt = ImageInfo[0, SnodasPxlRow_Arr_FrmSNODASShpFile, SnodasPxlCol_Arr_FrmSNODASShpFile]
      SNODAS1DArr = SNODAS1DArrInt.astype(np.float32)
      del ImageInfo
      del SNODAS1DArrInt

      for WhichNClimGridRowCol in range(PxlRowCol_SortedArr_FrmShpFile.size):

        Idxs = np.where( (nClimGridPxlRowCol_Arr_FrmSNODASShpFile == PxlRowCol_SortedArr_FrmShpFile[WhichNClimGridRowCol] ) & ~np.isnan(SNODAS1DArr) & ( SNODAS1DArr >= SNODAS_LowerLimit ) & (SNODAS1DArr <= SNODAS_UpperLimit) )[0]


        if Idxs.size:
          InfoArrayForPrcntl[0, WhichNClimGridRowCol] = np.nanmean(SNODAS1DArr[Idxs]) 
        #ende of if Idxs.size

        del Idxs

      #end of for WhichNClimGridRowCol in range(PxlRowCol_SortedArr_FrmShpFile.size)

      del SNODAS1DArr

    #end of with rasterio.open(..
  #end of with rasterio.Env()
 
  del SrcInfo

#end of if IfTifFileExists

del PxlRowCol_SortedArr_FrmShpFile
del SnodasPxlRow_Arr_FrmSNODASShpFile
del SnodasPxlCol_Arr_FrmSNODASShpFile
del nClimGridPxlRowCol_Arr_FrmSNODASShpFile

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


