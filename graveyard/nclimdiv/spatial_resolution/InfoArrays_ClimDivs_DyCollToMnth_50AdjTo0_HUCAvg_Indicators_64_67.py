from __future__ import division
import numpy as np
import os
import rasterio
from rasterio.features import shapes
import geopandas as gpd
from datetime import datetime, timedelta, date
import sys
import pandas as pd
import glob
import os
from calendar import monthrange

#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        ArgLSM ArgVariable ArgYearInt ArgMonthInt ArgHUC 
#ArgNum   1      2           3          4           5 

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

#ClimDivShpFile = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS_EPSG4326.shp'
ClimDivShpFile = '/discover/nobackup/syatheen/NIDIS/Data/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS_EPSG4326.shp'

mask = None

ArgLSM = sys.argv[1]
ArgVariable = sys.argv[2]

ArgYearInt = int(round(float(sys.argv[3])))
ArgMonthInt = int(round(float(sys.argv[4])))

ArgHUC = sys.argv[5] # Options are H02 (for HUC02), H04 (for HUC04), H06 (for HUC06), H08 (for HUC08)

if ArgHUC == 'H02':
  HUC_FileNameBase = 'test02'
elif ArgHUC == 'H04':
  HUC_FileNameBase = 'test04'
elif ArgHUC == 'H06':
  HUC_FileNameBase = 'test06'
elif ArgHUC == 'H08':
  HUC_FileNameBase = 'test08'

cmd = 'mkdir -p /discover/nobackup/projects/nca/syatheen/NLDAS_2_daily_Npzs/'
os.system(cmd)

ArrayFileName = '/discover/nobackup/projects/nca/syatheen/NLDAS_2_daily_Npzs/' + ArgLSM + '_' + ArgVariable  + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '_' + ArgHUC + '_ClimDivs.PERW.50AdjustTo0.npz'

SourceFileBasePath = '/discover/nobackup/projects/nca/syatheen/'

NLDAS_2_daily_LowerLimit = 0.
NLDAS_2_daily_ZerosLowerLimit = 50.49504470825193 # 50.495044708251945
#                                50.49504470825195312500 in Python
NLDAS_2_daily_ZerosUpperLimit = 50.49504470825198 # 50.49504470825197
NLDAS_2_daily_UpperLimit = 100.

#######END ANY EDITS REQUIRED#########

#BEGIN GETTING CLIMDIV SHAPEFILE DATA
ClimDivShp = gpd.read_file(ClimDivShpFile)
CLIMDIV_SortedList_FrmShpFile = sorted(ClimDivShp.CLIMDIV.values.tolist())
#END GETTING CLIMDIV SHAPEFILE DATA

NumDaysInMonth = int(round(float(monthrange(ArgYearInt, ArgMonthInt)[1]))) 

YYYYMMDD_Of_RefPrcntlArray = np.empty((NumDaysInMonth, 1), dtype=np.int32)
YYYYMMDD_Of_RefPrcntlArray[:] = -9999
RefPrcntlArray = np.empty((NumDaysInMonth, len(CLIMDIV_SortedList_FrmShpFile)))
RefPrcntlArray[:] = np.NaN

IfHUCTifFileExists = os.path.exists(HUC_FileNameBase + '.tif')
for WhichDayInMonth in range(1, NumDaysInMonth+1):

  YYYYMMDD_Of_RefPrcntlArray[WhichDayInMonth-1] = 10000*ArgYearInt + 100*ArgMonthInt + WhichDayInMonth 
  SourceFile = SourceFileBasePath + 'NLDAS_2_daily/' + ArgLSM + '.' + ArgVariable + '.' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + format(WhichDayInMonth,'02') + '.PERW.tif'

  IfTifFileExists = os.path.exists(SourceFile)
  if IfTifFileExists and IfHUCTifFileExists:
    with rasterio.Env():
      with rasterio.open(SourceFile) as SrcInfo:
        with rasterio.open(HUC_FileNameBase + '.tif') as HUCSrcInfo:
          ImageInfo = SrcInfo.read()
          HUCImageInfo = HUCSrcInfo.read()
          Idxs = np.where((ImageInfo >= NLDAS_2_daily_ZerosLowerLimit) & (ImageInfo <= NLDAS_2_daily_ZerosUpperLimit))
          ImageInfo[Idxs] = 0.0 
          HUCImageInfo = np.flip(HUCImageInfo, axis = 1) 
          Idxs = np.where( (HUCImageInfo < 0.) & (~np.isnan(ImageInfo)) )
          ImageInfo[Idxs] = np.NaN

          Uniq_PosHUCs = np.unique(HUCImageInfo[np.where( HUCImageInfo > 0.5)])

          for ThisUniq_PosHUCs in Uniq_PosHUCs:
            Idxs = np.where(HUCImageInfo == ThisUniq_PosHUCs)
            if (np.isnan(np.nanmean(ImageInfo[Idxs]))):
              print(WhichDayInMonth, ' ', ThisUniq_PosHUCs, ' : All NaNs!')
            ImageInfo[Idxs] = np.nanmean(ImageInfo[Idxs])

          ImageInfo = ImageInfo.astype(np.float32) 
           
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
                                       ( Intrsct.raster_val >= NLDAS_2_daily_LowerLimit ) &
                                       ( Intrsct.raster_val <= NLDAS_2_daily_UpperLimit ) &
                                       (Intrsct.geometry.area > 0) ]
            if len(Sel_Intrsct.index) > 0:
              RefPrcntlArray[WhichDayInMonth-1, iClimDiv] = (Sel_Intrsct.raster_val*Sel_Intrsct.geometry.area).sum()/Sel_Intrsct.geometry.area.sum()
    
          #end of for iClimDiv in range(len(CLIMDIV_SortedList_FrmShpFile))
        #end of with rasterio.open(HUC_FileNameBase + '.tif') as HUCSrcInfo
      #end of with rasterio.open(SourceFile) as SrcInfo
    #with rasterio.Env()
  #end of if IfTifFileExists

#end of for WhichDayInMonth in range(1, NumDaysInMonth+1)

print("YYYYMMDD_Of_RefPrcntlArray.shape is ",YYYYMMDD_Of_RefPrcntlArray.shape)
print("YYYYMMDD_Of_RefPrcntlArray is ",YYYYMMDD_Of_RefPrcntlArray)
print("RefPrcntlArray.shape is ",RefPrcntlArray.shape)
print("RefPrcntlArray is ",RefPrcntlArray)
print("np.amin(np.isnan(RefPrcntlArray).sum(axis=0)) is ",np.amin(np.isnan(RefPrcntlArray).sum(axis=0)))
print("np.amax(np.isnan(RefPrcntlArray).sum(axis=0)) is ",np.amax(np.isnan(RefPrcntlArray).sum(axis=0)))
print("np.amin(np.isnan(RefPrcntlArray).sum(axis=1)) is ",np.amin(np.isnan(RefPrcntlArray).sum(axis=1)))
print("np.amax(np.isnan(RefPrcntlArray).sum(axis=1)) is ",np.amax(np.isnan(RefPrcntlArray).sum(axis=1)))
print('overall min is ',np.nanmin(RefPrcntlArray),', overall max is ',np.nanmax(RefPrcntlArray))

np.savez_compressed(ArrayFileName, YYYYMMDD_Of_RefPrcntlArray = YYYYMMDD_Of_RefPrcntlArray, RefPrcntlArray = RefPrcntlArray)

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")


