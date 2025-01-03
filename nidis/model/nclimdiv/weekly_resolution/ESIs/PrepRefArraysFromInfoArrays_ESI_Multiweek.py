# Coded by Soni Yatheendradas
#         on Nov 16, 2021
from __future__ import division
from datetime import date, datetime, timedelta
import numpy as np

# BEGIN code arguments / editable section

ESI4Week_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/ESI/InfoArrsDailyToMean/ClimDivs/ESI4WeeksMean_20000101To20200530.npz'
ESI12Week_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/ESI/InfoArrsDailyToMean/ClimDivs/ESI12WeeksMean_20000101To20200530.npz'

ESI4Week_Info = np.load(ESI4Week_InfoFilename)
ESI12Week_Info = np.load(ESI12Week_InfoFilename)

ESI4Week_YYYYMMDD_Of_InfoArray  = ESI4Week_Info['YYYYMMDD_Of_InfoArrayForPrcntl']
ESI4Week_InfoArray  = ESI4Week_Info['InfoArrayForPrcntl']
ESI12Week_YYYYMMDD_Of_InfoArray  = ESI12Week_Info['YYYYMMDD_Of_InfoArrayForPrcntl']
ESI12Week_InfoArray  = ESI12Week_Info['InfoArrayForPrcntl']

def FindTuesdayAfter(ThisYYYYMMDD):

  ThisYear = int(round(ThisYYYYMMDD // 10000))
  ThisMonth = int(round((ThisYYYYMMDD - 10000 * ThisYear) // 100))
  ThisDayOfMonth = int(round(ThisYYYYMMDD % 100))

  ThisDateTime = datetime(ThisYear, ThisMonth, ThisDayOfMonth, 0, 0, 0)

  ThisDate = date(ThisYear, ThisMonth, ThisDayOfMonth)

  if ThisDate.weekday() > 1:
    TuesdayAfter_DateTime = ThisDateTime + timedelta(days = (8 - ThisDate.weekday()))
  elif ThisDate.weekday() == 1:
    TuesdayAfter_DateTime = ThisDateTime
  elif ThisDate.weekday() < 1:
    TuesdayAfter_DateTime = ThisDateTime + timedelta(days = (1 + ThisDate.weekday()))

  TuesdayAfter_DateVec = [TuesdayAfter_DateTime.year, TuesdayAfter_DateTime.month, TuesdayAfter_DateTime.day]

  return TuesdayAfter_DateVec

#end of def FindTuesdayAfter(ThisYYYYMMDD)

def FindTuesdayBefore(ThisYYYYMMDD):

  ThisYear = int(round(ThisYYYYMMDD // 10000))
  ThisMonth = int(round((ThisYYYYMMDD - 10000 * ThisYear) // 100))
  ThisDayOfMonth = int(round(ThisYYYYMMDD % 100))

  ThisDateTime = datetime(ThisYear, ThisMonth, ThisDayOfMonth, 0, 0, 0)

  ThisDate = date(ThisYear, ThisMonth, ThisDayOfMonth)

  if ThisDate.weekday() > 1:
    TuesdayBefore_DateTime = ThisDateTime - timedelta(days = (ThisDate.weekday() - 1))
  elif ThisDate.weekday() == 1:
    TuesdayBefore_DateTime = ThisDateTime
  elif ThisDate.weekday() < 1:
    TuesdayBefore_DateTime = ThisDateTime - timedelta(days = (ThisDate.weekday() + 6))

  TuesdayBefore_DateVec = [TuesdayBefore_DateTime.year, TuesdayBefore_DateTime.month, TuesdayBefore_DateTime.day]

  return TuesdayBefore_DateVec

#end of def FindTuesdayBefore(ThisYYYYMMDD)

ESI4Week_Ref_BeginDateVecList = FindTuesdayAfter(ESI4Week_YYYYMMDD_Of_InfoArray[0,0])  # 1Month IMERG beginning year, month, day of month, this is also a Tuesday
ESI4Week_Ref_EndDateVecList = FindTuesdayBefore(ESI4Week_YYYYMMDD_Of_InfoArray[-1,0])  # 1Month IMERG ending year, month, day of month, this is also a Tuesday
ESI12Week_Ref_BeginDateVecList = FindTuesdayAfter(ESI12Week_YYYYMMDD_Of_InfoArray[0,0])  # 2Month IMERG beginning year, month, day of month, this is also a Tuesday
ESI12Week_Ref_EndDateVecList = FindTuesdayBefore(ESI12Week_YYYYMMDD_Of_InfoArray[-1,0])  # 2Month IMERG ending year, month, day of month, this is also a Tuesday

ESI4Week_RefFileName = 'RefArrays/ClimDiv_ESI4Week_'+format(ESI4Week_Ref_BeginDateVecList[0],'04')+format(ESI4Week_Ref_BeginDateVecList[1],'02')+format(ESI4Week_Ref_BeginDateVecList[2],'02')+'To'+format(ESI4Week_Ref_EndDateVecList[0],'04')+format(ESI4Week_Ref_EndDateVecList[1],'02')+format(ESI4Week_Ref_EndDateVecList[2],'02')+'.npz'
ESI12Week_RefFileName = 'RefArrays/ClimDiv_ESI12Week_'+format(ESI12Week_Ref_BeginDateVecList[0],'04')+format(ESI12Week_Ref_BeginDateVecList[1],'02')+format(ESI12Week_Ref_BeginDateVecList[2],'02')+'To'+format(ESI12Week_Ref_EndDateVecList[0],'04')+format(ESI12Week_Ref_EndDateVecList[1],'02')+format(ESI12Week_Ref_EndDateVecList[2],'02')+'.npz'

# END code arguments / editable section

import sys
from calendar import monthrange
import time
import os

start_time = time.time()

ESI4Week_Ref_BeginDate = date(ESI4Week_Ref_BeginDateVecList[0], ESI4Week_Ref_BeginDateVecList[1], ESI4Week_Ref_BeginDateVecList[2])
ESI4Week_Ref_EndDate = date(ESI4Week_Ref_EndDateVecList[0], ESI4Week_Ref_EndDateVecList[1], ESI4Week_Ref_EndDateVecList[2])
ESI12Week_Ref_BeginDate = date(ESI12Week_Ref_BeginDateVecList[0], ESI12Week_Ref_BeginDateVecList[1], ESI12Week_Ref_BeginDateVecList[2])
ESI12Week_Ref_EndDate = date(ESI12Week_Ref_EndDateVecList[0], ESI12Week_Ref_EndDateVecList[1], ESI12Week_Ref_EndDateVecList[2])

#BEGIN check whether the beginning and ending days are indeed Tuesdays
if ESI4Week_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for ESI4Week_Ref needs to be a Tuesday!!')
  sys.exit(0)
if ESI4Week_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for ESI4Week_Ref needs to be a Tuesday!!')
  sys.exit(0)
if ESI12Week_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for ESI12Week_Ref needs to be a Tuesday!!')
  sys.exit(0)
if ESI12Week_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for ESI12Week_Ref needs to be a Tuesday!!')
  sys.exit(0)
#END check whether the beginning and ending days are indeed Tuesdays

if ESI4Week_Ref_BeginDate > ESI4Week_Ref_EndDate:
  print('ESI4Week_Ref_BeginDate should not be later than ESI4Week_Ref_EndDate!!!')
  sys.exit(0)
if ESI12Week_Ref_BeginDate > ESI12Week_Ref_EndDate:
  print('ESI12Week_Ref_BeginDate should not be later than ESI12Week_Ref_EndDate!!!')
  sys.exit(0)

#BEGIN section for time-interpolating info arrays to desired temporal resolution

def GetRealDatesListOfInfoArray(YYYYMMEtc_Of_InfoArray, NumDateElements, VariabNameForErrStr, WhereDayForNumDateElements2):
  # NumDateElements is 2 if YYYYMMEtc is in YYYYMM format, and 3 if in YYYYMMDD format
  # WhereDayForNumDateElements2 is 'begin' if value representative at month-beginning, 'mid' if value representative at mid-month, and 'end' if at end-month (e.g., accumulation)
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
      elif WhereDayForNumDateElements2 == 'begin':
        RealDatesList_Of_InfoArray.append(date(Years_Of_InfoArray[ii,0], Months_Of_InfoArray[ii,0], 1))
      else:
        print('WhereDayForNumDateElements2 should be mid or end in GetRealDatesListOfInfoArray for '+VariabNameForErrStr+'!!!')
        sys.exit(0)
  return RealDatesList_Of_InfoArray
#end of def GetRealDatesListOfInfoArray(YYYYMMEtc_Of_InfoArray, NumDateElements, VariabNameForErrStr, WhereDayForNumDateElements2):

ESI4Week_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(ESI4Week_YYYYMMDD_Of_InfoArray, 3, 'ESI4Week', np.NaN)
ESI12Week_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(ESI12Week_YYYYMMDD_Of_InfoArray, 3, 'ESI12Week', np.NaN)

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

ESI4Week_RealDatesList_Of_RefArray, ESI4Week_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(ESI4Week_Ref_BeginDate, ESI4Week_Ref_EndDate)
ESI12Week_RealDatesList_Of_RefArray, ESI12Week_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(ESI12Week_Ref_BeginDate, ESI12Week_Ref_EndDate)

#End calculating real dates list for reference arrays

ESI4Week_RefArray = np.empty([ ESI4Week_YYYYMMDD_Of_RefArray.shape[0], ESI4Week_InfoArray.shape[1]])
ESI4Week_RefArray[:] = np.NaN
ESI12Week_RefArray = np.empty([ ESI12Week_YYYYMMDD_Of_RefArray.shape[0], ESI12Week_InfoArray.shape[1]])
ESI12Week_RefArray[:] = np.NaN

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

ESI4Week_RefArray = TimeMeanValues(ESI4Week_RealDatesList_Of_InfoArray, ESI4Week_RealDatesList_Of_RefArray, ESI4Week_InfoArray, ESI4Week_RefArray, 7)
ESI12Week_RefArray = TimeMeanValues(ESI12Week_RealDatesList_Of_InfoArray, ESI12Week_RealDatesList_Of_RefArray, ESI12Week_InfoArray, ESI12Week_RefArray, 7)

print("--- %s seconds ---" % (time.time() - start_time))

np.savez_compressed(ESI4Week_RefFileName, ESI4Week_RefArray = ESI4Week_RefArray, ESI4Week_YYYYMMDD_Of_RefArray = ESI4Week_YYYYMMDD_Of_RefArray)
np.savez_compressed(ESI12Week_RefFileName, ESI12Week_RefArray = ESI12Week_RefArray, ESI12Week_YYYYMMDD_Of_RefArray = ESI12Week_YYYYMMDD_Of_RefArray)

print("ESI4Week_YYYYMMDD_Of_RefArray is ",ESI4Week_YYYYMMDD_Of_RefArray)

print("ESI4Week_RefArray.shape is ",ESI4Week_RefArray.shape)
print("ESI4Week_RefArray is ",ESI4Week_RefArray)
print("np.amin(np.isnan(ESI4Week_RefArray).sum(axis=0)) is ",np.amin(np.isnan(ESI4Week_RefArray).sum(axis=0)))
print("np.amax(np.isnan(ESI4Week_RefArray).sum(axis=0)) is ",np.amax(np.isnan(ESI4Week_RefArray).sum(axis=0)))
print("np.amin(np.isnan(ESI4Week_RefArray).sum(axis=1)) is ",np.amin(np.isnan(ESI4Week_RefArray).sum(axis=1)))
print("np.amax(np.isnan(ESI4Week_RefArray).sum(axis=1)) is ",np.amax(np.isnan(ESI4Week_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(ESI4Week_RefArray),', overall max is ',np.nanmax(ESI4Week_RefArray))

print("ESI12Week_YYYYMMDD_Of_RefArray.shape is ",ESI12Week_YYYYMMDD_Of_RefArray.shape)
print("ESI12Week_YYYYMMDD_Of_RefArray is ",ESI12Week_YYYYMMDD_Of_RefArray)

print("ESI12Week_RefArray.shape is ",ESI12Week_RefArray.shape)
print("ESI12Week_RefArray is ",ESI12Week_RefArray)
print("np.amin(np.isnan(ESI12Week_RefArray).sum(axis=0)) is ",np.amin(np.isnan(ESI12Week_RefArray).sum(axis=0)))
print("np.amax(np.isnan(ESI12Week_RefArray).sum(axis=0)) is ",np.amax(np.isnan(ESI12Week_RefArray).sum(axis=0)))
print("np.amin(np.isnan(ESI12Week_RefArray).sum(axis=1)) is ",np.amin(np.isnan(ESI12Week_RefArray).sum(axis=1)))
print("np.amax(np.isnan(ESI12Week_RefArray).sum(axis=1)) is ",np.amax(np.isnan(ESI12Week_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(ESI12Week_RefArray),', overall max is ',np.nanmax(ESI12Week_RefArray))



