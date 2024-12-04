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

#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        ArgVariable ArgYearInt ArgMonthInt
#ArgNum   1           2          3     

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

cmd = 'mkdir -p /discover/nobackup/projects/nca/syatheen/nClimGrid_Npzs/'
os.system(cmd)

#ClimDivShpFile = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS_EPSG4326.shp'
ClimDivShpFile = '/discover/nobackup/syatheen/NIDIS/Data/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS_EPSG4326.shp'

mask = None

ArgVariable = sys.argv[1] # Choices are: spei-gamma-01, spei-gamma-02, spei-gamma-03,
                          #              spei-gamma-06, spei-gamma-09, spei-gamma-12,
                          #              spei-gamma-24, spei-gamma-36, spei-gamma-48,
                          #              spei-gamma-60, spei-gamma-72,
                          #              spei-pearson-01, spei-pearson-02, spei-pearson-03,
                          #              spei-pearson-06, spei-pearson-09, spei-pearson-12,
                          #              spei-pearson-24, spei-pearson-36, spei-pearson-48,
                          #              spei-pearson-60, spei-pearson-72,
                          #              spi-gamma-01, spi-gamma-02, spi-gamma-03,
                          #              spi-gamma-06, spi-gamma-09, spi-gamma-12,
                          #              spi-gamma-24, spi-gamma-36, spi-gamma-48,
                          #              spi-gamma-60, spi-gamma-72,
                          #              spi-pearson-01, spi-pearson-02, spi-pearson-03,
                          #              spi-pearson-06, spi-pearson-09, spi-pearson-12,
                          #              spi-pearson-24, spi-pearson-36, spi-pearson-48,
                          #              spi-pearson-60, spi-pearson-72,
                          #              pet,
                          #              prcp, tavg, tmax
ArgYearInt = int(round(float(sys.argv[2])))
ArgMonthInt = int(round(float(sys.argv[3])))

ArrayFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_Npzs/' + ArgVariable+'_'+format(ArgYearInt,'04')+format(ArgMonthInt,'02')+'ClimDivs.npz'

if ( (ArgVariable[0:10] == 'spei-gamma') or
     (ArgVariable[0:12] == 'spei-pearson') or
     (ArgVariable[0:9] == 'spi-gamma') or
     (ArgVariable[0:11] == 'spi-pearson') ):
  Variable_LowerLimit = -3.09
  Variable_UpperLimit = 3.09
elif (ArgVariable == 'pet'):
  Variable_LowerLimit = 0
  Variable_UpperLimit = 3.402823466385289e+38
elif ( (ArgVariable == 'tavg') or
       (ArgVariable == 'tmax') ):
  Variable_LowerLimit = -100
  Variable_UpperLimit = 100
elif (ArgVariable == 'prcp'):
  Variable_LowerLimit = 0
  Variable_UpperLimit = 2000
#end of if ( (ArgVariable[0:10] == 'spei-gamma') or...

SourceFile = '/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif'

#######END ANY EDITS REQUIRED#########

#BEGIN GETTING CLIMDIV SHAPEFILE DATA
ClimDivShp = gpd.read_file(ClimDivShpFile)
CLIMDIV_SortedList_FrmShpFile = sorted(ClimDivShp.CLIMDIV.values.tolist())
#END GETTING CLIMDIV SHAPEFILE DATA

YYYYMM_Of_RefArrayForPrcntl = np.empty((1,1), dtype=np.int32)
YYYYMM_Of_RefArrayForPrcntl[:] = -9999
RefArrayForPrcntl = np.empty((1,len(CLIMDIV_SortedList_FrmShpFile)))
RefArrayForPrcntl[:] = np.NaN

YYYYMM_Of_RefArrayForPrcntl[0] = 100 * ArgYearInt + ArgMonthInt

IfTifFileExists = os.path.exists(SourceFile)
if IfTifFileExists:
  with rasterio.Env():
    with rasterio.open(SourceFile) as SrcInfo:
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
                                   ( Intrsct.raster_val >= Variable_LowerLimit  ) &
                                   ( Intrsct.raster_val <= Variable_UpperLimit  ) &
                                   (Intrsct.geometry.area > 0) ]
        if len(Sel_Intrsct.index) > 0:
          RefArrayForPrcntl[0, iClimDiv] = (Sel_Intrsct.raster_val*Sel_Intrsct.geometry.area).sum()/Sel_Intrsct.geometry.area.sum()

      #end of for iClimDiv in range(len(CLIMDIV_SortedList_FrmShpFile))
    #with rasterio.open(SourceFile) as SrcInfo
  #with rasterio.Env()
#end of if IfTifFileExists

print("YYYYMM_Of_RefArrayForPrcntl.shape is ",YYYYMM_Of_RefArrayForPrcntl.shape)
print("YYYYMM_Of_RefArrayForPrcntl is ",YYYYMM_Of_RefArrayForPrcntl)
print("RefArrayForPrcntl.shape is ",RefArrayForPrcntl.shape)
print("RefArrayForPrcntl is ",RefArrayForPrcntl)
print("np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)))
print("np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)))
print("np.amin(np.isnan(RefArrayForPrcntl).sum(axis=1)) is ",np.amin(np.isnan(RefArrayForPrcntl).sum(axis=1)))
print("np.amax(np.isnan(RefArrayForPrcntl).sum(axis=1)) is ",np.amax(np.isnan(RefArrayForPrcntl).sum(axis=1)))
print('overall min is ',np.nanmin(RefArrayForPrcntl),', overall max is ',np.nanmax(RefArrayForPrcntl))

np.savez_compressed(ArrayFileName, YYYYMM_Of_RefArrayForPrcntl = YYYYMM_Of_RefArrayForPrcntl, RefArrayForPrcntl = RefArrayForPrcntl)

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")


