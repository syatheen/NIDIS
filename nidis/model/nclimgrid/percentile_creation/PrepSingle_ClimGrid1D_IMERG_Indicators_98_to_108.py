#!/usr/bin/env python
# Coded by Soni Yatheendradas
#         on Oct 30, 2023
from __future__ import division
import sys
#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        NumMonthsStr
#ArgNum   1

# BEGIN code arguments / editable section

NumMonthsStr = '1Month' #sys.argv[1] # Choices are '1Month', '2Month', '3Month', '6Month', '9Month', '12Month', '24Month', '36Month', '48Month', '60Month', '72Month'

if NumMonthsStr == '1Month':
  RefArray_BeginDateVecList = [2000, 7, 4]
elif NumMonthsStr == '2Month':
  RefArray_BeginDateVecList = [2000, 8, 1]
elif NumMonthsStr == '3Month':
  RefArray_BeginDateVecList = [2000, 8, 29]
elif NumMonthsStr == '6Month':
  RefArray_BeginDateVecList = [2000, 11, 28]
elif NumMonthsStr == '9Month':
  RefArray_BeginDateVecList = [2001, 2, 27]
elif NumMonthsStr == '12Month':
  RefArray_BeginDateVecList = [2001, 6, 5]
elif NumMonthsStr == '24Month':
  RefArray_BeginDateVecList = [2002, 6, 4]
elif NumMonthsStr == '36Month':
  RefArray_BeginDateVecList = [2003, 6, 3]
elif NumMonthsStr == '48Month':
  RefArray_BeginDateVecList = [2004, 6, 1]
elif NumMonthsStr == '60Month':
  RefArray_BeginDateVecList = [2005, 5, 31]
elif NumMonthsStr == '72Month':
  RefArray_BeginDateVecList = [2006, 6, 6]
#end of if NumMonthsStr == '1Month'

SingleUnified_BeginDateVecList = [2006, 1, 3] # Beginning single-unified year, month, day of month, this is also a Tuesday
SingleUnified_EndDateVecList = [2019, 12, 31] # Ending single-unified year, month, day of month, this is also a Tuesday

IMERG_nMonth_RefFileName = '/discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS/RefArrays/ClimGrid1D_IMERG'+NumMonthsStr+'_'+format(RefArray_BeginDateVecList[0],'04')+format(RefArray_BeginDateVecList[1],'02')+format(RefArray_BeginDateVecList[2],'02')+'To20210525.npz'

SingleUnifiedDataFilename = '/discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG'+ NumMonthsStr + '_' + str(SingleUnified_BeginDateVecList[0]) + format(SingleUnified_BeginDateVecList[1],'02') + format(SingleUnified_BeginDateVecList[2],'02') + 'To' + str(SingleUnified_EndDateVecList[0]) + format(SingleUnified_EndDateVecList[1],'02') + format(SingleUnified_EndDateVecList[2],'02') + '.npz'

# END code arguments / editable section

from datetime import date, datetime, timedelta
import numpy as np
from scipy.interpolate import interp1d
from scipy.stats import rankdata

from nidis.model.nclimgrid.percentile_creation.Utils import \
  CreateMonthlyLists_YYYYMMDDAndArray, \
  PrepTrainPortion_ClimDivs_MonthlyPercBased, \
  PrintInfoAboutArray, \
  PrepTrainPortion_ClimDivs_OverallPercBased


#from CreateMonthlyLists_YYYYMMDDAndArray_File import CreateMonthlyLists_YYYYMMDDAndArray
#from PrepTrainPortion_ClimDivs_OverallPercBased_File import PrepTrainPortion_ClimDivs_OverallPercBased
#from PrepTrainPortion_ClimDivs_MonthlyPercBased_File import PrepTrainPortion_ClimDivs_MonthlyPercBased
#from PrintInfoAboutArray_File import PrintInfoAboutArray
#from PrintInfoAboutArray_2_File import PrintInfoAboutArray_2

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

IMERG_nMonth_RefObject = np.load(IMERG_nMonth_RefFileName)

IMERG_nMonth_YYYYMMDD_Of_RefArray = IMERG_nMonth_RefObject['IMERG_nMonth_YYYYMMDD_Of_RefArray']

IMERG_nMonth_RefArray = IMERG_nMonth_RefObject['IMERG_nMonth_RefArray']

EndIdx_Pre = np.where( IMERG_nMonth_YYYYMMDD_Of_RefArray == 10000 * SingleUnified_EndDateVecList[0] + 100 * SingleUnified_EndDateVecList[1] + SingleUnified_EndDateVecList[2] )[0][0]

IMERG_nMonth_YYYYMMDD_Of_RefArray = IMERG_nMonth_YYYYMMDD_Of_RefArray[:EndIdx_Pre+1]

IMERG_nMonth_RefArray = IMERG_nMonth_RefArray[:EndIdx_Pre+1]

if ( (NumMonthsStr == '1Month') or
     (NumMonthsStr == '2Month') or
     (NumMonthsStr == '3Month') or
     (NumMonthsStr == '6Month') or
     (NumMonthsStr == '9Month') ):
  MonthlyList_IMERG_nMonth_YYYYMMDD_Of_RefArray, MonthlyList_IMERG_nMonth_RefArray = CreateMonthlyLists_YYYYMMDDAndArray(IMERG_nMonth_YYYYMMDD_Of_RefArray, IMERG_nMonth_RefArray)
#end of if ( (NumMonthsStr == '1Month') or...

#BEGIN section for single-unified

if ( (NumMonthsStr == '1Month') or
     (NumMonthsStr == '2Month') or
     (NumMonthsStr == '3Month') or
     (NumMonthsStr == '6Month') or
     (NumMonthsStr == '9Month') ):

  IMERG_nMonth_YYYYMMDD_Of_PrcntlArray, IMERG_nMonth_PrcntlArray = PrepTrainPortion_ClimDivs_MonthlyPercBased(IMERG_nMonth_YYYYMMDD_Of_RefArray, IMERG_nMonth_RefArray, SingleUnified_BeginDateVecList, SingleUnified_EndDateVecList, MonthlyList_IMERG_nMonth_RefArray)

else:

  IMERG_nMonth_YYYYMMDD_Of_PrcntlArray, IMERG_nMonth_PrcntlArray = PrepTrainPortion_ClimDivs_OverallPercBased(IMERG_nMonth_YYYYMMDD_Of_RefArray, IMERG_nMonth_RefArray, SingleUnified_BeginDateVecList, SingleUnified_EndDateVecList)

#end of if ( (NumMonthsStr == '1Month') or...

print('Single-unified: NumDates = ', IMERG_nMonth_PrcntlArray.shape[0], ', NumSpatialUnits = ',IMERG_nMonth_PrcntlArray.shape[1])

PrintInfoAboutArray(IMERG_nMonth_YYYYMMDD_Of_PrcntlArray, 'IMERG_nMonth_YYYYMMDD_Of_PrcntlArray')

#PrintInfoAboutArray_2(IMERG_nMonth_PrcntlArray, 'IMERG_nMonth_PrcntlArray')

np.savez_compressed(SingleUnifiedDataFilename, 
                    YYYYMMDD_Of_Array = IMERG_nMonth_YYYYMMDD_Of_PrcntlArray, 
                    IMERG_nMonth_PrcntlArray = IMERG_nMonth_PrcntlArray)

#END section for single-unified

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")



