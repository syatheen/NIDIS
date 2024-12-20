# BEGIN code arguments / editable section
from datetime import date, datetime, timedelta
import sys
import numpy as np
from calendar import monthrange
import time

PMDI_InfoFilename = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/Indicators_1_to_4/pdiRefArray_20050101To20200104_ClmGrd1D.npz' 
PHDI_InfoFilename = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/Indicators_1_to_4/phdRefArray_20050604To20200104_ClmGrd1D.npz'

PMDI_Ref_BeginDateVecList = [2005, 1, 4]  # PMDI beginning year, month, day of month, this is also a Tuesday
PMDI_Ref_EndDateVecList = [2019, 12, 31]  # PMDI ending year, month, day of month, this is also a Tuesday
PHDI_Ref_BeginDateVecList = [2005, 6, 7]  # PHDI beginning year, month, day of month, this is also a Tuesday
PHDI_Ref_EndDateVecList = [2019, 12, 31]  # PHDI ending year, month, day of month, this is also a Tuesday

PMDI_RefFileName = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/Indicators_1_to_4/weekly_resolution_output/ClimGrid_PMDI_'+format(PMDI_Ref_BeginDateVecList[0],'04')+format(PMDI_Ref_BeginDateVecList[1],'02')+format(PMDI_Ref_BeginDateVecList[2],'02')+'To'+format(PMDI_Ref_EndDateVecList[0],'04')+format(PMDI_Ref_EndDateVecList[1],'02')+format(PMDI_Ref_EndDateVecList[2],'02')+'.npz'
PHDI_RefFileName = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/Indicators_1_to_4/weekly_resolution_output/ClimGrid_PHDI_'+format(PHDI_Ref_BeginDateVecList[0],'04')+format(PHDI_Ref_BeginDateVecList[1],'02')+format(PHDI_Ref_BeginDateVecList[2],'02')+'To'+format(PHDI_Ref_EndDateVecList[0],'04')+format(PHDI_Ref_EndDateVecList[1],'02')+format(PHDI_Ref_EndDateVecList[2],'02')+'.npz'

# END code arguments / editable section

start_time = time.time()

PMDI_Ref_BeginDate = date(PMDI_Ref_BeginDateVecList[0], PMDI_Ref_BeginDateVecList[1], PMDI_Ref_BeginDateVecList[2])
PMDI_Ref_EndDate = date(PMDI_Ref_EndDateVecList[0], PMDI_Ref_EndDateVecList[1], PMDI_Ref_EndDateVecList[2])
PHDI_Ref_BeginDate = date(PHDI_Ref_BeginDateVecList[0], PHDI_Ref_BeginDateVecList[1], PHDI_Ref_BeginDateVecList[2])
PHDI_Ref_EndDate = date(PHDI_Ref_EndDateVecList[0], PHDI_Ref_EndDateVecList[1], PHDI_Ref_EndDateVecList[2])

#BEGIN check whether the beginning and ending days are indeed Tuesdays
if PMDI_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for PMDI_Ref needs to be a Tuesday!!')
  sys.exit(0)
if PMDI_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for PMDI_Ref needs to be a Tuesday!!')
  sys.exit(0)
if PHDI_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for PHDI_Ref needs to be a Tuesday!!')
  sys.exit(0)
if PHDI_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for PHDI_Ref needs to be a Tuesday!!')
  sys.exit(0)

#END check whether the beginning and ending days are indeed Tuesdays

if PMDI_Ref_BeginDate > PMDI_Ref_EndDate:
  print('PMDI_Ref_BeginDate should not be later than PMDI_Ref_EndDate!!!')
  sys.exit(0)
if PHDI_Ref_BeginDate > PHDI_Ref_EndDate:
  print('PHDI_Ref_BeginDate should not be later than PHDI_Ref_EndDate!!!')
  sys.exit(0)


#BEGIN section for time-interpolating info arrays to desired temporal resolution

PMDI_Info = np.load(PMDI_InfoFilename)
PHDI_Info = np.load(PHDI_InfoFilename)
#USDM_Info = np.load(USDM_InfoFilename)

PMDI_YYYYMMDD_Of_InfoArray  = PMDI_Info['YYYYMMDD_Of_RefArrayForPrcntl']
PMDI_YYYYMMDD_Of_InfoArray = np.expand_dims(PMDI_YYYYMMDD_Of_InfoArray, axis = 1)
PMDI_InfoArray  = PMDI_Info['Palmer_RefArrayForPrcntl']
PHDI_YYYYMMDD_Of_InfoArray  = PHDI_Info['YYYYMMDD_Of_RefArrayForPrcntl']
PHDI_YYYYMMDD_Of_InfoArray = np.expand_dims(PHDI_YYYYMMDD_Of_InfoArray, axis = 1)
PHDI_InfoArray  = PHDI_Info['Palmer_RefArrayForPrcntl']
#USDM_YYYYMMDD_Of_InfoArray  = USDM_Info['YYYYMMDD_Of_InfoArray']
#USDM_InfoArray  = USDM_Info['InfoArray']

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

PMDI_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(PMDI_YYYYMMDD_Of_InfoArray, 3, 'PMDI', np.NaN)
PHDI_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(PHDI_YYYYMMDD_Of_InfoArray, 3, 'PHDI', np.NaN)
# USDM_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(USDM_YYYYMMDD_Of_InfoArray, 3, 'USDM', np.NaN)

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
PMDI_RealDatesList_Of_RefArray, PMDI_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(PMDI_Ref_BeginDate, PMDI_Ref_EndDate)
PHDI_RealDatesList_Of_RefArray, PHDI_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(PHDI_Ref_BeginDate, PHDI_Ref_EndDate)
#End calculating real dates list for reference arrays

PMDI_RefArray = np.empty([ PMDI_YYYYMMDD_Of_RefArray.shape[0], PMDI_InfoArray.shape[1]])
PMDI_RefArray[:] = np.NaN
PHDI_RefArray = np.empty([ PHDI_YYYYMMDD_Of_RefArray.shape[0], PHDI_InfoArray.shape[1]])
PHDI_RefArray[:] = np.NaN

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
 
PMDI_RefArray = TimeInterpolateValues(PMDI_RealDatesList_Of_InfoArray, PMDI_RealDatesList_Of_RefArray, PMDI_InfoArray, PMDI_RefArray)
PHDI_RefArray = TimeInterpolateValues(PHDI_RealDatesList_Of_InfoArray, PHDI_RealDatesList_Of_RefArray, PHDI_InfoArray, PHDI_RefArray)

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

print("--- %s seconds ---" % (time.time() - start_time))

np.savez_compressed(PMDI_RefFileName, PMDI_RefArray = PMDI_RefArray, PMDI_YYYYMMDD_Of_RefArray = PMDI_YYYYMMDD_Of_RefArray)
np.savez_compressed(PHDI_RefFileName, PHDI_RefArray = PHDI_RefArray, PHDI_YYYYMMDD_Of_RefArray = PHDI_YYYYMMDD_Of_RefArray)

print("PMDI_RefArray.shape is ",PMDI_RefArray.shape)
print("PMDI_RefArray is ",PMDI_RefArray)
print("np.amin(np.isnan(PMDI_RefArray).sum(axis=0)) is ",np.amin(np.isnan(PMDI_RefArray).sum(axis=0)))
print("np.amax(np.isnan(PMDI_RefArray).sum(axis=0)) is ",np.amax(np.isnan(PMDI_RefArray).sum(axis=0)))
print('overall min is ',np.nanmin(PMDI_RefArray),', overall max is ',np.nanmax(PMDI_RefArray))

print("PHDI_RefArray.shape is ",PHDI_RefArray.shape)
print("PHDI_RefArray is ",PHDI_RefArray)
print("np.amin(np.isnan(PHDI_RefArray).sum(axis=0)) is ",np.amin(np.isnan(PHDI_RefArray).sum(axis=0)))
print("np.amax(np.isnan(PHDI_RefArray).sum(axis=0)) is ",np.amax(np.isnan(PHDI_RefArray).sum(axis=0)))
print('overall min is ',np.nanmin(PHDI_RefArray),', overall max is ',np.nanmax(PHDI_RefArray))
