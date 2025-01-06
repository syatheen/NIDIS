# Coded by Soni Yatheendradas
#         on Mar 2, 2021
from __future__ import division
import sys
#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        EDDI_WhichPastPeriod
#ArgNum   1

# BEGIN code arguments / editable section

Training_BeginDateVecList = [2006, 1, 3] # Beginning training year, month, day of month, this is also a Tuesday
Training_EndDateVecList = [2018, 12, 25] # Ending training year, month, day of month, this is also a Tuesday

Eval_BeginDateVecList = [2019, 1, 1] # Beginning evaluation year, month, day of month, this is also a Tuesday
Eval_EndDateVecList = [2019, 12, 31] # Ending evaluation year, month, day of month, this is also a Tuesday

EDDI_WhichPastPeriod = sys.argv[1] # Choices range from '01wk' till '12wk' in 1-week increments, and '01mn' till '12mn' in 1-month increments

#EDDI_RefFileName = 'RefArrays/ClimDiv_EDDI_'+EDDI_WhichPastPeriod+'_19800108To20200825.npz'
EDDI_RefFileName = 'RefArrays/ClimDiv_EDDI_'+EDDI_WhichPastPeriod+'_19800108To20201229.npz'

TrainDataFilename = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI'+EDDI_WhichPastPeriod+'_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'

DevDataFilename = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI'+EDDI_WhichPastPeriod+'_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
TestDataFilename = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI'+EDDI_WhichPastPeriod+'_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

# END code arguments / editable section

from datetime import date, datetime, timedelta
#import sys
import numpy as np
from scipy.interpolate import interp1d
from scipy.stats import rankdata

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

EDDI_RefObject = np.load(EDDI_RefFileName)

EDDI_YYYYMMDD_Of_RefArray = EDDI_RefObject['EDDI_YYYYMMDD_Of_RefArray']

EDDI_RefArray = EDDI_RefObject['EDDI_RefArray']

def CreateYYYYMMDD_Of_Array(BeginDate, EndDate):
  TotalNumDaysDiff = abs(EndDate-BeginDate).days
  TotalNumWeeksDiff = TotalNumDaysDiff//7
  HumanDatesList_Of_Array = []
  for NumWeeksDiff in range(0,TotalNumWeeksDiff+1):
    IntermediateDate = BeginDate + timedelta(weeks=NumWeeksDiff)
    HumanDatesList_Of_Array.append(10000*IntermediateDate.year + 100*IntermediateDate.month + IntermediateDate.day)
  YYYYMMDD_Of_Array = np.array(HumanDatesList_Of_Array, dtype = np.int32)
  YYYYMMDD_Of_Array = np.expand_dims(YYYYMMDD_Of_Array, axis=1)
  return YYYYMMDD_Of_Array
#end of def CreateYYYYMMDD_Of_Array(BeginDate, EndDate)

def TimeSlice_YYYYMMDDAndRefArray(YYYYMMDD_Of_RefArray, RefArray, BeginDateVecList, EndDateVecList):
  BeginYYYYMMDD = 10000*BeginDateVecList[0] + 100*BeginDateVecList[1] + BeginDateVecList[2]
  EndYYYYMMDD = 10000*EndDateVecList[0] + 100*EndDateVecList[1] + EndDateVecList[2]
  if ( ( BeginYYYYMMDD in list(YYYYMMDD_Of_RefArray) ) and
       ( EndYYYYMMDD in list(YYYYMMDD_Of_RefArray) ) ) :
    BeginIdx = list(YYYYMMDD_Of_RefArray).index(10000*BeginDateVecList[0] + 100*BeginDateVecList[1] + BeginDateVecList[2])
    EndIdx = list(YYYYMMDD_Of_RefArray).index(10000*EndDateVecList[0] + 100*EndDateVecList[1] + EndDateVecList[2])
    YYYYMMDD_Of_PrcntlArray = YYYYMMDD_Of_RefArray[ BeginIdx : EndIdx+1 ] 
    PrcntlArray = RefArray[ BeginIdx : EndIdx+1 ] 
  else: # if ( (BeginYYYYMMDD in list(YYYYMMDD_Of_RefArray) and...
    BeginDate = date(BeginDateVecList[0], BeginDateVecList[1], BeginDateVecList[2])
    EndDate = date(EndDateVecList[0], EndDateVecList[1], EndDateVecList[2])
    YYYYMMDD_Of_PrcntlArray = CreateYYYYMMDD_Of_Array(BeginDate, EndDate)
    PrcntlArray = np.empty([YYYYMMDD_Of_PrcntlArray.shape[0], RefArray.shape[1]]) 
    PrcntlArray[:] = np.NaN
    if ( BeginYYYYMMDD in list(YYYYMMDD_Of_RefArray) ):
      BeginIdx = list(YYYYMMDD_Of_RefArray).index(10000*BeginDateVecList[0] + 100*BeginDateVecList[1] + BeginDateVecList[2])
      PrcntlArray[ : RefArray.shape[0]-BeginIdx ] = RefArray[ BeginIdx : ] 
    if ( EndYYYYMMDD in list(YYYYMMDD_Of_RefArray) ):
      EndIdx = list(YYYYMMDD_Of_RefArray).index(10000*EndDateVecList[0] + 100*EndDateVecList[1] + EndDateVecList[2])
      PrcntlArray[ PrcntlArray.shape[0]-(EndIdx+1) : ] = RefArray[ : EndIdx+1 ] 
  #end of if ( (BeginYYYYMMDD in list(YYYYMMDD_Of_RefArray) and...
  return YYYYMMDD_Of_PrcntlArray, PrcntlArray
#end of def TimeSlice_YYYYMMDDAndRefArray(YYYYMMDD_Of_RefArray, RefArray, BeginDateVecList, EndDateVecList):

def FindPercentilesForValues(RefArray_1d, Values_1d):
  RefArray_1d_NotNaN = RefArray_1d[~np.isnan(RefArray_1d)]
  SortedRef_1d = np.sort(RefArray_1d_NotNaN) 
  SortedRef_1d_size = SortedRef_1d.size
  QuantileInverses_OrdinalTieRanks = (rankdata(SortedRef_1d, method='ordinal') - 1) / \
                                     float(SortedRef_1d_size - 1) 
  QuantileInverses_AverageTieRanks = (rankdata(SortedRef_1d, method='average') - 1) / \
                                     float(SortedRef_1d_size - 1) 
  Percentiles_1d = np.interp(Values_1d, SortedRef_1d, QuantileInverses_OrdinalTieRanks) 
  IfValuesInSortedRef = np.isin(Values_1d, SortedRef_1d) 
  ValuesInSortedRef = Values_1d[np.where(IfValuesInSortedRef)] 
  Idxs_ValuesInSortedRef_In_SortedRef = np.searchsorted(SortedRef_1d, ValuesInSortedRef) 
  Percentiles_AverageTieRanks = QuantileInverses_AverageTieRanks[Idxs_ValuesInSortedRef_In_SortedRef] 
  Percentiles_1d[np.where(IfValuesInSortedRef)] = Percentiles_AverageTieRanks
  return Percentiles_1d
#end of def FindPercentilesForValues(RefArray_1d, Values_1d):

def LoopPercentileCalcOverSpatialUnits(RefArray, PrcntlArray):
  for WhichSpatialUnit in range(PrcntlArray.shape[1]):
    RefArray_ThisSpatialUnit = RefArray[:, WhichSpatialUnit]
    PrcntlArray_ThisSpatialUnit = PrcntlArray[:, WhichSpatialUnit]
    PrcntlArray_ThisSpatialUnit = FindPercentilesForValues(RefArray_ThisSpatialUnit, PrcntlArray_ThisSpatialUnit) 
    PrcntlArray[:, WhichSpatialUnit] = PrcntlArray_ThisSpatialUnit
  #end of for WhichSpatialUnit in range(PrcntlArray.shape[1]):
  return PrcntlArray
#end of def LoopPercentileCalcOverSpatialUnits(RefArray, PrcntlArray):

def PrintInfoAboutArray(ThisArray, ThisArray_Str):
  print(ThisArray_Str,".shape is ",ThisArray.shape)
  print(ThisArray_Str,".dtype is ",ThisArray.dtype)
  print(ThisArray_Str," is ",ThisArray)
  print("np.amin(np.isnan(",ThisArray_Str,").sum(axis=0)) is ",np.amin(np.isnan(ThisArray).sum(axis=0)))
  print("np.amax(np.isnan(",ThisArray_Str,").sum(axis=0)) is ",np.amax(np.isnan(ThisArray).sum(axis=0)))
  print('overall min is ',np.nanmin(ThisArray),', overall max is ',np.nanmax(ThisArray))
#end of def PrintInfoAboutArray(ThisArray, ThisArray_Str):

#BEGIN section for training

EDDI_YYYYMMDD_Of_PrcntlArray, EDDI_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(EDDI_YYYYMMDD_Of_RefArray, EDDI_RefArray, Training_BeginDateVecList, Training_EndDateVecList)

EDDI_PrcntlArray = LoopPercentileCalcOverSpatialUnits(EDDI_RefArray, EDDI_PrcntlArray)

print('Training: NumDates = ', EDDI_PrcntlArray.shape[0], ', NumSpatialUnits = ',EDDI_PrcntlArray.shape[1])
PrintInfoAboutArray(EDDI_PrcntlArray, 'EDDI_PrcntlArray')

np.savez_compressed(TrainDataFilename, YYYYMMDD_Of_Array = EDDI_YYYYMMDD_Of_PrcntlArray, EDDI_PrcntlArray = EDDI_PrcntlArray)

#END section for training

#BEGIN section for evaluation

EDDI_YYYYMMDD_Of_PrcntlArray, EDDI_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(EDDI_YYYYMMDD_Of_RefArray, EDDI_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)

EDDI_PrcntlArray = LoopPercentileCalcOverSpatialUnits(EDDI_RefArray, EDDI_PrcntlArray)

Dev_EDDI_YYYYMMDD_Of_PrcntlArray = EDDI_YYYYMMDD_Of_PrcntlArray[::2]
Dev_EDDI_PrcntlArray = EDDI_PrcntlArray[::2]

Test_EDDI_YYYYMMDD_Of_PrcntlArray = EDDI_YYYYMMDD_Of_PrcntlArray[1::2]
Test_EDDI_PrcntlArray = EDDI_PrcntlArray[1::2]

print('Evaluation: Dev NumDates = ', Dev_EDDI_PrcntlArray.shape[0], ', NumSpatialUnits = ', Dev_EDDI_PrcntlArray.shape[1])
PrintInfoAboutArray(Dev_EDDI_PrcntlArray, 'Dev_EDDI_PrcntlArray')

print('Evaluation: Test NumDates = ', Test_EDDI_PrcntlArray.shape[0], ', NumSpatialUnits = ', Test_EDDI_PrcntlArray.shape[1])
PrintInfoAboutArray(Test_EDDI_PrcntlArray, 'Test_EDDI_PrcntlArray')

np.savez_compressed(DevDataFilename, YYYYMMDD_Of_Array = Dev_EDDI_YYYYMMDD_Of_PrcntlArray, EDDI_PrcntlArray = Dev_EDDI_PrcntlArray)

np.savez_compressed(TestDataFilename, YYYYMMDD_Of_Array = Test_EDDI_YYYYMMDD_Of_PrcntlArray, EDDI_PrcntlArray = Test_EDDI_PrcntlArray)

#END section for evaluation

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")



