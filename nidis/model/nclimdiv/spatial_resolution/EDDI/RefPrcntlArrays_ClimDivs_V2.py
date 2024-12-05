from __future__ import division
import numpy as np
import sys
import os
import rasterio
from rasterio.features import shapes
import geopandas as gpd
from datetime import datetime, timedelta, date
import glob
import time

#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        ArgYear WhichAggregation
#ArgNum   1       2 

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

#ClimDivShpFile = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS.shp'
ClimDivShpFile = '/discover/nobackup/syatheen/NIDIS/Data/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS.shp'
crs = rasterio.crs.CRS({"init": "EPSG:4326"})
mask = None
LowerLimit = -9998
ArgYear = int(round(float(sys.argv[1]))) 
WhichAggregation = sys.argv[2] # 01wk, 02wk etc
ArrayFileName = 'RefPctlArrsDaily/'+sys.argv[1]+'_'+sys.argv[2]+'.npz'
#SourceFilePath = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/EDDI/'+WhichAggregation+'/'
SourceFilePath = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/EDDI/'+WhichAggregation+'/'

#######END ANY EDITS REQUIRED#########

#BEGIN GETTING CLIMDIV SHAPEFILE DATA
ClimDivShp = gpd.read_file(ClimDivShpFile)
CLIMDIV_SortedList_FrmShpFile = sorted(ClimDivShp.CLIMDIV.values.tolist())
#END GETTING CLIMDIV SHAPEFILE DATA

#if ( (ArgYear >= 1980) and (ArgYear <= 2020) ): 
#  BeginDateVecList = [ ArgYear, 1, 1, 0, 0, 0]
#else:
#  sys.exit("Invalid ArgYear Choice based on BeginDateVecList!!!")
#
#if ( (ArgYear >= 1980) and (ArgYear <= 2019) ): 
#  EndDateVecList = [ ArgYear, 12, 31, 0, 0, 0]
#elif ArgYear == 2020: 
#  EndDateVecList = [ ArgYear, 8, 26, 0, 0, 0]
#else:
#  sys.exit("Invalid ArgYear Choice based on EndDateVecList!!!")

BeginDateVecList = [ ArgYear, 1, 1, 0, 0, 0]
EndDateVecList = [ ArgYear, 12, 31, 0, 0, 0]

BeginDate = date(BeginDateVecList[0], BeginDateVecList[1], BeginDateVecList[2])
EndDate = date(EndDateVecList[0], EndDateVecList[1], EndDateVecList[2])
if BeginDate > EndDate:
  print('BeginDate should not be later than EndDate!!!')
  sys.exit(0)

TotalNumDaysDiff = abs(EndDate-BeginDate).days # Calcultting the number of days elapsed from the beginning date vector to the ending one
print('TotalNumDaysDiff is ', TotalNumDaysDiff)

YYYYMMDD_Of_RefArrayForPrcntl = np.empty((TotalNumDaysDiff+1,1), dtype=np.int32)
YYYYMMDD_Of_RefArrayForPrcntl[:] = np.NaN
RefArrayForPrcntl = np.empty((TotalNumDaysDiff+1,len(CLIMDIV_SortedList_FrmShpFile)))
RefArrayForPrcntl[:] = np.NaN

for NumDaysDiff in range(0,TotalNumDaysDiff+1):

  IntermediateDate = BeginDate + timedelta(days=NumDaysDiff)

  ThisYear = IntermediateDate.year
  ThisMonth = IntermediateDate.month
  ThisDoM = IntermediateDate.day

  YYYYMMDD_Of_RefArrayForPrcntl[NumDaysDiff] = 10000*ThisYear + 100*ThisMonth + ThisDoM

#  FileNames_EDDI=glob.glob(SourceFilePath+format(ThisYear,'04')+'/EDDI_ETrs_01wk_'+format(ThisYear,'04')+format(ThisMonth,'02')+format(ThisDoM,'02')+'.asc')
  FileNames_EDDI=glob.glob(SourceFilePath+format(ThisYear,'04')+'/EDDI_ETrs_'+WhichAggregation+'_'+format(ThisYear,'04')+format(ThisMonth,'02')+format(ThisDoM,'02')+'.asc')

  if (len(FileNames_EDDI) == 1):
    FileName_EDDI = FileNames_EDDI[0]

    IfAscFileExists = os.path.exists(FileName_EDDI)
    if IfAscFileExists:
      with rasterio.Env():
        with rasterio.open(FileName_EDDI, mode='r+') as SrcInfo:
          SrcInfo.crs = crs
          ImageInfo = SrcInfo.read()
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
          #end of for iClimDiv in range(len(CLIMDIV_SortedList_FrmShpFile))
        #with rasterio.open(FileName_EDDI) as SrcInfo
      #with rasterio.Env()
    #end of if IfAscFileExists

  #end of if (len(FileNames_EDDI) == 1)

#end of for NumDaysDiff in range(0,TotalNumDaysDiff+1):

print("YYYYMMDD_Of_RefArrayForPrcntl.shape is ",YYYYMMDD_Of_RefArrayForPrcntl.shape)
print("YYYYMMDD_Of_RefArrayForPrcntl is ",YYYYMMDD_Of_RefArrayForPrcntl)
print("RefArrayForPrcntl.shape is ",RefArrayForPrcntl.shape)
print("RefArrayForPrcntl is ",RefArrayForPrcntl)
print("np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)))
print("np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)))
print('overall min is ',np.nanmin(RefArrayForPrcntl),', overall max is ',np.nanmax(RefArrayForPrcntl))

np.savez_compressed(ArrayFileName, YYYYMMDD_Of_RefArrayForPrcntl = YYYYMMDD_Of_RefArrayForPrcntl, RefArrayForPrcntl = RefArrayForPrcntl)

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")


