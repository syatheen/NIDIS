# Coded by Soni Yatheendradas
#         on Mar 1, 2021
from __future__ import division
import sys
#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        EDDI_WhichPastPeriod
#ArgNum   1

# BEGIN code arguments / editable section

EDDI_InfoFilesDir = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/EDDI/RefPctlArrsDaily/'

EDDI_WhichPastPeriod = sys.argv[1] # Choices range from '01wk' till '12wk' in 1-week increments, and '01mn' till '12mn' in 1-month increments

EDDI_InfoFiles_BeginYear = 1980 # Begins [1980, 1, 1]
EDDI_InfoFiles_EndYear = 2020 # Ends [2020, 12, 31]

EDDI_Ref_BeginDateVecList = [1980, 1, 8]  # EDDI beginning year, month, day of month, this is also a Tuesday
#EDDI_Ref_EndDateVecList = [2020, 8, 25]  # EDDI ending year, month, day of month, this is also a Tuesday
EDDI_Ref_EndDateVecList = [2020, 12, 29]  # EDDI ending year, month, day of month, this is also a Tuesday

EDDI_RefFileName = 'RefArrays/ClimDiv_EDDI_'+EDDI_WhichPastPeriod+'_'+format(EDDI_Ref_BeginDateVecList[0],'04')+format(EDDI_Ref_BeginDateVecList[1],'02')+format(EDDI_Ref_BeginDateVecList[2],'02')+'To'+format(EDDI_Ref_EndDateVecList[0],'04')+format(EDDI_Ref_EndDateVecList[1],'02')+format(EDDI_Ref_EndDateVecList[2],'02')+'.npz'

# END code arguments / editable section

from datetime import date, datetime, timedelta
#import sys
import numpy as np
from calendar import monthrange
import time

start_time = time.time()

EDDI_Ref_BeginDate = date(EDDI_Ref_BeginDateVecList[0], EDDI_Ref_BeginDateVecList[1], EDDI_Ref_BeginDateVecList[2])
EDDI_Ref_EndDate = date(EDDI_Ref_EndDateVecList[0], EDDI_Ref_EndDateVecList[1], EDDI_Ref_EndDateVecList[2])

#BEGIN check whether the beginning and ending days are indeed Tuesdays
if EDDI_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for EDDI_Ref needs to be a Tuesday!!')
  sys.exit(0)
if EDDI_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for EDDI_Ref needs to be a Tuesday!!')
  sys.exit(0)
#END check whether the beginning and ending days are indeed Tuesdays

if EDDI_Ref_BeginDate > EDDI_Ref_EndDate:
  print('EDDI_Ref_BeginDate should not be later than EDDI_Ref_EndDate!!!')
  sys.exit(0)

#BEGIN section for time-interpolating info arrays to desired temporal resolution

for ThisYear in range(EDDI_InfoFiles_BeginYear, EDDI_InfoFiles_EndYear+1, 1):
  if EDDI_WhichPastPeriod == '01wk':
    ThisYear_EDDI_Info = np.load(EDDI_InfoFilesDir+format(ThisYear, '04')+'.npz')
  else:
    ThisYear_EDDI_Info = np.load(EDDI_InfoFilesDir+format(ThisYear, '04')+'_'+EDDI_WhichPastPeriod+'.npz')
  ThisYear_EDDI_YYYYMMDD_Of_InfoArray = ThisYear_EDDI_Info['YYYYMMDD_Of_RefArrayForPrcntl']
  ThisYear_EDDI_InfoArray  = ThisYear_EDDI_Info['RefArrayForPrcntl']
  if ThisYear == EDDI_InfoFiles_BeginYear:
    EDDI_YYYYMMDD_Of_InfoArray = np.copy(ThisYear_EDDI_YYYYMMDD_Of_InfoArray)
    EDDI_InfoArray = np.copy(ThisYear_EDDI_InfoArray)
  else:
    EDDI_YYYYMMDD_Of_InfoArray = np.concatenate((EDDI_YYYYMMDD_Of_InfoArray, ThisYear_EDDI_YYYYMMDD_Of_InfoArray), axis = 0)
    EDDI_InfoArray = np.concatenate((EDDI_InfoArray, ThisYear_EDDI_InfoArray), axis = 0)
  #end of if ThisYear == EDDI_InfoFiles_BeginYear
#end of for ThisYear in range(EDDI_InfoFiles_BeginYear, EDDI_InfoFiles_EndYear+1, 1)

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

EDDI_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(EDDI_YYYYMMDD_Of_InfoArray, 3, 'EDDI', np.NaN)

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
EDDI_RealDatesList_Of_RefArray, EDDI_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(EDDI_Ref_BeginDate, EDDI_Ref_EndDate)
#End calculating real dates list for reference arrays

EDDI_RefArray = np.empty([ EDDI_YYYYMMDD_Of_RefArray.shape[0], EDDI_InfoArray.shape[1]])
EDDI_RefArray[:] = np.NaN

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

EDDI_RefArray = TimeMeanValues(EDDI_RealDatesList_Of_InfoArray, EDDI_RealDatesList_Of_RefArray, EDDI_InfoArray, EDDI_RefArray, 7)

print("--- %s seconds ---" % (time.time() - start_time))

np.savez_compressed(EDDI_RefFileName, EDDI_RefArray = EDDI_RefArray, EDDI_YYYYMMDD_Of_RefArray = EDDI_YYYYMMDD_Of_RefArray)

print("EDDI_YYYYMMDD_Of_RefArray.shape is ",EDDI_YYYYMMDD_Of_RefArray.shape)
print("EDDI_YYYYMMDD_Of_RefArray is ",EDDI_YYYYMMDD_Of_RefArray)

print("EDDI_RefArray.shape is ",EDDI_RefArray.shape)
print("EDDI_RefArray is ",EDDI_RefArray)
print("np.amin(np.isnan(EDDI_RefArray).sum(axis=0)) is ",np.amin(np.isnan(EDDI_RefArray).sum(axis=0)))
print("np.amax(np.isnan(EDDI_RefArray).sum(axis=0)) is ",np.amax(np.isnan(EDDI_RefArray).sum(axis=0)))
print('overall min is ',np.nanmin(EDDI_RefArray),', overall max is ',np.nanmax(EDDI_RefArray))




