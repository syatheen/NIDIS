from __future__ import division
#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        ArgVariable ArgYear ArgMonth
#ArgNum   1           2       3

import rioxarray
import xarray as xr
import numpy as np
from datetime import date, datetime, timedelta
import sys
import os

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

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
                          #              prcp, tavg, tmax, tmin  
ArgYearStr = sys.argv[2]
ArgYearInt = int(round(float(ArgYearStr)))
ArgMonthStr = sys.argv[3]
ArgMonthInt = int(round(float(ArgMonthStr)))

if (ArgVariable[0:10] == 'spei-gamma'):
  OrigFilePath = 'monthly_spei_gamma/'
elif (ArgVariable[0:12] == 'spei-pearson'):
  OrigFilePath = 'monthly_spei_pearson/'
elif (ArgVariable[0:9] == 'spi-gamma'):
  OrigFilePath = 'monthly_spi_gamma/'
elif (ArgVariable[0:11] == 'spi-pearson'):
  OrigFilePath = 'monthly_spi_pearson/'
elif (ArgVariable == 'pet'):
  OrigFilePath = 'pet/'
elif ( (ArgVariable == 'prcp') or 
       (ArgVariable == 'tavg') or 
       (ArgVariable == 'tmax') or 
       (ArgVariable == 'tmin') ):
  OrigFilePath = 'base_files/'

#print("OrigFilePath is ", OrigFilePath)

NC_StartYear = 1895
NC_StartMonth = 1

#######END ANY EDITS REQUIRED#########

#cmd = 'mkdir -p nClimGrid'
#os.system(cmd)

cmd = 'cp ' + OrigFilePath + 'nclimgrid-' + ArgVariable + '.nc /discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '-' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.nc'
#print("cmd is ", cmd)
os.system(cmd)

nClimGrid_All = xr.open_dataset('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '-' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.nc')

nClimGrid_All = nClimGrid_All.rename({'lon': 'x','lat': 'y'})

nClimGrid_All = nClimGrid_All.astype(np.float32)

print('nClimGrid_All.dims is ', nClimGrid_All.dims)

TimeIndex_0Start = (ArgYearInt - NC_StartYear) * 12 + (ArgMonthInt - NC_StartMonth)

nClimGrid_temp = nClimGrid_All.isel(time = TimeIndex_0Start)
del nClimGrid_temp['time']
nClimGrid_temp.rio.write_crs("epsg:4326", inplace=True)

if ( (ArgVariable == 'spei-gamma-01') or (ArgVariable == 'spei-pearson-01') ):
  nClimGrid_temp["spei_01"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( (ArgVariable == 'spei-gamma-02') or (ArgVariable == 'spei-pearson-02') ):
  nClimGrid_temp["spei_02"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( (ArgVariable == 'spei-gamma-03') or (ArgVariable == 'spei-pearson-03') ):
  nClimGrid_temp["spei_03"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( (ArgVariable == 'spei-gamma-06') or (ArgVariable == 'spei-pearson-06') ):
  nClimGrid_temp["spei_06"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( (ArgVariable == 'spei-gamma-09') or (ArgVariable == 'spei-pearson-09') ):
  nClimGrid_temp["spei_09"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( (ArgVariable == 'spei-gamma-12') or (ArgVariable == 'spei-pearson-12') ):
  nClimGrid_temp["spei_12"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( (ArgVariable == 'spei-gamma-24') or (ArgVariable == 'spei-pearson-24') ):
  nClimGrid_temp["spei_24"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( (ArgVariable == 'spei-gamma-36') or (ArgVariable == 'spei-pearson-36') ):
  nClimGrid_temp["spei_36"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( (ArgVariable == 'spei-gamma-48') or (ArgVariable == 'spei-pearson-48') ):
  nClimGrid_temp["spei_48"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( (ArgVariable == 'spei-gamma-60') or (ArgVariable == 'spei-pearson-60') ):
  nClimGrid_temp["spei_60"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( (ArgVariable == 'spei-gamma-72') or (ArgVariable == 'spei-pearson-72') ):
  nClimGrid_temp["spei_72"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( (ArgVariable == 'spi-gamma-01') or (ArgVariable == 'spi-pearson-01') ):
  nClimGrid_temp["spi_01"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( (ArgVariable == 'spi-gamma-02') or (ArgVariable == 'spi-pearson-02') ):
  nClimGrid_temp["spi_02"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( (ArgVariable == 'spi-gamma-03') or (ArgVariable == 'spi-pearson-03') ):
  nClimGrid_temp["spi_03"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( (ArgVariable == 'spi-gamma-06') or (ArgVariable == 'spi-pearson-06') ):
  nClimGrid_temp["spi_06"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( (ArgVariable == 'spi-gamma-09') or (ArgVariable == 'spi-pearson-09') ):
  nClimGrid_temp["spi_09"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( (ArgVariable == 'spi-gamma-12') or (ArgVariable == 'spi-pearson-12') ):
  nClimGrid_temp["spi_12"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( (ArgVariable == 'spi-gamma-24') or (ArgVariable == 'spi-pearson-24') ):
  nClimGrid_temp["spi_24"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( (ArgVariable == 'spi-gamma-36') or (ArgVariable == 'spi-pearson-36') ):
  nClimGrid_temp["spi_36"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( (ArgVariable == 'spi-gamma-48') or (ArgVariable == 'spi-pearson-48') ):
  nClimGrid_temp["spi_48"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( (ArgVariable == 'spi-gamma-60') or (ArgVariable == 'spi-pearson-60') ):
  nClimGrid_temp["spi_60"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( (ArgVariable == 'spi-gamma-72') or (ArgVariable == 'spi-pearson-72') ):
  nClimGrid_temp["spi_72"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( ArgVariable == 'pet'):
  nClimGrid_temp["pet"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( ArgVariable == 'tavg'):
  nClimGrid_temp["tavg"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( ArgVariable == 'tmax'):
  nClimGrid_temp["tmax"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')
elif ( ArgVariable == 'prcp'):
  nClimGrid_temp["prcp"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.tif')

cmd = '/bin/rm /discover/nobackup/projects/nca/syatheen/nClimGrid/' + ArgVariable + '-' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '.nc' 
os.system(cmd)

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")




