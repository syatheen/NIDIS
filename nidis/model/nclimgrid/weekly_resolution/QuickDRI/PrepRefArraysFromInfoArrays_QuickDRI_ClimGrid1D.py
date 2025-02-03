#!/usr/bin/env python
# Coded by Soni Yatheendradas
#         on Nov 11, 2024
from __future__ import division

# BEGIN code arguments / editable section

#QuickDRI_InfoFilesDir = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/QuickDRI/InfoArrsWeekly/'
QuickDRI_InfoFilesDir = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/QuickDRI/InfoArrsWeekly/'

QuickDRI_Info_BeginYearWeekVecList = [2000, 3] # 2000/01/21 
QuickDRI_Info_EndYearWeekVecList = [2020, 52]  # 2020/12/31  

QuickDRI_Ref_BeginDateVecList = [2000, 1, 25] # QuickDRI beginning year, month, day of month, this is also a Tuesday
QuickDRI_Ref_EndDateVecList = [2020, 12, 29]  # QuickDRI ending year, month, day of month, this is also a Tuesday

QuickDRI_RefFileName = 'RefArrays/ClimGrid1D_QuickDRI_'+format(QuickDRI_Ref_BeginDateVecList[0],'04')+format(QuickDRI_Ref_BeginDateVecList[1],'02')+format(QuickDRI_Ref_BeginDateVecList[2],'02')+'To'+format(QuickDRI_Ref_EndDateVecList[0],'04')+format(QuickDRI_Ref_EndDateVecList[1],'02')+format(QuickDRI_Ref_EndDateVecList[2],'02')+'.npz'

# END code arguments / editable section

from datetime import date, datetime, timedelta
import sys
import numpy as np
from calendar import monthrange
import time

start_time = time.time()

QuickDRI_Ref_BeginDate = date(QuickDRI_Ref_BeginDateVecList[0], QuickDRI_Ref_BeginDateVecList[1], QuickDRI_Ref_BeginDateVecList[2])
QuickDRI_Ref_EndDate = date(QuickDRI_Ref_EndDateVecList[0], QuickDRI_Ref_EndDateVecList[1], QuickDRI_Ref_EndDateVecList[2])

#BEGIN check whether the beginning and ending days are indeed Tuesdays
if QuickDRI_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for QuickDRI_Ref needs to be a Tuesday!!')
  sys.exit(0)
if QuickDRI_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for QuickDRI_Ref needs to be a Tuesday!!')
  sys.exit(0)
#END check whether the beginning and ending days are indeed Tuesdays

if QuickDRI_Ref_BeginDate > QuickDRI_Ref_EndDate:
  print('QuickDRI_Ref_BeginDate should not be later than QuickDRI_Ref_EndDate!!!')
  sys.exit(0)

#BEGIN section for time-interpolating info arrays to desired temporal resolution

for WhichYear in range(QuickDRI_Info_BeginYearWeekVecList[0], QuickDRI_Info_EndYearWeekVecList[0]+1):

  if WhichYear == QuickDRI_Info_BeginYearWeekVecList[0]:
    BeginWeek = QuickDRI_Info_BeginYearWeekVecList[1]
  else:
    BeginWeek = 1

  if WhichYear == QuickDRI_Info_EndYearWeekVecList[0]:
    EndWeek = QuickDRI_Info_EndYearWeekVecList[1]
  else:
    EndWeek = 52

  for WhichWeek in range(BeginWeek, EndWeek+1):

    RelativeTo_DateVecList = [ WhichYear-1, 12, 31, 0, 0, 0]

    RelativeTo_Date = date(RelativeTo_DateVecList[0], RelativeTo_DateVecList[1], RelativeTo_DateVecList[2])
    WhichDate = RelativeTo_Date + timedelta(days=WhichWeek*7)
    WhichMonth = WhichDate.month
    WhichDoM = WhichDate.day

    InfoArrayFileName = QuickDRI_InfoFilesDir+format(WhichYear,'04')+format(WhichMonth,'02')+format(WhichDoM,'02')+'_ClimGrid1D.npz'

    InfoArrayFile_Info = np.load(InfoArrayFileName)

    WhichWeek_QuickDRI_YYYYMMDD_Of_InfoArray = InfoArrayFile_Info['YYYYMMDD_Of_RefArrayForPrcntl']
    WhichWeek_QuickDRI_InfoArray  = InfoArrayFile_Info['RefArrayForPrcntl']
    if WhichWeek == 52:
      WhichWeek_QuickDRI_YYYYMMDD_Of_InfoArray[0, 0] = 10000*WhichYear + 100*WhichMonth + 31  
    if ( (WhichYear == QuickDRI_Info_BeginYearWeekVecList[0]) and (WhichWeek == QuickDRI_Info_BeginYearWeekVecList[1])):
      QuickDRI_YYYYMMDD_Of_InfoArray = np.copy(WhichWeek_QuickDRI_YYYYMMDD_Of_InfoArray)
      QuickDRI_InfoArray = np.copy(WhichWeek_QuickDRI_InfoArray)
    else:
      QuickDRI_YYYYMMDD_Of_InfoArray = np.concatenate((QuickDRI_YYYYMMDD_Of_InfoArray, WhichWeek_QuickDRI_YYYYMMDD_Of_InfoArray), axis = 0)
      QuickDRI_InfoArray = np.concatenate((QuickDRI_InfoArray, WhichWeek_QuickDRI_InfoArray), axis = 0)
    #end of if ( (WhichYear == QuickDRI_Info_BeginYearWeekVecList[0]) and (WhichWeek == QuickDRI_Info_BeginYearWeekVecList[1]))

  #end of for WhichWeek in range(BeginWeek, EndWeek+1)

#end of for WhichYear in range(QuickDRI_Info_BeginYearWeekVecList[0], QuickDRI_Info_EndYearWeekVecList[0]+1)

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

QuickDRI_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(QuickDRI_YYYYMMDD_Of_InfoArray, 3, 'QuickDRI', np.NaN)

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

QuickDRI_RealDatesList_Of_RefArray, QuickDRI_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(QuickDRI_Ref_BeginDate, QuickDRI_Ref_EndDate)

#End calculating real dates list for reference arrays

QuickDRI_RefArray = np.empty([ QuickDRI_YYYYMMDD_Of_RefArray.shape[0], QuickDRI_InfoArray.shape[1]])
QuickDRI_RefArray[:] = np.NaN

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

QuickDRI_RefArray = TimeInterpolateValues(QuickDRI_RealDatesList_Of_InfoArray, QuickDRI_RealDatesList_Of_RefArray, QuickDRI_InfoArray, QuickDRI_RefArray)

print("--- %s seconds ---" % (time.time() - start_time))

np.savez_compressed(QuickDRI_RefFileName, QuickDRI_RefArray = QuickDRI_RefArray, QuickDRI_YYYYMMDD_Of_RefArray = QuickDRI_YYYYMMDD_Of_RefArray)

print("QuickDRI_YYYYMMDD_Of_RefArray.shape is ",QuickDRI_YYYYMMDD_Of_RefArray.shape)
print("QuickDRI_YYYYMMDD_Of_RefArray is ",QuickDRI_YYYYMMDD_Of_RefArray)

print("QuickDRI_RefArray.shape is ",QuickDRI_RefArray.shape)
print("QuickDRI_RefArray is ",QuickDRI_RefArray)
print("np.amin(np.isnan(QuickDRI_RefArray).sum(axis=0)) is ",np.amin(np.isnan(QuickDRI_RefArray).sum(axis=0)))
print("np.amax(np.isnan(QuickDRI_RefArray).sum(axis=0)) is ",np.amax(np.isnan(QuickDRI_RefArray).sum(axis=0)))
print("np.amin(np.isnan(QuickDRI_RefArray).sum(axis=1)) is ",np.amin(np.isnan(QuickDRI_RefArray).sum(axis=1)))
print("np.amax(np.isnan(QuickDRI_RefArray).sum(axis=1)) is ",np.amax(np.isnan(QuickDRI_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(QuickDRI_RefArray),', overall max is ',np.nanmax(QuickDRI_RefArray))




