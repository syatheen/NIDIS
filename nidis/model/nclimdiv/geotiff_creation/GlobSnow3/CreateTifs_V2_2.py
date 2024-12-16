from __future__ import division
#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        ArgYYYYMMDD 
#ArgNum   1      

import rioxarray
import xarray as xr
import numpy as np
from datetime import date, datetime, timedelta
import sys
import os
from calendar import monthrange

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

ArgYYYYMMDDStr = sys.argv[1]
ArgYYYYMMDDInt = int(round(float(ArgYYYYMMDDStr)))

#######END ANY EDITS REQUIRED#########

cmd = 'mkdir -p /discover/nobackup/projects/nca/syatheen/GlobSnow3/' 
os.system(cmd)

GlobSnow3_ThisDay = xr.open_dataset('/discover/nobackup/projects/nca/syatheen/GlobSnow3/' + format(ArgYYYYMMDDInt,'08') + '_northern_hemisphere_swe_0.25grid.nc')

#GlobSnow3_ThisDay = GlobSnow3_ThisDay.rename({'lon': 'x','lat': 'y'})

#GlobSnow3_ThisDay = GlobSnow3_ThisDay.astype(np.float32)

GlobSnow3_ThisDay.rio.write_crs("epsg:3408", inplace=True)
GlobSnow3_ThisDay["swe"].rio.to_raster('/discover/nobackup/projects/nca/syatheen/GlobSnow3/GlobSnow3_' + format(ArgYYYYMMDDInt,'08') + '.tif')

print('GlobSnow3_ThisDay.dims is ', GlobSnow3_ThisDay.dims)

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")




