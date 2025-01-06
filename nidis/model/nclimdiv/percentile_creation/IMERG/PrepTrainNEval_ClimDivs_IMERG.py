# Coded by Soni Yatheendradas
#         on Nov 12, 2021
from __future__ import division

# BEGIN code arguments / editable section

Training_BeginDateVecList = [2006, 1, 3] # Beginning training year, month, day of month, this is also a Tuesday
Training_EndDateVecList = [2018, 12, 25] # Ending training year, month, day of month, this is also a Tuesday

Eval_BeginDateVecList = [2019, 1, 1] # Beginning evaluation year, month, day of month, this is also a Tuesday
Eval_EndDateVecList = [2019, 12, 31] # Ending evaluation year, month, day of month, this is also a Tuesday

IMERG_01_RefFileName = 'RefArrays/ClimDiv_IMERG1Month_20000704To20210525.npz'
IMERG_02_RefFileName = 'RefArrays/ClimDiv_IMERG2Month_20000801To20210525.npz'
IMERG_03_RefFileName = 'RefArrays/ClimDiv_IMERG3Month_20000829To20210525.npz'
IMERG_06_RefFileName = 'RefArrays/ClimDiv_IMERG6Month_20001128To20210525.npz'
IMERG_09_RefFileName = 'RefArrays/ClimDiv_IMERG9Month_20010227To20210525.npz'
IMERG_12_RefFileName = 'RefArrays/ClimDiv_IMERG12Month_20010605To20210525.npz'
IMERG_24_RefFileName = 'RefArrays/ClimDiv_IMERG24Month_20020604To20210525.npz'
IMERG_36_RefFileName = 'RefArrays/ClimDiv_IMERG36Month_20030603To20210525.npz'
IMERG_48_RefFileName = 'RefArrays/ClimDiv_IMERG48Month_20040601To20210525.npz'
IMERG_60_RefFileName = 'RefArrays/ClimDiv_IMERG60Month_20050531To20210525.npz'
IMERG_72_RefFileName = 'RefArrays/ClimDiv_IMERG72Month_20060606To20210525.npz'

TrainDataFilename = 'PreppedTrainNEvalNpzs/ClimDivs/Train_IMERG_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'

DevDataFilename = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_IMERG_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
TestDataFilename = 'PreppedTrainNEvalNpzs/ClimDivs/Test_IMERG_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

# END code arguments / editable section

from datetime import date, datetime, timedelta
import sys
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

IMERG_01_RefObject = np.load(IMERG_01_RefFileName)
IMERG_02_RefObject = np.load(IMERG_02_RefFileName)
IMERG_03_RefObject = np.load(IMERG_03_RefFileName)
IMERG_06_RefObject = np.load(IMERG_06_RefFileName)
IMERG_09_RefObject = np.load(IMERG_09_RefFileName)
IMERG_12_RefObject = np.load(IMERG_12_RefFileName)
IMERG_24_RefObject = np.load(IMERG_24_RefFileName)
IMERG_36_RefObject = np.load(IMERG_36_RefFileName)
IMERG_48_RefObject = np.load(IMERG_48_RefFileName)
IMERG_60_RefObject = np.load(IMERG_60_RefFileName)
IMERG_72_RefObject = np.load(IMERG_72_RefFileName)

IMERG_01_YYYYMMDD_Of_RefArray = IMERG_01_RefObject['IMERG1Month_YYYYMMDD_Of_RefArray']
IMERG_02_YYYYMMDD_Of_RefArray = IMERG_02_RefObject['IMERG2Month_YYYYMMDD_Of_RefArray']
IMERG_03_YYYYMMDD_Of_RefArray = IMERG_03_RefObject['IMERG3Month_YYYYMMDD_Of_RefArray']
IMERG_06_YYYYMMDD_Of_RefArray = IMERG_06_RefObject['IMERG6Month_YYYYMMDD_Of_RefArray']
IMERG_09_YYYYMMDD_Of_RefArray = IMERG_09_RefObject['IMERG9Month_YYYYMMDD_Of_RefArray']
IMERG_12_YYYYMMDD_Of_RefArray = IMERG_12_RefObject['IMERG12Month_YYYYMMDD_Of_RefArray']
IMERG_24_YYYYMMDD_Of_RefArray = IMERG_24_RefObject['IMERG24Month_YYYYMMDD_Of_RefArray']
IMERG_36_YYYYMMDD_Of_RefArray = IMERG_36_RefObject['IMERG36Month_YYYYMMDD_Of_RefArray']
IMERG_48_YYYYMMDD_Of_RefArray = IMERG_48_RefObject['IMERG48Month_YYYYMMDD_Of_RefArray']
IMERG_60_YYYYMMDD_Of_RefArray = IMERG_60_RefObject['IMERG60Month_YYYYMMDD_Of_RefArray']
IMERG_72_YYYYMMDD_Of_RefArray = IMERG_72_RefObject['IMERG72Month_YYYYMMDD_Of_RefArray']

IMERG_01_RefArray = IMERG_01_RefObject['IMERG1Month_RefArray']
IMERG_02_RefArray = IMERG_02_RefObject['IMERG2Month_RefArray']
IMERG_03_RefArray = IMERG_03_RefObject['IMERG3Month_RefArray']
IMERG_06_RefArray = IMERG_06_RefObject['IMERG6Month_RefArray']
IMERG_09_RefArray = IMERG_09_RefObject['IMERG9Month_RefArray']
IMERG_12_RefArray = IMERG_12_RefObject['IMERG12Month_RefArray']
IMERG_24_RefArray = IMERG_24_RefObject['IMERG24Month_RefArray']
IMERG_36_RefArray = IMERG_36_RefObject['IMERG36Month_RefArray']
IMERG_48_RefArray = IMERG_48_RefObject['IMERG48Month_RefArray']
IMERG_60_RefArray = IMERG_60_RefObject['IMERG60Month_RefArray']
IMERG_72_RefArray = IMERG_72_RefObject['IMERG72Month_RefArray']

def MonthlyList_YYYYMMDDAndArray(YYYYMMDD_Of_Array, ThisArray):
  MM_Of_Array = (YYYYMMDD_Of_Array % 10000) // 100
  MonthlyList_YYYYMMDD_Of_Array = []
  MonthlyList_Array = []
  for WhichMonth in range(1,12+1):
    Idxs = np.where(MM_Of_Array == WhichMonth)
    YYYYMMDD_Of_Array_ThisMonth = YYYYMMDD_Of_Array[Idxs[0]]
    ThisArray_ThisMonth = ThisArray[Idxs[0]]
    MonthlyList_YYYYMMDD_Of_Array.append(YYYYMMDD_Of_Array_ThisMonth)
    MonthlyList_Array.append(ThisArray_ThisMonth)
  #end of for WhichMonth in range(1,12+1):
  return MonthlyList_YYYYMMDD_Of_Array, MonthlyList_Array
#end of def MonthlyList_YYYYMMDDAndArray(YYYYMMDD_Of_Array, ThisArray):

MonthlyList_IMERG_01_YYYYMMDD_Of_RefArray, MonthlyList_IMERG_01_RefArray = MonthlyList_YYYYMMDDAndArray(IMERG_01_YYYYMMDD_Of_RefArray, IMERG_01_RefArray)
MonthlyList_IMERG_02_YYYYMMDD_Of_RefArray, MonthlyList_IMERG_02_RefArray = MonthlyList_YYYYMMDDAndArray(IMERG_02_YYYYMMDD_Of_RefArray, IMERG_02_RefArray)
MonthlyList_IMERG_03_YYYYMMDD_Of_RefArray, MonthlyList_IMERG_03_RefArray = MonthlyList_YYYYMMDDAndArray(IMERG_03_YYYYMMDD_Of_RefArray, IMERG_03_RefArray)
MonthlyList_IMERG_06_YYYYMMDD_Of_RefArray, MonthlyList_IMERG_06_RefArray = MonthlyList_YYYYMMDDAndArray(IMERG_06_YYYYMMDD_Of_RefArray, IMERG_06_RefArray)
MonthlyList_IMERG_09_YYYYMMDD_Of_RefArray, MonthlyList_IMERG_09_RefArray = MonthlyList_YYYYMMDDAndArray(IMERG_09_YYYYMMDD_Of_RefArray, IMERG_09_RefArray)

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
  Values_1d_NotNaN = Values_1d[~np.isnan(Values_1d)]
  if RefArray_1d_NotNaN.size > 0:
    if Values_1d_NotNaN.size > 0:
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
    else: # if Values_1d_NotNaN.size > 0
      return Values_1d
    #end of if Values_1d_NotNaN.size > 0
  else: # if RefArray_1d_NotNaN.size > 0
    print('RefArray_1d_NotNaN.size == 0!!!')
    if Values_1d_NotNaN.size > 0:
      print('Values_1d_NotNaN.size > 0 when RefArray_1d_NotNaN.size == 0!!')
      sys.exit(0)
    else: # if Values_1d_NotNaN.size > 0
      return Values_1d
    #end of if Values_1d_NotNaN.size > 0
  #end of if RefArray_1d_NotNaN.size > 0
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

def LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_RefArray, MonthlyList_PrcntlArray):
  for WhichMonth in range(1,12+1):
    RefArray = MonthlyList_RefArray[WhichMonth-1]
    PrcntlArray = MonthlyList_PrcntlArray[WhichMonth-1]
    PrcntlArray = LoopPercentileCalcOverSpatialUnits(RefArray, PrcntlArray)
    MonthlyList_PrcntlArray[WhichMonth-1] = PrcntlArray
  #end of for WhichMonth in range(1,12+1):
  return MonthlyList_PrcntlArray
#end of def LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_RefArray, MonthlyList_PrcntlArray):

def ReAssembleArraysFromMonthlyList(YYYYMMDD_Of_PrcntlArray, PrcntlArray, MonthlyList_YYYYMMDD_Of_PrcntlArray, MonthlyList_PrcntlArray):
  YYYYMMDD_Of_PrcntlArray_1d = np.squeeze(YYYYMMDD_Of_PrcntlArray, axis = 1) 
  for WhichMonth in range(1,12+1):
    YYYYMMDD_Of_PrcntlArray_ThisMonth_1d = np.squeeze(MonthlyList_YYYYMMDD_Of_PrcntlArray[WhichMonth-1], axis = 1) 
    all_sorted = np.argsort(YYYYMMDD_Of_PrcntlArray_1d) 
    ThisMonth_pos = np.searchsorted(YYYYMMDD_Of_PrcntlArray_1d[all_sorted], YYYYMMDD_Of_PrcntlArray_ThisMonth_1d) 
    indices = all_sorted[ThisMonth_pos]
    PrcntlArray[indices, :] = MonthlyList_PrcntlArray[WhichMonth-1] 
  #end of for WhichMonth in range(1,12+1):
  return PrcntlArray
#end of def ReAssembleArraysFromMonthlyList(YYYYMMDD_Of_PrcntlArray, PrcntlArray, MonthlyList_YYYYMMDD_Of_PrcntlArray, MonthlyList_PrcntlArray):

def PrintInfoAboutArray(ThisArray, ThisArray_Str):
  print(ThisArray_Str,".shape is ",ThisArray.shape)
  print(ThisArray_Str,".dtype is ",ThisArray.dtype)
  print(ThisArray_Str," is ",ThisArray)
  print("np.amin(np.isnan(",ThisArray_Str,").sum(axis=0)) is ",np.amin(np.isnan(ThisArray).sum(axis=0)))
  print("np.amax(np.isnan(",ThisArray_Str,").sum(axis=0)) is ",np.amax(np.isnan(ThisArray).sum(axis=0)))
  print("np.amin(np.isnan(",ThisArray_Str,").sum(axis=1)) is ",np.amin(np.isnan(ThisArray).sum(axis=1)))
  print("np.amax(np.isnan(",ThisArray_Str,").sum(axis=1)) is ",np.amax(np.isnan(ThisArray).sum(axis=1)))
  print('overall min is ',np.nanmin(ThisArray),', overall max is ',np.nanmax(ThisArray))
#end of def PrintInfoAboutArray(ThisArray, ThisArray_Str):

#BEGIN section for training

IMERG_01_YYYYMMDD_Of_PrcntlArray, IMERG_01_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_01_YYYYMMDD_Of_RefArray, IMERG_01_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
IMERG_02_YYYYMMDD_Of_PrcntlArray, IMERG_02_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_02_YYYYMMDD_Of_RefArray, IMERG_02_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
IMERG_03_YYYYMMDD_Of_PrcntlArray, IMERG_03_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_03_YYYYMMDD_Of_RefArray, IMERG_03_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
IMERG_06_YYYYMMDD_Of_PrcntlArray, IMERG_06_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_06_YYYYMMDD_Of_RefArray, IMERG_06_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
IMERG_09_YYYYMMDD_Of_PrcntlArray, IMERG_09_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_09_YYYYMMDD_Of_RefArray, IMERG_09_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
IMERG_12_YYYYMMDD_Of_PrcntlArray, IMERG_12_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_12_YYYYMMDD_Of_RefArray, IMERG_12_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
IMERG_24_YYYYMMDD_Of_PrcntlArray, IMERG_24_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_24_YYYYMMDD_Of_RefArray, IMERG_24_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
IMERG_36_YYYYMMDD_Of_PrcntlArray, IMERG_36_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_36_YYYYMMDD_Of_RefArray, IMERG_36_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
IMERG_48_YYYYMMDD_Of_PrcntlArray, IMERG_48_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_48_YYYYMMDD_Of_RefArray, IMERG_48_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
IMERG_60_YYYYMMDD_Of_PrcntlArray, IMERG_60_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_60_YYYYMMDD_Of_RefArray, IMERG_60_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
IMERG_72_YYYYMMDD_Of_PrcntlArray, IMERG_72_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_72_YYYYMMDD_Of_RefArray, IMERG_72_RefArray, Training_BeginDateVecList, Training_EndDateVecList)

MonthlyList_IMERG_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_IMERG_01_PrcntlArray = MonthlyList_YYYYMMDDAndArray(IMERG_01_YYYYMMDD_Of_PrcntlArray, IMERG_01_PrcntlArray)
MonthlyList_IMERG_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_IMERG_02_PrcntlArray = MonthlyList_YYYYMMDDAndArray(IMERG_02_YYYYMMDD_Of_PrcntlArray, IMERG_02_PrcntlArray)
MonthlyList_IMERG_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_IMERG_03_PrcntlArray = MonthlyList_YYYYMMDDAndArray(IMERG_03_YYYYMMDD_Of_PrcntlArray, IMERG_03_PrcntlArray)
MonthlyList_IMERG_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_IMERG_06_PrcntlArray = MonthlyList_YYYYMMDDAndArray(IMERG_06_YYYYMMDD_Of_PrcntlArray, IMERG_06_PrcntlArray)
MonthlyList_IMERG_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_IMERG_09_PrcntlArray = MonthlyList_YYYYMMDDAndArray(IMERG_09_YYYYMMDD_Of_PrcntlArray, IMERG_09_PrcntlArray)

IMERG_12_PrcntlArray = LoopPercentileCalcOverSpatialUnits(IMERG_12_RefArray, IMERG_12_PrcntlArray)
IMERG_24_PrcntlArray = LoopPercentileCalcOverSpatialUnits(IMERG_24_RefArray, IMERG_24_PrcntlArray)
IMERG_36_PrcntlArray = LoopPercentileCalcOverSpatialUnits(IMERG_36_RefArray, IMERG_36_PrcntlArray)
IMERG_48_PrcntlArray = LoopPercentileCalcOverSpatialUnits(IMERG_48_RefArray, IMERG_48_PrcntlArray)
IMERG_60_PrcntlArray = LoopPercentileCalcOverSpatialUnits(IMERG_60_RefArray, IMERG_60_PrcntlArray)
IMERG_72_PrcntlArray = LoopPercentileCalcOverSpatialUnits(IMERG_72_RefArray, IMERG_72_PrcntlArray)

MonthlyList_IMERG_01_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_IMERG_01_RefArray, MonthlyList_IMERG_01_PrcntlArray)
MonthlyList_IMERG_02_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_IMERG_02_RefArray, MonthlyList_IMERG_02_PrcntlArray)
MonthlyList_IMERG_03_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_IMERG_03_RefArray, MonthlyList_IMERG_03_PrcntlArray)
MonthlyList_IMERG_06_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_IMERG_06_RefArray, MonthlyList_IMERG_06_PrcntlArray)
MonthlyList_IMERG_09_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_IMERG_09_RefArray, MonthlyList_IMERG_09_PrcntlArray)

IMERG_01_PrcntlArray = ReAssembleArraysFromMonthlyList(IMERG_01_YYYYMMDD_Of_PrcntlArray, IMERG_01_PrcntlArray, MonthlyList_IMERG_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_IMERG_01_PrcntlArray)
IMERG_02_PrcntlArray = ReAssembleArraysFromMonthlyList(IMERG_02_YYYYMMDD_Of_PrcntlArray, IMERG_02_PrcntlArray, MonthlyList_IMERG_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_IMERG_02_PrcntlArray)
IMERG_03_PrcntlArray = ReAssembleArraysFromMonthlyList(IMERG_03_YYYYMMDD_Of_PrcntlArray, IMERG_03_PrcntlArray, MonthlyList_IMERG_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_IMERG_03_PrcntlArray)
IMERG_06_PrcntlArray = ReAssembleArraysFromMonthlyList(IMERG_06_YYYYMMDD_Of_PrcntlArray, IMERG_06_PrcntlArray, MonthlyList_IMERG_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_IMERG_06_PrcntlArray)
IMERG_09_PrcntlArray = ReAssembleArraysFromMonthlyList(IMERG_09_YYYYMMDD_Of_PrcntlArray, IMERG_09_PrcntlArray, MonthlyList_IMERG_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_IMERG_09_PrcntlArray)

print('Training: NumDates = ', IMERG_01_PrcntlArray.shape[0], ', NumSpatialUnits = ',IMERG_01_PrcntlArray.shape[1])

PrintInfoAboutArray(IMERG_01_YYYYMMDD_Of_PrcntlArray, 'IMERG_01_YYYYMMDD_Of_PrcntlArray')

PrintInfoAboutArray(IMERG_01_PrcntlArray, 'IMERG_01_PrcntlArray')
PrintInfoAboutArray(IMERG_02_PrcntlArray, 'IMERG_02_PrcntlArray')
PrintInfoAboutArray(IMERG_03_PrcntlArray, 'IMERG_03_PrcntlArray')
PrintInfoAboutArray(IMERG_06_PrcntlArray, 'IMERG_06_PrcntlArray')
PrintInfoAboutArray(IMERG_09_PrcntlArray, 'IMERG_09_PrcntlArray')
PrintInfoAboutArray(IMERG_12_PrcntlArray, 'IMERG_12_PrcntlArray')
PrintInfoAboutArray(IMERG_24_PrcntlArray, 'IMERG_24_PrcntlArray')
PrintInfoAboutArray(IMERG_36_PrcntlArray, 'IMERG_36_PrcntlArray')
PrintInfoAboutArray(IMERG_48_PrcntlArray, 'IMERG_48_PrcntlArray')
PrintInfoAboutArray(IMERG_60_PrcntlArray, 'IMERG_60_PrcntlArray')
PrintInfoAboutArray(IMERG_72_PrcntlArray, 'IMERG_72_PrcntlArray')

np.savez_compressed(TrainDataFilename, 
                    YYYYMMDD_Of_Array = IMERG_01_YYYYMMDD_Of_PrcntlArray, 
                    IMERG_01_PrcntlArray = IMERG_01_PrcntlArray, 
                    IMERG_02_PrcntlArray = IMERG_02_PrcntlArray, 
                    IMERG_03_PrcntlArray = IMERG_03_PrcntlArray, 
                    IMERG_06_PrcntlArray = IMERG_06_PrcntlArray, 
                    IMERG_09_PrcntlArray = IMERG_09_PrcntlArray, 
                    IMERG_24_PrcntlArray = IMERG_24_PrcntlArray, 
                    IMERG_12_PrcntlArray = IMERG_12_PrcntlArray, 
                    IMERG_36_PrcntlArray = IMERG_36_PrcntlArray, 
                    IMERG_48_PrcntlArray = IMERG_48_PrcntlArray, 
                    IMERG_60_PrcntlArray = IMERG_60_PrcntlArray, 
                    IMERG_72_PrcntlArray = IMERG_72_PrcntlArray)

#END section for training

#BEGIN section for evaluation

IMERG_01_YYYYMMDD_Of_PrcntlArray, IMERG_01_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_01_YYYYMMDD_Of_RefArray, IMERG_01_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
IMERG_02_YYYYMMDD_Of_PrcntlArray, IMERG_02_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_02_YYYYMMDD_Of_RefArray, IMERG_02_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
IMERG_03_YYYYMMDD_Of_PrcntlArray, IMERG_03_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_03_YYYYMMDD_Of_RefArray, IMERG_03_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
IMERG_06_YYYYMMDD_Of_PrcntlArray, IMERG_06_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_06_YYYYMMDD_Of_RefArray, IMERG_06_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
IMERG_09_YYYYMMDD_Of_PrcntlArray, IMERG_09_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_09_YYYYMMDD_Of_RefArray, IMERG_09_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
IMERG_12_YYYYMMDD_Of_PrcntlArray, IMERG_12_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_12_YYYYMMDD_Of_RefArray, IMERG_12_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
IMERG_24_YYYYMMDD_Of_PrcntlArray, IMERG_24_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_24_YYYYMMDD_Of_RefArray, IMERG_24_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
IMERG_36_YYYYMMDD_Of_PrcntlArray, IMERG_36_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_36_YYYYMMDD_Of_RefArray, IMERG_36_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
IMERG_48_YYYYMMDD_Of_PrcntlArray, IMERG_48_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_48_YYYYMMDD_Of_RefArray, IMERG_48_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
IMERG_60_YYYYMMDD_Of_PrcntlArray, IMERG_60_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_60_YYYYMMDD_Of_RefArray, IMERG_60_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
IMERG_72_YYYYMMDD_Of_PrcntlArray, IMERG_72_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(IMERG_72_YYYYMMDD_Of_RefArray, IMERG_72_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)

MonthlyList_IMERG_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_IMERG_01_PrcntlArray = MonthlyList_YYYYMMDDAndArray(IMERG_01_YYYYMMDD_Of_PrcntlArray, IMERG_01_PrcntlArray)
MonthlyList_IMERG_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_IMERG_02_PrcntlArray = MonthlyList_YYYYMMDDAndArray(IMERG_02_YYYYMMDD_Of_PrcntlArray, IMERG_02_PrcntlArray)
MonthlyList_IMERG_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_IMERG_03_PrcntlArray = MonthlyList_YYYYMMDDAndArray(IMERG_03_YYYYMMDD_Of_PrcntlArray, IMERG_03_PrcntlArray)
MonthlyList_IMERG_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_IMERG_06_PrcntlArray = MonthlyList_YYYYMMDDAndArray(IMERG_06_YYYYMMDD_Of_PrcntlArray, IMERG_06_PrcntlArray)
MonthlyList_IMERG_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_IMERG_09_PrcntlArray = MonthlyList_YYYYMMDDAndArray(IMERG_09_YYYYMMDD_Of_PrcntlArray, IMERG_09_PrcntlArray)

IMERG_12_PrcntlArray = LoopPercentileCalcOverSpatialUnits(IMERG_12_RefArray, IMERG_12_PrcntlArray)
IMERG_24_PrcntlArray = LoopPercentileCalcOverSpatialUnits(IMERG_24_RefArray, IMERG_24_PrcntlArray)
IMERG_36_PrcntlArray = LoopPercentileCalcOverSpatialUnits(IMERG_36_RefArray, IMERG_36_PrcntlArray)
IMERG_48_PrcntlArray = LoopPercentileCalcOverSpatialUnits(IMERG_48_RefArray, IMERG_48_PrcntlArray)
IMERG_60_PrcntlArray = LoopPercentileCalcOverSpatialUnits(IMERG_60_RefArray, IMERG_60_PrcntlArray)
IMERG_72_PrcntlArray = LoopPercentileCalcOverSpatialUnits(IMERG_72_RefArray, IMERG_72_PrcntlArray)

MonthlyList_IMERG_01_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_IMERG_01_RefArray, MonthlyList_IMERG_01_PrcntlArray)
MonthlyList_IMERG_02_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_IMERG_02_RefArray, MonthlyList_IMERG_02_PrcntlArray)
MonthlyList_IMERG_03_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_IMERG_03_RefArray, MonthlyList_IMERG_03_PrcntlArray)
MonthlyList_IMERG_06_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_IMERG_06_RefArray, MonthlyList_IMERG_06_PrcntlArray)
MonthlyList_IMERG_09_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_IMERG_09_RefArray, MonthlyList_IMERG_09_PrcntlArray)

IMERG_01_PrcntlArray = ReAssembleArraysFromMonthlyList(IMERG_01_YYYYMMDD_Of_PrcntlArray, IMERG_01_PrcntlArray, MonthlyList_IMERG_01_YYYYMMDD_Of_PrcntlArray, MonthlyList_IMERG_01_PrcntlArray)
IMERG_02_PrcntlArray = ReAssembleArraysFromMonthlyList(IMERG_02_YYYYMMDD_Of_PrcntlArray, IMERG_02_PrcntlArray, MonthlyList_IMERG_02_YYYYMMDD_Of_PrcntlArray, MonthlyList_IMERG_02_PrcntlArray)
IMERG_03_PrcntlArray = ReAssembleArraysFromMonthlyList(IMERG_03_YYYYMMDD_Of_PrcntlArray, IMERG_03_PrcntlArray, MonthlyList_IMERG_03_YYYYMMDD_Of_PrcntlArray, MonthlyList_IMERG_03_PrcntlArray)
IMERG_06_PrcntlArray = ReAssembleArraysFromMonthlyList(IMERG_06_YYYYMMDD_Of_PrcntlArray, IMERG_06_PrcntlArray, MonthlyList_IMERG_06_YYYYMMDD_Of_PrcntlArray, MonthlyList_IMERG_06_PrcntlArray)
IMERG_09_PrcntlArray = ReAssembleArraysFromMonthlyList(IMERG_09_YYYYMMDD_Of_PrcntlArray, IMERG_09_PrcntlArray, MonthlyList_IMERG_09_YYYYMMDD_Of_PrcntlArray, MonthlyList_IMERG_09_PrcntlArray)

Dev_IMERG_01_YYYYMMDD_Of_PrcntlArray = IMERG_01_YYYYMMDD_Of_PrcntlArray[::2]
Dev_IMERG_02_YYYYMMDD_Of_PrcntlArray = IMERG_02_YYYYMMDD_Of_PrcntlArray[::2]
Dev_IMERG_03_YYYYMMDD_Of_PrcntlArray = IMERG_03_YYYYMMDD_Of_PrcntlArray[::2]
Dev_IMERG_06_YYYYMMDD_Of_PrcntlArray = IMERG_06_YYYYMMDD_Of_PrcntlArray[::2]
Dev_IMERG_09_YYYYMMDD_Of_PrcntlArray = IMERG_09_YYYYMMDD_Of_PrcntlArray[::2]
Dev_IMERG_12_YYYYMMDD_Of_PrcntlArray = IMERG_12_YYYYMMDD_Of_PrcntlArray[::2]
Dev_IMERG_24_YYYYMMDD_Of_PrcntlArray = IMERG_24_YYYYMMDD_Of_PrcntlArray[::2]
Dev_IMERG_36_YYYYMMDD_Of_PrcntlArray = IMERG_36_YYYYMMDD_Of_PrcntlArray[::2]
Dev_IMERG_48_YYYYMMDD_Of_PrcntlArray = IMERG_48_YYYYMMDD_Of_PrcntlArray[::2]
Dev_IMERG_60_YYYYMMDD_Of_PrcntlArray = IMERG_60_YYYYMMDD_Of_PrcntlArray[::2]
Dev_IMERG_72_YYYYMMDD_Of_PrcntlArray = IMERG_72_YYYYMMDD_Of_PrcntlArray[::2]

Dev_IMERG_01_PrcntlArray = IMERG_01_PrcntlArray[::2]
Dev_IMERG_02_PrcntlArray = IMERG_02_PrcntlArray[::2]
Dev_IMERG_03_PrcntlArray = IMERG_03_PrcntlArray[::2]
Dev_IMERG_06_PrcntlArray = IMERG_06_PrcntlArray[::2]
Dev_IMERG_09_PrcntlArray = IMERG_09_PrcntlArray[::2]
Dev_IMERG_12_PrcntlArray = IMERG_12_PrcntlArray[::2]
Dev_IMERG_24_PrcntlArray = IMERG_24_PrcntlArray[::2]
Dev_IMERG_36_PrcntlArray = IMERG_36_PrcntlArray[::2]
Dev_IMERG_48_PrcntlArray = IMERG_48_PrcntlArray[::2]
Dev_IMERG_60_PrcntlArray = IMERG_60_PrcntlArray[::2]
Dev_IMERG_72_PrcntlArray = IMERG_72_PrcntlArray[::2]

Test_IMERG_01_YYYYMMDD_Of_PrcntlArray = IMERG_01_YYYYMMDD_Of_PrcntlArray[1::2]
Test_IMERG_02_YYYYMMDD_Of_PrcntlArray = IMERG_02_YYYYMMDD_Of_PrcntlArray[1::2]
Test_IMERG_03_YYYYMMDD_Of_PrcntlArray = IMERG_03_YYYYMMDD_Of_PrcntlArray[1::2]
Test_IMERG_06_YYYYMMDD_Of_PrcntlArray = IMERG_06_YYYYMMDD_Of_PrcntlArray[1::2]
Test_IMERG_09_YYYYMMDD_Of_PrcntlArray = IMERG_09_YYYYMMDD_Of_PrcntlArray[1::2]
Test_IMERG_12_YYYYMMDD_Of_PrcntlArray = IMERG_12_YYYYMMDD_Of_PrcntlArray[1::2]
Test_IMERG_24_YYYYMMDD_Of_PrcntlArray = IMERG_24_YYYYMMDD_Of_PrcntlArray[1::2]
Test_IMERG_36_YYYYMMDD_Of_PrcntlArray = IMERG_36_YYYYMMDD_Of_PrcntlArray[1::2]
Test_IMERG_48_YYYYMMDD_Of_PrcntlArray = IMERG_48_YYYYMMDD_Of_PrcntlArray[1::2]
Test_IMERG_60_YYYYMMDD_Of_PrcntlArray = IMERG_60_YYYYMMDD_Of_PrcntlArray[1::2]
Test_IMERG_72_YYYYMMDD_Of_PrcntlArray = IMERG_72_YYYYMMDD_Of_PrcntlArray[1::2]

Test_IMERG_01_PrcntlArray = IMERG_01_PrcntlArray[1::2]
Test_IMERG_02_PrcntlArray = IMERG_02_PrcntlArray[1::2]
Test_IMERG_03_PrcntlArray = IMERG_03_PrcntlArray[1::2]
Test_IMERG_06_PrcntlArray = IMERG_06_PrcntlArray[1::2]
Test_IMERG_09_PrcntlArray = IMERG_09_PrcntlArray[1::2]
Test_IMERG_12_PrcntlArray = IMERG_12_PrcntlArray[1::2]
Test_IMERG_24_PrcntlArray = IMERG_24_PrcntlArray[1::2]
Test_IMERG_36_PrcntlArray = IMERG_36_PrcntlArray[1::2]
Test_IMERG_48_PrcntlArray = IMERG_48_PrcntlArray[1::2]
Test_IMERG_60_PrcntlArray = IMERG_60_PrcntlArray[1::2]
Test_IMERG_72_PrcntlArray = IMERG_72_PrcntlArray[1::2]

print('Evaluation: Dev NumDates = ', Dev_IMERG_01_PrcntlArray.shape[0], ', NumSpatialUnits = ',Dev_IMERG_01_PrcntlArray.shape[1])

PrintInfoAboutArray(Dev_IMERG_01_YYYYMMDD_Of_PrcntlArray, 'Dev_IMERG_01_YYYYMMDD_Of_PrcntlArray')

PrintInfoAboutArray(Dev_IMERG_01_PrcntlArray, 'Dev_IMERG_01_PrcntlArray')
PrintInfoAboutArray(Dev_IMERG_02_PrcntlArray, 'Dev_IMERG_02_PrcntlArray')
PrintInfoAboutArray(Dev_IMERG_03_PrcntlArray, 'Dev_IMERG_03_PrcntlArray')
PrintInfoAboutArray(Dev_IMERG_06_PrcntlArray, 'Dev_IMERG_06_PrcntlArray')
PrintInfoAboutArray(Dev_IMERG_09_PrcntlArray, 'Dev_IMERG_09_PrcntlArray')
PrintInfoAboutArray(Dev_IMERG_12_PrcntlArray, 'Dev_IMERG_12_PrcntlArray')
PrintInfoAboutArray(Dev_IMERG_24_PrcntlArray, 'Dev_IMERG_24_PrcntlArray')
PrintInfoAboutArray(Dev_IMERG_36_PrcntlArray, 'Dev_IMERG_36_PrcntlArray')
PrintInfoAboutArray(Dev_IMERG_48_PrcntlArray, 'Dev_IMERG_48_PrcntlArray')
PrintInfoAboutArray(Dev_IMERG_60_PrcntlArray, 'Dev_IMERG_60_PrcntlArray')
PrintInfoAboutArray(Dev_IMERG_72_PrcntlArray, 'Dev_IMERG_72_PrcntlArray')

print('Evaluation: Test NumDates = ', Test_IMERG_01_PrcntlArray.shape[0], ', NumSpatialUnits = ',Test_IMERG_01_PrcntlArray.shape[1])

PrintInfoAboutArray(Test_IMERG_01_YYYYMMDD_Of_PrcntlArray, 'Test_IMERG_01_YYYYMMDD_Of_PrcntlArray')

PrintInfoAboutArray(Test_IMERG_01_PrcntlArray, 'Test_IMERG_01_PrcntlArray')
PrintInfoAboutArray(Test_IMERG_02_PrcntlArray, 'Test_IMERG_02_PrcntlArray')
PrintInfoAboutArray(Test_IMERG_03_PrcntlArray, 'Test_IMERG_03_PrcntlArray')
PrintInfoAboutArray(Test_IMERG_06_PrcntlArray, 'Test_IMERG_06_PrcntlArray')
PrintInfoAboutArray(Test_IMERG_09_PrcntlArray, 'Test_IMERG_09_PrcntlArray')
PrintInfoAboutArray(Test_IMERG_12_PrcntlArray, 'Test_IMERG_12_PrcntlArray')
PrintInfoAboutArray(Test_IMERG_24_PrcntlArray, 'Test_IMERG_24_PrcntlArray')
PrintInfoAboutArray(Test_IMERG_36_PrcntlArray, 'Test_IMERG_36_PrcntlArray')
PrintInfoAboutArray(Test_IMERG_48_PrcntlArray, 'Test_IMERG_48_PrcntlArray')
PrintInfoAboutArray(Test_IMERG_60_PrcntlArray, 'Test_IMERG_60_PrcntlArray')
PrintInfoAboutArray(Test_IMERG_72_PrcntlArray, 'Test_IMERG_72_PrcntlArray')

np.savez_compressed(DevDataFilename, 
                    YYYYMMDD_Of_Array = Dev_IMERG_01_YYYYMMDD_Of_PrcntlArray, 
                    IMERG_01_PrcntlArray = Dev_IMERG_01_PrcntlArray, 
                    IMERG_02_PrcntlArray = Dev_IMERG_02_PrcntlArray, 
                    IMERG_03_PrcntlArray = Dev_IMERG_03_PrcntlArray, 
                    IMERG_06_PrcntlArray = Dev_IMERG_06_PrcntlArray, 
                    IMERG_09_PrcntlArray = Dev_IMERG_09_PrcntlArray, 
                    IMERG_24_PrcntlArray = Dev_IMERG_24_PrcntlArray, 
                    IMERG_12_PrcntlArray = Dev_IMERG_12_PrcntlArray, 
                    IMERG_36_PrcntlArray = Dev_IMERG_36_PrcntlArray, 
                    IMERG_48_PrcntlArray = Dev_IMERG_48_PrcntlArray, 
                    IMERG_60_PrcntlArray = Dev_IMERG_60_PrcntlArray, 
                    IMERG_72_PrcntlArray = Dev_IMERG_72_PrcntlArray)

np.savez_compressed(TestDataFilename, 
                    YYYYMMDD_Of_Array = Test_IMERG_01_YYYYMMDD_Of_PrcntlArray, 
                    IMERG_01_PrcntlArray = Test_IMERG_01_PrcntlArray, 
                    IMERG_02_PrcntlArray = Test_IMERG_02_PrcntlArray, 
                    IMERG_03_PrcntlArray = Test_IMERG_03_PrcntlArray, 
                    IMERG_06_PrcntlArray = Test_IMERG_06_PrcntlArray, 
                    IMERG_09_PrcntlArray = Test_IMERG_09_PrcntlArray, 
                    IMERG_24_PrcntlArray = Test_IMERG_24_PrcntlArray, 
                    IMERG_12_PrcntlArray = Test_IMERG_12_PrcntlArray, 
                    IMERG_36_PrcntlArray = Test_IMERG_36_PrcntlArray, 
                    IMERG_48_PrcntlArray = Test_IMERG_48_PrcntlArray, 
                    IMERG_60_PrcntlArray = Test_IMERG_60_PrcntlArray, 
                    IMERG_72_PrcntlArray = Test_IMERG_72_PrcntlArray)

#END section for evaluation

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")



