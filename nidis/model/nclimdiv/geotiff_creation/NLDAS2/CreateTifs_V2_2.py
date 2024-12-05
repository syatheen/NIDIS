from __future__ import division
#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        ArgLSM ArgVariable ArgYear ArgMonth 
#ArgNum   1      2           3       4

import rioxarray
import xarray as xr
import numpy as np
from datetime import date, datetime, timedelta
import sys
import os
from calendar import monthrange

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

ArgLSM = sys.argv[1]
ArgVariable = sys.argv[2]
ArgYearStr = sys.argv[3]
ArgYearInt = int(round(float(ArgYearStr)))
ArgMonthStr = sys.argv[4]
ArgMonthInt = int(round(float(ArgMonthStr)))
NC_filename_base = '/discover/nobackup/projects/nca/REFERENCE_DATA/drought/NLDAS/daily/' + ArgLSM + '/' + ArgVariable + '/' + format(ArgYearInt,'04') + '/' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') 

#######END ANY EDITS REQUIRED#########

cmd = 'mkdir -p /discover/nobackup/projects/nca/syatheen/NLDAS_2_daily/' 
os.system(cmd)

for WhichDayOfMonth in range(1, monthrange(ArgYearInt, ArgMonthInt)[1]+1):

  cmd = 'cp '+ NC_filename_base + format(WhichDayOfMonth,'02') + '.' + ArgVariable + '.' + ArgLSM + '.PERW.nc /discover/nobackup/projects/nca/syatheen/NLDAS_2_daily/.' 
  os.system(cmd)

  NLDAS_2_DayOfMonth = xr.open_dataset('/discover/nobackup/projects/nca/syatheen/NLDAS_2_daily/' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + format(WhichDayOfMonth,'02') + '.' + ArgVariable + '.' + ArgLSM + '.PERW.nc')
  
  NLDAS_2_DayOfMonth = NLDAS_2_DayOfMonth.rename({'lon': 'x','lat': 'y'})
  
  NLDAS_2_DayOfMonth = NLDAS_2_DayOfMonth.astype(np.float32)

  NLDAS_2_DayOfMonth.rio.write_crs("epsg:4326", inplace=True)
  NLDAS_2_DayOfMonth["percentile"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/NLDAS_2_daily/' + ArgLSM + '.' + ArgVariable + '.' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + format(WhichDayOfMonth,'02') + '.PERW.tif')

  cmd = '/bin/rm /discover/nobackup/projects/nca/syatheen/NLDAS_2_daily/' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + format(WhichDayOfMonth,'02') + '.' + ArgVariable + '.' + ArgLSM + '.PERW.nc' 
  os.system(cmd)

#end of for WhichDayOfMonth in range(1, monthrange(ArgYearInt, ArgMonthInt)[1]+1)

print('NLDAS_2_DayOfMonth.dims is ', NLDAS_2_DayOfMonth.dims)

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")




