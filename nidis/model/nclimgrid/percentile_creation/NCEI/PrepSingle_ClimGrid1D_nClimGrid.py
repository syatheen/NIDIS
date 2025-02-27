#!/usr/bin/env python
# Coded by Soni Yatheendradas
#         on Dec 23, 2022
from __future__ import division
import sys
#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        WhichVariable
#ArgNum   1
 
# BEGIN code arguments / editable section

SingleUnified_BeginDateVecList = [2006, 1, 3] # Beginning single-unified year, month, day of month, this is also a Tuesday
#SingleUnified_EndDateVecList = [2021, 7, 27] # Ending single-unified year, month, day of month, this is also a Tuesday
SingleUnified_EndDateVecList = [2019, 12, 31] # Ending single-unified year, month, day of month, this is also a Tuesday

WhichVariable = sys.argv[1] # Choices are
       # 'spei-gamma-01', 'spei-gamma-02', 'spei-gamma-03', 'spei-gamma-06',
       # 'spei-gamma-09', 'spei-gamma-12', 'spei-gamma-24', 'spei-gamma-36',
       # 'spei-gamma-48', 'spei-gamma-60', 'spei-gamma-72',
       # 'spei-pearson-01', 'spei-pearson-02', 'spei-pearson-03', 'spei-pearson-06',
       # 'spei-pearson-09', 'spei-pearson-12', 'spei-pearson-24', 'spei-pearson-36',
       # 'spei-pearson-48', 'spei-pearson-60', 'spei-pearson-72',
       # 'spi-gamma-01', 'spi-gamma-02', 'spi-gamma-03', 'spi-gamma-06',
       # 'spi-gamma-09', 'spi-gamma-12', 'spi-gamma-24', 'spi-gamma-36',
       # 'spi-gamma-48', 'spi-gamma-60', 'spi-gamma-72',
       # 'spi-pearson-01', 'spi-pearson-02', 'spi-pearson-03', 'spi-pearson-06',
       # 'spi-pearson-09', 'spi-pearson-12', 'spi-pearson-24', 'spi-pearson-36',
       # 'spi-pearson-48', 'spi-pearson-60', 'spi-pearson-72',
       # 'pet-01', 'pet-02', 'pet-03', 'pet-06',
       # 'pet-09', 'pet-12', 'pet-24', 'pet-36',
       # 'pet-48', 'pet-60', 'pet-72',
       # 'prcp-01', 'prcp-02', 'prcp-03', 'prcp-06',
       # 'prcp-09', 'prcp-12', 'prcp-24', 'prcp-36',
       # 'prcp-48', 'prcp-60', 'prcp-72',
       # 'tavg-01', 'tavg-02', 'tavg-03', 'tavg-06',
       # 'tavg-09', 'tavg-12', 'tavg-24', 'tavg-36',
       # 'tavg-48', 'tavg-60', 'tavg-72',
       # 'tmax-01', 'tmax-02', 'tmax-03', 'tmax-06',
       # 'tmax-09', 'tmax-12', 'tmax-24', 'tmax-36',
       # 'tmax-48', 'tmax-60', 'tmax-72'

if WhichVariable[-2:] == '01':
  nClimGrid_Ref_BeginDateVecList = [1895, 2, 5]  # nClimGrid_01 beginning year, month, day of month, this is also a Tuesday
elif WhichVariable[-2:] == '02':
  nClimGrid_Ref_BeginDateVecList = [1895, 3, 5]  # nClimGrid_02 beginning year, month, day of month, this is also a Tuesday
elif WhichVariable[-2:] == '03':
  nClimGrid_Ref_BeginDateVecList = [1895, 4, 2]  # nClimGrid_03 beginning year, month, day of month, this is also a Tuesday
elif WhichVariable[-2:] == '06':
  nClimGrid_Ref_BeginDateVecList = [1895, 7, 2]  # nClimGrid_06 beginning year, month, day of month, this is also a Tuesday
elif WhichVariable[-2:] == '09':
  nClimGrid_Ref_BeginDateVecList = [1895, 10, 1]  # nClimGrid_09 beginning year, month, day of month, this is also a Tuesday
elif WhichVariable[-2:] == '12':
  nClimGrid_Ref_BeginDateVecList = [1895, 12, 31]  # nClimGrid_12 beginning year, month, day of month, this is also a Tuesday
elif WhichVariable[-2:] == '24':
  nClimGrid_Ref_BeginDateVecList = [1897, 1, 5]  # nClimGrid_24 beginning year, month, day of month, this is also a Tuesday
elif WhichVariable[-2:] == '36':
  nClimGrid_Ref_BeginDateVecList = [1898, 1, 4]  # nClimGrid_36 beginning year, month, day of month, this is also a Tuesday
elif WhichVariable[-2:] == '48':
  nClimGrid_Ref_BeginDateVecList = [1899, 1, 3]  # nClimGrid_48 beginning year, month, day of month, this is also a Tuesday
elif WhichVariable[-2:] == '60':
  nClimGrid_Ref_BeginDateVecList = [1900, 1, 2]  # nClimGrid_60 beginning year, month, day of month, this is also a Tuesday
elif WhichVariable[-2:] == '72':
  nClimGrid_Ref_BeginDateVecList = [1901, 1, 1]  # nClimGrid_72 beginning year, month, day of month, this is also a Tuesday

nClimGrid_Ref_EndDateVecList = [2021, 7, 27]  # nClimGrid ending year, month, day of month, this is also a Tuesday

Variable_RefFileName = '/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/RefArrays/ClimGrid1D_'+WhichVariable.replace("-", "_")+'_'+format(nClimGrid_Ref_BeginDateVecList[0],'04')+format(nClimGrid_Ref_BeginDateVecList[1],'02')+format(nClimGrid_Ref_BeginDateVecList[2],'02')+'To'+format(nClimGrid_Ref_EndDateVecList[0],'04')+format(nClimGrid_Ref_EndDateVecList[1],'02')+format(nClimGrid_Ref_EndDateVecList[2],'02')+'.npz'

SingleUnifiedDataFilename = 'PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_'+WhichVariable.replace("-", "_")+'_'+str(SingleUnified_BeginDateVecList[0])+format(SingleUnified_BeginDateVecList[1],'02')+format(SingleUnified_BeginDateVecList[2],'02')+'To'+str(SingleUnified_EndDateVecList[0])+format(SingleUnified_EndDateVecList[1],'02')+format(SingleUnified_EndDateVecList[2],'02')+'.npz'

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

Variable_RefObject = np.load(Variable_RefFileName)

Variable_YYYYMMDD_Of_RefArray = Variable_RefObject['Variable_YYYYMMDD_Of_RefArray']

Variable_RefArray = Variable_RefObject['Variable_RefArray']

del Variable_RefObject

EndIdx_Pre = np.where( Variable_YYYYMMDD_Of_RefArray == 10000 * SingleUnified_EndDateVecList[0] + 100 * SingleUnified_EndDateVecList[1] + SingleUnified_EndDateVecList[2] )[0][0]

Variable_YYYYMMDD_Of_RefArray = Variable_YYYYMMDD_Of_RefArray[:EndIdx_Pre+1]

Variable_RefArray = Variable_RefArray[:EndIdx_Pre+1]

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

if ( (WhichVariable[-2:] == '01') or
     (WhichVariable[-2:] == '02') or
     (WhichVariable[-2:] == '03') or
     (WhichVariable[-2:] == '06') or
     (WhichVariable[-2:] == '09') ):
  MonthlyList_Variable_YYYYMMDD_Of_RefArray, MonthlyList_Variable_RefArray = MonthlyList_YYYYMMDDAndArray(Variable_YYYYMMDD_Of_RefArray, Variable_RefArray)
  del MonthlyList_Variable_YYYYMMDD_Of_RefArray
#end of if ( (WhichVariable[-2:] == '01') or...

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

#BEGIN section for single-unified

Variable_YYYYMMDD_Of_PrcntlArray, Variable_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(Variable_YYYYMMDD_Of_RefArray, Variable_RefArray, SingleUnified_BeginDateVecList, SingleUnified_EndDateVecList)
del Variable_YYYYMMDD_Of_RefArray

if ( (WhichVariable[-2:] == '12') or
     (WhichVariable[-2:] == '24') or
     (WhichVariable[-2:] == '36') or
     (WhichVariable[-2:] == '48') or
     (WhichVariable[-2:] == '60') or
     (WhichVariable[-2:] == '72') ):

  Variable_PrcntlArray = LoopPercentileCalcOverSpatialUnits(Variable_RefArray, Variable_PrcntlArray)

#end of if ( (WhichVariable[-2:] == '12') or...
del Variable_RefArray

if ( (WhichVariable[-2:] == '01') or
     (WhichVariable[-2:] == '02') or
     (WhichVariable[-2:] == '03') or
     (WhichVariable[-2:] == '06') or
     (WhichVariable[-2:] == '09') ):

  MonthlyList_Variable_YYYYMMDD_Of_PrcntlArray, MonthlyList_Variable_PrcntlArray = MonthlyList_YYYYMMDDAndArray(Variable_YYYYMMDD_Of_PrcntlArray, Variable_PrcntlArray)

  MonthlyList_Variable_PrcntlArray = LoopPrcntlCalcOverMonthsNSpatialUnits(MonthlyList_Variable_RefArray, MonthlyList_Variable_PrcntlArray)
  del MonthlyList_Variable_RefArray

  Variable_PrcntlArray = ReAssembleArraysFromMonthlyList(Variable_YYYYMMDD_Of_PrcntlArray, Variable_PrcntlArray, MonthlyList_Variable_YYYYMMDD_Of_PrcntlArray, MonthlyList_Variable_PrcntlArray)
  del MonthlyList_Variable_YYYYMMDD_Of_PrcntlArray
  del MonthlyList_Variable_PrcntlArray

#end of if ( (WhichVariable[-2:] == '01') or...

print('Single-unified: NumDates = ', Variable_PrcntlArray.shape[0], ', NumSpatialUnits = ',Variable_PrcntlArray.shape[1])

print(WhichVariable+"_YYYYMMDD_Of_PrcntlArray.shape is ",Variable_YYYYMMDD_Of_PrcntlArray.shape)
print(WhichVariable+"_YYYYMMDD_Of_PrcntlArray is ",Variable_YYYYMMDD_Of_PrcntlArray)

PrintInfoAboutArray(Variable_PrcntlArray, WhichVariable+'_PrcntlArray')

np.savez_compressed(SingleUnifiedDataFilename, 
                    YYYYMMDD_Of_Array = Variable_YYYYMMDD_Of_PrcntlArray, 
                    Variable_PrcntlArray = Variable_PrcntlArray)
del Variable_YYYYMMDD_Of_PrcntlArray
del Variable_PrcntlArray 
#END section for training

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")



