
# BEGIN code arguments / editable section

Training_BeginDateVecList = [2006, 1, 3] # Beginning training year, month, day of month, this is also a Tuesday
Training_EndDateVecList = [2018, 12, 25] # Ending training year, month, day of month, this is also a Tuesday

Eval_BeginDateVecList = [2019, 1, 1] # Beginning evaluation year, month, day of month, this is also a Tuesday
Eval_EndDateVecList = [2019, 12, 31] # Ending evaluation year, month, day of month, this is also a Tuesday

ZIndex_RefFileName = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/Indicators_1_to_4/weekly_resolution_output/ClimGrid_ZIndex_19320119To20191231.npz'
ZIndex60month_RefFileName = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/Indicators_1_to_4/weekly_resolution_output/ClimGrid_ZIndex60month_19320119To20191231.npz'
PMDI_RefFileName = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/Indicators_1_to_4/weekly_resolution_output/ClimGrid_PMDI_20050104To20191231.npz'
PHDI_RefFileName = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/Indicators_1_to_4/weekly_resolution_output/ClimGrid_PHDI_20050607To20191231.npz'

#USDM_InfoFileName = '/discover/nobackup/syatheen/NIDIS/Data/usdm_shapefiles/private/InfoArrWeekly_20000104To20200428.npz'
#USDM_InfoFileName = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/usdm_shapefiles/private/InfoArrWeekly_20000104To20200428.npz'

TrainDataFilename = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/Indicators_1_to_4/percentile_output/PreppedTrainNEvalNpzs/Train_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'

DevDataFilename = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/Indicators_1_to_4/percentile_output/PreppedTrainNEvalNpzs/Dev_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
TestDataFilename = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/Indicators_1_to_4/percentile_output/PreppedTrainNEvalNpzs/Test_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

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

ZIndex_RefObject = np.load(ZIndex_RefFileName)
ZIndex60month_RefObject = np.load(ZIndex60month_RefFileName)
PMDI_RefObject = np.load(PMDI_RefFileName)
PHDI_RefObject = np.load(PHDI_RefFileName)
#Pcpn1month_RefObject = np.load(Pcpn1month_RefFileName)
#Pcpn3month_RefObject = np.load(Pcpn3month_RefFileName)
#Pcpn6month_RefObject = np.load(Pcpn6month_RefFileName)
#Pcpn12month_RefObject = np.load(Pcpn12month_RefFileName)
#Pcpn24month_RefObject = np.load(Pcpn24month_RefFileName)
#Pcpn60month_RefObject = np.load(Pcpn60month_RefFileName)
#CPCsoilmoist_RefObject = np.load(CPCsoilmoist_RefFileName)

#USDM_InfoObject = np.load(USDM_InfoFileName)

ZIndex_YYYYMMDD_Of_RefArray = ZIndex_RefObject['ZIndex_YYYYMMDD_Of_RefArray']
PMDI_YYYYMMDD_Of_RefArray = PMDI_RefObject['PMDI_YYYYMMDD_Of_RefArray']
PHDI_YYYYMMDD_Of_RefArray = PHDI_RefObject['PHDI_YYYYMMDD_Of_RefArray']
#Pcpn_YYYYMMDD_Of_RefArray = Pcpn1month_RefObject['Pcpn_YYYYMMDD_Of_RefArray']
#CPCsoilmoist_YYYYMMDD_Of_RefArray = CPCsoilmoist_RefObject['CPCsoilmoist_YYYYMMDD_Of_RefArray']

#USDM_YYYYMMDD_Of_InfoArray = USDM_InfoObject['YYYYMMDD_Of_InfoArray']

ZIndex_RefArray = ZIndex_RefObject['ZIndex_RefArray']
ZIndex60month_RefArray = ZIndex60month_RefObject['ZIndex60month_RefArray']
PMDI_RefArray = PMDI_RefObject['PMDI_RefArray']
PHDI_RefArray = PHDI_RefObject['PHDI_RefArray']
#Pcpn1month_RefArray = Pcpn1month_RefObject['Pcpn1month_RefArray']
#Pcpn3month_RefArray = Pcpn3month_RefObject['Pcpn3month_RefArray']
#Pcpn6month_RefArray = Pcpn6month_RefObject['Pcpn6month_RefArray']
#Pcpn12month_RefArray = Pcpn12month_RefObject['Pcpn12month_RefArray']
#Pcpn24month_RefArray = Pcpn24month_RefObject['Pcpn24month_RefArray']
#Pcpn60month_RefArray = Pcpn60month_RefObject['Pcpn60month_RefArray']
#CPCsoilmoist_RefArray = CPCsoilmoist_RefObject['CPCsoilmoist_RefArray']

#USDM_InfoArray = USDM_InfoObject['InfoArray']

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

MonthlyList_PMDI_YYYYMMDD_Of_RefArray, MonthlyList_PMDI_RefArray = MonthlyList_YYYYMMDDAndArray(PMDI_YYYYMMDD_Of_RefArray, PMDI_RefArray)
MonthlyList_PHDI_YYYYMMDD_Of_RefArray, MonthlyList_PHDI_RefArray = MonthlyList_YYYYMMDDAndArray(PHDI_YYYYMMDD_Of_RefArray, PHDI_RefArray)
#MonthlyList_Pcpn_YYYYMMDD_Of_RefArray, MonthlyList_Pcpn1month_RefArray = MonthlyList_YYYYMMDDAndArray(Pcpn_YYYYMMDD_Of_RefArray, Pcpn1month_RefArray)
#MonthlyList_Pcpn_YYYYMMDD_Of_RefArray, MonthlyList_Pcpn3month_RefArray = MonthlyList_YYYYMMDDAndArray(Pcpn_YYYYMMDD_Of_RefArray, Pcpn3month_RefArray)
#MonthlyList_Pcpn_YYYYMMDD_Of_RefArray, MonthlyList_Pcpn6month_RefArray = MonthlyList_YYYYMMDDAndArray(Pcpn_YYYYMMDD_Of_RefArray, Pcpn6month_RefArray)
#MonthlyList_Pcpn_YYYYMMDD_Of_RefArray, MonthlyList_Pcpn12month_RefArray = MonthlyList_YYYYMMDDAndArray(Pcpn_YYYYMMDD_Of_RefArray, Pcpn12month_RefArray)
#MonthlyList_Pcpn_YYYYMMDD_Of_RefArray, MonthlyList_Pcpn24month_RefArray = MonthlyList_YYYYMMDDAndArray(Pcpn_YYYYMMDD_Of_RefArray, Pcpn24month_RefArray)
#MonthlyList_Pcpn_YYYYMMDD_Of_RefArray, MonthlyList_Pcpn60month_RefArray = MonthlyList_YYYYMMDDAndArray(Pcpn_YYYYMMDD_Of_RefArray, Pcpn60month_RefArray)
#MonthlyList_CPCsoilmoist_YYYYMMDD_Of_RefArray, MonthlyList_CPCsoilmoist_RefArray = MonthlyList_YYYYMMDDAndArray(CPCsoilmoist_YYYYMMDD_Of_RefArray, CPCsoilmoist_RefArray)

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

ZIndex_YYYYMMDD_Of_PrcntlArray, ZIndex_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(ZIndex_YYYYMMDD_Of_RefArray, ZIndex_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
ZIndex_YYYYMMDD_Of_PrcntlArray, ZIndex60month_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(ZIndex_YYYYMMDD_Of_RefArray, ZIndex60month_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
PMDI_YYYYMMDD_Of_PrcntlArray, PMDI_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(PMDI_YYYYMMDD_Of_RefArray, PMDI_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
PHDI_YYYYMMDD_Of_PrcntlArray, PHDI_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(PHDI_YYYYMMDD_Of_RefArray, PHDI_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
#Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn1month_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(Pcpn_YYYYMMDD_Of_RefArray, Pcpn1month_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
#Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn3month_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(Pcpn_YYYYMMDD_Of_RefArray, Pcpn3month_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
#Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn6month_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(Pcpn_YYYYMMDD_Of_RefArray, Pcpn6month_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
#Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn12month_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(Pcpn_YYYYMMDD_Of_RefArray, Pcpn12month_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
#Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn24month_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(Pcpn_YYYYMMDD_Of_RefArray, Pcpn24month_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
#Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn60month_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(Pcpn_YYYYMMDD_Of_RefArray, Pcpn60month_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
#CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, CPCsoilmoist_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(CPCsoilmoist_YYYYMMDD_Of_RefArray, CPCsoilmoist_RefArray, Training_BeginDateVecList, Training_EndDateVecList)

#USDM_YYYYMMDD_Of_TimeSlicedArray, USDM_TimeSlicedArray = TimeSlice_YYYYMMDDAndRefArray(USDM_YYYYMMDD_Of_InfoArray, USDM_InfoArray, Training_BeginDateVecList, Training_EndDateVecList)

MonthlyList_PMDI_YYYYMMDD_Of_PrcntlArray, MonthlyList_PMDI_PrcntlArray = MonthlyList_YYYYMMDDAndArray(PMDI_YYYYMMDD_Of_PrcntlArray, PMDI_PrcntlArray)
MonthlyList_PHDI_YYYYMMDD_Of_PrcntlArray, MonthlyList_PHDI_PrcntlArray = MonthlyList_YYYYMMDDAndArray(PHDI_YYYYMMDD_Of_PrcntlArray, PHDI_PrcntlArray)
#MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn1month_PrcntlArray = MonthlyList_YYYYMMDDAndArray(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn1month_PrcntlArray)
#MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn3month_PrcntlArray = MonthlyList_YYYYMMDDAndArray(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn3month_PrcntlArray)
#MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn6month_PrcntlArray = MonthlyList_YYYYMMDDAndArray(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn6month_PrcntlArray)
#MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn12month_PrcntlArray = MonthlyList_YYYYMMDDAndArray(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn12month_PrcntlArray)
#MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn24month_PrcntlArray = MonthlyList_YYYYMMDDAndArray(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn24month_PrcntlArray)
#MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn60month_PrcntlArray = MonthlyList_YYYYMMDDAndArray(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn60month_PrcntlArray)
#MonthlyList_CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, MonthlyList_CPCsoilmoist_PrcntlArray = MonthlyList_YYYYMMDDAndArray(CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, CPCsoilmoist_PrcntlArray)

ZIndex_PrcntlArray = LoopPercentileCalcOverSpatialUnits(ZIndex_RefArray, ZIndex_PrcntlArray)
ZIndex60month_PrcntlArray = LoopPercentileCalcOverSpatialUnits(ZIndex60month_RefArray, ZIndex60month_PrcntlArray)

MonthlyList_PMDI_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_PMDI_RefArray, MonthlyList_PMDI_PrcntlArray)
MonthlyList_PHDI_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_PHDI_RefArray, MonthlyList_PHDI_PrcntlArray)
#MonthlyList_Pcpn1month_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_Pcpn1month_RefArray, MonthlyList_Pcpn1month_PrcntlArray)
#MonthlyList_Pcpn3month_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_Pcpn3month_RefArray, MonthlyList_Pcpn3month_PrcntlArray)
#MonthlyList_Pcpn6month_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_Pcpn6month_RefArray, MonthlyList_Pcpn6month_PrcntlArray)
#MonthlyList_Pcpn12month_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_Pcpn12month_RefArray, MonthlyList_Pcpn12month_PrcntlArray)
#MonthlyList_Pcpn24month_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_Pcpn24month_RefArray, MonthlyList_Pcpn24month_PrcntlArray)
#MonthlyList_Pcpn60month_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_Pcpn60month_RefArray, MonthlyList_Pcpn60month_PrcntlArray)
#MonthlyList_CPCsoilmoist_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_CPCsoilmoist_RefArray, MonthlyList_CPCsoilmoist_PrcntlArray)

PMDI_PrcntlArray = ReAssembleArraysFromMonthlyList(PMDI_YYYYMMDD_Of_PrcntlArray, PMDI_PrcntlArray, MonthlyList_PMDI_YYYYMMDD_Of_PrcntlArray, MonthlyList_PMDI_PrcntlArray)
PHDI_PrcntlArray = ReAssembleArraysFromMonthlyList(PHDI_YYYYMMDD_Of_PrcntlArray, PHDI_PrcntlArray, MonthlyList_PHDI_YYYYMMDD_Of_PrcntlArray, MonthlyList_PHDI_PrcntlArray)
#Pcpn1month_PrcntlArray = ReAssembleArraysFromMonthlyList(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn1month_PrcntlArray, MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn1month_PrcntlArray)
#Pcpn3month_PrcntlArray = ReAssembleArraysFromMonthlyList(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn3month_PrcntlArray, MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn3month_PrcntlArray)
#Pcpn6month_PrcntlArray = ReAssembleArraysFromMonthlyList(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn6month_PrcntlArray, MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn6month_PrcntlArray)
#Pcpn12month_PrcntlArray = ReAssembleArraysFromMonthlyList(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn12month_PrcntlArray, MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn12month_PrcntlArray)
#Pcpn24month_PrcntlArray = ReAssembleArraysFromMonthlyList(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn24month_PrcntlArray, MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn24month_PrcntlArray)
#Pcpn60month_PrcntlArray = ReAssembleArraysFromMonthlyList(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn60month_PrcntlArray, MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn60month_PrcntlArray)
#CPCsoilmoist_PrcntlArray = ReAssembleArraysFromMonthlyList(CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, CPCsoilmoist_PrcntlArray, MonthlyList_CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, MonthlyList_CPCsoilmoist_PrcntlArray)

print('Training: NumDates = ', ZIndex_PrcntlArray.shape[0], ', NumSpatialUnits = ',ZIndex_PrcntlArray.shape[1])
PrintInfoAboutArray(ZIndex_PrcntlArray, 'ZIndex_PrcntlArray')
PrintInfoAboutArray(ZIndex60month_PrcntlArray, 'ZIndex60month_PrcntlArray')
PrintInfoAboutArray(PMDI_PrcntlArray, 'PMDI_PrcntlArray')
PrintInfoAboutArray(PHDI_PrcntlArray, 'PHDI_PrcntlArray')
#PrintInfoAboutArray(Pcpn1month_PrcntlArray, 'Pcpn1month_PrcntlArray')
#PrintInfoAboutArray(Pcpn3month_PrcntlArray, 'Pcpn3month_PrcntlArray')
#PrintInfoAboutArray(Pcpn6month_PrcntlArray, 'Pcpn6month_PrcntlArray')
#PrintInfoAboutArray(Pcpn12month_PrcntlArray, 'Pcpn12month_PrcntlArray')
#PrintInfoAboutArray(Pcpn24month_PrcntlArray, 'Pcpn24month_PrcntlArray')
#PrintInfoAboutArray(Pcpn60month_PrcntlArray, 'Pcpn60month_PrcntlArray')
#PrintInfoAboutArray(CPCsoilmoist_PrcntlArray, 'CPCsoilmoist_PrcntlArray')

#PrintInfoAboutArray(USDM_TimeSlicedArray, 'USDM_TimeSlicedArray')

np.savez_compressed(TrainDataFilename, YYYYMMDD_Of_Array = ZIndex_YYYYMMDD_Of_PrcntlArray, ZIndex_PrcntlArray = ZIndex_PrcntlArray, ZIndex60month_PrcntlArray = ZIndex60month_PrcntlArray, PMDI_PrcntlArray = PMDI_PrcntlArray, PHDI_PrcntlArray = PHDI_PrcntlArray)#, Pcpn1month_PrcntlArray = Pcpn1month_PrcntlArray, Pcpn3month_PrcntlArray = Pcpn3month_PrcntlArray, Pcpn6month_PrcntlArray = Pcpn6month_PrcntlArray, Pcpn12month_PrcntlArray = Pcpn12month_PrcntlArray, Pcpn24month_PrcntlArray = Pcpn24month_PrcntlArray, Pcpn60month_PrcntlArray = Pcpn60month_PrcntlArray, CPCsoilmoist_PrcntlArray = CPCsoilmoist_PrcntlArray)#, USDM_TimeSlicedArray = USDM_TimeSlicedArray) 

#END section for training

#BEGIN section for evaluation

ZIndex_YYYYMMDD_Of_PrcntlArray, ZIndex_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(ZIndex_YYYYMMDD_Of_RefArray, ZIndex_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
ZIndex_YYYYMMDD_Of_PrcntlArray, ZIndex60month_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(ZIndex_YYYYMMDD_Of_RefArray, ZIndex60month_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
PMDI_YYYYMMDD_Of_PrcntlArray, PMDI_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(PMDI_YYYYMMDD_Of_RefArray, PMDI_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
PHDI_YYYYMMDD_Of_PrcntlArray, PHDI_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(PHDI_YYYYMMDD_Of_RefArray, PHDI_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
#Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn1month_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(Pcpn_YYYYMMDD_Of_RefArray, Pcpn1month_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
#Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn3month_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(Pcpn_YYYYMMDD_Of_RefArray, Pcpn3month_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
#Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn6month_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(Pcpn_YYYYMMDD_Of_RefArray, Pcpn6month_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
#Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn12month_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(Pcpn_YYYYMMDD_Of_RefArray, Pcpn12month_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
#Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn24month_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(Pcpn_YYYYMMDD_Of_RefArray, Pcpn24month_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
#Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn60month_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(Pcpn_YYYYMMDD_Of_RefArray, Pcpn60month_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
#CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, CPCsoilmoist_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(CPCsoilmoist_YYYYMMDD_Of_RefArray, CPCsoilmoist_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)

#USDM_YYYYMMDD_Of_TimeSlicedArray, USDM_TimeSlicedArray = TimeSlice_YYYYMMDDAndRefArray(USDM_YYYYMMDD_Of_InfoArray, USDM_InfoArray, Eval_BeginDateVecList, Eval_EndDateVecList)

MonthlyList_PMDI_YYYYMMDD_Of_PrcntlArray, MonthlyList_PMDI_PrcntlArray = MonthlyList_YYYYMMDDAndArray(PMDI_YYYYMMDD_Of_PrcntlArray, PMDI_PrcntlArray)
MonthlyList_PHDI_YYYYMMDD_Of_PrcntlArray, MonthlyList_PHDI_PrcntlArray = MonthlyList_YYYYMMDDAndArray(PHDI_YYYYMMDD_Of_PrcntlArray, PHDI_PrcntlArray)
#MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn1month_PrcntlArray = MonthlyList_YYYYMMDDAndArray(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn1month_PrcntlArray)
#MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn3month_PrcntlArray = MonthlyList_YYYYMMDDAndArray(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn3month_PrcntlArray)
#MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn6month_PrcntlArray = MonthlyList_YYYYMMDDAndArray(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn6month_PrcntlArray)
#MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn12month_PrcntlArray = MonthlyList_YYYYMMDDAndArray(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn12month_PrcntlArray)
#MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn24month_PrcntlArray = MonthlyList_YYYYMMDDAndArray(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn24month_PrcntlArray)
#MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn60month_PrcntlArray = MonthlyList_YYYYMMDDAndArray(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn60month_PrcntlArray)
#MonthlyList_CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, MonthlyList_CPCsoilmoist_PrcntlArray = MonthlyList_YYYYMMDDAndArray(CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, CPCsoilmoist_PrcntlArray)

ZIndex_PrcntlArray = LoopPercentileCalcOverSpatialUnits(ZIndex_RefArray, ZIndex_PrcntlArray)
ZIndex60month_PrcntlArray = LoopPercentileCalcOverSpatialUnits(ZIndex60month_RefArray, ZIndex60month_PrcntlArray)

MonthlyList_PMDI_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_PMDI_RefArray, MonthlyList_PMDI_PrcntlArray)
MonthlyList_PHDI_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_PHDI_RefArray, MonthlyList_PHDI_PrcntlArray)
#MonthlyList_Pcpn1month_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_Pcpn1month_RefArray, MonthlyList_Pcpn1month_PrcntlArray)
#MonthlyList_Pcpn3month_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_Pcpn3month_RefArray, MonthlyList_Pcpn3month_PrcntlArray)
#MonthlyList_Pcpn6month_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_Pcpn6month_RefArray, MonthlyList_Pcpn6month_PrcntlArray)
#MonthlyList_Pcpn12month_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_Pcpn12month_RefArray, MonthlyList_Pcpn12month_PrcntlArray)
#MonthlyList_Pcpn24month_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_Pcpn24month_RefArray, MonthlyList_Pcpn24month_PrcntlArray)
#MonthlyList_Pcpn60month_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_Pcpn60month_RefArray, MonthlyList_Pcpn60month_PrcntlArray)
#MonthlyList_CPCsoilmoist_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_CPCsoilmoist_RefArray, MonthlyList_CPCsoilmoist_PrcntlArray)

PMDI_PrcntlArray = ReAssembleArraysFromMonthlyList(PMDI_YYYYMMDD_Of_PrcntlArray, PMDI_PrcntlArray, MonthlyList_PMDI_YYYYMMDD_Of_PrcntlArray, MonthlyList_PMDI_PrcntlArray)
PHDI_PrcntlArray = ReAssembleArraysFromMonthlyList(PHDI_YYYYMMDD_Of_PrcntlArray, PHDI_PrcntlArray, MonthlyList_PHDI_YYYYMMDD_Of_PrcntlArray, MonthlyList_PHDI_PrcntlArray)
#Pcpn1month_PrcntlArray = ReAssembleArraysFromMonthlyList(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn1month_PrcntlArray, MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn1month_PrcntlArray)
#Pcpn3month_PrcntlArray = ReAssembleArraysFromMonthlyList(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn3month_PrcntlArray, MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn3month_PrcntlArray)
#Pcpn6month_PrcntlArray = ReAssembleArraysFromMonthlyList(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn6month_PrcntlArray, MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn6month_PrcntlArray)
#Pcpn12month_PrcntlArray = ReAssembleArraysFromMonthlyList(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn12month_PrcntlArray, MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn12month_PrcntlArray)
#Pcpn24month_PrcntlArray = ReAssembleArraysFromMonthlyList(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn24month_PrcntlArray, MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn24month_PrcntlArray)
#Pcpn60month_PrcntlArray = ReAssembleArraysFromMonthlyList(Pcpn_YYYYMMDD_Of_PrcntlArray, Pcpn60month_PrcntlArray, MonthlyList_Pcpn_YYYYMMDD_Of_PrcntlArray, MonthlyList_Pcpn60month_PrcntlArray)
#CPCsoilmoist_PrcntlArray = ReAssembleArraysFromMonthlyList(CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, CPCsoilmoist_PrcntlArray, MonthlyList_CPCsoilmoist_YYYYMMDD_Of_PrcntlArray, MonthlyList_CPCsoilmoist_PrcntlArray)

Dev_ZIndex_YYYYMMDD_Of_PrcntlArray = ZIndex_YYYYMMDD_Of_PrcntlArray[::2]
Dev_ZIndex_PrcntlArray = ZIndex_PrcntlArray[::2]
Dev_ZIndex60month_PrcntlArray = ZIndex60month_PrcntlArray[::2]
Dev_PMDI_PrcntlArray = PMDI_PrcntlArray[::2]
Dev_PHDI_PrcntlArray = PHDI_PrcntlArray[::2]
#Dev_Pcpn1month_PrcntlArray = Pcpn1month_PrcntlArray[::2]
#Dev_Pcpn3month_PrcntlArray = Pcpn3month_PrcntlArray[::2]
#Dev_Pcpn6month_PrcntlArray = Pcpn6month_PrcntlArray[::2]
#Dev_Pcpn12month_PrcntlArray = Pcpn12month_PrcntlArray[::2]
#Dev_Pcpn24month_PrcntlArray = Pcpn24month_PrcntlArray[::2]
#Dev_Pcpn60month_PrcntlArray = Pcpn60month_PrcntlArray[::2]
#Dev_CPCsoilmoist_PrcntlArray = CPCsoilmoist_PrcntlArray[::2]

#Dev_USDM_TimeSlicedArray = USDM_TimeSlicedArray[::2]

Test_ZIndex_YYYYMMDD_Of_PrcntlArray = ZIndex_YYYYMMDD_Of_PrcntlArray[1::2]
Test_ZIndex_PrcntlArray = ZIndex_PrcntlArray[1::2]
Test_ZIndex60month_PrcntlArray = ZIndex60month_PrcntlArray[1::2]
Test_PMDI_PrcntlArray = PMDI_PrcntlArray[1::2]
Test_PHDI_PrcntlArray = PHDI_PrcntlArray[1::2]
#Test_Pcpn1month_PrcntlArray = Pcpn1month_PrcntlArray[1::2]
#Test_Pcpn3month_PrcntlArray = Pcpn3month_PrcntlArray[1::2]
#Test_Pcpn6month_PrcntlArray = Pcpn6month_PrcntlArray[1::2]
#Test_Pcpn12month_PrcntlArray = Pcpn12month_PrcntlArray[1::2]
#Test_Pcpn24month_PrcntlArray = Pcpn24month_PrcntlArray[1::2]
#Test_Pcpn60month_PrcntlArray = Pcpn60month_PrcntlArray[1::2]
#Test_CPCsoilmoist_PrcntlArray = CPCsoilmoist_PrcntlArray[1::2]

#Test_USDM_TimeSlicedArray = USDM_TimeSlicedArray[1::2]

print('Evaluation: Dev NumDates = ', Dev_ZIndex_PrcntlArray.shape[0], ', NumSpatialUnits = ', Dev_ZIndex_PrcntlArray.shape[1])
PrintInfoAboutArray(Dev_ZIndex_PrcntlArray, 'Dev_ZIndex_PrcntlArray')
PrintInfoAboutArray(Dev_ZIndex60month_PrcntlArray, 'Dev_ZIndex60month_PrcntlArray')
PrintInfoAboutArray(Dev_PMDI_PrcntlArray, 'Dev_PMDI_PrcntlArray')
PrintInfoAboutArray(Dev_PHDI_PrcntlArray, 'Dev_PHDI_PrcntlArray')
#PrintInfoAboutArray(Dev_Pcpn1month_PrcntlArray, 'Dev_Pcpn1month_PrcntlArray')
#PrintInfoAboutArray(Dev_Pcpn3month_PrcntlArray, 'Dev_Pcpn3month_PrcntlArray')
#PrintInfoAboutArray(Dev_Pcpn6month_PrcntlArray, 'Dev_Pcpn6month_PrcntlArray')
#PrintInfoAboutArray(Dev_Pcpn12month_PrcntlArray, 'Dev_Pcpn12month_PrcntlArray')
#PrintInfoAboutArray(Dev_Pcpn24month_PrcntlArray, 'Dev_Pcpn24month_PrcntlArray')
#PrintInfoAboutArray(Dev_Pcpn60month_PrcntlArray, 'Dev_Pcpn60month_PrcntlArray')
#PrintInfoAboutArray(Dev_CPCsoilmoist_PrcntlArray, 'Dev_CPCsoilmoist_PrcntlArray')

#PrintInfoAboutArray(Dev_USDM_TimeSlicedArray, 'Dev_USDM_TimeSlicedArray')

print('Evaluation: Test NumDates = ', Test_ZIndex_PrcntlArray.shape[0], ', NumSpatialUnits = ', Test_ZIndex_PrcntlArray.shape[1])
PrintInfoAboutArray(Test_ZIndex_PrcntlArray, 'Test_ZIndex_PrcntlArray')
PrintInfoAboutArray(Test_ZIndex60month_PrcntlArray, 'Test_ZIndex60month_PrcntlArray')
PrintInfoAboutArray(Test_PMDI_PrcntlArray, 'Test_PMDI_PrcntlArray')
PrintInfoAboutArray(Test_PHDI_PrcntlArray, 'Test_PHDI_PrcntlArray')
#PrintInfoAboutArray(Test_Pcpn1month_PrcntlArray, 'Test_Pcpn1month_PrcntlArray')
#PrintInfoAboutArray(Test_Pcpn3month_PrcntlArray, 'Test_Pcpn3month_PrcntlArray')
#PrintInfoAboutArray(Test_Pcpn6month_PrcntlArray, 'Test_Pcpn6month_PrcntlArray')
#PrintInfoAboutArray(Test_Pcpn12month_PrcntlArray, 'Test_Pcpn12month_PrcntlArray')
#PrintInfoAboutArray(Test_Pcpn24month_PrcntlArray, 'Test_Pcpn24month_PrcntlArray')
#PrintInfoAboutArray(Test_Pcpn60month_PrcntlArray, 'Test_Pcpn60month_PrcntlArray')
#PrintInfoAboutArray(Test_CPCsoilmoist_PrcntlArray, 'Test_CPCsoilmoist_PrcntlArray')

#PrintInfoAboutArray(Test_USDM_TimeSlicedArray, 'Test_USDM_TimeSlicedArray')

np.savez_compressed(DevDataFilename, YYYYMMDD_Of_Array = Dev_ZIndex_YYYYMMDD_Of_PrcntlArray, ZIndex_PrcntlArray = Dev_ZIndex_PrcntlArray, ZIndex60month_PrcntlArray = Dev_ZIndex60month_PrcntlArray, PMDI_PrcntlArray = Dev_PMDI_PrcntlArray, PHDI_PrcntlArray = Dev_PHDI_PrcntlArray)#, Pcpn1month_PrcntlArray = Dev_Pcpn1month_PrcntlArray, Pcpn3month_PrcntlArray = Dev_Pcpn3month_PrcntlArray, Pcpn6month_PrcntlArray = Dev_Pcpn6month_PrcntlArray, Pcpn12month_PrcntlArray = Dev_Pcpn12month_PrcntlArray, Pcpn24month_PrcntlArray = Dev_Pcpn24month_PrcntlArray, Pcpn60month_PrcntlArray = Dev_Pcpn60month_PrcntlArray, CPCsoilmoist_PrcntlArray = Dev_CPCsoilmoist_PrcntlArray, USDM_TimeSlicedArray = Dev_USDM_TimeSlicedArray) 

np.savez_compressed(TestDataFilename, YYYYMMDD_Of_Array = Test_ZIndex_YYYYMMDD_Of_PrcntlArray, ZIndex_PrcntlArray = Test_ZIndex_PrcntlArray, ZIndex60month_PrcntlArray = Test_ZIndex60month_PrcntlArray, PMDI_PrcntlArray = Test_PMDI_PrcntlArray, PHDI_PrcntlArray = Test_PHDI_PrcntlArray)#, Pcpn1month_PrcntlArray = Test_Pcpn1month_PrcntlArray, Pcpn3month_PrcntlArray = Test_Pcpn3month_PrcntlArray, Pcpn6month_PrcntlArray = Test_Pcpn6month_PrcntlArray, Pcpn12month_PrcntlArray = Test_Pcpn12month_PrcntlArray, Pcpn24month_PrcntlArray = Test_Pcpn24month_PrcntlArray, Pcpn60month_PrcntlArray = Test_Pcpn60month_PrcntlArray, CPCsoilmoist_PrcntlArray = Test_CPCsoilmoist_PrcntlArray, USDM_TimeSlicedArray = Test_USDM_TimeSlicedArray) 

#END section for evaluation

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")



