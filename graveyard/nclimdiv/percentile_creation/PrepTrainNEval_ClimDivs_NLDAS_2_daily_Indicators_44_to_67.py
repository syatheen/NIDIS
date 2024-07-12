# Coded by Soni Yatheendradas
#         on Nov 18, 2021
from __future__ import division
from datetime import date, datetime, timedelta
import numpy as np
import sys
from CreateMonthlyLists_YYYYMMDDAndArray_File import CreateMonthlyLists_YYYYMMDDAndArray
from PrepTrainPortion_ClimDivs_OverallPercBased_File import PrepTrainPortion_ClimDivs_OverallPercBased
from PrepTrainPortion_ClimDivs_MonthlyPercBased_File import PrepTrainPortion_ClimDivs_MonthlyPercBased
from PrepEvalPortions_ClimDivs_OverallPercBased_File import PrepEvalPortions_ClimDivs_OverallPercBased
from PrepEvalPortions_ClimDivs_MonthlyPercBased_File import PrepEvalPortions_ClimDivs_MonthlyPercBased
from PrintInfoAboutArray_File import PrintInfoAboutArray
from PrintInfoAboutArray_2_File import PrintInfoAboutArray_2
from PrintInfoAboutArray_3_File import PrintInfoAboutArray_3

# BEGIN code arguments / editable section

Training_BeginDateVecList = [2006, 1, 3] # Beginning training year, month, day of month, this is also a Tuesday
Training_EndDateVecList = [2018, 12, 25] # Ending training year, month, day of month, this is also a Tuesday

Eval_BeginDateVecList = [2019, 1, 1] # Beginning evaluation year, month, day of month, this is also a Tuesday
Eval_EndDateVecList = [2019, 12, 31] # Ending evaluation year, month, day of month, this is also a Tuesday

Mosaic_1MSM_RefFileName = 'RefArrays/ClimDiv_Mosaic_1MSM_19800101To20210831.npz'
Noah_1MSM_RefFileName = 'RefArrays/ClimDiv_Noah_1MSM_19800101To20210831.npz'
SAC_1MSM_RefFileName = 'RefArrays/ClimDiv_SAC_1MSM_19800101To20210831.npz'
VIC_1MSM_RefFileName = 'RefArrays/ClimDiv_VIC_1MSM_19800101To20210831.npz'
Mosaic_TCSM_RefFileName = 'RefArrays/ClimDiv_Mosaic_TCSM_19800101To20210831.npz'
Noah_TCSM_RefFileName = 'RefArrays/ClimDiv_Noah_TCSM_19800101To20210831.npz'
SAC_TCSM_RefFileName = 'RefArrays/ClimDiv_SAC_TCSM_19800101To20210831.npz'
VIC_TCSM_RefFileName = 'RefArrays/ClimDiv_VIC_TCSM_19800101To20210831.npz'
Mosaic_EVAP_RefFileName = 'RefArrays/ClimDiv_Mosaic_EVAP_19800101To20210831.npz'
Noah_EVAP_RefFileName = 'RefArrays/ClimDiv_Noah_EVAP_19800101To20210831.npz'
SAC_EVAP_RefFileName = 'RefArrays/ClimDiv_SAC_EVAP_19800101To20210831.npz'
VIC_EVAP_RefFileName = 'RefArrays/ClimDiv_VIC_EVAP_19800101To20210831.npz'
Mosaic_SWE_RefFileName = 'RefArrays/ClimDiv_Mosaic_SWE_19800101To20210831.npz'
Noah_SWE_RefFileName = 'RefArrays/ClimDiv_Noah_SWE_19800101To20210831.npz'
SAC_SWE_RefFileName = 'RefArrays/ClimDiv_SAC_SWE_19800101To20210831.npz'
VIC_SWE_RefFileName = 'RefArrays/ClimDiv_VIC_SWE_19800101To20210831.npz'
Mosaic_RUN_RefFileName = 'RefArrays/ClimDiv_Mosaic_RUN_19800101To20210831.npz'
Noah_RUN_RefFileName = 'RefArrays/ClimDiv_Noah_RUN_19800101To20210831.npz'
SAC_RUN_RefFileName = 'RefArrays/ClimDiv_SAC_RUN_19800101To20210831.npz'
VIC_RUN_RefFileName = 'RefArrays/ClimDiv_VIC_RUN_19800101To20210831.npz'
Mosaic_STRM_H02_RefFileName = 'RefArrays/ClimDiv_Mosaic_STRM_H02_19800101To20210831.npz'
Noah_STRM_H02_RefFileName = 'RefArrays/ClimDiv_Noah_STRM_H02_19800101To20210831.npz'
SAC_STRM_H02_RefFileName = 'RefArrays/ClimDiv_SAC_STRM_H02_19800101To20210831.npz'
VIC_STRM_H02_RefFileName = 'RefArrays/ClimDiv_VIC_STRM_H02_19800101To20210831.npz'
Mosaic_STRM_H04_RefFileName = 'RefArrays/ClimDiv_Mosaic_STRM_H04_19800101To20210831.npz'
Noah_STRM_H04_RefFileName = 'RefArrays/ClimDiv_Noah_STRM_H04_19800101To20210831.npz'
SAC_STRM_H04_RefFileName = 'RefArrays/ClimDiv_SAC_STRM_H04_19800101To20210831.npz'
VIC_STRM_H04_RefFileName = 'RefArrays/ClimDiv_VIC_STRM_H04_19800101To20210831.npz'
Mosaic_STRM_H06_RefFileName = 'RefArrays/ClimDiv_Mosaic_STRM_H06_19800101To20210831.npz'
Noah_STRM_H06_RefFileName = 'RefArrays/ClimDiv_Noah_STRM_H06_19800101To20210831.npz'
SAC_STRM_H06_RefFileName = 'RefArrays/ClimDiv_SAC_STRM_H06_19800101To20210831.npz'
VIC_STRM_H06_RefFileName = 'RefArrays/ClimDiv_VIC_STRM_H06_19800101To20210831.npz'
Mosaic_STRM_H08_RefFileName = 'RefArrays/ClimDiv_Mosaic_STRM_H08_19800101To20210831.npz'
Noah_STRM_H08_RefFileName = 'RefArrays/ClimDiv_Noah_STRM_H08_19800101To20210831.npz'
SAC_STRM_H08_RefFileName = 'RefArrays/ClimDiv_SAC_STRM_H08_19800101To20210831.npz'
VIC_STRM_H08_RefFileName = 'RefArrays/ClimDiv_VIC_STRM_H08_19800101To20210831.npz'

TrainDataFilename = 'PreppedTrainNEvalNpzs/Train_NLDAS_2_daily_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'

DevDataFilename = 'PreppedTrainNEvalNpzs/Dev_NLDAS_2_daily_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
TestDataFilename = 'PreppedTrainNEvalNpzs/Test_NLDAS_2_daily_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

Mosaic_1MSM_RefObject = np.load(Mosaic_1MSM_RefFileName)
Noah_1MSM_RefObject = np.load(Noah_1MSM_RefFileName)
SAC_1MSM_RefObject = np.load(SAC_1MSM_RefFileName)
VIC_1MSM_RefObject = np.load(VIC_1MSM_RefFileName)
Mosaic_TCSM_RefObject = np.load(Mosaic_TCSM_RefFileName)
Noah_TCSM_RefObject = np.load(Noah_TCSM_RefFileName)
SAC_TCSM_RefObject = np.load(SAC_TCSM_RefFileName)
VIC_TCSM_RefObject = np.load(VIC_TCSM_RefFileName)
Mosaic_EVAP_RefObject = np.load(Mosaic_EVAP_RefFileName)
Noah_EVAP_RefObject = np.load(Noah_EVAP_RefFileName)
SAC_EVAP_RefObject = np.load(SAC_EVAP_RefFileName)
VIC_EVAP_RefObject = np.load(VIC_EVAP_RefFileName)
Mosaic_SWE_RefObject = np.load(Mosaic_SWE_RefFileName)
Noah_SWE_RefObject = np.load(Noah_SWE_RefFileName)
SAC_SWE_RefObject = np.load(SAC_SWE_RefFileName)
VIC_SWE_RefObject = np.load(VIC_SWE_RefFileName)
Mosaic_RUN_RefObject = np.load(Mosaic_RUN_RefFileName)
Noah_RUN_RefObject = np.load(Noah_RUN_RefFileName)
SAC_RUN_RefObject = np.load(SAC_RUN_RefFileName)
VIC_RUN_RefObject = np.load(VIC_RUN_RefFileName)
Mosaic_STRM_H02_RefObject = np.load(Mosaic_STRM_H02_RefFileName)
Noah_STRM_H02_RefObject = np.load(Noah_STRM_H02_RefFileName)
SAC_STRM_H02_RefObject = np.load(SAC_STRM_H02_RefFileName)
VIC_STRM_H02_RefObject = np.load(VIC_STRM_H02_RefFileName)
Mosaic_STRM_H04_RefObject = np.load(Mosaic_STRM_H04_RefFileName)
Noah_STRM_H04_RefObject = np.load(Noah_STRM_H04_RefFileName)
SAC_STRM_H04_RefObject = np.load(SAC_STRM_H04_RefFileName)
VIC_STRM_H04_RefObject = np.load(VIC_STRM_H04_RefFileName)
Mosaic_STRM_H06_RefObject = np.load(Mosaic_STRM_H06_RefFileName)
Noah_STRM_H06_RefObject = np.load(Noah_STRM_H06_RefFileName)
SAC_STRM_H06_RefObject = np.load(SAC_STRM_H06_RefFileName)
VIC_STRM_H06_RefObject = np.load(VIC_STRM_H06_RefFileName)
Mosaic_STRM_H08_RefObject = np.load(Mosaic_STRM_H08_RefFileName)
Noah_STRM_H08_RefObject = np.load(Noah_STRM_H08_RefFileName)
SAC_STRM_H08_RefObject = np.load(SAC_STRM_H08_RefFileName)
VIC_STRM_H08_RefObject = np.load(VIC_STRM_H08_RefFileName)

NLDAS_2_YYYYMMDD_Of_RefArray = Mosaic_1MSM_RefObject['Mosaic_1MSM_YYYYMMDD_Of_RefArray']

Mosaic_1MSM_RefArray = Mosaic_1MSM_RefObject['Mosaic_1MSM_RefArray']
Noah_1MSM_RefArray = Noah_1MSM_RefObject['Noah_1MSM_RefArray']
SAC_1MSM_RefArray = SAC_1MSM_RefObject['SAC_1MSM_RefArray']
VIC_1MSM_RefArray = VIC_1MSM_RefObject['VIC_1MSM_RefArray']
Mosaic_TCSM_RefArray = Mosaic_TCSM_RefObject['Mosaic_TCSM_RefArray']
Noah_TCSM_RefArray = Noah_TCSM_RefObject['Noah_TCSM_RefArray']
SAC_TCSM_RefArray = SAC_TCSM_RefObject['SAC_TCSM_RefArray']
VIC_TCSM_RefArray = VIC_TCSM_RefObject['VIC_TCSM_RefArray']
Mosaic_EVAP_RefArray = Mosaic_EVAP_RefObject['Mosaic_EVAP_RefArray']
Noah_EVAP_RefArray = Noah_EVAP_RefObject['Noah_EVAP_RefArray']
SAC_EVAP_RefArray = SAC_EVAP_RefObject['SAC_EVAP_RefArray']
VIC_EVAP_RefArray = VIC_EVAP_RefObject['VIC_EVAP_RefArray']
Mosaic_SWE_RefArray = Mosaic_SWE_RefObject['Mosaic_SWE_RefArray']
Noah_SWE_RefArray = Noah_SWE_RefObject['Noah_SWE_RefArray']
SAC_SWE_RefArray = SAC_SWE_RefObject['SAC_SWE_RefArray']
VIC_SWE_RefArray = VIC_SWE_RefObject['VIC_SWE_RefArray']
Mosaic_RUN_RefArray = Mosaic_RUN_RefObject['Mosaic_RUN_RefArray']
Noah_RUN_RefArray = Noah_RUN_RefObject['Noah_RUN_RefArray']
SAC_RUN_RefArray = SAC_RUN_RefObject['SAC_RUN_RefArray']
VIC_RUN_RefArray = VIC_RUN_RefObject['VIC_RUN_RefArray']
Mosaic_STRM_H02_RefArray = Mosaic_STRM_H02_RefObject['Mosaic_STRM_H02_RefArray']
Noah_STRM_H02_RefArray = Noah_STRM_H02_RefObject['Noah_STRM_H02_RefArray']
SAC_STRM_H02_RefArray = SAC_STRM_H02_RefObject['SAC_STRM_H02_RefArray']
VIC_STRM_H02_RefArray = VIC_STRM_H02_RefObject['VIC_STRM_H02_RefArray']
Mosaic_STRM_H04_RefArray = Mosaic_STRM_H04_RefObject['Mosaic_STRM_H04_RefArray']
Noah_STRM_H04_RefArray = Noah_STRM_H04_RefObject['Noah_STRM_H04_RefArray']
SAC_STRM_H04_RefArray = SAC_STRM_H04_RefObject['SAC_STRM_H04_RefArray']
VIC_STRM_H04_RefArray = VIC_STRM_H04_RefObject['VIC_STRM_H04_RefArray']
Mosaic_STRM_H06_RefArray = Mosaic_STRM_H06_RefObject['Mosaic_STRM_H06_RefArray']
Noah_STRM_H06_RefArray = Noah_STRM_H06_RefObject['Noah_STRM_H06_RefArray']
SAC_STRM_H06_RefArray = SAC_STRM_H06_RefObject['SAC_STRM_H06_RefArray']
VIC_STRM_H06_RefArray = VIC_STRM_H06_RefObject['VIC_STRM_H06_RefArray']
Mosaic_STRM_H08_RefArray = Mosaic_STRM_H08_RefObject['Mosaic_STRM_H08_RefArray']
Noah_STRM_H08_RefArray = Noah_STRM_H08_RefObject['Noah_STRM_H08_RefArray']
SAC_STRM_H08_RefArray = SAC_STRM_H08_RefObject['SAC_STRM_H08_RefArray']
VIC_STRM_H08_RefArray = VIC_STRM_H08_RefObject['VIC_STRM_H08_RefArray']

# END code arguments / editable section

ssstart_Overall = datetime.now()

Training_BeginDate = date(Training_BeginDateVecList[0], Training_BeginDateVecList[1], Training_BeginDateVecList[2])
Training_EndDate = date(Training_EndDateVecList[0], Training_EndDateVecList[1], Training_EndDateVecList[2])
Eval_BeginDate = date(Eval_BeginDateVecList[0], Eval_BeginDateVecList[1], Eval_BeginDateVecList[2])
Eval_EndDate = date(Eval_EndDateVecList[0], Eval_EndDateVecList[1], Eval_EndDateVecList[2])

#BEGIN check whether the beginning and ending days are indeed Tuesdays
if Training_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for training needs to be a Tuesday!!')
  sys.exit(0)
if Training_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for training needs to be a Tuesday!!')
  sys.exit(0)
if Eval_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for evaluation needs to be a Tuesday!!')
  sys.exit(0)
if Eval_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for evaluation needs to be a Tuesday!!')
  sys.exit(0)
#END check whether the beginning and ending days are indeed Tuesdays

if Training_BeginDate > Training_EndDate:
  print('Training_BeginDate should not be later than Training_EndDate!!!')
  sys.exit(0)
if Eval_BeginDate > Eval_EndDate:
  print('Eval_BeginDate should not be later than Eval_EndDate!!!')
  sys.exit(0)

MonthlyList_NLDAS_2_YYYYMMDD_Of_RefArray, MonthlyList_Mosaic_1MSM_RefArray = CreateMonthlyLists_YYYYMMDDAndArray(NLDAS_2_YYYYMMDD_Of_RefArray, Mosaic_1MSM_RefArray)
MonthlyList_NLDAS_2_YYYYMMDD_Of_RefArray, MonthlyList_Noah_1MSM_RefArray = CreateMonthlyLists_YYYYMMDDAndArray(NLDAS_2_YYYYMMDD_Of_RefArray, Noah_1MSM_RefArray)
MonthlyList_NLDAS_2_YYYYMMDD_Of_RefArray, MonthlyList_SAC_1MSM_RefArray = CreateMonthlyLists_YYYYMMDDAndArray(NLDAS_2_YYYYMMDD_Of_RefArray, SAC_1MSM_RefArray)
MonthlyList_NLDAS_2_YYYYMMDD_Of_RefArray, MonthlyList_VIC_1MSM_RefArray = CreateMonthlyLists_YYYYMMDDAndArray(NLDAS_2_YYYYMMDD_Of_RefArray, VIC_1MSM_RefArray)
MonthlyList_NLDAS_2_YYYYMMDD_Of_RefArray, MonthlyList_Mosaic_TCSM_RefArray = CreateMonthlyLists_YYYYMMDDAndArray(NLDAS_2_YYYYMMDD_Of_RefArray, Mosaic_TCSM_RefArray)
MonthlyList_NLDAS_2_YYYYMMDD_Of_RefArray, MonthlyList_Noah_TCSM_RefArray = CreateMonthlyLists_YYYYMMDDAndArray(NLDAS_2_YYYYMMDD_Of_RefArray, Noah_TCSM_RefArray)
MonthlyList_NLDAS_2_YYYYMMDD_Of_RefArray, MonthlyList_SAC_TCSM_RefArray = CreateMonthlyLists_YYYYMMDDAndArray(NLDAS_2_YYYYMMDD_Of_RefArray, SAC_TCSM_RefArray)
MonthlyList_NLDAS_2_YYYYMMDD_Of_RefArray, MonthlyList_VIC_TCSM_RefArray = CreateMonthlyLists_YYYYMMDDAndArray(NLDAS_2_YYYYMMDD_Of_RefArray, VIC_TCSM_RefArray)
MonthlyList_NLDAS_2_YYYYMMDD_Of_RefArray, MonthlyList_Mosaic_EVAP_RefArray = CreateMonthlyLists_YYYYMMDDAndArray(NLDAS_2_YYYYMMDD_Of_RefArray, Mosaic_EVAP_RefArray)
MonthlyList_NLDAS_2_YYYYMMDD_Of_RefArray, MonthlyList_Noah_EVAP_RefArray = CreateMonthlyLists_YYYYMMDDAndArray(NLDAS_2_YYYYMMDD_Of_RefArray, Noah_EVAP_RefArray)
MonthlyList_NLDAS_2_YYYYMMDD_Of_RefArray, MonthlyList_SAC_EVAP_RefArray = CreateMonthlyLists_YYYYMMDDAndArray(NLDAS_2_YYYYMMDD_Of_RefArray, SAC_EVAP_RefArray)
MonthlyList_NLDAS_2_YYYYMMDD_Of_RefArray, MonthlyList_VIC_EVAP_RefArray = CreateMonthlyLists_YYYYMMDDAndArray(NLDAS_2_YYYYMMDD_Of_RefArray, VIC_EVAP_RefArray)

#BEGIN section for training

NLDAS_2_YYYYMMDD_Of_PrcntlArray, Mosaic_1MSM_PrcntlArray = PrepTrainPortion_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Mosaic_1MSM_RefArray, Training_BeginDateVecList, Training_EndDateVecList, MonthlyList_Mosaic_1MSM_RefArray)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, Noah_1MSM_PrcntlArray = PrepTrainPortion_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Noah_1MSM_RefArray, Training_BeginDateVecList, Training_EndDateVecList, MonthlyList_Noah_1MSM_RefArray)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, SAC_1MSM_PrcntlArray = PrepTrainPortion_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, SAC_1MSM_RefArray, Training_BeginDateVecList, Training_EndDateVecList, MonthlyList_SAC_1MSM_RefArray)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, VIC_1MSM_PrcntlArray = PrepTrainPortion_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, VIC_1MSM_RefArray, Training_BeginDateVecList, Training_EndDateVecList, MonthlyList_VIC_1MSM_RefArray)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, Mosaic_TCSM_PrcntlArray = PrepTrainPortion_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Mosaic_TCSM_RefArray, Training_BeginDateVecList, Training_EndDateVecList, MonthlyList_Mosaic_TCSM_RefArray)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, Noah_TCSM_PrcntlArray = PrepTrainPortion_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Noah_TCSM_RefArray, Training_BeginDateVecList, Training_EndDateVecList, MonthlyList_Noah_TCSM_RefArray)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, SAC_TCSM_PrcntlArray = PrepTrainPortion_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, SAC_TCSM_RefArray, Training_BeginDateVecList, Training_EndDateVecList, MonthlyList_SAC_TCSM_RefArray)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, VIC_TCSM_PrcntlArray = PrepTrainPortion_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, VIC_TCSM_RefArray, Training_BeginDateVecList, Training_EndDateVecList, MonthlyList_VIC_TCSM_RefArray)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, Mosaic_EVAP_PrcntlArray = PrepTrainPortion_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Mosaic_EVAP_RefArray, Training_BeginDateVecList, Training_EndDateVecList, MonthlyList_Mosaic_EVAP_RefArray)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, Noah_EVAP_PrcntlArray = PrepTrainPortion_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Noah_EVAP_RefArray, Training_BeginDateVecList, Training_EndDateVecList, MonthlyList_Noah_EVAP_RefArray)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, SAC_EVAP_PrcntlArray = PrepTrainPortion_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, SAC_EVAP_RefArray, Training_BeginDateVecList, Training_EndDateVecList, MonthlyList_SAC_EVAP_RefArray)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, VIC_EVAP_PrcntlArray = PrepTrainPortion_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, VIC_EVAP_RefArray, Training_BeginDateVecList, Training_EndDateVecList, MonthlyList_VIC_EVAP_RefArray)

NLDAS_2_YYYYMMDD_Of_PrcntlArray, Mosaic_SWE_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Mosaic_SWE_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, Noah_SWE_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Noah_SWE_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, SAC_SWE_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, SAC_SWE_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, VIC_SWE_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, VIC_SWE_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, Mosaic_RUN_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Mosaic_RUN_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, Noah_RUN_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Noah_RUN_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, SAC_RUN_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, SAC_RUN_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, VIC_RUN_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, VIC_RUN_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, Mosaic_STRM_H02_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Mosaic_STRM_H02_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, Noah_STRM_H02_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Noah_STRM_H02_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, SAC_STRM_H02_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, SAC_STRM_H02_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, VIC_STRM_H02_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, VIC_STRM_H02_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, Mosaic_STRM_H04_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Mosaic_STRM_H04_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, Noah_STRM_H04_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Noah_STRM_H04_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, SAC_STRM_H04_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, SAC_STRM_H04_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, VIC_STRM_H04_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, VIC_STRM_H04_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, Mosaic_STRM_H06_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Mosaic_STRM_H06_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, Noah_STRM_H06_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Noah_STRM_H06_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, SAC_STRM_H06_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, SAC_STRM_H06_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, VIC_STRM_H06_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, VIC_STRM_H06_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, Mosaic_STRM_H08_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Mosaic_STRM_H08_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, Noah_STRM_H08_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Noah_STRM_H08_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, SAC_STRM_H08_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, SAC_STRM_H08_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
NLDAS_2_YYYYMMDD_Of_PrcntlArray, VIC_STRM_H08_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, VIC_STRM_H08_RefArray, Training_BeginDateVecList, Training_EndDateVecList)

print('Training: NumDates = ', Mosaic_1MSM_PrcntlArray.shape[0], ', NumSpatialUnits = ', Mosaic_1MSM_PrcntlArray.shape[1])

PrintInfoAboutArray(NLDAS_2_YYYYMMDD_Of_PrcntlArray, 'NLDAS_2_YYYYMMDD_Of_PrcntlArray')

PrintInfoAboutArray_2(Mosaic_1MSM_PrcntlArray, 'Mosaic_1MSM_PrcntlArray')
PrintInfoAboutArray_2(Noah_1MSM_PrcntlArray, 'Noah_1MSM_PrcntlArray')
PrintInfoAboutArray_2(SAC_1MSM_PrcntlArray, 'SAC_1MSM_PrcntlArray')
PrintInfoAboutArray_2(VIC_1MSM_PrcntlArray, 'VIC_1MSM_PrcntlArray')
PrintInfoAboutArray_2(Mosaic_TCSM_PrcntlArray, 'Mosaic_TCSM_PrcntlArray')
PrintInfoAboutArray_2(Noah_TCSM_PrcntlArray, 'Noah_TCSM_PrcntlArray')
PrintInfoAboutArray_2(SAC_TCSM_PrcntlArray, 'SAC_TCSM_PrcntlArray')
PrintInfoAboutArray_2(VIC_TCSM_PrcntlArray, 'VIC_TCSM_PrcntlArray')
PrintInfoAboutArray_2(Mosaic_EVAP_PrcntlArray, 'Mosaic_EVAP_PrcntlArray')
PrintInfoAboutArray_2(Noah_EVAP_PrcntlArray, 'Noah_EVAP_PrcntlArray')
PrintInfoAboutArray_2(SAC_EVAP_PrcntlArray, 'SAC_EVAP_PrcntlArray')
PrintInfoAboutArray_2(VIC_EVAP_PrcntlArray, 'VIC_EVAP_PrcntlArray')
PrintInfoAboutArray_3(Mosaic_SWE_PrcntlArray, 'Mosaic_SWE_PrcntlArray')
PrintInfoAboutArray_3(Noah_SWE_PrcntlArray, 'Noah_SWE_PrcntlArray')
PrintInfoAboutArray_3(SAC_SWE_PrcntlArray, 'SAC_SWE_PrcntlArray')
PrintInfoAboutArray_3(VIC_SWE_PrcntlArray, 'VIC_SWE_PrcntlArray')
PrintInfoAboutArray_3(Mosaic_RUN_PrcntlArray, 'Mosaic_RUN_PrcntlArray')
PrintInfoAboutArray_2(Noah_RUN_PrcntlArray, 'Noah_RUN_PrcntlArray')
PrintInfoAboutArray_2(SAC_RUN_PrcntlArray, 'SAC_RUN_PrcntlArray')
PrintInfoAboutArray_2(VIC_RUN_PrcntlArray, 'VIC_RUN_PrcntlArray')
PrintInfoAboutArray_2(Mosaic_STRM_H02_PrcntlArray, 'Mosaic_STRM_H02_PrcntlArray')
PrintInfoAboutArray_2(Noah_STRM_H02_PrcntlArray, 'Noah_STRM_H02_PrcntlArray')
PrintInfoAboutArray_2(SAC_STRM_H02_PrcntlArray, 'SAC_STRM_H02_PrcntlArray')
PrintInfoAboutArray_2(VIC_STRM_H02_PrcntlArray, 'VIC_STRM_H02_PrcntlArray')
PrintInfoAboutArray_2(Mosaic_STRM_H04_PrcntlArray, 'Mosaic_STRM_H04_PrcntlArray')
PrintInfoAboutArray_2(Noah_STRM_H04_PrcntlArray, 'Noah_STRM_H04_PrcntlArray')
PrintInfoAboutArray_2(SAC_STRM_H04_PrcntlArray, 'SAC_STRM_H04_PrcntlArray')
PrintInfoAboutArray_2(VIC_STRM_H04_PrcntlArray, 'VIC_STRM_H04_PrcntlArray')
PrintInfoAboutArray_2(Mosaic_STRM_H06_PrcntlArray, 'Mosaic_STRM_H06_PrcntlArray')
PrintInfoAboutArray_2(Noah_STRM_H06_PrcntlArray, 'Noah_STRM_H06_PrcntlArray')
PrintInfoAboutArray_2(SAC_STRM_H06_PrcntlArray, 'SAC_STRM_H06_PrcntlArray')
PrintInfoAboutArray_2(VIC_STRM_H06_PrcntlArray, 'VIC_STRM_H06_PrcntlArray')
PrintInfoAboutArray_2(Mosaic_STRM_H08_PrcntlArray, 'Mosaic_STRM_H08_PrcntlArray')
PrintInfoAboutArray_2(Noah_STRM_H08_PrcntlArray, 'Noah_STRM_H08_PrcntlArray')
PrintInfoAboutArray_2(SAC_STRM_H08_PrcntlArray, 'SAC_STRM_H08_PrcntlArray')
PrintInfoAboutArray_2(VIC_STRM_H08_PrcntlArray, 'VIC_STRM_H08_PrcntlArray')

np.savez_compressed(TrainDataFilename, 
                    YYYYMMDD_Of_Array = NLDAS_2_YYYYMMDD_Of_PrcntlArray, 
                    Mosaic_1MSM_PrcntlArray = Mosaic_1MSM_PrcntlArray,
                    Noah_1MSM_PrcntlArray = Noah_1MSM_PrcntlArray,
                    SAC_1MSM_PrcntlArray = SAC_1MSM_PrcntlArray,
                    VIC_1MSM_PrcntlArray = VIC_1MSM_PrcntlArray,
                    Mosaic_TCSM_PrcntlArray = Mosaic_TCSM_PrcntlArray,
                    Noah_TCSM_PrcntlArray = Noah_TCSM_PrcntlArray,
                    SAC_TCSM_PrcntlArray = SAC_TCSM_PrcntlArray,
                    VIC_TCSM_PrcntlArray = VIC_TCSM_PrcntlArray,
                    Mosaic_EVAP_PrcntlArray = Mosaic_EVAP_PrcntlArray,
                    Noah_EVAP_PrcntlArray = Noah_EVAP_PrcntlArray,
                    SAC_EVAP_PrcntlArray = SAC_EVAP_PrcntlArray,
                    VIC_EVAP_PrcntlArray = VIC_EVAP_PrcntlArray,
                    Mosaic_SWE_PrcntlArray = Mosaic_SWE_PrcntlArray,
                    Noah_SWE_PrcntlArray = Noah_SWE_PrcntlArray,
                    SAC_SWE_PrcntlArray = SAC_SWE_PrcntlArray,
                    VIC_SWE_PrcntlArray = VIC_SWE_PrcntlArray,
                    Mosaic_RUN_PrcntlArray = Mosaic_RUN_PrcntlArray,
                    Noah_RUN_PrcntlArray = Noah_RUN_PrcntlArray,
                    SAC_RUN_PrcntlArray = SAC_RUN_PrcntlArray,
                    VIC_RUN_PrcntlArray = VIC_RUN_PrcntlArray,
                    Mosaic_STRM_H02_PrcntlArray = Mosaic_STRM_H02_PrcntlArray,
                    Noah_STRM_H02_PrcntlArray = Noah_STRM_H02_PrcntlArray,
                    SAC_STRM_H02_PrcntlArray = SAC_STRM_H02_PrcntlArray,
                    VIC_STRM_H02_PrcntlArray = VIC_STRM_H02_PrcntlArray,
                    Mosaic_STRM_H04_PrcntlArray = Mosaic_STRM_H04_PrcntlArray,
                    Noah_STRM_H04_PrcntlArray = Noah_STRM_H04_PrcntlArray,
                    SAC_STRM_H04_PrcntlArray = SAC_STRM_H04_PrcntlArray,
                    VIC_STRM_H04_PrcntlArray = VIC_STRM_H04_PrcntlArray,
                    Mosaic_STRM_H06_PrcntlArray = Mosaic_STRM_H06_PrcntlArray,
                    Noah_STRM_H06_PrcntlArray = Noah_STRM_H06_PrcntlArray,
                    SAC_STRM_H06_PrcntlArray = SAC_STRM_H06_PrcntlArray,
                    VIC_STRM_H06_PrcntlArray = VIC_STRM_H06_PrcntlArray,
                    Mosaic_STRM_H08_PrcntlArray = Mosaic_STRM_H08_PrcntlArray,
                    Noah_STRM_H08_PrcntlArray = Noah_STRM_H08_PrcntlArray,
                    SAC_STRM_H08_PrcntlArray = SAC_STRM_H08_PrcntlArray,
                    VIC_STRM_H08_PrcntlArray = VIC_STRM_H08_PrcntlArray)                            

#END section for training

#BEGIN section for evaluation

Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_Mosaic_1MSM_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_Mosaic_1MSM_PrcntlArray = PrepEvalPortions_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Mosaic_1MSM_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList, MonthlyList_Mosaic_1MSM_RefArray)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_Noah_1MSM_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_Noah_1MSM_PrcntlArray = PrepEvalPortions_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Noah_1MSM_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList, MonthlyList_Noah_1MSM_RefArray)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_SAC_1MSM_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_SAC_1MSM_PrcntlArray = PrepEvalPortions_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, SAC_1MSM_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList, MonthlyList_SAC_1MSM_RefArray)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_VIC_1MSM_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_VIC_1MSM_PrcntlArray = PrepEvalPortions_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, VIC_1MSM_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList, MonthlyList_VIC_1MSM_RefArray)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_Mosaic_TCSM_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_Mosaic_TCSM_PrcntlArray = PrepEvalPortions_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Mosaic_TCSM_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList, MonthlyList_Mosaic_TCSM_RefArray)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_Noah_TCSM_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_Noah_TCSM_PrcntlArray = PrepEvalPortions_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Noah_TCSM_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList, MonthlyList_Noah_TCSM_RefArray)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_SAC_TCSM_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_SAC_TCSM_PrcntlArray = PrepEvalPortions_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, SAC_TCSM_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList, MonthlyList_SAC_TCSM_RefArray)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_VIC_TCSM_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_VIC_TCSM_PrcntlArray = PrepEvalPortions_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, VIC_TCSM_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList, MonthlyList_VIC_TCSM_RefArray)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_Mosaic_EVAP_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_Mosaic_EVAP_PrcntlArray = PrepEvalPortions_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Mosaic_EVAP_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList, MonthlyList_Mosaic_EVAP_RefArray)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_Noah_EVAP_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_Noah_EVAP_PrcntlArray = PrepEvalPortions_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Noah_EVAP_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList, MonthlyList_Noah_EVAP_RefArray)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_SAC_EVAP_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_SAC_EVAP_PrcntlArray = PrepEvalPortions_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, SAC_EVAP_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList, MonthlyList_SAC_EVAP_RefArray)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_VIC_EVAP_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_VIC_EVAP_PrcntlArray = PrepEvalPortions_ClimDivs_MonthlyPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, VIC_EVAP_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList, MonthlyList_VIC_EVAP_RefArray)

Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_Mosaic_SWE_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_Mosaic_SWE_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Mosaic_SWE_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_Noah_SWE_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_Noah_SWE_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Noah_SWE_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_SAC_SWE_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_SAC_SWE_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, SAC_SWE_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_VIC_SWE_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_VIC_SWE_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, VIC_SWE_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_Mosaic_RUN_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_Mosaic_RUN_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Mosaic_RUN_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_Noah_RUN_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_Noah_RUN_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Noah_RUN_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_SAC_RUN_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_SAC_RUN_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, SAC_RUN_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_VIC_RUN_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_VIC_RUN_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, VIC_RUN_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_Mosaic_STRM_H02_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_Mosaic_STRM_H02_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Mosaic_STRM_H02_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_Noah_STRM_H02_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_Noah_STRM_H02_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Noah_STRM_H02_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_SAC_STRM_H02_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_SAC_STRM_H02_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, SAC_STRM_H02_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_VIC_STRM_H02_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_VIC_STRM_H02_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, VIC_STRM_H02_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_Mosaic_STRM_H04_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_Mosaic_STRM_H04_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Mosaic_STRM_H04_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_Noah_STRM_H04_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_Noah_STRM_H04_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Noah_STRM_H04_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_SAC_STRM_H04_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_SAC_STRM_H04_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, SAC_STRM_H04_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_VIC_STRM_H04_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_VIC_STRM_H04_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, VIC_STRM_H04_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_Mosaic_STRM_H06_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_Mosaic_STRM_H06_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Mosaic_STRM_H06_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_Noah_STRM_H06_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_Noah_STRM_H06_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Noah_STRM_H06_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_SAC_STRM_H06_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_SAC_STRM_H06_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, SAC_STRM_H06_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_VIC_STRM_H06_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_VIC_STRM_H06_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, VIC_STRM_H06_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_Mosaic_STRM_H08_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_Mosaic_STRM_H08_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Mosaic_STRM_H08_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_Noah_STRM_H08_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_Noah_STRM_H08_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, Noah_STRM_H08_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_SAC_STRM_H08_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_SAC_STRM_H08_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, SAC_STRM_H08_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Dev_VIC_STRM_H08_PrcntlArray, Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, Test_VIC_STRM_H08_PrcntlArray = PrepEvalPortions_ClimDivs_OverallPercBased(NLDAS_2_YYYYMMDD_Of_RefArray, VIC_STRM_H08_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)

print('Evaluation: Dev NumDates = ', Dev_Mosaic_1MSM_PrcntlArray.shape[0], ', NumSpatialUnits = ', Dev_Mosaic_1MSM_PrcntlArray.shape[1])

PrintInfoAboutArray(Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, 'Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray')

PrintInfoAboutArray_2(Dev_Mosaic_1MSM_PrcntlArray, 'Dev_Mosaic_1MSM_PrcntlArray')
PrintInfoAboutArray_2(Dev_Noah_1MSM_PrcntlArray, 'Dev_Noah_1MSM_PrcntlArray')
PrintInfoAboutArray_2(Dev_SAC_1MSM_PrcntlArray, 'Dev_SAC_1MSM_PrcntlArray')
PrintInfoAboutArray_2(Dev_VIC_1MSM_PrcntlArray, 'Dev_VIC_1MSM_PrcntlArray')
PrintInfoAboutArray_2(Dev_Mosaic_TCSM_PrcntlArray, 'Dev_Mosaic_TCSM_PrcntlArray')
PrintInfoAboutArray_2(Dev_Noah_TCSM_PrcntlArray, 'Dev_Noah_TCSM_PrcntlArray')
PrintInfoAboutArray_2(Dev_SAC_TCSM_PrcntlArray, 'Dev_SAC_TCSM_PrcntlArray')
PrintInfoAboutArray_2(Dev_VIC_TCSM_PrcntlArray, 'Dev_VIC_TCSM_PrcntlArray')
PrintInfoAboutArray_2(Dev_Mosaic_EVAP_PrcntlArray, 'Dev_Mosaic_EVAP_PrcntlArray')
PrintInfoAboutArray_2(Dev_Noah_EVAP_PrcntlArray, 'Dev_Noah_EVAP_PrcntlArray')
PrintInfoAboutArray_2(Dev_SAC_EVAP_PrcntlArray, 'Dev_SAC_EVAP_PrcntlArray')
PrintInfoAboutArray_2(Dev_VIC_EVAP_PrcntlArray, 'Dev_VIC_EVAP_PrcntlArray')
PrintInfoAboutArray_3(Dev_Mosaic_SWE_PrcntlArray, 'Dev_Mosaic_SWE_PrcntlArray')
PrintInfoAboutArray_3(Dev_Noah_SWE_PrcntlArray, 'Dev_Noah_SWE_PrcntlArray')
PrintInfoAboutArray_3(Dev_SAC_SWE_PrcntlArray, 'Dev_SAC_SWE_PrcntlArray')
PrintInfoAboutArray_3(Dev_VIC_SWE_PrcntlArray, 'Dev_VIC_SWE_PrcntlArray')
PrintInfoAboutArray_3(Dev_Mosaic_RUN_PrcntlArray, 'Dev_Mosaic_RUN_PrcntlArray')
PrintInfoAboutArray_2(Dev_Noah_RUN_PrcntlArray, 'Dev_Noah_RUN_PrcntlArray')
PrintInfoAboutArray_2(Dev_SAC_RUN_PrcntlArray, 'Dev_SAC_RUN_PrcntlArray')
PrintInfoAboutArray_2(Dev_VIC_RUN_PrcntlArray, 'Dev_VIC_RUN_PrcntlArray')
PrintInfoAboutArray_2(Dev_Mosaic_STRM_H02_PrcntlArray, 'Dev_Mosaic_STRM_H02_PrcntlArray')
PrintInfoAboutArray_2(Dev_Noah_STRM_H02_PrcntlArray, 'Dev_Noah_STRM_H02_PrcntlArray')
PrintInfoAboutArray_2(Dev_SAC_STRM_H02_PrcntlArray, 'Dev_SAC_STRM_H02_PrcntlArray')
PrintInfoAboutArray_2(Dev_VIC_STRM_H02_PrcntlArray, 'Dev_VIC_STRM_H02_PrcntlArray')
PrintInfoAboutArray_2(Dev_Mosaic_STRM_H04_PrcntlArray, 'Dev_Mosaic_STRM_H04_PrcntlArray')
PrintInfoAboutArray_2(Dev_Noah_STRM_H04_PrcntlArray, 'Dev_Noah_STRM_H04_PrcntlArray')
PrintInfoAboutArray_2(Dev_SAC_STRM_H04_PrcntlArray, 'Dev_SAC_STRM_H04_PrcntlArray')
PrintInfoAboutArray_2(Dev_VIC_STRM_H04_PrcntlArray, 'Dev_VIC_STRM_H04_PrcntlArray')
PrintInfoAboutArray_2(Dev_Mosaic_STRM_H06_PrcntlArray, 'Dev_Mosaic_STRM_H06_PrcntlArray')
PrintInfoAboutArray_2(Dev_Noah_STRM_H06_PrcntlArray, 'Dev_Noah_STRM_H06_PrcntlArray')
PrintInfoAboutArray_2(Dev_SAC_STRM_H06_PrcntlArray, 'Dev_SAC_STRM_H06_PrcntlArray')
PrintInfoAboutArray_2(Dev_VIC_STRM_H06_PrcntlArray, 'Dev_VIC_STRM_H06_PrcntlArray')
PrintInfoAboutArray_2(Dev_Mosaic_STRM_H08_PrcntlArray, 'Dev_Mosaic_STRM_H08_PrcntlArray')
PrintInfoAboutArray_2(Dev_Noah_STRM_H08_PrcntlArray, 'Dev_Noah_STRM_H08_PrcntlArray')
PrintInfoAboutArray_2(Dev_SAC_STRM_H08_PrcntlArray, 'Dev_SAC_STRM_H08_PrcntlArray')
PrintInfoAboutArray_2(Dev_VIC_STRM_H08_PrcntlArray, 'Dev_VIC_STRM_H08_PrcntlArray')

print('Evaluation: Test NumDates = ', Test_Mosaic_1MSM_PrcntlArray.shape[0], ', NumSpatialUnits = ', Test_Mosaic_1MSM_PrcntlArray.shape[1])

PrintInfoAboutArray(Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, 'Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray')

PrintInfoAboutArray_2(Test_Mosaic_1MSM_PrcntlArray, 'Test_Mosaic_1MSM_PrcntlArray')
PrintInfoAboutArray_2(Test_Noah_1MSM_PrcntlArray, 'Test_Noah_1MSM_PrcntlArray')
PrintInfoAboutArray_2(Test_SAC_1MSM_PrcntlArray, 'Test_SAC_1MSM_PrcntlArray')
PrintInfoAboutArray_2(Test_VIC_1MSM_PrcntlArray, 'Test_VIC_1MSM_PrcntlArray')
PrintInfoAboutArray_2(Test_Mosaic_TCSM_PrcntlArray, 'Test_Mosaic_TCSM_PrcntlArray')
PrintInfoAboutArray_2(Test_Noah_TCSM_PrcntlArray, 'Test_Noah_TCSM_PrcntlArray')
PrintInfoAboutArray_2(Test_SAC_TCSM_PrcntlArray, 'Test_SAC_TCSM_PrcntlArray')
PrintInfoAboutArray_2(Test_VIC_TCSM_PrcntlArray, 'Test_VIC_TCSM_PrcntlArray')
PrintInfoAboutArray_2(Test_Mosaic_EVAP_PrcntlArray, 'Test_Mosaic_EVAP_PrcntlArray')
PrintInfoAboutArray_2(Test_Noah_EVAP_PrcntlArray, 'Test_Noah_EVAP_PrcntlArray')
PrintInfoAboutArray_2(Test_SAC_EVAP_PrcntlArray, 'Test_SAC_EVAP_PrcntlArray')
PrintInfoAboutArray_2(Test_VIC_EVAP_PrcntlArray, 'Test_VIC_EVAP_PrcntlArray')
PrintInfoAboutArray_3(Test_Mosaic_SWE_PrcntlArray, 'Test_Mosaic_SWE_PrcntlArray')
PrintInfoAboutArray_3(Test_Noah_SWE_PrcntlArray, 'Test_Noah_SWE_PrcntlArray')
PrintInfoAboutArray_3(Test_SAC_SWE_PrcntlArray, 'Test_SAC_SWE_PrcntlArray')
PrintInfoAboutArray_3(Test_VIC_SWE_PrcntlArray, 'Test_VIC_SWE_PrcntlArray')
PrintInfoAboutArray_3(Test_Mosaic_RUN_PrcntlArray, 'Test_Mosaic_RUN_PrcntlArray')
PrintInfoAboutArray_2(Test_Noah_RUN_PrcntlArray, 'Test_Noah_RUN_PrcntlArray')
PrintInfoAboutArray_2(Test_SAC_RUN_PrcntlArray, 'Test_SAC_RUN_PrcntlArray')
PrintInfoAboutArray_2(Test_VIC_RUN_PrcntlArray, 'Test_VIC_RUN_PrcntlArray')
PrintInfoAboutArray_2(Test_Mosaic_STRM_H02_PrcntlArray, 'Test_Mosaic_STRM_H02_PrcntlArray')
PrintInfoAboutArray_2(Test_Noah_STRM_H02_PrcntlArray, 'Test_Noah_STRM_H02_PrcntlArray')
PrintInfoAboutArray_2(Test_SAC_STRM_H02_PrcntlArray, 'Test_SAC_STRM_H02_PrcntlArray')
PrintInfoAboutArray_2(Test_VIC_STRM_H02_PrcntlArray, 'Test_VIC_STRM_H02_PrcntlArray')
PrintInfoAboutArray_2(Test_Mosaic_STRM_H04_PrcntlArray, 'Test_Mosaic_STRM_H04_PrcntlArray')
PrintInfoAboutArray_2(Test_Noah_STRM_H04_PrcntlArray, 'Test_Noah_STRM_H04_PrcntlArray')
PrintInfoAboutArray_2(Test_SAC_STRM_H04_PrcntlArray, 'Test_SAC_STRM_H04_PrcntlArray')
PrintInfoAboutArray_2(Test_VIC_STRM_H04_PrcntlArray, 'Test_VIC_STRM_H04_PrcntlArray')
PrintInfoAboutArray_2(Test_Mosaic_STRM_H06_PrcntlArray, 'Test_Mosaic_STRM_H06_PrcntlArray')
PrintInfoAboutArray_2(Test_Noah_STRM_H06_PrcntlArray, 'Test_Noah_STRM_H06_PrcntlArray')
PrintInfoAboutArray_2(Test_SAC_STRM_H06_PrcntlArray, 'Test_SAC_STRM_H06_PrcntlArray')
PrintInfoAboutArray_2(Test_VIC_STRM_H06_PrcntlArray, 'Test_VIC_STRM_H06_PrcntlArray')
PrintInfoAboutArray_2(Test_Mosaic_STRM_H08_PrcntlArray, 'Test_Mosaic_STRM_H08_PrcntlArray')
PrintInfoAboutArray_2(Test_Noah_STRM_H08_PrcntlArray, 'Test_Noah_STRM_H08_PrcntlArray')
PrintInfoAboutArray_2(Test_SAC_STRM_H08_PrcntlArray, 'Test_SAC_STRM_H08_PrcntlArray')
PrintInfoAboutArray_2(Test_VIC_STRM_H08_PrcntlArray, 'Test_VIC_STRM_H08_PrcntlArray')

np.savez_compressed(DevDataFilename, 
                    YYYYMMDD_Of_Array = Dev_NLDAS_2_YYYYMMDD_Of_PrcntlArray, 
                    Mosaic_1MSM_PrcntlArray = Dev_Mosaic_1MSM_PrcntlArray,
                    Noah_1MSM_PrcntlArray = Dev_Noah_1MSM_PrcntlArray,
                    SAC_1MSM_PrcntlArray = Dev_SAC_1MSM_PrcntlArray,
                    VIC_1MSM_PrcntlArray = Dev_VIC_1MSM_PrcntlArray,
                    Mosaic_TCSM_PrcntlArray = Dev_Mosaic_TCSM_PrcntlArray,
                    Noah_TCSM_PrcntlArray = Dev_Noah_TCSM_PrcntlArray,
                    SAC_TCSM_PrcntlArray = Dev_SAC_TCSM_PrcntlArray,
                    VIC_TCSM_PrcntlArray = Dev_VIC_TCSM_PrcntlArray,
                    Mosaic_EVAP_PrcntlArray = Dev_Mosaic_EVAP_PrcntlArray,
                    Noah_EVAP_PrcntlArray = Dev_Noah_EVAP_PrcntlArray,
                    SAC_EVAP_PrcntlArray = Dev_SAC_EVAP_PrcntlArray,
                    VIC_EVAP_PrcntlArray = Dev_VIC_EVAP_PrcntlArray,
                    Mosaic_SWE_PrcntlArray = Dev_Mosaic_SWE_PrcntlArray,
                    Noah_SWE_PrcntlArray = Dev_Noah_SWE_PrcntlArray,
                    SAC_SWE_PrcntlArray = Dev_SAC_SWE_PrcntlArray,
                    VIC_SWE_PrcntlArray = Dev_VIC_SWE_PrcntlArray,
                    Mosaic_RUN_PrcntlArray = Dev_Mosaic_RUN_PrcntlArray,
                    Noah_RUN_PrcntlArray = Dev_Noah_RUN_PrcntlArray,
                    SAC_RUN_PrcntlArray = Dev_SAC_RUN_PrcntlArray,
                    VIC_RUN_PrcntlArray = Dev_VIC_RUN_PrcntlArray,
                    Mosaic_STRM_H02_PrcntlArray = Dev_Mosaic_STRM_H02_PrcntlArray,
                    Noah_STRM_H02_PrcntlArray = Dev_Noah_STRM_H02_PrcntlArray,
                    SAC_STRM_H02_PrcntlArray = Dev_SAC_STRM_H02_PrcntlArray,
                    VIC_STRM_H02_PrcntlArray = Dev_VIC_STRM_H02_PrcntlArray,
                    Mosaic_STRM_H04_PrcntlArray = Dev_Mosaic_STRM_H04_PrcntlArray,
                    Noah_STRM_H04_PrcntlArray = Dev_Noah_STRM_H04_PrcntlArray,
                    SAC_STRM_H04_PrcntlArray = Dev_SAC_STRM_H04_PrcntlArray,
                    VIC_STRM_H04_PrcntlArray = Dev_VIC_STRM_H04_PrcntlArray,
                    Mosaic_STRM_H06_PrcntlArray = Dev_Mosaic_STRM_H06_PrcntlArray,
                    Noah_STRM_H06_PrcntlArray = Dev_Noah_STRM_H06_PrcntlArray,
                    SAC_STRM_H06_PrcntlArray = Dev_SAC_STRM_H06_PrcntlArray,
                    VIC_STRM_H06_PrcntlArray = Dev_VIC_STRM_H06_PrcntlArray,
                    Mosaic_STRM_H08_PrcntlArray = Dev_Mosaic_STRM_H08_PrcntlArray,
                    Noah_STRM_H08_PrcntlArray = Dev_Noah_STRM_H08_PrcntlArray,
                    SAC_STRM_H08_PrcntlArray = Dev_SAC_STRM_H08_PrcntlArray,
                    VIC_STRM_H08_PrcntlArray = Dev_VIC_STRM_H08_PrcntlArray)                            

np.savez_compressed(TestDataFilename, 
                    YYYYMMDD_Of_Array = Test_NLDAS_2_YYYYMMDD_Of_PrcntlArray, 
                    Mosaic_1MSM_PrcntlArray = Test_Mosaic_1MSM_PrcntlArray,
                    Noah_1MSM_PrcntlArray = Test_Noah_1MSM_PrcntlArray,
                    SAC_1MSM_PrcntlArray = Test_SAC_1MSM_PrcntlArray,
                    VIC_1MSM_PrcntlArray = Test_VIC_1MSM_PrcntlArray,
                    Mosaic_TCSM_PrcntlArray = Test_Mosaic_TCSM_PrcntlArray,
                    Noah_TCSM_PrcntlArray = Test_Noah_TCSM_PrcntlArray,
                    SAC_TCSM_PrcntlArray = Test_SAC_TCSM_PrcntlArray,
                    VIC_TCSM_PrcntlArray = Test_VIC_TCSM_PrcntlArray,
                    Mosaic_EVAP_PrcntlArray = Test_Mosaic_EVAP_PrcntlArray,
                    Noah_EVAP_PrcntlArray = Test_Noah_EVAP_PrcntlArray,
                    SAC_EVAP_PrcntlArray = Test_SAC_EVAP_PrcntlArray,
                    VIC_EVAP_PrcntlArray = Test_VIC_EVAP_PrcntlArray,
                    Mosaic_SWE_PrcntlArray = Test_Mosaic_SWE_PrcntlArray,
                    Noah_SWE_PrcntlArray = Test_Noah_SWE_PrcntlArray,
                    SAC_SWE_PrcntlArray = Test_SAC_SWE_PrcntlArray,
                    VIC_SWE_PrcntlArray = Test_VIC_SWE_PrcntlArray,
                    Mosaic_RUN_PrcntlArray = Test_Mosaic_RUN_PrcntlArray,
                    Noah_RUN_PrcntlArray = Test_Noah_RUN_PrcntlArray,
                    SAC_RUN_PrcntlArray = Test_SAC_RUN_PrcntlArray,
                    VIC_RUN_PrcntlArray = Test_VIC_RUN_PrcntlArray,
                    Mosaic_STRM_H02_PrcntlArray = Test_Mosaic_STRM_H02_PrcntlArray,
                    Noah_STRM_H02_PrcntlArray = Test_Noah_STRM_H02_PrcntlArray,
                    SAC_STRM_H02_PrcntlArray = Test_SAC_STRM_H02_PrcntlArray,
                    VIC_STRM_H02_PrcntlArray = Test_VIC_STRM_H02_PrcntlArray,
                    Mosaic_STRM_H04_PrcntlArray = Test_Mosaic_STRM_H04_PrcntlArray,
                    Noah_STRM_H04_PrcntlArray = Test_Noah_STRM_H04_PrcntlArray,
                    SAC_STRM_H04_PrcntlArray = Test_SAC_STRM_H04_PrcntlArray,
                    VIC_STRM_H04_PrcntlArray = Test_VIC_STRM_H04_PrcntlArray,
                    Mosaic_STRM_H06_PrcntlArray = Test_Mosaic_STRM_H06_PrcntlArray,
                    Noah_STRM_H06_PrcntlArray = Test_Noah_STRM_H06_PrcntlArray,
                    SAC_STRM_H06_PrcntlArray = Test_SAC_STRM_H06_PrcntlArray,
                    VIC_STRM_H06_PrcntlArray = Test_VIC_STRM_H06_PrcntlArray,
                    Mosaic_STRM_H08_PrcntlArray = Test_Mosaic_STRM_H08_PrcntlArray,
                    Noah_STRM_H08_PrcntlArray = Test_Noah_STRM_H08_PrcntlArray,
                    SAC_STRM_H08_PrcntlArray = Test_SAC_STRM_H08_PrcntlArray,
                    VIC_STRM_H08_PrcntlArray = Test_VIC_STRM_H08_PrcntlArray)                            

#END section for evaluation

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")



