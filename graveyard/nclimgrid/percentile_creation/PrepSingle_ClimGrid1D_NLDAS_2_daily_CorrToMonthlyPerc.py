#!/usr/bin/env python
# Coded by Soni Yatheendradas
#         on Feb 23, 2023
from __future__ import division
import sys
#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#         ArgLSM ArgVariable ArgHUC
#ArgNum   1       2           3

# BEGIN code arguments / editable section

SingleUnified_BeginDateVecList = [2006, 1, 3] # Beginning single-unified year, month, day of month, this is also a Tuesday
SingleUnified_EndDateVecList = [2021, 8, 31] # Ending single-unified year, month, day of month, this is also a Tuesday

ArgLSM = sys.argv[1] # Choices are 'Mosaic', 'Noah', 'SAC', 'VIC'
ArgVariable = sys.argv[2] # Choices currently implemented are '1MSM', 'TCSM'
ArgHUC = sys.argv[3] # Choices currently implemented are 'NA' (for "Not Applicable")

if (ArgVariable == 'STRM') :

  NLDAS_2_daily_RefFileName = 'RefArrays/ClimGrid1D_' + ArgLSM + '_' + ArgVariable + '_' + ArgHUC + '_19800101To20210831.npz'

  SingleUnifiedDataFilename = 'PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_' + ArgLSM + '_' + ArgVariable + '_' + ArgHUC + '_Crr2MnthlyPrc_' + str(SingleUnified_BeginDateVecList[0]) + format(SingleUnified_BeginDateVecList[1],'02') + format(SingleUnified_BeginDateVecList[2],'02') + 'To' + str(SingleUnified_EndDateVecList[0]) + format(SingleUnified_EndDateVecList[1],'02') + format(SingleUnified_EndDateVecList[2],'02') + '.npz'

else:

  NLDAS_2_daily_RefFileName = 'RefArrays/ClimGrid1D_' + ArgLSM + '_' + ArgVariable + '_19800101To20210831.npz'

  SingleUnifiedDataFilename = 'PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_' + ArgLSM + '_' + ArgVariable + '_Crr2MnthlyPrc_' + str(SingleUnified_BeginDateVecList[0]) + format(SingleUnified_BeginDateVecList[1],'02') + format(SingleUnified_BeginDateVecList[2],'02') + 'To' + str(SingleUnified_EndDateVecList[0]) + format(SingleUnified_EndDateVecList[1],'02') + format(SingleUnified_EndDateVecList[2],'02') + '.npz'

#end of if (ArgVariable == 'STRM') :

# END code arguments / editable section

from datetime import date, datetime, timedelta
#import sys
import numpy as np
from scipy.interpolate import interp1d
from scipy.stats import rankdata
from CreateMonthlyLists_YYYYMMDDAndArray_File import CreateMonthlyLists_YYYYMMDDAndArray
from PrepTrainPortion_ClimDivs_MonthlyPercBased_File import PrepTrainPortion_ClimDivs_MonthlyPercBased
from PrintInfoAboutArray_File import PrintInfoAboutArray

ssstart_Overall = datetime.now()

SingleUnified_BeginDate = date(SingleUnified_BeginDateVecList[0], SingleUnified_BeginDateVecList[1], SingleUnified_BeginDateVecList[2])
SingleUnified_EndDate = date(SingleUnified_EndDateVecList[0], SingleUnified_EndDateVecList[1], SingleUnified_EndDateVecList[2])

#BEGIN check whether the beginning and ending days are indeed Tuesdays
if SingleUnified_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for single-unified needs to be a Tuesday!!')
  sys.exit(0)
if SingleUnified_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for single-unified needs to be a Tuesday!!')
  sys.exit(0)
#END check whether the beginning and ending days are indeed Tuesdays

if SingleUnified_BeginDate > SingleUnified_EndDate:
  print('SingleUnified_BeginDate should not be later than SingleUnified_EndDate!!!')
  sys.exit(0)

NLDAS_2_daily_RefObject = np.load(NLDAS_2_daily_RefFileName)

if ArgVariable == '1MSM':
  if ArgLSM == 'Mosaic':
    NLDAS_2_daily_YYYYMMDD_Of_RefArray = NLDAS_2_daily_RefObject['Mosaic_1MSM_YYYYMMDD_Of_RefArray']
    NLDAS_2_daily_RefArray = NLDAS_2_daily_RefObject['Mosaic_1MSM_RefArray']
  elif ArgLSM == 'Noah':
    NLDAS_2_daily_YYYYMMDD_Of_RefArray = NLDAS_2_daily_RefObject['Noah_1MSM_YYYYMMDD_Of_RefArray']
    NLDAS_2_daily_RefArray = NLDAS_2_daily_RefObject['Noah_1MSM_RefArray']
  elif ArgLSM == 'SAC':
    NLDAS_2_daily_YYYYMMDD_Of_RefArray = NLDAS_2_daily_RefObject['SAC_1MSM_YYYYMMDD_Of_RefArray']
    NLDAS_2_daily_RefArray = NLDAS_2_daily_RefObject['SAC_1MSM_RefArray']
  elif ArgLSM == 'VIC':
    NLDAS_2_daily_YYYYMMDD_Of_RefArray = NLDAS_2_daily_RefObject['VIC_1MSM_YYYYMMDD_Of_RefArray']
    NLDAS_2_daily_RefArray = NLDAS_2_daily_RefObject['VIC_1MSM_RefArray']
  #end of if ArgLSM == 'Mosaic'
elif ArgVariable == 'TCSM':
  if ArgLSM == 'Mosaic':
    NLDAS_2_daily_YYYYMMDD_Of_RefArray = NLDAS_2_daily_RefObject['Mosaic_TCSM_YYYYMMDD_Of_RefArray']
    NLDAS_2_daily_RefArray = NLDAS_2_daily_RefObject['Mosaic_TCSM_RefArray']
  elif ArgLSM == 'Noah':
    NLDAS_2_daily_YYYYMMDD_Of_RefArray = NLDAS_2_daily_RefObject['Noah_TCSM_YYYYMMDD_Of_RefArray']
    NLDAS_2_daily_RefArray = NLDAS_2_daily_RefObject['Noah_TCSM_RefArray']
  elif ArgLSM == 'SAC':
    NLDAS_2_daily_YYYYMMDD_Of_RefArray = NLDAS_2_daily_RefObject['SAC_TCSM_YYYYMMDD_Of_RefArray']
    NLDAS_2_daily_RefArray = NLDAS_2_daily_RefObject['SAC_TCSM_RefArray']
  elif ArgLSM == 'VIC':
    NLDAS_2_daily_YYYYMMDD_Of_RefArray = NLDAS_2_daily_RefObject['VIC_TCSM_YYYYMMDD_Of_RefArray']
    NLDAS_2_daily_RefArray = NLDAS_2_daily_RefObject['VIC_TCSM_RefArray']
  #end of if ArgLSM == 'Mosaic'
else: #of if ArgVariable == '1MSM'
  print('Add remaining np.savez_compressed code lines for other variables!!')
  sys.exit(0)
#end of if ArgVariable == '1MSM'

MonthlyList_NLDAS_2_daily_YYYYMMDD_Of_RefArray, MonthlyList_NLDAS_2_daily_RefArray = CreateMonthlyLists_YYYYMMDDAndArray(NLDAS_2_daily_YYYYMMDD_Of_RefArray, NLDAS_2_daily_RefArray)

#BEGIN section for single-unified

NLDAS_2_daily_YYYYMMDD_Of_PrcntlArray, NLDAS_2_daily_PrcntlArray = PrepTrainPortion_ClimDivs_MonthlyPercBased(NLDAS_2_daily_YYYYMMDD_Of_RefArray, NLDAS_2_daily_RefArray, SingleUnified_BeginDateVecList, SingleUnified_EndDateVecList, MonthlyList_NLDAS_2_daily_RefArray)

print('Single-unified: NumDates = ', NLDAS_2_daily_PrcntlArray.shape[0], ', NumSpatialUnits = ',NLDAS_2_daily_PrcntlArray.shape[1])

PrintInfoAboutArray(NLDAS_2_daily_YYYYMMDD_Of_PrcntlArray, 'NLDAS_2_daily_YYYYMMDD_Of_PrcntlArray')

PrintInfoAboutArray(NLDAS_2_daily_PrcntlArray, 'NLDAS_2_daily_PrcntlArray')

np.savez_compressed(SingleUnifiedDataFilename, 
                    YYYYMMDD_Of_Array = NLDAS_2_daily_YYYYMMDD_Of_PrcntlArray, 
                    NLDAS_2_daily_PrcntlArray = NLDAS_2_daily_PrcntlArray)

#END section for single-unified

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")



