from __future__ import division
from datetime import date, datetime, timedelta
import sys
import numpy as np
from scipy.stats import rankdata

def PrintInfoAboutArray(ThisArray, VariabNameStr):
    print('')
    print(VariabNameStr,".shape is ",ThisArray.shape)
    print(VariabNameStr,".dtype is ",ThisArray.dtype)
    print(VariabNameStr," is ",ThisArray)
    print("np.amin(np.isnan(",VariabNameStr,").sum(axis=0)) is ",np.amin(np.isnan(ThisArray).sum(axis=0)))
    print("np.amax(np.isnan(",VariabNameStr,").sum(axis=0)) is ",np.amax(np.isnan(ThisArray).sum(axis=0)))
    print("np.amin(np.isnan(",VariabNameStr,").sum(axis=1)) is ",np.amin(np.isnan(ThisArray).sum(axis=1)))
    print("np.amax(np.isnan(",VariabNameStr,").sum(axis=1)) is ",np.amax(np.isnan(ThisArray).sum(axis=1)))
    print("np.isnan(np.nansum(ThisArray, axis = 0)).sum() is ",np.isnan(np.nansum(ThisArray, axis = 0)).sum())
    print("np.isnan(np.nansum(ThisArray, axis = 1)).sum() is ",np.isnan(np.nansum(ThisArray, axis = 1)).sum())
    print('overall min is ',np.nanmin(ThisArray),', overall max is ',np.nanmax(ThisArray))
    print('')
    return

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
#end of def LoopPercentileCalcOverSpatialUnits(RefArray, PrcntlArray)

def LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_RefArray, MonthlyList_PrcntlArray):
  for WhichMonth in range(1,12+1):
    RefArray = MonthlyList_RefArray[WhichMonth-1]
    PrcntlArray = MonthlyList_PrcntlArray[WhichMonth-1]
    PrcntlArray = LoopPercentileCalcOverSpatialUnits(RefArray, PrcntlArray)
    MonthlyList_PrcntlArray[WhichMonth-1] = PrcntlArray
  #end of for WhichMonth in range(1,12+1):
  return MonthlyList_PrcntlArray
#end of def LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_RefArray, MonthlyList_PrcntlArray)

def CreateMonthlyLists_YYYYMMDDAndArray(YYYYMMDD_Of_Array, ThisArray):
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
#end of def CreateMonthlyLists_YYYYMMDDAndArray(YYYYMMDD_Of_Array, ThisArray)

def CreateYYYYMMDD_Of_Array_FromEndpointdates(BeginDate, EndDate):
  TotalNumDaysDiff = abs(EndDate-BeginDate).days
  TotalNumWeeksDiff = TotalNumDaysDiff//7
  HumanDatesList_Of_Array = []
  for NumWeeksDiff in range(0,TotalNumWeeksDiff+1):
    IntermediateDate = BeginDate + timedelta(weeks=NumWeeksDiff)
    HumanDatesList_Of_Array.append(10000*IntermediateDate.year + 100*IntermediateDate.month + IntermediateDate.day)
  YYYYMMDD_Of_Array = np.array(HumanDatesList_Of_Array, dtype = np.int32)
  YYYYMMDD_Of_Array = np.expand_dims(YYYYMMDD_Of_Array, axis=1)
  return YYYYMMDD_Of_Array
#end of def CreateYYYYMMDD_Of_Array_FromEndpointdates(BeginDate, EndDate)

def TimeSlice_YYYYMMDDAndRefArrays(YYYYMMDD_Of_RefArray, RefArray, BeginDateVecList, EndDateVecList):
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
    YYYYMMDD_Of_PrcntlArray = CreateYYYYMMDD_Of_Array_FromEndpointdates(BeginDate, EndDate)
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
#end of def TimeSlice_YYYYMMDDAndRefArrays(YYYYMMDD_Of_RefArray, RefArray, BeginDateVecList, EndDateVecList)

def ReAssembleArraysFromMonthlyList(YYYYMMDD_Of_PrcntlArray, PrcntlArray, MonthlyList_YYYYMMDD_Of_PrcntlArray, MonthlyList_PrcntlArray):
  YYYYMMDD_Of_PrcntlArray_1d = np.squeeze(YYYYMMDD_Of_PrcntlArray, axis = 1)
  for WhichMonth in range(1,12+1):
    YYYYMMDD_Of_PrcntlArray_ThisMonth_1d = np.squeeze(MonthlyList_YYYYMMDD_Of_PrcntlArray[WhichMonth-1], axis = 1)
    all_sorted = np.argsort(YYYYMMDD_Of_PrcntlArray_1d)
    ThisMonth_pos = np.searchsorted(YYYYMMDD_Of_PrcntlArray_1d[all_sorted], YYYYMMDD_Of_PrcntlArray_ThisMonth_1d)
    indices = all_sorted[ThisMonth_pos]
    PrcntlArray[indices, :] = MonthlyList_PrcntlArray[WhichMonth-1]
  #end of for WhichMonth in range(1,12+1)
  return PrcntlArray
#end of def ReAssembleArraysFromMonthlyList(YYYYMMDD_Of_PrcntlArray, PrcntlArray, MonthlyList_YYYYMMDD_Of_PrcntlArray, MonthlyList_PrcntlArray)

def PrepTrainPortion_ClimDivs_MonthlyPercBased(YYYYMMDD_Of_RefArray, RefArray, Training_BeginDateVecList, Training_EndDateVecList, MonthlyList_RefArray):

  YYYYMMDD_Of_PrcntlArray, PrcntlArray = TimeSlice_YYYYMMDDAndRefArrays(YYYYMMDD_Of_RefArray, RefArray, Training_BeginDateVecList, Training_EndDateVecList)

  MonthlyList_YYYYMMDD_Of_PrcntlArray, MonthlyList_PrcntlArray = CreateMonthlyLists_YYYYMMDDAndArray(YYYYMMDD_Of_PrcntlArray, PrcntlArray)

  MonthlyList_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_RefArray, MonthlyList_PrcntlArray)

  PrcntlArray = ReAssembleArraysFromMonthlyList(YYYYMMDD_Of_PrcntlArray, PrcntlArray, MonthlyList_YYYYMMDD_Of_PrcntlArray, MonthlyList_PrcntlArray)

  return YYYYMMDD_Of_PrcntlArray, PrcntlArray


def PrepTrainPortion_ClimDivs_OverallPercBased(YYYYMMDD_Of_RefArray, RefArray, Training_BeginDateVecList, Training_EndDateVecList):

  YYYYMMDD_Of_PrcntlArray, PrcntlArray = TimeSlice_YYYYMMDDAndRefArrays(YYYYMMDD_Of_RefArray, RefArray, Training_BeginDateVecList, Training_EndDateVecList)

  PrcntlArray = LoopPercentileCalcOverSpatialUnits(RefArray, PrcntlArray)

  return YYYYMMDD_Of_PrcntlArray, PrcntlArray