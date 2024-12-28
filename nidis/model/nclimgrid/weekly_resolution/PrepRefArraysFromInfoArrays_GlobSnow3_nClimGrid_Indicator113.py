# BEGIN code arguments / editable section

GlobSnow3_InfoFilesDir = '/discover/nobackup/projects/nca/syatheen/GlobSnow3_Npzs/'

GlobSnow3_InfoFiles_BeginYYYYMMDDVecList = [1979, 1, 6] # Sat 
GlobSnow3_InfoFiles_EndYYYYMMDDVecList = [2018, 5, 31] # Thu

GlobSnow3_Ref_BeginDateVecList = [1979, 1, 9]  # GlobSnow3 beginning year, month, day of month, this is also a Tuesday
GlobSnow3_Ref_EndDateVecList = [2018, 5, 29]  # GlobSnow3 ending year, month, day of month, this is also a Tuesday

GlobSnow3_RefFileName = 'RefArrays/ClimGrid1D_GlobSnow3_'+format(GlobSnow3_Ref_BeginDateVecList[0],'04')+format(GlobSnow3_Ref_BeginDateVecList[1],'02')+format(GlobSnow3_Ref_BeginDateVecList[2],'02')+'To'+format(GlobSnow3_Ref_EndDateVecList[0],'04')+format(GlobSnow3_Ref_EndDateVecList[1],'02')+format(GlobSnow3_Ref_EndDateVecList[2],'02')+'.npz'

AnyYearZeroFill_BeginMonth = 5
AnyYearZeroFill_BeginDoM = 26
AnyYearZeroFill_EndMonth = 10
AnyYearZeroFill_EndDoM = 10

# END code arguments / editable section

from datetime import date, datetime, timedelta
import sys
import numpy as np
#np.set_printoptions(threshold=np.inf)
from calendar import monthrange
import time
import os
import copy

start_time = time.time()

GlobSnow3_Ref_BeginDate = date(GlobSnow3_Ref_BeginDateVecList[0], GlobSnow3_Ref_BeginDateVecList[1], GlobSnow3_Ref_BeginDateVecList[2])
GlobSnow3_Ref_EndDate = date(GlobSnow3_Ref_EndDateVecList[0], GlobSnow3_Ref_EndDateVecList[1], GlobSnow3_Ref_EndDateVecList[2])

#BEGIN check whether the beginning and ending days are indeed Tuesdays
if GlobSnow3_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for GlobSnow3_Ref needs to be a Tuesday!!')
  sys.exit(0)
if GlobSnow3_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for GlobSnow3_Ref needs to be a Tuesday!!')
  sys.exit(0)
#END check whether the beginning and ending days are indeed Tuesdays

if GlobSnow3_Ref_BeginDate > GlobSnow3_Ref_EndDate:
  print('GlobSnow3_Ref_BeginDate should not be later than GlobSnow3_Ref_EndDate!!!')
  sys.exit(0)

#BEGIN section for concatenating daily arrays

for WhichYear in range(GlobSnow3_InfoFiles_BeginYYYYMMDDVecList[0], GlobSnow3_InfoFiles_EndYYYYMMDDVecList[0]+1):

  if WhichYear == GlobSnow3_InfoFiles_BeginYYYYMMDDVecList[0]:
    BeginMonth = GlobSnow3_InfoFiles_BeginYYYYMMDDVecList[1]
  else:
    BeginMonth = 1
  #end of if WhichYear == GlobSnow3_InfoFiles_BeginYYYYMMDDVecList[0]

  if WhichYear == GlobSnow3_InfoFiles_EndYYYYMMDDVecList[0]:
    EndMonth = GlobSnow3_InfoFiles_EndYYYYMMDDVecList[1]
  else:
    EndMonth = 12
  #end of if WhichYear == GlobSnow3_InfoFiles_EndYYYYMMDDVecList[0]

  for WhichMonth in range(BeginMonth, EndMonth+1):

    if ( (WhichYear == GlobSnow3_InfoFiles_BeginYYYYMMDDVecList[0]) and (WhichMonth == BeginMonth) ):
      BeginDoM = GlobSnow3_InfoFiles_BeginYYYYMMDDVecList[2]
    else:
      BeginDoM = 1
    #end of if WhichMonth == BeginMonth

    if ( (WhichYear == GlobSnow3_InfoFiles_EndYYYYMMDDVecList[0]) and (WhichMonth == EndMonth) ):
      EndDoM = GlobSnow3_InfoFiles_EndYYYYMMDDVecList[2]
    else:
      EndDoM = monthrange(WhichYear, WhichMonth)[1]
    #end of if WhichMonth == EndMonth

    ThisYYYYMM_ClimDivs_Info = np.load(GlobSnow3_InfoFilesDir + 'GlobSnow3_' + format(WhichYear, '04') + format(WhichMonth, '02') + '_ClimGrid1D.npz')

    ThisYYYYMMDD_Of_InfoArrayForPrcntl = ThisYYYYMM_ClimDivs_Info['YYYYMMDD_Of_InfoArray']
    ThisYYYYMMDD_InfoArrayForPrcntl = ThisYYYYMM_ClimDivs_Info['InfoArray'] 
        
    if ( (WhichYear == GlobSnow3_InfoFiles_BeginYYYYMMDDVecList[0]) and
         (WhichMonth == GlobSnow3_InfoFiles_BeginYYYYMMDDVecList[1]) ) :
      GlobSnow3_YYYYMMDD_Of_InfoArray = np.copy(ThisYYYYMMDD_Of_InfoArrayForPrcntl)
      GlobSnow3_InfoArray = np.copy(ThisYYYYMMDD_InfoArrayForPrcntl)
    else: #of if ( (WhichYear == GlobSnow3_InfoFiles_BeginYYYYMMDDVecList[0]) and....
      GlobSnow3_YYYYMMDD_Of_InfoArray = np.concatenate((GlobSnow3_YYYYMMDD_Of_InfoArray, ThisYYYYMMDD_Of_InfoArrayForPrcntl), axis = 0)
      GlobSnow3_InfoArray = np.concatenate((GlobSnow3_InfoArray, ThisYYYYMMDD_InfoArrayForPrcntl), axis = 0)
    #end of if ( (WhichYear == GlobSnow3_InfoFiles_BeginYYYYMMDDVecList[0]) and....

  #end of for WhichMonth in range(BeginMonth, EndMonth+1)
  
#end of for WhichYear in range(GlobSnow3_InfoFiles_BeginYYYYMMDDVecList[0], GlobSnow3_InfoFiles_EndYYYYMMDDVecList[0]+1)

for WhichYear in range(GlobSnow3_InfoFiles_BeginYYYYMMDDVecList[0], GlobSnow3_InfoFiles_EndYYYYMMDDVecList[0]+1):

  BeginYYYYMMDD_ZeroFillEarliestPossible_ThisYear = 10000 * WhichYear + 100 * AnyYearZeroFill_BeginMonth + AnyYearZeroFill_BeginDoM
  EndYYYYMMDD_ZeroFillLatestPossible_ThisYear = 10000 * WhichYear + 100 * AnyYearZeroFill_EndMonth + AnyYearZeroFill_EndDoM

  if WhichYear == GlobSnow3_InfoFiles_BeginYYYYMMDDVecList[0]:
    BeginYYYYMMDD_ThisYear = 10000 * WhichYear + 100 * GlobSnow3_InfoFiles_BeginYYYYMMDDVecList[1] + GlobSnow3_InfoFiles_BeginYYYYMMDDVecList[2]
    if BeginYYYYMMDD_ThisYear <= BeginYYYYMMDD_ZeroFillEarliestPossible_ThisYear :
      BeginYYYYMMDD_ZeroFill_ThisYear = copy.deepcopy(BeginYYYYMMDD_ZeroFillEarliestPossible_ThisYear)
    elif ( (BeginYYYYMMDD_ThisYear > BeginYYYYMMDD_ZeroFillEarliestPossible_ThisYear) and
           (BeginYYYYMMDD_ThisYear <= EndYYYYMMDD_ZeroFillLatestPossible_ThisYear) ):
      BeginYYYYMMDD_ZeroFill_ThisYear = copy.deepcopy(BeginYYYYMMDD_ThisYear)
    else:
      BeginYYYYMMDD_ZeroFill_ThisYear = -1
    #end of if BeginYYYYMMDD_ThisYear <= BeginYYYYMMDD_ZeroFillEarliestPossible_ThisYear 
  else:
    BeginYYYYMMDD_ZeroFill_ThisYear = copy.deepcopy(BeginYYYYMMDD_ZeroFillEarliestPossible_ThisYear)
  #end of if WhichYear == GlobSnow3_InfoFiles_BeginYYYYMMDDVecList[0]

  if WhichYear == GlobSnow3_InfoFiles_EndYYYYMMDDVecList[0]:
    EndYYYYMMDD_ThisYear = 10000 * WhichYear + 100 * GlobSnow3_InfoFiles_EndYYYYMMDDVecList[1] + GlobSnow3_InfoFiles_EndYYYYMMDDVecList[2] 
    if EndYYYYMMDD_ThisYear >= EndYYYYMMDD_ZeroFillLatestPossible_ThisYear :
      EndYYYYMMDD_ZeroFill_ThisYear = copy.deepcopy(EndYYYYMMDD_ZeroFillLatestPossible_ThisYear)
    elif ( (EndYYYYMMDD_ThisYear >= BeginYYYYMMDD_ZeroFillEarliestPossible_ThisYear) and
           (EndYYYYMMDD_ThisYear < EndYYYYMMDD_ZeroFillLatestPossible_ThisYear) ):
      EndYYYYMMDD_ZeroFill_ThisYear = copy.deepcopy(EndYYYYMMDD_ThisYear)
    else:
      EndYYYYMMDD_ZeroFill_ThisYear = -1
  else:
    EndYYYYMMDD_ZeroFill_ThisYear = copy.deepcopy(EndYYYYMMDD_ZeroFillLatestPossible_ThisYear)
  #end of if WhichYear == GlobSnow3_InfoFiles_EndYYYYMMDDVecList[0]

  if ( ( BeginYYYYMMDD_ZeroFill_ThisYear > 0 ) and ( EndYYYYMMDD_ZeroFill_ThisYear > 0 ) ): 

    BeginIdxs = np.where(GlobSnow3_YYYYMMDD_Of_InfoArray == BeginYYYYMMDD_ZeroFill_ThisYear)  
    EndIdxs = np.where(GlobSnow3_YYYYMMDD_Of_InfoArray == EndYYYYMMDD_ZeroFill_ThisYear)  

    GlobSnow3_InfoArray[ BeginIdxs[0][0] : (EndIdxs[0][0] + 1), : ]  = 0.0

  #end of if ( ( BeginYYYYMMDD_ZeroFill_ThisYear != -1 ) and ( EndYYYYMMDD_ZeroFill_ThisYear != -1 ) )

#end of for WhichYear in range(GlobSnow3_InfoFiles_BeginYYYYMMDDVecList[0], GlobSnow3_InfoFiles_EndYYYYMMDDVecList[0]+1)

#END section for concatenating daily arrays

#print("GlobSnow3_YYYYMMDD_Of_InfoArray.shape is ",GlobSnow3_YYYYMMDD_Of_InfoArray.shape)
#print("GlobSnow3_YYYYMMDD_Of_InfoArray is ",GlobSnow3_YYYYMMDD_Of_InfoArray)

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

GlobSnow3_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(GlobSnow3_YYYYMMDD_Of_InfoArray, 3, 'GlobSnow3', np.NaN)

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

GlobSnow3_RealDatesList_Of_RefArray, GlobSnow3_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(GlobSnow3_Ref_BeginDate, GlobSnow3_Ref_EndDate)

#print("GlobSnow3_YYYYMMDD_Of_RefArray.shape is ",GlobSnow3_YYYYMMDD_Of_RefArray.shape)
#print("GlobSnow3_YYYYMMDD_Of_RefArray is ",GlobSnow3_YYYYMMDD_Of_RefArray)

#End calculating real dates list for reference arrays

GlobSnow3_RefArray = np.empty([ GlobSnow3_YYYYMMDD_Of_RefArray.shape[0], GlobSnow3_InfoArray.shape[1]])
GlobSnow3_RefArray[:] = np.NaN

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

GlobSnow3_RefArray = TimeMeanValues(GlobSnow3_RealDatesList_Of_InfoArray, GlobSnow3_RealDatesList_Of_RefArray, GlobSnow3_InfoArray, GlobSnow3_RefArray, 7)

print("--- %s seconds ---" % (time.time() - start_time))

np.savez_compressed(GlobSnow3_RefFileName, GlobSnow3_RefArray = GlobSnow3_RefArray, GlobSnow3_YYYYMMDD_Of_RefArray = GlobSnow3_YYYYMMDD_Of_RefArray)

print("GlobSnow3_YYYYMMDD_Of_RefArray.shape is ",GlobSnow3_YYYYMMDD_Of_RefArray.shape)
print("GlobSnow3_YYYYMMDD_Of_RefArray is ",GlobSnow3_YYYYMMDD_Of_RefArray)

print("GlobSnow3_RefArray.shape is ",GlobSnow3_RefArray.shape)
print("GlobSnow3_RefArray is ",GlobSnow3_RefArray)
#print("GlobSnow3_RefArray[100,:] is ",GlobSnow3_RefArray[100,:])
print("np.amin(np.isnan(GlobSnow3_RefArray).sum(axis=0)) is ",np.amin(np.isnan(GlobSnow3_RefArray).sum(axis=0)))
print("np.amax(np.isnan(GlobSnow3_RefArray).sum(axis=0)) is ",np.amax(np.isnan(GlobSnow3_RefArray).sum(axis=0)))
print("np.amin(np.isnan(GlobSnow3_RefArray).sum(axis=1)) is ",np.amin(np.isnan(GlobSnow3_RefArray).sum(axis=1)))
print("np.amax(np.isnan(GlobSnow3_RefArray).sum(axis=1)) is ",np.amax(np.isnan(GlobSnow3_RefArray).sum(axis=1)))
print('overall min is ',np.nanmin(GlobSnow3_RefArray),', overall max is ',np.nanmax(GlobSnow3_RefArray))




