#!/usr/bin/env python
# Coded by Soni Yatheendradas
#         on Apr 30, 2023
from __future__ import division
from datetime import date, datetime, timedelta
import sys
import numpy as np
from calendar import monthrange
import time

# BEGIN code arguments / editable section

GRACEDA_InfoFilesDir = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/GRACE/RefPctlArrsWeekly/'

GRACEDA_WhichVariable = 'sfsm_inst' # choices are gws_inst, rtzsm_inst and sfsm_inst

GRACEDA_InfoFiles_BeginYear = 2002 # Begins [2002, 4, 1]
GRACEDA_InfoFiles_EndYear = 2020 # Ends [2020, 10, 26] 

GRACEDA_Ref_BeginDateVecList = [2002, 4, 2]  # GRACEDA beginning year, month, day of month, this is also a Tuesday
GRACEDA_Ref_EndDateVecList = [2020, 10, 20]  # GRACEDA ending year, month, day of month, this is also a Tuesday

GRACEDA_RefFileName = 'RefArrays/ClimGrid1D_GRACEDA_'+GRACEDA_WhichVariable+'_'+format(GRACEDA_Ref_BeginDateVecList[0],'04')+format(GRACEDA_Ref_BeginDateVecList[1],'02')+format(GRACEDA_Ref_BeginDateVecList[2],'02')+'To'+format(GRACEDA_Ref_EndDateVecList[0],'04')+format(GRACEDA_Ref_EndDateVecList[1],'02')+format(GRACEDA_Ref_EndDateVecList[2],'02')+'.npz'

# END code arguments / editable section

start_time = time.time()

GRACEDA_Ref_BeginDate = date(GRACEDA_Ref_BeginDateVecList[0], GRACEDA_Ref_BeginDateVecList[1], GRACEDA_Ref_BeginDateVecList[2])
GRACEDA_Ref_EndDate = date(GRACEDA_Ref_EndDateVecList[0], GRACEDA_Ref_EndDateVecList[1], GRACEDA_Ref_EndDateVecList[2])

#BEGIN check whether the beginning and ending days are indeed Tuesdays
if GRACEDA_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for GRACEDA_Ref needs to be a Tuesday!!')
  sys.exit(0)
if GRACEDA_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for GRACEDA_Ref needs to be a Tuesday!!')
  sys.exit(0)
#END check whether the beginning and ending days are indeed Tuesdays

if GRACEDA_Ref_BeginDate > GRACEDA_Ref_EndDate:
  print('GRACEDA_Ref_BeginDate should not be later than GRACEDA_Ref_EndDate!!!')
  sys.exit(0)

#BEGIN section for time-interpolating info arrays to desired temporal resolution

for ThisYear in range(GRACEDA_InfoFiles_BeginYear, GRACEDA_InfoFiles_EndYear+1, 1):
  ThisYear_GRACEDA_Info = np.load(GRACEDA_InfoFilesDir+format(ThisYear, '04')+'_'+GRACEDA_WhichVariable+'_ClimGrid1D.npz')  
  ThisYear_GRACEDA_YYYYMMDD_Of_InfoArray = ThisYear_GRACEDA_Info['YYYYMMDD_Of_RefArrayForPrcntl']
  ThisYear_GRACEDA_InfoArray  = ThisYear_GRACEDA_Info['RefArrayForPrcntl']
  if ThisYear == GRACEDA_InfoFiles_BeginYear:
    GRACEDA_YYYYMMDD_Of_InfoArray = np.copy(ThisYear_GRACEDA_YYYYMMDD_Of_InfoArray)
    GRACEDA_InfoArray = np.copy(ThisYear_GRACEDA_InfoArray)
  else: 
    GRACEDA_YYYYMMDD_Of_InfoArray = np.concatenate((GRACEDA_YYYYMMDD_Of_InfoArray, ThisYear_GRACEDA_YYYYMMDD_Of_InfoArray), axis = 0)
    GRACEDA_InfoArray = np.concatenate((GRACEDA_InfoArray, ThisYear_GRACEDA_InfoArray), axis = 0)
  #end of if ThisYear == GRACEDA_InfoFiles_BeginYear
#end of for WhichYear in range(GRACEDA_InfoFiles_BeginYear, GRACEDA_InfoFiles_EndYear+1, 1)

def GetRealDatesListOfInfoArray(YYYYMMEtc_Of_InfoArray, NumDateElements, VariabNameForErrStr, WhereDayForNumDateElements2):
  # NumDateElements is 2 if YYYYMMEtc is in YYYYMM format, and 3 if in YYYYMMDD format
  # WhereDayForNumDateElements2 is 'begin' if value representative at month-beginning, 'mid' if value representative at mid-month, and 'end' if at end-month (e.g., accumulation)
  if NumDateElements == 3:
    Years_Of_InfoArray = YYYYMMEtc_Of_InfoArray // 10000
    Months_Of_InfoArray = (YYYYMMEtc_Of_InfoArray % 10000) // 100
    DaysOfMonth_Of_InfoArray = YYYYMMEtc_Of_InfoArray % 100
  elif NumDateElements == 2:
    Years_Of_InfoArray = YYYYMMEtc_Of_InfoArray // 100
    Months_Of_InfoArray = YYYYMMEtc_Of_InfoArray % 100
  else:
    print('NumDateElements should be 3 or 2 in GetRealDatesListOfInfoArray for '+VariabNameForErrStr+'!!!')
    sys.exit(0)
  RealDatesList_Of_InfoArray = []
  for ii in range(len(Years_Of_InfoArray)):
    if NumDateElements == 3:
      RealDatesList_Of_InfoArray.append(date(Years_Of_InfoArray[ii,0], Months_Of_InfoArray[ii,0], DaysOfMonth_Of_InfoArray[ii,0]))
    elif NumDateElements == 2:
      if WhereDayForNumDateElements2 == 'mid':
        RealDatesList_Of_InfoArray.append(date(Years_Of_InfoArray[ii,0], Months_Of_InfoArray[ii,0], 15)) # NOTE
      elif WhereDayForNumDateElements2 == 'end':
        RealDatesList_Of_InfoArray.append(date(Years_Of_InfoArray[ii,0], Months_Of_InfoArray[ii,0], (monthrange(Years_Of_InfoArray[ii,0], Months_Of_InfoArray[ii,0]))[1])) # NOTE
      elif WhereDayForNumDateElements2 == 'begin':
        RealDatesList_Of_InfoArray.append(date(Years_Of_InfoArray[ii,0], Months_Of_InfoArray[ii,0], 1))
      else:
        print('WhereDayForNumDateElements2 should be mid or end in GetRealDatesListOfInfoArray for '+VariabNameForErrStr+'!!!')
        sys.exit(0)
  return RealDatesList_Of_InfoArray
#end of def GetRealDatesListOfInfoArray(YYYYMMEtc_Of_InfoArray, NumDateElements, VariabNameForErrStr, WhereDayForNumDateElements2):

GRACEDA_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(GRACEDA_YYYYMMDD_Of_InfoArray, 3, 'GRACEDA', np.NaN)

#Begin calculating real dates list for reference arrays

def GetTimeInfoOfRefArray(Ref_BeginDate, Ref_EndDate):
  TotalNumDaysDiff = abs(Ref_EndDate-Ref_BeginDate).days
  TotalNumWeeksDiff = TotalNumDaysDiff//7
  RealDatesList_Of_RefArray = []
  HumanDatesList_Of_RefArray = []
  for NumWeeksDiff in range(0,TotalNumWeeksDiff+1):
    Ref_IntermediateDate = Ref_BeginDate + timedelta(weeks=NumWeeksDiff)
    RealDatesList_Of_RefArray.append(Ref_IntermediateDate)
    HumanDatesList_Of_RefArray.append(10000*Ref_IntermediateDate.year + 100*Ref_IntermediateDate.month + Ref_IntermediateDate.day)
  YYYYMMDD_Of_RefArray = np.array(HumanDatesList_Of_RefArray, dtype = np.int32)
  YYYYMMDD_Of_RefArray = np.expand_dims(YYYYMMDD_Of_RefArray, axis=1)
  return RealDatesList_Of_RefArray, YYYYMMDD_Of_RefArray
#end of def GetTimeInfoOfRefArray(Ref_BeginDate, Ref_EndDate):

GRACEDA_RealDatesList_Of_RefArray, GRACEDA_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(GRACEDA_Ref_BeginDate, GRACEDA_Ref_EndDate)

#End calculating real dates list for reference arrays

GRACEDA_RefArray = np.empty([ GRACEDA_YYYYMMDD_Of_RefArray.shape[0], GRACEDA_InfoArray.shape[1]])
GRACEDA_RefArray[:] = np.NaN

def TimeInterpolateValues(SourceDatesList, DestinationDatesList, SourceArray, DestinationArray):
  for DestinationDateIdx in range(len(DestinationDatesList)):
    ThisDestinationDate = DestinationDatesList[DestinationDateIdx] 
    if ThisDestinationDate in SourceDatesList:
      SourceIdxForThisDest = SourceDatesList.index(ThisDestinationDate) 
      DestinationArray[DestinationDateIdx,:] = SourceArray[SourceIdxForThisDest,:] 
    else:
      DaysDiffList = []
      for ThisSourceDate in SourceDatesList:
        DaysDiffList.append((ThisDestinationDate - ThisSourceDate).days)
      DaysDiffArray = np.array(DaysDiffList)
      SourceLowerIdxForThisDest = np.amax(np.where(DaysDiffArray > 0)) 
      SrcSlice = SourceArray[SourceLowerIdxForThisDest:SourceLowerIdxForThisDest+2,:]
      SrcSlice_isnan = np.isnan(SrcSlice)  
      SrcSlice_isnan_int = SrcSlice_isnan.astype(np.int32)
      SrcSlice_isnan_sum = np.sum(SrcSlice_isnan_int, axis = 0)
      Idxs_NotAllRowsNan = np.where(SrcSlice_isnan_sum < SrcSlice.shape[0])
      if Idxs_NotAllRowsNan[0].size > 0:
        SrcSlice_notnan = ~SrcSlice_isnan 
        SrcSlice_notnan_int = SrcSlice_notnan.astype(np.int32)
        Wt1 = float(-DaysDiffList[SourceLowerIdxForThisDest+1])
        Wt2 = float(DaysDiffList[SourceLowerIdxForThisDest])
        WtsMat = np.repeat(np.array([[Wt1],[Wt2]], dtype = SrcSlice.dtype), repeats = SrcSlice.shape[1], axis = 1) 
  
        Wtd_SrcSlice = np.multiply(SrcSlice, WtsMat)
        BooledWtsMat = np.multiply(WtsMat, SrcSlice_notnan_int)     
        Wtd_SrcSlice_NotAllRowsNan = Wtd_SrcSlice[:, Idxs_NotAllRowsNan[0]]
        BooledWtsMat_NotAllRowsNan = BooledWtsMat[:, Idxs_NotAllRowsNan[0]]
        Sum_Wtd_SrcSlice_NotAllRowsNan = np.nansum(Wtd_SrcSlice_NotAllRowsNan, axis = 0)
        Sum_Wts_NotAllRowsNan = np.nansum(BooledWtsMat_NotAllRowsNan, axis = 0)
        DestinationArray[DestinationDateIdx,Idxs_NotAllRowsNan[0]] = np.divide(Sum_Wtd_SrcSlice_NotAllRowsNan, 
                                                           Sum_Wts_NotAllRowsNan)
      #end of if Idxs_NotAllRowsNan[0].size > 0:
    #end of if ThisDestinationDate in SourceDatesList:
  #end of for DestinationDateIdx in range(len(DestinationDatesList)):
  return DestinationArray
#end of def TimeInterpolateValues(SourceDatesList, DestinationDatesList, SourceArray, DestinationArray):
 
GRACEDA_RefArray = TimeInterpolateValues(GRACEDA_RealDatesList_Of_InfoArray, GRACEDA_RealDatesList_Of_RefArray, GRACEDA_InfoArray, GRACEDA_RefArray)

print("--- %s seconds ---" % (time.time() - start_time))

np.savez_compressed(GRACEDA_RefFileName, GRACEDA_RefArray = GRACEDA_RefArray, GRACEDA_YYYYMMDD_Of_RefArray = GRACEDA_YYYYMMDD_Of_RefArray)

print("For ", GRACEDA_WhichVariable, ":")
print("--------------")

print("GRACEDA_YYYYMMDD_Of_RefArray.shape is ",GRACEDA_YYYYMMDD_Of_RefArray.shape)
print("GRACEDA_YYYYMMDD_Of_RefArray is ",GRACEDA_YYYYMMDD_Of_RefArray)

print("GRACEDA_RefArray.shape is ",GRACEDA_RefArray.shape)
print("GRACEDA_RefArray is ",GRACEDA_RefArray)
print("np.amin(np.isnan(GRACEDA_RefArray).sum(axis=0)) is ",np.amin(np.isnan(GRACEDA_RefArray).sum(axis=0)))
print("np.amax(np.isnan(GRACEDA_RefArray).sum(axis=0)) is ",np.amax(np.isnan(GRACEDA_RefArray).sum(axis=0)))
print("np.amin(np.isnan(GRACEDA_RefArray).sum(axis=1)) is ",np.amin(np.isnan(GRACEDA_RefArray).sum(axis=1)))
print("np.amax(np.isnan(GRACEDA_RefArray).sum(axis=1)) is ",np.amax(np.isnan(GRACEDA_RefArray).sum(axis=1)))
print("np.isnan(np.nansum(GRACEDA_RefArray, axis = 0)).sum() is ",np.isnan(np.nansum(GRACEDA_RefArray, axis = 0)).sum())
print("np.isnan(np.nansum(GRACEDA_RefArray, axis = 1)).sum() is ",np.isnan(np.nansum(GRACEDA_RefArray, axis = 1)).sum())
print('overall min is ',np.nanmin(GRACEDA_RefArray),', overall max is ',np.nanmax(GRACEDA_RefArray))


