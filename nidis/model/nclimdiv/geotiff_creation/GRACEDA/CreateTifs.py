from __future__ import division
from datetime import datetime, timedelta
import glob
import xarray as xr
import sys
import rioxarray
import xarray as xr

# BEGIN code arguments / editable section

# Available dates range from 2002/04/01 to 2020/08/10

BeginDateVecList = [2002, 4, 1, 0, 0, 0]
#EndDateVecList = [2020, 8, 10, 0, 0, 0]
EndDateVecList = [2020, 10, 26, 0, 0, 0] # v040

# END code arguments / editable section

ssstart_Overall = datetime.now()

BeginDateTime = datetime(BeginDateVecList[0], BeginDateVecList[1], BeginDateVecList[2], BeginDateVecList[3], BeginDateVecList[4], BeginDateVecList[5])
EndDateTime = datetime(EndDateVecList[0], EndDateVecList[1], EndDateVecList[2], EndDateVecList[3], EndDateVecList[4], EndDateVecList[5])
DiffTimee = EndDateTime - BeginDateTime
NumWeeks = int(round(DiffTimee.total_seconds()/(3600*24*7)) + 1)
print('NumWeeks = ',NumWeeks)

for WhichWeek in range(NumWeeks):

  ThisDateTime = BeginDateTime + timedelta(days=(WhichWeek*7))
  ThisYear = ThisDateTime.year
  ThisMonth = ThisDateTime.month
  ThisDoM = ThisDateTime.day

#  FileNames_GRACE=glob.glob('/att/nobackup/dmocko/GRACE/'+format(ThisYear,'04')+format(ThisMonth,'02')+format(ThisDoM,'02')+'/GRACEDADM_CLSM0125US_7D.A'+format(ThisYear,'04')+format(ThisMonth,'02')+format(ThisDoM,'02')+'.030.nc4')
  FileNames_GRACE=glob.glob('/att/nobackup/dmocko/GRACE/v040/GRACEDADM_CLSM0125US_7D.A'+format(ThisYear,'04')+format(ThisMonth,'02')+format(ThisDoM,'02')+'.040.nc4')

  if (len(FileNames_GRACE) == 1):
    FileName_GRACE = FileNames_GRACE[0]
    grace = xr.open_dataset(FileName_GRACE)
    grace = grace.rename({'lon': 'x','lat': 'y'})
    grace.rio.write_crs("epsg:4326", inplace=True)
#    grace['rtzsm_inst'].rio.to_raster('TifFiles/rtzsm_inst/GRACEDADM_CLSM0125US_7D.A'+format(ThisYear,'04')+format(ThisMonth,'02')+format(ThisDoM,'02')+'.030.tif')
#    grace['sfsm_inst'].rio.to_raster('TifFiles/sfsm_inst/GRACEDADM_CLSM0125US_7D.A'+format(ThisYear,'04')+format(ThisMonth,'02')+format(ThisDoM,'02')+'.030.tif')
#    grace['gws_inst'].rio.to_raster('TifFiles/gws_inst/GRACEDADM_CLSM0125US_7D.A'+format(ThisYear,'04')+format(ThisMonth,'02')+format(ThisDoM,'02')+'.030.tif')
    grace['rtzsm_inst'].rio.to_raster('TifFiles/v040/rtzsm_inst/GRACEDADM_CLSM0125US_7D.A'+format(ThisYear,'04')+format(ThisMonth,'02')+format(ThisDoM,'02')+'.040.tif')
    grace['sfsm_inst'].rio.to_raster('TifFiles/v040/sfsm_inst/GRACEDADM_CLSM0125US_7D.A'+format(ThisYear,'04')+format(ThisMonth,'02')+format(ThisDoM,'02')+'.040.tif')
    grace['gws_inst'].rio.to_raster('TifFiles/v040/gws_inst/GRACEDADM_CLSM0125US_7D.A'+format(ThisYear,'04')+format(ThisMonth,'02')+format(ThisDoM,'02')+'.040.tif')
  else:   # if (len(FileNames_GRACE) == 1):
    sys.exit("len(FileNames_GRACE) != 1 for "+format(ThisYear,'04')+format(ThisMonth,'02')+format(ThisDoM,'02')+"!!!")
#    if ( (ThisYear == 2019) and (ThisMonth == 12) and (ThisDoM == 9) ):
#      pass
#    else:
#      sys.exit("len(FileNames_GRACE) != 1 for "+format(ThisYear,'04')+format(ThisMonth,'02')+format(ThisDoM,'02')+"!!!")
  #end of if (len(FileNames_GRACE) == 1)

#end of for WhichWeek in range(NumWeeks)

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")






