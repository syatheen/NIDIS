from __future__ import division
#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        ArgYear ArgMonth ArgDayOfMonth 
#ArgNum   1       2        3        

import rioxarray
import xarray as xr
import numpy as np
from datetime import date, datetime, timedelta
import sys
import os
from netCDF4 import Dataset as nc

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

ArgYearStr = sys.argv[1]
ArgYearInt = int(round(float(ArgYearStr)))
ArgMonthStr = sys.argv[2]
ArgMonthInt = int(round(float(ArgMonthStr)))
ArgDayOfMonthStr = sys.argv[3]
ArgDayOfMonthInt = int(round(float(ArgDayOfMonthStr)))
NC_filename = '/discover/nobackup/projects/nca/syatheen/IMERG/daily_Final_V06/' + format(ArgYearInt,'04') + '/3B-DAY.MS.MRG.3IMERG.' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + format(ArgDayOfMonthInt,'02') + '-S000000-E235959.V06.nc4'

#######END ANY EDITS REQUIRED#########

ds = nc(NC_filename)

#Read in Variables
lat = ds.variables['lat'][:]
lat.astype(np.float64)
lon = ds.variables['lon'][:]
lon.astype(np.float64)
prec=ds.variables['precipitationCal'][:]
prec = prec[0, :, :]
prec = np.transpose(prec)

IMERG_Daily = xr.Dataset(
    data_vars=dict(
        precip=(["y", "x"], prec),
    ),
    coords=dict(
        lat=(["y"], lat),
        lon=(["x"], lon),
    ),
    attrs = dict(description="IMERG Final Daily precipitationCal"),
)

IMERG_Daily = IMERG_Daily.rename({'lon': 'x','lat': 'y'})

print('IMERG_Daily.dims is ', IMERG_Daily.dims)

IMERG_Daily = IMERG_Daily.astype(np.float32)

IMERG_Daily.rio.write_crs("epsg:4326", inplace=True)

IMERG_Daily["precip"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/IMERG/daily_Final_V06_Tifs/IMERG' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + format(ArgDayOfMonthInt,'02') + '.tif')

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")




