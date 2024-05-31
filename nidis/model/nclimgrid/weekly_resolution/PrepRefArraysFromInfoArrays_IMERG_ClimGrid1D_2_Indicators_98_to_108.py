#!/usr/bin/env python
# Coded by Soni Yatheendradas
#         on Nov 3, 2023
from __future__ import division
from datetime import date, datetime, timedelta
import numpy as np
import sys
#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        NumMonthsStr 
#ArgNum   1      

# BEGIN code arguments / editable section

NumMonthsStr = sys.argv[1] # Choices are '1Month', '2Month', '3Month', '6Month', '9Month', '12Month', '24Month', '36Month', '48Month', '60Month', '72Month' 

if NumMonthsStr == '1Month':
  IMERG_nMonth_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimGrid1D/IMERG1MonthsMean_20000630To20210531.npz'
elif NumMonthsStr == '2Month':
  IMERG_nMonth_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimGrid1D/IMERG2MonthsMean_20000730To20210531.npz'
elif NumMonthsStr == '3Month':
  IMERG_nMonth_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimGrid1D/IMERG3MonthsMean_20000829To20210531.npz'
elif NumMonthsStr == '6Month':
  IMERG_nMonth_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimGrid1D/IMERG6MonthsMean_20001127To20210531.npz'
elif NumMonthsStr == '9Month':
  IMERG_nMonth_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimGrid1D/IMERG9MonthsMean_20010225To20210531.npz'
elif NumMonthsStr == '12Month':
  IMERG_nMonth_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimGrid1D/IMERG12MonthsMean_20010531To20210531.npz'
elif NumMonthsStr == '24Month':
  IMERG_nMonth_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimGrid1D/IMERG24MonthsMean_20020531To20210531.npz'
elif NumMonthsStr == '36Month':
  IMERG_nMonth_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimGrid1D/IMERG36MonthsMean_20030531To20210531.npz'
elif NumMonthsStr == '48Month':
  IMERG_nMonth_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimGrid1D/IMERG48MonthsMean_20040531To20210531.npz'
elif NumMonthsStr == '60Month':
  IMERG_nMonth_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimGrid1D/IMERG60MonthsMean_20050531To20210531.npz'
elif NumMonthsStr == '72Month':
  IMERG_nMonth_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimGrid1D/IMERG72MonthsMean_20060531To20210531.npz'
#end of if NumMonthsStr == '1Month'

IMERG_nMonth_Info = np.load(IMERG_nMonth_InfoFilename)

IMERG_nMonth_YYYYMMDD_Of_InfoArray  = IMERG_nMonth_Info['YYYYMMDD_Of_InfoArrayForPrcntl']
IMERG_nMonth_InfoArray  = IMERG_nMonth_Info['InfoArrayForPrcntl']

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

IMERG_nMonth_Ref_BeginDateVecList = FindTuesdayAfter(IMERG_nMonth_YYYYMMDD_Of_InfoArray[0,0])  # 1Month IMERG beginning year, month, day of month, this is also a Tuesday
IMERG_nMonth_Ref_EndDateVecList = FindTuesdayBefore(IMERG_nMonth_YYYYMMDD_Of_InfoArray[-1,0])  # 1Month IMERG ending year, month, day of month, this is also a Tuesday

IMERG_nMonth_RefFileName = 'RefArrays/ClimGrid1D_IMERG'+NumMonthsStr+'_'+format(IMERG_nMonth_Ref_BeginDateVecList[0],'04')+format(IMERG_nMonth_Ref_BeginDateVecList[1],'02')+format(IMERG_nMonth_Ref_BeginDateVecList[2],'02')+'To'+format(IMERG_nMonth_Ref_EndDateVecList[0],'04')+format(IMERG_nMonth_Ref_EndDateVecList[1],'02')+format(IMERG_nMonth_Ref_EndDateVecList[2],'02')+'.npz'

# END code arguments / editable section

#np.set_printoptions(threshold=np.inf)
from calendar import monthrange
import time
import os

start_time = time.time()

IMERG_nMonth_Ref_BeginDate = date(IMERG_nMonth_Ref_BeginDateVecList[0], IMERG_nMonth_Ref_BeginDateVecList[1], IMERG_nMonth_Ref_BeginDateVecList[2])
IMERG_nMonth_Ref_EndDate = date(IMERG_nMonth_Ref_EndDateVecList[0], IMERG_nMonth_Ref_EndDateVecList[1], IMERG_nMonth_Ref_EndDateVecList[2])

#BEGIN check whether the beginning and ending days are indeed Tuesdays
if IMERG_nMonth_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for IMERG_nMonth_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG_nMonth_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for IMERG_nMonth_Ref needs to be a Tuesday!!')
  sys.exit(0)
#END check whether the beginning and ending days are indeed Tuesdays

if IMERG_nMonth_Ref_BeginDate > IMERG_nMonth_Ref_EndDate:
  print('IMERG_nMonth_Ref_BeginDate should not be later than IMERG_nMonth_Ref_EndDate!!!')
  sys.exit(0)
#end of if IMERG_nMonth_Ref_BeginDate > IMERG_nMonth_Ref_EndDate

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
      elif WhereDayForNumDateElements2 == 'begin':
        RealDatesList_Of_InfoArray.append(date(Years_Of_InfoArray[ii,0], Months_Of_InfoArray[ii,0], 1))
      else:
        print('WhereDayForNumDateElements2 should be mid or end in GetRealDatesListOfInfoArray for '+VariabNameForErrStr+'!!!')
        sys.exit(0)
  return RealDatesList_Of_InfoArray
#end of def GetRealDatesListOfInfoArray(YYYYMMEtc_Of_InfoArray, NumDateElements, VariabNameForErrStr, WhereDayForNumDateElements2):

IMERG_nMonth_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(IMERG_nMonth_YYYYMMDD_Of_InfoArray, 3, 'IMERG' + NumMonthsStr, np.NaN)

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

IMERG_nMonth_RealDatesList_Of_RefArray, IMERG_nMonth_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(IMERG_nMonth_Ref_BeginDate, IMERG_nMonth_Ref_EndDate)

#End calculating real dates list for reference arrays

IMERG_nMonth_RefArray = np.empty([ IMERG_nMonth_YYYYMMDD_Of_RefArray.shape[0], IMERG_nMonth_InfoArray.shape[1]])
IMERG_nMonth_RefArray[:] = np.NaN

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

IMERG_nMonth_RefArray = TimeMeanValues(IMERG_nMonth_RealDatesList_Of_InfoArray, IMERG_nMonth_RealDatesList_Of_RefArray, IMERG_nMonth_InfoArray, IMERG_nMonth_RefArray, 7)

print("--- %s seconds ---" % (time.time() - start_time))

np.savez_compressed(IMERG_nMonth_RefFileName, IMERG_nMonth_RefArray = IMERG_nMonth_RefArray, IMERG_nMonth_YYYYMMDD_Of_RefArray = IMERG_nMonth_YYYYMMDD_Of_RefArray)

def PrintArrayInfo_3(ThisArray, ThisArray_Str, VariabNameStr):
  print('')
  print('For '+VariabNameStr+":")
  print(ThisArray_Str, ".shape is ",ThisArray.shape)
  print(ThisArray_Str, " is ", ThisArray)
  print("np.amin(np.isnan(", ThisArray_Str, ").sum(axis=0)) is ",np.amin(np.isnan(ThisArray).sum(axis=0)))
  print("np.amax(np.isnan(", ThisArray_Str, ").sum(axis=0)) is ",np.amax(np.isnan(ThisArray).sum(axis=0)))
  print("np.amin(np.isnan(", ThisArray_Str, ").sum(axis=1)) is ",np.amin(np.isnan(ThisArray).sum(axis=1)))
  print("np.amax(np.isnan(", ThisArray_Str, ").sum(axis=1)) is ",np.amax(np.isnan(ThisArray).sum(axis=1)))
  print("np.isnan(np.nansum(", ThisArray_Str, ", axis = 0)).sum() is ",np.isnan(np.nansum(ThisArray, axis = 0)).sum())
  print("np.isnan(np.nansum(", ThisArray_Str, ", axis = 1)).sum() is ",np.isnan(np.nansum(ThisArray, axis = 1)).sum())
  print('overall min is ',np.nanmin(ThisArray),', overall max is ',np.nanmax(ThisArray))
  print('')
#end of def PrintArrayInfo_3(ThisArray, ThisArray_Str, VariabNameStr)

PrintArrayInfo_3(IMERG_nMonth_YYYYMMDD_Of_RefArray, 'IMERG_nMonth_YYYYMMDD_Of_RefArray', 'IMERG_nMonth_YYYYMMDD')

PrintArrayInfo_3(IMERG_nMonth_RefArray, 'IMERG_nMonth_RefArray', 'IMERG_nMonth')


