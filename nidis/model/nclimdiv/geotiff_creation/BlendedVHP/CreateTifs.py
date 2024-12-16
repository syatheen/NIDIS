# Coded by Soni Yatheendradas
#         on Oct 21, 2021
from __future__ import division

#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        Filename 
#ArgNum   1        

import rioxarray
import xarray as xr
import numpy as np
from datetime import date, datetime, timedelta
import sys

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

Filename = sys.argv[1] # e.g., 'VHP.G04.C07.NC.P1981035.SM.SMN.tif'

#######END ANY EDITS REQUIRED#########

BlendedVHP = xr.open_rasterio('/discover/nobackup/projects/nca/syatheen/BlendedVHP/' + Filename)

#BlendedVHP = BlendedVHP.rename({'lon': 'x','lat': 'y'})

#BlendedVHP = BlendedVHP.astype(np.float32)

print('BlendedVHP.dims is ', BlendedVHP.dims)
print('BlendedVHP.sizes is ', BlendedVHP.sizes)

BlendedVHP_temp = BlendedVHP.isel(band=0)
del BlendedVHP_temp['band']

BlendedVHP_temp_masked = BlendedVHP_temp.where(BlendedVHP_temp > -9998.)

BlendedVHP_temp_masked.rio.write_crs("epsg:4326", inplace=True)

TruncFilenamePart1 = Filename[:12]
TruncFilenamePart2 = Filename[-19:]

TruncFilename = TruncFilenamePart1 + TruncFilenamePart2

BlendedVHP_temp_masked.rio.to_raster('/discover/nobackup/projects/nca/syatheen/BlendedVHP_RenamedTifs/' + TruncFilename)

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")

