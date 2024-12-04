import numpy as np
#######BEGIN ANY EDITS REQUIRED#######
BeginDateVec = [2008, 2, 5] # Beginning year, month, day of month
EndDateVec = [2020, 1, 6] # Ending year, month, day of month, this is 6 days after 2019-end, and is a Monday FYI 
SourceFilePath = '/att/nobackup/dmocko/CPCsoilmoisture/total/'
#SourceFilePath = '/discover/nobackup/syatheen/NIDIS/Testing/CPCsoilmoisture/total/'
ClimDivShpFile = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS.shp'
#ClimDivShpFile = '/discover/nobackup/syatheen/NIDIS/Data/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS.shp'
mask = None
LowerLimit = 0.0
UpperLimit =  np.NaN
ArrayFileName = 'RefArrDaily_'+format(BeginDateVec[0],'04')+format(BeginDateVec[1],'02')+format(BeginDateVec[2],'02')+'To'+format(EndDateVec[0],'04')+format(EndDateVec[1],'02')+format(EndDateVec[2],'02')+'.npz'
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
start_time = time.time()

BeginDate = date(BeginDateVec[0],BeginDateVec[1], BeginDateVec[2])
EndDate = date(EndDateVec[0],EndDateVec[1], EndDateVec[2])
if BeginDate > EndDate:
  print('BeginDate should not be later than EndDate!!!')
  sys.exit(0)

#BEGIN GETTING CLIMDIV SHAPEFILE DATA
ClimDivShp = gpd.read_file(ClimDivShpFile)
CLIMDIV_SortedList_FrmShpFile = sorted(ClimDivShp.CLIMDIV.values.tolist())
#END GETTING CLIMDIV SHAPEFILE DATA

def GetSrcInfoFromZipOrTifFile(SomeDateVec, SourceFilePath):

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
      SrcInfo = None
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
        with rasterio.Env():
          with rasterio.open(TifFileName) as SrcInfo:
            ImageInfo = SrcInfo.read()
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
        SrcInfo = None
        ImageInfo = None
      # end of if ( (FileName_root+'.dbf' in ZipObject.namelist()) etc
    #end of if IfIncompleteFile:

  elif IfTifFileExists:

    IfFileSetExists = True
    with rasterio.Env():
      with rasterio.open(SourceTifFileName) as SrcInfo:
        ImageInfo = SrcInfo.read()

  else: # if IfZipFileExists

    IfFileSetExists = False
    SrcInfo = None
    ImageInfo = None

  return IfFileSetExists, SrcInfo, ImageInfo
#end of def GetSrcInfoFromZipOrTifFile(SomeDateVec, SourceFilePath):

TotalNumDaysDiff = abs(EndDate-BeginDate).days # Calcultting the number of days elapsed from the beginning date vector to the ending one
print('TotalNumDaysDiff is ', TotalNumDaysDiff)
YYYYMMDD_Of_RefArrayForPrcntl = np.empty((TotalNumDaysDiff+1,1), dtype=np.int32)
YYYYMMDD_Of_RefArrayForPrcntl[:] = np.NaN
RefArrayForPrcntl = np.empty((TotalNumDaysDiff+1,len(CLIMDIV_SortedList_FrmShpFile)))
RefArrayForPrcntl[:] = np.NaN
for NumDaysDiff in range(0,TotalNumDaysDiff+1):

  IntermediateDate = BeginDate + timedelta(days=NumDaysDiff)
  YYYYMMDD_Of_RefArrayForPrcntl[NumDaysDiff] = 10000*IntermediateDate.year + 100*IntermediateDate.month + IntermediateDate.day
  IfFileSetExists, SrcInfo, ImageInfo = GetSrcInfoFromZipOrTifFile([IntermediateDate.year, IntermediateDate.month, IntermediateDate.day], SourceFilePath)

  if IfFileSetExists:
    results = ( {'properties': {'raster_val': vv}, 'geometry': ss}
               for ii, (ss, vv) in enumerate( shapes(ImageInfo, mask = mask,
                                                     transform = SrcInfo.transform)))
    geoms = list(results)
    gpd_polygonized_raster  = gpd.GeoDataFrame.from_features(geoms)
    gpd_polygonized_raster.crs = SrcInfo.crs

    Intrsct = gpd.overlay(df1 = gpd_polygonized_raster, df2 = ClimDivShp)

    for iClimDiv in range(len(CLIMDIV_SortedList_FrmShpFile)):

      Sel_Intrsct = Intrsct.loc[ (Intrsct.CLIMDIV == CLIMDIV_SortedList_FrmShpFile[iClimDiv]) &
                                 ( ~(Intrsct.geometry.is_empty | Intrsct.geometry.isna()) ) &
                                 ( ~(Intrsct.raster_val.isnull()) ) &
                                 (Intrsct.raster_val > LowerLimit) &
                                 (Intrsct.geometry.area > 0) ]
      if len(Sel_Intrsct.index) > 0:
        RefArrayForPrcntl[NumDaysDiff, iClimDiv] = (Sel_Intrsct.raster_val*Sel_Intrsct.geometry.area).sum()/Sel_Intrsct.geometry.area.sum()
    #end of for iClimDiv in range(len(CLIMDIV_SortedList_FrmShpFile)):
  #end of if IfFileSetExists:
#end of for NumDaysDiff in range(0,TotalNumDaysDiff+1):

print("YYYYMMDD_Of_RefArrayForPrcntl.shape is ",YYYYMMDD_Of_RefArrayForPrcntl.shape)
print("YYYYMMDD_Of_RefArrayForPrcntl is ",YYYYMMDD_Of_RefArrayForPrcntl)
print("RefArrayForPrcntl.shape is ",RefArrayForPrcntl.shape)
print("RefArrayForPrcntl is ",RefArrayForPrcntl)
print("np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)))
print("np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)))
print('overall min is ',np.nanmin(RefArrayForPrcntl),', overall max is ',np.nanmax(RefArrayForPrcntl))

print("--- %s seconds ---" % (time.time() - start_time))

np.savez_compressed(ArrayFileName, YYYYMMDD_Of_RefArrayForPrcntl = YYYYMMDD_Of_RefArrayForPrcntl, RefArrayForPrcntl = RefArrayForPrcntl)



