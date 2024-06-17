from __future__ import division
#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        ArgYear 
#ArgNum   1     
# 

import rioxarray
import xarray as xr
import numpy as np
from datetime import date, datetime, timedelta
import sys

ssstart_Overall = datetime.now()

#######BEGIN ANY EDITS REQUIRED#######

ArgYearStr = sys.argv[1]
ArgYearInt = int(round(float(ArgYearStr)))
# NC_filename = 'YearlyNCFiles_HavingDaysInYear/esi_fppm_y'+ArgYearStr+'.nc'
NC_filename = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/OriginalData/ESI/esi_fppm_y'+ArgYearStr+'.nc'
InitialNumDaysOfYearToProcess = int(round(float(sys.argv[2]))) # if -ve number like -9999, then processes all days of the year

#######END ANY EDITS REQUIRED#########

esi_ForDaysOfYear = xr.open_dataset(NC_filename)

esi_ForDaysOfYear = esi_ForDaysOfYear.rename({'lon': 'x','lat': 'y'})

esi_ForDaysOfYear = esi_ForDaysOfYear.astype(np.float32)

print('esi_ForDaysOfYear.dims is ', esi_ForDaysOfYear.dims)

if InitialNumDaysOfYearToProcess <= 0:
  days_in_year = (date(ArgYearInt,12,31)-date(ArgYearInt-1,12,31)).days
  print('days_in_year = ',days_in_year)
  if esi_ForDaysOfYear.dims['time'] != days_in_year:
   sys.exit("time dimension of year array doesnt match with days_in_year!!!")
else:
  days_in_year = InitialNumDaysOfYearToProcess
  print('considered initial days_in_year = ',days_in_year)

RefDateTime = datetime(ArgYearInt-1, 12, 31, 0, 0, 0)

for WhichDayOfYear in range(1,days_in_year+1):

  ThisDateTime = RefDateTime + timedelta(days=WhichDayOfYear)
  ThisYear = ThisDateTime.year
  ThisMonth = ThisDateTime.month
  ThisDoM = ThisDateTime.day

  esi_temp = esi_ForDaysOfYear.isel(time = (WhichDayOfYear-1))
  del esi_temp['time']
  esi_temp.rio.write_crs("epsg:4326", inplace=True)
  esi_temp["esi"].rio.to_raster('/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/OriginalData/ESI/'+format(ThisYear,'04')+format(ThisMonth,'02')+format(ThisDoM,'02')+'.tif')

#end of for WhichDayOfYear in range(1,days_in_year+1)

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")


