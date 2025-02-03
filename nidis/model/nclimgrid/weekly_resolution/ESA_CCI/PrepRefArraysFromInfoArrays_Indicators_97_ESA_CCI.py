#!/usr/bin/env python
# Coded by Soni Yatheendradas
#         on Feb 21, 2023

from __future__ import division
import os
import sys
import time
import logging
import numpy as np
import pandas as pd
from calendar import monthrange
from datetime import date, datetime, timedelta
from multiprocessing import Pool, cpu_count

def ConcatMonthlyArraysContainingDailyInfo(ESA_CCI_Info_BeginYYYYMMVecList, ESA_CCI_Info_EndYYYYMMVecList, InfoFilesDir):

  for WhichYear in range(ESA_CCI_Info_BeginYYYYMMVecList[0], ESA_CCI_Info_EndYYYYMMVecList[0]+1):
  
    if WhichYear == ESA_CCI_Info_BeginYYYYMMVecList[0]:
      BeginMonth = ESA_CCI_Info_BeginYYYYMMVecList[1]
    else:
      BeginMonth = 1
    #end of if WhichYear == ESA_CCI_Info_BeginYYYYMMVecList[0]
  
    if WhichYear == ESA_CCI_Info_EndYYYYMMVecList[0]:
      EndMonth = ESA_CCI_Info_EndYYYYMMVecList[1]
    else:
      EndMonth = 12
    #end of if WhichYear == ESA_CCI_Info_EndYYYYMMVecList[0]
  
    for WhichMonth in range(BeginMonth, EndMonth+1):

      ThisYYYYMM_Info = np.load(InfoFilesDir + 'ESA_CCI_' + format(WhichYear, '04') + format(WhichMonth, '02') + '_ClimGrid1D.npz')
      ThisYYYYMMDD_Of_InfoArrayForPrcntl = ThisYYYYMM_Info['YYYYMMDD_Of_RefArrayForPrcntl']
      ThisInfoArrayForPrcntl = ThisYYYYMM_Info['RefArrayForPrcntl']
  
      if ( (WhichYear == ESA_CCI_Info_BeginYYYYMMVecList[0]) and
           (WhichMonth == ESA_CCI_Info_BeginYYYYMMVecList[1]) ):
        ESA_CCI_YYYYMMDD_Of_InfoArray = np.copy(ThisYYYYMMDD_Of_InfoArrayForPrcntl)
        ESA_CCI_InfoArray = np.copy(ThisInfoArrayForPrcntl)
      else: #of if ( (WhichYear == ESA_CCI_Info_BeginYYYYMMVecList[0]) and....
        ESA_CCI_YYYYMMDD_Of_InfoArray = np.concatenate((ESA_CCI_YYYYMMDD_Of_InfoArray, ThisYYYYMMDD_Of_InfoArrayForPrcntl), axis = 0)
        ESA_CCI_InfoArray = np.concatenate((ESA_CCI_InfoArray, ThisInfoArrayForPrcntl), axis = 0)
      #end of if ( (WhichYear == ESA_CCI_Info_BeginYYYYMMVecList[0]) and....
  
    #end of for WhichMonth in range(BeginMonth, EndMonth+1)
  
  #end of for WhichYear in range(ESA_CCI_Info_BeginYYYYMMVecList[0], ESA_CCI_Info_EndYYYYMMVecList[0]+1)

  return ESA_CCI_YYYYMMDD_Of_InfoArray, ESA_CCI_InfoArray

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

def PrintArrayInfo(ThisArray, VariabNameStr):
  print('')
  print('For '+VariabNameStr+":")
  print("ThisArray.shape is ",ThisArray.shape)
  print("ThisArray is ",ThisArray)
  print("np.amin(np.isnan(ThisArray).sum(axis=0)) is ",np.amin(np.isnan(ThisArray).sum(axis=0)))
  print("np.amax(np.isnan(ThisArray).sum(axis=0)) is ",np.amax(np.isnan(ThisArray).sum(axis=0)))
  print("np.amin(np.isnan(ThisArray).sum(axis=1)) is ",np.amin(np.isnan(ThisArray).sum(axis=1)))
  print("np.amax(np.isnan(ThisArray).sum(axis=1)) is ",np.amax(np.isnan(ThisArray).sum(axis=1)))
  print("np.isnan(np.nansum(ThisArray, axis = 0)).sum() is ",np.isnan(np.nansum(ThisArray, axis = 0)).sum())
  print("np.isnan(np.nansum(ThisArray, axis = 1)).sum() is ",np.isnan(np.nansum(ThisArray, axis = 1)).sum())
  print('overall min is ',np.nanmin(ThisArray),', overall max is ',np.nanmax(ThisArray))
  print('')
  return


def main():

    # needs the / at the end because of concatenation
    # move to os.path.join to remove this dependency
    InfoFilesDir = '/discover/nobackup/projects/nca/syatheen/ESA_CCI_Npzs/'

    ESA_CCI_Info_BeginYYYYMMVecList = [1978, 11] # Beginning year and month 
    ESA_CCI_Info_EndYYYYMMVecList = [2020, 12] # Ending year and month 

    ESA_CCI_YYYYMMDD_Of_InfoArray, ESA_CCI_InfoArray = ConcatMonthlyArraysContainingDailyInfo(ESA_CCI_Info_BeginYYYYMMVecList, ESA_CCI_Info_EndYYYYMMVecList, InfoFilesDir)

    ESA_CCI_Ref_BeginDateVecList = FindTuesdayAfter(ESA_CCI_YYYYMMDD_Of_InfoArray[0,0])  # ESA_CCI beginning year, month, day of month, this is also a Tuesday
    ESA_CCI_Ref_EndDateVecList = FindTuesdayBefore(ESA_CCI_YYYYMMDD_Of_InfoArray[-1,0])  # ESA_CCI ending year, month, day of month, this is also a Tuesday
    print("After ESA_CCI_Ref_BeginDateVecList")

    save_data_path = '/discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS/PreppedTrainNEvalNpzs/ClimGrid1D'
    os.makedirs(save_data_path, exist_ok=True)

    ESA_CCI_RefFileName = os.path.join(
          save_data_path,
          'ClimGrid1D_' + 'ESA_CCI_' + format(ESA_CCI_Ref_BeginDateVecList[0],'04') + format(ESA_CCI_Ref_BeginDateVecList[1],'02') + format(ESA_CCI_Ref_BeginDateVecList[2],'02') + 'To' + format(ESA_CCI_Ref_EndDateVecList[0],'04') + format(ESA_CCI_Ref_EndDateVecList[1],'02') + format(ESA_CCI_Ref_EndDateVecList[2],'02') + '.npz'
        )

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

    #BEGIN section for time-interpolating info arrays to desired temporal resolution


    ESA_CCI_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(ESA_CCI_YYYYMMDD_Of_InfoArray, 3, 'ESA_CCI', np.NaN)

    #Begin calculating real dates list for reference arrays


    ESA_CCI_RealDatesList_Of_RefArray, ESA_CCI_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(ESA_CCI_Ref_BeginDate, ESA_CCI_Ref_EndDate)

    #End calculating real dates list for reference arrays

    ESA_CCI_RefArray = np.empty([ ESA_CCI_YYYYMMDD_Of_RefArray.shape[0], ESA_CCI_InfoArray.shape[1]])
    ESA_CCI_RefArray[:] = np.NaN

    ESA_CCI_RefArray = TimeMeanValues(ESA_CCI_RealDatesList_Of_InfoArray, ESA_CCI_RealDatesList_Of_RefArray, ESA_CCI_InfoArray, ESA_CCI_RefArray, 7)

    print("--- %s seconds ---" % (time.time() - start_time))

    np.savez_compressed(ESA_CCI_RefFileName, ESA_CCI_RefArray = ESA_CCI_RefArray, ESA_CCI_YYYYMMDD_Of_RefArray = ESA_CCI_YYYYMMDD_Of_RefArray)
    PrintArrayInfo(ESA_CCI_YYYYMMDD_Of_RefArray, 'YYYYMMDD')

    PrintArrayInfo(ESA_CCI_RefArray, 'ESA_CCI')

    return


if __name__ == '__main__':
    main()
