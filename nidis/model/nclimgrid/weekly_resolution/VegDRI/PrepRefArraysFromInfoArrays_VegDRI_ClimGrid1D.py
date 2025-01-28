#!/usr/bin/env python
# Coded by Soni Yatheendradas
#         on Nov 11, 2024
from __future__ import division

# BEGIN code arguments / editable section

VegDRI_InfoFilesDir = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/VegDRI/RefArrsWeekly/'

VegDRI_Info_BeginDateVecList = [2009, 4, 26] # VegDRI beginning year, month, day of month, this is also a Sunday
VegDRI_Info_EndDateVecList = [2020, 8, 9]  # VegDRI ending year, month, day of month, this is also a Sunday

VegDRI_Ref_BeginDateVecList = [2009, 4, 28] # VegDRI beginning year, month, day of month, this is also a Tuesday
VegDRI_Ref_EndDateVecList = [2020, 8, 4]  # VegDRI ending year, month, day of month, this is also a Tuesday

VegDRI_RefFileName = 'RefArrays/ClimGrid1D_VegDRI_'+format(VegDRI_Ref_BeginDateVecList[0],'04')+format(VegDRI_Ref_BeginDateVecList[1],'02')+format(VegDRI_Ref_BeginDateVecList[2],'02')+'To'+format(VegDRI_Ref_EndDateVecList[0],'04')+format(VegDRI_Ref_EndDateVecList[1],'02')+format(VegDRI_Ref_EndDateVecList[2],'02')+'.npz'

# END code arguments / editable section

from datetime import date, datetime, timedelta
import sys
import numpy as np
from calendar import monthrange
import time

start_time = time.time()

VegDRI_Info_BeginDateTime = datetime(VegDRI_Info_BeginDateVecList[0], VegDRI_Info_BeginDateVecList[1], VegDRI_Info_BeginDateVecList[2], 0, 0, 0)
VegDRI_Info_EndDateTime = datetime(VegDRI_Info_EndDateVecList[0], VegDRI_Info_EndDateVecList[1], VegDRI_Info_EndDateVecList[2], 0, 0, 0)
DiffTimee = VegDRI_Info_EndDateTime - VegDRI_Info_BeginDateTime
NumWeeks = int(round(DiffTimee.total_seconds()/(3600*24*7)) + 1)
print('Info NumWeeks = ',NumWeeks)

VegDRI_Ref_BeginDate = date(VegDRI_Ref_BeginDateVecList[0], VegDRI_Ref_BeginDateVecList[1], VegDRI_Ref_BeginDateVecList[2])
VegDRI_Ref_EndDate = date(VegDRI_Ref_EndDateVecList[0], VegDRI_Ref_EndDateVecList[1], VegDRI_Ref_EndDateVecList[2])

#BEGIN check whether the beginning and ending days are indeed Tuesdays
if VegDRI_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for VegDRI_Ref needs to be a Tuesday!!')
  sys.exit(0)
if VegDRI_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for VegDRI_Ref needs to be a Tuesday!!')
  sys.exit(0)
#END check whether the beginning and ending days are indeed Tuesdays

if VegDRI_Ref_BeginDate > VegDRI_Ref_EndDate:
  print('VegDRI_Ref_BeginDate should not be later than VegDRI_Ref_EndDate!!!')
  sys.exit(0)

#BEGIN section for time-interpolating info arrays to desired temporal resolution

for ThisWeek in range(NumWeeks):

  ThisDateTime = VegDRI_Info_BeginDateTime + timedelta(days=(ThisWeek*7))
  ThisYear = ThisDateTime.year
  ThisMonth = ThisDateTime.month
  ThisDoM = ThisDateTime.day

  InfoArrayFileName = VegDRI_InfoFilesDir+format(ThisYear,'04')+format(ThisMonth,'02')+format(ThisDoM,'02')+'_ClimGrid1D.npz'

  InfoArrayFile_Info = np.load(InfoArrayFileName)

  ThisWeek_VegDRI_YYYYMMDD_Of_InfoArray = InfoArrayFile_Info['YYYYMMDD_Of_RefArrayForPrcntl']
  ThisWeek_VegDRI_InfoArray  = InfoArrayFile_Info['RefArrayForPrcntl']
  if ThisWeek == 0:
    VegDRI_YYYYMMDD_Of_InfoArray = np.copy(ThisWeek_VegDRI_YYYYMMDD_Of_InfoArray)
    VegDRI_InfoArray = np.copy(ThisWeek_VegDRI_InfoArray)
  else:
    VegDRI_YYYYMMDD_Of_InfoArray = np.concatenate((VegDRI_YYYYMMDD_Of_InfoArray, ThisWeek_VegDRI_YYYYMMDD_Of_InfoArray), axis = 0)
    VegDRI_InfoArray = np.concatenate((VegDRI_InfoArray, ThisWeek_VegDRI_InfoArray), axis = 0)
  #end of if ThisWeek == 0

#end of for ThisWeek in range(NumWeeks)

def GetRealDatesListOfInfoArray(YYYYMMEtc_Of_InfoArray, NumDateElements, VariabNameForErrStr, WhereDayForNumDateElements2):
  # NumDateElements is 2 if YYYYMMEtc is in YYYYMM format, and 3 if in YYYYMMDD format
  # WhereDayForNumDateElements2 is 'mid' if value representative at mid-month, and 'end' if at end-month (e.g., accumulation)
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
      else:
        print('WhereDayForNumDateElements2 should be mid or end in GetRealDatesListOfInfoArray for '+VariabNameForErrStr+'!!!')
        sys.exit(0)
  return RealDatesList_Of_InfoArray
#end of def GetRealDatesListOfInfoArray(YYYYMMEtc_Of_InfoArray, NumDateElements, VariabNameForErrStr, WhereDayForNumDateElements2):

VegDRI_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(VegDRI_YYYYMMDD_Of_InfoArray, 3, 'VegDRI', np.NaN)

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

VegDRI_RealDatesList_Of_RefArray, VegDRI_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(VegDRI_Ref_BeginDate, VegDRI_Ref_EndDate)

#End calculating real dates list for reference arrays

VegDRI_RefArray = np.empty([ VegDRI_YYYYMMDD_Of_RefArray.shape[0], VegDRI_InfoArray.shape[1]])
VegDRI_RefArray[:] = np.NaN

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

VegDRI_RefArray = TimeInterpolateValues(VegDRI_RealDatesList_Of_InfoArray, VegDRI_RealDatesList_Of_RefArray, VegDRI_InfoArray, VegDRI_RefArray)

print("--- %s seconds ---" % (time.time() - start_time))

np.savez_compressed(VegDRI_RefFileName, VegDRI_RefArray = VegDRI_RefArray, VegDRI_YYYYMMDD_Of_RefArray = VegDRI_YYYYMMDD_Of_RefArray)

print("VegDRI_YYYYMMDD_Of_RefArray.shape is ",VegDRI_YYYYMMDD_Of_RefArray.shape)
print("VegDRI_YYYYMMDD_Of_RefArray is ",VegDRI_YYYYMMDD_Of_RefArray)

print("VegDRI_RefArray.shape is ",VegDRI_RefArray.shape)
print("VegDRI_RefArray is ",VegDRI_RefArray)
print("np.amin(np.isnan(VegDRI_RefArray).sum(axis=0)) is ",np.amin(np.isnan(VegDRI_RefArray).sum(axis=0)))
print("np.amax(np.isnan(VegDRI_RefArray).sum(axis=0)) is ",np.amax(np.isnan(VegDRI_RefArray).sum(axis=0)))
print("np.amin(np.isnan(VegDRI_RefArray).sum(axis=1)) is ",np.amin(np.isnan(VegDRI_RefArray).sum(axis=1)))
print("np.amax(np.isnan(VegDRI_RefArray).sum(axis=1)) is ",np.amax(np.isnan(VegDRI_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(VegDRI_RefArray),', overall max is ',np.nanmax(VegDRI_RefArray))




