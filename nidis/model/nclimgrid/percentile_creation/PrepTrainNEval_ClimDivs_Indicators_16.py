
# BEGIN code arguments / editable section

Training_BeginDateVecList = [2006, 1, 3] # Beginning training year, month, day of month, this is also a Tuesday
Training_EndDateVecList = [2018, 12, 25] # Ending training year, month, day of month, this is also a Tuesday

Eval_BeginDateVecList = [2019, 1, 1] # Beginning evaluation year, month, day of month, this is also a Tuesday
Eval_EndDateVecList = [2019, 12, 31] # Ending evaluation year, month, day of month, this is also a Tuesday

CPCsoilmoist_RefFileName = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/Indicator_16/weekly_resolution/RefArrays/ClimGrid_CPCsoilmoist_20080205To20191231.npz'


TrainDataFilename = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/Indicator_16/percentile_creation/PreppedTrainNEvalNpzs/Train_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'

DevDataFilename = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/Indicator_16/percentile_creation/PreppedTrainNEvalNpzs/PreppedTrainNEvalNpzs/Dev_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
TestDataFilename = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/Indicator_16/percentile_creation/PreppedTrainNEvalNpzs/PreppedTrainNEvalNpzs/Test_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

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

CPCsoilmoist_RefObject = np.load(CPCsoilmoist_RefFileName)
CPCsoilmoist_YYYYMMDD_Of_RefArray = CPCsoilmoist_RefObject['CPCsoilmoist_YYYYMMDD_Of_RefArray']

CPCsoilmoist_RefArray = CPCsoilmoist_RefObject['CPCsoilmoist_RefArray']

print(CPCsoilmoist_YYYYMMDD_Of_RefArray.shape)
print(CPCsoilmoist_RefArray.shape)

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

MonthlyList_CPCsoilmoist_YYYYMMDD_Of_RefArray, MonthlyList_CPCsoilmoist_RefArray = MonthlyList_YYYYMMDDAndArray(CPCsoilmoist_YYYYMMDD_Of_RefArray, CPCsoilmoist_RefArray)

print("Done with MonthlyList_CPCsoilmoist_YYYYMMDD_Of_RefArray", MonthlyList_CPCsoilmoist_YYYYMMDD_Of_RefArray.shape, MonthlyList_CPCsoilmoist_RefArray.shape)

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
  print('overall min is ',np.nanmin(ThisArray),', overall max is ',np.nanmax(ThisArray))
#end of def PrintInfoAboutArray(ThisArray, ThisArray_Str):

#BEGIN section for training

CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, CPCsoilmoist_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(CPCsoilmoist_YYYYMMDD_Of_RefArray, CPCsoilmoist_RefArray, Training_BeginDateVecList, Training_EndDateVecList)

MonthlyList_CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, MonthlyList_CPCsoilmoist_PrcntlArray = MonthlyList_YYYYMMDDAndArray(CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, CPCsoilmoist_PrcntlArray)

MonthlyList_CPCsoilmoist_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_CPCsoilmoist_RefArray, MonthlyList_CPCsoilmoist_PrcntlArray)

CPCsoilmoist_PrcntlArray = ReAssembleArraysFromMonthlyList(CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, CPCsoilmoist_PrcntlArray, MonthlyList_CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, MonthlyList_CPCsoilmoist_PrcntlArray)

PrintInfoAboutArray(CPCsoilmoist_PrcntlArray, 'CPCsoilmoist_PrcntlArray')


np.savez_compressed(TrainDataFilename, YYYYMMDD_Of_Array = CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, CPCsoilmoist_PrcntlArray = CPCsoilmoist_PrcntlArray) 

#END section for training

#BEGIN section for evaluation

Dev_CPCsoilmoist_YYYYMMDD_Of_PrcntlArray = CPCsoilmoist_YYYYMMDD_Of_PrcntlArray[::2]
Test_CPCsoilmoist_YYYYMMDD_Of_PrcntlArray = CPCsoilmoist_YYYYMMDD_Of_PrcntlArray[1::2]


CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, CPCsoilmoist_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(CPCsoilmoist_YYYYMMDD_Of_RefArray, CPCsoilmoist_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)

MonthlyList_CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, MonthlyList_CPCsoilmoist_PrcntlArray = MonthlyList_YYYYMMDDAndArray(CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, CPCsoilmoist_PrcntlArray)

MonthlyList_CPCsoilmoist_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_CPCsoilmoist_RefArray, MonthlyList_CPCsoilmoist_PrcntlArray)

CPCsoilmoist_PrcntlArray = ReAssembleArraysFromMonthlyList(CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, CPCsoilmoist_PrcntlArray, MonthlyList_CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, MonthlyList_CPCsoilmoist_PrcntlArray)

Dev_CPCsoilmoist_PrcntlArray = CPCsoilmoist_PrcntlArray[::2]

Test_CPCsoilmoist_PrcntlArray = CPCsoilmoist_PrcntlArray[1::2]

PrintInfoAboutArray(Dev_CPCsoilmoist_PrcntlArray, 'Dev_CPCsoilmoist_PrcntlArray')

PrintInfoAboutArray(Test_CPCsoilmoist_PrcntlArray, 'Test_CPCsoilmoist_PrcntlArray')

np.savez_compressed(DevDataFilename, YYYYMMDD_Of_Array = Dev_CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, CPCsoilmoist_PrcntlArray = Dev_CPCsoilmoist_PrcntlArray) 

np.savez_compressed(TestDataFilename, YYYYMMDD_Of_Array = Test_CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, CPCsoilmoist_PrcntlArray = Test_CPCsoilmoist_PrcntlArray) 

#END section for evaluation

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")



