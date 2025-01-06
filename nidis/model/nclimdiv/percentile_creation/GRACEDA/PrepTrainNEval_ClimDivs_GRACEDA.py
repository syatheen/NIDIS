from __future__ import division

# BEGIN code arguments / editable section

Training_BeginDateVecList = [2006, 1, 3] # Beginning training year, month, day of month, this is also a Tuesday
Training_EndDateVecList = [2018, 12, 25] # Ending training year, month, day of month, this is also a Tuesday

Eval_BeginDateVecList = [2019, 1, 1] # Beginning evaluation year, month, day of month, this is also a Tuesday
Eval_EndDateVecList = [2019, 12, 31] # Ending evaluation year, month, day of month, this is also a Tuesday

GRACEDA_rtzsm_inst_RefFileName = 'RefArrays/ClimDiv_GRACEDA_rtzsm_inst_20020402To20201020.npz'
GRACEDA_sfsm_inst_RefFileName = 'RefArrays/ClimDiv_GRACEDA_sfsm_inst_20020402To20201020.npz'
GRACEDA_gws_inst_RefFileName = 'RefArrays/ClimDiv_GRACEDA_gws_inst_20020402To20201020.npz'

#USDM_InfoFileName = '/discover/nobackup/syatheen/NIDIS/Data/usdm_shapefiles/private/InfoArrWeekly_20000104To20200428.npz'
USDM_InfoFileName = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/usdm_shapefiles/private/InfoArrWeekly_20000104To20200428.npz'

TrainDataFilename = 'PreppedTrainNEvalNpzs/ClimDivs/Train_GRACEDA_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'

DevDataFilename = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_GRACEDA_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
TestDataFilename = 'PreppedTrainNEvalNpzs/ClimDivs/Test_GRACEDA_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

# END code arguments / editable section

from datetime import date, datetime, timedelta
import sys
import numpy as np
from scipy.interpolate import interp1d
from scipy.stats import rankdata

ssstart_Overall = datetime.now()

Training_BeginDate = date(Training_BeginDateVecList[0], Training_BeginDateVecList[1], Training_BeginDateVecList[2])
Training_EndDate = date(Training_EndDateVecList[0], Training_EndDateVecList[1], Training_EndDateVecList[2])
Eval_BeginDate = date(Eval_BeginDateVecList[0], Eval_BeginDateVecList[1], Eval_BeginDateVecList[2])
Eval_EndDate = date(Eval_EndDateVecList[0], Eval_EndDateVecList[1], Eval_EndDateVecList[2])

#BEGIN check whether the beginning and ending days are indeed Tuesdays
if Training_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for training needs to be a Tuesday!!')
  sys.exit(0)
if Training_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for training needs to be a Tuesday!!')
  sys.exit(0)
if Eval_BeginDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Beginning Date Vector for evaluation needs to be a Tuesday!!')
  sys.exit(0)
if Eval_EndDate.weekday() != 1:  # 0 for Monday, 1 for Tuesday
  print('Ending Date Vector for evaluation needs to be a Tuesday!!')
  sys.exit(0)
#END check whether the beginning and ending days are indeed Tuesdays

if Training_BeginDate > Training_EndDate:
  print('Training_BeginDate should not be later than Training_EndDate!!!')
  sys.exit(0)
if Eval_BeginDate > Eval_EndDate:
  print('Eval_BeginDate should not be later than Eval_EndDate!!!')
  sys.exit(0)

GRACEDA_rtzsm_inst_RefObject = np.load(GRACEDA_rtzsm_inst_RefFileName)
GRACEDA_sfsm_inst_RefObject = np.load(GRACEDA_sfsm_inst_RefFileName)
GRACEDA_gws_inst_RefObject = np.load(GRACEDA_gws_inst_RefFileName)

GRACEDA_YYYYMMDD_Of_RefArray = GRACEDA_rtzsm_inst_RefObject['GRACEDA_YYYYMMDD_Of_RefArray']

GRACEDA_rtzsm_inst_RefArray = GRACEDA_rtzsm_inst_RefObject['GRACEDA_RefArray']
GRACEDA_sfsm_inst_RefArray = GRACEDA_sfsm_inst_RefObject['GRACEDA_RefArray']
GRACEDA_gws_inst_RefArray = GRACEDA_gws_inst_RefObject['GRACEDA_RefArray']

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

def PrintInfoAboutArray(ThisArray, ThisArray_Str):
  print(ThisArray_Str,".shape is ",ThisArray.shape)
  print(ThisArray_Str,".dtype is ",ThisArray.dtype)
  print(ThisArray_Str," is ",ThisArray)
  print("np.amin(np.isnan(",ThisArray_Str,").sum(axis=0)) is ",np.amin(np.isnan(ThisArray).sum(axis=0)))
  print("np.amax(np.isnan(",ThisArray_Str,").sum(axis=0)) is ",np.amax(np.isnan(ThisArray).sum(axis=0)))
  print('overall min is ',np.nanmin(ThisArray),', overall max is ',np.nanmax(ThisArray))
#end of def PrintInfoAboutArray(ThisArray, ThisArray_Str):

#BEGIN section for training

GRACEDA_YYYYMMDD_Of_PrcntlArray, GRACEDA_rtzsm_inst_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(GRACEDA_YYYYMMDD_Of_RefArray, GRACEDA_rtzsm_inst_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
GRACEDA_YYYYMMDD_Of_PrcntlArray, GRACEDA_sfsm_inst_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(GRACEDA_YYYYMMDD_Of_RefArray, GRACEDA_sfsm_inst_RefArray, Training_BeginDateVecList, Training_EndDateVecList)
GRACEDA_YYYYMMDD_Of_PrcntlArray, GRACEDA_gws_inst_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(GRACEDA_YYYYMMDD_Of_RefArray, GRACEDA_gws_inst_RefArray, Training_BeginDateVecList, Training_EndDateVecList)

GRACEDA_rtzsm_inst_PrcntlArray = GRACEDA_rtzsm_inst_PrcntlArray/100
GRACEDA_sfsm_inst_PrcntlArray = GRACEDA_sfsm_inst_PrcntlArray/100
GRACEDA_gws_inst_PrcntlArray = GRACEDA_gws_inst_PrcntlArray/100

print('Training: NumDates = ', GRACEDA_rtzsm_inst_PrcntlArray.shape[0], ', NumSpatialUnits = ',GRACEDA_rtzsm_inst_PrcntlArray.shape[1])
PrintInfoAboutArray(GRACEDA_rtzsm_inst_PrcntlArray, 'GRACEDA_rtzsm_inst_PrcntlArray')
PrintInfoAboutArray(GRACEDA_sfsm_inst_PrcntlArray, 'GRACEDA_sfsm_inst_PrcntlArray')
PrintInfoAboutArray(GRACEDA_gws_inst_PrcntlArray, 'GRACEDA_gws_inst_PrcntlArray')

np.savez_compressed(TrainDataFilename, YYYYMMDD_Of_Array = GRACEDA_YYYYMMDD_Of_PrcntlArray, GRACEDA_rtzsm_inst_PrcntlArray = GRACEDA_rtzsm_inst_PrcntlArray, GRACEDA_sfsm_inst_PrcntlArray = GRACEDA_sfsm_inst_PrcntlArray, GRACEDA_gws_inst_PrcntlArray = GRACEDA_gws_inst_PrcntlArray)

#END section for training

#BEGIN section for evaluation

GRACEDA_YYYYMMDD_Of_PrcntlArray, GRACEDA_rtzsm_inst_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(GRACEDA_YYYYMMDD_Of_RefArray, GRACEDA_rtzsm_inst_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
GRACEDA_YYYYMMDD_Of_PrcntlArray, GRACEDA_sfsm_inst_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(GRACEDA_YYYYMMDD_Of_RefArray, GRACEDA_sfsm_inst_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)
GRACEDA_YYYYMMDD_Of_PrcntlArray, GRACEDA_gws_inst_PrcntlArray = TimeSlice_YYYYMMDDAndRefArray(GRACEDA_YYYYMMDD_Of_RefArray, GRACEDA_gws_inst_RefArray, Eval_BeginDateVecList, Eval_EndDateVecList)

GRACEDA_rtzsm_inst_PrcntlArray = GRACEDA_rtzsm_inst_PrcntlArray/100
GRACEDA_sfsm_inst_PrcntlArray = GRACEDA_sfsm_inst_PrcntlArray/100
GRACEDA_gws_inst_PrcntlArray = GRACEDA_gws_inst_PrcntlArray/100

Dev_GRACEDA_YYYYMMDD_Of_PrcntlArray = GRACEDA_YYYYMMDD_Of_PrcntlArray[::2]
Dev_GRACEDA_rtzsm_inst_PrcntlArray = GRACEDA_rtzsm_inst_PrcntlArray[::2]
Dev_GRACEDA_sfsm_inst_PrcntlArray = GRACEDA_sfsm_inst_PrcntlArray[::2]
Dev_GRACEDA_gws_inst_PrcntlArray = GRACEDA_gws_inst_PrcntlArray[::2]

Test_GRACEDA_YYYYMMDD_Of_PrcntlArray = GRACEDA_YYYYMMDD_Of_PrcntlArray[1::2]
Test_GRACEDA_rtzsm_inst_PrcntlArray = GRACEDA_rtzsm_inst_PrcntlArray[1::2]
Test_GRACEDA_sfsm_inst_PrcntlArray = GRACEDA_sfsm_inst_PrcntlArray[1::2]
Test_GRACEDA_gws_inst_PrcntlArray = GRACEDA_gws_inst_PrcntlArray[1::2]

print('Evaluation: Dev NumDates = ', Dev_GRACEDA_rtzsm_inst_PrcntlArray.shape[0], ', NumSpatialUnits = ', Dev_GRACEDA_rtzsm_inst_PrcntlArray.shape[1])
PrintInfoAboutArray(Dev_GRACEDA_rtzsm_inst_PrcntlArray, 'Dev_GRACEDA_rtzsm_inst_PrcntlArray')
PrintInfoAboutArray(Dev_GRACEDA_sfsm_inst_PrcntlArray, 'Dev_GRACEDA_sfsm_inst_PrcntlArray')
PrintInfoAboutArray(Dev_GRACEDA_gws_inst_PrcntlArray, 'Dev_GRACEDA_gws_inst_PrcntlArray')

print('Evaluation: Test NumDates = ', Test_GRACEDA_rtzsm_inst_PrcntlArray.shape[0], ', NumSpatialUnits = ', Test_GRACEDA_rtzsm_inst_PrcntlArray.shape[1])
PrintInfoAboutArray(Test_GRACEDA_rtzsm_inst_PrcntlArray, 'Test_GRACEDA_rtzsm_inst_PrcntlArray')
PrintInfoAboutArray(Test_GRACEDA_sfsm_inst_PrcntlArray, 'Test_GRACEDA_sfsm_inst_PrcntlArray')
PrintInfoAboutArray(Test_GRACEDA_gws_inst_PrcntlArray, 'Test_GRACEDA_gws_inst_PrcntlArray')

np.savez_compressed(DevDataFilename, YYYYMMDD_Of_Array = Dev_GRACEDA_YYYYMMDD_Of_PrcntlArray, GRACEDA_rtzsm_inst_PrcntlArray =  Dev_GRACEDA_rtzsm_inst_PrcntlArray, GRACEDA_sfsm_inst_PrcntlArray =  Dev_GRACEDA_sfsm_inst_PrcntlArray, GRACEDA_gws_inst_PrcntlArray =  Dev_GRACEDA_gws_inst_PrcntlArray)

np.savez_compressed(TestDataFilename, YYYYMMDD_Of_Array = Test_GRACEDA_YYYYMMDD_Of_PrcntlArray, GRACEDA_rtzsm_inst_PrcntlArray =  Test_GRACEDA_rtzsm_inst_PrcntlArray, GRACEDA_sfsm_inst_PrcntlArray =  Test_GRACEDA_sfsm_inst_PrcntlArray, GRACEDA_gws_inst_PrcntlArray =  Test_GRACEDA_gws_inst_PrcntlArray)

#END section for evaluation

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")



