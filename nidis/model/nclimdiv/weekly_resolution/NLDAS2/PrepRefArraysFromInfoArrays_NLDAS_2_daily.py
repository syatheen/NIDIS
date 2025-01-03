# Coded by Soni Yatheendradas
#         on Nov 17, 2021
from __future__ import division
import numpy as np
from datetime import date, datetime, timedelta

# BEGIN code arguments / editable section

InfoFilesDir = '/discover/nobackup/projects/nca/syatheen/NLDAS_2_daily_Npzs/'

NLDAS_2_daily_Info_BeginYYYYMMVecList = [1980, 1] # Beginning year and month 
NLDAS_2_daily_Info_EndYYYYMMVecList = [2021, 8] # Ending year and month 

#BEGIN subsection for concatenating monthly-containing-daily Arrays

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
        ThisYYYYMM_Info = np.load(InfoFilesDir + WhichLSM + '_' + WhichVariable + '_' + format(WhichYear, '04') + format(WhichMonth, '02') + '_ClimDivs.PERW.npz')
      elif ( (WhichVariable == 'EVAP') or 
             (WhichVariable == 'SWE') or
             (WhichVariable == 'RUN') ):
        ThisYYYYMM_Info = np.load(InfoFilesDir + WhichLSM + '_' + WhichVariable + '_' + format(WhichYear, '04') + format(WhichMonth, '02') + '_ClimDivs.PERW.50AdjustTo0.npz')
      elif (WhichVariable == 'STRM') :
        ThisYYYYMM_Info = np.load(InfoFilesDir + WhichLSM + '_' + WhichVariable + '_' + format(WhichYear, '04') + format(WhichMonth, '02') + '_' + WhichHUC + '_ClimDivs.PERW.50AdjustTo0.npz')
 
      ThisYYYYMMDD_Of_InfoArrayForPrcntl = ThisYYYYMM_Info['YYYYMMDD_Of_RefPrcntlArray']
      ThisInfoArrayForPrcntl = ThisYYYYMM_Info['RefPrcntlArray']
  
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

#end of def ConcatMonthlyArraysContainingDailyInfo(WhichLSM, WhichVariable, WhichHUC, NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)

Mosaic_1MSM_daily_YYYYMMDD_Of_InfoArray, Mosaic_1MSM_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Mosaic', '1MSM', '', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
Noah_1MSM_daily_YYYYMMDD_Of_InfoArray, Noah_1MSM_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Noah', '1MSM', '', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
SAC_1MSM_daily_YYYYMMDD_Of_InfoArray, SAC_1MSM_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo('SAC', '1MSM', '', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
VIC_1MSM_daily_YYYYMMDD_Of_InfoArray, VIC_1MSM_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo('VIC', '1MSM', '', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
Mosaic_TCSM_daily_YYYYMMDD_Of_InfoArray, Mosaic_TCSM_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Mosaic', 'TCSM', '', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
Noah_TCSM_daily_YYYYMMDD_Of_InfoArray, Noah_TCSM_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Noah', 'TCSM', '', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
SAC_TCSM_daily_YYYYMMDD_Of_InfoArray, SAC_TCSM_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo('SAC', 'TCSM', '', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
VIC_TCSM_daily_YYYYMMDD_Of_InfoArray, VIC_TCSM_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo('VIC', 'TCSM', '', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
Mosaic_EVAP_daily_YYYYMMDD_Of_InfoArray, Mosaic_EVAP_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Mosaic', 'EVAP', '', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
Noah_EVAP_daily_YYYYMMDD_Of_InfoArray, Noah_EVAP_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Noah', 'EVAP', '', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
SAC_EVAP_daily_YYYYMMDD_Of_InfoArray, SAC_EVAP_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo('SAC', 'EVAP', '', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
VIC_EVAP_daily_YYYYMMDD_Of_InfoArray, VIC_EVAP_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo('VIC', 'EVAP', '', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
Mosaic_SWE_daily_YYYYMMDD_Of_InfoArray, Mosaic_SWE_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Mosaic', 'SWE', '', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
Noah_SWE_daily_YYYYMMDD_Of_InfoArray, Noah_SWE_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Noah', 'SWE', '', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
SAC_SWE_daily_YYYYMMDD_Of_InfoArray, SAC_SWE_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo('SAC', 'SWE', '', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
VIC_SWE_daily_YYYYMMDD_Of_InfoArray, VIC_SWE_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo('VIC', 'SWE', '', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
Mosaic_RUN_daily_YYYYMMDD_Of_InfoArray, Mosaic_RUN_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Mosaic', 'RUN', '', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
Noah_RUN_daily_YYYYMMDD_Of_InfoArray, Noah_RUN_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Noah', 'RUN', '', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
SAC_RUN_daily_YYYYMMDD_Of_InfoArray, SAC_RUN_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo('SAC', 'RUN', '', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
VIC_RUN_daily_YYYYMMDD_Of_InfoArray, VIC_RUN_daily_InfoArray = ConcatMonthlyArraysContainingDailyInfo('VIC', 'RUN', '', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
Mosaic_STRM_daily_H02_YYYYMMDD_Of_InfoArray, Mosaic_STRM_daily_H02_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Mosaic', 'STRM', 'H02', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
Noah_STRM_daily_H02_YYYYMMDD_Of_InfoArray, Noah_STRM_daily_H02_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Noah', 'STRM', 'H02', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
SAC_STRM_daily_H02_YYYYMMDD_Of_InfoArray, SAC_STRM_daily_H02_InfoArray = ConcatMonthlyArraysContainingDailyInfo('SAC', 'STRM', 'H02', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
VIC_STRM_daily_H02_YYYYMMDD_Of_InfoArray, VIC_STRM_daily_H02_InfoArray = ConcatMonthlyArraysContainingDailyInfo('VIC', 'STRM', 'H02', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
Mosaic_STRM_daily_H04_YYYYMMDD_Of_InfoArray, Mosaic_STRM_daily_H04_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Mosaic', 'STRM', 'H04', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
Noah_STRM_daily_H04_YYYYMMDD_Of_InfoArray, Noah_STRM_daily_H04_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Noah', 'STRM', 'H04', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
SAC_STRM_daily_H04_YYYYMMDD_Of_InfoArray, SAC_STRM_daily_H04_InfoArray = ConcatMonthlyArraysContainingDailyInfo('SAC', 'STRM', 'H04', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
VIC_STRM_daily_H04_YYYYMMDD_Of_InfoArray, VIC_STRM_daily_H04_InfoArray = ConcatMonthlyArraysContainingDailyInfo('VIC', 'STRM', 'H04', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
Mosaic_STRM_daily_H06_YYYYMMDD_Of_InfoArray, Mosaic_STRM_daily_H06_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Mosaic', 'STRM', 'H06', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
Noah_STRM_daily_H06_YYYYMMDD_Of_InfoArray, Noah_STRM_daily_H06_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Noah', 'STRM', 'H06', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
SAC_STRM_daily_H06_YYYYMMDD_Of_InfoArray, SAC_STRM_daily_H06_InfoArray = ConcatMonthlyArraysContainingDailyInfo('SAC', 'STRM', 'H06', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
VIC_STRM_daily_H06_YYYYMMDD_Of_InfoArray, VIC_STRM_daily_H06_InfoArray = ConcatMonthlyArraysContainingDailyInfo('VIC', 'STRM', 'H06', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
Mosaic_STRM_daily_H08_YYYYMMDD_Of_InfoArray, Mosaic_STRM_daily_H08_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Mosaic', 'STRM', 'H08', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
Noah_STRM_daily_H08_YYYYMMDD_Of_InfoArray, Noah_STRM_daily_H08_InfoArray = ConcatMonthlyArraysContainingDailyInfo('Noah', 'STRM', 'H08', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
SAC_STRM_daily_H08_YYYYMMDD_Of_InfoArray, SAC_STRM_daily_H08_InfoArray = ConcatMonthlyArraysContainingDailyInfo('SAC', 'STRM', 'H08', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)
VIC_STRM_daily_H08_YYYYMMDD_Of_InfoArray, VIC_STRM_daily_H08_InfoArray = ConcatMonthlyArraysContainingDailyInfo('VIC', 'STRM', 'H08', NLDAS_2_daily_Info_BeginYYYYMMVecList, NLDAS_2_daily_Info_EndYYYYMMVecList)

#END subsection for concatenating monthly-containing-daily Arrays

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

NLDAS_2_Ref_BeginDateVecList = FindTuesdayAfter(Mosaic_1MSM_daily_YYYYMMDD_Of_InfoArray[0,0])  # NLDAS_2_daily beginning year, month, day of month, this is also a Tuesday
NLDAS_2_Ref_EndDateVecList = FindTuesdayBefore(Mosaic_1MSM_daily_YYYYMMDD_Of_InfoArray[-1,0])  # NLDAS_2_daily ending year, month, day of month, this is also a Tuesday

Mosaic_1MSM_RefFileName = 'RefArrays/ClimDiv_Mosaic_1MSM_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
Noah_1MSM_RefFileName = 'RefArrays/ClimDiv_Noah_1MSM_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
SAC_1MSM_RefFileName = 'RefArrays/ClimDiv_SAC_1MSM_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
VIC_1MSM_RefFileName = 'RefArrays/ClimDiv_VIC_1MSM_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
Mosaic_TCSM_RefFileName = 'RefArrays/ClimDiv_Mosaic_TCSM_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
Noah_TCSM_RefFileName = 'RefArrays/ClimDiv_Noah_TCSM_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
SAC_TCSM_RefFileName = 'RefArrays/ClimDiv_SAC_TCSM_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
VIC_TCSM_RefFileName = 'RefArrays/ClimDiv_VIC_TCSM_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
Mosaic_EVAP_RefFileName = 'RefArrays/ClimDiv_Mosaic_EVAP_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
Noah_EVAP_RefFileName = 'RefArrays/ClimDiv_Noah_EVAP_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
SAC_EVAP_RefFileName = 'RefArrays/ClimDiv_SAC_EVAP_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
VIC_EVAP_RefFileName = 'RefArrays/ClimDiv_VIC_EVAP_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
Mosaic_SWE_RefFileName = 'RefArrays/ClimDiv_Mosaic_SWE_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
Noah_SWE_RefFileName = 'RefArrays/ClimDiv_Noah_SWE_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
SAC_SWE_RefFileName = 'RefArrays/ClimDiv_SAC_SWE_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
VIC_SWE_RefFileName = 'RefArrays/ClimDiv_VIC_SWE_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
Mosaic_RUN_RefFileName = 'RefArrays/ClimDiv_Mosaic_RUN_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
Noah_RUN_RefFileName = 'RefArrays/ClimDiv_Noah_RUN_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
SAC_RUN_RefFileName = 'RefArrays/ClimDiv_SAC_RUN_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
VIC_RUN_RefFileName = 'RefArrays/ClimDiv_VIC_RUN_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
Mosaic_STRM_H02_RefFileName = 'RefArrays/ClimDiv_Mosaic_STRM_H02_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
Noah_STRM_H02_RefFileName = 'RefArrays/ClimDiv_Noah_STRM_H02_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
SAC_STRM_H02_RefFileName = 'RefArrays/ClimDiv_SAC_STRM_H02_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
VIC_STRM_H02_RefFileName = 'RefArrays/ClimDiv_VIC_STRM_H02_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
Mosaic_STRM_H04_RefFileName = 'RefArrays/ClimDiv_Mosaic_STRM_H04_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
Noah_STRM_H04_RefFileName = 'RefArrays/ClimDiv_Noah_STRM_H04_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
SAC_STRM_H04_RefFileName = 'RefArrays/ClimDiv_SAC_STRM_H04_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
VIC_STRM_H04_RefFileName = 'RefArrays/ClimDiv_VIC_STRM_H04_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
Mosaic_STRM_H06_RefFileName = 'RefArrays/ClimDiv_Mosaic_STRM_H06_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
Noah_STRM_H06_RefFileName = 'RefArrays/ClimDiv_Noah_STRM_H06_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
SAC_STRM_H06_RefFileName = 'RefArrays/ClimDiv_SAC_STRM_H06_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
VIC_STRM_H06_RefFileName = 'RefArrays/ClimDiv_VIC_STRM_H06_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
Mosaic_STRM_H08_RefFileName = 'RefArrays/ClimDiv_Mosaic_STRM_H08_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
Noah_STRM_H08_RefFileName = 'RefArrays/ClimDiv_Noah_STRM_H08_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
SAC_STRM_H08_RefFileName = 'RefArrays/ClimDiv_SAC_STRM_H08_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'
VIC_STRM_H08_RefFileName = 'RefArrays/ClimDiv_VIC_STRM_H08_'+format(NLDAS_2_Ref_BeginDateVecList[0],'04')+format(NLDAS_2_Ref_BeginDateVecList[1],'02')+format(NLDAS_2_Ref_BeginDateVecList[2],'02')+'To'+format(NLDAS_2_Ref_EndDateVecList[0],'04')+format(NLDAS_2_Ref_EndDateVecList[1],'02')+format(NLDAS_2_Ref_EndDateVecList[2],'02')+'.npz'

# END code arguments / editable section

import sys
from calendar import monthrange
import time

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

NLDAS_2_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(Mosaic_1MSM_daily_YYYYMMDD_Of_InfoArray, 3, 'NLDAS_2', np.NaN)

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

NLDAS_2_RealDatesList_Of_RefArray, NLDAS_2_YYYYMMDD_Of_RefArray  = GetTimeInfoOfRefArray(NLDAS_2_Ref_BeginDate, NLDAS_2_Ref_EndDate)

#End calculating real dates list for reference arrays

Mosaic_1MSM_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], Mosaic_1MSM_daily_InfoArray.shape[1]])
Mosaic_1MSM_RefArray[:] = np.NaN
Noah_1MSM_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], Noah_1MSM_daily_InfoArray.shape[1]])
Noah_1MSM_RefArray[:] = np.NaN
SAC_1MSM_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], SAC_1MSM_daily_InfoArray.shape[1]])
SAC_1MSM_RefArray[:] = np.NaN
VIC_1MSM_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], VIC_1MSM_daily_InfoArray.shape[1]])
VIC_1MSM_RefArray[:] = np.NaN
Mosaic_TCSM_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], Mosaic_TCSM_daily_InfoArray.shape[1]])
Mosaic_TCSM_RefArray[:] = np.NaN
Noah_TCSM_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], Noah_TCSM_daily_InfoArray.shape[1]])
Noah_TCSM_RefArray[:] = np.NaN
SAC_TCSM_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], SAC_TCSM_daily_InfoArray.shape[1]])
SAC_TCSM_RefArray[:] = np.NaN
VIC_TCSM_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], VIC_TCSM_daily_InfoArray.shape[1]])
VIC_TCSM_RefArray[:] = np.NaN
Mosaic_EVAP_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], Mosaic_EVAP_daily_InfoArray.shape[1]])
Mosaic_EVAP_RefArray[:] = np.NaN
Noah_EVAP_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], Noah_EVAP_daily_InfoArray.shape[1]])
Noah_EVAP_RefArray[:] = np.NaN
SAC_EVAP_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], SAC_EVAP_daily_InfoArray.shape[1]])
SAC_EVAP_RefArray[:] = np.NaN
VIC_EVAP_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], VIC_EVAP_daily_InfoArray.shape[1]])
VIC_EVAP_RefArray[:] = np.NaN
Mosaic_SWE_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], Mosaic_SWE_daily_InfoArray.shape[1]])
Mosaic_SWE_RefArray[:] = np.NaN
Noah_SWE_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], Noah_SWE_daily_InfoArray.shape[1]])
Noah_SWE_RefArray[:] = np.NaN
SAC_SWE_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], SAC_SWE_daily_InfoArray.shape[1]])
SAC_SWE_RefArray[:] = np.NaN
VIC_SWE_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], VIC_SWE_daily_InfoArray.shape[1]])
VIC_SWE_RefArray[:] = np.NaN
Mosaic_RUN_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], Mosaic_RUN_daily_InfoArray.shape[1]])
Mosaic_RUN_RefArray[:] = np.NaN
Noah_RUN_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], Noah_RUN_daily_InfoArray.shape[1]])
Noah_RUN_RefArray[:] = np.NaN
SAC_RUN_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], SAC_RUN_daily_InfoArray.shape[1]])
SAC_RUN_RefArray[:] = np.NaN
VIC_RUN_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], VIC_RUN_daily_InfoArray.shape[1]])
VIC_RUN_RefArray[:] = np.NaN
Mosaic_STRM_H02_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], Mosaic_STRM_daily_H02_InfoArray.shape[1]])
Mosaic_STRM_H02_RefArray[:] = np.NaN
Noah_STRM_H02_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], Noah_STRM_daily_H02_InfoArray.shape[1]])
Noah_STRM_H02_RefArray[:] = np.NaN
SAC_STRM_H02_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], SAC_STRM_daily_H02_InfoArray.shape[1]])
SAC_STRM_H02_RefArray[:] = np.NaN
VIC_STRM_H02_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], VIC_STRM_daily_H02_InfoArray.shape[1]])
VIC_STRM_H02_RefArray[:] = np.NaN
Mosaic_STRM_H04_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], Mosaic_STRM_daily_H04_InfoArray.shape[1]])
Mosaic_STRM_H04_RefArray[:] = np.NaN
Noah_STRM_H04_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], Noah_STRM_daily_H04_InfoArray.shape[1]])
Noah_STRM_H04_RefArray[:] = np.NaN
SAC_STRM_H04_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], SAC_STRM_daily_H04_InfoArray.shape[1]])
SAC_STRM_H04_RefArray[:] = np.NaN
VIC_STRM_H04_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], VIC_STRM_daily_H04_InfoArray.shape[1]])
VIC_STRM_H04_RefArray[:] = np.NaN
Mosaic_STRM_H06_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], Mosaic_STRM_daily_H06_InfoArray.shape[1]])
Mosaic_STRM_H06_RefArray[:] = np.NaN
Noah_STRM_H06_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], Noah_STRM_daily_H06_InfoArray.shape[1]])
Noah_STRM_H06_RefArray[:] = np.NaN
SAC_STRM_H06_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], SAC_STRM_daily_H06_InfoArray.shape[1]])
SAC_STRM_H06_RefArray[:] = np.NaN
VIC_STRM_H06_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], VIC_STRM_daily_H06_InfoArray.shape[1]])
VIC_STRM_H06_RefArray[:] = np.NaN
Mosaic_STRM_H08_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], Mosaic_STRM_daily_H08_InfoArray.shape[1]])
Mosaic_STRM_H08_RefArray[:] = np.NaN
Noah_STRM_H08_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], Noah_STRM_daily_H08_InfoArray.shape[1]])
Noah_STRM_H08_RefArray[:] = np.NaN
SAC_STRM_H08_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], SAC_STRM_daily_H08_InfoArray.shape[1]])
SAC_STRM_H08_RefArray[:] = np.NaN
VIC_STRM_H08_RefArray = np.empty([ NLDAS_2_YYYYMMDD_Of_RefArray.shape[0], VIC_STRM_daily_H08_InfoArray.shape[1]])
VIC_STRM_H08_RefArray[:] = np.NaN

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

Mosaic_1MSM_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, Mosaic_1MSM_daily_InfoArray, Mosaic_1MSM_RefArray, 7)
Noah_1MSM_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, Noah_1MSM_daily_InfoArray, Noah_1MSM_RefArray, 7)
SAC_1MSM_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, SAC_1MSM_daily_InfoArray, SAC_1MSM_RefArray, 7)
VIC_1MSM_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, VIC_1MSM_daily_InfoArray, VIC_1MSM_RefArray, 7)
Mosaic_TCSM_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, Mosaic_TCSM_daily_InfoArray, Mosaic_TCSM_RefArray, 7)
Noah_TCSM_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, Noah_TCSM_daily_InfoArray, Noah_TCSM_RefArray, 7)
SAC_TCSM_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, SAC_TCSM_daily_InfoArray, SAC_TCSM_RefArray, 7)
VIC_TCSM_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, VIC_TCSM_daily_InfoArray, VIC_TCSM_RefArray, 7)
Mosaic_EVAP_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, Mosaic_EVAP_daily_InfoArray, Mosaic_EVAP_RefArray, 7)
Noah_EVAP_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, Noah_EVAP_daily_InfoArray, Noah_EVAP_RefArray, 7)
SAC_EVAP_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, SAC_EVAP_daily_InfoArray, SAC_EVAP_RefArray, 7)
VIC_EVAP_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, VIC_EVAP_daily_InfoArray, VIC_EVAP_RefArray, 7)
Mosaic_SWE_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, Mosaic_SWE_daily_InfoArray, Mosaic_SWE_RefArray, 7)
Noah_SWE_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, Noah_SWE_daily_InfoArray, Noah_SWE_RefArray, 7)
SAC_SWE_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, SAC_SWE_daily_InfoArray, SAC_SWE_RefArray, 7)
VIC_SWE_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, VIC_SWE_daily_InfoArray, VIC_SWE_RefArray, 7)
Mosaic_RUN_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, Mosaic_RUN_daily_InfoArray, Mosaic_RUN_RefArray, 7)
Noah_RUN_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, Noah_RUN_daily_InfoArray, Noah_RUN_RefArray, 7)
SAC_RUN_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, SAC_RUN_daily_InfoArray, SAC_RUN_RefArray, 7)
VIC_RUN_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, VIC_RUN_daily_InfoArray, VIC_RUN_RefArray, 7)
Mosaic_STRM_H02_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, Mosaic_STRM_daily_H02_InfoArray, Mosaic_STRM_H02_RefArray, 7)
Noah_STRM_H02_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, Noah_STRM_daily_H02_InfoArray, Noah_STRM_H02_RefArray, 7)
SAC_STRM_H02_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, SAC_STRM_daily_H02_InfoArray, SAC_STRM_H02_RefArray, 7)
VIC_STRM_H02_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, VIC_STRM_daily_H02_InfoArray, VIC_STRM_H02_RefArray, 7)
Mosaic_STRM_H04_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, Mosaic_STRM_daily_H04_InfoArray, Mosaic_STRM_H04_RefArray, 7)
Noah_STRM_H04_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, Noah_STRM_daily_H04_InfoArray, Noah_STRM_H04_RefArray, 7)
SAC_STRM_H04_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, SAC_STRM_daily_H04_InfoArray, SAC_STRM_H04_RefArray, 7)
VIC_STRM_H04_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, VIC_STRM_daily_H04_InfoArray, VIC_STRM_H04_RefArray, 7)
Mosaic_STRM_H06_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, Mosaic_STRM_daily_H06_InfoArray, Mosaic_STRM_H06_RefArray, 7)
Noah_STRM_H06_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, Noah_STRM_daily_H06_InfoArray, Noah_STRM_H06_RefArray, 7)
SAC_STRM_H06_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, SAC_STRM_daily_H06_InfoArray, SAC_STRM_H06_RefArray, 7)
VIC_STRM_H06_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, VIC_STRM_daily_H06_InfoArray, VIC_STRM_H06_RefArray, 7)
Mosaic_STRM_H08_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, Mosaic_STRM_daily_H08_InfoArray, Mosaic_STRM_H08_RefArray, 7)
Noah_STRM_H08_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, Noah_STRM_daily_H08_InfoArray, Noah_STRM_H08_RefArray, 7)
SAC_STRM_H08_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, SAC_STRM_daily_H08_InfoArray, SAC_STRM_H08_RefArray, 7)
VIC_STRM_H08_RefArray = TimeMeanValues(NLDAS_2_RealDatesList_Of_InfoArray, NLDAS_2_RealDatesList_Of_RefArray, VIC_STRM_daily_H08_InfoArray, VIC_STRM_H08_RefArray, 7)

print("--- %s seconds ---" % (time.time() - start_time))

np.savez_compressed(Mosaic_1MSM_RefFileName, Mosaic_1MSM_RefArray = Mosaic_1MSM_RefArray, Mosaic_1MSM_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(Noah_1MSM_RefFileName, Noah_1MSM_RefArray = Noah_1MSM_RefArray, Noah_1MSM_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(SAC_1MSM_RefFileName, SAC_1MSM_RefArray = SAC_1MSM_RefArray, SAC_1MSM_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(VIC_1MSM_RefFileName, VIC_1MSM_RefArray = VIC_1MSM_RefArray, VIC_1MSM_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(Mosaic_TCSM_RefFileName, Mosaic_TCSM_RefArray = Mosaic_TCSM_RefArray, Mosaic_TCSM_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(Noah_TCSM_RefFileName, Noah_TCSM_RefArray = Noah_TCSM_RefArray, Noah_TCSM_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(SAC_TCSM_RefFileName, SAC_TCSM_RefArray = SAC_TCSM_RefArray, SAC_TCSM_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(VIC_TCSM_RefFileName, VIC_TCSM_RefArray = VIC_TCSM_RefArray, VIC_TCSM_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(Mosaic_EVAP_RefFileName, Mosaic_EVAP_RefArray = Mosaic_EVAP_RefArray, Mosaic_EVAP_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(Noah_EVAP_RefFileName, Noah_EVAP_RefArray = Noah_EVAP_RefArray, Noah_EVAP_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(SAC_EVAP_RefFileName, SAC_EVAP_RefArray = SAC_EVAP_RefArray, SAC_EVAP_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(VIC_EVAP_RefFileName, VIC_EVAP_RefArray = VIC_EVAP_RefArray, VIC_EVAP_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(Mosaic_SWE_RefFileName, Mosaic_SWE_RefArray = Mosaic_SWE_RefArray, Mosaic_SWE_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(Noah_SWE_RefFileName, Noah_SWE_RefArray = Noah_SWE_RefArray, Noah_SWE_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(SAC_SWE_RefFileName, SAC_SWE_RefArray = SAC_SWE_RefArray, SAC_SWE_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(VIC_SWE_RefFileName, VIC_SWE_RefArray = VIC_SWE_RefArray, VIC_SWE_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(Mosaic_RUN_RefFileName, Mosaic_RUN_RefArray = Mosaic_RUN_RefArray, Mosaic_RUN_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(Noah_RUN_RefFileName, Noah_RUN_RefArray = Noah_RUN_RefArray, Noah_RUN_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(SAC_RUN_RefFileName, SAC_RUN_RefArray = SAC_RUN_RefArray, SAC_RUN_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(VIC_RUN_RefFileName, VIC_RUN_RefArray = VIC_RUN_RefArray, VIC_RUN_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(Mosaic_STRM_H02_RefFileName, Mosaic_STRM_H02_RefArray = Mosaic_STRM_H02_RefArray, Mosaic_STRM_H02_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(Noah_STRM_H02_RefFileName, Noah_STRM_H02_RefArray = Noah_STRM_H02_RefArray, Noah_STRM_H02_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(SAC_STRM_H02_RefFileName, SAC_STRM_H02_RefArray = SAC_STRM_H02_RefArray, SAC_STRM_H02_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(VIC_STRM_H02_RefFileName, VIC_STRM_H02_RefArray = VIC_STRM_H02_RefArray, VIC_STRM_H02_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(Mosaic_STRM_H04_RefFileName, Mosaic_STRM_H04_RefArray = Mosaic_STRM_H04_RefArray, Mosaic_STRM_H04_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(Noah_STRM_H04_RefFileName, Noah_STRM_H04_RefArray = Noah_STRM_H04_RefArray, Noah_STRM_H04_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(SAC_STRM_H04_RefFileName, SAC_STRM_H04_RefArray = SAC_STRM_H04_RefArray, SAC_STRM_H04_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(VIC_STRM_H04_RefFileName, VIC_STRM_H04_RefArray = VIC_STRM_H04_RefArray, VIC_STRM_H04_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(Mosaic_STRM_H06_RefFileName, Mosaic_STRM_H06_RefArray = Mosaic_STRM_H06_RefArray, Mosaic_STRM_H06_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(Noah_STRM_H06_RefFileName, Noah_STRM_H06_RefArray = Noah_STRM_H06_RefArray, Noah_STRM_H06_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(SAC_STRM_H06_RefFileName, SAC_STRM_H06_RefArray = SAC_STRM_H06_RefArray, SAC_STRM_H06_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(VIC_STRM_H06_RefFileName, VIC_STRM_H06_RefArray = VIC_STRM_H06_RefArray, VIC_STRM_H06_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(Mosaic_STRM_H08_RefFileName, Mosaic_STRM_H08_RefArray = Mosaic_STRM_H08_RefArray, Mosaic_STRM_H08_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(Noah_STRM_H08_RefFileName, Noah_STRM_H08_RefArray = Noah_STRM_H08_RefArray, Noah_STRM_H08_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(SAC_STRM_H08_RefFileName, SAC_STRM_H08_RefArray = SAC_STRM_H08_RefArray, SAC_STRM_H08_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)
np.savez_compressed(VIC_STRM_H08_RefFileName, VIC_STRM_H08_RefArray = VIC_STRM_H08_RefArray, VIC_STRM_H08_YYYYMMDD_Of_RefArray = NLDAS_2_YYYYMMDD_Of_RefArray)

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
#end of def PrintArrayInfo(ThisArray)

PrintArrayInfo(NLDAS_2_YYYYMMDD_Of_RefArray, 'YYYYMMDD')

PrintArrayInfo(Mosaic_1MSM_RefArray, 'Mosaic_1MSM')
PrintArrayInfo(Noah_1MSM_RefArray, 'Noah_1MSM')
PrintArrayInfo(SAC_1MSM_RefArray, 'SAC_1MSM')
PrintArrayInfo(VIC_1MSM_RefArray, 'VIC_1MSM')
PrintArrayInfo(Mosaic_TCSM_RefArray, 'Mosaic_TCSM')
PrintArrayInfo(Noah_TCSM_RefArray, 'Noah_TCSM')
PrintArrayInfo(SAC_TCSM_RefArray, 'SAC_TCSM')
PrintArrayInfo(VIC_TCSM_RefArray, 'VIC_TCSM')
PrintArrayInfo(Mosaic_EVAP_RefArray, 'Mosaic_EVAP')
PrintArrayInfo(Noah_EVAP_RefArray, 'Noah_EVAP')
PrintArrayInfo(SAC_EVAP_RefArray, 'SAC_EVAP')
PrintArrayInfo(VIC_EVAP_RefArray, 'VIC_EVAP')
PrintArrayInfo(Mosaic_SWE_RefArray, 'Mosaic_SWE')
PrintArrayInfo(Noah_SWE_RefArray, 'Noah_SWE')
PrintArrayInfo(SAC_SWE_RefArray, 'SAC_SWE')
PrintArrayInfo(VIC_SWE_RefArray, 'VIC_SWE')
PrintArrayInfo(Mosaic_RUN_RefArray, 'Mosaic_RUN')
PrintArrayInfo(Noah_RUN_RefArray, 'Noah_RUN')
PrintArrayInfo(SAC_RUN_RefArray, 'SAC_RUN')
PrintArrayInfo(VIC_RUN_RefArray, 'VIC_RUN')
PrintArrayInfo(Mosaic_STRM_H02_RefArray, 'Mosaic_STRM_H02')
PrintArrayInfo(Noah_STRM_H02_RefArray, 'Noah_STRM_H02')
PrintArrayInfo(SAC_STRM_H02_RefArray, 'SAC_STRM_H02')
PrintArrayInfo(VIC_STRM_H02_RefArray, 'VIC_STRM_H02')
PrintArrayInfo(Mosaic_STRM_H04_RefArray, 'Mosaic_STRM_H04')
PrintArrayInfo(Noah_STRM_H04_RefArray, 'Noah_STRM_H04')
PrintArrayInfo(SAC_STRM_H04_RefArray, 'SAC_STRM_H04')
PrintArrayInfo(VIC_STRM_H04_RefArray, 'VIC_STRM_H04')
PrintArrayInfo(Mosaic_STRM_H06_RefArray, 'Mosaic_STRM_H06')
PrintArrayInfo(Noah_STRM_H06_RefArray, 'Noah_STRM_H06')
PrintArrayInfo(SAC_STRM_H06_RefArray, 'SAC_STRM_H06')
PrintArrayInfo(VIC_STRM_H06_RefArray, 'VIC_STRM_H06')
PrintArrayInfo(Mosaic_STRM_H08_RefArray, 'Mosaic_STRM_H08')
PrintArrayInfo(Noah_STRM_H08_RefArray, 'Noah_STRM_H08')
PrintArrayInfo(SAC_STRM_H08_RefArray, 'SAC_STRM_H08')
PrintArrayInfo(VIC_STRM_H08_RefArray, 'VIC_STRM_H08')


