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

#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        ThisYear ThisMonth InitialNumDaysOfMonthToProcess
#ArgNum   1        2         3

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

#SourceFilePath = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/ESI/DailyInfoTiffs/'
SourceFilePath = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/OriginalData/ESI/'

#ClimDivShpFile = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS.shp'
# ClimDivShpFile = '/discover/nobackup/syatheen/NIDIS/Data/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS.shp'
ClimGrid1DShpFile = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/nClimGrid_as_poly_NoNans.shp'

mask = None

ArgYearInt = int(round(float(sys.argv[1])))
ArgMonthInt = int(round(float(sys.argv[2])))
InitialNumDaysOfMonthToProcess = int(round(float(sys.argv[3]))) # if -ve number like -9999, then processes all days of the month

ArrayFileName = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/Indicators_70_to_71/spatial_resolution/InfoArrsDaily/'+format(ThisYear,'04')+format(ThisMonth,'02')+'.npz'

NLDAS_2_daily_LowerLimit = 0.
NLDAS_2_daily_ZerosLowerLimit = 50.49504470825193 # 50.495044708251945
#                                50.49504470825195312500 in Python
NLDAS_2_daily_ZerosUpperLimit = 50.49504470825198 # 50.49504470825197
NLDAS_2_daily_UpperLimit = 100.

xres = 0.125000000000/3
yres = 0.125000000000/3
resample_alg = 'near'
Width = 1385
Height = 596
output_bounds = [-124 - 17*xres, 24 + 13*yres, -67, 49 + 9*yres]

#######END ANY EDITS REQUIRED#########

#BEGIN GETTING CLIMDIV SHAPEFILE DATA
#ClimDivShp = gpd.read_file(ClimDivShpFile)
#CLIMDIV_SortedList_FrmShpFile = sorted(ClimDivShp.CLIMDIV.values.tolist())

ClimGrid1DShp = gpd.read_file(ClimGrid1DShpFile)
PxlRowCol_SortedList_FrmShpFile = sorted(ClimGrid1DShp.PxlRowCol.values.tolist())
PxlRowCol_SortedArr_FrmShpFile = np.array(PxlRowCol_SortedList_FrmShpFile)
PxlRow_SortedArr_FrmShpFile = (np.around(PxlRowCol_SortedArr_FrmShpFile // 10000)).astype(int)
PxlCol_SortedArr_FrmShpFile = (np.around(PxlRowCol_SortedArr_FrmShpFile % 10000)).astype(int)

#END GETTING CLIMDIV SHAPEFILE DATA

NumDaysInMonth = int(round(float(monthrange(ArgYearInt, ArgMonthInt)[1]))) 

YYYYMMDD_Of_RefArrayForPrcntl = np.empty((NumDaysInMonth, 1), dtype=np.int32)
YYYYMMDD_Of_RefArrayForPrcntl[:] = -9999
RefArrayForPrcntl = np.empty((NumDaysInMonth, len(PxlRowCol_SortedList_FrmShpFile)))
RefArrayForPrcntl[:] = np.NaN

#if InitialNumDaysOfMonthToProcess <= 0:
#  days_in_month = monthrange(ThisYear, ThisMonth)[1] 
#else:
#  days_in_month = InitialNumDaysOfMonthToProcess

BeginDateVecList = [ ArgYearInt, ArgMonthInt, 1, 0, 0, 0]

BeginDate = date(BeginDateVecList[0], BeginDateVecList[1], BeginDateVecList[2])

#YYYYMMDD_Of_RefArrayForPrcntl = np.empty((days_in_month,1), dtype=np.int32)
#YYYYMMDD_Of_RefArrayForPrcntl[:] = -9999
#RefArrayForPrcntl = np.empty((days_in_month,len(CLIMDIV_SortedList_FrmShpFile)))
#RefArrayForPrcntl[:] = np.NaN

for WhichDayFromStart in range(1, NumDaysInMonth+1):

  IntermediateDate = BeginDate + timedelta(days=WhichDayFromStart)

  ThisDoM = IntermediateDate.day

  YYYYMMDD_Of_RefArrayForPrcntl[WhichDayFromStart] = 10000*ArgYearInt + 100*ArgMonthInt + ThisDoM
  
  FileNames_ESI=glob.glob(SourceFilePath+format(ArgYearInt,'04')+format(ArgMonthInt,'02')+format(ThisDoM,'02')+'.tif')
  
  if (len(FileNames_ESI) == 1):
    FileName_ESI = FileNames_ESI[0]
  
    IfTifFileExists = os.path.exists(FileName_ESI)
    if IfTifFileExists:
      with rasterio.Env():
        with rasterio.open(FileName_ESI) as SrcInfo:
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
                                       ~np.isnan( Intrsct.raster_val ) &
                                       (Intrsct.geometry.area > 0) ]
            if len(Sel_Intrsct.index) > 0:
              RefArrayForPrcntl[WhichDayFromStart, iClimDiv] = (Sel_Intrsct.raster_val*Sel_Intrsct.geometry.area).sum()/Sel_Intrsct.geometry.area.sum()
  
          #end of for iClimDiv in range(len(CLIMDIV_SortedList_FrmShpFile))
        #with rasterio.open(FileName_ESI) as SrcInfo
      #with rasterio.Env()
    #end of if IfTifFileExists
  
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


