# Coded by Soni Yatheendradas
#         on Nov 8, 2021
from __future__ import division
from datetime import date, datetime, timedelta
import numpy as np

# BEGIN code arguments / editable section

IMERG1Month_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimDivs/IMERG1MonthsMean_20000630To20210531.npz'
IMERG2Month_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimDivs/IMERG2MonthsMean_20000730To20210531.npz'
IMERG3Month_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimDivs/IMERG3MonthsMean_20000829To20210531.npz'
IMERG6Month_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimDivs/IMERG6MonthsMean_20001127To20210531.npz'
IMERG9Month_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimDivs/IMERG9MonthsMean_20010225To20210531.npz'
IMERG12Month_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimDivs/IMERG12MonthsMean_20010531To20210531.npz'
IMERG24Month_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimDivs/IMERG24MonthsMean_20020531To20210531.npz'
IMERG36Month_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimDivs/IMERG36MonthsMean_20030531To20210531.npz'
IMERG48Month_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimDivs/IMERG48MonthsMean_20040531To20210531.npz'
IMERG60Month_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimDivs/IMERG60MonthsMean_20050531To20210531.npz'
IMERG72Month_InfoFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG/InfoArrsDailyMean/ClimDivs/IMERG72MonthsMean_20060531To20210531.npz'

IMERG1Month_Info = np.load(IMERG1Month_InfoFilename)
IMERG2Month_Info = np.load(IMERG2Month_InfoFilename)
IMERG3Month_Info = np.load(IMERG3Month_InfoFilename)
IMERG6Month_Info = np.load(IMERG6Month_InfoFilename)
IMERG9Month_Info = np.load(IMERG9Month_InfoFilename)
IMERG12Month_Info = np.load(IMERG12Month_InfoFilename)
IMERG24Month_Info = np.load(IMERG24Month_InfoFilename)
IMERG36Month_Info = np.load(IMERG36Month_InfoFilename)
IMERG48Month_Info = np.load(IMERG48Month_InfoFilename)
IMERG60Month_Info = np.load(IMERG60Month_InfoFilename)
IMERG72Month_Info = np.load(IMERG72Month_InfoFilename)

IMERG1Month_YYYYMMDD_Of_InfoArray  = IMERG1Month_Info['YYYYMMDD_Of_InfoArrayForPrcntl']
IMERG1Month_InfoArray  = IMERG1Month_Info['InfoArrayForPrcntl']
IMERG2Month_YYYYMMDD_Of_InfoArray  = IMERG2Month_Info['YYYYMMDD_Of_InfoArrayForPrcntl']
IMERG2Month_InfoArray  = IMERG2Month_Info['InfoArrayForPrcntl']
IMERG3Month_YYYYMMDD_Of_InfoArray  = IMERG3Month_Info['YYYYMMDD_Of_InfoArrayForPrcntl']
IMERG3Month_InfoArray  = IMERG3Month_Info['InfoArrayForPrcntl']
IMERG6Month_YYYYMMDD_Of_InfoArray  = IMERG6Month_Info['YYYYMMDD_Of_InfoArrayForPrcntl']
IMERG6Month_InfoArray  = IMERG6Month_Info['InfoArrayForPrcntl']
IMERG9Month_YYYYMMDD_Of_InfoArray  = IMERG9Month_Info['YYYYMMDD_Of_InfoArrayForPrcntl']
IMERG9Month_InfoArray  = IMERG9Month_Info['InfoArrayForPrcntl']
IMERG12Month_YYYYMMDD_Of_InfoArray  = IMERG12Month_Info['YYYYMMDD_Of_InfoArrayForPrcntl']
IMERG12Month_InfoArray  = IMERG12Month_Info['InfoArrayForPrcntl']
IMERG24Month_YYYYMMDD_Of_InfoArray  = IMERG24Month_Info['YYYYMMDD_Of_InfoArrayForPrcntl']
IMERG24Month_InfoArray  = IMERG24Month_Info['InfoArrayForPrcntl']
IMERG36Month_YYYYMMDD_Of_InfoArray  = IMERG36Month_Info['YYYYMMDD_Of_InfoArrayForPrcntl']
IMERG36Month_InfoArray  = IMERG36Month_Info['InfoArrayForPrcntl']
IMERG48Month_YYYYMMDD_Of_InfoArray  = IMERG48Month_Info['YYYYMMDD_Of_InfoArrayForPrcntl']
IMERG48Month_InfoArray  = IMERG48Month_Info['InfoArrayForPrcntl']
IMERG60Month_YYYYMMDD_Of_InfoArray  = IMERG60Month_Info['YYYYMMDD_Of_InfoArrayForPrcntl']
IMERG60Month_InfoArray  = IMERG60Month_Info['InfoArrayForPrcntl']
IMERG72Month_YYYYMMDD_Of_InfoArray  = IMERG72Month_Info['YYYYMMDD_Of_InfoArrayForPrcntl']
IMERG72Month_InfoArray  = IMERG72Month_Info['InfoArrayForPrcntl']

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

IMERG1Month_Ref_BeginDateVecList = FindTuesdayAfter(IMERG1Month_YYYYMMDD_Of_InfoArray[0,0])  # 1Month IMERG beginning year, month, day of month, this is also a Tuesday
IMERG1Month_Ref_EndDateVecList = FindTuesdayBefore(IMERG1Month_YYYYMMDD_Of_InfoArray[-1,0])  # 1Month IMERG ending year, month, day of month, this is also a Tuesday
IMERG2Month_Ref_BeginDateVecList = FindTuesdayAfter(IMERG2Month_YYYYMMDD_Of_InfoArray[0,0])  # 2Month IMERG beginning year, month, day of month, this is also a Tuesday
IMERG2Month_Ref_EndDateVecList = FindTuesdayBefore(IMERG2Month_YYYYMMDD_Of_InfoArray[-1,0])  # 2Month IMERG ending year, month, day of month, this is also a Tuesday
IMERG3Month_Ref_BeginDateVecList = FindTuesdayAfter(IMERG3Month_YYYYMMDD_Of_InfoArray[0,0])  # 3Month IMERG beginning year, month, day of month, this is also a Tuesday
IMERG3Month_Ref_EndDateVecList = FindTuesdayBefore(IMERG3Month_YYYYMMDD_Of_InfoArray[-1,0])  # 3Month IMERG ending year, month, day of month, this is also a Tuesday
IMERG6Month_Ref_BeginDateVecList = FindTuesdayAfter(IMERG6Month_YYYYMMDD_Of_InfoArray[0,0])  # 6Month IMERG beginning year, month, day of month, this is also a Tuesday
IMERG6Month_Ref_EndDateVecList = FindTuesdayBefore(IMERG6Month_YYYYMMDD_Of_InfoArray[-1,0])  # 6Month IMERG ending year, month, day of month, this is also a Tuesday
IMERG9Month_Ref_BeginDateVecList = FindTuesdayAfter(IMERG9Month_YYYYMMDD_Of_InfoArray[0,0])  # 9Month IMERG beginning year, month, day of month, this is also a Tuesday
IMERG9Month_Ref_EndDateVecList = FindTuesdayBefore(IMERG9Month_YYYYMMDD_Of_InfoArray[-1,0])  # 9Month IMERG ending year, month, day of month, this is also a Tuesday
IMERG12Month_Ref_BeginDateVecList = FindTuesdayAfter(IMERG12Month_YYYYMMDD_Of_InfoArray[0,0])  # 12Month IMERG beginning year, month, day of month, this is also a Tuesday
IMERG12Month_Ref_EndDateVecList = FindTuesdayBefore(IMERG12Month_YYYYMMDD_Of_InfoArray[-1,0])  # 12Month IMERG ending year, month, day of month, this is also a Tuesday
IMERG24Month_Ref_BeginDateVecList = FindTuesdayAfter(IMERG24Month_YYYYMMDD_Of_InfoArray[0,0])  # 24Month IMERG beginning year, month, day of month, this is also a Tuesday
IMERG24Month_Ref_EndDateVecList = FindTuesdayBefore(IMERG24Month_YYYYMMDD_Of_InfoArray[-1,0])  # 24Month IMERG ending year, month, day of month, this is also a Tuesday
IMERG36Month_Ref_BeginDateVecList = FindTuesdayAfter(IMERG36Month_YYYYMMDD_Of_InfoArray[0,0])  # 36Month IMERG beginning year, month, day of month, this is also a Tuesday
IMERG36Month_Ref_EndDateVecList = FindTuesdayBefore(IMERG36Month_YYYYMMDD_Of_InfoArray[-1,0])  # 36Month IMERG ending year, month, day of month, this is also a Tuesday
IMERG48Month_Ref_BeginDateVecList = FindTuesdayAfter(IMERG48Month_YYYYMMDD_Of_InfoArray[0,0])  # 48Month IMERG beginning year, month, day of month, this is also a Tuesday
IMERG48Month_Ref_EndDateVecList = FindTuesdayBefore(IMERG48Month_YYYYMMDD_Of_InfoArray[-1,0])  # 48Month IMERG ending year, month, day of month, this is also a Tuesday
IMERG60Month_Ref_BeginDateVecList = FindTuesdayAfter(IMERG60Month_YYYYMMDD_Of_InfoArray[0,0])  # 60Month IMERG beginning year, month, day of month, this is also a Tuesday
IMERG60Month_Ref_EndDateVecList = FindTuesdayBefore(IMERG60Month_YYYYMMDD_Of_InfoArray[-1,0])  # 60Month IMERG ending year, month, day of month, this is also a Tuesday
IMERG72Month_Ref_BeginDateVecList = FindTuesdayAfter(IMERG72Month_YYYYMMDD_Of_InfoArray[0,0])  # 72Month IMERG beginning year, month, day of month, this is also a Tuesday
IMERG72Month_Ref_EndDateVecList = FindTuesdayBefore(IMERG72Month_YYYYMMDD_Of_InfoArray[-1,0])  # 72Month IMERG ending year, month, day of month, this is also a Tuesday

IMERG1Month_RefFileName = 'RefArrays/ClimDiv_IMERG1Month_'+format(IMERG1Month_Ref_BeginDateVecList[0],'04')+format(IMERG1Month_Ref_BeginDateVecList[1],'02')+format(IMERG1Month_Ref_BeginDateVecList[2],'02')+'To'+format(IMERG1Month_Ref_EndDateVecList[0],'04')+format(IMERG1Month_Ref_EndDateVecList[1],'02')+format(IMERG1Month_Ref_EndDateVecList[2],'02')+'.npz'
IMERG2Month_RefFileName = 'RefArrays/ClimDiv_IMERG2Month_'+format(IMERG2Month_Ref_BeginDateVecList[0],'04')+format(IMERG2Month_Ref_BeginDateVecList[1],'02')+format(IMERG2Month_Ref_BeginDateVecList[2],'02')+'To'+format(IMERG2Month_Ref_EndDateVecList[0],'04')+format(IMERG2Month_Ref_EndDateVecList[1],'02')+format(IMERG2Month_Ref_EndDateVecList[2],'02')+'.npz'
IMERG3Month_RefFileName = 'RefArrays/ClimDiv_IMERG3Month_'+format(IMERG3Month_Ref_BeginDateVecList[0],'04')+format(IMERG3Month_Ref_BeginDateVecList[1],'02')+format(IMERG3Month_Ref_BeginDateVecList[2],'02')+'To'+format(IMERG3Month_Ref_EndDateVecList[0],'04')+format(IMERG3Month_Ref_EndDateVecList[1],'02')+format(IMERG3Month_Ref_EndDateVecList[2],'02')+'.npz'
IMERG6Month_RefFileName = 'RefArrays/ClimDiv_IMERG6Month_'+format(IMERG6Month_Ref_BeginDateVecList[0],'04')+format(IMERG6Month_Ref_BeginDateVecList[1],'02')+format(IMERG6Month_Ref_BeginDateVecList[2],'02')+'To'+format(IMERG6Month_Ref_EndDateVecList[0],'04')+format(IMERG6Month_Ref_EndDateVecList[1],'02')+format(IMERG6Month_Ref_EndDateVecList[2],'02')+'.npz'
IMERG9Month_RefFileName = 'RefArrays/ClimDiv_IMERG9Month_'+format(IMERG9Month_Ref_BeginDateVecList[0],'04')+format(IMERG9Month_Ref_BeginDateVecList[1],'02')+format(IMERG9Month_Ref_BeginDateVecList[2],'02')+'To'+format(IMERG9Month_Ref_EndDateVecList[0],'04')+format(IMERG9Month_Ref_EndDateVecList[1],'02')+format(IMERG9Month_Ref_EndDateVecList[2],'02')+'.npz'
IMERG12Month_RefFileName = 'RefArrays/ClimDiv_IMERG12Month_'+format(IMERG12Month_Ref_BeginDateVecList[0],'04')+format(IMERG12Month_Ref_BeginDateVecList[1],'02')+format(IMERG12Month_Ref_BeginDateVecList[2],'02')+'To'+format(IMERG12Month_Ref_EndDateVecList[0],'04')+format(IMERG12Month_Ref_EndDateVecList[1],'02')+format(IMERG12Month_Ref_EndDateVecList[2],'02')+'.npz'
IMERG24Month_RefFileName = 'RefArrays/ClimDiv_IMERG24Month_'+format(IMERG24Month_Ref_BeginDateVecList[0],'04')+format(IMERG24Month_Ref_BeginDateVecList[1],'02')+format(IMERG24Month_Ref_BeginDateVecList[2],'02')+'To'+format(IMERG24Month_Ref_EndDateVecList[0],'04')+format(IMERG24Month_Ref_EndDateVecList[1],'02')+format(IMERG24Month_Ref_EndDateVecList[2],'02')+'.npz'
IMERG36Month_RefFileName = 'RefArrays/ClimDiv_IMERG36Month_'+format(IMERG36Month_Ref_BeginDateVecList[0],'04')+format(IMERG36Month_Ref_BeginDateVecList[1],'02')+format(IMERG36Month_Ref_BeginDateVecList[2],'02')+'To'+format(IMERG36Month_Ref_EndDateVecList[0],'04')+format(IMERG36Month_Ref_EndDateVecList[1],'02')+format(IMERG36Month_Ref_EndDateVecList[2],'02')+'.npz'
IMERG48Month_RefFileName = 'RefArrays/ClimDiv_IMERG48Month_'+format(IMERG48Month_Ref_BeginDateVecList[0],'04')+format(IMERG48Month_Ref_BeginDateVecList[1],'02')+format(IMERG48Month_Ref_BeginDateVecList[2],'02')+'To'+format(IMERG48Month_Ref_EndDateVecList[0],'04')+format(IMERG48Month_Ref_EndDateVecList[1],'02')+format(IMERG48Month_Ref_EndDateVecList[2],'02')+'.npz'
IMERG60Month_RefFileName = 'RefArrays/ClimDiv_IMERG60Month_'+format(IMERG60Month_Ref_BeginDateVecList[0],'04')+format(IMERG60Month_Ref_BeginDateVecList[1],'02')+format(IMERG60Month_Ref_BeginDateVecList[2],'02')+'To'+format(IMERG60Month_Ref_EndDateVecList[0],'04')+format(IMERG60Month_Ref_EndDateVecList[1],'02')+format(IMERG60Month_Ref_EndDateVecList[2],'02')+'.npz'
IMERG72Month_RefFileName = 'RefArrays/ClimDiv_IMERG72Month_'+format(IMERG72Month_Ref_BeginDateVecList[0],'04')+format(IMERG72Month_Ref_BeginDateVecList[1],'02')+format(IMERG72Month_Ref_BeginDateVecList[2],'02')+'To'+format(IMERG72Month_Ref_EndDateVecList[0],'04')+format(IMERG72Month_Ref_EndDateVecList[1],'02')+format(IMERG72Month_Ref_EndDateVecList[2],'02')+'.npz'

# END code arguments / editable section

import sys
#np.set_printoptions(threshold=np.inf)
from calendar import monthrange
import time
import os

start_time = time.time()

IMERG1Month_Ref_BeginDate = date(IMERG1Month_Ref_BeginDateVecList[0], IMERG1Month_Ref_BeginDateVecList[1], IMERG1Month_Ref_BeginDateVecList[2])
IMERG1Month_Ref_EndDate = date(IMERG1Month_Ref_EndDateVecList[0], IMERG1Month_Ref_EndDateVecList[1], IMERG1Month_Ref_EndDateVecList[2])
IMERG2Month_Ref_BeginDate = date(IMERG2Month_Ref_BeginDateVecList[0], IMERG2Month_Ref_BeginDateVecList[1], IMERG2Month_Ref_BeginDateVecList[2])
IMERG2Month_Ref_EndDate = date(IMERG2Month_Ref_EndDateVecList[0], IMERG2Month_Ref_EndDateVecList[1], IMERG2Month_Ref_EndDateVecList[2])
IMERG3Month_Ref_BeginDate = date(IMERG3Month_Ref_BeginDateVecList[0], IMERG3Month_Ref_BeginDateVecList[1], IMERG3Month_Ref_BeginDateVecList[2])
IMERG3Month_Ref_EndDate = date(IMERG3Month_Ref_EndDateVecList[0], IMERG3Month_Ref_EndDateVecList[1], IMERG3Month_Ref_EndDateVecList[2])
IMERG6Month_Ref_BeginDate = date(IMERG6Month_Ref_BeginDateVecList[0], IMERG6Month_Ref_BeginDateVecList[1], IMERG6Month_Ref_BeginDateVecList[2])
IMERG6Month_Ref_EndDate = date(IMERG6Month_Ref_EndDateVecList[0], IMERG6Month_Ref_EndDateVecList[1], IMERG6Month_Ref_EndDateVecList[2])
IMERG9Month_Ref_BeginDate = date(IMERG9Month_Ref_BeginDateVecList[0], IMERG9Month_Ref_BeginDateVecList[1], IMERG9Month_Ref_BeginDateVecList[2])
IMERG9Month_Ref_EndDate = date(IMERG9Month_Ref_EndDateVecList[0], IMERG9Month_Ref_EndDateVecList[1], IMERG9Month_Ref_EndDateVecList[2])
IMERG12Month_Ref_BeginDate = date(IMERG12Month_Ref_BeginDateVecList[0], IMERG12Month_Ref_BeginDateVecList[1], IMERG12Month_Ref_BeginDateVecList[2])
IMERG12Month_Ref_EndDate = date(IMERG12Month_Ref_EndDateVecList[0], IMERG12Month_Ref_EndDateVecList[1], IMERG12Month_Ref_EndDateVecList[2])
IMERG24Month_Ref_BeginDate = date(IMERG24Month_Ref_BeginDateVecList[0], IMERG24Month_Ref_BeginDateVecList[1], IMERG24Month_Ref_BeginDateVecList[2])
IMERG24Month_Ref_EndDate = date(IMERG24Month_Ref_EndDateVecList[0], IMERG24Month_Ref_EndDateVecList[1], IMERG24Month_Ref_EndDateVecList[2])
IMERG36Month_Ref_BeginDate = date(IMERG36Month_Ref_BeginDateVecList[0], IMERG36Month_Ref_BeginDateVecList[1], IMERG36Month_Ref_BeginDateVecList[2])
IMERG36Month_Ref_EndDate = date(IMERG36Month_Ref_EndDateVecList[0], IMERG36Month_Ref_EndDateVecList[1], IMERG36Month_Ref_EndDateVecList[2])
IMERG48Month_Ref_BeginDate = date(IMERG48Month_Ref_BeginDateVecList[0], IMERG48Month_Ref_BeginDateVecList[1], IMERG48Month_Ref_BeginDateVecList[2])
IMERG48Month_Ref_EndDate = date(IMERG48Month_Ref_EndDateVecList[0], IMERG48Month_Ref_EndDateVecList[1], IMERG48Month_Ref_EndDateVecList[2])
IMERG60Month_Ref_BeginDate = date(IMERG60Month_Ref_BeginDateVecList[0], IMERG60Month_Ref_BeginDateVecList[1], IMERG60Month_Ref_BeginDateVecList[2])
IMERG60Month_Ref_EndDate = date(IMERG60Month_Ref_EndDateVecList[0], IMERG60Month_Ref_EndDateVecList[1], IMERG60Month_Ref_EndDateVecList[2])
IMERG72Month_Ref_BeginDate = date(IMERG72Month_Ref_BeginDateVecList[0], IMERG72Month_Ref_BeginDateVecList[1], IMERG72Month_Ref_BeginDateVecList[2])
IMERG72Month_Ref_EndDate = date(IMERG72Month_Ref_EndDateVecList[0], IMERG72Month_Ref_EndDateVecList[1], IMERG72Month_Ref_EndDateVecList[2])

#BEGIN check whether the beginning and ending days are indeed Tuesdays
if IMERG1Month_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for IMERG1Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG1Month_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for IMERG1Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG2Month_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for IMERG2Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG2Month_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for IMERG2Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG3Month_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for IMERG3Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG3Month_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for IMERG3Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG6Month_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for IMERG6Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG6Month_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for IMERG6Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG9Month_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for IMERG9Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG9Month_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for IMERG9Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG12Month_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for IMERG12Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG12Month_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for IMERG12Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG24Month_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for IMERG24Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG24Month_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for IMERG24Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG36Month_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for IMERG36Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG36Month_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for IMERG36Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG48Month_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for IMERG48Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG48Month_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for IMERG48Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG60Month_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for IMERG60Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG60Month_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for IMERG60Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG72Month_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for IMERG72Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
if IMERG72Month_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for IMERG72Month_Ref needs to be a Tuesday!!')
  sys.exit(0)
#END check whether the beginning and ending days are indeed Tuesdays

if IMERG1Month_Ref_BeginDate > IMERG1Month_Ref_EndDate:
  print('IMERG1Month_Ref_BeginDate should not be later than IMERG1Month_Ref_EndDate!!!')
  sys.exit(0)
if IMERG2Month_Ref_BeginDate > IMERG2Month_Ref_EndDate:
  print('IMERG2Month_Ref_BeginDate should not be later than IMERG2Month_Ref_EndDate!!!')
  sys.exit(0)
if IMERG3Month_Ref_BeginDate > IMERG3Month_Ref_EndDate:
  print('IMERG3Month_Ref_BeginDate should not be later than IMERG3Month_Ref_EndDate!!!')
  sys.exit(0)
if IMERG6Month_Ref_BeginDate > IMERG6Month_Ref_EndDate:
  print('IMERG6Month_Ref_BeginDate should not be later than IMERG6Month_Ref_EndDate!!!')
  sys.exit(0)
if IMERG9Month_Ref_BeginDate > IMERG9Month_Ref_EndDate:
  print('IMERG9Month_Ref_BeginDate should not be later than IMERG9Month_Ref_EndDate!!!')
  sys.exit(0)
if IMERG12Month_Ref_BeginDate > IMERG12Month_Ref_EndDate:
  print('IMERG12Month_Ref_BeginDate should not be later than IMERG12Month_Ref_EndDate!!!')
  sys.exit(0)
if IMERG24Month_Ref_BeginDate > IMERG24Month_Ref_EndDate:
  print('IMERG24Month_Ref_BeginDate should not be later than IMERG24Month_Ref_EndDate!!!')
  sys.exit(0)
if IMERG36Month_Ref_BeginDate > IMERG36Month_Ref_EndDate:
  print('IMERG36Month_Ref_BeginDate should not be later than IMERG36Month_Ref_EndDate!!!')
  sys.exit(0)
if IMERG48Month_Ref_BeginDate > IMERG48Month_Ref_EndDate:
  print('IMERG48Month_Ref_BeginDate should not be later than IMERG48Month_Ref_EndDate!!!')
  sys.exit(0)
if IMERG60Month_Ref_BeginDate > IMERG60Month_Ref_EndDate:
  print('IMERG60Month_Ref_BeginDate should not be later than IMERG60Month_Ref_EndDate!!!')
  sys.exit(0)
if IMERG72Month_Ref_BeginDate > IMERG72Month_Ref_EndDate:
  print('IMERG72Month_Ref_BeginDate should not be later than IMERG72Month_Ref_EndDate!!!')
  sys.exit(0)

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

IMERG1Month_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(IMERG1Month_YYYYMMDD_Of_InfoArray, 3, 'IMERG1Month', np.NaN)
IMERG2Month_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(IMERG2Month_YYYYMMDD_Of_InfoArray, 3, 'IMERG2Month', np.NaN)
IMERG3Month_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(IMERG3Month_YYYYMMDD_Of_InfoArray, 3, 'IMERG3Month', np.NaN)
IMERG6Month_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(IMERG6Month_YYYYMMDD_Of_InfoArray, 3, 'IMERG6Month', np.NaN)
IMERG9Month_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(IMERG9Month_YYYYMMDD_Of_InfoArray, 3, 'IMERG9Month', np.NaN)
IMERG12Month_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(IMERG12Month_YYYYMMDD_Of_InfoArray, 3, 'IMERG12Month', np.NaN)
IMERG24Month_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(IMERG24Month_YYYYMMDD_Of_InfoArray, 3, 'IMERG24Month', np.NaN)
IMERG36Month_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(IMERG36Month_YYYYMMDD_Of_InfoArray, 3, 'IMERG36Month', np.NaN)
IMERG48Month_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(IMERG48Month_YYYYMMDD_Of_InfoArray, 3, 'IMERG48Month', np.NaN)
IMERG60Month_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(IMERG60Month_YYYYMMDD_Of_InfoArray, 3, 'IMERG60Month', np.NaN)
IMERG72Month_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(IMERG72Month_YYYYMMDD_Of_InfoArray, 3, 'IMERG72Month', np.NaN)

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

IMERG1Month_RealDatesList_Of_RefArray, IMERG1Month_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(IMERG1Month_Ref_BeginDate, IMERG1Month_Ref_EndDate)
IMERG2Month_RealDatesList_Of_RefArray, IMERG2Month_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(IMERG2Month_Ref_BeginDate, IMERG2Month_Ref_EndDate)
IMERG3Month_RealDatesList_Of_RefArray, IMERG3Month_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(IMERG3Month_Ref_BeginDate, IMERG3Month_Ref_EndDate)
IMERG6Month_RealDatesList_Of_RefArray, IMERG6Month_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(IMERG6Month_Ref_BeginDate, IMERG6Month_Ref_EndDate)
IMERG9Month_RealDatesList_Of_RefArray, IMERG9Month_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(IMERG9Month_Ref_BeginDate, IMERG9Month_Ref_EndDate)
IMERG12Month_RealDatesList_Of_RefArray, IMERG12Month_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(IMERG12Month_Ref_BeginDate, IMERG12Month_Ref_EndDate)
IMERG24Month_RealDatesList_Of_RefArray, IMERG24Month_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(IMERG24Month_Ref_BeginDate, IMERG24Month_Ref_EndDate)
IMERG36Month_RealDatesList_Of_RefArray, IMERG36Month_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(IMERG36Month_Ref_BeginDate, IMERG36Month_Ref_EndDate)
IMERG48Month_RealDatesList_Of_RefArray, IMERG48Month_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(IMERG48Month_Ref_BeginDate, IMERG48Month_Ref_EndDate)
IMERG60Month_RealDatesList_Of_RefArray, IMERG60Month_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(IMERG60Month_Ref_BeginDate, IMERG60Month_Ref_EndDate)
IMERG72Month_RealDatesList_Of_RefArray, IMERG72Month_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(IMERG72Month_Ref_BeginDate, IMERG72Month_Ref_EndDate)

#End calculating real dates list for reference arrays

IMERG1Month_RefArray = np.empty([ IMERG1Month_YYYYMMDD_Of_RefArray.shape[0], IMERG1Month_InfoArray.shape[1]])
IMERG1Month_RefArray[:] = np.NaN
IMERG2Month_RefArray = np.empty([ IMERG2Month_YYYYMMDD_Of_RefArray.shape[0], IMERG2Month_InfoArray.shape[1]])
IMERG2Month_RefArray[:] = np.NaN
IMERG3Month_RefArray = np.empty([ IMERG3Month_YYYYMMDD_Of_RefArray.shape[0], IMERG3Month_InfoArray.shape[1]])
IMERG3Month_RefArray[:] = np.NaN
IMERG6Month_RefArray = np.empty([ IMERG6Month_YYYYMMDD_Of_RefArray.shape[0], IMERG6Month_InfoArray.shape[1]])
IMERG6Month_RefArray[:] = np.NaN
IMERG9Month_RefArray = np.empty([ IMERG9Month_YYYYMMDD_Of_RefArray.shape[0], IMERG9Month_InfoArray.shape[1]])
IMERG9Month_RefArray[:] = np.NaN
IMERG12Month_RefArray = np.empty([ IMERG12Month_YYYYMMDD_Of_RefArray.shape[0], IMERG12Month_InfoArray.shape[1]])
IMERG12Month_RefArray[:] = np.NaN
IMERG24Month_RefArray = np.empty([ IMERG24Month_YYYYMMDD_Of_RefArray.shape[0], IMERG24Month_InfoArray.shape[1]])
IMERG24Month_RefArray[:] = np.NaN
IMERG36Month_RefArray = np.empty([ IMERG36Month_YYYYMMDD_Of_RefArray.shape[0], IMERG36Month_InfoArray.shape[1]])
IMERG36Month_RefArray[:] = np.NaN
IMERG48Month_RefArray = np.empty([ IMERG48Month_YYYYMMDD_Of_RefArray.shape[0], IMERG48Month_InfoArray.shape[1]])
IMERG48Month_RefArray[:] = np.NaN
IMERG60Month_RefArray = np.empty([ IMERG60Month_YYYYMMDD_Of_RefArray.shape[0], IMERG60Month_InfoArray.shape[1]])
IMERG60Month_RefArray[:] = np.NaN
IMERG72Month_RefArray = np.empty([ IMERG72Month_YYYYMMDD_Of_RefArray.shape[0], IMERG72Month_InfoArray.shape[1]])
IMERG72Month_RefArray[:] = np.NaN

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

IMERG1Month_RefArray = TimeMeanValues(IMERG1Month_RealDatesList_Of_InfoArray, IMERG1Month_RealDatesList_Of_RefArray, IMERG1Month_InfoArray, IMERG1Month_RefArray, 7)
IMERG2Month_RefArray = TimeMeanValues(IMERG2Month_RealDatesList_Of_InfoArray, IMERG2Month_RealDatesList_Of_RefArray, IMERG2Month_InfoArray, IMERG2Month_RefArray, 7)
IMERG3Month_RefArray = TimeMeanValues(IMERG3Month_RealDatesList_Of_InfoArray, IMERG3Month_RealDatesList_Of_RefArray, IMERG3Month_InfoArray, IMERG3Month_RefArray, 7)
IMERG6Month_RefArray = TimeMeanValues(IMERG6Month_RealDatesList_Of_InfoArray, IMERG6Month_RealDatesList_Of_RefArray, IMERG6Month_InfoArray, IMERG6Month_RefArray, 7)
IMERG9Month_RefArray = TimeMeanValues(IMERG9Month_RealDatesList_Of_InfoArray, IMERG9Month_RealDatesList_Of_RefArray, IMERG9Month_InfoArray, IMERG9Month_RefArray, 7)
IMERG12Month_RefArray = TimeMeanValues(IMERG12Month_RealDatesList_Of_InfoArray, IMERG12Month_RealDatesList_Of_RefArray, IMERG12Month_InfoArray, IMERG12Month_RefArray, 7)
IMERG24Month_RefArray = TimeMeanValues(IMERG24Month_RealDatesList_Of_InfoArray, IMERG24Month_RealDatesList_Of_RefArray, IMERG24Month_InfoArray, IMERG24Month_RefArray, 7)
IMERG36Month_RefArray = TimeMeanValues(IMERG36Month_RealDatesList_Of_InfoArray, IMERG36Month_RealDatesList_Of_RefArray, IMERG36Month_InfoArray, IMERG36Month_RefArray, 7)
IMERG48Month_RefArray = TimeMeanValues(IMERG48Month_RealDatesList_Of_InfoArray, IMERG48Month_RealDatesList_Of_RefArray, IMERG48Month_InfoArray, IMERG48Month_RefArray, 7)
IMERG60Month_RefArray = TimeMeanValues(IMERG60Month_RealDatesList_Of_InfoArray, IMERG60Month_RealDatesList_Of_RefArray, IMERG60Month_InfoArray, IMERG60Month_RefArray, 7)
IMERG72Month_RefArray = TimeMeanValues(IMERG72Month_RealDatesList_Of_InfoArray, IMERG72Month_RealDatesList_Of_RefArray, IMERG72Month_InfoArray, IMERG72Month_RefArray, 7)

print("--- %s seconds ---" % (time.time() - start_time))

np.savez_compressed(IMERG1Month_RefFileName, IMERG1Month_RefArray = IMERG1Month_RefArray, IMERG1Month_YYYYMMDD_Of_RefArray = IMERG1Month_YYYYMMDD_Of_RefArray)
np.savez_compressed(IMERG2Month_RefFileName, IMERG2Month_RefArray = IMERG2Month_RefArray, IMERG2Month_YYYYMMDD_Of_RefArray = IMERG2Month_YYYYMMDD_Of_RefArray)
np.savez_compressed(IMERG3Month_RefFileName, IMERG3Month_RefArray = IMERG3Month_RefArray, IMERG3Month_YYYYMMDD_Of_RefArray = IMERG3Month_YYYYMMDD_Of_RefArray)
np.savez_compressed(IMERG6Month_RefFileName, IMERG6Month_RefArray = IMERG6Month_RefArray, IMERG6Month_YYYYMMDD_Of_RefArray = IMERG6Month_YYYYMMDD_Of_RefArray)
np.savez_compressed(IMERG9Month_RefFileName, IMERG9Month_RefArray = IMERG9Month_RefArray, IMERG9Month_YYYYMMDD_Of_RefArray = IMERG9Month_YYYYMMDD_Of_RefArray)
np.savez_compressed(IMERG12Month_RefFileName, IMERG12Month_RefArray = IMERG12Month_RefArray, IMERG12Month_YYYYMMDD_Of_RefArray = IMERG12Month_YYYYMMDD_Of_RefArray)
np.savez_compressed(IMERG24Month_RefFileName, IMERG24Month_RefArray = IMERG24Month_RefArray, IMERG24Month_YYYYMMDD_Of_RefArray = IMERG24Month_YYYYMMDD_Of_RefArray)
np.savez_compressed(IMERG36Month_RefFileName, IMERG36Month_RefArray = IMERG36Month_RefArray, IMERG36Month_YYYYMMDD_Of_RefArray = IMERG36Month_YYYYMMDD_Of_RefArray)
np.savez_compressed(IMERG48Month_RefFileName, IMERG48Month_RefArray = IMERG48Month_RefArray, IMERG48Month_YYYYMMDD_Of_RefArray = IMERG48Month_YYYYMMDD_Of_RefArray)
np.savez_compressed(IMERG60Month_RefFileName, IMERG60Month_RefArray = IMERG60Month_RefArray, IMERG60Month_YYYYMMDD_Of_RefArray = IMERG60Month_YYYYMMDD_Of_RefArray)
np.savez_compressed(IMERG72Month_RefFileName, IMERG72Month_RefArray = IMERG72Month_RefArray, IMERG72Month_YYYYMMDD_Of_RefArray = IMERG72Month_YYYYMMDD_Of_RefArray)

print("IMERG1Month_YYYYMMDD_Of_RefArray.shape is ",IMERG1Month_YYYYMMDD_Of_RefArray.shape)
print("IMERG1Month_YYYYMMDD_Of_RefArray is ",IMERG1Month_YYYYMMDD_Of_RefArray)

print("IMERG1Month_RefArray.shape is ",IMERG1Month_RefArray.shape)
print("IMERG1Month_RefArray is ",IMERG1Month_RefArray)
print("np.amin(np.isnan(IMERG1Month_RefArray).sum(axis=0)) is ",np.amin(np.isnan(IMERG1Month_RefArray).sum(axis=0)))
print("np.amax(np.isnan(IMERG1Month_RefArray).sum(axis=0)) is ",np.amax(np.isnan(IMERG1Month_RefArray).sum(axis=0)))
print("np.amin(np.isnan(IMERG1Month_RefArray).sum(axis=1)) is ",np.amin(np.isnan(IMERG1Month_RefArray).sum(axis=1)))
print("np.amax(np.isnan(IMERG1Month_RefArray).sum(axis=1)) is ",np.amax(np.isnan(IMERG1Month_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(IMERG1Month_RefArray),', overall max is ',np.nanmax(IMERG1Month_RefArray))

print("IMERG2Month_YYYYMMDD_Of_RefArray.shape is ",IMERG2Month_YYYYMMDD_Of_RefArray.shape)
print("IMERG2Month_YYYYMMDD_Of_RefArray is ",IMERG2Month_YYYYMMDD_Of_RefArray)

print("IMERG2Month_RefArray.shape is ",IMERG2Month_RefArray.shape)
print("IMERG2Month_RefArray is ",IMERG2Month_RefArray)
print("np.amin(np.isnan(IMERG2Month_RefArray).sum(axis=0)) is ",np.amin(np.isnan(IMERG2Month_RefArray).sum(axis=0)))
print("np.amax(np.isnan(IMERG2Month_RefArray).sum(axis=0)) is ",np.amax(np.isnan(IMERG2Month_RefArray).sum(axis=0)))
print("np.amin(np.isnan(IMERG2Month_RefArray).sum(axis=1)) is ",np.amin(np.isnan(IMERG2Month_RefArray).sum(axis=1)))
print("np.amax(np.isnan(IMERG2Month_RefArray).sum(axis=1)) is ",np.amax(np.isnan(IMERG2Month_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(IMERG2Month_RefArray),', overall max is ',np.nanmax(IMERG2Month_RefArray))

print("IMERG3Month_YYYYMMDD_Of_RefArray.shape is ",IMERG3Month_YYYYMMDD_Of_RefArray.shape)
print("IMERG3Month_YYYYMMDD_Of_RefArray is ",IMERG3Month_YYYYMMDD_Of_RefArray)

print("IMERG3Month_RefArray.shape is ",IMERG3Month_RefArray.shape)
print("IMERG3Month_RefArray is ",IMERG3Month_RefArray)
print("np.amin(np.isnan(IMERG3Month_RefArray).sum(axis=0)) is ",np.amin(np.isnan(IMERG3Month_RefArray).sum(axis=0)))
print("np.amax(np.isnan(IMERG3Month_RefArray).sum(axis=0)) is ",np.amax(np.isnan(IMERG3Month_RefArray).sum(axis=0)))
print("np.amin(np.isnan(IMERG3Month_RefArray).sum(axis=1)) is ",np.amin(np.isnan(IMERG3Month_RefArray).sum(axis=1)))
print("np.amax(np.isnan(IMERG3Month_RefArray).sum(axis=1)) is ",np.amax(np.isnan(IMERG3Month_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(IMERG3Month_RefArray),', overall max is ',np.nanmax(IMERG3Month_RefArray))

print("IMERG6Month_YYYYMMDD_Of_RefArray.shape is ",IMERG6Month_YYYYMMDD_Of_RefArray.shape)
print("IMERG6Month_YYYYMMDD_Of_RefArray is ",IMERG6Month_YYYYMMDD_Of_RefArray)

print("IMERG6Month_RefArray.shape is ",IMERG6Month_RefArray.shape)
print("IMERG6Month_RefArray is ",IMERG6Month_RefArray)
print("np.amin(np.isnan(IMERG6Month_RefArray).sum(axis=0)) is ",np.amin(np.isnan(IMERG6Month_RefArray).sum(axis=0)))
print("np.amax(np.isnan(IMERG6Month_RefArray).sum(axis=0)) is ",np.amax(np.isnan(IMERG6Month_RefArray).sum(axis=0)))
print("np.amin(np.isnan(IMERG6Month_RefArray).sum(axis=1)) is ",np.amin(np.isnan(IMERG6Month_RefArray).sum(axis=1)))
print("np.amax(np.isnan(IMERG6Month_RefArray).sum(axis=1)) is ",np.amax(np.isnan(IMERG6Month_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(IMERG6Month_RefArray),', overall max is ',np.nanmax(IMERG6Month_RefArray))

print("IMERG9Month_YYYYMMDD_Of_RefArray.shape is ",IMERG9Month_YYYYMMDD_Of_RefArray.shape)
print("IMERG9Month_YYYYMMDD_Of_RefArray is ",IMERG9Month_YYYYMMDD_Of_RefArray)

print("IMERG9Month_RefArray.shape is ",IMERG9Month_RefArray.shape)
print("IMERG9Month_RefArray is ",IMERG9Month_RefArray)
print("np.amin(np.isnan(IMERG9Month_RefArray).sum(axis=0)) is ",np.amin(np.isnan(IMERG9Month_RefArray).sum(axis=0)))
print("np.amax(np.isnan(IMERG9Month_RefArray).sum(axis=0)) is ",np.amax(np.isnan(IMERG9Month_RefArray).sum(axis=0)))
print("np.amin(np.isnan(IMERG9Month_RefArray).sum(axis=1)) is ",np.amin(np.isnan(IMERG9Month_RefArray).sum(axis=1)))
print("np.amax(np.isnan(IMERG9Month_RefArray).sum(axis=1)) is ",np.amax(np.isnan(IMERG9Month_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(IMERG9Month_RefArray),', overall max is ',np.nanmax(IMERG9Month_RefArray))

print("IMERG12Month_YYYYMMDD_Of_RefArray.shape is ",IMERG12Month_YYYYMMDD_Of_RefArray.shape)
print("IMERG12Month_YYYYMMDD_Of_RefArray is ",IMERG12Month_YYYYMMDD_Of_RefArray)

print("IMERG12Month_RefArray.shape is ",IMERG12Month_RefArray.shape)
print("IMERG12Month_RefArray is ",IMERG12Month_RefArray)
print("np.amin(np.isnan(IMERG12Month_RefArray).sum(axis=0)) is ",np.amin(np.isnan(IMERG12Month_RefArray).sum(axis=0)))
print("np.amax(np.isnan(IMERG12Month_RefArray).sum(axis=0)) is ",np.amax(np.isnan(IMERG12Month_RefArray).sum(axis=0)))
print("np.amin(np.isnan(IMERG12Month_RefArray).sum(axis=1)) is ",np.amin(np.isnan(IMERG12Month_RefArray).sum(axis=1)))
print("np.amax(np.isnan(IMERG12Month_RefArray).sum(axis=1)) is ",np.amax(np.isnan(IMERG12Month_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(IMERG12Month_RefArray),', overall max is ',np.nanmax(IMERG12Month_RefArray))

print("IMERG24Month_YYYYMMDD_Of_RefArray.shape is ",IMERG24Month_YYYYMMDD_Of_RefArray.shape)
print("IMERG24Month_YYYYMMDD_Of_RefArray is ",IMERG24Month_YYYYMMDD_Of_RefArray)

print("IMERG24Month_RefArray.shape is ",IMERG24Month_RefArray.shape)
print("IMERG24Month_RefArray is ",IMERG24Month_RefArray)
print("np.amin(np.isnan(IMERG24Month_RefArray).sum(axis=0)) is ",np.amin(np.isnan(IMERG24Month_RefArray).sum(axis=0)))
print("np.amax(np.isnan(IMERG24Month_RefArray).sum(axis=0)) is ",np.amax(np.isnan(IMERG24Month_RefArray).sum(axis=0)))
print("np.amin(np.isnan(IMERG24Month_RefArray).sum(axis=1)) is ",np.amin(np.isnan(IMERG24Month_RefArray).sum(axis=1)))
print("np.amax(np.isnan(IMERG24Month_RefArray).sum(axis=1)) is ",np.amax(np.isnan(IMERG24Month_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(IMERG24Month_RefArray),', overall max is ',np.nanmax(IMERG24Month_RefArray))

print("IMERG36Month_YYYYMMDD_Of_RefArray.shape is ",IMERG36Month_YYYYMMDD_Of_RefArray.shape)
print("IMERG36Month_YYYYMMDD_Of_RefArray is ",IMERG36Month_YYYYMMDD_Of_RefArray)

print("IMERG36Month_RefArray.shape is ",IMERG36Month_RefArray.shape)
print("IMERG36Month_RefArray is ",IMERG36Month_RefArray)
print("np.amin(np.isnan(IMERG36Month_RefArray).sum(axis=0)) is ",np.amin(np.isnan(IMERG36Month_RefArray).sum(axis=0)))
print("np.amax(np.isnan(IMERG36Month_RefArray).sum(axis=0)) is ",np.amax(np.isnan(IMERG36Month_RefArray).sum(axis=0)))
print("np.amin(np.isnan(IMERG36Month_RefArray).sum(axis=1)) is ",np.amin(np.isnan(IMERG36Month_RefArray).sum(axis=1)))
print("np.amax(np.isnan(IMERG36Month_RefArray).sum(axis=1)) is ",np.amax(np.isnan(IMERG36Month_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(IMERG36Month_RefArray),', overall max is ',np.nanmax(IMERG36Month_RefArray))

print("IMERG48Month_YYYYMMDD_Of_RefArray.shape is ",IMERG48Month_YYYYMMDD_Of_RefArray.shape)
print("IMERG48Month_YYYYMMDD_Of_RefArray is ",IMERG48Month_YYYYMMDD_Of_RefArray)

print("IMERG48Month_RefArray.shape is ",IMERG48Month_RefArray.shape)
print("IMERG48Month_RefArray is ",IMERG48Month_RefArray)
print("np.amin(np.isnan(IMERG48Month_RefArray).sum(axis=0)) is ",np.amin(np.isnan(IMERG48Month_RefArray).sum(axis=0)))
print("np.amax(np.isnan(IMERG48Month_RefArray).sum(axis=0)) is ",np.amax(np.isnan(IMERG48Month_RefArray).sum(axis=0)))
print("np.amin(np.isnan(IMERG48Month_RefArray).sum(axis=1)) is ",np.amin(np.isnan(IMERG48Month_RefArray).sum(axis=1)))
print("np.amax(np.isnan(IMERG48Month_RefArray).sum(axis=1)) is ",np.amax(np.isnan(IMERG48Month_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(IMERG48Month_RefArray),', overall max is ',np.nanmax(IMERG48Month_RefArray))

print("IMERG60Month_YYYYMMDD_Of_RefArray.shape is ",IMERG60Month_YYYYMMDD_Of_RefArray.shape)
print("IMERG60Month_YYYYMMDD_Of_RefArray is ",IMERG60Month_YYYYMMDD_Of_RefArray)

print("IMERG60Month_RefArray.shape is ",IMERG60Month_RefArray.shape)
print("IMERG60Month_RefArray is ",IMERG60Month_RefArray)
print("np.amin(np.isnan(IMERG60Month_RefArray).sum(axis=0)) is ",np.amin(np.isnan(IMERG60Month_RefArray).sum(axis=0)))
print("np.amax(np.isnan(IMERG60Month_RefArray).sum(axis=0)) is ",np.amax(np.isnan(IMERG60Month_RefArray).sum(axis=0)))
print("np.amin(np.isnan(IMERG60Month_RefArray).sum(axis=1)) is ",np.amin(np.isnan(IMERG60Month_RefArray).sum(axis=1)))
print("np.amax(np.isnan(IMERG60Month_RefArray).sum(axis=1)) is ",np.amax(np.isnan(IMERG60Month_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(IMERG60Month_RefArray),', overall max is ',np.nanmax(IMERG60Month_RefArray))

print("IMERG72Month_YYYYMMDD_Of_RefArray.shape is ",IMERG72Month_YYYYMMDD_Of_RefArray.shape)
print("IMERG72Month_YYYYMMDD_Of_RefArray is ",IMERG72Month_YYYYMMDD_Of_RefArray)

print("IMERG72Month_RefArray.shape is ",IMERG72Month_RefArray.shape)
print("IMERG72Month_RefArray is ",IMERG72Month_RefArray)
print("np.amin(np.isnan(IMERG72Month_RefArray).sum(axis=0)) is ",np.amin(np.isnan(IMERG72Month_RefArray).sum(axis=0)))
print("np.amax(np.isnan(IMERG72Month_RefArray).sum(axis=0)) is ",np.amax(np.isnan(IMERG72Month_RefArray).sum(axis=0)))
print("np.amin(np.isnan(IMERG72Month_RefArray).sum(axis=1)) is ",np.amin(np.isnan(IMERG72Month_RefArray).sum(axis=1)))
print("np.amax(np.isnan(IMERG72Month_RefArray).sum(axis=1)) is ",np.amax(np.isnan(IMERG72Month_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(IMERG72Month_RefArray),', overall max is ',np.nanmax(IMERG72Month_RefArray))




