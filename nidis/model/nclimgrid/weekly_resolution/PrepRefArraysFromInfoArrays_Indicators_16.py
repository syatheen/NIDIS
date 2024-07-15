# BEGIN code arguments / editable section


CPCsoilmoist_InfoFilename = '/discover/nobackup/projects/nca/syatheen/CPCsoilmoisture_Npzs/RefArrDaily_20080205To20200106_ClimGrid1D.npz'

CPCsoilmoist_Ref_BeginDateVecList = [2008, 2, 5]  # CPCsoilmoist beginning year, month, day of month, this is also a Tuesday
CPCsoilmoist_Ref_EndDateVecList = [2019, 12, 31]  # CPCsoilmoist ending year, month, day of month, this is also a Tuesday


CPCsoilmoist_RefFileName = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/Indicator_16/weekly_resolution/RefArrays/ClimGrid_CPCsoilmoist_'+format(CPCsoilmoist_Ref_BeginDateVecList[0],'04')+format(CPCsoilmoist_Ref_BeginDateVecList[1],'02')+format(CPCsoilmoist_Ref_BeginDateVecList[2],'02')+'To'+format(CPCsoilmoist_Ref_EndDateVecList[0],'04')+format(CPCsoilmoist_Ref_EndDateVecList[1],'02')+format(CPCsoilmoist_Ref_EndDateVecList[2],'02')+'.npz'

# END code arguments / editable section

from datetime import date, datetime, timedelta
import sys
import numpy as np
from calendar import monthrange
import time

start_time = time.time()

CPCsoilmoist_Ref_BeginDate = date(CPCsoilmoist_Ref_BeginDateVecList[0], CPCsoilmoist_Ref_BeginDateVecList[1], CPCsoilmoist_Ref_BeginDateVecList[2])
CPCsoilmoist_Ref_EndDate = date(CPCsoilmoist_Ref_EndDateVecList[0], CPCsoilmoist_Ref_EndDateVecList[1], CPCsoilmoist_Ref_EndDateVecList[2])


if CPCsoilmoist_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for CPCsoilmoist_Ref needs to be a Tuesday!!')
  sys.exit(0)
if CPCsoilmoist_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for CPCsoilmoist_Ref needs to be a Tuesday!!')
  sys.exit(0)
#END check whether the beginning and ending days are indeed Tuesdays

if CPCsoilmoist_Ref_BeginDate > CPCsoilmoist_Ref_EndDate:
  print('CPCsoilmoist_Ref_BeginDate should not be later than CPCsoilmoist_Ref_EndDate!!!')
  sys.exit(0)

#BEGIN section for time-interpolating info arrays to desired temporal resolution


CPCsoilmoist_Info = np.load(CPCsoilmoist_InfoFilename)

CPCsoilmoist_YYYYMMDD_Of_InfoArray  = CPCsoilmoist_Info['YYYYMMDD_Of_RefArrayForPrcntl']
CPCsoilmoist_InfoArray  = CPCsoilmoist_Info['RefArrayForPrcntl']


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

CPCsoilmoist_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(CPCsoilmoist_YYYYMMDD_Of_InfoArray, 3, 'CPCsoilmoist', np.NaN)

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
CPCsoilmoist_RealDatesList_Of_RefArray, CPCsoilmoist_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(CPCsoilmoist_Ref_BeginDate, CPCsoilmoist_Ref_EndDate)
#End calculating real dates list for reference arrays

CPCsoilmoist_RefArray = np.empty([ CPCsoilmoist_YYYYMMDD_Of_RefArray.shape[0], CPCsoilmoist_InfoArray.shape[1]])
CPCsoilmoist_RefArray[:] = np.NaN

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
 
def TimeMeanValues(SourceDatesList, DestinationDatesList, SourceArray, DestinationArray, EndingWindowSizeForMean):
  for DestinationDateIdx in range(len(DestinationDatesList)):
    ThisDestinationDate = DestinationDatesList[DestinationDateIdx] 
    SourceIdxForThisDest = SourceDatesList.index(ThisDestinationDate) 
    if SourceIdxForThisDest >= (EndingWindowSizeForMean - 1):
      DestinationArray[DestinationDateIdx,:] = np.nanmean(
             SourceArray[(SourceIdxForThisDest-(EndingWindowSizeForMean-1)):
                         (SourceIdxForThisDest+1),:], axis = 0) 
    else:
      DestinationArray[DestinationDateIdx,:] = np.nanmean(
             SourceArray[0:SourceIdxForThisDest+1,:], axis = 0) 
    #end of if SourceIdxForThisDest >= (EndingWindowSizeForMean - 1):
  #end of for DestinationDateIdx in range(len(DestinationDatesList)):
  return DestinationArray
#end of def TimeMeanValues(SourceDatesList, DestinationDatesList, SourceArray, DestinationArray, EndingWindowSizeForMean):

CPCsoilmoist_RefArray = TimeMeanValues(CPCsoilmoist_RealDatesList_Of_InfoArray, CPCsoilmoist_RealDatesList_Of_RefArray, CPCsoilmoist_InfoArray, CPCsoilmoist_RefArray, 7)

print("--- %s seconds ---" % (time.time() - start_time))

np.savez_compressed(CPCsoilmoist_RefFileName, CPCsoilmoist_RefArray = CPCsoilmoist_RefArray, CPCsoilmoist_YYYYMMDD_Of_RefArray = CPCsoilmoist_YYYYMMDD_Of_RefArray)


print("CPCsoilmoist_RefArray.shape is ",CPCsoilmoist_RefArray.shape)
print("CPCsoilmoist_RefArray is ",CPCsoilmoist_RefArray)
print("np.amin(np.isnan(CPCsoilmoist_RefArray).sum(axis=0)) is ",np.amin(np.isnan(CPCsoilmoist_RefArray).sum(axis=0)))
print("np.amax(np.isnan(CPCsoilmoist_RefArray).sum(axis=0)) is ",np.amax(np.isnan(CPCsoilmoist_RefArray).sum(axis=0)))
print('overall min is ',np.nanmin(CPCsoilmoist_RefArray),', overall max is ',np.nanmax(CPCsoilmoist_RefArray))




