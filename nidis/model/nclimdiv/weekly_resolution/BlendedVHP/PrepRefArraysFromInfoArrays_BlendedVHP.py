# BEGIN code arguments / editable section

BlendedVHP_InfoFilesDir = '/discover/nobackup/projects/nca/syatheen/BlendedVHP_Npzs/'

BlendedVHP_InfoFiles_BeginYearWeekVecList = [1981, 35] # [1981, 35] is [1981, 9, 2] Wed 
BlendedVHP_InfoFiles_EndYearWeekVecList = [2021, 39] # [2021, 39] is [2021, 9, 30] Thu

BlendedVHP_Ref_BeginDateVecList = [1981, 9, 8]  # BlendedVHP beginning year, month, day of month, this is also a Tuesday
BlendedVHP_Ref_EndDateVecList = [2021, 9, 28]  # BlendedVHP ending year, month, day of month, this is also a Tuesday

WhichVariable = 'VHI' # Choices are 'SMN', 'TCI', 'VCI' and 'VHI'

if WhichVariable == 'SMN':
  FileNameStartStr = 'SM.SMN'
elif WhichVariable == 'TCI':
  FileNameStartStr = 'VH.TCI'
elif WhichVariable == 'VCI':
  FileNameStartStr = 'VH.VCI'
elif WhichVariable == 'VHI':
  FileNameStartStr = 'VH.VHI'

BlendedVHP_RefFileName = 'RefArrays/ClimDiv_BlendedVHP_'+WhichVariable+'_'+format(BlendedVHP_Ref_BeginDateVecList[0],'04')+format(BlendedVHP_Ref_BeginDateVecList[1],'02')+format(BlendedVHP_Ref_BeginDateVecList[2],'02')+'To'+format(BlendedVHP_Ref_EndDateVecList[0],'04')+format(BlendedVHP_Ref_EndDateVecList[1],'02')+format(BlendedVHP_Ref_EndDateVecList[2],'02')+'.npz'

# END code arguments / editable section

from datetime import date, datetime, timedelta
import sys
import numpy as np
#np.set_printoptions(threshold=np.inf)
from calendar import monthrange
import time
import os

start_time = time.time()

BlendedVHP_Ref_BeginDate = date(BlendedVHP_Ref_BeginDateVecList[0], BlendedVHP_Ref_BeginDateVecList[1], BlendedVHP_Ref_BeginDateVecList[2])
BlendedVHP_Ref_EndDate = date(BlendedVHP_Ref_EndDateVecList[0], BlendedVHP_Ref_EndDateVecList[1], BlendedVHP_Ref_EndDateVecList[2])

#BEGIN check whether the beginning and ending days are indeed Tuesdays
if BlendedVHP_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for BlendedVHP_Ref needs to be a Tuesday!!')
  sys.exit(0)
if BlendedVHP_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for BlendedVHP_Ref needs to be a Tuesday!!')
  sys.exit(0)
#END check whether the beginning and ending days are indeed Tuesdays

if BlendedVHP_Ref_BeginDate > BlendedVHP_Ref_EndDate:
  print('BlendedVHP_Ref_BeginDate should not be later than BlendedVHP_Ref_EndDate!!!')
  sys.exit(0)

def YearWeekToYYYYMMDD(YearWeekVecList):

  ThisYear = YearWeekVecList[0]
  ThisWeek = YearWeekVecList[1]

  RelativeTo_ThisDateVecList = [ ThisYear-1, 12, 31, 0, 0, 0]
  RelativeTo_ThisDate = date(RelativeTo_ThisDateVecList[0], RelativeTo_ThisDateVecList[1], RelativeTo_ThisDateVecList[2])

  ThisDate = RelativeTo_ThisDate + timedelta(days=ThisWeek*7)
  ThisMonth = ThisDate.month
  ThisDoM = ThisDate.day

  ThisYYYYMMDDVecList = [ThisYear, ThisMonth, ThisDoM]

  return ThisYYYYMMDDVecList 
  
#end of def YearWeekToYYYYMMDD(YearWeekVecList)

BlendedVHP_InfoFiles_BeginYYYYMMDDVecList = YearWeekToYYYYMMDD(BlendedVHP_InfoFiles_BeginYearWeekVecList)

#BEGIN section for concatenating daily and partial ClimDiv Arrays

for WhichYear in range(BlendedVHP_InfoFiles_BeginYearWeekVecList[0], BlendedVHP_InfoFiles_EndYearWeekVecList[0]+1):

  if WhichYear == BlendedVHP_InfoFiles_BeginYearWeekVecList[0]:
    BeginWeek = BlendedVHP_InfoFiles_BeginYearWeekVecList[1]
  else:
    BeginWeek = 1
  #end of if WhichYear == BlendedVHP_InfoFiles_BeginYearWeekVecList[0]

  if WhichYear == BlendedVHP_InfoFiles_EndYearWeekVecList[0]:
    EndWeek = BlendedVHP_InfoFiles_EndYearWeekVecList[1]
  else:
    EndWeek = 52
  #end of if WhichYear == BlendedVHP_InfoFiles_EndYearWeekVecList[0]

  for WhichWeek in range(BeginWeek, EndWeek+1):

    WhichYYYYMMDD = YearWeekToYYYYMMDD([WhichYear, WhichWeek]) 

    WhichMonth = WhichYYYYMMDD[1]
    WhichDoM = WhichYYYYMMDD[2]

    If1stFileExists = os.path.exists(BlendedVHP_InfoFilesDir + FileNameStartStr + '_' + format(WhichYear, '04') + format(WhichMonth, '02') + format(WhichDoM, '02') + '_1stClimDivsPortion.npz')
    If2ndFileExists = os.path.exists(BlendedVHP_InfoFilesDir + FileNameStartStr + '_' + format(WhichYear, '04') + format(WhichMonth, '02') + format(WhichDoM, '02') + '_2ndClimDivsPortion.npz')

    if (If1stFileExists and If2ndFileExists):

      ThisYYYYMMDD_1stClimDivsSplit_Info = np.load(BlendedVHP_InfoFilesDir + FileNameStartStr + '_' + format(WhichYear, '04') + format(WhichMonth, '02') + format(WhichDoM, '02') + '_1stClimDivsPortion.npz')
      ThisYYYYMMDD_2ndClimDivsSplit_Info = np.load(BlendedVHP_InfoFilesDir + FileNameStartStr + '_' + format(WhichYear, '04') + format(WhichMonth, '02') + format(WhichDoM, '02') + '_2ndClimDivsPortion.npz')

      ThisYYYYMMDD_Of_InfoArrayForPrcntl = ThisYYYYMMDD_1stClimDivsSplit_Info['YYYYMMDD_Of_InfoArrayForPrcntl']
      ThisYYYYMMDD_1stClimDivsSplit_InfoArray = ThisYYYYMMDD_1stClimDivsSplit_Info['InfoArrayForPrcntl'] 
      ThisYYYYMMDD_2ndClimDivsSplit_InfoArray = ThisYYYYMMDD_2ndClimDivsSplit_Info['InfoArrayForPrcntl'] 
      ThisYYYYMMDD_InfoArray = np.concatenate((ThisYYYYMMDD_1stClimDivsSplit_InfoArray, ThisYYYYMMDD_2ndClimDivsSplit_InfoArray), axis = 1)
      
    else: #of if If1stFileExists and If2ndFileExists
      
      ThisYYYYMMDD_Of_InfoArrayForPrcntl = np.empty((1, 1), dtype=np.int32)
      ThisYYYYMMDD_Of_InfoArrayForPrcntl[0] = 10000*WhichYear + 100*WhichMonth + WhichDoM 
      ThisYYYYMMDD_InfoArray = np.empty((1, BlendedVHP_InfoArray.shape[1]))
      ThisYYYYMMDD_InfoArray[:] = np.NaN

    #end of if If1stFileExists and If2ndFileExists

    if ( (WhichYear == BlendedVHP_InfoFiles_BeginYYYYMMDDVecList[0]) and
         (WhichMonth == BlendedVHP_InfoFiles_BeginYYYYMMDDVecList[1]) and
         (WhichDoM == BlendedVHP_InfoFiles_BeginYYYYMMDDVecList[2]) ):
      BlendedVHP_YYYYMMDD_Of_InfoArray = np.copy(ThisYYYYMMDD_Of_InfoArrayForPrcntl)
      BlendedVHP_InfoArray = np.copy(ThisYYYYMMDD_InfoArray)
    else: #of if ( (WhichYear == BlendedVHP_InfoFiles_BeginYYYYMMDDVecList[0]) and....
      BlendedVHP_YYYYMMDD_Of_InfoArray = np.concatenate((BlendedVHP_YYYYMMDD_Of_InfoArray, ThisYYYYMMDD_Of_InfoArrayForPrcntl), axis = 0)
      BlendedVHP_InfoArray = np.concatenate((BlendedVHP_InfoArray, ThisYYYYMMDD_InfoArray), axis = 0)
    #end of if ( (WhichYear == BlendedVHP_InfoFiles_BeginYYYYMMDDVecList[0]) and....

  #end of for WhichWeek in range(BeginWeek, EndWeek+1)
  
#end of for WhichYear in range(BlendedVHP_InfoFiles_BeginYearWeekVecList[0], BlendedVHP_InfoFiles_EndYearWeekVecList[0]+1)

#END section for concatenating daily and partial ClimDiv Arrays

#print("BlendedVHP_YYYYMMDD_Of_InfoArray.shape is ",BlendedVHP_YYYYMMDD_Of_InfoArray.shape)
#print("BlendedVHP_YYYYMMDD_Of_InfoArray is ",BlendedVHP_YYYYMMDD_Of_InfoArray)

#BEGIN section for time-interpolating info arrays to desired temporal resolution

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

BlendedVHP_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(BlendedVHP_YYYYMMDD_Of_InfoArray, 3, 'BlendedVHP', np.NaN)

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

BlendedVHP_RealDatesList_Of_RefArray, BlendedVHP_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(BlendedVHP_Ref_BeginDate, BlendedVHP_Ref_EndDate)

#print("BlendedVHP_YYYYMMDD_Of_RefArray.shape is ",BlendedVHP_YYYYMMDD_Of_RefArray.shape)
#print("BlendedVHP_YYYYMMDD_Of_RefArray is ",BlendedVHP_YYYYMMDD_Of_RefArray)

#End calculating real dates list for reference arrays

BlendedVHP_RefArray = np.empty([ BlendedVHP_YYYYMMDD_Of_RefArray.shape[0], BlendedVHP_InfoArray.shape[1]])
BlendedVHP_RefArray[:] = np.NaN

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

def TimeInterpolateValues2(SourceDatesList, DestinationDatesList, SourceArray, DestinationArray):
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
      Idxs_AllRowsValid = np.where(SrcSlice_isnan_sum == 0)
      if Idxs_AllRowsValid[0].size > 0:
        SrcSlice_notnan = ~SrcSlice_isnan
        SrcSlice_notnan_int = SrcSlice_notnan.astype(np.int32)
        Wt1 = float(-DaysDiffList[SourceLowerIdxForThisDest+1])
        Wt2 = float(DaysDiffList[SourceLowerIdxForThisDest])
        WtsMat = np.repeat(np.array([[Wt1],[Wt2]], dtype = SrcSlice.dtype), repeats = SrcSlice.shape[1], axis = 1)
        Wtd_SrcSlice = np.multiply(SrcSlice, WtsMat)
        BooledWtsMat = np.multiply(WtsMat, SrcSlice_notnan_int)
        Wtd_SrcSlice_AllRowsValid = Wtd_SrcSlice[:, Idxs_AllRowsValid[0]]
        BooledWtsMat_AllRowsValid = BooledWtsMat[:, Idxs_AllRowsValid[0]]
        Sum_Wtd_SrcSlice_AllRowsValid = np.nansum(Wtd_SrcSlice_AllRowsValid, axis = 0)
        Sum_Wts_AllRowsValid = np.nansum(BooledWtsMat_AllRowsValid, axis = 0)
        DestinationArray[DestinationDateIdx,Idxs_AllRowsValid[0]] = np.divide(Sum_Wtd_SrcSlice_AllRowsValid,
                                                           Sum_Wts_AllRowsValid)
      #end of if Idxs_AllRowsValid[0].size > 0:
    #end of if ThisDestinationDate in SourceDatesList:
  #end of for DestinationDateIdx in range(len(DestinationDatesList)):
  return DestinationArray
#end of def TimeInterpolateValues2(SourceDatesList, DestinationDatesList, SourceArray, DestinationArray):

BlendedVHP_RefArray = TimeInterpolateValues2(BlendedVHP_RealDatesList_Of_InfoArray, BlendedVHP_RealDatesList_Of_RefArray, BlendedVHP_InfoArray, BlendedVHP_RefArray)

print("--- %s seconds ---" % (time.time() - start_time))

np.savez_compressed(BlendedVHP_RefFileName, BlendedVHP_RefArray = BlendedVHP_RefArray, BlendedVHP_YYYYMMDD_Of_RefArray = BlendedVHP_YYYYMMDD_Of_RefArray)

print("BlendedVHP_YYYYMMDD_Of_RefArray.shape is ",BlendedVHP_YYYYMMDD_Of_RefArray.shape)
print("BlendedVHP_YYYYMMDD_Of_RefArray is ",BlendedVHP_YYYYMMDD_Of_RefArray)

print("BlendedVHP_RefArray.shape is ",BlendedVHP_RefArray.shape)
print("BlendedVHP_RefArray is ",BlendedVHP_RefArray)
#print("BlendedVHP_RefArray[100,:] is ",BlendedVHP_RefArray[100,:])
print("np.amin(np.isnan(BlendedVHP_RefArray).sum(axis=0)) is ",np.amin(np.isnan(BlendedVHP_RefArray).sum(axis=0)))
print("np.amax(np.isnan(BlendedVHP_RefArray).sum(axis=0)) is ",np.amax(np.isnan(BlendedVHP_RefArray).sum(axis=0)))
print("np.amin(np.isnan(BlendedVHP_RefArray).sum(axis=1)) is ",np.amin(np.isnan(BlendedVHP_RefArray).sum(axis=1)))
print("np.amax(np.isnan(BlendedVHP_RefArray).sum(axis=1)) is ",np.amax(np.isnan(BlendedVHP_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(BlendedVHP_RefArray),', overall max is ',np.nanmax(BlendedVHP_RefArray))




