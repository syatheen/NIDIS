# BEGIN code arguments / editable section

ESA_CCI_InfoFilesDir = '/discover/nobackup/projects/nca/syatheen/ESA_CCI_Npzs/'

ESA_CCI_InfoFiles_BeginYYYYMMVecList = [1978, 11]
ESA_CCI_InfoFiles_EndYYYYMMVecList = [2020, 12]

ESA_CCI_Ref_BeginDateVecList = [1978, 11, 7]  # ESA_CCI beginning year, month, day of month, this is also a Tuesday
ESA_CCI_Ref_EndDateVecList = [2020, 12, 29]  # ESA_CCI ending year, month, day of month, this is also a Tuesday

ESA_CCI_RefFileName = 'RefArrays/ClimDiv_ESA_CCI_'+format(ESA_CCI_Ref_BeginDateVecList[0],'04')+format(ESA_CCI_Ref_BeginDateVecList[1],'02')+format(ESA_CCI_Ref_BeginDateVecList[2],'02')+'To'+format(ESA_CCI_Ref_EndDateVecList[0],'04')+format(ESA_CCI_Ref_EndDateVecList[1],'02')+format(ESA_CCI_Ref_EndDateVecList[2],'02')+'.npz'

# END code arguments / editable section

from datetime import date, datetime, timedelta
import sys
import numpy as np
from calendar import monthrange
import time
import os

start_time = time.time()

ESA_CCI_Ref_BeginDate = date(ESA_CCI_Ref_BeginDateVecList[0], ESA_CCI_Ref_BeginDateVecList[1], ESA_CCI_Ref_BeginDateVecList[2])
ESA_CCI_Ref_EndDate = date(ESA_CCI_Ref_EndDateVecList[0], ESA_CCI_Ref_EndDateVecList[1], ESA_CCI_Ref_EndDateVecList[2])

#BEGIN check whether the beginning and ending days are indeed Tuesdays
if ESA_CCI_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for ESA_CCI_Ref needs to be a Tuesday!!')
  sys.exit(0)
if ESA_CCI_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for ESA_CCI_Ref needs to be a Tuesday!!')
  sys.exit(0)
#END check whether the beginning and ending days are indeed Tuesdays

if ESA_CCI_Ref_BeginDate > ESA_CCI_Ref_EndDate:
  print('ESA_CCI_Ref_BeginDate should not be later than ESA_CCI_Ref_EndDate!!!')
  sys.exit(0)

#BEGIN section for concatenating monthly-containing-daily Arrays

for WhichYear in range(ESA_CCI_InfoFiles_BeginYYYYMMVecList[0], ESA_CCI_InfoFiles_EndYYYYMMVecList[0]+1):

  if WhichYear == ESA_CCI_InfoFiles_BeginYYYYMMVecList[0]:
    BeginMonth = ESA_CCI_InfoFiles_BeginYYYYMMVecList[1]
  else:
    BeginMonth = 1
  #end of if WhichYear == ESA_CCI_InfoFiles_BeginYYYYMMVecList[0]

  if WhichYear == ESA_CCI_InfoFiles_EndYYYYMMVecList[0]:
    EndMonth = ESA_CCI_InfoFiles_EndYYYYMMVecList[1]
  else:
    EndMonth = 12
  #end of if WhichYear == ESA_CCI_InfoFiles_EndYYYYMMVecList[0]

  for WhichMonth in range(BeginMonth, EndMonth+1):

    ThisYYYYMM_Info = np.load(ESA_CCI_InfoFilesDir + 'ESA_CCI_' + format(WhichYear, '04') + format(WhichMonth, '02') + '_ClimDivs.npz')

    ThisYYYYMMDD_Of_InfoArrayForPrcntl = ThisYYYYMM_Info['YYYYMMDD_Of_RefArrayForPrcntl']
    ThisInfoArrayForPrcntl = ThisYYYYMM_Info['RefArrayForPrcntl']

    if ( (WhichYear == ESA_CCI_InfoFiles_BeginYYYYMMVecList[0]) and
         (WhichMonth == ESA_CCI_InfoFiles_BeginYYYYMMVecList[1]) ):
      ESA_CCI_YYYYMMDD_Of_InfoArray = np.copy(ThisYYYYMMDD_Of_InfoArrayForPrcntl)
      ESA_CCI_InfoArray = np.copy(ThisInfoArrayForPrcntl)
    else: #of if ( (WhichYear == ESA_CCI_InfoFiles_BeginYYYYMMVecList[0]) and....
      ESA_CCI_YYYYMMDD_Of_InfoArray = np.concatenate((ESA_CCI_YYYYMMDD_Of_InfoArray, ThisYYYYMMDD_Of_InfoArrayForPrcntl), axis = 0)
      ESA_CCI_InfoArray = np.concatenate((ESA_CCI_InfoArray, ThisInfoArrayForPrcntl), axis = 0)
    #end of if ( (WhichYear == ESA_CCI_InfoFiles_BeginYYYYMMVecList[0]) and....

  #end of for WhichMonth in range(BeginMonth, EndMonth+1)

#end of for WhichYear in range(ESA_CCI_InfoFiles_BeginYYYYMMVecList[0], ESA_CCI_InfoFiles_EndYYYYMMVecList[0]+1)

#END section for concatenating monthly-containing-daily Arrays

#BEGIN section for time-interpolating info arrays to desired temporal resolution

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

ESA_CCI_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(ESA_CCI_YYYYMMDD_Of_InfoArray, 3, 'ESA_CCI', np.NaN)

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

ESA_CCI_RealDatesList_Of_RefArray, ESA_CCI_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(ESA_CCI_Ref_BeginDate, ESA_CCI_Ref_EndDate)

#End calculating real dates list for reference arrays

ESA_CCI_RefArray = np.empty([ ESA_CCI_YYYYMMDD_Of_RefArray.shape[0], ESA_CCI_InfoArray.shape[1]])
ESA_CCI_RefArray[:] = np.NaN

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

ESA_CCI_RefArray = TimeMeanValues(ESA_CCI_RealDatesList_Of_InfoArray, ESA_CCI_RealDatesList_Of_RefArray, ESA_CCI_InfoArray, ESA_CCI_RefArray, 7)

print("--- %s seconds ---" % (time.time() - start_time))

np.savez_compressed(ESA_CCI_RefFileName, ESA_CCI_RefArray = ESA_CCI_RefArray, ESA_CCI_YYYYMMDD_Of_RefArray = ESA_CCI_YYYYMMDD_Of_RefArray)

print("ESA_CCI_YYYYMMDD_Of_RefArray.shape is ",ESA_CCI_YYYYMMDD_Of_RefArray.shape)
print("ESA_CCI_YYYYMMDD_Of_RefArray is ",ESA_CCI_YYYYMMDD_Of_RefArray)

print("ESA_CCI_RefArray.shape is ",ESA_CCI_RefArray.shape)
print("ESA_CCI_RefArray is ",ESA_CCI_RefArray)
print("np.amin(np.isnan(ESA_CCI_RefArray).sum(axis=0)) is ",np.amin(np.isnan(ESA_CCI_RefArray).sum(axis=0)))
print("np.amax(np.isnan(ESA_CCI_RefArray).sum(axis=0)) is ",np.amax(np.isnan(ESA_CCI_RefArray).sum(axis=0)))
print("np.amin(np.isnan(ESA_CCI_RefArray).sum(axis=1)) is ",np.amin(np.isnan(ESA_CCI_RefArray).sum(axis=1)))
print("np.amax(np.isnan(ESA_CCI_RefArray).sum(axis=1)) is ",np.amax(np.isnan(ESA_CCI_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(ESA_CCI_RefArray),', overall max is ',np.nanmax(ESA_CCI_RefArray))

