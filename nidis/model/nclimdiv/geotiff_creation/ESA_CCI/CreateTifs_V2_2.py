from __future__ import division
#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        ArgYear ArgMonth 
#ArgNum   1       2

import rioxarray
import xarray as xr
import numpy as np
from datetime import date, datetime, timedelta
import sys
import os
from calendar import monthrange

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

ArgYearStr = sys.argv[1]
ArgYearInt = int(round(float(ArgYearStr)))
ArgMonthStr = sys.argv[2]
ArgMonthInt = int(round(float(ArgMonthStr)))
NC_filename_base = '/discover/nobackup/projects/lis/RS_DATA/ESACCI/v06.1/COMBINED/' + format(ArgYearInt,'04') + '/ESACCI-SOILMOISTURE-L3S-SSMV-COMBINED-' + format(ArgYearInt,'04') + format(ArgMonthInt,'02')  

#######END ANY EDITS REQUIRED#########

cmd = 'mkdir -p /discover/nobackup/projects/nca/syatheen/ESA_CCI/' 
os.system(cmd)

for WhichDayOfMonth in range(1, monthrange(ArgYearInt, ArgMonthInt)[1]+1):

  cmd = 'cp '+ NC_filename_base + format(WhichDayOfMonth,'02') + '000000-fv06.1.nc  /discover/nobackup/projects/nca/syatheen/ESA_CCI/.' 
  os.system(cmd)

  ESC_CCI_DayOfMonth = xr.open_dataset('/discover/nobackup/projects/nca/syatheen/ESA_CCI/ESACCI-SOILMOISTURE-L3S-SSMV-COMBINED-' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + format(WhichDayOfMonth,'02') + '000000-fv06.1.nc')
  
  ESC_CCI_DayOfMonth = ESC_CCI_DayOfMonth.rename({'lon': 'x','lat': 'y'})
  
  ESC_CCI_DayOfMonth = ESC_CCI_DayOfMonth.astype(np.float32)

  ESC_CCI_temp = ESC_CCI_DayOfMonth.isel(time = 0)
  del ESC_CCI_temp['time']

  ESC_CCI_temp.rio.write_crs("epsg:4326", inplace=True)
  ESC_CCI_temp["sm"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/ESA_CCI/ESA_CCI_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + format(WhichDayOfMonth,'02') + '.tif')

  cmd = '/bin/rm /discover/nobackup/projects/nca/syatheen/ESA_CCI/ESACCI-SOILMOISTURE-L3S-SSMV-COMBINED-' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + format(WhichDayOfMonth,'02') + '000000-fv06.1.nc' 
  os.system(cmd)

#end of for WhichDayOfMonth in range(1, monthrange(ArgYearInt, ArgMonthInt)[1]+1)

print('ESC_CCI_DayOfMonth.dims is ', ESC_CCI_DayOfMonth.dims)

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")




