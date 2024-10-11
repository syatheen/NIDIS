# BEGIN code arguments / editable section


#/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/VegDRI/RefArrsWeekly/????????_ClimGrid1D.npz
#SNODAS_20061001_ClimGrid1D.npz
#!/usr/bin/env python
# Coded by Soni Yatheendradas
#         on Apr 30, 2023
from __future__ import division


from datetime import date, datetime, timedelta
import sys
import numpy as np
#np.set_printoptions(threshold=np.inf)
from calendar import monthrange
import time
import os


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




def main():


  # BEGIN code arguments / editable section

  #SNODAS_InfoFilesDir = '/discover/nobackup/projects/nca/syatheen/SNODAS_Npzs/'
  SNODAS_InfoFilesDir = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/QuickDRI/InfoArrsWeekly/'

  SNODAS_InfoFiles_BeginYYYYMMDDVecList = [2000, 1, 21] 
  SNODAS_InfoFiles_EndYYYYMMDDVecList = [2020, 12, 29] 

  SNODAS_Ref_BeginDateVecList = [2000, 1, 25]  # SNODAS beginning year, month, day of month, this is also a Tuesday
  SNODAS_Ref_EndDateVecList = [2020, 12, 29]  # SNODAS ending year, month, day of month, this is also a Tuesday

  SNODAS_RefFileName = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/Indicator_69/RefArrays/ClimGrid1D_QuickDRI_'+format(SNODAS_Ref_BeginDateVecList[0],'04')+format(SNODAS_Ref_BeginDateVecList[1],'02')+format(SNODAS_Ref_BeginDateVecList[2],'02')+'To'+format(SNODAS_Ref_EndDateVecList[0],'04')+format(SNODAS_Ref_EndDateVecList[1],'02')+format(SNODAS_Ref_EndDateVecList[2],'02')+'.npz'

  # END code arguments / editable section

  start_time = time.time()

  SNODAS_Ref_BeginDate = date(SNODAS_Ref_BeginDateVecList[0], SNODAS_Ref_BeginDateVecList[1], SNODAS_Ref_BeginDateVecList[2])
  SNODAS_Ref_EndDate = date(SNODAS_Ref_EndDateVecList[0], SNODAS_Ref_EndDateVecList[1], SNODAS_Ref_EndDateVecList[2])

  #BEGIN check whether the beginning and ending days are indeed Tuesdays
  if SNODAS_Ref_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
    print('Beginning Date Vector for SNODAS_Ref needs to be a Tuesday!!')
    sys.exit(0)
  if SNODAS_Ref_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
    print('Ending Date Vector for SNODAS_Ref needs to be a Tuesday!!')
    sys.exit(0)
  #END check whether the beginning and ending days are indeed Tuesdays

  if SNODAS_Ref_BeginDate > SNODAS_Ref_EndDate:
    print('SNODAS_Ref_BeginDate should not be later than SNODAS_Ref_EndDate!!!')
    sys.exit(0)

  #BEGIN section for concatenating daily and partial ClimDiv Arrays

  for WhichYear in range(SNODAS_InfoFiles_BeginYYYYMMDDVecList[0], SNODAS_InfoFiles_EndYYYYMMDDVecList[0]+1):

    if WhichYear == SNODAS_InfoFiles_BeginYYYYMMDDVecList[0]:
      BeginMonth = SNODAS_InfoFiles_BeginYYYYMMDDVecList[1]
    else:
      BeginMonth = 1
    #end of if WhichYear == SNODAS_InfoFiles_BeginYYYYMMDDVecList[0]

    if WhichYear == SNODAS_InfoFiles_EndYYYYMMDDVecList[0]:
      EndMonth = SNODAS_InfoFiles_EndYYYYMMDDVecList[1]
    else:
      EndMonth = 12
    #end of if WhichYear == SNODAS_InfoFiles_EndYYYYMMDDVecList[0]

    for WhichMonth in range(BeginMonth, EndMonth+1):

      if ( (WhichYear == SNODAS_InfoFiles_BeginYYYYMMDDVecList[0]) and (WhichMonth == BeginMonth) ):
        BeginDoM = SNODAS_InfoFiles_BeginYYYYMMDDVecList[2]
      else:
        BeginDoM = 1
      #end of if WhichMonth == BeginMonth

      if ( (WhichYear == SNODAS_InfoFiles_EndYYYYMMDDVecList[0]) and (WhichMonth == EndMonth) ):
        EndDoM = SNODAS_InfoFiles_EndYYYYMMDDVecList[2]
      else:
        EndDoM = monthrange(WhichYear, WhichMonth)[1]
      #end of if WhichMonth == EndMonth

      for WhichDoM in range(BeginDoM, EndDoM+1):

        IfFileExists = os.path.exists(SNODAS_InfoFilesDir + format(WhichYear, '04') + format(WhichMonth, '02') + format(WhichDoM, '02') + '_ClimGrid1D.npz')

        print(SNODAS_InfoFilesDir + format(WhichYear, '04') + format(WhichMonth, '02') + format(WhichDoM, '02') + '_ClimGrid1D.npz')

        if IfFileExists:

          ThisYYYYMMDD_ClimGrid1D_Info = np.load(SNODAS_InfoFilesDir + format(WhichYear, '04') + format(WhichMonth, '02') + format(WhichDoM, '02') + '_ClimGrid1D.npz')
    
          ThisYYYYMMDD_Of_InfoArrayForPrcntl = ThisYYYYMMDD_ClimGrid1D_Info['YYYYMMDD_Of_RefArrayForPrcntl']
          ThisYYYYMMDD_InfoArray = ThisYYYYMMDD_ClimGrid1D_Info['RefArrayForPrcntl'] 
          
        else: #of if IfFileExists
          
          ThisYYYYMMDD_Of_InfoArrayForPrcntl = np.empty((1, 1), dtype=np.int32)
          ThisYYYYMMDD_Of_InfoArrayForPrcntl[0] = 10000*WhichYear + 100*WhichMonth + WhichDoM 
          ThisYYYYMMDD_InfoArray = np.empty((1, SNODAS_InfoArray.shape[1]))
          ThisYYYYMMDD_InfoArray[:] = np.NaN

        #end of if IfFileExists

        if ( (WhichYear == SNODAS_InfoFiles_BeginYYYYMMDDVecList[0]) and
            (WhichMonth == SNODAS_InfoFiles_BeginYYYYMMDDVecList[1]) and
            (WhichDoM == SNODAS_InfoFiles_BeginYYYYMMDDVecList[2]) ):
          SNODAS_YYYYMMDD_Of_InfoArray = np.copy(ThisYYYYMMDD_Of_InfoArrayForPrcntl)
          SNODAS_InfoArray = np.copy(ThisYYYYMMDD_InfoArray)
        else: #of if ( (WhichYear == SNODAS_InfoFiles_BeginYYYYMMDDVecList[0]) and....
          SNODAS_YYYYMMDD_Of_InfoArray = np.concatenate((SNODAS_YYYYMMDD_Of_InfoArray, ThisYYYYMMDD_Of_InfoArrayForPrcntl), axis = 0)
          SNODAS_InfoArray = np.concatenate((SNODAS_InfoArray, ThisYYYYMMDD_InfoArray), axis = 0)
        #end of if ( (WhichYear == SNODAS_InfoFiles_BeginYYYYMMDDVecList[0]) and....

      #end of for WhichDoM in range(BeginDoM, EndDoM+1)

    #end of for WhichMonth in range(BeginMonth, EndMonth+1)
    
  #end of for WhichYear in range(SNODAS_InfoFiles_BeginYYYYMMDDVecList[0], SNODAS_InfoFiles_EndYYYYMMDDVecList[0]+1)

  #END section for concatenating daily and partial ClimDiv Arrays

  #print("SNODAS_YYYYMMDD_Of_InfoArray.shape is ",SNODAS_YYYYMMDD_Of_InfoArray.shape)
  #print("SNODAS_YYYYMMDD_Of_InfoArray is ",SNODAS_YYYYMMDD_Of_InfoArray)

  #BEGIN section for time-interpolating info arrays to desired temporal resolution

  SNODAS_RealDatesList_Of_InfoArray = GetRealDatesListOfInfoArray(SNODAS_YYYYMMDD_Of_InfoArray, 3, 'QuickDRI', np.NaN)

  SNODAS_RealDatesList_Of_RefArray, SNODAS_YYYYMMDD_Of_RefArray = GetTimeInfoOfRefArray(SNODAS_Ref_BeginDate, SNODAS_Ref_EndDate)

  #print("SNODAS_YYYYMMDD_Of_RefArray.shape is ",SNODAS_YYYYMMDD_Of_RefArray.shape)
  #print("SNODAS_YYYYMMDD_Of_RefArray is ",SNODAS_YYYYMMDD_Of_RefArray)

  #End calculating real dates list for reference arrays

  SNODAS_RefArray = np.empty([ SNODAS_YYYYMMDD_Of_RefArray.shape[0], SNODAS_InfoArray.shape[1]])
  SNODAS_RefArray[:] = np.NaN



  SNODAS_RefArray = TimeMeanValues(SNODAS_RealDatesList_Of_InfoArray, SNODAS_RealDatesList_Of_RefArray, SNODAS_InfoArray, SNODAS_RefArray, 7)

  print("--- %s seconds ---" % (time.time() - start_time))

  np.savez_compressed(SNODAS_RefFileName, 
                      QuickDRI_RefArray = SNODAS_RefArray, 
                      QuickDRI_YYYYMMDD_Of_RefArray = SNODAS_YYYYMMDD_Of_RefArray)

  print("Saved file")
  print("SNODAS_YYYYMMDD_Of_RefArray.shape is ",SNODAS_YYYYMMDD_Of_RefArray.shape)
  print("SNODAS_YYYYMMDD_Of_RefArray is ",SNODAS_YYYYMMDD_Of_RefArray)

  print("SNODAS_RefArray.shape is ",SNODAS_RefArray.shape)
  print("SNODAS_RefArray is ",SNODAS_RefArray)
  #print("SNODAS_RefArray[100,:] is ",SNODAS_RefArray[100,:])
  print("np.amin(np.isnan(SNODAS_RefArray).sum(axis=0)) is ",np.amin(np.isnan(SNODAS_RefArray).sum(axis=0)))
  print("np.amax(np.isnan(SNODAS_RefArray).sum(axis=0)) is ",np.amax(np.isnan(SNODAS_RefArray).sum(axis=0)))
  print("np.amin(np.isnan(SNODAS_RefArray).sum(axis=1)) is ",np.amin(np.isnan(SNODAS_RefArray).sum(axis=1)))
  print("np.amax(np.isnan(SNODAS_RefArray).sum(axis=1)) is ",np.amax(np.isnan(SNODAS_RefArray).sum(axis=1)))
  print('overall min is ',np.nanmin(SNODAS_RefArray),', overall max is ',np.nanmax(SNODAS_RefArray))
  return


if __name__ == '__main__':
    main()
