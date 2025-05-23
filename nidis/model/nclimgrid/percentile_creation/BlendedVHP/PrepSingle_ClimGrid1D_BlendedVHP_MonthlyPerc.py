#!/usr/bin/env python
# Coded by Soni Yatheendradas
#         on Jul 13, 2023
from __future__ import division

# BEGIN code arguments / editable section

SingleUnified_BeginDateVecList = [2003, 9, 30]  # Beginning single-unified year, month, day of month, this is also a Tuesday
#SingleUnified_EndDateVecList = [2020, 12, 29]  # Ending single-unified year, month, day of month, this is also a Tuesday
SingleUnified_EndDateVecList = [2019, 12, 31]  # Ending single-unified year, month, day of month, this is also a Tuesday

BlendedVHP_SMN_RefFileName = 'RefArrays/ClimGrid1D_BlendedVHP_SMN_19810908To20210928.npz'
BlendedVHP_TCI_RefFileName = 'RefArrays/ClimGrid1D_BlendedVHP_TCI_19810908To20210928.npz'
BlendedVHP_VCI_RefFileName = 'RefArrays/ClimGrid1D_BlendedVHP_VCI_19810908To20210928.npz'
BlendedVHP_VHI_RefFileName = 'RefArrays/ClimGrid1D_BlendedVHP_VHI_19810908To20210928.npz'

SingleUnifiedDataFilename = 'PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_BlendedVHP_Corr2MonthlyPerc_' + str(SingleUnified_BeginDateVecList[0]) + format(SingleUnified_BeginDateVecList[1],'02') + format(SingleUnified_BeginDateVecList[2],'02') + 'To' + str(SingleUnified_EndDateVecList[0]) + format(SingleUnified_EndDateVecList[1],'02') + format(SingleUnified_EndDateVecList[2],'02') + '.npz'

# END code arguments / editable section

from datetime import date, datetime, timedelta
import sys
import numpy as np
from scipy.interpolate import interp1d
from scipy.stats import rankdata

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

BlendedVHP_SMN_RefObject = np.load(BlendedVHP_SMN_RefFileName)
BlendedVHP_TCI_RefObject = np.load(BlendedVHP_TCI_RefFileName)
BlendedVHP_VCI_RefObject = np.load(BlendedVHP_VCI_RefFileName)
BlendedVHP_VHI_RefObject = np.load(BlendedVHP_VHI_RefFileName)

BlendedVHP_YYYYMMDD_Of_RefArray = BlendedVHP_SMN_RefObject['BlendedVHP_YYYYMMDD_Of_RefArray']

BlendedVHP_SMN_RefArray = BlendedVHP_SMN_RefObject['BlendedVHP_RefArray']
BlendedVHP_TCI_RefArray = BlendedVHP_TCI_RefObject['BlendedVHP_RefArray']
BlendedVHP_VCI_RefArray = BlendedVHP_VCI_RefObject['BlendedVHP_RefArray']
BlendedVHP_VHI_RefArray = BlendedVHP_VHI_RefObject['BlendedVHP_RefArray']

del BlendedVHP_SMN_RefObject
del BlendedVHP_TCI_RefObject
del BlendedVHP_VCI_RefObject
del BlendedVHP_VHI_RefObject

EndIdx_Pre = np.where( BlendedVHP_YYYYMMDD_Of_RefArray == 10000 * SingleUnified_EndDateVecList[0] + 100 * SingleUnified_EndDateVecList[1] + SingleUnified_EndDateVecList[2] )[0][0]

BlendedVHP_YYYYMMDD_Of_RefArray = BlendedVHP_YYYYMMDD_Of_RefArray[:EndIdx_Pre+1]

BlendedVHP_SMN_RefArray = BlendedVHP_SMN_RefArray[:EndIdx_Pre+1]
BlendedVHP_TCI_RefArray = BlendedVHP_TCI_RefArray[:EndIdx_Pre+1]
BlendedVHP_VCI_RefArray = BlendedVHP_VCI_RefArray[:EndIdx_Pre+1]
BlendedVHP_VHI_RefArray = BlendedVHP_VHI_RefArray[:EndIdx_Pre+1]

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

MonthlyList_BlendedVHP_YYYYMMDD_Of_RefArray, MonthlyList_BlendedVHP_SMN_RefArray = CreateMonthlyLists_YYYYMMDDAndArray(BlendedVHP_YYYYMMDD_Of_RefArray, BlendedVHP_SMN_RefArray)
MonthlyList_BlendedVHP_YYYYMMDD_Of_RefArray, MonthlyList_BlendedVHP_TCI_RefArray = CreateMonthlyLists_YYYYMMDDAndArray(BlendedVHP_YYYYMMDD_Of_RefArray, BlendedVHP_TCI_RefArray)
MonthlyList_BlendedVHP_YYYYMMDD_Of_RefArray, MonthlyList_BlendedVHP_VCI_RefArray = CreateMonthlyLists_YYYYMMDDAndArray(BlendedVHP_YYYYMMDD_Of_RefArray, BlendedVHP_VCI_RefArray)
MonthlyList_BlendedVHP_YYYYMMDD_Of_RefArray, MonthlyList_BlendedVHP_VHI_RefArray = CreateMonthlyLists_YYYYMMDDAndArray(BlendedVHP_YYYYMMDD_Of_RefArray, BlendedVHP_VHI_RefArray)

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

def PrintInfoAboutArray(ThisArray, ThisArray_Str):
  print('')
  print(ThisArray_Str,".shape is ",ThisArray.shape)
  print(ThisArray_Str,".dtype is ",ThisArray.dtype)
  print(ThisArray_Str," is ",ThisArray)
  print("np.amin(np.isnan(",ThisArray_Str,").sum(axis=0)) is ",np.amin(np.isnan(ThisArray).sum(axis=0)))
  print("np.amax(np.isnan(",ThisArray_Str,").sum(axis=0)) is ",np.amax(np.isnan(ThisArray).sum(axis=0)))
  print("np.amin(np.isnan(",ThisArray_Str,").sum(axis=1)) is ",np.amin(np.isnan(ThisArray).sum(axis=1)))
  print("np.amax(np.isnan(",ThisArray_Str,").sum(axis=1)) is ",np.amax(np.isnan(ThisArray).sum(axis=1)))
  print("np.isnan(np.nansum(",ThisArray_Str,", axis = 0)).sum() is ",np.isnan(np.nansum(ThisArray, axis = 0)).sum())
  print("np.isnan(np.nansum(",ThisArray_Str,", axis = 1)).sum() is ",np.isnan(np.nansum(ThisArray, axis = 1)).sum())
  print('overall min is ',np.nanmin(ThisArray),', overall max is ',np.nanmax(ThisArray))
  print('')
#end of def PrintInfoAboutArray(ThisArray, ThisArray_Str):

#BEGIN section for SingleUnified

BlendedVHP_YYYYMMDD_Of_PrcntlArray, BlendedVHP_SMN_PrcntlArray = TimeSlice_YYYYMMDDAndRefArrays(BlendedVHP_YYYYMMDD_Of_RefArray, BlendedVHP_SMN_RefArray, SingleUnified_BeginDateVecList, SingleUnified_EndDateVecList)
BlendedVHP_YYYYMMDD_Of_PrcntlArray, BlendedVHP_TCI_PrcntlArray = TimeSlice_YYYYMMDDAndRefArrays(BlendedVHP_YYYYMMDD_Of_RefArray, BlendedVHP_TCI_RefArray, SingleUnified_BeginDateVecList, SingleUnified_EndDateVecList)
BlendedVHP_YYYYMMDD_Of_PrcntlArray, BlendedVHP_VCI_PrcntlArray = TimeSlice_YYYYMMDDAndRefArrays(BlendedVHP_YYYYMMDD_Of_RefArray, BlendedVHP_VCI_RefArray, SingleUnified_BeginDateVecList, SingleUnified_EndDateVecList)
BlendedVHP_YYYYMMDD_Of_PrcntlArray, BlendedVHP_VHI_PrcntlArray = TimeSlice_YYYYMMDDAndRefArrays(BlendedVHP_YYYYMMDD_Of_RefArray, BlendedVHP_VHI_RefArray, SingleUnified_BeginDateVecList, SingleUnified_EndDateVecList)

MonthlyList_BlendedVHP_YYYYMMDD_Of_PrcntlArray, MonthlyList_BlendedVHP_SMN_PrcntlArray = CreateMonthlyLists_YYYYMMDDAndArray(BlendedVHP_YYYYMMDD_Of_PrcntlArray, BlendedVHP_SMN_PrcntlArray)
MonthlyList_BlendedVHP_YYYYMMDD_Of_PrcntlArray, MonthlyList_BlendedVHP_TCI_PrcntlArray = CreateMonthlyLists_YYYYMMDDAndArray(BlendedVHP_YYYYMMDD_Of_PrcntlArray, BlendedVHP_TCI_PrcntlArray)
MonthlyList_BlendedVHP_YYYYMMDD_Of_PrcntlArray, MonthlyList_BlendedVHP_VCI_PrcntlArray = CreateMonthlyLists_YYYYMMDDAndArray(BlendedVHP_YYYYMMDD_Of_PrcntlArray, BlendedVHP_VCI_PrcntlArray)
MonthlyList_BlendedVHP_YYYYMMDD_Of_PrcntlArray, MonthlyList_BlendedVHP_VHI_PrcntlArray = CreateMonthlyLists_YYYYMMDDAndArray(BlendedVHP_YYYYMMDD_Of_PrcntlArray, BlendedVHP_VHI_PrcntlArray)

MonthlyList_BlendedVHP_SMN_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_BlendedVHP_SMN_RefArray, MonthlyList_BlendedVHP_SMN_PrcntlArray)
MonthlyList_BlendedVHP_TCI_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_BlendedVHP_TCI_RefArray, MonthlyList_BlendedVHP_TCI_PrcntlArray)
MonthlyList_BlendedVHP_VCI_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_BlendedVHP_VCI_RefArray, MonthlyList_BlendedVHP_VCI_PrcntlArray)
MonthlyList_BlendedVHP_VHI_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_BlendedVHP_VHI_RefArray, MonthlyList_BlendedVHP_VHI_PrcntlArray)

BlendedVHP_SMN_PrcntlArray = ReAssembleArraysFromMonthlyList(BlendedVHP_YYYYMMDD_Of_PrcntlArray, BlendedVHP_SMN_PrcntlArray, MonthlyList_BlendedVHP_YYYYMMDD_Of_PrcntlArray, MonthlyList_BlendedVHP_SMN_PrcntlArray)
BlendedVHP_TCI_PrcntlArray = ReAssembleArraysFromMonthlyList(BlendedVHP_YYYYMMDD_Of_PrcntlArray, BlendedVHP_TCI_PrcntlArray, MonthlyList_BlendedVHP_YYYYMMDD_Of_PrcntlArray, MonthlyList_BlendedVHP_TCI_PrcntlArray)
BlendedVHP_VCI_PrcntlArray = ReAssembleArraysFromMonthlyList(BlendedVHP_YYYYMMDD_Of_PrcntlArray, BlendedVHP_VCI_PrcntlArray, MonthlyList_BlendedVHP_YYYYMMDD_Of_PrcntlArray, MonthlyList_BlendedVHP_VCI_PrcntlArray)
BlendedVHP_VHI_PrcntlArray = ReAssembleArraysFromMonthlyList(BlendedVHP_YYYYMMDD_Of_PrcntlArray, BlendedVHP_VHI_PrcntlArray, MonthlyList_BlendedVHP_YYYYMMDD_Of_PrcntlArray, MonthlyList_BlendedVHP_VHI_PrcntlArray)

print('Single-unified: NumDates = ', BlendedVHP_SMN_PrcntlArray.shape[0], ', NumSpatialUnits = ',BlendedVHP_SMN_PrcntlArray.shape[1])

print("BlendedVHP_YYYYMMDD_Of_PrcntlArray.shape is ", BlendedVHP_YYYYMMDD_Of_PrcntlArray.shape)
print("BlendedVHP_YYYYMMDD_Of_PrcntlArray is ", BlendedVHP_YYYYMMDD_Of_PrcntlArray)

PrintInfoAboutArray(BlendedVHP_SMN_PrcntlArray, 'BlendedVHP_SMN_PrcntlArray')
PrintInfoAboutArray(BlendedVHP_TCI_PrcntlArray, 'BlendedVHP_TCI_PrcntlArray')
PrintInfoAboutArray(BlendedVHP_VCI_PrcntlArray, 'BlendedVHP_VCI_PrcntlArray')
PrintInfoAboutArray(BlendedVHP_VHI_PrcntlArray, 'BlendedVHP_VHI_PrcntlArray')

np.savez_compressed(SingleUnifiedDataFilename, 
                    YYYYMMDD_Of_Array = BlendedVHP_YYYYMMDD_Of_PrcntlArray, 
                    BlendedVHP_SMN_PrcntlArray = BlendedVHP_SMN_PrcntlArray,
                    BlendedVHP_TCI_PrcntlArray = BlendedVHP_TCI_PrcntlArray,
                    BlendedVHP_VCI_PrcntlArray = BlendedVHP_VCI_PrcntlArray,
                    BlendedVHP_VHI_PrcntlArray = BlendedVHP_VHI_PrcntlArray) 

del BlendedVHP_YYYYMMDD_Of_PrcntlArray
del BlendedVHP_SMN_PrcntlArray
del BlendedVHP_TCI_PrcntlArray
del BlendedVHP_VCI_PrcntlArray
del BlendedVHP_VHI_PrcntlArray

#END section for SingleUnified

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")



