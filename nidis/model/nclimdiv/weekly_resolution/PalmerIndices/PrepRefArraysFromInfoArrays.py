# BEGIN code arguments / editable section

ZIndex_InfoFilename = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/Palmer/monthly/private/RefArr_1MonthAccumzndx_193201To202001.npz' 
ZIndex60month_InfoFilename = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/Palmer/monthly/private/RefArr_60MonthAccumzndx_193201To202001.npz' 
PMDI_InfoFilename = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/Palmer/weekly/private/pdiRefArray_20050101To20200104.npz' 
PHDI_InfoFilename = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/Palmer/weekly/private/phdRefArray_20050604To20200104.npz'
Pcpn1month_InfoFilename = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/Palmer/monthly/private/RefArr_1MonthPcpn_193201To202001.npz'
Pcpn3month_InfoFilename = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/Palmer/monthly/private/RefArr_3MonthPcpn_193201To202001.npz'
Pcpn6month_InfoFilename = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/Palmer/monthly/private/RefArr_6MonthPcpn_193201To202001.npz'
Pcpn12month_InfoFilename = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/Palmer/monthly/private/RefArr_12MonthPcpn_193201To202001.npz'
Pcpn24month_InfoFilename = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/Palmer/monthly/private/RefArr_24MonthPcpn_193201To202001.npz'
Pcpn60month_InfoFilename = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/Palmer/monthly/private/RefArr_60MonthPcpn_193201To202001.npz'
CPCsoilmoist_InfoFilename = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/CPCsoilmoisture/total/daily/private/QC_test/RefArrDaily_20080205To20200106.npz'
USDM_InfoFilename = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/usdm_shapefiles/private/InfoArrWeekly_20000104To20200428.npz' 

ZIndex_Ref_BeginDateVecList = [1932, 1, 19]  # ZIndex beginning year, month, day of month, this is also a Tuesday
ZIndex_Ref_EndDateVecList = [2019, 12, 31]  # ZIndex ending year, month, day of month, this is also a Tuesday
PMDI_Ref_BeginDateVecList = [2005, 1, 4]  # PMDI beginning year, month, day of month, this is also a Tuesday
PMDI_Ref_EndDateVecList = [2019, 12, 31]  # PMDI ending year, month, day of month, this is also a Tuesday
PHDI_Ref_BeginDateVecList = [2005, 6, 7]  # PHDI beginning year, month, day of month, this is also a Tuesday
PHDI_Ref_EndDateVecList = [2019, 12, 31]  # PHDI ending year, month, day of month, this is also a Tuesday
Pcpn_Ref_BeginDateVecList = [1932, 2, 2]  # Pcpn beginning year, month, day of month, this is also a Tuesday
Pcpn_Ref_EndDateVecList = [2019, 12, 31]  # Pcpn ending year, month, day of month, this is also a Tuesday
CPCsoilmoist_Ref_BeginDateVecList = [2008, 2, 5]  # CPCsoilmoist beginning year, month, day of month, this is also a Tuesday
CPCsoilmoist_Ref_EndDateVecList = [2019, 12, 31]  # CPCsoilmoist ending year, month, day of month, this is also a Tuesday

#ZIndex_Ref_BeginDateVecList = [2019, 12, 3]  # ZIndex beginning year, month, day of month, this is also a Tuesday
#ZIndex_Ref_EndDateVecList = [2019, 12, 31]  # ZIndex ending year, month, day of month, this is also a Tuesday
#PMDI_Ref_BeginDateVecList = [2019, 12, 3]  # PMDI beginning year, month, day of month, this is also a Tuesday
#PMDI_Ref_EndDateVecList = [2019, 12, 31]  # PMDI ending year, month, day of month, this is also a Tuesday
#PHDI_Ref_BeginDateVecList = [2019, 12, 3]  # PHDI beginning year, month, day of month, this is also a Tuesday
#PHDI_Ref_EndDateVecList = [2019, 12, 31]  # PHDI ending year, month, day of month, this is also a Tuesday
#Pcpn_Ref_BeginDateVecList = [2019, 12, 3]  # Pcpn beginning year, month, day of month, this is also a Tuesday
#Pcpn_Ref_EndDateVecList = [2019, 12, 31]  # Pcpn ending year, month, day of month, this is also a Tuesday
#CPCsoilmoist_Ref_BeginDateVecList = [2019, 12, 3]  # CPCsoilmoist beginning year, month, day of month, this is also a Tuesday
#CPCsoilmoist_Ref_EndDateVecList = [2019, 12, 31]  # CPCsoilmoist ending year, month, day of month, this is also a Tuesday

ZIndex_RefFileName = 'RefArrays/ClimDiv_ZIndex_'+format(ZIndex_Ref_BeginDateVecList[0],'04')+format(ZIndex_Ref_BeginDateVecList[1],'02')+format(ZIndex_Ref_BeginDateVecList[2],'02')+'To'+format(ZIndex_Ref_EndDateVecList[0],'04')+format(ZIndex_Ref_EndDateVecList[1],'02')+format(ZIndex_Ref_EndDateVecList[2],'02')+'.npz'
ZIndex60month_RefFileName = 'RefArrays/ClimDiv_ZIndex60month_'+format(ZIndex_Ref_BeginDateVecList[0],'04')+format(ZIndex_Ref_BeginDateVecList[1],'02')+format(ZIndex_Ref_BeginDateVecList[2],'02')+'To'+format(ZIndex_Ref_EndDateVecList[0],'04')+format(ZIndex_Ref_EndDateVecList[1],'02')+format(ZIndex_Ref_EndDateVecList[2],'02')+'.npz'
PMDI_RefFileName = 'RefArrays/ClimDiv_PMDI_'+format(PMDI_Ref_BeginDateVecList[0],'04')+format(PMDI_Ref_BeginDateVecList[1],'02')+format(PMDI_Ref_BeginDateVecList[2],'02')+'To'+format(PMDI_Ref_EndDateVecList[0],'04')+format(PMDI_Ref_EndDateVecList[1],'02')+format(PMDI_Ref_EndDateVecList[2],'02')+'.npz'
PHDI_RefFileName = 'RefArrays/ClimDiv_PHDI_'+format(PHDI_Ref_BeginDateVecList[0],'04')+format(PHDI_Ref_BeginDateVecList[1],'02')+format(PHDI_Ref_BeginDateVecList[2],'02')+'To'+format(PHDI_Ref_EndDateVecList[0],'04')+format(PHDI_Ref_EndDateVecList[1],'02')+format(PHDI_Ref_EndDateVecList[2],'02')+'.npz'
Pcpn1month_RefFileName = 'RefArrays/ClimDiv_Pcpn1month_'+format(Pcpn_Ref_BeginDateVecList[0],'04')+format(Pcpn_Ref_BeginDateVecList[1],'02')+format(Pcpn_Ref_BeginDateVecList[2],'02')+'To'+format(Pcpn_Ref_EndDateVecList[0],'04')+format(Pcpn_Ref_EndDateVecList[1],'02')+format(Pcpn_Ref_EndDateVecList[2],'02')+'.npz'
Pcpn3month_RefFileName = 'RefArrays/ClimDiv_Pcpn3month_'+format(Pcpn_Ref_BeginDateVecList[0],'04')+format(Pcpn_Ref_BeginDateVecList[1],'02')+format(Pcpn_Ref_BeginDateVecList[2],'02')+'To'+format(Pcpn_Ref_EndDateVecList[0],'04')+format(Pcpn_Ref_EndDateVecList[1],'02')+format(Pcpn_Ref_EndDateVecList[2],'02')+'.npz'
Pcpn6month_RefFileName = 'RefArrays/ClimDiv_Pcpn6month_'+format(Pcpn_Ref_BeginDateVecList[0],'04')+format(Pcpn_Ref_BeginDateVecList[1],'02')+format(Pcpn_Ref_BeginDateVecList[2],'02')+'To'+format(Pcpn_Ref_EndDateVecList[0],'04')+format(Pcpn_Ref_EndDateVecList[1],'02')+format(Pcpn_Ref_EndDateVecList[2],'02')+'.npz'
Pcpn12month_RefFileName = 'RefArrays/ClimDiv_Pcpn12month_'+format(Pcpn_Ref_BeginDateVecList[0],'04')+format(Pcpn_Ref_BeginDateVecList[1],'02')+format(Pcpn_Ref_BeginDateVecList[2],'02')+'To'+format(Pcpn_Ref_EndDateVecList[0],'04')+format(Pcpn_Ref_EndDateVecList[1],'02')+format(Pcpn_Ref_EndDateVecList[2],'02')+'.npz'
Pcpn24month_RefFileName = 'RefArrays/ClimDiv_Pcpn24month_'+format(Pcpn_Ref_BeginDateVecList[0],'04')+format(Pcpn_Ref_BeginDateVecList[1],'02')+format(Pcpn_Ref_BeginDateVecList[2],'02')+'To'+format(Pcpn_Ref_EndDateVecList[0],'04')+format(Pcpn_Ref_EndDateVecList[1],'02')+format(Pcpn_Ref_EndDateVecList[2],'02')+'.npz'
Pcpn60month_RefFileName = 'RefArrays/ClimDiv_Pcpn60month_'+format(Pcpn_Ref_BeginDateVecList[0],'04')+format(Pcpn_Ref_BeginDateVecList[1],'02')+format(Pcpn_Ref_BeginDateVecList[2],'02')+'To'+format(Pcpn_Ref_EndDateVecList[0],'04')+format(Pcpn_Ref_EndDateVecList[1],'02')+format(Pcpn_Ref_EndDateVecList[2],'02')+'.npz'
CPCsoilmoist_RefFileName = 'RefArrays/ClimDiv_CPCsoilmoist_'+format(CPCsoilmoist_Ref_BeginDateVecList[0],'04')+format(CPCsoilmoist_Ref_BeginDateVecList[1],'02')+format(CPCsoilmoist_Ref_BeginDateVecList[2],'02')+'To'+format(CPCsoilmoist_Ref_EndDateVecList[0],'04')+format(CPCsoilmoist_Ref_EndDateVecList[1],'02')+format(CPCsoilmoist_Ref_EndDateVecList[2],'02')+'.npz'

# END code arguments / editable section

from datetime import date, datetime, timedelta
import sys
import numpy as np
from calendar import monthrange
import time

start_time = time.time()

ZIndex_Ref_BeginDate = date(ZIndex_Ref_BeginDateVecList[0], ZIndex_Ref_BeginDateVecList[1], ZIndex_Ref_BeginDateVecList[2])
ZIndex_Ref_EndDate = date(ZIndex_Ref_EndDateVecList[0], ZIndex_Ref_EndDateVecList[1], ZIndex_Ref_EndDateVecList[2])
PMDI_Ref_BeginDate = date(PMDI_Ref_BeginDateVecList[0], PMDI_Ref_BeginDateVecList[1], PMDI_Ref_BeginDateVecList[2])
PMDI_Ref_EndDate = date(PMDI_Ref_EndDateVecList[0], PMDI_Ref_EndDateVecList[1], PMDI_Ref_EndDateVecList[2])
PHDI_Ref_BeginDate = date(PHDI_Ref_BeginDateVecList[0], PHDI_Ref_BeginDateVecList[1], PHDI_Ref_BeginDateVecList[2])
PHDI_Ref_EndDate = date(PHDI_Ref_EndDateVecList[0], PHDI_Ref_EndDateVecList[1], PHDI_Ref_EndDateVecList[2])
Pcpn_Ref_BeginDate = date(Pcpn_Ref_BeginDateVecList[0], Pcpn_Ref_BeginDateVecList[1], Pcpn_Ref_BeginDateVecList[2])
Pcpn_Ref_EndDate = date(Pcpn_Ref_EndDateVecList[0], Pcpn_Ref_EndDateVecList[1], Pcpn_Ref_EndDateVecList[2])
CPCsoilmoist_Ref_BeginDate = date(CPCsoilmoist_Ref_BeginDateVecList[0], CPCsoilmoist_Ref_BeginDateVecList[1], CPCsoilmoist_Ref_BeginDateVecList[2])
CPCsoilmoist_Ref_EndDate = date(CPCsoilmoist_Ref_EndDateVecList[0], CPCsoilmoist_Ref_EndDateVecList[1], CPCsoilmoist_Ref_EndDateVecList[2])

#BEGIN check whether the beginning and ending days are indeed Tuesdays
if ZIndex_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for ZIndex_Ref needs to be a Tuesday!!')
  sys.exit(0)
if ZIndex_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for ZIndex_Ref needs to be a Tuesday!!')
  sys.exit(0)
if PMDI_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for PMDI_Ref needs to be a Tuesday!!')
  sys.exit(0)
if PMDI_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for PMDI_Ref needs to be a Tuesday!!')
  sys.exit(0)
if PHDI_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for PHDI_Ref needs to be a Tuesday!!')
  sys.exit(0)
if PHDI_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for PHDI_Ref needs to be a Tuesday!!')
  sys.exit(0)
if Pcpn_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for Pcpn_Ref needs to be a Tuesday!!')
  sys.exit(0)
if Pcpn_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for Pcpn_Ref needs to be a Tuesday!!')
  sys.exit(0)
if CPCsoilmoist_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for CPCsoilmoist_Ref needs to be a Tuesday!!')
  sys.exit(0)
if CPCsoilmoist_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for CPCsoilmoist_Ref needs to be a Tuesday!!')
  sys.exit(0)
#END check whether the beginning and ending days are indeed Tuesdays

if ZIndex_Ref_BeginDate > ZIndex_Ref_EndDate:
  print('ZIndex_Ref_BeginDate should not be later than ZIndex_Ref_EndDate!!!')
  sys.exit(0)
if PMDI_Ref_BeginDate > PMDI_Ref_EndDate:
  print('PMDI_Ref_BeginDate should not be later than PMDI_Ref_EndDate!!!')
  sys.exit(0)
if PHDI_Ref_BeginDate > PHDI_Ref_EndDate:
  print('PHDI_Ref_BeginDate should not be later than PHDI_Ref_EndDate!!!')
  sys.exit(0)
if Pcpn_Ref_BeginDate > Pcpn_Ref_EndDate:
  print('Pcpn_Ref_BeginDate should not be later than Pcpn_Ref_EndDate!!!')
  sys.exit(0)
if CPCsoilmoist_Ref_BeginDate > CPCsoilmoist_Ref_EndDate:
  print('CPCsoilmoist_Ref_BeginDate should not be later than CPCsoilmoist_Ref_EndDate!!!')
  sys.exit(0)

#BEGIN section for time-interpolating info arrays to desired temporal resolution

ZIndex_Info = np.load(ZIndex_InfoFilename)
ZIndex60month_Info = np.load(ZIndex60month_InfoFilename)
PMDI_Info = np.load(PMDI_InfoFilename)
PHDI_Info = np.load(PHDI_InfoFilename)
Pcpn1month_Info = np.load(Pcpn1month_InfoFilename)
Pcpn3month_Info = np.load(Pcpn3month_InfoFilename)
Pcpn6month_Info = np.load(Pcpn6month_InfoFilename)
Pcpn12month_Info = np.load(Pcpn12month_InfoFilename)
Pcpn24month_Info = np.load(Pcpn24month_InfoFilename)
Pcpn60month_Info = np.load(Pcpn60month_InfoFilename)
CPCsoilmoist_Info = np.load(CPCsoilmoist_InfoFilename)
USDM_Info = np.load(USDM_InfoFilename)

ZIndex_YYYYMM_Of_InfoArray  = ZIndex_Info['YYYYMM_Of_RefArrayForPrcntl']
ZIndex_InfoArray  = ZIndex_Info['RefArrayForPrcntl']
ZIndex60month_YYYYMM_Of_InfoArray  = ZIndex60month_Info['YYYYMM_Of_RefArrayForPrcntl']
ZIndex60month_InfoArray  = ZIndex60month_Info['RefArrayForPrcntl']
PMDI_YYYYMMDD_Of_InfoArray  = PMDI_Info['YYYYMMDD_Of_RefArrayForPrcntl']
PMDI_YYYYMMDD_Of_InfoArray = np.expand_dims(PMDI_YYYYMMDD_Of_InfoArray, axis = 1)
PMDI_InfoArray  = PMDI_Info['Palmer_RefArrayForPrcntl']
PHDI_YYYYMMDD_Of_InfoArray  = PHDI_Info['YYYYMMDD_Of_RefArrayForPrcntl']
PHDI_YYYYMMDD_Of_InfoArray = np.expand_dims(PHDI_YYYYMMDD_Of_InfoArray, axis = 1)
PHDI_InfoArray  = PHDI_Info['Palmer_RefArrayForPrcntl']
Pcpn1month_YYYYMM_Of_InfoArray  = Pcpn1month_Info['YYYYMM_Of_RefArrayForPrcntl']
Pcpn1month_InfoArray  = Pcpn1month_Info['RefArrayForPrcntl']
Pcpn3month_YYYYMM_Of_InfoArray  = Pcpn3month_Info['YYYYMM_Of_RefArrayForPrcntl']
Pcpn3month_InfoArray  = Pcpn3month_Info['RefArrayForPrcntl']
Pcpn6month_YYYYMM_Of_InfoArray  = Pcpn6month_Info['YYYYMM_Of_RefArrayForPrcntl']
Pcpn6month_InfoArray  = Pcpn6month_Info['RefArrayForPrcntl']
Pcpn12month_YYYYMM_Of_InfoArray  = Pcpn12month_Info['YYYYMM_Of_RefArrayForPrcntl']
Pcpn12month_InfoArray  = Pcpn12month_Info['RefArrayForPrcntl']
Pcpn24month_YYYYMM_Of_InfoArray  = Pcpn24month_Info['YYYYMM_Of_RefArrayForPrcntl']
Pcpn24month_InfoArray  = Pcpn24month_Info['RefArrayForPrcntl']
Pcpn60month_YYYYMM_Of_InfoArray  = Pcpn60month_Info['YYYYMM_Of_RefArrayForPrcntl']
Pcpn60month_InfoArray  = Pcpn60month_Info['RefArrayForPrcntl']
CPCsoilmoist_YYYYMMDD_Of_InfoArray  = CPCsoilmoist_Info['YYYYMMDD_Of_RefArrayForPrcntl']
CPCsoilmoist_InfoArray  = CPCsoilmoist_Info['RefArrayForPrcntl']
USDM_YYYYMMDD_Of_InfoArray  = USDM_Info['YYYYMMDD_Of_InfoArray']
USDM_InfoArray  = USDM_Info['InfoArray']

def GetRealDatesListOfInfoArray(YYYYMMEtc_Of_InfoArray, NumDateElements, VariabNameForErrStr, WhereDayForNumDateElements2):
  # NumDateElements is 2 if YYYYMMEtc is in YYYYMM format, and 3 if in YYYYMMDD format
  # WhereDayForNumDateElements2 is 'mid' if value representative at mid-month, and 'end' if at end-month (e.g., accumulation)
  if NumDateElements == 3:
    Years_Of_InfoArray = YYYYMMEtc_Of_InfoArray // 10000
    Months_Of_InfoArray = (YYYYMMEtc_Of_InfoArray % 10000) // 100
    DaysOfMonth_Of_InfoArray = YYYYMMEtc_Of_InfoArray % 100 
  elif NumDateElements == 2:
    Years_Of_InfoArray = YYYYMMEtc_Of_InfoArray // 100
    Months_Of_InfoArray = YYYYMMEtc_Of_InfoArray % 100
  else:
    print('NumDateElements should be 3 or 2 in GetRealDatesListOfInfoArray for '+VariabNameForErrStr+'!!!')
    sys.exit(0)
  RealDatesList_Of_InfoArray = []
  for ii in range(len(Years_Of_InfoArray)):
    if NumDateElements == 3:
      RealDatesList_Of_InfoArray.append(date(Years_Of_InfoArray[ii,0], Months_Of_InfoArray[ii,0], DaysOfMonth_Of_InfoArray[ii,0])) 
    elif NumDateElements == 2:
      if WhereDayForNumDateElements2 == 'mid':
        RealDatesList_Of_InfoArray.append(date(Years_Of_InfoArray[ii,0], Months_Of_InfoArray[ii,0], 15)) # NOTE 
      elif WhereDayForNumDateElements2 == 'end':
        RealDatesList_Of_InfoArray.append(date(Years_Of_InfoArray[ii,0], Months_Of_InfoArray[ii,0], (monthrange(Years_Of_InfoArray[ii,0], Months_Of_InfoArray[ii,0]))[1])) # NOTE 
      else:
        print('WhereDayForNumDateElements2 should be mid or end in GetRealDatesListOfInfoArray for '+VariabNameForErrStr+'!!!')
        sys.exit(0)
  return RealDatesList_Of_InfoArray
#end of def GetRealDatesListOfInfoArray(YYYYMMEtc_Of_InfoArray, NumDateElements, VariabNameForErrStr, WhereDayForNumDateElements2):

ZIndex_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(ZIndex_YYYYMM_Of_InfoArray, 2, 'ZIndex', 'mid')
ZIndex60month_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(ZIndex60month_YYYYMM_Of_InfoArray, 2, 'ZIndex60month', 'mid')
PMDI_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(PMDI_YYYYMMDD_Of_InfoArray, 3, 'PMDI', np.NaN)
PHDI_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(PHDI_YYYYMMDD_Of_InfoArray, 3, 'PHDI', np.NaN)
Pcpn1month_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(Pcpn1month_YYYYMM_Of_InfoArray, 2, 'Pcpn1month', 'end')
Pcpn3month_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(Pcpn3month_YYYYMM_Of_InfoArray, 2, 'Pcpn3month', 'end')
Pcpn6month_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(Pcpn6month_YYYYMM_Of_InfoArray, 2, 'Pcpn6month', 'end')
Pcpn12month_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(Pcpn12month_YYYYMM_Of_InfoArray, 2, 'Pcpn12month', 'end')
Pcpn24month_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(Pcpn24month_YYYYMM_Of_InfoArray, 2, 'Pcpn24month', 'end')
Pcpn60month_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(Pcpn60month_YYYYMM_Of_InfoArray, 2, 'Pcpn60month', 'end')
CPCsoilmoist_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(CPCsoilmoist_YYYYMMDD_Of_InfoArray, 3, 'CPCsoilmoist', np.NaN)
USDM_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(USDM_YYYYMMDD_Of_InfoArray, 3, 'USDM', np.NaN)

#Begin calculating real dates list for reference arrays
def GetTimeInfoOfRefArray(Ref_BeginDate, Ref_EndDate):
  TotalNumDaysDiff = abs(Ref_EndDate-Ref_BeginDate).days
  TotalNumWeeksDiff = TotalNumDaysDiff//7
  RealDatesList_Of_RefArray = []
  HumanDatesList_Of_RefArray = []
  for NumWeeksDiff in range(0,TotalNumWeeksDiff+1):
    Ref_IntermediateDate = Ref_BeginDate + timedelta(weeks=NumWeeksDiff)
    RealDatesList_Of_RefArray.append(Ref_IntermediateDate)
    HumanDatesList_Of_RefArray.append(10000*Ref_IntermediateDate.year + 100*Ref_IntermediateDate.month + Ref_IntermediateDate.day)
  YYYYMMDD_Of_RefArray = np.array(HumanDatesList_Of_RefArray, dtype = np.int32)
  YYYYMMDD_Of_RefArray = np.expand_dims(YYYYMMDD_Of_RefArray, axis=1)
  return RealDatesList_Of_RefArray, YYYYMMDD_Of_RefArray
#end of def GetTimeInfoOfRefArray(Ref_BeginDate, Ref_EndDate):
ZIndex_RealDatesList_Of_RefArray, ZIndex_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(ZIndex_Ref_BeginDate, ZIndex_Ref_EndDate)
PMDI_RealDatesList_Of_RefArray, PMDI_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(PMDI_Ref_BeginDate, PMDI_Ref_EndDate)
PHDI_RealDatesList_Of_RefArray, PHDI_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(PHDI_Ref_BeginDate, PHDI_Ref_EndDate)
Pcpn_RealDatesList_Of_RefArray, Pcpn_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(Pcpn_Ref_BeginDate, Pcpn_Ref_EndDate)
CPCsoilmoist_RealDatesList_Of_RefArray, CPCsoilmoist_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(CPCsoilmoist_Ref_BeginDate, CPCsoilmoist_Ref_EndDate)
#End calculating real dates list for reference arrays

ZIndex_RefArray = np.empty([ ZIndex_YYYYMMDD_Of_RefArray.shape[0], ZIndex_InfoArray.shape[1]])
ZIndex_RefArray[:] = np.NaN
ZIndex60month_RefArray = np.empty([ ZIndex_YYYYMMDD_Of_RefArray.shape[0], ZIndex60month_InfoArray.shape[1]])
ZIndex60month_RefArray[:] = np.NaN
PMDI_RefArray = np.empty([ PMDI_YYYYMMDD_Of_RefArray.shape[0], PMDI_InfoArray.shape[1]])
PMDI_RefArray[:] = np.NaN
PHDI_RefArray = np.empty([ PHDI_YYYYMMDD_Of_RefArray.shape[0], PHDI_InfoArray.shape[1]])
PHDI_RefArray[:] = np.NaN
Pcpn1month_RefArray = np.empty([ Pcpn_YYYYMMDD_Of_RefArray.shape[0], Pcpn1month_InfoArray.shape[1]])
Pcpn1month_RefArray[:] = np.NaN
Pcpn3month_RefArray = np.empty([ Pcpn_YYYYMMDD_Of_RefArray.shape[0], Pcpn3month_InfoArray.shape[1]])
Pcpn3month_RefArray[:] = np.NaN
Pcpn6month_RefArray = np.empty([ Pcpn_YYYYMMDD_Of_RefArray.shape[0], Pcpn6month_InfoArray.shape[1]])
Pcpn6month_RefArray[:] = np.NaN
Pcpn12month_RefArray = np.empty([ Pcpn_YYYYMMDD_Of_RefArray.shape[0], Pcpn12month_InfoArray.shape[1]])
Pcpn12month_RefArray[:] = np.NaN
Pcpn24month_RefArray = np.empty([ Pcpn_YYYYMMDD_Of_RefArray.shape[0], Pcpn24month_InfoArray.shape[1]])
Pcpn24month_RefArray[:] = np.NaN
Pcpn60month_RefArray = np.empty([ Pcpn_YYYYMMDD_Of_RefArray.shape[0], Pcpn60month_InfoArray.shape[1]])
Pcpn60month_RefArray[:] = np.NaN
CPCsoilmoist_RefArray = np.empty([ CPCsoilmoist_YYYYMMDD_Of_RefArray.shape[0], CPCsoilmoist_InfoArray.shape[1]])
CPCsoilmoist_RefArray[:] = np.NaN

def TimeInterpolateValues(SourceDatesList, DestinationDatesList, SourceArray, DestinationArray):
  for DestinationDateIdx in range(len(DestinationDatesList)):
    ThisDestinationDate = DestinationDatesList[DestinationDateIdx] 
    if ThisDestinationDate in SourceDatesList:
      SourceIdxForThisDest = SourceDatesList.index(ThisDestinationDate) 
      DestinationArray[DestinationDateIdx,:] = SourceArray[SourceIdxForThisDest,:] 
    else:
      DaysDiffList = []
      for ThisSourceDate in SourceDatesList:
        DaysDiffList.append((ThisDestinationDate - ThisSourceDate).days)
      DaysDiffArray = np.array(DaysDiffList)
      SourceLowerIdxForThisDest = np.amax(np.where(DaysDiffArray > 0)) 
      SrcSlice = SourceArray[SourceLowerIdxForThisDest:SourceLowerIdxForThisDest+2,:]
      SrcSlice_isnan = np.isnan(SrcSlice)  
      SrcSlice_isnan_int = SrcSlice_isnan.astype(np.int32)
      SrcSlice_isnan_sum = np.sum(SrcSlice_isnan_int, axis = 0)
      Idxs_NotAllRowsNan = np.where(SrcSlice_isnan_sum < SrcSlice.shape[0])
      if Idxs_NotAllRowsNan[0].size > 0:
        SrcSlice_notnan = ~SrcSlice_isnan 
        SrcSlice_notnan_int = SrcSlice_notnan.astype(np.int32)
        Wt1 = float(-DaysDiffList[SourceLowerIdxForThisDest+1])
        Wt2 = float(DaysDiffList[SourceLowerIdxForThisDest])
        WtsMat = np.repeat(np.array([[Wt1],[Wt2]], dtype = SrcSlice.dtype), repeats = SrcSlice.shape[1], axis = 1) 
  
        Wtd_SrcSlice = np.multiply(SrcSlice, WtsMat)
        BooledWtsMat = np.multiply(WtsMat, SrcSlice_notnan_int)     
        Wtd_SrcSlice_NotAllRowsNan = Wtd_SrcSlice[:, Idxs_NotAllRowsNan[0]]
        BooledWtsMat_NotAllRowsNan = BooledWtsMat[:, Idxs_NotAllRowsNan[0]]
        Sum_Wtd_SrcSlice_NotAllRowsNan = np.nansum(Wtd_SrcSlice_NotAllRowsNan, axis = 0)
        Sum_Wts_NotAllRowsNan = np.nansum(BooledWtsMat_NotAllRowsNan, axis = 0)
        DestinationArray[DestinationDateIdx,Idxs_NotAllRowsNan[0]] = np.divide(Sum_Wtd_SrcSlice_NotAllRowsNan, 
                                                           Sum_Wts_NotAllRowsNan)
      #end of if Idxs_NotAllRowsNan[0].size > 0:
    #end of if ThisDestinationDate in SourceDatesList:
  #end of for DestinationDateIdx in range(len(DestinationDatesList)):
  return DestinationArray
#end of def TimeInterpolateValues(SourceDatesList, DestinationDatesList, SourceArray, DestinationArray):
 
ZIndex_RefArray = TimeInterpolateValues(ZIndex_RealDatesList_Of_InfoArray, ZIndex_RealDatesList_Of_RefArray, ZIndex_InfoArray, ZIndex_RefArray)
ZIndex60month_RefArray = TimeInterpolateValues(ZIndex60month_RealDatesList_Of_InfoArray, ZIndex_RealDatesList_Of_RefArray, ZIndex60month_InfoArray, ZIndex60month_RefArray)
PMDI_RefArray = TimeInterpolateValues(PMDI_RealDatesList_Of_InfoArray, PMDI_RealDatesList_Of_RefArray, PMDI_InfoArray, PMDI_RefArray)
PHDI_RefArray = TimeInterpolateValues(PHDI_RealDatesList_Of_InfoArray, PHDI_RealDatesList_Of_RefArray, PHDI_InfoArray, PHDI_RefArray)
Pcpn1month_RefArray = TimeInterpolateValues(Pcpn1month_RealDatesList_Of_InfoArray, Pcpn_RealDatesList_Of_RefArray, Pcpn1month_InfoArray, Pcpn1month_RefArray)
Pcpn3month_RefArray = TimeInterpolateValues(Pcpn3month_RealDatesList_Of_InfoArray, Pcpn_RealDatesList_Of_RefArray, Pcpn3month_InfoArray, Pcpn3month_RefArray)
Pcpn6month_RefArray = TimeInterpolateValues(Pcpn6month_RealDatesList_Of_InfoArray, Pcpn_RealDatesList_Of_RefArray, Pcpn6month_InfoArray, Pcpn6month_RefArray)
Pcpn12month_RefArray = TimeInterpolateValues(Pcpn12month_RealDatesList_Of_InfoArray, Pcpn_RealDatesList_Of_RefArray, Pcpn12month_InfoArray, Pcpn12month_RefArray)
Pcpn24month_RefArray = TimeInterpolateValues(Pcpn24month_RealDatesList_Of_InfoArray, Pcpn_RealDatesList_Of_RefArray, Pcpn24month_InfoArray, Pcpn24month_RefArray)
Pcpn60month_RefArray = TimeInterpolateValues(Pcpn60month_RealDatesList_Of_InfoArray, Pcpn_RealDatesList_Of_RefArray, Pcpn60month_InfoArray, Pcpn60month_RefArray)

def TimeMeanValues(SourceDatesList, DestinationDatesList, SourceArray, DestinationArray, EndingWindowSizeForMean):
  for DestinationDateIdx in range(len(DestinationDatesList)):
    ThisDestinationDate = DestinationDatesList[DestinationDateIdx] 
    SourceIdxForThisDest = SourceDatesList.index(ThisDestinationDate) 
    if SourceIdxForThisDest >= (EndingWindowSizeForMean - 1):
      DestinationArray[DestinationDateIdx,:] = np.nanmean(
             SourceArray[(SourceIdxForThisDest-(EndingWindowSizeForMean-1)):
                         (SourceIdxForThisDest+1),:], axis = 0) 
    else:
      DestinationArray[DestinationDateIdx,:] = np.nanmean(
             SourceArray[0:SourceIdxForThisDest+1,:], axis = 0) 
    #end of if SourceIdxForThisDest >= (EndingWindowSizeForMean - 1):
  #end of for DestinationDateIdx in range(len(DestinationDatesList)):
  return DestinationArray
#end of def TimeMeanValues(SourceDatesList, DestinationDatesList, SourceArray, DestinationArray, EndingWindowSizeForMean):

CPCsoilmoist_RefArray = TimeMeanValues(CPCsoilmoist_RealDatesList_Of_InfoArray, CPCsoilmoist_RealDatesList_Of_RefArray, CPCsoilmoist_InfoArray, CPCsoilmoist_RefArray, 7)

print("--- %s seconds ---" % (time.time() - start_time))

np.savez_compressed(ZIndex_RefFileName, ZIndex_RefArray = ZIndex_RefArray, ZIndex_YYYYMMDD_Of_RefArray = ZIndex_YYYYMMDD_Of_RefArray)
np.savez_compressed(ZIndex60month_RefFileName, ZIndex60month_RefArray = ZIndex60month_RefArray, ZIndex_YYYYMMDD_Of_RefArray = ZIndex_YYYYMMDD_Of_RefArray)
np.savez_compressed(PMDI_RefFileName, PMDI_RefArray = PMDI_RefArray, PMDI_YYYYMMDD_Of_RefArray = PMDI_YYYYMMDD_Of_RefArray)
np.savez_compressed(PHDI_RefFileName, PHDI_RefArray = PHDI_RefArray, PHDI_YYYYMMDD_Of_RefArray = PHDI_YYYYMMDD_Of_RefArray)
np.savez_compressed(Pcpn1month_RefFileName, Pcpn1month_RefArray = Pcpn1month_RefArray, Pcpn_YYYYMMDD_Of_RefArray = Pcpn_YYYYMMDD_Of_RefArray)
np.savez_compressed(Pcpn3month_RefFileName, Pcpn3month_RefArray = Pcpn3month_RefArray, Pcpn_YYYYMMDD_Of_RefArray = Pcpn_YYYYMMDD_Of_RefArray)
np.savez_compressed(Pcpn6month_RefFileName, Pcpn6month_RefArray = Pcpn6month_RefArray, Pcpn_YYYYMMDD_Of_RefArray = Pcpn_YYYYMMDD_Of_RefArray)
np.savez_compressed(Pcpn12month_RefFileName, Pcpn12month_RefArray = Pcpn12month_RefArray, Pcpn_YYYYMMDD_Of_RefArray = Pcpn_YYYYMMDD_Of_RefArray)
np.savez_compressed(Pcpn24month_RefFileName, Pcpn24month_RefArray = Pcpn24month_RefArray, Pcpn_YYYYMMDD_Of_RefArray = Pcpn_YYYYMMDD_Of_RefArray)
np.savez_compressed(Pcpn60month_RefFileName, Pcpn60month_RefArray = Pcpn60month_RefArray, Pcpn_YYYYMMDD_Of_RefArray = Pcpn_YYYYMMDD_Of_RefArray)
np.savez_compressed(CPCsoilmoist_RefFileName, CPCsoilmoist_RefArray = CPCsoilmoist_RefArray, CPCsoilmoist_YYYYMMDD_Of_RefArray = CPCsoilmoist_YYYYMMDD_Of_RefArray)

print("ZIndex_YYYYMMDD_Of_RefArray.shape is ",ZIndex_YYYYMMDD_Of_RefArray.shape)
print("ZIndex_YYYYMMDD_Of_RefArray is ",ZIndex_YYYYMMDD_Of_RefArray)

print("ZIndex_RefArray.shape is ",ZIndex_RefArray.shape)
print("ZIndex_RefArray is ",ZIndex_RefArray)
print("np.amin(np.isnan(ZIndex_RefArray).sum(axis=0)) is ",np.amin(np.isnan(ZIndex_RefArray).sum(axis=0)))
print("np.amax(np.isnan(ZIndex_RefArray).sum(axis=0)) is ",np.amax(np.isnan(ZIndex_RefArray).sum(axis=0)))
print('overall min is ',np.nanmin(ZIndex_RefArray),', overall max is ',np.nanmax(ZIndex_RefArray))

print("ZIndex60month_RefArray.shape is ",ZIndex60month_RefArray.shape)
print("ZIndex60month_RefArray is ",ZIndex60month_RefArray)
print("np.amin(np.isnan(ZIndex60month_RefArray).sum(axis=0)) is ",np.amin(np.isnan(ZIndex60month_RefArray).sum(axis=0)))
print("np.amax(np.isnan(ZIndex60month_RefArray).sum(axis=0)) is ",np.amax(np.isnan(ZIndex60month_RefArray).sum(axis=0)))
print('overall min is ',np.nanmin(ZIndex60month_RefArray),', overall max is ',np.nanmax(ZIndex60month_RefArray))

print("PMDI_RefArray.shape is ",PMDI_RefArray.shape)
print("PMDI_RefArray is ",PMDI_RefArray)
print("np.amin(np.isnan(PMDI_RefArray).sum(axis=0)) is ",np.amin(np.isnan(PMDI_RefArray).sum(axis=0)))
print("np.amax(np.isnan(PMDI_RefArray).sum(axis=0)) is ",np.amax(np.isnan(PMDI_RefArray).sum(axis=0)))
print('overall min is ',np.nanmin(PMDI_RefArray),', overall max is ',np.nanmax(PMDI_RefArray))

print("PHDI_RefArray.shape is ",PHDI_RefArray.shape)
print("PHDI_RefArray is ",PHDI_RefArray)
print("np.amin(np.isnan(PHDI_RefArray).sum(axis=0)) is ",np.amin(np.isnan(PHDI_RefArray).sum(axis=0)))
print("np.amax(np.isnan(PHDI_RefArray).sum(axis=0)) is ",np.amax(np.isnan(PHDI_RefArray).sum(axis=0)))
print('overall min is ',np.nanmin(PHDI_RefArray),', overall max is ',np.nanmax(PHDI_RefArray))

print("Pcpn1month_RefArray.shape is ",Pcpn1month_RefArray.shape)
print("Pcpn1month_RefArray is ",Pcpn1month_RefArray)
print("np.amin(np.isnan(Pcpn1month_RefArray).sum(axis=0)) is ",np.amin(np.isnan(Pcpn1month_RefArray).sum(axis=0)))
print("np.amax(np.isnan(Pcpn1month_RefArray).sum(axis=0)) is ",np.amax(np.isnan(Pcpn1month_RefArray).sum(axis=0)))
print('overall min is ',np.nanmin(Pcpn1month_RefArray),', overall max is ',np.nanmax(Pcpn1month_RefArray))

print("Pcpn3month_RefArray.shape is ",Pcpn3month_RefArray.shape)
print("Pcpn3month_RefArray is ",Pcpn3month_RefArray)
print("np.amin(np.isnan(Pcpn3month_RefArray).sum(axis=0)) is ",np.amin(np.isnan(Pcpn3month_RefArray).sum(axis=0)))
print("np.amax(np.isnan(Pcpn3month_RefArray).sum(axis=0)) is ",np.amax(np.isnan(Pcpn3month_RefArray).sum(axis=0)))
print('overall min is ',np.nanmin(Pcpn3month_RefArray),', overall max is ',np.nanmax(Pcpn3month_RefArray))

print("Pcpn6month_RefArray.shape is ",Pcpn6month_RefArray.shape)
print("Pcpn6month_RefArray is ",Pcpn6month_RefArray)
print("np.amin(np.isnan(Pcpn6month_RefArray).sum(axis=0)) is ",np.amin(np.isnan(Pcpn6month_RefArray).sum(axis=0)))
print("np.amax(np.isnan(Pcpn6month_RefArray).sum(axis=0)) is ",np.amax(np.isnan(Pcpn6month_RefArray).sum(axis=0)))
print('overall min is ',np.nanmin(Pcpn6month_RefArray),', overall max is ',np.nanmax(Pcpn6month_RefArray))

print("Pcpn12month_RefArray.shape is ",Pcpn12month_RefArray.shape)
print("Pcpn12month_RefArray is ",Pcpn12month_RefArray)
print("np.amin(np.isnan(Pcpn12month_RefArray).sum(axis=0)) is ",np.amin(np.isnan(Pcpn12month_RefArray).sum(axis=0)))
print("np.amax(np.isnan(Pcpn12month_RefArray).sum(axis=0)) is ",np.amax(np.isnan(Pcpn12month_RefArray).sum(axis=0)))
print('overall min is ',np.nanmin(Pcpn12month_RefArray),', overall max is ',np.nanmax(Pcpn12month_RefArray))

print("Pcpn24month_RefArray.shape is ",Pcpn24month_RefArray.shape)
print("Pcpn24month_RefArray is ",Pcpn24month_RefArray)
print("np.amin(np.isnan(Pcpn24month_RefArray).sum(axis=0)) is ",np.amin(np.isnan(Pcpn24month_RefArray).sum(axis=0)))
print("np.amax(np.isnan(Pcpn24month_RefArray).sum(axis=0)) is ",np.amax(np.isnan(Pcpn24month_RefArray).sum(axis=0)))
print('overall min is ',np.nanmin(Pcpn24month_RefArray),', overall max is ',np.nanmax(Pcpn24month_RefArray))

print("Pcpn60month_RefArray.shape is ",Pcpn60month_RefArray.shape)
print("Pcpn60month_RefArray is ",Pcpn60month_RefArray)
print("np.amin(np.isnan(Pcpn60month_RefArray).sum(axis=0)) is ",np.amin(np.isnan(Pcpn60month_RefArray).sum(axis=0)))
print("np.amax(np.isnan(Pcpn60month_RefArray).sum(axis=0)) is ",np.amax(np.isnan(Pcpn60month_RefArray).sum(axis=0)))
print('overall min is ',np.nanmin(Pcpn60month_RefArray),', overall max is ',np.nanmax(Pcpn60month_RefArray))

print("CPCsoilmoist_RefArray.shape is ",CPCsoilmoist_RefArray.shape)
print("CPCsoilmoist_RefArray is ",CPCsoilmoist_RefArray)
print("np.amin(np.isnan(CPCsoilmoist_RefArray).sum(axis=0)) is ",np.amin(np.isnan(CPCsoilmoist_RefArray).sum(axis=0)))
print("np.amax(np.isnan(CPCsoilmoist_RefArray).sum(axis=0)) is ",np.amax(np.isnan(CPCsoilmoist_RefArray).sum(axis=0)))
print('overall min is ',np.nanmin(CPCsoilmoist_RefArray),', overall max is ',np.nanmax(CPCsoilmoist_RefArray))




