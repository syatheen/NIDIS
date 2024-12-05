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

#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        WhichVar ArgYear
#ArgNum   1        2

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

SourceFilePath = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/GRACE/'
ClimDivShpFile = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS.shp'
#ClimDivShpFile = '/discover/nobackup/syatheen/NIDIS/Data/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS.shp'
mask = None
LowerLimit = 0.0
UpperLimit =  100.0
WhichVar = sys.argv[1] # choices are gws_inst, rtzsm_inst and sfsm_inst
ArgYear = int(round(float(sys.argv[2]))) 
ArrayFileName = 'RefPctlArrsWeekly/'+sys.argv[2]+'_'+WhichVar+'.npz'

#######END ANY EDITS REQUIRED#########

#BEGIN GETTING CLIMDIV SHAPEFILE DATA
ClimDivShp = gpd.read_file(ClimDivShpFile)
CLIMDIV_SortedList_FrmShpFile = sorted(ClimDivShp.CLIMDIV.values.tolist())
#END GETTING CLIMDIV SHAPEFILE DATA

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
RefArrayForPrcntl = np.empty((NumWeeks,len(CLIMDIV_SortedList_FrmShpFile)))
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
      with rasterio.Env():
        with rasterio.open(FileName_GRACE) as SrcInfo:
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
                                       (Intrsct.raster_val >= LowerLimit) &
                                       (Intrsct.raster_val <= UpperLimit) &
                                       (Intrsct.geometry.area > 0) ]
            if len(Sel_Intrsct.index) > 0:
              RefArrayForPrcntl[WhichWeek, iClimDiv] = (Sel_Intrsct.raster_val*Sel_Intrsct.geometry.area).sum()/Sel_Intrsct.geometry.area.sum()
          #end of for iClimDiv in range(len(CLIMDIV_SortedList_FrmShpFile))
        #with rasterio.open(FileName_GRACE) as SrcInfo
      #with rasterio.Env()
    #end of if IfTifFileExists

  #end of if (len(FileNames_GRACE) == 1)

#end of for WhichWeek in range(NumWeeks)

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


