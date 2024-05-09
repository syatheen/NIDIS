#!/usr/bin/env python
# Coded by Soni Yatheendradas
#         on Feb 21, 2023

from __future__ import division
import sys
import time
import logging
import numpy as np
import pandas as pd
from calendar import monthrange
from datetime import date, datetime, timedelta
from multiprocessing import Pool, cpu_count

# NOTE: sys.argv indices start at 1, not 0
# Python arguments to this program will be (for now):
#        ArgLSM ArgVariable ArgHUC
# ArgNum   1      2           3

def ConcatMonthlyArraysContainingDailyInfo(WhichLSM, WhichVariable, WhichHUC, NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList):

  for WhichYear in range(NLDAS_2_daily_Info_BeginYYYYMMVecList[0], NLDAS_2_daily_Info_EndYYYYMMVecList[0]+1):
  
    if WhichYear == NLDAS_2_daily_Info_BeginYYYYMMVecList[0]:
      BeginMonth = NLDAS_2_daily_Info_BeginYYYYMMVecList[1]
    else:
      BeginMonth = 1
    #end of if WhichYear == NLDAS_2_daily_Info_BeginYYYYMMVecList[0]
  
    if WhichYear == NLDAS_2_daily_Info_EndYYYYMMVecList[0]:
      EndMonth = NLDAS_2_daily_Info_EndYYYYMMVecList[1]
    else:
      EndMonth = 12
    #end of if WhichYear == NLDAS_2_daily_Info_EndYYYYMMVecList[0]
  
    for WhichMonth in range(BeginMonth, EndMonth+1):

      if ( (WhichVariable == '1MSM') or 
           (WhichVariable == 'TCSM') ):
        ThisYYYYMM_Info = np.load(InfoFilesDir + WhichLSM + '_' + WhichVariable + '_' + format(WhichYear, '04') + format(WhichMonth, '02') + '_ClimGrid1D.PERW.npz')
      elif ( (WhichVariable == 'EVAP') or 
             (WhichVariable == 'SWE') or
             (WhichVariable == 'RUN') ):
        ThisYYYYMM_Info = np.load(InfoFilesDir + WhichLSM + '_' + WhichVariable + '_' + format(WhichYear, '04') + format(WhichMonth, '02') + '_ClimGrid1D.PERW.50AdjustTo0.npz')
      elif (WhichVariable == 'STRM') :
        ThisYYYYMM_Info = np.load(InfoFilesDir + WhichLSM + '_' + WhichVariable + '_' + format(WhichYear, '04') + format(WhichMonth, '02') + '_' + WhichHUC + '_ClimGrid1D.PERW.50AdjustTo0.npz')
 
      ThisYYYYMMDD_Of_InfoArrayForPrcntl = ThisYYYYMM_Info['YYYYMMDD_Of_RefArrayForPrcntl']
      ThisInfoArrayForPrcntl = ThisYYYYMM_Info['RefArrayForPrcntl']
  
      if ( (WhichYear == NLDAS_2_daily_Info_BeginYYYYMMVecList[0]) and
           (WhichMonth == NLDAS_2_daily_Info_BeginYYYYMMVecList[1]) ):
        NLDAS_2_daily_YYYYMMDD_Of_InfoArray = np.copy(ThisYYYYMMDD_Of_InfoArrayForPrcntl)
        NLDAS_2_daily_InfoArray = np.copy(ThisInfoArrayForPrcntl)
      else: #of if ( (WhichYear == NLDAS_2_daily_Info_BeginYYYYMMVecList[0]) and....
        NLDAS_2_daily_YYYYMMDD_Of_InfoArray = np.concatenate((NLDAS_2_daily_YYYYMMDD_Of_InfoArray, ThisYYYYMMDD_Of_InfoArrayForPrcntl), axis = 0)
        NLDAS_2_daily_InfoArray = np.concatenate((NLDAS_2_daily_InfoArray, ThisInfoArrayForPrcntl), axis = 0)
      #end of if ( (WhichYear == NLDAS_2_daily_Info_BeginYYYYMMVecList[0]) and....
  
    #end of for WhichMonth in range(BeginMonth, EndMonth+1)
  
  #end of for WhichYear in range(NLDAS_2_daily_Info_BeginYYYYMMVecList[0], NLDAS_2_daily_Info_EndYYYYMMVecList[0]+1)

  return NLDAS_2_daily_YYYYMMDD_Of_InfoArray, NLDAS_2_daily_InfoArray

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

    # BEGIN code arguments / editable section

    InfoFilesDir = '/discover/nobackup/projects/nca/syatheen/NLDAS_2_daily_Npzs/'

    NLDAS_2_daily_Info_BeginYYYYMMVecList = [1980, 1] # Beginning year and month 
    NLDAS_2_daily_Info_EndYYYYMMVecList = [2021, 8] # Ending year and month 

    return

"""


ArgLSM = sys.argv[1] # Choices are 'Mosaic', 'Noah', 'SAC', 'VIC'
ArgVariable = sys.argv[2] # Choices currently implemented are '1MSM', 'TCSM'
ArgHUC = sys.argv[3] # Choices currently implemented are 'NA' (for "Not Applicable")

#BEGIN subsection for concatenating monthly-containing-daily Arrays


if (ArgVariable == 'STRM') :
  LSM_Variable_daily_YYYYMMDD_Of_InfoArray, LSM_Variable_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo(ArgLSM, ArgVariable, ArgHUC, NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
else:
  LSM_Variable_daily_YYYYMMDD_Of_InfoArray, LSM_Variable_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo(ArgLSM, ArgVariable, '', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
#Mosaic_STRM_daily_H02_YYYYMMDD_Of_InfoArray, Mosaic_STRM_daily_H02_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Mosaic', 'STRM', 'H02', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
#Noah_STRM_daily_H02_YYYYMMDD_Of_InfoArray, Noah_STRM_daily_H02_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Noah', 'STRM', 'H02', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
#SAC_STRM_daily_H02_YYYYMMDD_Of_InfoArray, SAC_STRM_daily_H02_InfoArray = ConcatMonthlyArraysContainingDailyInfo('SAC', 'STRM', 'H02', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
#VIC_STRM_daily_H02_YYYYMMDD_Of_InfoArray, VIC_STRM_daily_H02_InfoArray = ConcatMonthlyArraysContainingDailyInfo('VIC', 'STRM', 'H02', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
#Mosaic_STRM_daily_H04_YYYYMMDD_Of_InfoArray, Mosaic_STRM_daily_H04_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Mosaic', 'STRM', 'H04', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
#Noah_STRM_daily_H04_YYYYMMDD_Of_InfoArray, Noah_STRM_daily_H04_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Noah', 'STRM', 'H04', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
#SAC_STRM_daily_H04_YYYYMMDD_Of_InfoArray, SAC_STRM_daily_H04_InfoArray = ConcatMonthlyArraysContainingDailyInfo('SAC', 'STRM', 'H04', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
#VIC_STRM_daily_H04_YYYYMMDD_Of_InfoArray, VIC_STRM_daily_H04_InfoArray = ConcatMonthlyArraysContainingDailyInfo('VIC', 'STRM', 'H04', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
#Mosaic_STRM_daily_H06_YYYYMMDD_Of_InfoArray, Mosaic_STRM_daily_H06_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Mosaic', 'STRM', 'H06', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
#Noah_STRM_daily_H06_YYYYMMDD_Of_InfoArray, Noah_STRM_daily_H06_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Noah', 'STRM', 'H06', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
#SAC_STRM_daily_H06_YYYYMMDD_Of_InfoArray, SAC_STRM_daily_H06_InfoArray = ConcatMonthlyArraysContainingDailyInfo('SAC', 'STRM', 'H06', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
#VIC_STRM_daily_H06_YYYYMMDD_Of_InfoArray, VIC_STRM_daily_H06_InfoArray = ConcatMonthlyArraysContainingDailyInfo('VIC', 'STRM', 'H06', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
#Mosaic_STRM_daily_H08_YYYYMMDD_Of_InfoArray, Mosaic_STRM_daily_H08_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Mosaic', 'STRM', 'H08', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
#Noah_STRM_daily_H08_YYYYMMDD_Of_InfoArray, Noah_STRM_daily_H08_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Noah', 'STRM', 'H08', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
#SAC_STRM_daily_H08_YYYYMMDD_Of_InfoArray, SAC_STRM_daily_H08_InfoArray = ConcatMonthlyArraysContainingDailyInfo('SAC', 'STRM', 'H08', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
#VIC_STRM_daily_H08_YYYYMMDD_Of_InfoArray, VIC_STRM_daily_H08_InfoArray = ConcatMonthlyArraysContainingDailyInfo('VIC', 'STRM', 'H08', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)

#END subsection for concatenating monthly-containing-daily Arrays

NLDAS_2_Ref_BeginDateVecList = FindTuesdayAfter(LSM_Variable_daily_YYYYMMDD_Of_InfoArray[0,0])  # NLDAS_2_daily beginning year, month, day of month, this is also a Tuesday
NLDAS_2_Ref_EndDateVecList = FindTuesdayBefore(LSM_Variable_daily_YYYYMMDD_Of_InfoArray[-1,0])  # NLDAS_2_daily ending year, month, day of month, this is also a Tuesday

if (ArgVariable == 'STRM') :
  LSM_Variable_RefFileName = 'RefArrays/ClimGrid1D_' + ArgLSM + '_' + ArgVariable + '_' + ArgHUC + '_' + format(NLDAS_2_Ref_BeginDateVecList[0],'04') + format(NLDAS_2_Ref_BeginDateVecList[1],'02') + format(NLDAS_2_Ref_BeginDateVecList[2],'02') + 'To' + format(NLDAS_2_Ref_EndDateVecList[0],'04') + format(NLDAS_2_Ref_EndDateVecList[1],'02') + format(NLDAS_2_Ref_EndDateVecList[2],'02') + '.npz'
else:
  LSM_Variable_RefFileName = 'RefArrays/ClimGrid1D_' + ArgLSM + '_' + ArgVariable + '_' + format(NLDAS_2_Ref_BeginDateVecList[0],'04') + format(NLDAS_2_Ref_BeginDateVecList[1],'02') + format(NLDAS_2_Ref_BeginDateVecList[2],'02') + 'To' + format(NLDAS_2_Ref_EndDateVecList[0],'04') + format(NLDAS_2_Ref_EndDateVecList[1],'02') + format(NLDAS_2_Ref_EndDateVecList[2],'02') + '.npz'
#Mosaic_STRM_H02_RefFileName = 'RefArrays/ClimGrid1D_Mosaic_STRM_H02_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
#Noah_STRM_H02_RefFileName = 'RefArrays/ClimGrid1D_Noah_STRM_H02_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
#SAC_STRM_H02_RefFileName = 'RefArrays/ClimGrid1D_SAC_STRM_H02_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
#VIC_STRM_H02_RefFileName = 'RefArrays/ClimGrid1D_VIC_STRM_H02_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
#Mosaic_STRM_H04_RefFileName = 'RefArrays/ClimGrid1D_Mosaic_STRM_H04_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
#Noah_STRM_H04_RefFileName = 'RefArrays/ClimGrid1D_Noah_STRM_H04_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
#SAC_STRM_H04_RefFileName = 'RefArrays/ClimGrid1D_SAC_STRM_H04_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
#VIC_STRM_H04_RefFileName = 'RefArrays/ClimGrid1D_VIC_STRM_H04_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
#Mosaic_STRM_H06_RefFileName = 'RefArrays/ClimGrid1D_Mosaic_STRM_H06_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
#Noah_STRM_H06_RefFileName = 'RefArrays/ClimGrid1D_Noah_STRM_H06_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
#SAC_STRM_H06_RefFileName = 'RefArrays/ClimGrid1D_SAC_STRM_H06_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
#VIC_STRM_H06_RefFileName = 'RefArrays/ClimGrid1D_VIC_STRM_H06_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
#Mosaic_STRM_H08_RefFileName = 'RefArrays/ClimGrid1D_Mosaic_STRM_H08_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
#Noah_STRM_H08_RefFileName = 'RefArrays/ClimGrid1D_Noah_STRM_H08_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
#SAC_STRM_H08_RefFileName = 'RefArrays/ClimGrid1D_SAC_STRM_H08_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
#VIC_STRM_H08_RefFileName = 'RefArrays/ClimGrid1D_VIC_STRM_H08_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'

# END code arguments / editable section

start_time = time.time()

NLDAS_2_Ref_BeginDate = date(NLDAS_2_Ref_BeginDateVecList[0], NLDAS_2_Ref_BeginDateVecList[1], NLDAS_2_Ref_BeginDateVecList[2])
NLDAS_2_Ref_EndDate = date(NLDAS_2_Ref_EndDateVecList[0], NLDAS_2_Ref_EndDateVecList[1], NLDAS_2_Ref_EndDateVecList[2])

#BEGIN check whether the beginning and ending days are indeed Tuesdays

if NLDAS_2_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for NLDAS_2_Ref needs to be a Tuesday!!')
  sys.exit(0)
if NLDAS_2_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for NLDAS_2_Ref needs to be a Tuesday!!')
  sys.exit(0)

#END check whether the beginning and ending days are indeed Tuesdays

if NLDAS_2_Ref_BeginDate > NLDAS_2_Ref_EndDate:
  print('NLDAS_2_Ref_BeginDate should not be later than NLDAS_2_Ref_EndDate!!!')
  sys.exit(0)

#BEGIN section for time-interpolating info arrays to desired temporal resolution



NLDAS_2_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(LSM_Variable_daily_YYYYMMDD_Of_InfoArray, 3, 'NLDAS_2', np.NaN)

#Begin calculating real dates list for reference arrays


NLDAS_2_RealDatesList_Of_RefArray, NLDAS_2_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(NLDAS_2_Ref_BeginDate, NLDAS_2_Ref_EndDate)

#End calculating real dates list for reference arrays

LSM_Variable_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], LSM_Variable_daily_InfoArray.shape[1]])
LSM_Variable_RefArray[:] = np.NaN


LSM_Variable_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, LSM_Variable_daily_InfoArray, LSM_Variable_RefArray, 7)

print("--- %s seconds ---" % (time.time() - start_time))

if ArgVariable == '1MSM':
  if ArgLSM == 'Mosaic':
    np.savez_compressed(LSM_Variable_RefFileName, Mosaic_1MSM_RefArray = LSM_Variable_RefArray, Mosaic_1MSM_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
  elif ArgLSM == 'Noah':
    np.savez_compressed(LSM_Variable_RefFileName, Noah_1MSM_RefArray = LSM_Variable_RefArray, Noah_1MSM_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
  elif ArgLSM == 'SAC':
    np.savez_compressed(LSM_Variable_RefFileName, SAC_1MSM_RefArray = LSM_Variable_RefArray, SAC_1MSM_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
  elif ArgLSM == 'VIC':
    np.savez_compressed(LSM_Variable_RefFileName, VIC_1MSM_RefArray = LSM_Variable_RefArray, VIC_1MSM_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
  #end of if ArgLSM == 'Mosaic'
elif ArgVariable == 'TCSM':
  if ArgLSM == 'Mosaic':
    np.savez_compressed(LSM_Variable_RefFileName, Mosaic_TCSM_RefArray = LSM_Variable_RefArray, Mosaic_TCSM_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
  elif ArgLSM == 'Noah':
    np.savez_compressed(LSM_Variable_RefFileName, Noah_TCSM_RefArray = LSM_Variable_RefArray, Noah_TCSM_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
  elif ArgLSM == 'SAC':
    np.savez_compressed(LSM_Variable_RefFileName, SAC_TCSM_RefArray = LSM_Variable_RefArray, SAC_TCSM_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
  elif ArgLSM == 'VIC':
    np.savez_compressed(LSM_Variable_RefFileName, VIC_TCSM_RefArray = LSM_Variable_RefArray, VIC_TCSM_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
else: #of if ArgVariable == '1MSM'
  print('Add remaining np.savez_compressed code lines for other variables!!')
  sys.exit(0)
#end of if ArgVariable == '1MSM'
    #np.savez_compressed(Mosaic_STRM_H02_RefFileName, Mosaic_STRM_H02_RefArray = Mosaic_STRM_H02_RefArray, Mosaic_STRM_H02_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
    #np.savez_compressed(Noah_STRM_H02_RefFileName, Noah_STRM_H02_RefArray = Noah_STRM_H02_RefArray, Noah_STRM_H02_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
    #np.savez_compressed(SAC_STRM_H02_RefFileName, SAC_STRM_H02_RefArray = SAC_STRM_H02_RefArray, SAC_STRM_H02_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
    #np.savez_compressed(VIC_STRM_H02_RefFileName, VIC_STRM_H02_RefArray = VIC_STRM_H02_RefArray, VIC_STRM_H02_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
    #np.savez_compressed(Mosaic_STRM_H04_RefFileName, Mosaic_STRM_H04_RefArray = Mosaic_STRM_H04_RefArray, Mosaic_STRM_H04_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
    #np.savez_compressed(Noah_STRM_H04_RefFileName, Noah_STRM_H04_RefArray = Noah_STRM_H04_RefArray, Noah_STRM_H04_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
    #np.savez_compressed(SAC_STRM_H04_RefFileName, SAC_STRM_H04_RefArray = SAC_STRM_H04_RefArray, SAC_STRM_H04_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
    #np.savez_compressed(VIC_STRM_H04_RefFileName, VIC_STRM_H04_RefArray = VIC_STRM_H04_RefArray, VIC_STRM_H04_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
    #np.savez_compressed(Mosaic_STRM_H06_RefFileName, Mosaic_STRM_H06_RefArray = Mosaic_STRM_H06_RefArray, Mosaic_STRM_H06_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
    #np.savez_compressed(Noah_STRM_H06_RefFileName, Noah_STRM_H06_RefArray = Noah_STRM_H06_RefArray, Noah_STRM_H06_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
    #np.savez_compressed(SAC_STRM_H06_RefFileName, SAC_STRM_H06_RefArray = SAC_STRM_H06_RefArray, SAC_STRM_H06_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
    #np.savez_compressed(VIC_STRM_H06_RefFileName, VIC_STRM_H06_RefArray = VIC_STRM_H06_RefArray, VIC_STRM_H06_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
    #np.savez_compressed(Mosaic_STRM_H08_RefFileName, Mosaic_STRM_H08_RefArray = Mosaic_STRM_H08_RefArray, Mosaic_STRM_H08_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
    #np.savez_compressed(Noah_STRM_H08_RefFileName, Noah_STRM_H08_RefArray = Noah_STRM_H08_RefArray, Noah_STRM_H08_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
    #np.savez_compressed(SAC_STRM_H08_RefFileName, SAC_STRM_H08_RefArray = SAC_STRM_H08_RefArray, SAC_STRM_H08_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
    #np.savez_compressed(VIC_STRM_H08_RefFileName, VIC_STRM_H08_RefArray = VIC_STRM_H08_RefArray, VIC_STRM_H08_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)



PrintArrayInfo(NLDAS_2_YYYYMMDD_Of_RefArray, 'YYYYMMDD')

if (ArgVariable == 'STRM') :
  PrintArrayInfo(LSM_Variable_RefArray, ArgLSM + '_' + ArgVariable + '_' + ArgHUC)
else:
  PrintArrayInfo(LSM_Variable_RefArray, ArgLSM + '_' + ArgVariable)


"""

def main_wrapper(args):
   return main(*args)


def main_multiprocessing(
            ArgLSMList,
            ArgVariableList,
            StartDate,
            EndDate,
            ArgHUC,
            n_processes: int = 100
        ):

    logging.info("Inside main multiprocessing")

    # Generate date combinations
    date_list = pd.date_range(start=StartDate, end=EndDate, freq='MS')

    # Generating combination of parameters
    multiprocessing_arguments = []
    for lsm in ArgLSMList:
        for variable in ArgVariableList:
            for mdate in date_list:
                multiprocessing_arguments.append(
                    [lsm, variable, mdate.year, mdate.month, ArgHUC])

    # Start processing
    logging.info(f'Initiating {len(multiprocessing_arguments)} processes.')

    # temporary for testing
    # multiprocessing_arguments = multiprocessing_arguments[:1]
    # logging.info(f'Only processing {multiprocessing_arguments}')

    p = Pool(processes=n_processes)
    p.starmap(
        main_wrapper,
        zip(multiprocessing_arguments)
    )

    return


if __name__ == '__main__':
    main()