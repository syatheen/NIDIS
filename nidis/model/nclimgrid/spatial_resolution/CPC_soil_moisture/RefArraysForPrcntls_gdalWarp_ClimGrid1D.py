#!/usr/bin/env python

import numpy as np

#######BEGIN ANY EDITS REQUIRED#######

BeginDateVec = [2008, 2, 5] # Beginning year, month, day of month
#EndDateVec = [2008, 2, 10] # Ending year, month, day of month
EndDateVec = [2020, 1, 6] # Ending year, month, day of month, this is 6 days after 2019-end, and is a Monday FYI 
SourceFilePath = '/discover/nobackup/syatheen/NIDIS/Testing/CPCsoilmoisture/total/'
ClimGrid1DShpFile = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/nClimGrid_as_poly_NoNans.shp'

LowerLimit = 0.0
UpperLimit =  np.NaN

ArrayFileName = '/discover/nobackup/projects/nca/syatheen/CPCsoilmoisture_Npzs/RefArrDaily_'+format(BeginDateVec[0],'04')+format(BeginDateVec[1],'02')+format(BeginDateVec[2],'02')+'To'+format(EndDateVec[0],'04')+format(EndDateVec[1],'02')+format(EndDateVec[2],'02')+'_ClimGrid1D.npz'

#######END ANY EDITS REQUIRED#########

import sys
import os
import rasterio
from rasterio.features import shapes
import geopandas as gpd
if sys.version_info >= (3, 6):
  import zipfile
else:
  import zipfile36 as zipfile
from datetime import date, timedelta
import time
from osgeo import gdal
import shapely.speedups
import fiona
import rioxarray
import xarray as xr

start_time = time.time()

BeginDate = date(BeginDateVec[0],BeginDateVec[1], BeginDateVec[2])
EndDate = date(EndDateVec[0],EndDateVec[1], EndDateVec[2])
if BeginDate > EndDate:
  print('BeginDate should not be later than EndDate!!!')
  sys.exit(0)

xres=0.125000000000/3
yres=0.125000000000/3
resample_alg = 'near'
Width = 1385
Height = 596
output_bounds = [-124 - 17*xres, 24 + 13*yres, -67, 49 + 9*yres]

#BEGIN GETTING PxlRowCol ETC SHAPEFILE DATA
ClimGrid1DShp = gpd.read_file(ClimGrid1DShpFile)
PxlRowCol_SortedList_FrmShpFile = sorted(ClimGrid1DShp.PxlRowCol.values.tolist())
PxlRowCol_SortedArr_FrmShpFile = np.array(PxlRowCol_SortedList_FrmShpFile)
PxlRow_SortedArr_FrmShpFile = (np.around(PxlRowCol_SortedArr_FrmShpFile // 10000)).astype(int)
PxlCol_SortedArr_FrmShpFile = (np.around(PxlRowCol_SortedArr_FrmShpFile % 10000)).astype(int)
#END GETTING PxlRowCol ETC SHAPEFILE DATA

def GetSrcInfoFromZipOrTifFile_GdalWarp(SomeDateVec, SourceFilePath):

  Len_SomeDateVec = len(SomeDateVec)
  if Len_SomeDateVec == 2: # monthly
    FileName_root = 'w.full.'+format(SomeDateVec[0],'04')+format(SomeDateVec[1],'02')
  elif Len_SomeDateVec == 3: # daily
    FileName_root = 'w.full.'+format(SomeDateVec[0],'04')+format(SomeDateVec[1],'02')+format(SomeDateVec[2],'02')
  ZipFileName = FileName_root+'.zip'
  TifFileName = FileName_root+'.tif'
  if Len_SomeDateVec == 2: # monthly
    SourceZipFileName = SourceFilePath+'monthly/'+ZipFileName
    SourceTifFileName = SourceFilePath+'monthly/'+TifFileName
  elif Len_SomeDateVec == 3: # daily
    SourceZipFileName = SourceFilePath+'daily/'+ZipFileName
    SourceTifFileName = SourceFilePath+'daily/'+TifFileName

  PreOutFileName = SourceFilePath + 'TempFiles/' + FileName_root + '.tif'   
  OutFileName = SourceFilePath + 'TempFiles/upsampTo_nCG_' + FileName_root + '.tif'   

  IfZipFileExists = os.path.exists(SourceZipFileName)
  IfTifFileExists = os.path.exists(SourceTifFileName)

  if IfZipFileExists:

    IfIncompleteFile = False
    if Len_SomeDateVec == 3: # daily
      if ( (SomeDateVec[0] == 2008) and
           (SomeDateVec[1] == 12) and
           (SomeDateVec[2] == 25) ):
        IfIncompleteFile = True

    if IfIncompleteFile:
      IfFileSetExists = False
      ImageInfo = None
    else:
      returned_value = os.system('cp '+SourceZipFileName+' '+ZipFileName)
      if returned_value != 0:
        if Len_SomeDateVec == 2: # monthly
          print('Zip file could not be copied properly for '+SomeDateVec[0]+'/'+SomeDateVec[1]+'!!!')
        elif Len_SomeDateVec == 3: # daily
          print('Zip file could not be copied properly for '+SomeDateVec[0]+'/'+SomeDateVec[1]+'/'+SomeDateVec[2]+'!!!')
        sys.exit(0)
      NestedZipLevel = 0
      ZipObject = zipfile.ZipFile(open(ZipFileName, 'rb'))
      while ( ( not ( (FileName_root+'.dbf' in ZipObject.namelist()) and
                      (FileName_root+'.prj' in ZipObject.namelist()) and
                      (FileName_root+'.shp' in ZipObject.namelist()) and
                      (FileName_root+'.shx' in ZipObject.namelist()) and
                      (TifFileName in ZipObject.namelist()) ) ) and
              (ZipFileName in ZipObject.namelist()) ):
        NestedZipLevel = NestedZipLevel + 1
        bb = ZipObject.extractall(FileName_root)
        returned_value = os.system('mv '+FileName_root+'/'+ZipFileName+' '+ZipFileName)
        if returned_value != 0:
          if Len_SomeDateVec == 2: # monthly
            print('Zip file from nested level '+NestedZipLevel+' could not be moved properly for '+SomeDateVec[0]+'/'+SomeDateVec[1]+'!!!')
          elif Len_SomeDateVec == 3: # daily
            print('Zip file from nested level '+NestedZipLevel+' could not be moved properly for '+SomeDateVec[0]+'/'+SomeDateVec[1]+'/'+SomeDateVec[2]+'!!!')
          sys.exit(0)
        returned_value = os.system('rm -rf '+FileName_root)
        if returned_value != 0:
          if Len_SomeDateVec == 2: # monthly
            print('Unzipped dir that contained zip of nested level '+NestedZipLevel+' could not be removed properly for '+SomeDateVec[0]+'/'+SomeDateVec[1]+'!!!')
          elif Len_SomeDateVec == 3: # daily
            print('Unzipped dir that contained zip of nested level '+NestedZipLevel+' could not be removed properly for '+SomeDateVec[0]+'/'+SomeDateVec[1]+'/'+SomeDateVec[2]+'!!!')
          sys.exit(0)
        ZipObject = zipfile.ZipFile(open(ZipFileName, 'rb'))
      #end of "while ( ( not ( (FileName_root+'.dbf' in ZipObject.namelist())... etc"
      if ( (FileName_root+'.dbf' in ZipObject.namelist()) and
           (FileName_root+'.prj' in ZipObject.namelist()) and
           (FileName_root+'.shp' in ZipObject.namelist()) and
           (FileName_root+'.shx' in ZipObject.namelist()) and
           (TifFileName in ZipObject.namelist()) ) :
        bb = ZipObject.extractall(FileName_root)
        IfFileSetExists = True
        TifFileName = FileName_root+'/'+FileName_root+'.tif'
        image_Array = xr.open_rasterio(TifFileName)
        image_ArrayValues = image_Array.values
        image_ArrayValues[np.where( image_ArrayValues < LowerLimit )] = np.NaN
        outImage_Array = xr.where(
          xr.ufuncs.isnan(image_Array) |
          (~xr.ufuncs.isnan(image_Array)),
          image_ArrayValues, image_ArrayValues)
        outImage_Array = outImage_Array.assign_attrs(nodatavals = image_Array.attrs['nodatavals'],
                                                     transform = image_Array.attrs['transform'],
                                                     crs = image_Array.attrs['crs'],
                                                     res = image_Array.attrs['res'],
                                                     is_tiled = image_Array.attrs['is_tiled'])
        outImage_Array.rio.to_raster(PreOutFileName)
        del outImage_Array, image_ArrayValues, image_Array 
        try:
          os.remove(OutFileName)
        except OSError:
          pass
        ds = gdal.Warp(OutFileName, PreOutFileName, options = gdal.WarpOptions(resampleAlg=resample_alg, width=Width, height=Height, outputBounds=output_bounds, dstNodata = np.NaN))
        ds = None
        try:
          os.remove(PreOutFileName)
        except OSError:
          pass
        with rasterio.Env():
          with rasterio.open(OutFileName) as SrcInfo:
            ImageInfo = SrcInfo.read()
            ImageInfo = np.flip(ImageInfo, axis = 1)
        try:
          os.remove(OutFileName)
        except OSError:
          pass
        returned_value = os.system('rm -rf '+FileName_root)
        if returned_value != 0:
          if Len_SomeDateVec == 2: # monthly
            print('Unzipped dir could not be removed properly for '+SomeDateVec[0]+'/'+SomeDateVec[1]+'!!!')
          elif Len_SomeDateVec == 3: # daily
            print('Unzipped dir could not be removed properly for '+SomeDateVec[0]+'/'+SomeDateVec[1]+'/'+SomeDateVec[2]+'!!!')
          sys.exit(0)
        #end of if returned_value != 0:
        returned_value = os.system('rm -rf '+ZipFileName)
        if returned_value != 0:
          if Len_SomeDateVec == 2: # monthly
            print('Zip file could not be removed properly for '+SomeDateVec[0]+'/'+SomeDateVec[1]+'!!!')
          elif Len_SomeDateVec == 3: # daily
            print('Zip file could not be removed properly for '+SomeDateVec[0]+'/'+SomeDateVec[1]+'/'+SomeDateVec[2]+'!!!')
          sys.exit(0)
        #end of if returned_value != 0:
      else: # if ( (FileName_root+'.dbf' in ZipObject.namelist()) etc...
        IfFileSetExists = False
        ImageInfo = None
      # end of if ( (FileName_root+'.dbf' in ZipObject.namelist()) etc
    #end of if IfIncompleteFile:

  elif IfTifFileExists:

    IfFileSetExists = True
    image_Array = xr.open_rasterio(SourceTifFileName)
    image_ArrayValues = image_Array.values
    image_ArrayValues[np.where( image_ArrayValues < LowerLimit )] = np.NaN
    outImage_Array = xr.where(
      xr.ufuncs.isnan(image_Array) |
      (~xr.ufuncs.isnan(image_Array)),
      image_ArrayValues, image_ArrayValues)
    outImage_Array = outImage_Array.assign_attrs(nodatavals = image_Array.attrs['nodatavals'],
                                                 transform = image_Array.attrs['transform'],
                                                 crs = image_Array.attrs['crs'],
                                                 res = image_Array.attrs['res'],
                                                 is_tiled = image_Array.attrs['is_tiled'])
    outImage_Array.rio.to_raster(PreOutFileName)
    del outImage_Array, image_ArrayValues, image_Array 
    try:
      os.remove(OutFileName)
    except OSError:
      pass
    ds = gdal.Warp(OutFileName, PreOutFileName, options = gdal.WarpOptions(resampleAlg=resample_alg, width=Width, height=Height, outputBounds=output_bounds, dstNodata = np.NaN))
    ds = None
    try:
      os.remove(PreOutFileName)
    except OSError:
      pass
    with rasterio.Env():
      with rasterio.open(OutFileName) as SrcInfo:
        ImageInfo = SrcInfo.read()
        ImageInfo = np.flip(ImageInfo, axis = 1)
    try:
      os.remove(OutFileName)
    except OSError:
      pass

  else: # if IfZipFileExists

    IfFileSetExists = False
    ImageInfo = None

  return IfFileSetExists, ImageInfo
#end of def GetSrcInfoFromZipOrTifFile_GdalWarp(SomeDateVec, SourceFilePath):

TotalNumDaysDiff = abs(EndDate-BeginDate).days # Calculating the number of days elapsed from the beginning date vector to the ending one
print('TotalNumDaysDiff is ', TotalNumDaysDiff)
YYYYMMDD_Of_RefArrayForPrcntl = np.empty((TotalNumDaysDiff+1,1), dtype=np.int32)
YYYYMMDD_Of_RefArrayForPrcntl[:] = -9999
RefArrayForPrcntl = np.empty((TotalNumDaysDiff+1,len(PxlRowCol_SortedList_FrmShpFile)))
RefArrayForPrcntl[:] = np.NaN

for NumDaysDiff in range(0,TotalNumDaysDiff+1):

  IntermediateDate = BeginDate + timedelta(days=NumDaysDiff)
  YYYYMMDD_Of_RefArrayForPrcntl[NumDaysDiff] = 10000*IntermediateDate.year + 100*IntermediateDate.month + IntermediateDate.day
  IfFileSetExists, ImageInfo = GetSrcInfoFromZipOrTifFile_GdalWarp([IntermediateDate.year, IntermediateDate.month, IntermediateDate.day], SourceFilePath)

  if IfFileSetExists:
    RefArrayForPrcntl[NumDaysDiff, :] = ImageInfo[0, PxlRow_SortedArr_FrmShpFile, PxlCol_SortedArr_FrmShpFile]
  #end of if IfFileSetExists:

#end of for NumDaysDiff in range(0,TotalNumDaysDiff+1):

print("YYYYMMDD_Of_RefArrayForPrcntl.shape is ",YYYYMMDD_Of_RefArrayForPrcntl.shape)
print("YYYYMMDD_Of_RefArrayForPrcntl is ",YYYYMMDD_Of_RefArrayForPrcntl)
print("RefArrayForPrcntl.shape is ",RefArrayForPrcntl.shape)
print("RefArrayForPrcntl is ",RefArrayForPrcntl)
print("np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)))
print("np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)))
print("np.amin(np.isnan(RefArrayForPrcntl).sum(axis=1)) is ",np.amin(np.isnan(RefArrayForPrcntl).sum(axis=1)))
print("np.amax(np.isnan(RefArrayForPrcntl).sum(axis=1)) is ",np.amax(np.isnan(RefArrayForPrcntl).sum(axis=1)))
print('overall min is ',np.nanmin(RefArrayForPrcntl),', overall max is ',np.nanmax(RefArrayForPrcntl))

print("--- %s seconds ---" % (time.time() - start_time))

np.savez_compressed(ArrayFileName, 
                    YYYYMMDD_Of_RefArrayForPrcntl = YYYYMMDD_Of_RefArrayForPrcntl, 
                    RefArrayForPrcntl = RefArrayForPrcntl)



