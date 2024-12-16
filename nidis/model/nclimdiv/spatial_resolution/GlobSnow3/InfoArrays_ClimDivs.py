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
#        ArgYYYYMMDDInt
#ArgNum   1      

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

#ClimDivShpFile = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS_EPSG3408.shp'
ClimDivShpFile = '/discover/nobackup/syatheen/NIDIS/Data/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS_EPSG3408.shp'

mask = None

ArgYYYYMMDDStr = sys.argv[1]
ArgYYYYMMDDInt = int(round(float(ArgYYYYMMDDStr)))

cmd = 'mkdir -p /discover/nobackup/projects/nca/syatheen/GlobSnow3_Npzs/'
os.system(cmd)

ArrayFileName = '/discover/nobackup/projects/nca/syatheen/GlobSnow3_Npzs/GlobSnow3_' + format(ArgYYYYMMDDInt,'08') + '_ClimDivs.npz'

GlobSnow3_ThisDay_LowerLimit = 0.

#######END ANY EDITS REQUIRED#########

#BEGIN GETTING CLIMDIV SHAPEFILE DATA
ClimDivShp = gpd.read_file(ClimDivShpFile)
CLIMDIV_SortedList_FrmShpFile = sorted(ClimDivShp.CLIMDIV.values.tolist())
#END GETTING CLIMDIV SHAPEFILE DATA

YYYYMMDD_Of_InfoArray = np.empty((1, 1), dtype=np.int32)
YYYYMMDD_Of_InfoArray[:] = -9999
InfoArray = np.empty((1, len(CLIMDIV_SortedList_FrmShpFile)))
InfoArray[:] = np.NaN

YYYYMMDD_Of_InfoArray[0] = ArgYYYYMMDDInt 
SourceFile = '/discover/nobackup/projects/nca/syatheen/GlobSnow3/GlobSnow3_' + format(ArgYYYYMMDDInt,'08') + '.tif'

IfTifFileExists = os.path.exists(SourceFile)
if IfTifFileExists:
  with rasterio.Env():
    with rasterio.open(SourceFile) as SrcInfo:
      ImageInfo = SrcInfo.read()
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
                                   ( Intrsct.raster_val >= GlobSnow3_ThisDay_LowerLimit  ) &
                                   (Intrsct.geometry.area > 0) ]
        if len(Sel_Intrsct.index) > 0:
          InfoArray[0, iClimDiv] = (Sel_Intrsct.raster_val*Sel_Intrsct.geometry.area).sum()/Sel_Intrsct.geometry.area.sum()

      #end of for iClimDiv in range(len(CLIMDIV_SortedList_FrmShpFile))
    #end of with rasterio.open(SourceFile) as SrcInfo
  #with rasterio.Env()
#end of if IfTifFileExists

print("YYYYMMDD_Of_InfoArray.shape is ",YYYYMMDD_Of_InfoArray.shape)
print("YYYYMMDD_Of_InfoArray is ",YYYYMMDD_Of_InfoArray)
print("InfoArray.shape is ",InfoArray.shape)
print("InfoArray is ",InfoArray)
print("np.amin(np.isnan(InfoArray).sum(axis=1)) is ",np.amin(np.isnan(InfoArray).sum(axis=1)))
print("np.amax(np.isnan(InfoArray).sum(axis=1)) is ",np.amax(np.isnan(InfoArray).sum(axis=1)))
print('overall min is ',np.nanmin(InfoArray),', overall max is ',np.nanmax(InfoArray))

np.savez_compressed(ArrayFileName, YYYYMMDD_Of_InfoArray = YYYYMMDD_Of_InfoArray, InfoArray = InfoArray)

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")


