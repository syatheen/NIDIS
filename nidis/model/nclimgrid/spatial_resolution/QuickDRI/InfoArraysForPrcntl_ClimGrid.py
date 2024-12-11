#!/usr/bin/env python
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
import fiona
import rasterio

shapely.speedups.enable()

#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        ThisYear ThisWeek
#ArgNum   1        2     

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

ClimGrid1DShpFile = r'/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/nClimGrid_as_poly_NoNans.shp'

ThisYear = int(round(float(sys.argv[1])))
ThisWeek = int(round(float(sys.argv[2])))

if ThisYear < 2013:
  QuickDRI1DShpFile = r'/discover/nobackup/projects/nca/syatheen/QuickDRI_Shapefiles/qdri_poly_2000wk03_w_nClimGridRowCol.shp'  
elif ThisYear < 2014:
  QuickDRI1DShpFile = r'/discover/nobackup/projects/nca/syatheen/QuickDRI_Shapefiles/qdri_poly_2013wk01_w_nClimGridRowCol.shp'  
elif ThisYear < 2016:
  QuickDRI1DShpFile = r'/discover/nobackup/projects/nca/syatheen/QuickDRI_Shapefiles/qdri_poly_2014wk01_w_nClimGridRowCol.shp'  
elif ThisYear < 2017:
  QuickDRI1DShpFile = r'/discover/nobackup/projects/nca/syatheen/QuickDRI_Shapefiles/qdri_poly_2016wk01_w_nClimGridRowCol.shp'  
else:  # ThisYear >= 2017
  QuickDRI1DShpFile = r'/discover/nobackup/projects/nca/syatheen/VegDRI_Shapefile/vegdri_poly_w_nClimGridRowCol.shp'  #  Note that this is same as VegDRI shapefile for this period
#end of if ThisYear < 2013

RefDateVecList = [ ThisYear-1, 12, 31, 0, 0, 0]

RefDate = date(RefDateVecList[0], RefDateVecList[1], RefDateVecList[2])
ThisDate = RefDate + timedelta(days=ThisWeek*7)
ThisMonth = ThisDate.month
ThisDoM = ThisDate.day

ArrayFileName = 'InfoArrsWeekly/'+format(ThisYear,'04')+format(ThisMonth,'02')+format(ThisDoM,'02')+'_ClimGrid1D.npz'

QuickDRI_LowerLimit = -200
QuickDRI_UpperLimit = 200

SourceFilePath = r'/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/QuickDRI/'

#######END ANY EDITS REQUIRED#########

#BEGIN GETTING PxlRowCol ETC SHAPEFILE DATA of nClimGrid
ClimGrid1DShp = gpd.read_file(ClimGrid1DShpFile)
PxlRowCol_SortedList_FrmShpFile = sorted(ClimGrid1DShp.PxlRowCol.values.tolist())
PxlRowCol_SortedArr_FrmShpFile = np.array(PxlRowCol_SortedList_FrmShpFile)
del ClimGrid1DShp
#END GETTING PxlRowCol ETC SHAPEFILE DATA of nClimGrid

#BEGIN GETTING PxlRowCol ETC SHAPEFILE DATA of QuickDRI
QuickDRI1DShp = gpd.read_file(QuickDRI1DShpFile)
QuickDriPxlRowCol_Arr_FrmQuickDRIShpFile = QuickDRI1DShp.gridcode.values
QuickDriPxlRow_Arr_FrmQuickDRIShpFile = (np.around(QuickDriPxlRowCol_Arr_FrmQuickDRIShpFile // 10000)).astype(int)
QuickDriPxlCol_Arr_FrmQuickDRIShpFile = (np.around(QuickDriPxlRowCol_Arr_FrmQuickDRIShpFile % 10000)).astype(int)
del QuickDriPxlRowCol_Arr_FrmQuickDRIShpFile
nClimGridPxlRowCol_Arr_FrmQuickDRIShpFile = QuickDRI1DShp.PxlRowCol.values
del QuickDRI1DShp
#END GETTING PxlRowCol ETC SHAPEFILE DATA of QuickDRI

YYYYMMDD_Of_RefArrayForPrcntl = np.empty((1,1), dtype=np.int32)
YYYYMMDD_Of_RefArrayForPrcntl[:] = -9999
RefArrayForPrcntl = np.empty((1,len(PxlRowCol_SortedList_FrmShpFile)), dtype=np.float32)
RefArrayForPrcntl[:] = np.NaN

del PxlRowCol_SortedList_FrmShpFile

YYYYMMDD_Of_RefArrayForPrcntl[0] = 10000*ThisYear + 100*ThisMonth + ThisDoM

FileNames_QuickDRI=glob.glob(SourceFilePath + r'Data/qdri_'+format(ThisYear,'04')+'wk'+format(ThisWeek,'02')+'.tif')

if (len(FileNames_QuickDRI) == 1) and not ( (ThisYear == 2014) and (ThisWeek == 14) ):

  FileName_QuickDRI = FileNames_QuickDRI[0]
  
  IfTifFileExists = os.path.exists(FileName_QuickDRI)
  if IfTifFileExists:

    with rasterio.Env():
      with rasterio.open(FileName_QuickDRI) as SrcInfo:

          ImageInfo = SrcInfo.read()

          QuickDRI1DArrInt = ImageInfo[0, QuickDriPxlRow_Arr_FrmQuickDRIShpFile, QuickDriPxlCol_Arr_FrmQuickDRIShpFile]
          QuickDRI1DArr = QuickDRI1DArrInt.astype(np.float32)
          del ImageInfo
          del QuickDRI1DArrInt

          for WhichNClimGridRowCol in range(PxlRowCol_SortedArr_FrmShpFile.size):

            Idxs = np.where( (nClimGridPxlRowCol_Arr_FrmQuickDRIShpFile == PxlRowCol_SortedArr_FrmShpFile[WhichNClimGridRowCol] ) & ~np.isnan(QuickDRI1DArr) & ( QuickDRI1DArr >= QuickDRI_LowerLimit ) & (QuickDRI1DArr <= QuickDRI_UpperLimit) )[0]

            if Idxs.size:
              RefArrayForPrcntl[0, WhichNClimGridRowCol] = np.nanmean(QuickDRI1DArr[Idxs])
            #end of if Idxs.size

            del Idxs

          #end of for WhichNClimGridRowCol in range(PxlRowCol_SortedArr_FrmShpFile.shape)

          del QuickDRI1DArr

      #end of with rasterio.open(..
    #end of with rasterio.Env()

    del SrcInfo

  #end of if IfTifFileExists

#end of if (len(FileNames_QuickDRI) == 1) and (ThisYear != 2014) and (ThisWeek != 14)

del PxlRowCol_SortedArr_FrmShpFile
del QuickDriPxlRow_Arr_FrmQuickDRIShpFile
del QuickDriPxlCol_Arr_FrmQuickDRIShpFile
del nClimGridPxlRowCol_Arr_FrmQuickDRIShpFile

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


