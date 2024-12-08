#!/usr/bin/env python
from __future__ import division
from osgeo import gdal, gdalconst
import os
import pandas as pd
from shapely.geometry import Polygon
import geopandas as gpd
from datetime import datetime, timedelta, date
import shapely.speedups
import numpy as np
import fiona
import rasterio
import rioxarray
import xarray as xr
import sys
import glob

shapely.speedups.enable()

#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        ThisYear ThisMonth ThisDoM
#ArgNum   1        2         3

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

ClimGrid1DShpFile = r'/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/nClimGrid_as_poly_NoNans.shp'

VegDRI1DShpFile = r'/discover/nobackup/projects/nca/syatheen/VegDRI_Shapefile/vegdri_poly_w_nClimGridRowCol.shp'

ThisYear = int(round(float(sys.argv[1])))
ThisMonth = int(round(float(sys.argv[2])))
ThisDoM = int(round(float(sys.argv[3])))
#
ArrayFileName = r'RefArrsWeekly/' + format(ThisYear,'04') + format(ThisMonth,'02') + format(ThisDoM,'02') + r'_ClimGrid1D.npz'

VegDRI_LowerLimit = 1
VegDRI_UpperLimit = 252

SourceFilePath = r'/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/VegDRI/'

#######END ANY EDITS REQUIRED#########

#BEGIN GETTING PxlRowCol ETC SHAPEFILE DATA of nClimGrid
ClimGrid1DShp = gpd.read_file(ClimGrid1DShpFile)
PxlRowCol_SortedList_FrmShpFile = sorted(ClimGrid1DShp.PxlRowCol.values.tolist())
PxlRowCol_SortedArr_FrmShpFile = np.array(PxlRowCol_SortedList_FrmShpFile)
del ClimGrid1DShp
#END GETTING PxlRowCol ETC SHAPEFILE DATA of nClimGrid

#BEGIN GETTING PxlRowCol ETC SHAPEFILE DATA of VegDRI
VegDRI1DShp = gpd.read_file(VegDRI1DShpFile)
VegDriPxlRowCol_Arr_FrmVegDRIShpFile = VegDRI1DShp.gridcode.values
VegDriPxlRow_Arr_FrmVegDRIShpFile = (np.around(VegDriPxlRowCol_Arr_FrmVegDRIShpFile // 10000)).astype(int)
VegDriPxlCol_Arr_FrmVegDRIShpFile = (np.around(VegDriPxlRowCol_Arr_FrmVegDRIShpFile % 10000)).astype(int)
del VegDriPxlRowCol_Arr_FrmVegDRIShpFile
nClimGridPxlRowCol_Arr_FrmVegDRIShpFile = VegDRI1DShp.PxlRowCol.values
del VegDRI1DShp
#END GETTING PxlRowCol ETC SHAPEFILE DATA of VegDRI

YYYYMMDD_Of_RefArrayForPrcntl = np.empty((1,1), dtype=np.int32)
YYYYMMDD_Of_RefArrayForPrcntl[:] = -9999
#RefArrayForPrcntl = np.empty((1,len(PxlRowCol_SortedList_FrmShpFile)))
RefArrayForPrcntl = np.empty((1,len(PxlRowCol_SortedList_FrmShpFile)), dtype=np.float32)
RefArrayForPrcntl[:] = np.NaN

del PxlRowCol_SortedList_FrmShpFile

YYYYMMDD_Of_RefArrayForPrcntl[0] = 10000*ThisYear + 100*ThisMonth + ThisDoM

FileNames_VegDRI=glob.glob(SourceFilePath + r'Data/' + format(ThisYear,'04') + r'/vegdri_emodis_week' + date(ThisYear, ThisMonth, ThisDoM).strftime("%U").lstrip('0') + r'_' + format(ThisMonth,'02') + format(ThisDoM,'02') + format(ThisYear%100,'02') + r'.tif')

if (len(FileNames_VegDRI) == 1):

  FileName_VegDRI = FileNames_VegDRI[0]

  IfTifFileExists = os.path.exists(FileName_VegDRI)
  if IfTifFileExists:

    with rasterio.Env():
      with rasterio.open(FileName_VegDRI) as SrcInfo:

          ImageInfo = SrcInfo.read()
  
          VegDRI1DArrInt = ImageInfo[0, VegDriPxlRow_Arr_FrmVegDRIShpFile, VegDriPxlCol_Arr_FrmVegDRIShpFile]
          VegDRI1DArr = VegDRI1DArrInt.astype(np.float32)
          del ImageInfo
          del VegDRI1DArrInt
 
          for WhichNClimGridRowCol in range(PxlRowCol_SortedArr_FrmShpFile.size):
  
            Idxs = np.where( (nClimGridPxlRowCol_Arr_FrmVegDRIShpFile == PxlRowCol_SortedArr_FrmShpFile[WhichNClimGridRowCol] ) & ~np.isnan(VegDRI1DArr) & ( VegDRI1DArr >= VegDRI_LowerLimit ) & (VegDRI1DArr <= VegDRI_UpperLimit) )[0] 


            if Idxs.size: 
              RefArrayForPrcntl[0, WhichNClimGridRowCol] = np.nanmean(VegDRI1DArr[Idxs])  
            #ende of if Idxs.size

            del Idxs

 
          #end of for WhichNClimGridRowCol in range(PxlRowCol_SortedArr_FrmShpFile.shape)

          del VegDRI1DArr

      #end of with rasterio.open(..
    #end of with rasterio.Env()

    del SrcInfo

  #end of if IfTifFileExists

#end of if (len(FileNames_VegDRI) == 1)

del PxlRowCol_SortedArr_FrmShpFile
del VegDriPxlRow_Arr_FrmVegDRIShpFile
del VegDriPxlCol_Arr_FrmVegDRIShpFile
del nClimGridPxlRowCol_Arr_FrmVegDRIShpFile

print("YYYYMMDD_Of_RefArrayForPrcntl.shape is ",YYYYMMDD_Of_RefArrayForPrcntl.shape)
print("YYYYMMDD_Of_RefArrayForPrcntl is ",YYYYMMDD_Of_RefArrayForPrcntl)
print("RefArrayForPrcntl.shape is ",RefArrayForPrcntl.shape)
print("RefArrayForPrcntl is ",RefArrayForPrcntl)
print("np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)))
print("np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)))
print("np.amin(np.isnan(RefArrayForPrcntl).sum(axis=1)) is ",np.amin(np.isnan(RefArrayForPrcntl).sum(axis=1)))
print("np.amax(np.isnan(RefArrayForPrcntl).sum(axis=1)) is ",np.amax(np.isnan(RefArrayForPrcntl).sum(axis=1)))
print('overall min is ',np.nanmin(RefArrayForPrcntl),', overall max is ',np.nanmax(RefArrayForPrcntl))

#np.savez_compressed(ArrayFileName, 
np.savez(ArrayFileName, 
                    YYYYMMDD_Of_RefArrayForPrcntl = YYYYMMDD_Of_RefArrayForPrcntl, 
                    RefArrayForPrcntl = RefArrayForPrcntl)

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")

