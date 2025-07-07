# Coded by Soni Yatheendradas
#         on Nov 27, 2021
from __future__ import division
import sys
#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        IfMakeTargetBinary IfIncludeD0AsDrought WhichTrainData WhichDevData TargetVariable SpatialDomain NumInpLayers NumInpsForNDFracMI WhichInpCombinForNDFracMI WhichSeason WhichEvent
#ArgNum   1                  2                    3              4            5              6             7            8                  9                         10          11
import numpy as np
from datetime import datetime, timedelta
import geopandas as gpd
from sklearn.feature_selection import mutual_info_classif
from scipy.stats import entropy
from MI_classif_1ValueForMultiFeatures_Code import MI_classif_1ValueForMultiFeatures

IfMakeTargetBinary = sys.argv[1] # Choices are 'Y' for yes, and 'N' for no
IfIncludeD0AsDrought = sys.argv[2] # Choices are 'Y' for yes, and 'N' for no
WhichTrainData = sys.argv[3] # Choices are 'Trn13yrs' (for 2006/01/03 to 2018/12/25 weekly) # NOTE that train and dev data are mixed and randomized
WhichDevData = sys.argv[4] # Choices are 'Dv1yr_1' (for 2019/01/01 to 2019/12/31 weekly) only # NOTE that train and dev data are mixed and randomized
TargetVariable = sys.argv[5] # Choices are 'USDM', 'CPC_S' (for short-term), 'CPC_LE' (for long-term Eastern), and 'CPC_LW' (for long-term Western)  
SpatialDomain = sys.argv[6] # Choices are 'CONUS', 'CONWUS' (W for Western), 'CONEUS' (E for Eastern), 'USDMW' (W for West), 'USDMMW' (W for Midwest), 'USDMHP' (HP for HighPlains), 'USDMS' (S for South), 'USDMSE' (SE for Southeast), 'USDMNE' (NE for Northeast), 'Event' (for events, but gets assigned 'Event'+WhichEvent further below),
WhichArgForNumInpLayers = 7 # Which argument has info about number of input layers
NumInpLayers = int(round(float(sys.argv[WhichArgForNumInpLayers]))) # 113 for all input channels, 0 for All CPC Blend input channels, -1 for CPC Short-Term Blend, -2 for CPC Long-Term Blend (NonWest), -3 for CPC Long-Term Blend (Western), -4 for CPC Short-Term Blend & CPC Long-Term Blend (NonWest) together, -10 for remotely-sensed, -11 for modeled, -12 for modeled+PrecipObs
NumInpsForNDFracMI = sys.argv[8]
WhichInpCombinForNDFracMI = int(round(float(sys.argv[9]))) # 0-start
WhichSeason = sys.argv[10] # Choices are 'P' for sPring (Mar-May), 'U' for sUmmer (Jun-Aug), 'F' for Fall (Sep-Nov), 'W' for Winter (Dec-Feb), 'A' for all-seasons-together
WhichEvent = sys.argv[11] # Choices are 'SE' (for Southeast 2006-2008), 'T' (Texas 2011), 'MwC' (Midwest / Central U.S. 2012), 'C' (California 2012-17), and 'NP' (Northern Plains 2017) 

Num_random_states = 101
n_neighbors = 3

# BEGIN code arguments / editable section

if WhichSeason not in ['P', 'U', 'F', 'W', 'A']:
  sys.exit("Invalid WhichSeason Choice: should be 'P, 'U', 'F', 'W' or 'A'!!!")

if IfMakeTargetBinary not in ['Y', 'N']:
  sys.exit("Invalid IfMakeTargetBinary Choice: should be 'Y' or 'N'!!!")

if IfIncludeD0AsDrought not in ['Y', 'N']:
  sys.exit("Invalid IfIncludeD0AsDrought Choice: should be 'Y' or 'N'!!!")

if WhichTrainData == 'Trn13yrs':
  Training_BeginDateVecList = [2006, 1, 3] # Beginning training year, month, day of month, this is also a Tuesday
  Training_EndDateVecList = [2018, 12, 25] # Ending training year, month, day of month, this is also a Tuesday
  WhichTrainData_ShortStr = 'Trn13'
else:
  sys.exit("Invalid training data Choice!!!")

if WhichDevData == 'Dv1yr_1':
  Eval_BeginDateVecList = [2019, 1, 1] # Beginning evaluation year, month, day of month, this is also a Tuesday
  Eval_EndDateVecList = [2019, 12, 31] # Ending evaluation year, month, day of month, this is also a Tuesday
  WhichDevData_ShortStr = 'DT1'
else:
  sys.exit("Invalid eval data Choice!!!")

if ( (SpatialDomain == 'Event') and 
     ( (WhichEvent == 'SE') or
       (WhichEvent == 'T') or
       (WhichEvent == 'MwC') or
       (WhichEvent == 'C') or
       (WhichEvent == 'NP') ) ):
  SpatialDomain = 'Event' + WhichEvent
  if (WhichEvent == 'SE'):
    Event_BeginDateVecList = [2007, 4, 24]
    Event_EndDateVecList = [2008, 4, 1]
  elif (WhichEvent == 'T'):
    Event_BeginDateVecList = [2010, 12, 7]
    Event_EndDateVecList = [2012, 5, 15]
  elif (WhichEvent == 'MwC'):
    Event_BeginDateVecList = [2012, 6, 19]
    Event_EndDateVecList = [2013, 5, 28]
  elif (WhichEvent == 'C'):
    Event_BeginDateVecList = [2012, 1, 3]
    Event_EndDateVecList = [2017, 2, 7]
  elif (WhichEvent == 'NP'):
    Event_BeginDateVecList = [2017, 4, 25]
    Event_EndDateVecList = [2018, 4, 10]
else:
  #sys.exit("Invalid WhichEvent Choice!!!")
  Event_BeginDateVecList = Training_BeginDateVecList.copy()  
  Event_EndDateVecList = Training_EndDateVecList.copy()  
#end of if ( (SpatialDomain == 'Event') and... 

if ( (TargetVariable == 'USDM') and (SpatialDomain == 'CONUS') and
     (not NumInpLayers in [113, 0, -1, -10, -11, -12]) ):
  #sys.exit("NumInpLayers needs to be 113, 0, -1, -10, -11, or -12!!!")
  print("***********************NumInpLayers needs to be 113, 0, -1, -10, -11, or -12!!!***************")
#end of if ( (TargetVariable == 'USDM') and (SpatialDomain == 'CONUS') and...
if ( (TargetVariable == 'USDM') and (SpatialDomain == 'CONWUS') and
     (not NumInpLayers in [113, 0, -3, -10, -11, -12]) ):
  #sys.exit("NumInpLayers needs to be 113, 0, -3, -10, -11, or -12!!!")
  print("***********************NumInpLayers needs to be 113, 0, -3, -10, -11, or -12!!!***************")
#end of if ( (TargetVariable == 'USDM') and (SpatialDomain == 'CONWUS') and...
if ( (TargetVariable == 'USDM') and (SpatialDomain == 'CONEUS') and
     (not NumInpLayers in [113, 0, -2, -10, -11, -12]) ):
  #sys.exit("NumInpLayers needs to be 113, 0, -2, -10, -11, or -12!!!")
  print("***********************NumInpLayers needs to be 113, 0, -2, -10, -11, or -12!!!***************")
#end of if ( (TargetVariable == 'USDM') and (SpatialDomain == 'CONEUS') and...
if ( (TargetVariable == 'USDM') and (SpatialDomain == 'USDMW') and
     (not NumInpLayers in [113, 0, -10, -11, -12]) ):
  #sys.exit("NumInpLayers needs to be 113, 0, -10, -11, or -12!!!")
  print("***********************NumInpLayers needs to be 113, 0, -10, -11, or -12!!!***************")
#end of if ( (TargetVariable == 'USDM') and (SpatialDomain == 'USDMW') and...
if ( (TargetVariable == 'USDM') and (SpatialDomain == 'USDMMW') and
     (not NumInpLayers in [113, 0, -4, -10, -11, -12]) ):
  #sys.exit("NumInpLayers needs to be 113, 0, -4, -10, -11, or -12!!!")
  print("***********************NumInpLayers needs to be 113, 0, -4, -10, -11, or -12!!!***************")
#end of if ( (TargetVariable == 'USDM') and (SpatialDomain == 'USDMMW') and...
if ( (TargetVariable == 'USDM') and (SpatialDomain == 'USDMHP') and
     (not NumInpLayers in [113, 0, -10, -11, -12]) ):
  #sys.exit("NumInpLayers needs to be 113, 0, -10, -11, or -12!!!")
  print("***********************NumInpLayers needs to be 113, 0, -10, -11, or -12!!!***************")
#end of if ( (TargetVariable == 'USDM') and (SpatialDomain == 'USDMHP') and...
if ( (TargetVariable == 'USDM') and (SpatialDomain == 'USDMS') and
     (not NumInpLayers in [113, 0, -10, -11, -12]) ):
  #sys.exit("NumInpLayers needs to be 113, 0, -10, -11, or -12!!!")
  print("***********************NumInpLayers needs to be 113, 0, -10, -11, or -12!!!***************")
#end of if ( (TargetVariable == 'USDM') and (SpatialDomain == 'USDMS') and...
if ( (TargetVariable == 'USDM') and (SpatialDomain == 'USDMSE') and
     (not NumInpLayers in [113, 0, -4, -10, -11, -12]) ):
  #sys.exit("NumInpLayers needs to be 113, 0, -4, -10, -11, or -12!!!")
  print("***********************NumInpLayers needs to be 113, 0, -4, -10, -11, or -12!!!***************")
#end of if ( (TargetVariable == 'USDM') and (SpatialDomain == 'USDMSE') and...
if ( (TargetVariable == 'USDM') and (SpatialDomain == 'USDMNE') and
     (not NumInpLayers in [113, 0, -4, -10, -11, -12]) ):
  #sys.exit("NumInpLayers needs to be 113, 0, -4, -10, -11, or -12!!!")
  print("***********************NumInpLayers needs to be 113, 0, -4, -10, -11, or -12!!!***************")
#end of if ( (TargetVariable == 'USDM') and (SpatialDomain == 'USDMNE') and...
if ( (TargetVariable == 'USDM') and 
     ( (SpatialDomain == 'EventSE') or 
       (SpatialDomain == 'EventT') or 
       (SpatialDomain == 'EventMwC') or 
       (SpatialDomain == 'EventC') or 
       (SpatialDomain == 'EventNP') ) and
     (not NumInpLayers in [113, 0, -10, -11, -12] ) ):
  #sys.exit("NumInpLayers needs to be 113, 0, -10, -11, or -12!!!")
  print("***********************NumInpLayers needs to be 113, 0, -10, -11, or -12!!!***************")
#end of if ( (TargetVariable == 'USDM') and... 

if SpatialDomain == 'CONUS':
  IfSpatialSubDomain = False
elif SpatialDomain == 'CONWUS':
  IfSpatialSubDomain = True
  SpatialSubDomain = 'Western' 
  SpatialSubDomain_ShortStr = 'Wst' 
elif SpatialDomain == 'CONEUS':
  IfSpatialSubDomain = True
  SpatialSubDomain = 'NotWest' 
  SpatialSubDomain_ShortStr = 'NtWst' 
elif SpatialDomain == 'USDMW':
  IfSpatialSubDomain = True
  SpatialSubDomain = 'USDMWest' 
  SpatialSubDomain_ShortStr = 'U_W' 
elif SpatialDomain == 'USDMMW':
  IfSpatialSubDomain = True
  SpatialSubDomain = 'USDMMidwest' 
  SpatialSubDomain_ShortStr = 'U_MW' 
elif SpatialDomain == 'USDMHP':
  IfSpatialSubDomain = True
  SpatialSubDomain = 'USDMHighPlains' 
  SpatialSubDomain_ShortStr = 'U_HP' 
elif SpatialDomain == 'USDMS':
  IfSpatialSubDomain = True
  SpatialSubDomain = 'USDMSouth' 
  SpatialSubDomain_ShortStr = 'U_S' 
elif SpatialDomain == 'USDMSE':
  IfSpatialSubDomain = True
  SpatialSubDomain = 'USDMSoutheast' 
  SpatialSubDomain_ShortStr = 'U_SE' 
elif SpatialDomain == 'USDMNE':
  IfSpatialSubDomain = True
  SpatialSubDomain = 'USDMNortheast' 
  SpatialSubDomain_ShortStr = 'U_NE' 
elif SpatialDomain == 'EventSE':
  IfSpatialSubDomain = True
  SpatialSubDomain = 'EventSE' 
  SpatialSubDomain_ShortStr = 'EvSE' 
elif SpatialDomain == 'EventT':
  IfSpatialSubDomain = True
  SpatialSubDomain = 'EventT' 
  SpatialSubDomain_ShortStr = 'EvT' 
elif SpatialDomain == 'EventMwC':
  IfSpatialSubDomain = True
  SpatialSubDomain = 'EventMwC' 
  SpatialSubDomain_ShortStr = 'EvMwC' 
elif SpatialDomain == 'EventC':
  IfSpatialSubDomain = True
  SpatialSubDomain = 'EventC' 
  SpatialSubDomain_ShortStr = 'EvC' 
elif SpatialDomain == 'EventNP':
  IfSpatialSubDomain = True
  SpatialSubDomain = 'EventNP' 
  SpatialSubDomain_ShortStr = 'EvNP' 
else:
  sys.exit("Invalid SpatialDomain Choice!!!")
#end of if SpatialDomain == 'CONUS':

if SpatialDomain in ['CONUS', 'CONWUS', 'CONEUS', 'USDMW', 'USDMMW', 'USDMHP', 'USDMS', 'USDMSE', 'USDMNE', 'EventSE', 'EventT', 'EventMwC', 'EventC', 'EventNP']:

  if TargetVariable == 'USDM':

    TargetVariable_ShortStr = 'U'

    TrainDataFilename_USDM_New = 'PreppedTrainNEvalNpzs/ClimDivs/Train_USDM_New_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_USDM_New = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_USDM_New_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_USDM_New = 'PreppedTrainNEvalNpzs/ClimDivs/Test_USDM_New_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename = 'PreppedTrainNEvalNpzs/ClimDivs/Train_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename = 'PreppedTrainNEvalNpzs/ClimDivs/Test_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_OverallPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_Corr2OverallPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_OverallPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_Corr2OverallPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_OverallPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_Corr2OverallPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_AllnCG = 'PreppedTrainNEvalNpzs/ClimDivs/Train_AllnCG_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_AllnCG = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_AllnCG_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_AllnCG = 'PreppedTrainNEvalNpzs/ClimDivs/Test_AllnCG_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_GRACEDA = 'PreppedTrainNEvalNpzs/ClimDivs/Train_GRACEDA_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_GRACEDA = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_GRACEDA_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_GRACEDA = 'PreppedTrainNEvalNpzs/ClimDivs/Test_GRACEDA_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_GRACEDA_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_GRACEDA_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_GRACEDA_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_GRACEDA_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_GRACEDA_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_GRACEDA_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI1wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI01wk_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI1wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI01wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI1wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI01wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI2wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI02wk_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI2wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI02wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI2wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI02wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI3wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI03wk_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI3wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI03wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI3wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI03wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI4wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI04wk_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI4wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI04wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI4wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI04wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI5wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI05wk_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI5wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI05wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI5wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI05wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI6wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI06wk_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI6wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI06wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI6wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI06wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI7wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI07wk_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI7wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI07wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI7wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI07wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI8wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI08wk_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI8wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI08wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI8wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI08wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI9wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI09wk_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI9wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI09wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI9wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI09wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI10wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI10wk_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI10wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI10wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI10wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI10wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI11wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI11wk_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI11wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI11wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI11wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI11wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI12wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI12wk_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI12wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI12wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI12wk_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI12wk_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI1mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI01mn_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI1mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI01mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI1mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI01mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI2mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI02mn_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI2mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI02mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI2mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI02mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI3mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI03mn_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI3mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI03mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI3mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI03mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI4mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI04mn_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI4mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI04mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI4mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI04mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI5mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI05mn_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI5mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI05mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI5mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI05mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI6mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI06mn_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI6mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI06mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI6mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI06mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI7mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI07mn_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI7mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI07mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI7mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI07mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI8mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI08mn_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI8mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI08mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI8mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI08mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI9mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI09mn_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI9mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI09mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI9mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI09mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI10mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI10mn_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI10mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI10mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI10mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI10mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI11mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI11mn_Corr2MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI11mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI11mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI11mn_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI11mn_Corr2MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_EDDI12mn = 'PreppedTrainNEvalNpzs/ClimDivs/Train_EDDI12mn_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_EDDI12mn = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_EDDI12mn_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_EDDI12mn = 'PreppedTrainNEvalNpzs/ClimDivs/Test_EDDI12mn_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
 
#    TrainDataFilename_NLDAS_2_1mSM_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_NLDAS_2_1mSM_MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
#    DevDataFilename_NLDAS_2_1mSM_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_NLDAS_2_1mSM_MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
#    TestDataFilename_NLDAS_2_1mSM_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_NLDAS_2_1mSM_MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_NLDAS_2_daily = 'PreppedTrainNEvalNpzs/ClimDivs/Train_NLDAS_2_daily_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_NLDAS_2_daily = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_NLDAS_2_daily_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_NLDAS_2_daily = 'PreppedTrainNEvalNpzs/ClimDivs/Test_NLDAS_2_daily_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_VegDRI_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_VegDRI_MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_VegDRI_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_VegDRI_MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_VegDRI_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_VegDRI_MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_QuickDRI_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_QuickDRI_MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_QuickDRI_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_QuickDRI_MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_QuickDRI_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_QuickDRI_MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

#    TrainDataFilename_ESI_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_ESI_MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
#    DevDataFilename_ESI_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_ESI_MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
#    TestDataFilename_ESI_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_ESI_MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_ESImultiWeek_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_ESImultiWeek_MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_ESImultiWeek_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_ESImultiWeek_MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_ESImultiWeek_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_ESImultiWeek_MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

#    TrainDataFilename_SPI_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_SPI_MnthlyPrc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
#    DevDataFilename_SPI_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_SPI_MnthlyPrc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
#    TestDataFilename_SPI_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_SPI_MnthlyPrc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
#
#    TrainDataFilename_SPI_OverallPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_SPI_OvrllPrc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
#    DevDataFilename_SPI_OverallPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_SPI_OvrllPrc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
#    TestDataFilename_SPI_OverallPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_SPI_OvrllPrc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_SNODASnESACCI = 'PreppedTrainNEvalNpzs/ClimDivs/Train_SNODASnESACCI_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_SNODASnESACCI = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_SNODASnESACCI_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_SNODASnESACCI = 'PreppedTrainNEvalNpzs/ClimDivs/Test_SNODASnESACCI_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_IMERG = 'PreppedTrainNEvalNpzs/ClimDivs/Train_IMERG_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_IMERG = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_IMERG_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_IMERG = 'PreppedTrainNEvalNpzs/ClimDivs/Test_IMERG_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_BlendedVHP_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_BlendedVHP_MonthlyPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_BlendedVHP_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_BlendedVHP_MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_BlendedVHP_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_BlendedVHP_MonthlyPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

    TrainDataFilename_GlobSnow3_OverallPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Train_GlobSnow3_OverallPerc_'+str(Training_BeginDateVecList[0])+format(Training_BeginDateVecList[1],'02')+format(Training_BeginDateVecList[2],'02')+'To'+str(Training_EndDateVecList[0])+format(Training_EndDateVecList[1],'02')+format(Training_EndDateVecList[2],'02')+'.npz'
    DevDataFilename_GlobSnow3_OverallPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Dev_GlobSnow3_OverallPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'
    TestDataFilename_GlobSnow3_OverallPerc = 'PreppedTrainNEvalNpzs/ClimDivs/Test_GlobSnow3_OverallPerc_'+str(Eval_BeginDateVecList[0])+format(Eval_BeginDateVecList[1],'02')+format(Eval_BeginDateVecList[2],'02')+'To'+str(Eval_EndDateVecList[0])+format(Eval_EndDateVecList[1],'02')+format(Eval_EndDateVecList[2],'02')+'.npz'

  else: # if TargetVariable == 'USDM'

    sys.exit("Invalid TargetVariable choice, add relevant code lines!!!")

  # end of if TargetVariable == 'USDM'

  SpatialDomain_ShortStr = 'C'
else:
  sys.exit("Invalid SpatialDomain choice, add relevant code lines!!!")
#end of if SpatialDomain in ['CONUS', 'CONWUS', 'CONEUS', 'USDMW', 'USDMMW', 'USDMHP', 'USDMS', 'USDMSE', 'USDMNE', 'EventSE', 'EventT', 'EventMwC', 'EventC', 'EventNP']

#ShapeFilesDir = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/private/CONUS_CLIMATE_DIVISIONS/'
ShapeFilesDir = '/discover/nobackup/syatheen/NIDIS/Data/private/CONUS_CLIMATE_DIVISIONS/'

if IfSpatialSubDomain:
  if SpatialDomain in ['CONUS', 'CONWUS', 'CONEUS', 'USDMW', 'USDMMW', 'USDMHP', 'USDMS', 'USDMSE', 'USDMNE', 'EventSE', 'EventT', 'EventMwC', 'EventC', 'EventNP']:
    ClimDivShpFile = ShapeFilesDir + 'GIS.OFFICIAL_CLIM_DIVISIONS.shp'
    if SpatialSubDomain == 'Western':
      ClimDivShpFile_Sub = ShapeFilesDir + 'GIS.OFFICIAL_CLIM_DIVISIONS_Western.shp'
    elif SpatialSubDomain == 'NotWest':
      ClimDivShpFile_Sub = ShapeFilesDir + 'GIS.OFFICIAL_CLIM_DIVISIONS_NotWest.shp'
    elif SpatialSubDomain == 'USDMWest':
      ClimDivShpFile_Sub = ShapeFilesDir + 'GIS.OFFICIAL_CLIM_DIVISIONS_USDM_West.shp'
    elif SpatialSubDomain == 'USDMMidwest':
      ClimDivShpFile_Sub = ShapeFilesDir + 'GIS.OFFICIAL_CLIM_DIVISIONS_USDM_MidWest.shp'
    elif SpatialSubDomain == 'USDMHighPlains':
      ClimDivShpFile_Sub = ShapeFilesDir + 'GIS.OFFICIAL_CLIM_DIVISIONS_USDM_HighPlains.shp'
    elif SpatialSubDomain == 'USDMSouth':
      ClimDivShpFile_Sub = ShapeFilesDir + 'GIS.OFFICIAL_CLIM_DIVISIONS_USDM_South.shp'
    elif SpatialSubDomain == 'USDMSoutheast':
      ClimDivShpFile_Sub = ShapeFilesDir + 'GIS.OFFICIAL_CLIM_DIVISIONS_USDM_Southeast.shp'
    elif SpatialSubDomain == 'USDMNortheast':
      ClimDivShpFile_Sub = ShapeFilesDir + 'GIS.OFFICIAL_CLIM_DIVISIONS_USDM_Northeast.shp'
    elif SpatialSubDomain == 'EventSE':
      ClimDivShpFile_Sub = ShapeFilesDir + 'GIS.OFFICIAL_CLIM_DIVISIONS_Southeast2006To08Event.shp'
    elif SpatialSubDomain == 'EventT':
      ClimDivShpFile_Sub = ShapeFilesDir + 'GIS.OFFICIAL_CLIM_DIVISIONS_Texas2011Event.shp'
    elif SpatialSubDomain == 'EventMwC':
      ClimDivShpFile_Sub = ShapeFilesDir + 'GIS.OFFICIAL_CLIM_DIVISIONS_MidwNCentr2012Event.shp'
    elif SpatialSubDomain == 'EventC':
      ClimDivShpFile_Sub = ShapeFilesDir + 'GIS.OFFICIAL_CLIM_DIVISIONS_CA2012To17Event.shp'
    elif SpatialSubDomain == 'EventNP':
      ClimDivShpFile_Sub = ShapeFilesDir + 'GIS.OFFICIAL_CLIM_DIVISIONS_NorthernPlains2017Event.shp'
    else:
      sys.exit("Invalid SpatialSubDomain Choice!!!")
  else:
    sys.exit("Invalid SpatialDomain Choice!!!")
  #end of if SpatialDomain in ['CONUS', 'CONWUS', 'CONEUS', 'USDMW', 'USDMMW', 'USDMHP', 'USDMS', 'USDMSE', 'USDMNE', 'EventSE', 'EventT', 'EventMwC', 'EventC', 'EventNP']
#end of if IfSpatialSubDomain:

# Inp channel info. 
  # 1: Z-index ;
  # 2: 60-month Z-index ;
  # 3: PMDI; 
  # 4: PHDI; 
  # 5: 1-month nCG precip;
  # 6: 2-month nCG precip;
  # 7: 3-month nCG precip;
  # 8: 6-month nCG precip;
  # 9: 9-month nCG precip;
  # 10: 12-month nCG precip;
  # 11: 24-month nCG precip;
  # 12: 36-month nCG precip;
  # 13: 48-month nCG precip;
  # 14: 60-month nCG precip;
  # 15: 72-month nCG precip;
  # 16: CPC soil moisture;
  # 17: GRACE DA gw
  # 18: GRACE DA sfsm
  # 19: GRACE DA rzsm
  # 20: EDDI 1-wk
  # 21: EDDI 2-wk
  # 22: EDDI 3-wk
  # 23: EDDI 4-wk
  # 24: EDDI 5-wk
  # 25: EDDI 6-wk
  # 26: EDDI 7-wk
  # 27: EDDI 8-wk
  # 28: EDDI 9-wk
  # 29: EDDI 10-wk
  # 30: EDDI 11-wk
  # 31: EDDI 12-wk
  # 32: EDDI 1-mn
  # 33: EDDI 2-mn
  # 34: EDDI 3-mn
  # 35: EDDI 4-mn
  # 36: EDDI 5-mn
  # 37: EDDI 6-mn
  # 38: EDDI 7-mn
  # 39: EDDI 8-mn
  # 40: EDDI 9-mn
  # 41: EDDI 10-mn
  # 42: EDDI 11-mn
  # 43: EDDI 12-mn
  # 44: NLDAS-2 daily 1-m SM (Mosaic)
  # 45: NLDAS-2 daily 1-m SM (Noah)
  # 46: NLDAS-2 daily 1-m SM (SAC)
  # 47: NLDAS-2 daily 1-m SM (VIC)
  # 48: NLDAS-2 daily Total Column SM (Mosaic)
  # 49: NLDAS-2 daily Total Column SM (Noah)
  # 50: NLDAS-2 daily Total Column SM (SAC)
  # 51: NLDAS-2 daily Total Column SM (VIC)
  # 52: NLDAS-2 daily Evap (Mosaic)
  # 53: NLDAS-2 daily Evap (Noah)
  # 54: NLDAS-2 daily Evap (SAC)
  # 55: NLDAS-2 daily Evap (VIC)
  # 56: NLDAS-2 daily SWE (Mosaic)
  # 57: NLDAS-2 daily SWE (Noah)
  # 58: NLDAS-2 daily SWE (SAC)
  # 59: NLDAS-2 daily SWE (VIC)
  # 60: NLDAS-2 daily Runoff (Mosaic)
  # 61: NLDAS-2 daily Runoff (Noah)
  # 62: NLDAS-2 daily Runoff (SAC)
  # 63: NLDAS-2 daily Runoff (VIC)
  # 64: NLDAS-2 daily HUC04-level streamflow (Mosaic)
  # 65: NLDAS-2 daily HUC04-level streamflow (Noah)
  # 66: NLDAS-2 daily HUC04-level streamflow (SAC)
  # 67: NLDAS-2 daily HUC04-level streamflow (VIC)
  # 68: VegDRI
  # 69: QuickDRI
  # 70: 4-week ESI
  # 71: 12-week ESI
  # 72: 1-month nCG SPI gamma
  # 73: 2-month nCG SPI gamma
  # 74: 3-month nCG SPI gamma
  # 75: 6-month nCG SPI gamma
  # 76: 9-month nCG SPI gamma
  # 77: 12-month nCG SPI gamma
  # 78: 24-month nCG SPI gamma
  # 79: 36-month nCG SPI gamma
  # 80: 48-month nCG SPI gamma
  # 81: 60-month nCG SPI gamma
  # 82: 72-month nCG SPI gamma
  # 83: 1-month nCG SPEI Pearson
  # 84: 2-month nCG SPEI Pearson
  # 85: 3-month nCG SPEI Pearson
  # 86: 6-month nCG SPEI Pearson
  # 87: 9-month nCG SPEI Pearson
  # 88: 12-month nCG SPEI Pearson
  # 89: 24-month nCG SPEI Pearson
  # 90: 36-month nCG SPEI Pearson
  # 91: 48-month nCG SPEI Pearson
  # 92: 60-month nCG SPEI Pearson
  # 93: 72-month nCG SPEI Pearson
  # 94: 1-month nCG mean air temperature
  # 95: 1-month nCG max air temperature 
  # 96: SNODAS
  # 97: ESA-CCI
  # 98: 1-month IMERG;
  # 99: 2-month IMERG;
  # 100: 3-month IMERG;
  # 101: 6-month IMERG;
  # 102: 9-month IMERG;
  # 103: 12-month IMERG;
  # 104: 24-month IMERG;
  # 105: 36-month IMERG;
  # 106: 48-month IMERG;
  # 107: 60-month IMERG;
  # 108: 72-month IMERG;
  # 109: Smoothed NDVI (BlendedVHP)
  # 110: TCI (BlendedVHP)
  # 111: VCI (BlendedVHP)
  # 112: VHI (BlendedVHP)
  # 113: GlobSnow3

if NumInpLayers > 0: # All input channels
  InpLayerNumsCombination = list(range(1,NumInpLayers+1))
elif NumInpLayers == 0: # All CPC Blend input channels
  InpLayerNumsCombination = [1, 2, 3, 4, 5, 7, 8, 10, 11, 14, 16]
elif NumInpLayers < 0: # Predecided Groupings of input channels
  if NumInpLayers == -1: # CPC Short-Term Blend
    InpLayerNumsCombination = [1, 3, 5, 7, 16]
  elif NumInpLayers == -2: # CPC Long-Term Blend (NonWest)
    InpLayerNumsCombination = [4, 8, 10, 11, 14, 16]
  elif NumInpLayers == -3: # CPC Long-Term Blend (Western)
    InpLayerNumsCombination = [2, 4, 10, 11, 14, 16]
  elif NumInpLayers == -4: # CPC Short-Term Blend & CPC Long-Term Blend (NonWest)
    InpLayerNumsCombination = [1, 3, 4, 5, 7, 8, 10, 11, 14, 16]
  elif NumInpLayers == -10: # Remotely-sensed
    InpLayerNumsCombination = [*range(68, 72), *range(97, 114)]
  elif NumInpLayers == -11: # Modeled
    InpLayerNumsCombination = [*range(16, 68), 96]
  elif NumInpLayers == -12: # Modeled+PrecipObs
    InpLayerNumsCombination = [*range(5, 68), 96]
  else:
    sys.exit("Invalid choice in NumInpLayers < 0!!!")
  #end of if NumInpLayers == -1
#end of if NumInpLayers > 0

DictofNumNamePairs_Channels = {1: 'Z_index',
                               2: 'Z_index_60_month',
                               3: 'PMDI',
                               4: 'PHDI',
                               5: 'prcp_01_nCG',
                               6: 'prcp_02_nCG',
                               7: 'prcp_03_nCG',
                               8: 'prcp_06_nCG',
                               9: 'prcp_09_nCG',
                               10: 'prcp_12_nCG',
                               11: 'prcp_24_nCG',
                               12: 'prcp_36_nCG',
                               13: 'prcp_48_nCG',
                               14: 'prcp_60_nCG',
                               15: 'prcp_72_nCG',
                               16: 'CPC_soil_moisture',
                               17: 'GRACE_DA_gw',
                               18: 'GRACE_DA_sfsm',
                               19: 'GRACE_DA_rzsm',
                               20: 'EDDI_1wk',
                               21: 'EDDI_2wk',
                               22: 'EDDI_3wk',
                               23: 'EDDI_4wk',
                               24: 'EDDI_5wk',
                               25: 'EDDI_6wk',
                               26: 'EDDI_7wk',
                               27: 'EDDI_8wk',
                               28: 'EDDI_9wk',
                               29: 'EDDI_10wk',
                               30: 'EDDI_11wk',
                               31: 'EDDI_12wk',
                               32: 'EDDI_1mn',
                               33: 'EDDI_2mn',
                               34: 'EDDI_3mn',
                               35: 'EDDI_4mn',
                               36: 'EDDI_5mn',
                               37: 'EDDI_6mn',
                               38: 'EDDI_7mn',
                               39: 'EDDI_8mn',
                               40: 'EDDI_9mn',
                               41: 'EDDI_10mn',
                               42: 'EDDI_11mn',
                               43: 'EDDI_12mn',
                               44: 'NLDAS2D_1MSM_Mosaic',
                               45: 'NLDAS2D_1MSM_Noah',
                               46: 'NLDAS2D_1MSM_SAC',
                               47: 'NLDAS2D_1MSM_VIC',
                               48: 'NLDAS2D_TCSM_Mosaic',
                               49: 'NLDAS2D_TCSM_Noah',
                               50: 'NLDAS2D_TCSM_SAC',
                               51: 'NLDAS2D_TCSM_VIC',
                               52: 'NLDAS2D_EVAP_Mosaic',
                               53: 'NLDAS2D_EVAP_Noah',
                               54: 'NLDAS2D_EVAP_SAC',
                               55: 'NLDAS2D_EVAP_VIC',
                               56: 'NLDAS2D_SWE_Mosaic',
                               57: 'NLDAS2D_SWE_Noah',
                               58: 'NLDAS2D_SWE_SAC',
                               59: 'NLDAS2D_SWE_VIC',
                               60: 'NLDAS2D_RUN_Mosaic',
                               61: 'NLDAS2D_RUN_Noah',
                               62: 'NLDAS2D_RUN_SAC',
                               63: 'NLDAS2D_RUN_VIC',
                               64: 'NLDAS2D_STRMH04_Mosaic',
                               65: 'NLDAS2D_STRMH04_Noah',
                               66: 'NLDAS2D_STRMH04_SAC',
                               67: 'NLDAS2D_STRMH04_VIC',
                               68: 'VegDRI',
                               69: 'QuickDRI',
                               70: 'ESI_4wk',
                               71: 'ESI_12wk',
                               72: 'SPI_gamma_01_nCG',
                               73: 'SPI_gamma_02_nCG',
                               74: 'SPI_gamma_03_nCG',
                               75: 'SPI_gamma_06_nCG',
                               76: 'SPI_gamma_09_nCG',
                               77: 'SPI_gamma_12_nCG',
                               78: 'SPI_gamma_24_nCG',
                               79: 'SPI_gamma_36_nCG',
                               80: 'SPI_gamma_48_nCG',
                               81: 'SPI_gamma_60_nCG',
                               82: 'SPI_gamma_72_nCG',
                               83: 'SPEI_pear_01_nCG',
                               84: 'SPEI_pear_02_nCG',
                               85: 'SPEI_pear_03_nCG',
                               86: 'SPEI_pear_06_nCG',
                               87: 'SPEI_pear_09_nCG',
                               88: 'SPEI_pear_12_nCG',
                               89: 'SPEI_pear_24_nCG',
                               90: 'SPEI_pear_36_nCG',
                               91: 'SPEI_pear_48_nCG',
                               92: 'SPEI_pear_60_nCG',
                               93: 'SPEI_pear_72_nCG',
                               94: 'tavg_01_nCG',
                               95: 'tmax_01_nCG',
                               96: 'SNODAS',
                               97: 'ESA_CCI',
                               98: 'IMERG_01',
                               99: 'IMERG_02',
                               100: 'IMERG_03',
                               101: 'IMERG_06',
                               102: 'IMERG_09',
                               103: 'IMERG_12',
                               104: 'IMERG_24',
                               105: 'IMERG_36',
                               106: 'IMERG_48',
                               107: 'IMERG_60',
                               108: 'IMERG_72',
                               109: 'SmNDVI_BlendedVHP',
                               110: 'TCI_BlendedVHP',
                               111: 'VCI_BlendedVHP',
                               112: 'VHI_BlendedVHP',
                               113: 'GlobSnow3'}

InpLayersCombination = []
for WhichInpLayer in range(1,len(InpLayerNumsCombination)+1):
  InpLayersCombination.append( DictofNumNamePairs_Channels[InpLayerNumsCombination[WhichInpLayer-1]] )

if SpatialSubDomain[0:5] == 'Event':
  FracI_ClimDivs_AllValid_NDFeat_FileName = 'FracI_ClimDivs_AllValid_V2b_New/' + NumInpsForNDFracMI + '/' + IfMakeTargetBinary + IfIncludeD0AsDrought + '_' + TargetVariable_ShortStr + '_' + SpatialDomain_ShortStr 
else: # if SpatialSubDomain[0:5] == 'Event'
  FracI_ClimDivs_AllValid_NDFeat_FileName = 'FracI_ClimDivs_AllValid_V2b_New/' + NumInpsForNDFracMI + '/' + IfMakeTargetBinary + IfIncludeD0AsDrought + '_' + WhichTrainData_ShortStr + '_' + TargetVariable_ShortStr + '_' + SpatialDomain_ShortStr 
#end of if SpatialSubDomain[0:5] == 'Event'
if IfSpatialSubDomain:
  FracI_ClimDivs_AllValid_NDFeat_FileName = FracI_ClimDivs_AllValid_NDFeat_FileName + SpatialSubDomain_ShortStr
if NumInpLayers >= 0:
  FracI_ClimDivs_AllValid_NDFeat_FileName = FracI_ClimDivs_AllValid_NDFeat_FileName + '_In' + str(NumInpLayers)
elif NumInpLayers < 0:
  FracI_ClimDivs_AllValid_NDFeat_FileName = FracI_ClimDivs_AllValid_NDFeat_FileName + '_InM' + str(-NumInpLayers)
#end of if NumInpLayers >= 0
FracI_ClimDivs_AllValid_NDFeat_FileName = FracI_ClimDivs_AllValid_NDFeat_FileName + '_' + str(WhichInpCombinForNDFracMI) + '_' + WhichSeason + '.txt'
ActualNumInpLayers = len(InpLayersCombination)
if ActualNumInpLayers < 2:
  sys.exit("Minimum of 2 actual input layers enforced for now!!!")

# END code arguments / editable section

ssstart_Overall = datetime.now()

TrainDatas = {}
DevDatas = {}
TestDatas = {}

TrainData_USDM_New = np.load(TrainDataFilename_USDM_New)
DevData_USDM_New = np.load(DevDataFilename_USDM_New)
TestData_USDM_New = np.load(TestDataFilename_USDM_New)
TrainDatas['XYData_USDM_New'] = TrainData_USDM_New
DevDatas['XYData_USDM_New'] = DevData_USDM_New
TestDatas['XYData_USDM_New'] = TestData_USDM_New

#if ( ('Z_index' in InpLayersCombination) or
#     ('Z_index_60_month' in InpLayersCombination) or
#     ('CPC_soil_moisture' in InpLayersCombination) ):
TrainData = np.load(TrainDataFilename)
DevData = np.load(DevDataFilename)
TestData = np.load(TestDataFilename)
TrainDatas['XYData'] = TrainData
DevDatas['XYData'] = DevData
TestDatas['XYData'] = TestData
#end of if ( ('Z_index' in InpLayersCombination) or....

if ( ('PMDI' in InpLayersCombination) or
     ('PHDI' in InpLayersCombination) ):
  TrainData_OverallPerc = np.load(TrainDataFilename_OverallPerc)
  DevData_OverallPerc = np.load(DevDataFilename_OverallPerc)
  TestData_OverallPerc = np.load(TestDataFilename_OverallPerc)
  TrainDatas['XYData_OverallPerc'] = TrainData_OverallPerc
  DevDatas['XYData_OverallPerc'] = DevData_OverallPerc
  TestDatas['XYData_OverallPerc'] = TestData_OverallPerc
#end of if ( ('PMDI' in InpLayersCombination) or....

if ( ('prcp_01_nCG' in InpLayersCombination) or
     ('prcp_02_nCG' in InpLayersCombination) or
     ('prcp_03_nCG' in InpLayersCombination) or
     ('prcp_06_nCG' in InpLayersCombination) or
     ('prcp_09_nCG' in InpLayersCombination) or
     ('prcp_12_nCG' in InpLayersCombination) or
     ('prcp_24_nCG' in InpLayersCombination) or
     ('prcp_36_nCG' in InpLayersCombination) or
     ('prcp_48_nCG' in InpLayersCombination) or
     ('prcp_60_nCG' in InpLayersCombination) or
     ('prcp_72_nCG' in InpLayersCombination) or
     ('SPI_gamma_01_nCG' in InpLayersCombination) or
     ('SPI_gamma_02_nCG' in InpLayersCombination) or
     ('SPI_gamma_03_nCG' in InpLayersCombination) or
     ('SPI_gamma_06_nCG' in InpLayersCombination) or
     ('SPI_gamma_09_nCG' in InpLayersCombination) or
     ('SPI_gamma_12_nCG' in InpLayersCombination) or
     ('SPI_gamma_24_nCG' in InpLayersCombination) or
     ('SPI_gamma_36_nCG' in InpLayersCombination) or
     ('SPI_gamma_48_nCG' in InpLayersCombination) or
     ('SPI_gamma_60_nCG' in InpLayersCombination) or
     ('SPI_gamma_72_nCG' in InpLayersCombination) or
     ('SPEI_pear_01_nCG' in InpLayersCombination) or
     ('SPEI_pear_02_nCG' in InpLayersCombination) or
     ('SPEI_pear_03_nCG' in InpLayersCombination) or
     ('SPEI_pear_06_nCG' in InpLayersCombination) or
     ('SPEI_pear_09_nCG' in InpLayersCombination) or
     ('SPEI_pear_12_nCG' in InpLayersCombination) or
     ('SPEI_pear_24_nCG' in InpLayersCombination) or
     ('SPEI_pear_36_nCG' in InpLayersCombination) or
     ('SPEI_pear_48_nCG' in InpLayersCombination) or
     ('SPEI_pear_60_nCG' in InpLayersCombination) or
     ('SPEI_pear_72_nCG' in InpLayersCombination) or
     ('tavg_01_nCG' in InpLayersCombination) or
     ('tmax_01_nCG' in InpLayersCombination) ):
  TrainData_AllnCG = np.load(TrainDataFilename_AllnCG)
  DevData_AllnCG = np.load(DevDataFilename_AllnCG)
  TestData_AllnCG = np.load(TestDataFilename_AllnCG)
  TrainDatas['XYData_AllnCG'] = TrainData_AllnCG
  DevDatas['XYData_AllnCG'] = DevData_AllnCG
  TestDatas['XYData_AllnCG'] = TestData_AllnCG
#end of if ( ('prcp_01_nCG' in InpLayersCombination) or...

if ('GRACE_DA_gw' in InpLayersCombination):
  TrainData_GRACEDA = np.load(TrainDataFilename_GRACEDA)
  DevData_GRACEDA = np.load(DevDataFilename_GRACEDA)
  TestData_GRACEDA = np.load(TestDataFilename_GRACEDA)
  TrainDatas['XYData_GRACEDA'] = TrainData_GRACEDA
  DevDatas['XYData_GRACEDA'] = DevData_GRACEDA
  TestDatas['XYData_GRACEDA'] = TestData_GRACEDA
#end of if ('GRACE_DA_gw' in InpLayersCombination)

if ( ('GRACE_DA_sfsm' in InpLayersCombination) or
     ('GRACE_DA_rzsm' in InpLayersCombination) ):
  TrainData_GRACEDA_MonthlyPerc = np.load(TrainDataFilename_GRACEDA_MonthlyPerc)
  DevData_GRACEDA_MonthlyPerc = np.load(DevDataFilename_GRACEDA_MonthlyPerc)
  TestData_GRACEDA_MonthlyPerc = np.load(TestDataFilename_GRACEDA_MonthlyPerc)
  TrainDatas['XYData_GRACEDA_MonthlyPerc'] = TrainData_GRACEDA_MonthlyPerc
  DevDatas['XYData_GRACEDA_MonthlyPerc'] = DevData_GRACEDA_MonthlyPerc
  TestDatas['XYData_GRACEDA_MonthlyPerc'] = TestData_GRACEDA_MonthlyPerc
#end of if ( ('GRACE_DA_sfsm' in InpLayersCombination) or...

if ('EDDI_1wk' in InpLayersCombination):
  TrainData_EDDI1wk_MonthlyPerc = np.load(TrainDataFilename_EDDI1wk_MonthlyPerc)
  DevData_EDDI1wk_MonthlyPerc = np.load(DevDataFilename_EDDI1wk_MonthlyPerc)
  TestData_EDDI1wk_MonthlyPerc = np.load(TestDataFilename_EDDI1wk_MonthlyPerc)
  TrainDatas['XYData_EDDI1wk_MonthlyPerc'] = TrainData_EDDI1wk_MonthlyPerc
  DevDatas['XYData_EDDI1wk_MonthlyPerc'] = DevData_EDDI1wk_MonthlyPerc
  TestDatas['XYData_EDDI1wk_MonthlyPerc'] = TestData_EDDI1wk_MonthlyPerc
#end of if ('EDDI_1wk' in InpLayersCombination)

if ('EDDI_2wk' in InpLayersCombination):
  TrainData_EDDI2wk_MonthlyPerc = np.load(TrainDataFilename_EDDI2wk_MonthlyPerc)
  DevData_EDDI2wk_MonthlyPerc = np.load(DevDataFilename_EDDI2wk_MonthlyPerc)
  TestData_EDDI2wk_MonthlyPerc = np.load(TestDataFilename_EDDI2wk_MonthlyPerc)
  TrainDatas['XYData_EDDI2wk_MonthlyPerc'] = TrainData_EDDI2wk_MonthlyPerc
  DevDatas['XYData_EDDI2wk_MonthlyPerc'] = DevData_EDDI2wk_MonthlyPerc
  TestDatas['XYData_EDDI2wk_MonthlyPerc'] = TestData_EDDI2wk_MonthlyPerc
#end of if ('EDDI_2wk' in InpLayersCombination)

if ('EDDI_3wk' in InpLayersCombination):
  TrainData_EDDI3wk_MonthlyPerc = np.load(TrainDataFilename_EDDI3wk_MonthlyPerc)
  DevData_EDDI3wk_MonthlyPerc = np.load(DevDataFilename_EDDI3wk_MonthlyPerc)
  TestData_EDDI3wk_MonthlyPerc = np.load(TestDataFilename_EDDI3wk_MonthlyPerc)
  TrainDatas['XYData_EDDI3wk_MonthlyPerc'] = TrainData_EDDI3wk_MonthlyPerc
  DevDatas['XYData_EDDI3wk_MonthlyPerc'] = DevData_EDDI3wk_MonthlyPerc
  TestDatas['XYData_EDDI3wk_MonthlyPerc'] = TestData_EDDI3wk_MonthlyPerc
#end of if ('EDDI_3wk' in InpLayersCombination)

if ('EDDI_4wk' in InpLayersCombination):
  TrainData_EDDI4wk_MonthlyPerc = np.load(TrainDataFilename_EDDI4wk_MonthlyPerc)
  DevData_EDDI4wk_MonthlyPerc = np.load(DevDataFilename_EDDI4wk_MonthlyPerc)
  TestData_EDDI4wk_MonthlyPerc = np.load(TestDataFilename_EDDI4wk_MonthlyPerc)
  TrainDatas['XYData_EDDI4wk_MonthlyPerc'] = TrainData_EDDI4wk_MonthlyPerc
  DevDatas['XYData_EDDI4wk_MonthlyPerc'] = DevData_EDDI4wk_MonthlyPerc
  TestDatas['XYData_EDDI4wk_MonthlyPerc'] = TestData_EDDI4wk_MonthlyPerc
#end of if ('EDDI_4wk' in InpLayersCombination)

if ('EDDI_5wk' in InpLayersCombination):
  TrainData_EDDI5wk_MonthlyPerc = np.load(TrainDataFilename_EDDI5wk_MonthlyPerc)
  DevData_EDDI5wk_MonthlyPerc = np.load(DevDataFilename_EDDI5wk_MonthlyPerc)
  TestData_EDDI5wk_MonthlyPerc = np.load(TestDataFilename_EDDI5wk_MonthlyPerc)
  TrainDatas['XYData_EDDI5wk_MonthlyPerc'] = TrainData_EDDI5wk_MonthlyPerc
  DevDatas['XYData_EDDI5wk_MonthlyPerc'] = DevData_EDDI5wk_MonthlyPerc
  TestDatas['XYData_EDDI5wk_MonthlyPerc'] = TestData_EDDI5wk_MonthlyPerc
#end of if ('EDDI_5wk' in InpLayersCombination)

if ('EDDI_6wk' in InpLayersCombination):
  TrainData_EDDI6wk_MonthlyPerc = np.load(TrainDataFilename_EDDI6wk_MonthlyPerc)
  DevData_EDDI6wk_MonthlyPerc = np.load(DevDataFilename_EDDI6wk_MonthlyPerc)
  TestData_EDDI6wk_MonthlyPerc = np.load(TestDataFilename_EDDI6wk_MonthlyPerc)
  TrainDatas['XYData_EDDI6wk_MonthlyPerc'] = TrainData_EDDI6wk_MonthlyPerc
  DevDatas['XYData_EDDI6wk_MonthlyPerc'] = DevData_EDDI6wk_MonthlyPerc
  TestDatas['XYData_EDDI6wk_MonthlyPerc'] = TestData_EDDI6wk_MonthlyPerc
#end of if ('EDDI_6wk' in InpLayersCombination)

if ('EDDI_7wk' in InpLayersCombination):
  TrainData_EDDI7wk_MonthlyPerc = np.load(TrainDataFilename_EDDI7wk_MonthlyPerc)
  DevData_EDDI7wk_MonthlyPerc = np.load(DevDataFilename_EDDI7wk_MonthlyPerc)
  TestData_EDDI7wk_MonthlyPerc = np.load(TestDataFilename_EDDI7wk_MonthlyPerc)
  TrainDatas['XYData_EDDI7wk_MonthlyPerc'] = TrainData_EDDI7wk_MonthlyPerc
  DevDatas['XYData_EDDI7wk_MonthlyPerc'] = DevData_EDDI7wk_MonthlyPerc
  TestDatas['XYData_EDDI7wk_MonthlyPerc'] = TestData_EDDI7wk_MonthlyPerc
#end of if ('EDDI_7wk' in InpLayersCombination)

if ('EDDI_8wk' in InpLayersCombination):
  TrainData_EDDI8wk_MonthlyPerc = np.load(TrainDataFilename_EDDI8wk_MonthlyPerc)
  DevData_EDDI8wk_MonthlyPerc = np.load(DevDataFilename_EDDI8wk_MonthlyPerc)
  TestData_EDDI8wk_MonthlyPerc = np.load(TestDataFilename_EDDI8wk_MonthlyPerc)
  TrainDatas['XYData_EDDI8wk_MonthlyPerc'] = TrainData_EDDI8wk_MonthlyPerc
  DevDatas['XYData_EDDI8wk_MonthlyPerc'] = DevData_EDDI8wk_MonthlyPerc
  TestDatas['XYData_EDDI8wk_MonthlyPerc'] = TestData_EDDI8wk_MonthlyPerc
#end of if ('EDDI_8wk' in InpLayersCombination)

if ('EDDI_9wk' in InpLayersCombination):
  TrainData_EDDI9wk_MonthlyPerc = np.load(TrainDataFilename_EDDI9wk_MonthlyPerc)
  DevData_EDDI9wk_MonthlyPerc = np.load(DevDataFilename_EDDI9wk_MonthlyPerc)
  TestData_EDDI9wk_MonthlyPerc = np.load(TestDataFilename_EDDI9wk_MonthlyPerc)
  TrainDatas['XYData_EDDI9wk_MonthlyPerc'] = TrainData_EDDI9wk_MonthlyPerc
  DevDatas['XYData_EDDI9wk_MonthlyPerc'] = DevData_EDDI9wk_MonthlyPerc
  TestDatas['XYData_EDDI9wk_MonthlyPerc'] = TestData_EDDI9wk_MonthlyPerc
#end of if ('EDDI_9wk' in InpLayersCombination)

if ('EDDI_10wk' in InpLayersCombination):
  TrainData_EDDI10wk_MonthlyPerc = np.load(TrainDataFilename_EDDI10wk_MonthlyPerc)
  DevData_EDDI10wk_MonthlyPerc = np.load(DevDataFilename_EDDI10wk_MonthlyPerc)
  TestData_EDDI10wk_MonthlyPerc = np.load(TestDataFilename_EDDI10wk_MonthlyPerc)
  TrainDatas['XYData_EDDI10wk_MonthlyPerc'] = TrainData_EDDI10wk_MonthlyPerc
  DevDatas['XYData_EDDI10wk_MonthlyPerc'] = DevData_EDDI10wk_MonthlyPerc
  TestDatas['XYData_EDDI10wk_MonthlyPerc'] = TestData_EDDI10wk_MonthlyPerc
#end of if ('EDDI_10wk' in InpLayersCombination)

if ('EDDI_11wk' in InpLayersCombination):
  TrainData_EDDI11wk_MonthlyPerc = np.load(TrainDataFilename_EDDI11wk_MonthlyPerc)
  DevData_EDDI11wk_MonthlyPerc = np.load(DevDataFilename_EDDI11wk_MonthlyPerc)
  TestData_EDDI11wk_MonthlyPerc = np.load(TestDataFilename_EDDI11wk_MonthlyPerc)
  TrainDatas['XYData_EDDI11wk_MonthlyPerc'] = TrainData_EDDI11wk_MonthlyPerc
  DevDatas['XYData_EDDI11wk_MonthlyPerc'] = DevData_EDDI11wk_MonthlyPerc
  TestDatas['XYData_EDDI11wk_MonthlyPerc'] = TestData_EDDI11wk_MonthlyPerc
#end of if ('EDDI_11wk' in InpLayersCombination)

if ('EDDI_12wk' in InpLayersCombination):
  TrainData_EDDI12wk_MonthlyPerc = np.load(TrainDataFilename_EDDI12wk_MonthlyPerc)
  DevData_EDDI12wk_MonthlyPerc = np.load(DevDataFilename_EDDI12wk_MonthlyPerc)
  TestData_EDDI12wk_MonthlyPerc = np.load(TestDataFilename_EDDI12wk_MonthlyPerc)
  TrainDatas['XYData_EDDI12wk_MonthlyPerc'] = TrainData_EDDI12wk_MonthlyPerc
  DevDatas['XYData_EDDI12wk_MonthlyPerc'] = DevData_EDDI12wk_MonthlyPerc
  TestDatas['XYData_EDDI12wk_MonthlyPerc'] = TestData_EDDI12wk_MonthlyPerc
#end of if ('EDDI_12wk' in InpLayersCombination)

if ('EDDI_1mn' in InpLayersCombination):
  TrainData_EDDI1mn_MonthlyPerc = np.load(TrainDataFilename_EDDI1mn_MonthlyPerc)
  DevData_EDDI1mn_MonthlyPerc = np.load(DevDataFilename_EDDI1mn_MonthlyPerc)
  TestData_EDDI1mn_MonthlyPerc = np.load(TestDataFilename_EDDI1mn_MonthlyPerc)
  TrainDatas['XYData_EDDI1mn_MonthlyPerc'] = TrainData_EDDI1mn_MonthlyPerc
  DevDatas['XYData_EDDI1mn_MonthlyPerc'] = DevData_EDDI1mn_MonthlyPerc
  TestDatas['XYData_EDDI1mn_MonthlyPerc'] = TestData_EDDI1mn_MonthlyPerc
#end of if ('EDDI_1mn' in InpLayersCombination)

if ('EDDI_2mn' in InpLayersCombination):
  TrainData_EDDI2mn_MonthlyPerc = np.load(TrainDataFilename_EDDI2mn_MonthlyPerc)
  DevData_EDDI2mn_MonthlyPerc = np.load(DevDataFilename_EDDI2mn_MonthlyPerc)
  TestData_EDDI2mn_MonthlyPerc = np.load(TestDataFilename_EDDI2mn_MonthlyPerc)
  TrainDatas['XYData_EDDI2mn_MonthlyPerc'] = TrainData_EDDI2mn_MonthlyPerc
  DevDatas['XYData_EDDI2mn_MonthlyPerc'] = DevData_EDDI2mn_MonthlyPerc
  TestDatas['XYData_EDDI2mn_MonthlyPerc'] = TestData_EDDI2mn_MonthlyPerc
#end of if ('EDDI_2mn' in InpLayersCombination)

if ('EDDI_3mn' in InpLayersCombination):
  TrainData_EDDI3mn_MonthlyPerc = np.load(TrainDataFilename_EDDI3mn_MonthlyPerc)
  DevData_EDDI3mn_MonthlyPerc = np.load(DevDataFilename_EDDI3mn_MonthlyPerc)
  TestData_EDDI3mn_MonthlyPerc = np.load(TestDataFilename_EDDI3mn_MonthlyPerc)
  TrainDatas['XYData_EDDI3mn_MonthlyPerc'] = TrainData_EDDI3mn_MonthlyPerc
  DevDatas['XYData_EDDI3mn_MonthlyPerc'] = DevData_EDDI3mn_MonthlyPerc
  TestDatas['XYData_EDDI3mn_MonthlyPerc'] = TestData_EDDI3mn_MonthlyPerc
#end of if ('EDDI_3mn' in InpLayersCombination)

if ('EDDI_4mn' in InpLayersCombination):
  TrainData_EDDI4mn_MonthlyPerc = np.load(TrainDataFilename_EDDI4mn_MonthlyPerc)
  DevData_EDDI4mn_MonthlyPerc = np.load(DevDataFilename_EDDI4mn_MonthlyPerc)
  TestData_EDDI4mn_MonthlyPerc = np.load(TestDataFilename_EDDI4mn_MonthlyPerc)
  TrainDatas['XYData_EDDI4mn_MonthlyPerc'] = TrainData_EDDI4mn_MonthlyPerc
  DevDatas['XYData_EDDI4mn_MonthlyPerc'] = DevData_EDDI4mn_MonthlyPerc
  TestDatas['XYData_EDDI4mn_MonthlyPerc'] = TestData_EDDI4mn_MonthlyPerc
#end of if ('EDDI_4mn' in InpLayersCombination)

if ('EDDI_5mn' in InpLayersCombination):
  TrainData_EDDI5mn_MonthlyPerc = np.load(TrainDataFilename_EDDI5mn_MonthlyPerc)
  DevData_EDDI5mn_MonthlyPerc = np.load(DevDataFilename_EDDI5mn_MonthlyPerc)
  TestData_EDDI5mn_MonthlyPerc = np.load(TestDataFilename_EDDI5mn_MonthlyPerc)
  TrainDatas['XYData_EDDI5mn_MonthlyPerc'] = TrainData_EDDI5mn_MonthlyPerc
  DevDatas['XYData_EDDI5mn_MonthlyPerc'] = DevData_EDDI5mn_MonthlyPerc
  TestDatas['XYData_EDDI5mn_MonthlyPerc'] = TestData_EDDI5mn_MonthlyPerc
#end of if ('EDDI_5mn' in InpLayersCombination)

if ('EDDI_6mn' in InpLayersCombination):
  TrainData_EDDI6mn_MonthlyPerc = np.load(TrainDataFilename_EDDI6mn_MonthlyPerc)
  DevData_EDDI6mn_MonthlyPerc = np.load(DevDataFilename_EDDI6mn_MonthlyPerc)
  TestData_EDDI6mn_MonthlyPerc = np.load(TestDataFilename_EDDI6mn_MonthlyPerc)
  TrainDatas['XYData_EDDI6mn_MonthlyPerc'] = TrainData_EDDI6mn_MonthlyPerc
  DevDatas['XYData_EDDI6mn_MonthlyPerc'] = DevData_EDDI6mn_MonthlyPerc
  TestDatas['XYData_EDDI6mn_MonthlyPerc'] = TestData_EDDI6mn_MonthlyPerc
#end of if ('EDDI_6mn' in InpLayersCombination)

if ('EDDI_7mn' in InpLayersCombination):
  TrainData_EDDI7mn_MonthlyPerc = np.load(TrainDataFilename_EDDI7mn_MonthlyPerc)
  DevData_EDDI7mn_MonthlyPerc = np.load(DevDataFilename_EDDI7mn_MonthlyPerc)
  TestData_EDDI7mn_MonthlyPerc = np.load(TestDataFilename_EDDI7mn_MonthlyPerc)
  TrainDatas['XYData_EDDI7mn_MonthlyPerc'] = TrainData_EDDI7mn_MonthlyPerc
  DevDatas['XYData_EDDI7mn_MonthlyPerc'] = DevData_EDDI7mn_MonthlyPerc
  TestDatas['XYData_EDDI7mn_MonthlyPerc'] = TestData_EDDI7mn_MonthlyPerc
#end of if ('EDDI_7mn' in InpLayersCombination)

if ('EDDI_8mn' in InpLayersCombination):
  TrainData_EDDI8mn_MonthlyPerc = np.load(TrainDataFilename_EDDI8mn_MonthlyPerc)
  DevData_EDDI8mn_MonthlyPerc = np.load(DevDataFilename_EDDI8mn_MonthlyPerc)
  TestData_EDDI8mn_MonthlyPerc = np.load(TestDataFilename_EDDI8mn_MonthlyPerc)
  TrainDatas['XYData_EDDI8mn_MonthlyPerc'] = TrainData_EDDI8mn_MonthlyPerc
  DevDatas['XYData_EDDI8mn_MonthlyPerc'] = DevData_EDDI8mn_MonthlyPerc
  TestDatas['XYData_EDDI8mn_MonthlyPerc'] = TestData_EDDI8mn_MonthlyPerc
#end of if ('EDDI_8mn' in InpLayersCombination)

if ('EDDI_9mn' in InpLayersCombination):
  TrainData_EDDI9mn_MonthlyPerc = np.load(TrainDataFilename_EDDI9mn_MonthlyPerc)
  DevData_EDDI9mn_MonthlyPerc = np.load(DevDataFilename_EDDI9mn_MonthlyPerc)
  TestData_EDDI9mn_MonthlyPerc = np.load(TestDataFilename_EDDI9mn_MonthlyPerc)
  TrainDatas['XYData_EDDI9mn_MonthlyPerc'] = TrainData_EDDI9mn_MonthlyPerc
  DevDatas['XYData_EDDI9mn_MonthlyPerc'] = DevData_EDDI9mn_MonthlyPerc
  TestDatas['XYData_EDDI9mn_MonthlyPerc'] = TestData_EDDI9mn_MonthlyPerc
#end of if ('EDDI_9mn' in InpLayersCombination)

if ('EDDI_10mn' in InpLayersCombination):
  TrainData_EDDI10mn_MonthlyPerc = np.load(TrainDataFilename_EDDI10mn_MonthlyPerc)
  DevData_EDDI10mn_MonthlyPerc = np.load(DevDataFilename_EDDI10mn_MonthlyPerc)
  TestData_EDDI10mn_MonthlyPerc = np.load(TestDataFilename_EDDI10mn_MonthlyPerc)
  TrainDatas['XYData_EDDI10mn_MonthlyPerc'] = TrainData_EDDI10mn_MonthlyPerc
  DevDatas['XYData_EDDI10mn_MonthlyPerc'] = DevData_EDDI10mn_MonthlyPerc
  TestDatas['XYData_EDDI10mn_MonthlyPerc'] = TestData_EDDI10mn_MonthlyPerc
#end of if ('EDDI_10mn' in InpLayersCombination)

if ('EDDI_11mn' in InpLayersCombination):
  TrainData_EDDI11mn_MonthlyPerc = np.load(TrainDataFilename_EDDI11mn_MonthlyPerc)
  DevData_EDDI11mn_MonthlyPerc = np.load(DevDataFilename_EDDI11mn_MonthlyPerc)
  TestData_EDDI11mn_MonthlyPerc = np.load(TestDataFilename_EDDI11mn_MonthlyPerc)
  TrainDatas['XYData_EDDI11mn_MonthlyPerc'] = TrainData_EDDI11mn_MonthlyPerc
  DevDatas['XYData_EDDI11mn_MonthlyPerc'] = DevData_EDDI11mn_MonthlyPerc
  TestDatas['XYData_EDDI11mn_MonthlyPerc'] = TestData_EDDI11mn_MonthlyPerc
#end of if ('EDDI_11mn' in InpLayersCombination)

if ('EDDI_12mn' in InpLayersCombination):
  TrainData_EDDI12mn = np.load(TrainDataFilename_EDDI12mn)
  DevData_EDDI12mn = np.load(DevDataFilename_EDDI12mn)
  TestData_EDDI12mn = np.load(TestDataFilename_EDDI12mn)
  TrainDatas['XYData_EDDI12mn'] = TrainData_EDDI12mn
  DevDatas['XYData_EDDI12mn'] = DevData_EDDI12mn
  TestDatas['XYData_EDDI12mn'] = TestData_EDDI12mn
#end of if ('EDDI_12mn' in InpLayersCombination)

#if ( ('NLDAS2_1mSM_Mosaic' in InpLayersCombination) or
#     ('NLDAS2_1mSM_Noah' in InpLayersCombination) or
#     ('NLDAS2_1mSM_SAC' in InpLayersCombination) or
#     ('NLDAS2_1mSM_VIC' in InpLayersCombination) ):
#  TrainData_NLDAS_2_1mSM_MonthlyPerc = np.load(TrainDataFilename_NLDAS_2_1mSM_MonthlyPerc)
#  DevData_NLDAS_2_1mSM_MonthlyPerc = np.load(DevDataFilename_NLDAS_2_1mSM_MonthlyPerc)
#  TestData_NLDAS_2_1mSM_MonthlyPerc = np.load(TestDataFilename_NLDAS_2_1mSM_MonthlyPerc)
#  TrainDatas['XYData_NLDAS_2_1mSM_MonthlyPerc'] = TrainData_NLDAS_2_1mSM_MonthlyPerc
#  DevDatas['XYData_NLDAS_2_1mSM_MonthlyPerc'] = DevData_NLDAS_2_1mSM_MonthlyPerc
#  TestDatas['XYData_NLDAS_2_1mSM_MonthlyPerc'] = TestData_NLDAS_2_1mSM_MonthlyPerc
##end of if ( ('NLDAS2_1mSM_Mosaic' in InpLayersCombination) or...

if ( ('NLDAS2D_1MSM_Mosaic' in InpLayersCombination) or
     ('NLDAS2D_1MSM_Noah' in InpLayersCombination) or
     ('NLDAS2D_1MSM_SAC' in InpLayersCombination) or
     ('NLDAS2D_1MSM_VIC' in InpLayersCombination) or
     ('NLDAS2D_TCSM_Mosaic' in InpLayersCombination) or
     ('NLDAS2D_TCSM_Noah' in InpLayersCombination) or
     ('NLDAS2D_TCSM_SAC' in InpLayersCombination) or
     ('NLDAS2D_TCSM_VIC' in InpLayersCombination) or
     ('NLDAS2D_EVAP_Mosaic' in InpLayersCombination) or
     ('NLDAS2D_EVAP_Noah' in InpLayersCombination) or
     ('NLDAS2D_EVAP_SAC' in InpLayersCombination) or
     ('NLDAS2D_EVAP_VIC' in InpLayersCombination) or
     ('NLDAS2D_SWE_Mosaic' in InpLayersCombination) or
     ('NLDAS2D_SWE_Noah' in InpLayersCombination) or
     ('NLDAS2D_SWE_SAC' in InpLayersCombination) or
     ('NLDAS2D_SWE_VIC' in InpLayersCombination) or
     ('NLDAS2D_RUN_Mosaic' in InpLayersCombination) or
     ('NLDAS2D_RUN_Noah' in InpLayersCombination) or
     ('NLDAS2D_RUN_SAC' in InpLayersCombination) or
     ('NLDAS2D_RUN_VIC' in InpLayersCombination) or
     ('NLDAS2D_STRMH04_Mosaic' in InpLayersCombination) or
     ('NLDAS2D_STRMH04_Noah' in InpLayersCombination) or
     ('NLDAS2D_STRMH04_SAC' in InpLayersCombination) or
     ('NLDAS2D_STRMH04_VIC' in InpLayersCombination) ):
  TrainData_NLDAS_2_daily = np.load(TrainDataFilename_NLDAS_2_daily)
  DevData_NLDAS_2_daily = np.load(DevDataFilename_NLDAS_2_daily)
  TestData_NLDAS_2_daily = np.load(TestDataFilename_NLDAS_2_daily)
  TrainDatas['XYData_NLDAS_2_daily'] = TrainData_NLDAS_2_daily
  DevDatas['XYData_NLDAS_2_daily'] = DevData_NLDAS_2_daily
  TestDatas['XYData_NLDAS_2_daily'] = TestData_NLDAS_2_daily
#end of if ( ('NLDAS2D_1MSM_Mosaic' in InpLayersCombination) or...

if ('VegDRI' in InpLayersCombination):
  TrainData_VegDRI_MonthlyPerc = np.load(TrainDataFilename_VegDRI_MonthlyPerc)
  DevData_VegDRI_MonthlyPerc = np.load(DevDataFilename_VegDRI_MonthlyPerc)
  TestData_VegDRI_MonthlyPerc = np.load(TestDataFilename_VegDRI_MonthlyPerc)
  TrainDatas['XYData_VegDRI_MonthlyPerc'] = TrainData_VegDRI_MonthlyPerc
  DevDatas['XYData_VegDRI_MonthlyPerc'] = DevData_VegDRI_MonthlyPerc
  TestDatas['XYData_VegDRI_MonthlyPerc'] = TestData_VegDRI_MonthlyPerc
#end of if ('VegDRI' in InpLayersCombination)

if ('QuickDRI' in InpLayersCombination):
  TrainData_QuickDRI_MonthlyPerc = np.load(TrainDataFilename_QuickDRI_MonthlyPerc)
  DevData_QuickDRI_MonthlyPerc = np.load(DevDataFilename_QuickDRI_MonthlyPerc)
  TestData_QuickDRI_MonthlyPerc = np.load(TestDataFilename_QuickDRI_MonthlyPerc)
  TrainDatas['XYData_QuickDRI_MonthlyPerc'] = TrainData_QuickDRI_MonthlyPerc
  DevDatas['XYData_QuickDRI_MonthlyPerc'] = DevData_QuickDRI_MonthlyPerc
  TestDatas['XYData_QuickDRI_MonthlyPerc'] = TestData_QuickDRI_MonthlyPerc
#end of if ('QuickDRI' in InpLayersCombination)

#if ('ESI' in InpLayersCombination):
#  TrainData_ESI_MonthlyPerc = np.load(TrainDataFilename_ESI_MonthlyPerc)
#  DevData_ESI_MonthlyPerc = np.load(DevDataFilename_ESI_MonthlyPerc)
#  TestData_ESI_MonthlyPerc = np.load(TestDataFilename_ESI_MonthlyPerc)
#  TrainDatas['XYData_ESI_MonthlyPerc'] = TrainData_ESI_MonthlyPerc
#  DevDatas['XYData_ESI_MonthlyPerc'] = DevData_ESI_MonthlyPerc
#  TestDatas['XYData_ESI_MonthlyPerc'] = TestData_ESI_MonthlyPerc
##end of if ('ESI' in InpLayersCombination)

if ( ('ESI_4wk' in InpLayersCombination) or
     ('ESI_12wk' in InpLayersCombination) ):
  TrainData_ESImultiWeek_MonthlyPerc = np.load(TrainDataFilename_ESImultiWeek_MonthlyPerc)
  DevData_ESImultiWeek_MonthlyPerc = np.load(DevDataFilename_ESImultiWeek_MonthlyPerc)
  TestData_ESImultiWeek_MonthlyPerc = np.load(TestDataFilename_ESImultiWeek_MonthlyPerc)
  TrainDatas['XYData_ESImultiWeek_MonthlyPerc'] = TrainData_ESImultiWeek_MonthlyPerc
  DevDatas['XYData_ESImultiWeek_MonthlyPerc'] = DevData_ESImultiWeek_MonthlyPerc
  TestDatas['XYData_ESImultiWeek_MonthlyPerc'] = TestData_ESImultiWeek_MonthlyPerc
#end of if ('ESI' in InpLayersCombination)

#if ( ('SPI_1_month' in InpLayersCombination) or
#     ('SPI_2_month' in InpLayersCombination) or
#     ('SPI_3_month' in InpLayersCombination) or
#     ('SPI_6_month' in InpLayersCombination) or
#     ('SPI_9_month' in InpLayersCombination) ):
#  TrainData_SPI_MonthlyPerc = np.load(TrainDataFilename_SPI_MonthlyPerc)
#  DevData_SPI_MonthlyPerc = np.load(DevDataFilename_SPI_MonthlyPerc)
#  TestData_SPI_MonthlyPerc = np.load(TestDataFilename_SPI_MonthlyPerc)
#  TrainDatas['XYData_SPI_MonthlyPerc'] = TrainData_SPI_MonthlyPerc
#  DevDatas['XYData_SPI_MonthlyPerc'] = DevData_SPI_MonthlyPerc
#  TestDatas['XYData_SPI_MonthlyPerc'] = TestData_SPI_MonthlyPerc
##end of if ( ('SPI_1_month' in InpLayersCombination) or...
#
#if ( ('SPI_12_month' in InpLayersCombination) or
#     ('SPI_24_month' in InpLayersCombination) ):
#  TrainData_SPI_OverallPerc = np.load(TrainDataFilename_SPI_OverallPerc)
#  DevData_SPI_OverallPerc = np.load(DevDataFilename_SPI_OverallPerc)
#  TestData_SPI_OverallPerc = np.load(TestDataFilename_SPI_OverallPerc)
#  TrainDatas['XYData_SPI_OverallPerc'] = TrainData_SPI_OverallPerc
#  DevDatas['XYData_SPI_OverallPerc'] = DevData_SPI_OverallPerc
#  TestDatas['XYData_SPI_OverallPerc'] = TestData_SPI_OverallPerc
##end of if ( ('SPI_12_month' in InpLayersCombination) or...

if ( ('SNODAS' in InpLayersCombination) or
     ('ESA_CCI' in InpLayersCombination) ):
  TrainData_SNODASnESACCI = np.load(TrainDataFilename_SNODASnESACCI)
  DevData_SNODASnESACCI = np.load(DevDataFilename_SNODASnESACCI)
  TestData_SNODASnESACCI = np.load(TestDataFilename_SNODASnESACCI)
  TrainDatas['XYData_SNODASnESACCI'] = TrainData_SNODASnESACCI
  DevDatas['XYData_SNODASnESACCI'] = DevData_SNODASnESACCI
  TestDatas['XYData_SNODASnESACCI'] = TestData_SNODASnESACCI
#end of if ( ('SNODAS' in InpLayersCombination) or...

if ( ('IMERG_01' in InpLayersCombination) or
     ('IMERG_02' in InpLayersCombination) or
     ('IMERG_03' in InpLayersCombination) or
     ('IMERG_06' in InpLayersCombination) or
     ('IMERG_09' in InpLayersCombination) or
     ('IMERG_12' in InpLayersCombination) or
     ('IMERG_24' in InpLayersCombination) or
     ('IMERG_36' in InpLayersCombination) or
     ('IMERG_48' in InpLayersCombination) or
     ('IMERG_60' in InpLayersCombination) or
     ('IMERG_72' in InpLayersCombination) ):
  TrainData_IMERG = np.load(TrainDataFilename_IMERG)
  DevData_IMERG = np.load(DevDataFilename_IMERG)
  TestData_IMERG = np.load(TestDataFilename_IMERG)
  TrainDatas['XYData_IMERG'] = TrainData_IMERG
  DevDatas['XYData_IMERG'] = DevData_IMERG
  TestDatas['XYData_IMERG'] = TestData_IMERG
#end of if ( ('IMERG_01' in InpLayersCombination) or...

if ( ('SmNDVI_BlendedVHP' in InpLayersCombination) or
     ('TCI_BlendedVHP' in InpLayersCombination) or
     ('VCI_BlendedVHP' in InpLayersCombination) or
     ('VHI_BlendedVHP' in InpLayersCombination) ):
  TrainData_BlendedVHP_MonthlyPerc = np.load(TrainDataFilename_BlendedVHP_MonthlyPerc)
  DevData_BlendedVHP_MonthlyPerc = np.load(DevDataFilename_BlendedVHP_MonthlyPerc)
  TestData_BlendedVHP_MonthlyPerc = np.load(TestDataFilename_BlendedVHP_MonthlyPerc)
  TrainDatas['XYData_BlendedVHP_MonthlyPerc'] = TrainData_BlendedVHP_MonthlyPerc
  DevDatas['XYData_BlendedVHP_MonthlyPerc'] = DevData_BlendedVHP_MonthlyPerc
  TestDatas['XYData_BlendedVHP_MonthlyPerc'] = TestData_BlendedVHP_MonthlyPerc
#end of if ('SmNDVI_BlendedVHP' in InpLayersCombination) or...

if ('GlobSnow3' in InpLayersCombination):
  TrainData_GlobSnow3_OverallPerc = np.load(TrainDataFilename_GlobSnow3_OverallPerc)
  DevData_GlobSnow3_OverallPerc = np.load(DevDataFilename_GlobSnow3_OverallPerc)
  TestData_GlobSnow3_OverallPerc = np.load(TestDataFilename_GlobSnow3_OverallPerc)
  TrainDatas['XYData_GlobSnow3_OverallPerc'] = TrainData_GlobSnow3_OverallPerc
  DevDatas['XYData_GlobSnow3_OverallPerc'] = DevData_GlobSnow3_OverallPerc
  TestDatas['XYData_GlobSnow3_OverallPerc'] = TestData_GlobSnow3_OverallPerc
#end of if ('GlobSnow3' in InpLayersCombination)

if IfSpatialSubDomain:

  ClimDivShp = gpd.read_file(ClimDivShpFile)
  CLIMDIV_SortedArray_FrmShpFile = np.array(sorted(ClimDivShp.CLIMDIV.values))

  ClimDivShp_Sub = gpd.read_file(ClimDivShpFile_Sub)
  CLIMDIV_SortedArray_FrmShpFile_Sub = np.array(sorted(ClimDivShp_Sub.CLIMDIV.values))

  WhichCols = np.where(np.isin(CLIMDIV_SortedArray_FrmShpFile, CLIMDIV_SortedArray_FrmShpFile_Sub))

else:

  WhichCols = None

#end of if IfSpatialSubDomain

def GetInpAndTargArraysFromFile(XYDatas, InpLayersCombination, IfSpatialSubDomain, WhichCols, IfMakeTargetBinary, IfIncludeD0AsDrought, WhichSeason, Event_BeginDateVecList, Event_EndDateVecList):

  XYData_USDM_New = XYDatas['XYData_USDM_New']

#if ( ('Z_index' in InpLayersCombination) or
#     ('Z_index_60_month' in InpLayersCombination) or
#     ('CPC_soil_moisture' in InpLayersCombination) ):
  XYData = XYDatas['XYData']
#end of if ( ('PMDI' in InpLayersCombination) or....

  if ( ('PMDI' in InpLayersCombination) or
       ('PHDI' in InpLayersCombination) ):
    XYData_OverallPerc = XYDatas['XYData_OverallPerc']
  #end of if ( ('PMDI' in InpLayersCombination) or....

  if ( ('prcp_01_nCG' in InpLayersCombination) or
       ('prcp_02_nCG' in InpLayersCombination) or
       ('prcp_03_nCG' in InpLayersCombination) or
       ('prcp_06_nCG' in InpLayersCombination) or
       ('prcp_09_nCG' in InpLayersCombination) or
       ('prcp_12_nCG' in InpLayersCombination) or
       ('prcp_24_nCG' in InpLayersCombination) or
       ('prcp_36_nCG' in InpLayersCombination) or
       ('prcp_48_nCG' in InpLayersCombination) or
       ('prcp_60_nCG' in InpLayersCombination) or
       ('prcp_72_nCG' in InpLayersCombination) or
       ('SPI_gamma_01_nCG' in InpLayersCombination) or
       ('SPI_gamma_02_nCG' in InpLayersCombination) or
       ('SPI_gamma_03_nCG' in InpLayersCombination) or
       ('SPI_gamma_06_nCG' in InpLayersCombination) or
       ('SPI_gamma_09_nCG' in InpLayersCombination) or
       ('SPI_gamma_12_nCG' in InpLayersCombination) or
       ('SPI_gamma_24_nCG' in InpLayersCombination) or
       ('SPI_gamma_36_nCG' in InpLayersCombination) or
       ('SPI_gamma_48_nCG' in InpLayersCombination) or
       ('SPI_gamma_60_nCG' in InpLayersCombination) or
       ('SPI_gamma_72_nCG' in InpLayersCombination) or
       ('SPEI_pear_01_nCG' in InpLayersCombination) or
       ('SPEI_pear_02_nCG' in InpLayersCombination) or
       ('SPEI_pear_03_nCG' in InpLayersCombination) or
       ('SPEI_pear_06_nCG' in InpLayersCombination) or
       ('SPEI_pear_09_nCG' in InpLayersCombination) or
       ('SPEI_pear_12_nCG' in InpLayersCombination) or
       ('SPEI_pear_24_nCG' in InpLayersCombination) or
       ('SPEI_pear_36_nCG' in InpLayersCombination) or
       ('SPEI_pear_48_nCG' in InpLayersCombination) or
       ('SPEI_pear_60_nCG' in InpLayersCombination) or
       ('SPEI_pear_72_nCG' in InpLayersCombination) or
       ('tavg_01_nCG' in InpLayersCombination) or
       ('tmax_01_nCG' in InpLayersCombination) ):
    XYData_AllnCG = XYDatas['XYData_AllnCG']
  #end of if ( ('prcp_01_nCG' in InpLayersCombination) or...

  if ('GRACE_DA_gw' in InpLayersCombination):
    XYData_GRACEDA = XYDatas['XYData_GRACEDA']
  #end of if ('GRACE_DA_gw' in InpLayersCombination)

  if ( ('GRACE_DA_sfsm' in InpLayersCombination) or
       ('GRACE_DA_rzsm' in InpLayersCombination) ):
    XYData_GRACEDA_MonthlyPerc = XYDatas['XYData_GRACEDA_MonthlyPerc']
  #end of if ( ('GRACE_DA_sfsm' in InpLayersCombination) or...
  
  if ('EDDI_1wk' in InpLayersCombination):
    XYData_EDDI1wk_MonthlyPerc = XYDatas['XYData_EDDI1wk_MonthlyPerc']
  #end of if ('EDDI_1wk' in InpLayersCombination)

  if ('EDDI_2wk' in InpLayersCombination):
    XYData_EDDI2wk_MonthlyPerc = XYDatas['XYData_EDDI2wk_MonthlyPerc']
  #end of if ('EDDI_2wk' in InpLayersCombination)

  if ('EDDI_3wk' in InpLayersCombination):
    XYData_EDDI3wk_MonthlyPerc = XYDatas['XYData_EDDI3wk_MonthlyPerc']
  #end of if ('EDDI_3wk' in InpLayersCombination)

  if ('EDDI_4wk' in InpLayersCombination):
    XYData_EDDI4wk_MonthlyPerc = XYDatas['XYData_EDDI4wk_MonthlyPerc']
  #end of if ('EDDI_4wk' in InpLayersCombination)

  if ('EDDI_5wk' in InpLayersCombination):
    XYData_EDDI5wk_MonthlyPerc = XYDatas['XYData_EDDI5wk_MonthlyPerc']
  #end of if ('EDDI_5wk' in InpLayersCombination)

  if ('EDDI_6wk' in InpLayersCombination):
    XYData_EDDI6wk_MonthlyPerc = XYDatas['XYData_EDDI6wk_MonthlyPerc']
  #end of if ('EDDI_6wk' in InpLayersCombination)

  if ('EDDI_7wk' in InpLayersCombination):
    XYData_EDDI7wk_MonthlyPerc = XYDatas['XYData_EDDI7wk_MonthlyPerc']
  #end of if ('EDDI_7wk' in InpLayersCombination)

  if ('EDDI_8wk' in InpLayersCombination):
    XYData_EDDI8wk_MonthlyPerc = XYDatas['XYData_EDDI8wk_MonthlyPerc']
  #end of if ('EDDI_8wk' in InpLayersCombination)

  if ('EDDI_9wk' in InpLayersCombination):
    XYData_EDDI9wk_MonthlyPerc = XYDatas['XYData_EDDI9wk_MonthlyPerc']
  #end of if ('EDDI_9wk' in InpLayersCombination)

  if ('EDDI_10wk' in InpLayersCombination):
    XYData_EDDI10wk_MonthlyPerc = XYDatas['XYData_EDDI10wk_MonthlyPerc']
  #end of if ('EDDI_10wk' in InpLayersCombination)

  if ('EDDI_11wk' in InpLayersCombination):
    XYData_EDDI11wk_MonthlyPerc = XYDatas['XYData_EDDI11wk_MonthlyPerc']
  #end of if ('EDDI_11wk' in InpLayersCombination)

  if ('EDDI_12wk' in InpLayersCombination):
    XYData_EDDI12wk_MonthlyPerc = XYDatas['XYData_EDDI12wk_MonthlyPerc']
  #end of if ('EDDI_12wk' in InpLayersCombination)

  if ('EDDI_1mn' in InpLayersCombination):
    XYData_EDDI1mn_MonthlyPerc = XYDatas['XYData_EDDI1mn_MonthlyPerc']
  #end of if ('EDDI_1mn' in InpLayersCombination)

  if ('EDDI_2mn' in InpLayersCombination):
    XYData_EDDI2mn_MonthlyPerc = XYDatas['XYData_EDDI2mn_MonthlyPerc']
  #end of if ('EDDI_2mn' in InpLayersCombination)

  if ('EDDI_3mn' in InpLayersCombination):
    XYData_EDDI3mn_MonthlyPerc = XYDatas['XYData_EDDI3mn_MonthlyPerc']
  #end of if ('EDDI_3mn' in InpLayersCombination)

  if ('EDDI_4mn' in InpLayersCombination):
    XYData_EDDI4mn_MonthlyPerc = XYDatas['XYData_EDDI4mn_MonthlyPerc']
  #end of if ('EDDI_4mn' in InpLayersCombination)

  if ('EDDI_5mn' in InpLayersCombination):
    XYData_EDDI5mn_MonthlyPerc = XYDatas['XYData_EDDI5mn_MonthlyPerc']
  #end of if ('EDDI_5mn' in InpLayersCombination)

  if ('EDDI_6mn' in InpLayersCombination):
    XYData_EDDI6mn_MonthlyPerc = XYDatas['XYData_EDDI6mn_MonthlyPerc']
  #end of if ('EDDI_6mn' in InpLayersCombination)

  if ('EDDI_7mn' in InpLayersCombination):
    XYData_EDDI7mn_MonthlyPerc = XYDatas['XYData_EDDI7mn_MonthlyPerc']
  #end of if ('EDDI_7mn' in InpLayersCombination)

  if ('EDDI_8mn' in InpLayersCombination):
    XYData_EDDI8mn_MonthlyPerc = XYDatas['XYData_EDDI8mn_MonthlyPerc']
  #end of if ('EDDI_8mn' in InpLayersCombination)

  if ('EDDI_9mn' in InpLayersCombination):
    XYData_EDDI9mn_MonthlyPerc = XYDatas['XYData_EDDI9mn_MonthlyPerc']
  #end of if ('EDDI_9mn' in InpLayersCombination)

  if ('EDDI_10mn' in InpLayersCombination):
    XYData_EDDI10mn_MonthlyPerc = XYDatas['XYData_EDDI10mn_MonthlyPerc']
  #end of if ('EDDI_10mn' in InpLayersCombination)

  if ('EDDI_11mn' in InpLayersCombination):
    XYData_EDDI11mn_MonthlyPerc = XYDatas['XYData_EDDI11mn_MonthlyPerc']
  #end of if ('EDDI_11mn' in InpLayersCombination)

  if ('EDDI_12mn' in InpLayersCombination):
    XYData_EDDI12mn = XYDatas['XYData_EDDI12mn']
  #end of if ('EDDI_12mn' in InpLayersCombination)

#  if ( ('NLDAS2_1mSM_Mosaic' in InpLayersCombination) or
#       ('NLDAS2_1mSM_Noah' in InpLayersCombination) or
#       ('NLDAS2_1mSM_SAC' in InpLayersCombination) or
#       ('NLDAS2_1mSM_VIC' in InpLayersCombination) ):
#    XYData_NLDAS_2_1mSM_MonthlyPerc = XYDatas['XYData_NLDAS_2_1mSM_MonthlyPerc']
#  #end of if ( ('NLDAS2_1mSM_Mosaic' in InpLayersCombination) or...

  if ( ('NLDAS2D_1MSM_Mosaic' in InpLayersCombination) or
       ('NLDAS2D_1MSM_Noah' in InpLayersCombination) or
       ('NLDAS2D_1MSM_SAC' in InpLayersCombination) or
       ('NLDAS2D_1MSM_VIC' in InpLayersCombination) or
       ('NLDAS2D_TCSM_Mosaic' in InpLayersCombination) or
       ('NLDAS2D_TCSM_Noah' in InpLayersCombination) or
       ('NLDAS2D_TCSM_SAC' in InpLayersCombination) or
       ('NLDAS2D_TCSM_VIC' in InpLayersCombination) or
       ('NLDAS2D_EVAP_Mosaic' in InpLayersCombination) or
       ('NLDAS2D_EVAP_Noah' in InpLayersCombination) or
       ('NLDAS2D_EVAP_SAC' in InpLayersCombination) or
       ('NLDAS2D_EVAP_VIC' in InpLayersCombination) or
       ('NLDAS2D_SWE_Mosaic' in InpLayersCombination) or
       ('NLDAS2D_SWE_Noah' in InpLayersCombination) or
       ('NLDAS2D_SWE_SAC' in InpLayersCombination) or
       ('NLDAS2D_SWE_VIC' in InpLayersCombination) or
       ('NLDAS2D_RUN_Mosaic' in InpLayersCombination) or
       ('NLDAS2D_RUN_Noah' in InpLayersCombination) or
       ('NLDAS2D_RUN_SAC' in InpLayersCombination) or
       ('NLDAS2D_RUN_VIC' in InpLayersCombination) or
       ('NLDAS2D_STRMH04_Mosaic' in InpLayersCombination) or
       ('NLDAS2D_STRMH04_Noah' in InpLayersCombination) or
       ('NLDAS2D_STRMH04_SAC' in InpLayersCombination) or
       ('NLDAS2D_STRMH04_VIC' in InpLayersCombination) ):
      XYData_NLDAS_2_daily = XYDatas['XYData_NLDAS_2_daily']
  #end of if ( ('NLDAS2D_1MSM_Mosaic' in InpLayersCombination) or...

  if ('VegDRI' in InpLayersCombination):
    XYData_VegDRI_MonthlyPerc = XYDatas['XYData_VegDRI_MonthlyPerc']
  #end of if ('VegDRI' in InpLayersCombination)
  
  if ('QuickDRI' in InpLayersCombination):
    XYData_QuickDRI_MonthlyPerc = XYDatas['XYData_QuickDRI_MonthlyPerc']
  #end of if ('QuickDRI' in InpLayersCombination)
  
#  if ('ESI' in InpLayersCombination):
#    XYData_ESI_MonthlyPerc = XYDatas['XYData_ESI_MonthlyPerc']
#  #end of if ('ESI' in InpLayersCombination)

  if ( ('ESI_4wk' in InpLayersCombination) or
       ('ESI_12wk' in InpLayersCombination) ):
    XYData_ESImultiWeek_MonthlyPerc = XYDatas['XYData_ESImultiWeek_MonthlyPerc']
  #end of if ('ESI_4wk' in InpLayersCombination)
  
#  if ( ('SPI_1_month' in InpLayersCombination) or
#       ('SPI_2_month' in InpLayersCombination) or
#       ('SPI_3_month' in InpLayersCombination) or
#       ('SPI_6_month' in InpLayersCombination) or
#       ('SPI_9_month' in InpLayersCombination) ):
#    XYData_SPI_MonthlyPerc = XYDatas['XYData_SPI_MonthlyPerc']
#  #end of if ( ('SPI_1_month' in InpLayersCombination) or...
#  
#  if ( ('SPI_12_month' in InpLayersCombination) or
#       ('SPI_24_month' in InpLayersCombination) ):
#    XYData_SPI_OverallPerc = XYDatas['XYData_SPI_OverallPerc']
#  #end of if ( ('SPI_12_month' in InpLayersCombination) or...

  if ( ('SNODAS' in InpLayersCombination) or
       ('ESA_CCI' in InpLayersCombination) ):
    XYData_SNODASnESACCI = XYDatas['XYData_SNODASnESACCI']
  #end of if ( ('SNODAS' in InpLayersCombination) or...

  if ( ('IMERG_01' in InpLayersCombination) or
       ('IMERG_02' in InpLayersCombination) or
       ('IMERG_03' in InpLayersCombination) or
       ('IMERG_06' in InpLayersCombination) or
       ('IMERG_09' in InpLayersCombination) or
       ('IMERG_12' in InpLayersCombination) or
       ('IMERG_24' in InpLayersCombination) or
       ('IMERG_36' in InpLayersCombination) or
       ('IMERG_48' in InpLayersCombination) or
       ('IMERG_60' in InpLayersCombination) or
       ('IMERG_72' in InpLayersCombination) ):
    XYData_IMERG = XYDatas['XYData_IMERG']
  #end of if ( ('IMERG_01' in InpLayersCombination) or...

  if ( ('SmNDVI_BlendedVHP' in InpLayersCombination) or
       ('TCI_BlendedVHP' in InpLayersCombination) or
       ('VCI_BlendedVHP' in InpLayersCombination) or
       ('VHI_BlendedVHP' in InpLayersCombination) ):
    XYData_BlendedVHP_MonthlyPerc = XYDatas['XYData_BlendedVHP_MonthlyPerc']
  #end of if ( ('SmNDVI_BlendedVHP' in InpLayersCombination) or...

  if ('GlobSnow3' in InpLayersCombination):
    XYData_GlobSnow3_OverallPerc = XYDatas['XYData_GlobSnow3_OverallPerc']
  #end of if ('GlobSnow3' in InpLayersCombination)

  Target_Array = XYData_USDM_New['USDM_TimeSlicedArray'] # Target data array
  YYYYMMDD_Of_Array = XYData_USDM_New['YYYYMMDD_Of_Array']
  YYYY_Of_Array = YYYYMMDD_Of_Array // 10000
  MM_Of_Array = (YYYYMMDD_Of_Array - YYYY_Of_Array * 10000) // 100

  if IfMakeTargetBinary == 'Y':

    if IfIncludeD0AsDrought == 'Y':
      DroughtValues_LowerLimit = 0
    else:
      DroughtValues_LowerLimit = 1
    Drought_Idxs = np.where(Target_Array >= DroughtValues_LowerLimit)
    NoDrought_Idxs = np.where(Target_Array < DroughtValues_LowerLimit)
    Target_Array[Drought_Idxs] = 1
    Target_Array[NoDrought_Idxs] = 0

  else:

    Target_Array = Target_Array + 1 # Since currently it's -1-start for drought categories, not 0-start

  #end of if IfMakeTargetBinary == 'Y':

  #Begin input percentile arrays
  if 'Z_index' in InpLayersCombination:
    ZIndex_PrcntlArray = XYData['ZIndex_PrcntlArray']
  if 'Z_index_60_month' in InpLayersCombination:
    ZIndex60month_PrcntlArray = XYData['ZIndex60month_PrcntlArray']
  if 'PMDI' in InpLayersCombination:
    PMDI_PrcntlArray = XYData_OverallPerc['PMDI_PrcntlArray']
  if 'PHDI' in InpLayersCombination:
    PHDI_PrcntlArray = XYData_OverallPerc['PHDI_PrcntlArray']
  if 'prcp_01_nCG' in InpLayersCombination:
    prcp_01_PrcntlArray = XYData_AllnCG['prcp_01_PrcntlArray']
  if 'prcp_02_nCG' in InpLayersCombination:
    prcp_02_PrcntlArray = XYData_AllnCG['prcp_02_PrcntlArray']
  if 'prcp_03_nCG' in InpLayersCombination:
    prcp_03_PrcntlArray = XYData_AllnCG['prcp_03_PrcntlArray']
  if 'prcp_06_nCG' in InpLayersCombination:
    prcp_06_PrcntlArray = XYData_AllnCG['prcp_06_PrcntlArray']
  if 'prcp_09_nCG' in InpLayersCombination:
    prcp_09_PrcntlArray = XYData_AllnCG['prcp_09_PrcntlArray']
  if 'prcp_12_nCG' in InpLayersCombination:
    prcp_12_PrcntlArray = XYData_AllnCG['prcp_12_PrcntlArray']
  if 'prcp_24_nCG' in InpLayersCombination:
    prcp_24_PrcntlArray = XYData_AllnCG['prcp_24_PrcntlArray']
  if 'prcp_36_nCG' in InpLayersCombination:
    prcp_36_PrcntlArray = XYData_AllnCG['prcp_36_PrcntlArray']
  if 'prcp_48_nCG' in InpLayersCombination:
    prcp_48_PrcntlArray = XYData_AllnCG['prcp_48_PrcntlArray']
  if 'prcp_60_nCG' in InpLayersCombination:
    prcp_60_PrcntlArray = XYData_AllnCG['prcp_60_PrcntlArray']
  if 'prcp_72_nCG' in InpLayersCombination:
    prcp_72_PrcntlArray = XYData_AllnCG['prcp_72_PrcntlArray']
  if 'CPC_soil_moisture' in InpLayersCombination:
    CPCsoilmoist_PrcntlArray = XYData['CPCsoilmoist_PrcntlArray']
  if 'GRACE_DA_gw' in InpLayersCombination:
    GRACE_DA_gw_PrcntlArray = XYData_GRACEDA['GRACEDA_gws_inst_PrcntlArray']
  if 'GRACE_DA_sfsm' in InpLayersCombination:
    GRACE_DA_sfsm_PrcntlArray = XYData_GRACEDA_MonthlyPerc['GRACEDA_sfsm_inst_PrcntlArray']
  if 'GRACE_DA_rzsm' in InpLayersCombination:
    GRACE_DA_rzsm_PrcntlArray = XYData_GRACEDA_MonthlyPerc['GRACEDA_rtzsm_inst_PrcntlArray']
  if 'EDDI_1wk' in InpLayersCombination:
    EDDI1wk_PrcntlArray = XYData_EDDI1wk_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_2wk' in InpLayersCombination:
    EDDI2wk_PrcntlArray = XYData_EDDI2wk_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_3wk' in InpLayersCombination:
    EDDI3wk_PrcntlArray = XYData_EDDI3wk_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_4wk' in InpLayersCombination:
    EDDI4wk_PrcntlArray = XYData_EDDI4wk_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_5wk' in InpLayersCombination:
    EDDI5wk_PrcntlArray = XYData_EDDI5wk_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_6wk' in InpLayersCombination:
    EDDI6wk_PrcntlArray = XYData_EDDI6wk_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_7wk' in InpLayersCombination:
    EDDI7wk_PrcntlArray = XYData_EDDI7wk_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_8wk' in InpLayersCombination:
    EDDI8wk_PrcntlArray = XYData_EDDI8wk_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_9wk' in InpLayersCombination:
    EDDI9wk_PrcntlArray = XYData_EDDI9wk_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_10wk' in InpLayersCombination:
    EDDI10wk_PrcntlArray = XYData_EDDI10wk_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_11wk' in InpLayersCombination:
    EDDI11wk_PrcntlArray = XYData_EDDI11wk_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_12wk' in InpLayersCombination:
    EDDI12wk_PrcntlArray = XYData_EDDI12wk_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_1mn' in InpLayersCombination:
    EDDI1mn_PrcntlArray = XYData_EDDI1mn_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_2mn' in InpLayersCombination:
    EDDI2mn_PrcntlArray = XYData_EDDI2mn_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_3mn' in InpLayersCombination:
    EDDI3mn_PrcntlArray = XYData_EDDI3mn_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_4mn' in InpLayersCombination:
    EDDI4mn_PrcntlArray = XYData_EDDI4mn_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_5mn' in InpLayersCombination:
    EDDI5mn_PrcntlArray = XYData_EDDI5mn_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_6mn' in InpLayersCombination:
    EDDI6mn_PrcntlArray = XYData_EDDI6mn_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_7mn' in InpLayersCombination:
    EDDI7mn_PrcntlArray = XYData_EDDI7mn_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_8mn' in InpLayersCombination:
    EDDI8mn_PrcntlArray = XYData_EDDI8mn_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_9mn' in InpLayersCombination:
    EDDI9mn_PrcntlArray = XYData_EDDI9mn_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_10mn' in InpLayersCombination:
    EDDI10mn_PrcntlArray = XYData_EDDI10mn_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_11mn' in InpLayersCombination:
    EDDI11mn_PrcntlArray = XYData_EDDI11mn_MonthlyPerc['EDDI_PrcntlArray']
  if 'EDDI_12mn' in InpLayersCombination:
    EDDI12mn_PrcntlArray = XYData_EDDI12mn['EDDI_PrcntlArray']
#  if 'NLDAS2_1mSM_Mosaic' in InpLayersCombination:
#    NLDAS2_1mSM_Mosaic_PrcntlArray = XYData_NLDAS_2_1mSM_MonthlyPerc['NLDAS_2_1mSM_Mosaic_PrcntlArray']
#  if 'NLDAS2_1mSM_Noah' in InpLayersCombination:
#    NLDAS2_1mSM_Noah_PrcntlArray = XYData_NLDAS_2_1mSM_MonthlyPerc['NLDAS_2_1mSM_Noah_PrcntlArray']
#  if 'NLDAS2_1mSM_SAC' in InpLayersCombination:
#    NLDAS2_1mSM_SAC_PrcntlArray = XYData_NLDAS_2_1mSM_MonthlyPerc['NLDAS_2_1mSM_SAC_PrcntlArray']
#  if 'NLDAS2_1mSM_VIC' in InpLayersCombination:
#    NLDAS2_1mSM_VIC_PrcntlArray = XYData_NLDAS_2_1mSM_MonthlyPerc['NLDAS_2_1mSM_VIC_PrcntlArray']
  if 'NLDAS2D_1MSM_Mosaic' in InpLayersCombination:
    Mosaic_1MSM_PrcntlArray = XYData_NLDAS_2_daily['Mosaic_1MSM_PrcntlArray']
  if 'NLDAS2D_1MSM_Noah' in InpLayersCombination:
    Noah_1MSM_PrcntlArray = XYData_NLDAS_2_daily['Noah_1MSM_PrcntlArray']
  if 'NLDAS2D_1MSM_SAC' in InpLayersCombination:
    SAC_1MSM_PrcntlArray = XYData_NLDAS_2_daily['SAC_1MSM_PrcntlArray']
  if 'NLDAS2D_1MSM_VIC' in InpLayersCombination:
    VIC_1MSM_PrcntlArray = XYData_NLDAS_2_daily['VIC_1MSM_PrcntlArray']
  if 'NLDAS2D_TCSM_Mosaic' in InpLayersCombination:
    Mosaic_TCSM_PrcntlArray = XYData_NLDAS_2_daily['Mosaic_TCSM_PrcntlArray']
  if 'NLDAS2D_TCSM_Noah' in InpLayersCombination:
    Noah_TCSM_PrcntlArray = XYData_NLDAS_2_daily['Noah_TCSM_PrcntlArray']
  if 'NLDAS2D_TCSM_SAC' in InpLayersCombination:
    SAC_TCSM_PrcntlArray = XYData_NLDAS_2_daily['SAC_TCSM_PrcntlArray']
  if 'NLDAS2D_TCSM_VIC' in InpLayersCombination:
    VIC_TCSM_PrcntlArray = XYData_NLDAS_2_daily['VIC_TCSM_PrcntlArray']
  if 'NLDAS2D_EVAP_Mosaic' in InpLayersCombination:
    Mosaic_EVAP_PrcntlArray = XYData_NLDAS_2_daily['Mosaic_EVAP_PrcntlArray']
  if 'NLDAS2D_EVAP_Noah' in InpLayersCombination:
    Noah_EVAP_PrcntlArray = XYData_NLDAS_2_daily['Noah_EVAP_PrcntlArray']
  if 'NLDAS2D_EVAP_SAC' in InpLayersCombination:
    SAC_EVAP_PrcntlArray = XYData_NLDAS_2_daily['SAC_EVAP_PrcntlArray']
  if 'NLDAS2D_EVAP_VIC' in InpLayersCombination:
    VIC_EVAP_PrcntlArray = XYData_NLDAS_2_daily['VIC_EVAP_PrcntlArray']
  if 'NLDAS2D_SWE_Mosaic' in InpLayersCombination:
    Mosaic_SWE_PrcntlArray = XYData_NLDAS_2_daily['Mosaic_SWE_PrcntlArray']
  if 'NLDAS2D_SWE_Noah' in InpLayersCombination:
    Noah_SWE_PrcntlArray = XYData_NLDAS_2_daily['Noah_SWE_PrcntlArray']
  if 'NLDAS2D_SWE_SAC' in InpLayersCombination:
    SAC_SWE_PrcntlArray = XYData_NLDAS_2_daily['SAC_SWE_PrcntlArray']
  if 'NLDAS2D_SWE_VIC' in InpLayersCombination:
    VIC_SWE_PrcntlArray = XYData_NLDAS_2_daily['VIC_SWE_PrcntlArray']
  if 'NLDAS2D_RUN_Mosaic' in InpLayersCombination:
    Mosaic_RUN_PrcntlArray = XYData_NLDAS_2_daily['Mosaic_RUN_PrcntlArray']
  if 'NLDAS2D_RUN_Noah' in InpLayersCombination:
    Noah_RUN_PrcntlArray = XYData_NLDAS_2_daily['Noah_RUN_PrcntlArray']
  if 'NLDAS2D_RUN_SAC' in InpLayersCombination:
    SAC_RUN_PrcntlArray = XYData_NLDAS_2_daily['SAC_RUN_PrcntlArray']
  if 'NLDAS2D_RUN_VIC' in InpLayersCombination:
    VIC_RUN_PrcntlArray = XYData_NLDAS_2_daily['VIC_RUN_PrcntlArray']
  if 'NLDAS2D_STRMH04_Mosaic' in InpLayersCombination:
    Mosaic_STRM_H04_PrcntlArray = XYData_NLDAS_2_daily['Mosaic_STRM_H04_PrcntlArray']
  if 'NLDAS2D_STRMH04_Noah' in InpLayersCombination:
    Noah_STRM_H04_PrcntlArray = XYData_NLDAS_2_daily['Noah_STRM_H04_PrcntlArray']
  if 'NLDAS2D_STRMH04_SAC' in InpLayersCombination:
    SAC_STRM_H04_PrcntlArray = XYData_NLDAS_2_daily['SAC_STRM_H04_PrcntlArray']
  if 'NLDAS2D_STRMH04_VIC' in InpLayersCombination:
    VIC_STRM_H04_PrcntlArray = XYData_NLDAS_2_daily['VIC_STRM_H04_PrcntlArray']
  if 'VegDRI' in InpLayersCombination:
    VegDRI_PrcntlArray = XYData_VegDRI_MonthlyPerc['VegDRI_PrcntlArray']
  if 'QuickDRI' in InpLayersCombination:
    QuickDRI_PrcntlArray = XYData_QuickDRI_MonthlyPerc['QuickDRI_PrcntlArray']
#  if 'ESI' in InpLayersCombination:
#    ESI_PrcntlArray = XYData_ESI_MonthlyPerc['ESI_PrcntlArray']
  if 'ESI_4wk' in InpLayersCombination:
    ESI4Week_PrcntlArray = XYData_ESImultiWeek_MonthlyPerc['ESI4Week_PrcntlArray']
  if 'ESI_12wk' in InpLayersCombination:
    ESI12Week_PrcntlArray = XYData_ESImultiWeek_MonthlyPerc['ESI12Week_PrcntlArray']
#  if 'SPI_1_month' in InpLayersCombination:
#    SPI01_PrcntlArray = XYData_SPI_MonthlyPerc['sp01_PrcntlArray']
#  if 'SPI_2_month' in InpLayersCombination:
#    SPI02_PrcntlArray = XYData_SPI_MonthlyPerc['sp02_PrcntlArray']
#  if 'SPI_3_month' in InpLayersCombination:
#    SPI03_PrcntlArray = XYData_SPI_MonthlyPerc['sp03_PrcntlArray']
#  if 'SPI_6_month' in InpLayersCombination:
#    SPI06_PrcntlArray = XYData_SPI_MonthlyPerc['sp06_PrcntlArray']
#  if 'SPI_9_month' in InpLayersCombination:
#    SPI09_PrcntlArray = XYData_SPI_MonthlyPerc['sp09_PrcntlArray']
#  if 'SPI_12_month' in InpLayersCombination:
#    SPI12_PrcntlArray = XYData_SPI_OverallPerc['sp12_PrcntlArray']
#  if 'SPI_24_month' in InpLayersCombination:
#    SPI24_PrcntlArray = XYData_SPI_OverallPerc['sp24_PrcntlArray']
  if 'SPI_gamma_01_nCG' in InpLayersCombination:
    spi_gamma_01_PrcntlArray = XYData_AllnCG['spi_gamma_01_PrcntlArray']
  if 'SPI_gamma_02_nCG' in InpLayersCombination:
    spi_gamma_02_PrcntlArray = XYData_AllnCG['spi_gamma_02_PrcntlArray']
  if 'SPI_gamma_03_nCG' in InpLayersCombination:
    spi_gamma_03_PrcntlArray = XYData_AllnCG['spi_gamma_03_PrcntlArray']
  if 'SPI_gamma_06_nCG' in InpLayersCombination:
    spi_gamma_06_PrcntlArray = XYData_AllnCG['spi_gamma_06_PrcntlArray']
  if 'SPI_gamma_09_nCG' in InpLayersCombination:
    spi_gamma_09_PrcntlArray = XYData_AllnCG['spi_gamma_09_PrcntlArray']
  if 'SPI_gamma_12_nCG' in InpLayersCombination:
    spi_gamma_12_PrcntlArray = XYData_AllnCG['spi_gamma_12_PrcntlArray']
  if 'SPI_gamma_24_nCG' in InpLayersCombination:
    spi_gamma_24_PrcntlArray = XYData_AllnCG['spi_gamma_24_PrcntlArray']
  if 'SPI_gamma_36_nCG' in InpLayersCombination:
    spi_gamma_36_PrcntlArray = XYData_AllnCG['spi_gamma_36_PrcntlArray']
  if 'SPI_gamma_48_nCG' in InpLayersCombination:
    spi_gamma_48_PrcntlArray = XYData_AllnCG['spi_gamma_48_PrcntlArray']
  if 'SPI_gamma_60_nCG' in InpLayersCombination:
    spi_gamma_60_PrcntlArray = XYData_AllnCG['spi_gamma_60_PrcntlArray']
  if 'SPI_gamma_72_nCG' in InpLayersCombination:
    spi_gamma_72_PrcntlArray = XYData_AllnCG['spi_gamma_72_PrcntlArray']
  if 'SPEI_pear_01_nCG' in InpLayersCombination:
    spei_pearson_01_PrcntlArray = XYData_AllnCG['spei_pearson_01_PrcntlArray']
  if 'SPEI_pear_02_nCG' in InpLayersCombination:
    spei_pearson_02_PrcntlArray = XYData_AllnCG['spei_pearson_02_PrcntlArray']
  if 'SPEI_pear_03_nCG' in InpLayersCombination:
    spei_pearson_03_PrcntlArray = XYData_AllnCG['spei_pearson_03_PrcntlArray']
  if 'SPEI_pear_06_nCG' in InpLayersCombination:
    spei_pearson_06_PrcntlArray = XYData_AllnCG['spei_pearson_06_PrcntlArray']
  if 'SPEI_pear_09_nCG' in InpLayersCombination:
    spei_pearson_09_PrcntlArray = XYData_AllnCG['spei_pearson_09_PrcntlArray']
  if 'SPEI_pear_12_nCG' in InpLayersCombination:
    spei_pearson_12_PrcntlArray = XYData_AllnCG['spei_pearson_12_PrcntlArray']
  if 'SPEI_pear_24_nCG' in InpLayersCombination:
    spei_pearson_24_PrcntlArray = XYData_AllnCG['spei_pearson_24_PrcntlArray']
  if 'SPEI_pear_36_nCG' in InpLayersCombination:
    spei_pearson_36_PrcntlArray = XYData_AllnCG['spei_pearson_36_PrcntlArray']
  if 'SPEI_pear_48_nCG' in InpLayersCombination:
    spei_pearson_48_PrcntlArray = XYData_AllnCG['spei_pearson_48_PrcntlArray']
  if 'SPEI_pear_60_nCG' in InpLayersCombination:
    spei_pearson_60_PrcntlArray = XYData_AllnCG['spei_pearson_60_PrcntlArray']
  if 'SPEI_pear_72_nCG' in InpLayersCombination:
    spei_pearson_72_PrcntlArray = XYData_AllnCG['spei_pearson_72_PrcntlArray']
  if 'tavg_01_nCG' in InpLayersCombination:
    tavg_01_PrcntlArray = XYData_AllnCG['tavg_01_PrcntlArray']
  if 'tmax_01_nCG' in InpLayersCombination:
    tmax_01_PrcntlArray = XYData_AllnCG['tmax_01_PrcntlArray']
  if 'SNODAS' in InpLayersCombination:
    SNODAS_PrcntlArray = XYData_SNODASnESACCI['SNODAS_PrcntlArray']
  if 'ESA_CCI' in InpLayersCombination:
    ESA_CCI_PrcntlArray = XYData_SNODASnESACCI['ESA_CCI_PrcntlArray']
  if 'IMERG_01' in InpLayersCombination:
    IMERG_01_PrcntlArray = XYData_IMERG['IMERG_01_PrcntlArray']
  if 'IMERG_02' in InpLayersCombination:
    IMERG_02_PrcntlArray = XYData_IMERG['IMERG_02_PrcntlArray']
  if 'IMERG_03' in InpLayersCombination:
    IMERG_03_PrcntlArray = XYData_IMERG['IMERG_03_PrcntlArray']
  if 'IMERG_06' in InpLayersCombination:
    IMERG_06_PrcntlArray = XYData_IMERG['IMERG_06_PrcntlArray']
  if 'IMERG_09' in InpLayersCombination:
    IMERG_09_PrcntlArray = XYData_IMERG['IMERG_09_PrcntlArray']
  if 'IMERG_12' in InpLayersCombination:
    IMERG_12_PrcntlArray = XYData_IMERG['IMERG_12_PrcntlArray']
  if 'IMERG_24' in InpLayersCombination:
    IMERG_24_PrcntlArray = XYData_IMERG['IMERG_24_PrcntlArray']
  if 'IMERG_36' in InpLayersCombination:
    IMERG_36_PrcntlArray = XYData_IMERG['IMERG_36_PrcntlArray']
  if 'IMERG_48' in InpLayersCombination:
    IMERG_48_PrcntlArray = XYData_IMERG['IMERG_48_PrcntlArray']
  if 'IMERG_60' in InpLayersCombination:
    IMERG_60_PrcntlArray = XYData_IMERG['IMERG_60_PrcntlArray']
  if 'IMERG_72' in InpLayersCombination:
    IMERG_72_PrcntlArray = XYData_IMERG['IMERG_72_PrcntlArray']
  if 'SmNDVI_BlendedVHP' in InpLayersCombination:
    SmNDVI_BlendedVHP_PrcntlArray = XYData_BlendedVHP_MonthlyPerc['BlendedVHP_SMN_PrcntlArray']
  if 'TCI_BlendedVHP' in InpLayersCombination:
    TCI_BlendedVHP_PrcntlArray = XYData_BlendedVHP_MonthlyPerc['BlendedVHP_TCI_PrcntlArray']
  if 'VCI_BlendedVHP' in InpLayersCombination:
    VCI_BlendedVHP_PrcntlArray = XYData_BlendedVHP_MonthlyPerc['BlendedVHP_VCI_PrcntlArray']
  if 'VHI_BlendedVHP' in InpLayersCombination:
    VHI_BlendedVHP_PrcntlArray = XYData_BlendedVHP_MonthlyPerc['BlendedVHP_VHI_PrcntlArray']
  if 'GlobSnow3' in InpLayersCombination:
    GlobSnow3_PrcntlArray = XYData_GlobSnow3_OverallPerc['GlobSnow3_PrcntlArray']
  #End input percentile arrays

  if IfSpatialSubDomain:
  
    Target_Array = Target_Array[:, WhichCols[0]]
    if 'Z_index' in InpLayersCombination:
      ZIndex_PrcntlArray = ZIndex_PrcntlArray[:, WhichCols[0]]
    if 'Z_index_60_month' in InpLayersCombination:
      ZIndex60month_PrcntlArray = ZIndex60month_PrcntlArray[:, WhichCols[0]]
    if 'PMDI' in InpLayersCombination:
      PMDI_PrcntlArray = PMDI_PrcntlArray[:, WhichCols[0]]
    if 'PHDI' in InpLayersCombination:
      PHDI_PrcntlArray = PHDI_PrcntlArray[:, WhichCols[0]]
    if 'prcp_01_nCG' in InpLayersCombination:
      prcp_01_PrcntlArray = prcp_01_PrcntlArray[:, WhichCols[0]]
    if 'prcp_02_nCG' in InpLayersCombination:
      prcp_02_PrcntlArray = prcp_02_PrcntlArray[:, WhichCols[0]]
    if 'prcp_03_nCG' in InpLayersCombination:
      prcp_03_PrcntlArray = prcp_03_PrcntlArray[:, WhichCols[0]]
    if 'prcp_06_nCG' in InpLayersCombination:
      prcp_06_PrcntlArray = prcp_06_PrcntlArray[:, WhichCols[0]]
    if 'prcp_09_nCG' in InpLayersCombination:
      prcp_09_PrcntlArray = prcp_09_PrcntlArray[:, WhichCols[0]]
    if 'prcp_12_nCG' in InpLayersCombination:
      prcp_12_PrcntlArray = prcp_12_PrcntlArray[:, WhichCols[0]]
    if 'prcp_24_nCG' in InpLayersCombination:
      prcp_24_PrcntlArray = prcp_24_PrcntlArray[:, WhichCols[0]]
    if 'prcp_36_nCG' in InpLayersCombination:
      prcp_36_PrcntlArray = prcp_36_PrcntlArray[:, WhichCols[0]]
    if 'prcp_48_nCG' in InpLayersCombination:
      prcp_48_PrcntlArray = prcp_48_PrcntlArray[:, WhichCols[0]]
    if 'prcp_60_nCG' in InpLayersCombination:
      prcp_60_PrcntlArray = prcp_60_PrcntlArray[:, WhichCols[0]]
    if 'prcp_72_nCG' in InpLayersCombination:
      prcp_72_PrcntlArray = prcp_72_PrcntlArray[:, WhichCols[0]]
    if 'CPC_soil_moisture' in InpLayersCombination:
      CPCsoilmoist_PrcntlArray = CPCsoilmoist_PrcntlArray[:, WhichCols[0]]
    if 'GRACE_DA_gw' in InpLayersCombination:
      GRACE_DA_gw_PrcntlArray = GRACE_DA_gw_PrcntlArray[:, WhichCols[0]]
    if 'GRACE_DA_sfsm' in InpLayersCombination:
      GRACE_DA_sfsm_PrcntlArray = GRACE_DA_sfsm_PrcntlArray[:, WhichCols[0]]
    if 'GRACE_DA_rzsm' in InpLayersCombination:
      GRACE_DA_rzsm_PrcntlArray = GRACE_DA_rzsm_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_1wk' in InpLayersCombination:
      EDDI1wk_PrcntlArray = EDDI1wk_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_2wk' in InpLayersCombination:
      EDDI2wk_PrcntlArray = EDDI2wk_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_3wk' in InpLayersCombination:
      EDDI3wk_PrcntlArray = EDDI3wk_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_4wk' in InpLayersCombination:
      EDDI4wk_PrcntlArray = EDDI4wk_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_5wk' in InpLayersCombination:
      EDDI5wk_PrcntlArray = EDDI5wk_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_6wk' in InpLayersCombination:
      EDDI6wk_PrcntlArray = EDDI6wk_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_7wk' in InpLayersCombination:
      EDDI7wk_PrcntlArray = EDDI7wk_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_8wk' in InpLayersCombination:
      EDDI8wk_PrcntlArray = EDDI8wk_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_9wk' in InpLayersCombination:
      EDDI9wk_PrcntlArray = EDDI9wk_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_10wk' in InpLayersCombination:
      EDDI10wk_PrcntlArray = EDDI10wk_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_11wk' in InpLayersCombination:
      EDDI11wk_PrcntlArray = EDDI11wk_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_12wk' in InpLayersCombination:
      EDDI12wk_PrcntlArray = EDDI12wk_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_1mn' in InpLayersCombination:
      EDDI1mn_PrcntlArray = EDDI1mn_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_2mn' in InpLayersCombination:
      EDDI2mn_PrcntlArray = EDDI2mn_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_3mn' in InpLayersCombination:
      EDDI3mn_PrcntlArray = EDDI3mn_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_4mn' in InpLayersCombination:
      EDDI4mn_PrcntlArray = EDDI4mn_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_5mn' in InpLayersCombination:
      EDDI5mn_PrcntlArray = EDDI5mn_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_6mn' in InpLayersCombination:
      EDDI6mn_PrcntlArray = EDDI6mn_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_7mn' in InpLayersCombination:
      EDDI7mn_PrcntlArray = EDDI7mn_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_8mn' in InpLayersCombination:
      EDDI8mn_PrcntlArray = EDDI8mn_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_9mn' in InpLayersCombination:
      EDDI9mn_PrcntlArray = EDDI9mn_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_10mn' in InpLayersCombination:
      EDDI10mn_PrcntlArray = EDDI10mn_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_11mn' in InpLayersCombination:
      EDDI11mn_PrcntlArray = EDDI11mn_PrcntlArray[:, WhichCols[0]]
    if 'EDDI_12mn' in InpLayersCombination:
      EDDI12mn_PrcntlArray = EDDI12mn_PrcntlArray[:, WhichCols[0]]
#    if 'NLDAS2_1mSM_Mosaic' in InpLayersCombination:
#      NLDAS2_1mSM_Mosaic_PrcntlArray = NLDAS2_1mSM_Mosaic_PrcntlArray[:, WhichCols[0]]
#    if 'NLDAS2_1mSM_Noah' in InpLayersCombination:
#      NLDAS2_1mSM_Noah_PrcntlArray = NLDAS2_1mSM_Noah_PrcntlArray[:, WhichCols[0]]
#    if 'NLDAS2_1mSM_SAC' in InpLayersCombination:
#      NLDAS2_1mSM_SAC_PrcntlArray = NLDAS2_1mSM_SAC_PrcntlArray[:, WhichCols[0]]
#    if 'NLDAS2_1mSM_VIC' in InpLayersCombination:
#      NLDAS2_1mSM_VIC_PrcntlArray = NLDAS2_1mSM_VIC_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_1MSM_Mosaic' in InpLayersCombination:
      Mosaic_1MSM_PrcntlArray = Mosaic_1MSM_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_1MSM_Noah' in InpLayersCombination:
      Noah_1MSM_PrcntlArray = Noah_1MSM_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_1MSM_SAC' in InpLayersCombination:
      SAC_1MSM_PrcntlArray = SAC_1MSM_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_1MSM_VIC' in InpLayersCombination:
      VIC_1MSM_PrcntlArray = VIC_1MSM_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_TCSM_Mosaic' in InpLayersCombination:
      Mosaic_TCSM_PrcntlArray = Mosaic_TCSM_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_TCSM_Noah' in InpLayersCombination:
      Noah_TCSM_PrcntlArray = Noah_TCSM_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_TCSM_SAC' in InpLayersCombination:
      SAC_TCSM_PrcntlArray = SAC_TCSM_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_TCSM_VIC' in InpLayersCombination:
      VIC_TCSM_PrcntlArray = VIC_TCSM_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_EVAP_Mosaic' in InpLayersCombination:
      Mosaic_EVAP_PrcntlArray = Mosaic_EVAP_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_EVAP_Noah' in InpLayersCombination:
      Noah_EVAP_PrcntlArray = Noah_EVAP_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_EVAP_SAC' in InpLayersCombination:
      SAC_EVAP_PrcntlArray = SAC_EVAP_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_EVAP_VIC' in InpLayersCombination:
      VIC_EVAP_PrcntlArray = VIC_EVAP_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_SWE_Mosaic' in InpLayersCombination:
      Mosaic_SWE_PrcntlArray = Mosaic_SWE_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_SWE_Noah' in InpLayersCombination:
      Noah_SWE_PrcntlArray = Noah_SWE_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_SWE_SAC' in InpLayersCombination:
      SAC_SWE_PrcntlArray = SAC_SWE_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_SWE_VIC' in InpLayersCombination:
      VIC_SWE_PrcntlArray = VIC_SWE_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_RUN_Mosaic' in InpLayersCombination:
      Mosaic_RUN_PrcntlArray = Mosaic_RUN_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_RUN_Noah' in InpLayersCombination:
      Noah_RUN_PrcntlArray = Noah_RUN_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_RUN_SAC' in InpLayersCombination:
      SAC_RUN_PrcntlArray = SAC_RUN_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_RUN_VIC' in InpLayersCombination:
      VIC_RUN_PrcntlArray = VIC_RUN_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_STRMH04_Mosaic' in InpLayersCombination:
      Mosaic_STRM_H04_PrcntlArray = Mosaic_STRM_H04_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_STRMH04_Noah' in InpLayersCombination:
      Noah_STRM_H04_PrcntlArray = Noah_STRM_H04_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_STRMH04_SAC' in InpLayersCombination:
      SAC_STRM_H04_PrcntlArray = SAC_STRM_H04_PrcntlArray[:, WhichCols[0]]
    if 'NLDAS2D_STRMH04_VIC' in InpLayersCombination:
      VIC_STRM_H04_PrcntlArray = VIC_STRM_H04_PrcntlArray[:, WhichCols[0]]
    if 'VegDRI' in InpLayersCombination:
      VegDRI_PrcntlArray = VegDRI_PrcntlArray[:, WhichCols[0]]
    if 'QuickDRI' in InpLayersCombination:
      QuickDRI_PrcntlArray = QuickDRI_PrcntlArray[:, WhichCols[0]]
#    if 'ESI' in InpLayersCombination:
#      ESI_PrcntlArray = ESI_PrcntlArray[:, WhichCols[0]]
    if 'ESI_4wk' in InpLayersCombination:
      ESI4Week_PrcntlArray = ESI4Week_PrcntlArray[:, WhichCols[0]]
    if 'ESI_12wk' in InpLayersCombination:
      ESI12Week_PrcntlArray = ESI12Week_PrcntlArray[:, WhichCols[0]]
#    if 'SPI_1_month' in InpLayersCombination:
#      SPI01_PrcntlArray = SPI01_PrcntlArray[:, WhichCols[0]]
#    if 'SPI_2_month' in InpLayersCombination:
#      SPI02_PrcntlArray = SPI02_PrcntlArray[:, WhichCols[0]]
#    if 'SPI_3_month' in InpLayersCombination:
#      SPI03_PrcntlArray = SPI03_PrcntlArray[:, WhichCols[0]]
#    if 'SPI_6_month' in InpLayersCombination:
#      SPI06_PrcntlArray = SPI06_PrcntlArray[:, WhichCols[0]]
#    if 'SPI_9_month' in InpLayersCombination:
#      SPI09_PrcntlArray = SPI09_PrcntlArray[:, WhichCols[0]]
#    if 'SPI_12_month' in InpLayersCombination:
#      SPI12_PrcntlArray = SPI12_PrcntlArray[:, WhichCols[0]]
#    if 'SPI_24_month' in InpLayersCombination:
#      SPI24_PrcntlArray = SPI24_PrcntlArray[:, WhichCols[0]]
    if 'SPI_gamma_01_nCG' in InpLayersCombination:
      spi_gamma_01_PrcntlArray = spi_gamma_01_PrcntlArray[:, WhichCols[0]]
    if 'SPI_gamma_02_nCG' in InpLayersCombination:
      spi_gamma_02_PrcntlArray = spi_gamma_02_PrcntlArray[:, WhichCols[0]]
    if 'SPI_gamma_03_nCG' in InpLayersCombination:
      spi_gamma_03_PrcntlArray = spi_gamma_03_PrcntlArray[:, WhichCols[0]]
    if 'SPI_gamma_06_nCG' in InpLayersCombination:
      spi_gamma_06_PrcntlArray = spi_gamma_06_PrcntlArray[:, WhichCols[0]]
    if 'SPI_gamma_09_nCG' in InpLayersCombination:
      spi_gamma_09_PrcntlArray = spi_gamma_09_PrcntlArray[:, WhichCols[0]]
    if 'SPI_gamma_12_nCG' in InpLayersCombination:
      spi_gamma_12_PrcntlArray = spi_gamma_12_PrcntlArray[:, WhichCols[0]]
    if 'SPI_gamma_24_nCG' in InpLayersCombination:
      spi_gamma_24_PrcntlArray = spi_gamma_24_PrcntlArray[:, WhichCols[0]]
    if 'SPI_gamma_36_nCG' in InpLayersCombination:
      spi_gamma_36_PrcntlArray = spi_gamma_36_PrcntlArray[:, WhichCols[0]]
    if 'SPI_gamma_48_nCG' in InpLayersCombination:
      spi_gamma_48_PrcntlArray = spi_gamma_48_PrcntlArray[:, WhichCols[0]]
    if 'SPI_gamma_60_nCG' in InpLayersCombination:
      spi_gamma_60_PrcntlArray = spi_gamma_60_PrcntlArray[:, WhichCols[0]]
    if 'SPI_gamma_72_nCG' in InpLayersCombination:
      spi_gamma_72_PrcntlArray = spi_gamma_72_PrcntlArray[:, WhichCols[0]]
    if 'SPEI_pear_01_nCG' in InpLayersCombination:
      spei_pearson_01_PrcntlArray = spei_pearson_01_PrcntlArray[:, WhichCols[0]]
    if 'SPEI_pear_02_nCG' in InpLayersCombination:
      spei_pearson_02_PrcntlArray = spei_pearson_02_PrcntlArray[:, WhichCols[0]]
    if 'SPEI_pear_03_nCG' in InpLayersCombination:
      spei_pearson_03_PrcntlArray = spei_pearson_03_PrcntlArray[:, WhichCols[0]]
    if 'SPEI_pear_06_nCG' in InpLayersCombination:
      spei_pearson_06_PrcntlArray = spei_pearson_06_PrcntlArray[:, WhichCols[0]]
    if 'SPEI_pear_09_nCG' in InpLayersCombination:
      spei_pearson_09_PrcntlArray = spei_pearson_09_PrcntlArray[:, WhichCols[0]]
    if 'SPEI_pear_12_nCG' in InpLayersCombination:
      spei_pearson_12_PrcntlArray = spei_pearson_12_PrcntlArray[:, WhichCols[0]]
    if 'SPEI_pear_24_nCG' in InpLayersCombination:
      spei_pearson_24_PrcntlArray = spei_pearson_24_PrcntlArray[:, WhichCols[0]]
    if 'SPEI_pear_36_nCG' in InpLayersCombination:
      spei_pearson_36_PrcntlArray = spei_pearson_36_PrcntlArray[:, WhichCols[0]]
    if 'SPEI_pear_48_nCG' in InpLayersCombination:
      spei_pearson_48_PrcntlArray = spei_pearson_48_PrcntlArray[:, WhichCols[0]]
    if 'SPEI_pear_60_nCG' in InpLayersCombination:
      spei_pearson_60_PrcntlArray = spei_pearson_60_PrcntlArray[:, WhichCols[0]]
    if 'SPEI_pear_72_nCG' in InpLayersCombination:
      spei_pearson_72_PrcntlArray = spei_pearson_72_PrcntlArray[:, WhichCols[0]]
    if 'tavg_01_nCG' in InpLayersCombination:
      tavg_01_PrcntlArray = tavg_01_PrcntlArray[:, WhichCols[0]] 
    if 'tmax_01_nCG' in InpLayersCombination:
      tmax_01_PrcntlArray = tmax_01_PrcntlArray[:, WhichCols[0]]
    if 'SNODAS' in InpLayersCombination:
      SNODAS_PrcntlArray = SNODAS_PrcntlArray[:, WhichCols[0]]
    if 'ESA_CCI' in InpLayersCombination:
      ESA_CCI_PrcntlArray = ESA_CCI_PrcntlArray[:, WhichCols[0]]
    if 'IMERG_01' in InpLayersCombination:
      IMERG_01_PrcntlArray = IMERG_01_PrcntlArray[:, WhichCols[0]]
    if 'IMERG_02' in InpLayersCombination:
      IMERG_02_PrcntlArray = IMERG_02_PrcntlArray[:, WhichCols[0]]
    if 'IMERG_03' in InpLayersCombination:
      IMERG_03_PrcntlArray = IMERG_03_PrcntlArray[:, WhichCols[0]]
    if 'IMERG_06' in InpLayersCombination:
      IMERG_06_PrcntlArray = IMERG_06_PrcntlArray[:, WhichCols[0]]
    if 'IMERG_09' in InpLayersCombination:
      IMERG_09_PrcntlArray = IMERG_09_PrcntlArray[:, WhichCols[0]]
    if 'IMERG_12' in InpLayersCombination:
      IMERG_12_PrcntlArray = IMERG_12_PrcntlArray[:, WhichCols[0]]
    if 'IMERG_24' in InpLayersCombination:
      IMERG_24_PrcntlArray = IMERG_24_PrcntlArray[:, WhichCols[0]]
    if 'IMERG_36' in InpLayersCombination:
      IMERG_36_PrcntlArray = IMERG_36_PrcntlArray[:, WhichCols[0]]
    if 'IMERG_48' in InpLayersCombination:
      IMERG_48_PrcntlArray = IMERG_48_PrcntlArray[:, WhichCols[0]]
    if 'IMERG_60' in InpLayersCombination:
      IMERG_60_PrcntlArray = IMERG_60_PrcntlArray[:, WhichCols[0]]
    if 'IMERG_72' in InpLayersCombination:
      IMERG_72_PrcntlArray = IMERG_72_PrcntlArray[:, WhichCols[0]]
    if 'SmNDVI_BlendedVHP' in InpLayersCombination:
      SmNDVI_BlendedVHP_PrcntlArray = SmNDVI_BlendedVHP_PrcntlArray[:, WhichCols[0]]
    if 'TCI_BlendedVHP' in InpLayersCombination:
      TCI_BlendedVHP_PrcntlArray = TCI_BlendedVHP_PrcntlArray[:, WhichCols[0]]
    if 'VCI_BlendedVHP' in InpLayersCombination:
      VCI_BlendedVHP_PrcntlArray = VCI_BlendedVHP_PrcntlArray[:, WhichCols[0]]
    if 'VHI_BlendedVHP' in InpLayersCombination:
      VHI_BlendedVHP_PrcntlArray = VHI_BlendedVHP_PrcntlArray[:, WhichCols[0]]
    if 'GlobSnow3' in InpLayersCombination:
      GlobSnow3_PrcntlArray = GlobSnow3_PrcntlArray[:, WhichCols[0]]

  #end of if IfSpatialSubDomain:
  
  if SpatialSubDomain[0:5] == 'Event':
    Event_BeginYYYYMMDD = 10000 * Event_BeginDateVecList[0] + 100 * Event_BeginDateVecList[1] + Event_BeginDateVecList[2]
    Event_EndYYYYMMDD = 10000 * Event_EndDateVecList[0] + 100 * Event_EndDateVecList[1] + Event_EndDateVecList[2]
    if WhichSeason == 'P':
      WhichRows = np.where( (YYYYMMDD_Of_Array >= Event_BeginYYYYMMDD) & 
                            (YYYYMMDD_Of_Array <= Event_EndYYYYMMDD) & 
                            (MM_Of_Array >= 3) & (MM_Of_Array <= 5) )
    elif WhichSeason == 'U':
      WhichRows = np.where( (YYYYMMDD_Of_Array >= Event_BeginYYYYMMDD) & 
                            (YYYYMMDD_Of_Array <= Event_EndYYYYMMDD) & 
                            (MM_Of_Array >= 6) & (MM_Of_Array <= 8) )
    elif WhichSeason == 'F':
      WhichRows = np.where( (YYYYMMDD_Of_Array >= Event_BeginYYYYMMDD) & 
                            (YYYYMMDD_Of_Array <= Event_EndYYYYMMDD) & 
                            (MM_Of_Array >= 9) & (MM_Of_Array <= 11) )
    elif WhichSeason == 'W':
      WhichRows = np.where( (YYYYMMDD_Of_Array >= Event_BeginYYYYMMDD) & 
                            (YYYYMMDD_Of_Array <= Event_EndYYYYMMDD) & 
                            ( (MM_Of_Array >= 12) | (MM_Of_Array <= 2) ) )
    elif WhichSeason == 'A':
      WhichRows = np.where( (YYYYMMDD_Of_Array >= Event_BeginYYYYMMDD) & 
                            (YYYYMMDD_Of_Array <= Event_EndYYYYMMDD) )
    #end of elif WhichSeason == 'W'
  else: # of if SpatialSubDomain[0:5] == 'Event'
    if WhichSeason == 'P':
      WhichRows = np.where( (MM_Of_Array >= 3) & (MM_Of_Array <= 5) )
    elif WhichSeason == 'U':
      WhichRows = np.where( (MM_Of_Array >= 6) & (MM_Of_Array <= 8) )
    elif WhichSeason == 'F':
      WhichRows = np.where( (MM_Of_Array >= 9) & (MM_Of_Array <= 11) )
    elif WhichSeason == 'W':
      WhichRows = np.where( (MM_Of_Array >= 12) | (MM_Of_Array <= 2) )
  #end of if SpatialSubDomain[0:5] == 'Event'
    
  if ( (WhichSeason in ['P', 'U', 'F', 'W']) or
       (SpatialSubDomain[0:5] == 'Event') ):
    Target_Array = Target_Array[WhichRows[0], :]
    if 'Z_index' in InpLayersCombination:
      ZIndex_PrcntlArray = ZIndex_PrcntlArray[WhichRows[0], :]
    if 'Z_index_60_month' in InpLayersCombination:
      ZIndex60month_PrcntlArray = ZIndex60month_PrcntlArray[WhichRows[0], :]
    if 'PMDI' in InpLayersCombination:
      PMDI_PrcntlArray = PMDI_PrcntlArray[WhichRows[0], :]
    if 'PHDI' in InpLayersCombination:
      PHDI_PrcntlArray = PHDI_PrcntlArray[WhichRows[0], :]
    if 'prcp_01_nCG' in InpLayersCombination:
      prcp_01_PrcntlArray = prcp_01_PrcntlArray[WhichRows[0], :]
    if 'prcp_02_nCG' in InpLayersCombination:
      prcp_02_PrcntlArray = prcp_02_PrcntlArray[WhichRows[0], :]
    if 'prcp_03_nCG' in InpLayersCombination:
      prcp_03_PrcntlArray = prcp_03_PrcntlArray[WhichRows[0], :]
    if 'prcp_06_nCG' in InpLayersCombination:
      prcp_06_PrcntlArray = prcp_06_PrcntlArray[WhichRows[0], :]
    if 'prcp_09_nCG' in InpLayersCombination:
      prcp_09_PrcntlArray = prcp_09_PrcntlArray[WhichRows[0], :]
    if 'prcp_12_nCG' in InpLayersCombination:
      prcp_12_PrcntlArray = prcp_12_PrcntlArray[WhichRows[0], :]
    if 'prcp_24_nCG' in InpLayersCombination:
      prcp_24_PrcntlArray = prcp_24_PrcntlArray[WhichRows[0], :]
    if 'prcp_36_nCG' in InpLayersCombination:
      prcp_36_PrcntlArray = prcp_36_PrcntlArray[WhichRows[0], :]
    if 'prcp_48_nCG' in InpLayersCombination:
      prcp_48_PrcntlArray = prcp_48_PrcntlArray[WhichRows[0], :]
    if 'prcp_60_nCG' in InpLayersCombination:
      prcp_60_PrcntlArray = prcp_60_PrcntlArray[WhichRows[0], :]
    if 'prcp_72_nCG' in InpLayersCombination:
      prcp_72_PrcntlArray = prcp_72_PrcntlArray[WhichRows[0], :]
    if 'CPC_soil_moisture' in InpLayersCombination:
      CPCsoilmoist_PrcntlArray = CPCsoilmoist_PrcntlArray[WhichRows[0], :]
    if 'GRACE_DA_gw' in InpLayersCombination:
      GRACE_DA_gw_PrcntlArray = GRACE_DA_gw_PrcntlArray[WhichRows[0], :]
    if 'GRACE_DA_sfsm' in InpLayersCombination:
      GRACE_DA_sfsm_PrcntlArray = GRACE_DA_sfsm_PrcntlArray[WhichRows[0], :]
    if 'GRACE_DA_rzsm' in InpLayersCombination:
      GRACE_DA_rzsm_PrcntlArray = GRACE_DA_rzsm_PrcntlArray[WhichRows[0], :]
    if 'EDDI_1wk' in InpLayersCombination:
      EDDI1wk_PrcntlArray = EDDI1wk_PrcntlArray[WhichRows[0], :]
    if 'EDDI_2wk' in InpLayersCombination:
      EDDI2wk_PrcntlArray = EDDI2wk_PrcntlArray[WhichRows[0], :]
    if 'EDDI_3wk' in InpLayersCombination:
      EDDI3wk_PrcntlArray = EDDI3wk_PrcntlArray[WhichRows[0], :]
    if 'EDDI_4wk' in InpLayersCombination:
      EDDI4wk_PrcntlArray = EDDI4wk_PrcntlArray[WhichRows[0], :]
    if 'EDDI_5wk' in InpLayersCombination:
      EDDI5wk_PrcntlArray = EDDI5wk_PrcntlArray[WhichRows[0], :]
    if 'EDDI_6wk' in InpLayersCombination:
      EDDI6wk_PrcntlArray = EDDI6wk_PrcntlArray[WhichRows[0], :]
    if 'EDDI_7wk' in InpLayersCombination:
      EDDI7wk_PrcntlArray = EDDI7wk_PrcntlArray[WhichRows[0], :]
    if 'EDDI_8wk' in InpLayersCombination:
      EDDI8wk_PrcntlArray = EDDI8wk_PrcntlArray[WhichRows[0], :]
    if 'EDDI_9wk' in InpLayersCombination:
      EDDI9wk_PrcntlArray = EDDI9wk_PrcntlArray[WhichRows[0], :]
    if 'EDDI_10wk' in InpLayersCombination:
      EDDI10wk_PrcntlArray = EDDI10wk_PrcntlArray[WhichRows[0], :]
    if 'EDDI_11wk' in InpLayersCombination:
      EDDI11wk_PrcntlArray = EDDI11wk_PrcntlArray[WhichRows[0], :]
    if 'EDDI_12wk' in InpLayersCombination:
      EDDI12wk_PrcntlArray = EDDI12wk_PrcntlArray[WhichRows[0], :]
    if 'EDDI_1mn' in InpLayersCombination:
      EDDI1mn_PrcntlArray = EDDI1mn_PrcntlArray[WhichRows[0], :]
    if 'EDDI_2mn' in InpLayersCombination:
      EDDI2mn_PrcntlArray = EDDI2mn_PrcntlArray[WhichRows[0], :]
    if 'EDDI_3mn' in InpLayersCombination:
      EDDI3mn_PrcntlArray = EDDI3mn_PrcntlArray[WhichRows[0], :]
    if 'EDDI_4mn' in InpLayersCombination:
      EDDI4mn_PrcntlArray = EDDI4mn_PrcntlArray[WhichRows[0], :]
    if 'EDDI_5mn' in InpLayersCombination:
      EDDI5mn_PrcntlArray = EDDI5mn_PrcntlArray[WhichRows[0], :]
    if 'EDDI_6mn' in InpLayersCombination:
      EDDI6mn_PrcntlArray = EDDI6mn_PrcntlArray[WhichRows[0], :]
    if 'EDDI_7mn' in InpLayersCombination:
      EDDI7mn_PrcntlArray = EDDI7mn_PrcntlArray[WhichRows[0], :]
    if 'EDDI_8mn' in InpLayersCombination:
      EDDI8mn_PrcntlArray = EDDI8mn_PrcntlArray[WhichRows[0], :]
    if 'EDDI_9mn' in InpLayersCombination:
      EDDI9mn_PrcntlArray = EDDI9mn_PrcntlArray[WhichRows[0], :]
    if 'EDDI_10mn' in InpLayersCombination:
      EDDI10mn_PrcntlArray = EDDI10mn_PrcntlArray[WhichRows[0], :]
    if 'EDDI_11mn' in InpLayersCombination:
      EDDI11mn_PrcntlArray = EDDI11mn_PrcntlArray[WhichRows[0], :]
    if 'EDDI_12mn' in InpLayersCombination:
      EDDI12mn_PrcntlArray = EDDI12mn_PrcntlArray[WhichRows[0], :]
#    if 'NLDAS2_1mSM_Mosaic' in InpLayersCombination:
#      NLDAS2_1mSM_Mosaic_PrcntlArray = NLDAS2_1mSM_Mosaic_PrcntlArray[WhichRows[0], :]
#    if 'NLDAS2_1mSM_Noah' in InpLayersCombination:
#      NLDAS2_1mSM_Noah_PrcntlArray = NLDAS2_1mSM_Noah_PrcntlArray[WhichRows[0], :]
#    if 'NLDAS2_1mSM_SAC' in InpLayersCombination:
#      NLDAS2_1mSM_SAC_PrcntlArray = NLDAS2_1mSM_SAC_PrcntlArray[WhichRows[0], :]
#    if 'NLDAS2_1mSM_VIC' in InpLayersCombination:
#      NLDAS2_1mSM_VIC_PrcntlArray = NLDAS2_1mSM_VIC_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_1MSM_Mosaic' in InpLayersCombination:
      Mosaic_1MSM_PrcntlArray = Mosaic_1MSM_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_1MSM_Noah' in InpLayersCombination:
      Noah_1MSM_PrcntlArray = Noah_1MSM_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_1MSM_SAC' in InpLayersCombination:
      SAC_1MSM_PrcntlArray = SAC_1MSM_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_1MSM_VIC' in InpLayersCombination:
      VIC_1MSM_PrcntlArray = VIC_1MSM_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_TCSM_Mosaic' in InpLayersCombination:
      Mosaic_TCSM_PrcntlArray = Mosaic_TCSM_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_TCSM_Noah' in InpLayersCombination:
      Noah_TCSM_PrcntlArray = Noah_TCSM_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_TCSM_SAC' in InpLayersCombination:
      SAC_TCSM_PrcntlArray = SAC_TCSM_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_TCSM_VIC' in InpLayersCombination:
      VIC_TCSM_PrcntlArray = VIC_TCSM_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_EVAP_Mosaic' in InpLayersCombination:
      Mosaic_EVAP_PrcntlArray = Mosaic_EVAP_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_EVAP_Noah' in InpLayersCombination:
      Noah_EVAP_PrcntlArray = Noah_EVAP_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_EVAP_SAC' in InpLayersCombination:
      SAC_EVAP_PrcntlArray = SAC_EVAP_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_EVAP_VIC' in InpLayersCombination:
      VIC_EVAP_PrcntlArray = VIC_EVAP_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_SWE_Mosaic' in InpLayersCombination:
      Mosaic_SWE_PrcntlArray = Mosaic_SWE_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_SWE_Noah' in InpLayersCombination:
      Noah_SWE_PrcntlArray = Noah_SWE_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_SWE_SAC' in InpLayersCombination:
      SAC_SWE_PrcntlArray = SAC_SWE_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_SWE_VIC' in InpLayersCombination:
      VIC_SWE_PrcntlArray = VIC_SWE_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_RUN_Mosaic' in InpLayersCombination:
      Mosaic_RUN_PrcntlArray = Mosaic_RUN_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_RUN_Noah' in InpLayersCombination:
      Noah_RUN_PrcntlArray = Noah_RUN_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_RUN_SAC' in InpLayersCombination:
      SAC_RUN_PrcntlArray = SAC_RUN_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_RUN_VIC' in InpLayersCombination:
      VIC_RUN_PrcntlArray = VIC_RUN_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_STRMH04_Mosaic' in InpLayersCombination:
      Mosaic_STRM_H04_PrcntlArray = Mosaic_STRM_H04_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_STRMH04_Noah' in InpLayersCombination:
      Noah_STRM_H04_PrcntlArray = Noah_STRM_H04_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_STRMH04_SAC' in InpLayersCombination:
      SAC_STRM_H04_PrcntlArray = SAC_STRM_H04_PrcntlArray[WhichRows[0], :]
    if 'NLDAS2D_STRMH04_VIC' in InpLayersCombination:
      VIC_STRM_H04_PrcntlArray = VIC_STRM_H04_PrcntlArray[WhichRows[0], :]
    if 'VegDRI' in InpLayersCombination:
      VegDRI_PrcntlArray = VegDRI_PrcntlArray[WhichRows[0], :]
    if 'QuickDRI' in InpLayersCombination:
      QuickDRI_PrcntlArray = QuickDRI_PrcntlArray[WhichRows[0], :]
#    if 'ESI' in InpLayersCombination:
#      ESI_PrcntlArray = ESI_PrcntlArray[WhichRows[0], :]
    if 'ESI_4wk' in InpLayersCombination:
      ESI4Week_PrcntlArray = ESI4Week_PrcntlArray[WhichRows[0], :]
    if 'ESI_12wk' in InpLayersCombination:
      ESI12Week_PrcntlArray = ESI12Week_PrcntlArray[WhichRows[0], :]
#    if 'SPI_1_month' in InpLayersCombination:
#      SPI01_PrcntlArray = SPI01_PrcntlArray[WhichRows[0], :]
#    if 'SPI_2_month' in InpLayersCombination:
#      SPI02_PrcntlArray = SPI02_PrcntlArray[WhichRows[0], :]
#    if 'SPI_3_month' in InpLayersCombination:
#      SPI03_PrcntlArray = SPI03_PrcntlArray[WhichRows[0], :]
#    if 'SPI_6_month' in InpLayersCombination:
#      SPI06_PrcntlArray = SPI06_PrcntlArray[WhichRows[0], :]
#    if 'SPI_9_month' in InpLayersCombination:
#      SPI09_PrcntlArray = SPI09_PrcntlArray[WhichRows[0], :]
#    if 'SPI_12_month' in InpLayersCombination:
#      SPI12_PrcntlArray = SPI12_PrcntlArray[WhichRows[0], :]
#    if 'SPI_24_month' in InpLayersCombination:
#      SPI24_PrcntlArray = SPI24_PrcntlArray[WhichRows[0], :]
    if 'SPI_gamma_01_nCG' in InpLayersCombination:
      spi_gamma_01_PrcntlArray = spi_gamma_01_PrcntlArray[WhichRows[0], :]
    if 'SPI_gamma_02_nCG' in InpLayersCombination:
      spi_gamma_02_PrcntlArray = spi_gamma_02_PrcntlArray[WhichRows[0], :]
    if 'SPI_gamma_03_nCG' in InpLayersCombination:
      spi_gamma_03_PrcntlArray = spi_gamma_03_PrcntlArray[WhichRows[0], :]
    if 'SPI_gamma_06_nCG' in InpLayersCombination:
      spi_gamma_06_PrcntlArray = spi_gamma_06_PrcntlArray[WhichRows[0], :]
    if 'SPI_gamma_09_nCG' in InpLayersCombination:
      spi_gamma_09_PrcntlArray = spi_gamma_09_PrcntlArray[WhichRows[0], :]
    if 'SPI_gamma_12_nCG' in InpLayersCombination:
      spi_gamma_12_PrcntlArray = spi_gamma_12_PrcntlArray[WhichRows[0], :]
    if 'SPI_gamma_24_nCG' in InpLayersCombination:
      spi_gamma_24_PrcntlArray = spi_gamma_24_PrcntlArray[WhichRows[0], :]
    if 'SPI_gamma_36_nCG' in InpLayersCombination:
      spi_gamma_36_PrcntlArray = spi_gamma_36_PrcntlArray[WhichRows[0], :]
    if 'SPI_gamma_48_nCG' in InpLayersCombination:
      spi_gamma_48_PrcntlArray = spi_gamma_48_PrcntlArray[WhichRows[0], :]
    if 'SPI_gamma_60_nCG' in InpLayersCombination:
      spi_gamma_60_PrcntlArray = spi_gamma_60_PrcntlArray[WhichRows[0], :]
    if 'SPI_gamma_72_nCG' in InpLayersCombination:
      spi_gamma_72_PrcntlArray = spi_gamma_72_PrcntlArray[WhichRows[0], :]
    if 'SPEI_pear_01_nCG' in InpLayersCombination:
      spei_pearson_01_PrcntlArray = spei_pearson_01_PrcntlArray[WhichRows[0], :]
    if 'SPEI_pear_02_nCG' in InpLayersCombination:
      spei_pearson_02_PrcntlArray = spei_pearson_02_PrcntlArray[WhichRows[0], :]
    if 'SPEI_pear_03_nCG' in InpLayersCombination:
      spei_pearson_03_PrcntlArray = spei_pearson_03_PrcntlArray[WhichRows[0], :]
    if 'SPEI_pear_06_nCG' in InpLayersCombination:
      spei_pearson_06_PrcntlArray = spei_pearson_06_PrcntlArray[WhichRows[0], :]
    if 'SPEI_pear_09_nCG' in InpLayersCombination:
      spei_pearson_09_PrcntlArray = spei_pearson_09_PrcntlArray[WhichRows[0], :]
    if 'SPEI_pear_12_nCG' in InpLayersCombination:
      spei_pearson_12_PrcntlArray = spei_pearson_12_PrcntlArray[WhichRows[0], :]
    if 'SPEI_pear_24_nCG' in InpLayersCombination:
      spei_pearson_24_PrcntlArray = spei_pearson_24_PrcntlArray[WhichRows[0], :]
    if 'SPEI_pear_36_nCG' in InpLayersCombination:
      spei_pearson_36_PrcntlArray = spei_pearson_36_PrcntlArray[WhichRows[0], :]
    if 'SPEI_pear_48_nCG' in InpLayersCombination:
      spei_pearson_48_PrcntlArray = spei_pearson_48_PrcntlArray[WhichRows[0], :]
    if 'SPEI_pear_60_nCG' in InpLayersCombination:
      spei_pearson_60_PrcntlArray = spei_pearson_60_PrcntlArray[WhichRows[0], :]
    if 'SPEI_pear_72_nCG' in InpLayersCombination:
      spei_pearson_72_PrcntlArray = spei_pearson_72_PrcntlArray[WhichRows[0], :]
    if 'tavg_01_nCG' in InpLayersCombination:
      tavg_01_PrcntlArray = tavg_01_PrcntlArray[WhichRows[0], :]
    if 'tmax_01_nCG' in InpLayersCombination:
      tmax_01_PrcntlArray = tmax_01_PrcntlArray[WhichRows[0], :]
    if 'SNODAS' in InpLayersCombination:
      SNODAS_PrcntlArray = SNODAS_PrcntlArray[WhichRows[0], :]
    if 'ESA_CCI' in InpLayersCombination:
      ESA_CCI_PrcntlArray = ESA_CCI_PrcntlArray[WhichRows[0], :]
    if 'IMERG_01' in InpLayersCombination:
      IMERG_01_PrcntlArray = IMERG_01_PrcntlArray[WhichRows[0], :]
    if 'IMERG_02' in InpLayersCombination:
      IMERG_02_PrcntlArray = IMERG_02_PrcntlArray[WhichRows[0], :]
    if 'IMERG_03' in InpLayersCombination:
      IMERG_03_PrcntlArray = IMERG_03_PrcntlArray[WhichRows[0], :]
    if 'IMERG_06' in InpLayersCombination:
      IMERG_06_PrcntlArray = IMERG_06_PrcntlArray[WhichRows[0], :]
    if 'IMERG_09' in InpLayersCombination:
      IMERG_09_PrcntlArray = IMERG_09_PrcntlArray[WhichRows[0], :]
    if 'IMERG_12' in InpLayersCombination:
      IMERG_12_PrcntlArray = IMERG_12_PrcntlArray[WhichRows[0], :]
    if 'IMERG_24' in InpLayersCombination:
      IMERG_24_PrcntlArray = IMERG_24_PrcntlArray[WhichRows[0], :]
    if 'IMERG_36' in InpLayersCombination:
      IMERG_36_PrcntlArray = IMERG_36_PrcntlArray[WhichRows[0], :]
    if 'IMERG_48' in InpLayersCombination:
      IMERG_48_PrcntlArray = IMERG_48_PrcntlArray[WhichRows[0], :]
    if 'IMERG_60' in InpLayersCombination:
      IMERG_60_PrcntlArray = IMERG_60_PrcntlArray[WhichRows[0], :]
    if 'IMERG_72' in InpLayersCombination:
      IMERG_72_PrcntlArray = IMERG_72_PrcntlArray[WhichRows[0], :]
    if 'SmNDVI_BlendedVHP' in InpLayersCombination:
      SmNDVI_BlendedVHP_PrcntlArray = SmNDVI_BlendedVHP_PrcntlArray[WhichRows[0], :]
    if 'TCI_BlendedVHP' in InpLayersCombination:
      TCI_BlendedVHP_PrcntlArray = TCI_BlendedVHP_PrcntlArray[WhichRows[0], :]
    if 'VCI_BlendedVHP' in InpLayersCombination:
      VCI_BlendedVHP_PrcntlArray = VCI_BlendedVHP_PrcntlArray[WhichRows[0], :]
    if 'VHI_BlendedVHP' in InpLayersCombination:
      VHI_BlendedVHP_PrcntlArray = VHI_BlendedVHP_PrcntlArray[WhichRows[0], :]
    if 'GlobSnow3' in InpLayersCombination:
      GlobSnow3_PrcntlArray = GlobSnow3_PrcntlArray[WhichRows[0], :]

  #end of if ( (WhichSeason in ['P', 'U', 'F', 'W']) or...

  Target_Array = np.reshape(Target_Array, (Target_Array.size, 1))

  Inputs_Mat = np.copy(Target_Array) # REMEMBER to remove this 1st column below

  if 'Z_index' in InpLayersCombination:
    ZIndex_PrcntlArray = np.reshape(ZIndex_PrcntlArray, (ZIndex_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, ZIndex_PrcntlArray ), axis = 1)
  if 'Z_index_60_month' in InpLayersCombination:
    ZIndex60month_PrcntlArray = np.reshape(ZIndex60month_PrcntlArray, (ZIndex60month_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, ZIndex60month_PrcntlArray ), axis = 1)
  if 'PMDI' in InpLayersCombination:
    PMDI_PrcntlArray = np.reshape(PMDI_PrcntlArray, (PMDI_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, PMDI_PrcntlArray ), axis = 1)
  if 'PHDI' in InpLayersCombination:
    PHDI_PrcntlArray = np.reshape(PHDI_PrcntlArray, (PHDI_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, PHDI_PrcntlArray ), axis = 1)
  if 'prcp_01_nCG' in InpLayersCombination:
    prcp_01_PrcntlArray = np.reshape(prcp_01_PrcntlArray, (prcp_01_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_01_PrcntlArray ), axis = 1)
  if 'prcp_02_nCG' in InpLayersCombination:
    prcp_02_PrcntlArray = np.reshape(prcp_02_PrcntlArray, (prcp_02_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_02_PrcntlArray ), axis = 1)
  if 'prcp_03_nCG' in InpLayersCombination:
    prcp_03_PrcntlArray = np.reshape(prcp_03_PrcntlArray, (prcp_03_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_03_PrcntlArray ), axis = 1)
  if 'prcp_06_nCG' in InpLayersCombination:
    prcp_06_PrcntlArray = np.reshape(prcp_06_PrcntlArray, (prcp_06_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_06_PrcntlArray ), axis = 1)
  if 'prcp_09_nCG' in InpLayersCombination:
    prcp_09_PrcntlArray = np.reshape(prcp_09_PrcntlArray, (prcp_09_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_09_PrcntlArray ), axis = 1)
  if 'prcp_12_nCG' in InpLayersCombination:
    prcp_12_PrcntlArray = np.reshape(prcp_12_PrcntlArray, (prcp_12_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_12_PrcntlArray ), axis = 1)
  if 'prcp_24_nCG' in InpLayersCombination:
    prcp_24_PrcntlArray = np.reshape(prcp_24_PrcntlArray, (prcp_24_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_24_PrcntlArray ), axis = 1)
  if 'prcp_36_nCG' in InpLayersCombination:
    prcp_36_PrcntlArray = np.reshape(prcp_36_PrcntlArray, (prcp_36_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_36_PrcntlArray ), axis = 1)
  if 'prcp_48_nCG' in InpLayersCombination:
    prcp_48_PrcntlArray = np.reshape(prcp_48_PrcntlArray, (prcp_48_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_48_PrcntlArray ), axis = 1)
  if 'prcp_60_nCG' in InpLayersCombination:
    prcp_60_PrcntlArray = np.reshape(prcp_60_PrcntlArray, (prcp_60_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_60_PrcntlArray ), axis = 1)
  if 'prcp_72_nCG' in InpLayersCombination:
    prcp_72_PrcntlArray = np.reshape(prcp_72_PrcntlArray, (prcp_72_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_72_PrcntlArray ), axis = 1)
  if 'CPC_soil_moisture' in InpLayersCombination:
    CPCsoilmoist_PrcntlArray = np.reshape(CPCsoilmoist_PrcntlArray, (CPCsoilmoist_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, CPCsoilmoist_PrcntlArray ), axis = 1)
  if 'GRACE_DA_gw' in InpLayersCombination:
    GRACE_DA_gw_PrcntlArray = np.reshape(GRACE_DA_gw_PrcntlArray, (GRACE_DA_gw_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, GRACE_DA_gw_PrcntlArray ), axis = 1)
  if 'GRACE_DA_sfsm' in InpLayersCombination:
    GRACE_DA_sfsm_PrcntlArray = np.reshape(GRACE_DA_sfsm_PrcntlArray, (GRACE_DA_sfsm_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, GRACE_DA_sfsm_PrcntlArray ), axis = 1)
  if 'GRACE_DA_rzsm' in InpLayersCombination:
    GRACE_DA_rzsm_PrcntlArray = np.reshape(GRACE_DA_rzsm_PrcntlArray, (GRACE_DA_rzsm_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, GRACE_DA_rzsm_PrcntlArray ), axis = 1)
  if 'EDDI_1wk' in InpLayersCombination:
    EDDI1wk_PrcntlArray = np.reshape(EDDI1wk_PrcntlArray, (EDDI1wk_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI1wk_PrcntlArray ), axis = 1)
  if 'EDDI_2wk' in InpLayersCombination:
    EDDI2wk_PrcntlArray = np.reshape(EDDI2wk_PrcntlArray, (EDDI2wk_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI2wk_PrcntlArray ), axis = 1)
  if 'EDDI_3wk' in InpLayersCombination:
    EDDI3wk_PrcntlArray = np.reshape(EDDI3wk_PrcntlArray, (EDDI3wk_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI3wk_PrcntlArray ), axis = 1)
  if 'EDDI_4wk' in InpLayersCombination:
    EDDI4wk_PrcntlArray = np.reshape(EDDI4wk_PrcntlArray, (EDDI4wk_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI4wk_PrcntlArray ), axis = 1)
  if 'EDDI_5wk' in InpLayersCombination:
    EDDI5wk_PrcntlArray = np.reshape(EDDI5wk_PrcntlArray, (EDDI5wk_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI5wk_PrcntlArray ), axis = 1)
  if 'EDDI_6wk' in InpLayersCombination:
    EDDI6wk_PrcntlArray = np.reshape(EDDI6wk_PrcntlArray, (EDDI6wk_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI6wk_PrcntlArray ), axis = 1)
  if 'EDDI_7wk' in InpLayersCombination:
    EDDI7wk_PrcntlArray = np.reshape(EDDI7wk_PrcntlArray, (EDDI7wk_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI7wk_PrcntlArray ), axis = 1)
  if 'EDDI_8wk' in InpLayersCombination:
    EDDI8wk_PrcntlArray = np.reshape(EDDI8wk_PrcntlArray, (EDDI8wk_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI8wk_PrcntlArray ), axis = 1)
  if 'EDDI_9wk' in InpLayersCombination:
    EDDI9wk_PrcntlArray = np.reshape(EDDI9wk_PrcntlArray, (EDDI9wk_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI9wk_PrcntlArray ), axis = 1)
  if 'EDDI_10wk' in InpLayersCombination:
    EDDI10wk_PrcntlArray = np.reshape(EDDI10wk_PrcntlArray, (EDDI10wk_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI10wk_PrcntlArray ), axis = 1)
  if 'EDDI_11wk' in InpLayersCombination:
    EDDI11wk_PrcntlArray = np.reshape(EDDI11wk_PrcntlArray, (EDDI11wk_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI11wk_PrcntlArray ), axis = 1)
  if 'EDDI_12wk' in InpLayersCombination:
    EDDI12wk_PrcntlArray = np.reshape(EDDI12wk_PrcntlArray, (EDDI12wk_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI12wk_PrcntlArray ), axis = 1)
  if 'EDDI_1mn' in InpLayersCombination:
    EDDI1mn_PrcntlArray = np.reshape(EDDI1mn_PrcntlArray, (EDDI1mn_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI1mn_PrcntlArray ), axis = 1)
  if 'EDDI_2mn' in InpLayersCombination:
    EDDI2mn_PrcntlArray = np.reshape(EDDI2mn_PrcntlArray, (EDDI2mn_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI2mn_PrcntlArray ), axis = 1)
  if 'EDDI_3mn' in InpLayersCombination:
    EDDI3mn_PrcntlArray = np.reshape(EDDI3mn_PrcntlArray, (EDDI3mn_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI3mn_PrcntlArray ), axis = 1)
  if 'EDDI_4mn' in InpLayersCombination:
    EDDI4mn_PrcntlArray = np.reshape(EDDI4mn_PrcntlArray, (EDDI4mn_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI4mn_PrcntlArray ), axis = 1)
  if 'EDDI_5mn' in InpLayersCombination:
    EDDI5mn_PrcntlArray = np.reshape(EDDI5mn_PrcntlArray, (EDDI5mn_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI5mn_PrcntlArray ), axis = 1)
  if 'EDDI_6mn' in InpLayersCombination:
    EDDI6mn_PrcntlArray = np.reshape(EDDI6mn_PrcntlArray, (EDDI6mn_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI6mn_PrcntlArray ), axis = 1)
  if 'EDDI_7mn' in InpLayersCombination:
    EDDI7mn_PrcntlArray = np.reshape(EDDI7mn_PrcntlArray, (EDDI7mn_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI7mn_PrcntlArray ), axis = 1)
  if 'EDDI_8mn' in InpLayersCombination:
    EDDI8mn_PrcntlArray = np.reshape(EDDI8mn_PrcntlArray, (EDDI8mn_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI8mn_PrcntlArray ), axis = 1)
  if 'EDDI_9mn' in InpLayersCombination:
    EDDI9mn_PrcntlArray = np.reshape(EDDI9mn_PrcntlArray, (EDDI9mn_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI9mn_PrcntlArray ), axis = 1)
  if 'EDDI_10mn' in InpLayersCombination:
    EDDI10mn_PrcntlArray = np.reshape(EDDI10mn_PrcntlArray, (EDDI10mn_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI10mn_PrcntlArray ), axis = 1)
  if 'EDDI_11mn' in InpLayersCombination:
    EDDI11mn_PrcntlArray = np.reshape(EDDI11mn_PrcntlArray, (EDDI11mn_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI11mn_PrcntlArray ), axis = 1)
  if 'EDDI_12mn' in InpLayersCombination:
    EDDI12mn_PrcntlArray = np.reshape(EDDI12mn_PrcntlArray, (EDDI12mn_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI12mn_PrcntlArray ), axis = 1)
#  if 'NLDAS2_1mSM_Mosaic' in InpLayersCombination:
#    NLDAS2_1mSM_Mosaic_PrcntlArray = np.reshape(NLDAS2_1mSM_Mosaic_PrcntlArray, (NLDAS2_1mSM_Mosaic_PrcntlArray.size, 1))
#    Inputs_Mat = np.concatenate( (Inputs_Mat, NLDAS2_1mSM_Mosaic_PrcntlArray ), axis = 1)
#  if 'NLDAS2_1mSM_Noah' in InpLayersCombination:
#    NLDAS2_1mSM_Noah_PrcntlArray = np.reshape(NLDAS2_1mSM_Noah_PrcntlArray, (NLDAS2_1mSM_Noah_PrcntlArray.size, 1))
#    Inputs_Mat = np.concatenate( (Inputs_Mat, NLDAS2_1mSM_Noah_PrcntlArray ), axis = 1)
#  if 'NLDAS2_1mSM_SAC' in InpLayersCombination:
#    NLDAS2_1mSM_SAC_PrcntlArray = np.reshape(NLDAS2_1mSM_SAC_PrcntlArray, (NLDAS2_1mSM_SAC_PrcntlArray.size, 1))
#    Inputs_Mat = np.concatenate( (Inputs_Mat, NLDAS2_1mSM_SAC_PrcntlArray ), axis = 1)
#  if 'NLDAS2_1mSM_VIC' in InpLayersCombination:
#    NLDAS2_1mSM_VIC_PrcntlArray = np.reshape(NLDAS2_1mSM_VIC_PrcntlArray, (NLDAS2_1mSM_VIC_PrcntlArray.size, 1))
#    Inputs_Mat = np.concatenate( (Inputs_Mat, NLDAS2_1mSM_VIC_PrcntlArray ), axis = 1)
  if 'NLDAS2D_1MSM_Mosaic' in InpLayersCombination:
    Mosaic_1MSM_PrcntlArray = np.reshape(Mosaic_1MSM_PrcntlArray, (Mosaic_1MSM_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, Mosaic_1MSM_PrcntlArray ), axis = 1)
  if 'NLDAS2D_1MSM_Noah' in InpLayersCombination:
    Noah_1MSM_PrcntlArray = np.reshape(Noah_1MSM_PrcntlArray, (Noah_1MSM_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, Noah_1MSM_PrcntlArray ), axis = 1)
  if 'NLDAS2D_1MSM_SAC' in InpLayersCombination:
    SAC_1MSM_PrcntlArray = np.reshape(SAC_1MSM_PrcntlArray, (SAC_1MSM_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, SAC_1MSM_PrcntlArray ), axis = 1)
  if 'NLDAS2D_1MSM_VIC' in InpLayersCombination:
    VIC_1MSM_PrcntlArray = np.reshape(VIC_1MSM_PrcntlArray, (VIC_1MSM_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, VIC_1MSM_PrcntlArray ), axis = 1)
  if 'NLDAS2D_TCSM_Mosaic' in InpLayersCombination:
    Mosaic_TCSM_PrcntlArray = np.reshape(Mosaic_TCSM_PrcntlArray, (Mosaic_TCSM_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, Mosaic_TCSM_PrcntlArray ), axis = 1)
  if 'NLDAS2D_TCSM_Noah' in InpLayersCombination:
    Noah_TCSM_PrcntlArray = np.reshape(Noah_TCSM_PrcntlArray, (Noah_TCSM_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, Noah_TCSM_PrcntlArray ), axis = 1)
  if 'NLDAS2D_TCSM_SAC' in InpLayersCombination:
    SAC_TCSM_PrcntlArray = np.reshape(SAC_TCSM_PrcntlArray, (SAC_TCSM_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, SAC_TCSM_PrcntlArray ), axis = 1)
  if 'NLDAS2D_TCSM_VIC' in InpLayersCombination:
    VIC_TCSM_PrcntlArray = np.reshape(VIC_TCSM_PrcntlArray, (VIC_TCSM_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, VIC_TCSM_PrcntlArray ), axis = 1)
  if 'NLDAS2D_EVAP_Mosaic' in InpLayersCombination:
    Mosaic_EVAP_PrcntlArray = np.reshape(Mosaic_EVAP_PrcntlArray, (Mosaic_EVAP_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, Mosaic_EVAP_PrcntlArray ), axis = 1)
  if 'NLDAS2D_EVAP_Noah' in InpLayersCombination:
    Noah_EVAP_PrcntlArray = np.reshape(Noah_EVAP_PrcntlArray, (Noah_EVAP_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, Noah_EVAP_PrcntlArray ), axis = 1)
  if 'NLDAS2D_EVAP_SAC' in InpLayersCombination:
    SAC_EVAP_PrcntlArray = np.reshape(SAC_EVAP_PrcntlArray, (SAC_EVAP_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, SAC_EVAP_PrcntlArray ), axis = 1)
  if 'NLDAS2D_EVAP_VIC' in InpLayersCombination:
    VIC_EVAP_PrcntlArray = np.reshape(VIC_EVAP_PrcntlArray, (VIC_EVAP_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, VIC_EVAP_PrcntlArray ), axis = 1)
  if 'NLDAS2D_SWE_Mosaic' in InpLayersCombination:
    Mosaic_SWE_PrcntlArray = np.reshape(Mosaic_SWE_PrcntlArray, (Mosaic_SWE_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, Mosaic_SWE_PrcntlArray ), axis = 1)
  if 'NLDAS2D_SWE_Noah' in InpLayersCombination:
    Noah_SWE_PrcntlArray = np.reshape(Noah_SWE_PrcntlArray, (Noah_SWE_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, Noah_SWE_PrcntlArray ), axis = 1)
  if 'NLDAS2D_SWE_SAC' in InpLayersCombination:
    SAC_SWE_PrcntlArray = np.reshape(SAC_SWE_PrcntlArray, (SAC_SWE_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, SAC_SWE_PrcntlArray ), axis = 1)
  if 'NLDAS2D_SWE_VIC' in InpLayersCombination:
    VIC_SWE_PrcntlArray = np.reshape(VIC_SWE_PrcntlArray, (VIC_SWE_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, VIC_SWE_PrcntlArray ), axis = 1)
  if 'NLDAS2D_RUN_Mosaic' in InpLayersCombination:
    Mosaic_RUN_PrcntlArray = np.reshape(Mosaic_RUN_PrcntlArray, (Mosaic_RUN_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, Mosaic_RUN_PrcntlArray ), axis = 1)
  if 'NLDAS2D_RUN_Noah' in InpLayersCombination:
    Noah_RUN_PrcntlArray = np.reshape(Noah_RUN_PrcntlArray, (Noah_RUN_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, Noah_RUN_PrcntlArray ), axis = 1)
  if 'NLDAS2D_RUN_SAC' in InpLayersCombination:
    SAC_RUN_PrcntlArray = np.reshape(SAC_RUN_PrcntlArray, (SAC_RUN_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, SAC_RUN_PrcntlArray ), axis = 1)
  if 'NLDAS2D_RUN_VIC' in InpLayersCombination:
    VIC_RUN_PrcntlArray = np.reshape(VIC_RUN_PrcntlArray, (VIC_RUN_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, VIC_RUN_PrcntlArray ), axis = 1)
  if 'NLDAS2D_STRMH04_Mosaic' in InpLayersCombination:
    Mosaic_STRM_H04_PrcntlArray = np.reshape(Mosaic_STRM_H04_PrcntlArray, (Mosaic_STRM_H04_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, Mosaic_STRM_H04_PrcntlArray ), axis = 1)
  if 'NLDAS2D_STRMH04_Noah' in InpLayersCombination:
    Noah_STRM_H04_PrcntlArray = np.reshape(Noah_STRM_H04_PrcntlArray, (Noah_STRM_H04_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, Noah_STRM_H04_PrcntlArray ), axis = 1)
  if 'NLDAS2D_STRMH04_SAC' in InpLayersCombination:
    SAC_STRM_H04_PrcntlArray = np.reshape(SAC_STRM_H04_PrcntlArray, (SAC_STRM_H04_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, SAC_STRM_H04_PrcntlArray ), axis = 1)
  if 'NLDAS2D_STRMH04_VIC' in InpLayersCombination:
    VIC_STRM_H04_PrcntlArray = np.reshape(VIC_STRM_H04_PrcntlArray, (VIC_STRM_H04_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, VIC_STRM_H04_PrcntlArray ), axis = 1)
  if 'VegDRI' in InpLayersCombination:
    VegDRI_PrcntlArray = np.reshape(VegDRI_PrcntlArray, (VegDRI_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, VegDRI_PrcntlArray ), axis = 1)
  if 'QuickDRI' in InpLayersCombination:
    QuickDRI_PrcntlArray = np.reshape(QuickDRI_PrcntlArray, (QuickDRI_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, QuickDRI_PrcntlArray ), axis = 1)
#  if 'ESI' in InpLayersCombination:
#    ESI_PrcntlArray = np.reshape(ESI_PrcntlArray, (ESI_PrcntlArray.size, 1))
#    Inputs_Mat = np.concatenate( (Inputs_Mat, ESI_PrcntlArray ), axis = 1)
  if 'ESI_4wk' in InpLayersCombination:
    ESI4Week_PrcntlArray = np.reshape(ESI4Week_PrcntlArray, (ESI4Week_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, ESI4Week_PrcntlArray ), axis = 1)
  if 'ESI_12wk' in InpLayersCombination:
    ESI12Week_PrcntlArray = np.reshape(ESI12Week_PrcntlArray, (ESI12Week_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, ESI12Week_PrcntlArray ), axis = 1)
#  if 'SPI_1_month' in InpLayersCombination:
#    SPI01_PrcntlArray = np.reshape(SPI01_PrcntlArray, (SPI01_PrcntlArray.size, 1))
#    Inputs_Mat = np.concatenate( (Inputs_Mat, SPI01_PrcntlArray ), axis = 1)
#  if 'SPI_2_month' in InpLayersCombination:
#    SPI02_PrcntlArray = np.reshape(SPI02_PrcntlArray, (SPI02_PrcntlArray.size, 1))
#    Inputs_Mat = np.concatenate( (Inputs_Mat, SPI02_PrcntlArray ), axis = 1)
#  if 'SPI_3_month' in InpLayersCombination:
#    SPI03_PrcntlArray = np.reshape(SPI03_PrcntlArray, (SPI03_PrcntlArray.size, 1))
#    Inputs_Mat = np.concatenate( (Inputs_Mat, SPI03_PrcntlArray ), axis = 1)
#  if 'SPI_6_month' in InpLayersCombination:
#    SPI06_PrcntlArray = np.reshape(SPI06_PrcntlArray, (SPI06_PrcntlArray.size, 1))
#    Inputs_Mat = np.concatenate( (Inputs_Mat, SPI06_PrcntlArray ), axis = 1)
#  if 'SPI_9_month' in InpLayersCombination:
#    SPI09_PrcntlArray = np.reshape(SPI09_PrcntlArray, (SPI09_PrcntlArray.size, 1))
#    Inputs_Mat = np.concatenate( (Inputs_Mat, SPI09_PrcntlArray ), axis = 1)
#  if 'SPI_12_month' in InpLayersCombination:
#    SPI12_PrcntlArray = np.reshape(SPI12_PrcntlArray, (SPI12_PrcntlArray.size, 1))
#    Inputs_Mat = np.concatenate( (Inputs_Mat, SPI12_PrcntlArray ), axis = 1)
#  if 'SPI_24_month' in InpLayersCombination:
#    SPI24_PrcntlArray = np.reshape(SPI24_PrcntlArray, (SPI24_PrcntlArray.size, 1))
#    Inputs_Mat = np.concatenate( (Inputs_Mat, SPI24_PrcntlArray ), axis = 1)
  if 'SPI_gamma_01_nCG' in InpLayersCombination:
    spi_gamma_01_PrcntlArray = np.reshape(spi_gamma_01_PrcntlArray, (spi_gamma_01_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_01_PrcntlArray ), axis = 1)
  if 'SPI_gamma_02_nCG' in InpLayersCombination:
    spi_gamma_02_PrcntlArray = np.reshape(spi_gamma_02_PrcntlArray, (spi_gamma_02_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_02_PrcntlArray ), axis = 1)
  if 'SPI_gamma_03_nCG' in InpLayersCombination:
    spi_gamma_03_PrcntlArray = np.reshape(spi_gamma_03_PrcntlArray, (spi_gamma_03_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_03_PrcntlArray ), axis = 1)
  if 'SPI_gamma_06_nCG' in InpLayersCombination:
    spi_gamma_06_PrcntlArray = np.reshape(spi_gamma_06_PrcntlArray, (spi_gamma_06_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_06_PrcntlArray ), axis = 1)
  if 'SPI_gamma_09_nCG' in InpLayersCombination:
    spi_gamma_09_PrcntlArray = np.reshape(spi_gamma_09_PrcntlArray, (spi_gamma_09_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_09_PrcntlArray ), axis = 1)
  if 'SPI_gamma_12_nCG' in InpLayersCombination:
    spi_gamma_12_PrcntlArray = np.reshape(spi_gamma_12_PrcntlArray, (spi_gamma_12_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_12_PrcntlArray ), axis = 1)
  if 'SPI_gamma_24_nCG' in InpLayersCombination:
    spi_gamma_24_PrcntlArray = np.reshape(spi_gamma_24_PrcntlArray, (spi_gamma_24_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_24_PrcntlArray ), axis = 1)
  if 'SPI_gamma_36_nCG' in InpLayersCombination:
    spi_gamma_36_PrcntlArray = np.reshape(spi_gamma_36_PrcntlArray, (spi_gamma_36_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_36_PrcntlArray ), axis = 1)
  if 'SPI_gamma_48_nCG' in InpLayersCombination:
    spi_gamma_48_PrcntlArray = np.reshape(spi_gamma_48_PrcntlArray, (spi_gamma_48_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_48_PrcntlArray ), axis = 1)
  if 'SPI_gamma_60_nCG' in InpLayersCombination:
    spi_gamma_60_PrcntlArray = np.reshape(spi_gamma_60_PrcntlArray, (spi_gamma_60_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_60_PrcntlArray ), axis = 1)
  if 'SPI_gamma_72_nCG' in InpLayersCombination:
    spi_gamma_72_PrcntlArray = np.reshape(spi_gamma_72_PrcntlArray, (spi_gamma_72_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_72_PrcntlArray ), axis = 1)
  if 'SPEI_pear_01_nCG' in InpLayersCombination:
    spei_pearson_01_PrcntlArray = np.reshape(spei_pearson_01_PrcntlArray, (spei_pearson_01_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_01_PrcntlArray ), axis = 1)
  if 'SPEI_pear_02_nCG' in InpLayersCombination:
    spei_pearson_02_PrcntlArray = np.reshape(spei_pearson_02_PrcntlArray, (spei_pearson_02_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_02_PrcntlArray ), axis = 1)
  if 'SPEI_pear_03_nCG' in InpLayersCombination:
    spei_pearson_03_PrcntlArray = np.reshape(spei_pearson_03_PrcntlArray, (spei_pearson_03_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_03_PrcntlArray ), axis = 1)
  if 'SPEI_pear_06_nCG' in InpLayersCombination:
    spei_pearson_06_PrcntlArray = np.reshape(spei_pearson_06_PrcntlArray, (spei_pearson_06_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_06_PrcntlArray ), axis = 1)
  if 'SPEI_pear_09_nCG' in InpLayersCombination:
    spei_pearson_09_PrcntlArray = np.reshape(spei_pearson_09_PrcntlArray, (spei_pearson_09_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_09_PrcntlArray ), axis = 1)
  if 'SPEI_pear_12_nCG' in InpLayersCombination:
    spei_pearson_12_PrcntlArray = np.reshape(spei_pearson_12_PrcntlArray, (spei_pearson_12_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_12_PrcntlArray ), axis = 1)
  if 'SPEI_pear_24_nCG' in InpLayersCombination:
    spei_pearson_24_PrcntlArray = np.reshape(spei_pearson_24_PrcntlArray, (spei_pearson_24_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_24_PrcntlArray ), axis = 1)
  if 'SPEI_pear_36_nCG' in InpLayersCombination:
    spei_pearson_36_PrcntlArray = np.reshape(spei_pearson_36_PrcntlArray, (spei_pearson_36_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_36_PrcntlArray ), axis = 1)
  if 'SPEI_pear_48_nCG' in InpLayersCombination:
    spei_pearson_48_PrcntlArray = np.reshape(spei_pearson_48_PrcntlArray, (spei_pearson_48_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_48_PrcntlArray ), axis = 1)
  if 'SPEI_pear_60_nCG' in InpLayersCombination:
    spei_pearson_60_PrcntlArray = np.reshape(spei_pearson_60_PrcntlArray, (spei_pearson_60_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_60_PrcntlArray ), axis = 1)
  if 'SPEI_pear_72_nCG' in InpLayersCombination:
    spei_pearson_72_PrcntlArray = np.reshape(spei_pearson_72_PrcntlArray, (spei_pearson_72_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_72_PrcntlArray ), axis = 1)
  if 'tavg_01_nCG' in InpLayersCombination:
    tavg_01_PrcntlArray = np.reshape(tavg_01_PrcntlArray, (tavg_01_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, tavg_01_PrcntlArray ), axis = 1)
  if 'tmax_01_nCG' in InpLayersCombination:
    tmax_01_PrcntlArray = np.reshape(tmax_01_PrcntlArray, (tmax_01_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, tmax_01_PrcntlArray ), axis = 1)
  if 'SNODAS' in InpLayersCombination:
    SNODAS_PrcntlArray = np.reshape(SNODAS_PrcntlArray, (SNODAS_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, SNODAS_PrcntlArray ), axis = 1)
  if 'ESA_CCI' in InpLayersCombination:
    ESA_CCI_PrcntlArray = np.reshape(ESA_CCI_PrcntlArray, (ESA_CCI_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, ESA_CCI_PrcntlArray ), axis = 1)
  if 'IMERG_01' in InpLayersCombination:
    IMERG_01_PrcntlArray = np.reshape(IMERG_01_PrcntlArray, (IMERG_01_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_01_PrcntlArray ), axis = 1)
  if 'IMERG_02' in InpLayersCombination:
    IMERG_02_PrcntlArray = np.reshape(IMERG_02_PrcntlArray, (IMERG_02_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_02_PrcntlArray ), axis = 1)
  if 'IMERG_03' in InpLayersCombination:
    IMERG_03_PrcntlArray = np.reshape(IMERG_03_PrcntlArray, (IMERG_03_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_03_PrcntlArray ), axis = 1)
  if 'IMERG_06' in InpLayersCombination:
    IMERG_06_PrcntlArray = np.reshape(IMERG_06_PrcntlArray, (IMERG_06_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_06_PrcntlArray ), axis = 1)
  if 'IMERG_09' in InpLayersCombination:
    IMERG_09_PrcntlArray = np.reshape(IMERG_09_PrcntlArray, (IMERG_09_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_09_PrcntlArray ), axis = 1)
  if 'IMERG_12' in InpLayersCombination:
    IMERG_12_PrcntlArray = np.reshape(IMERG_12_PrcntlArray, (IMERG_12_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_12_PrcntlArray ), axis = 1)
  if 'IMERG_24' in InpLayersCombination:
    IMERG_24_PrcntlArray = np.reshape(IMERG_24_PrcntlArray, (IMERG_24_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_24_PrcntlArray ), axis = 1)
  if 'IMERG_36' in InpLayersCombination:
    IMERG_36_PrcntlArray = np.reshape(IMERG_36_PrcntlArray, (IMERG_36_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_36_PrcntlArray ), axis = 1)
  if 'IMERG_48' in InpLayersCombination:
    IMERG_48_PrcntlArray = np.reshape(IMERG_48_PrcntlArray, (IMERG_48_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_48_PrcntlArray ), axis = 1)
  if 'IMERG_60' in InpLayersCombination:
    IMERG_60_PrcntlArray = np.reshape(IMERG_60_PrcntlArray, (IMERG_60_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_60_PrcntlArray ), axis = 1)
  if 'IMERG_72' in InpLayersCombination:
    IMERG_72_PrcntlArray = np.reshape(IMERG_72_PrcntlArray, (IMERG_72_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_72_PrcntlArray ), axis = 1)
  if 'SmNDVI_BlendedVHP' in InpLayersCombination:
    SmNDVI_BlendedVHP_PrcntlArray = np.reshape(SmNDVI_BlendedVHP_PrcntlArray, (SmNDVI_BlendedVHP_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, SmNDVI_BlendedVHP_PrcntlArray ), axis = 1)
  if 'TCI_BlendedVHP' in InpLayersCombination:
    TCI_BlendedVHP_PrcntlArray = np.reshape(TCI_BlendedVHP_PrcntlArray, (TCI_BlendedVHP_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, TCI_BlendedVHP_PrcntlArray ), axis = 1)
  if 'VCI_BlendedVHP' in InpLayersCombination:
    VCI_BlendedVHP_PrcntlArray = np.reshape(VCI_BlendedVHP_PrcntlArray, (VCI_BlendedVHP_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, VCI_BlendedVHP_PrcntlArray ), axis = 1)
  if 'VHI_BlendedVHP' in InpLayersCombination:
    VHI_BlendedVHP_PrcntlArray = np.reshape(VHI_BlendedVHP_PrcntlArray, (VHI_BlendedVHP_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, VHI_BlendedVHP_PrcntlArray ), axis = 1)
  if 'GlobSnow3' in InpLayersCombination:
    GlobSnow3_PrcntlArray = np.reshape(GlobSnow3_PrcntlArray, (GlobSnow3_PrcntlArray.size, 1))
    Inputs_Mat = np.concatenate( (Inputs_Mat, GlobSnow3_PrcntlArray ), axis = 1)
  #end of if 'Z_index' in InpLayersCombination

  Inputs_Mat = Inputs_Mat[:, 1:] # PER 'REMEMBER' comment above

  ValidRows = np.where( ~np.isnan(np.sum(Inputs_Mat, axis = 1)) )
  Target_Array = Target_Array[ ValidRows[0], :]
  Inputs_Mat = Inputs_Mat[ ValidRows[0], :]

  return Target_Array, Inputs_Mat

#end of def GetInpAndTargArraysFromFile(XYDatas, InpLayersCombination, IfSpatialSubDomain, WhichCols, IfMakeTargetBinary, IfIncludeD0AsDrought, WhichSeason, Event_BeginDateVecList, Event_EndDateVecList)

Train_Target_Array, Train_Inputs_Mat = GetInpAndTargArraysFromFile(TrainDatas, InpLayersCombination, IfSpatialSubDomain, WhichCols, IfMakeTargetBinary, IfIncludeD0AsDrought, WhichSeason, Event_BeginDateVecList, Event_EndDateVecList)

if SpatialSubDomain[0:5] == 'Event':
  
  All_Inputs_Mat = np.copy( Train_Inputs_Mat )
  All_Target_Array = np.copy( Train_Target_Array )

else:

  Dev_Target_Array, Dev_Inputs_Mat = GetInpAndTargArraysFromFile(DevDatas, InpLayersCombination, IfSpatialSubDomain, WhichCols, IfMakeTargetBinary, IfIncludeD0AsDrought, WhichSeason, Event_BeginDateVecList, Event_EndDateVecList)
  Test_Target_Array, Test_Inputs_Mat = GetInpAndTargArraysFromFile(TestDatas, InpLayersCombination, IfSpatialSubDomain, WhichCols, IfMakeTargetBinary, IfIncludeD0AsDrought, WhichSeason, Event_BeginDateVecList, Event_EndDateVecList)

  All_Inputs_Mat = np.concatenate( ( Train_Inputs_Mat, Dev_Inputs_Mat, Test_Inputs_Mat ) )
  All_Target_Array = np.concatenate( ( Train_Target_Array, Dev_Target_Array, Test_Target_Array ) )

#end of if SpatialSubDomain[0:5] == 'Event'

##All_Target_Array = All_Target_Array[:, 0]

#ColCombinations = np.loadtxt('Combinations' + NumInpsForNDFracMI + 'of' + str(NumInpLayers) + '.txt', dtype = 'int', ndmin = 2)
ColCombinations = np.loadtxt('Combinations' + NumInpsForNDFracMI + 'of' + str(len(InpLayersCombination)) + '.txt', dtype = 'int', ndmin = 2)
SelectCols = ColCombinations[WhichInpCombinForNDFracMI, :]
SelectCols = SelectCols - 1
All_Inputs_Mat = All_Inputs_Mat[:, SelectCols] 

def calc_MI_info(Inp_name_key, Targ_name_key, Inp_array_key, Targ_array_key, If_discrete_features_key, Num_random_states_key, n_neighbors_key, Inp_names_list_key, MI_values_list_key, MI_lowersofrange_list_key, MI_uppersofrange_list_key, MI_ranges_list_key, sample_sizes_list_key, Entropy_list_key, RelMI_values_list_key, RelMI_lowersofrange_list_key, RelMI_uppersofrange_list_key):
  XX = Inp_array_key[:,0:1]
  YY = Targ_array_key[:,0:1]
  Idxs = np.where((~np.isnan(XX)) & (~np.isnan(YY)))
  XX = XX[Idxs[0]]
  YY = YY[Idxs[0]]
  YY = YY[:,0]
  Percentiles_for_n_neighbors = np.empty((3,))
  Percentiles_for_n_neighbors[:] = np.NaN
  MIs_this_n_neighbors = np.empty((Num_random_states_key,))
  MIs_this_n_neighbors[:] = np.NaN
  for Which_Random_state_value in range(Num_random_states_key):
    Random_state_value = 3 + Which_Random_state_value*100
    MIs_this_n_neighbors[Which_Random_state_value] = mutual_info_classif(XX,YY,discrete_features=If_discrete_features_key, n_neighbors=n_neighbors_key, copy=True, random_state = Random_state_value)
  Percentiles_for_n_neighbors[0] = np.percentile(MIs_this_n_neighbors, 5)
  Percentiles_for_n_neighbors[1] = np.percentile(MIs_this_n_neighbors, 50)
  Percentiles_for_n_neighbors[2] = np.percentile(MIs_this_n_neighbors, 95)
  print(Inp_name_key,": median MI ", Percentiles_for_n_neighbors[1], ", MI 90-perc range ",Percentiles_for_n_neighbors[2]-Percentiles_for_n_neighbors[0], ", sample size ", YY.size)
  Unique_YY_values, unique_counts = np.unique(YY, return_counts=True)
  YY_probabs = unique_counts / sum(unique_counts)
  Entropyy = entropy(YY_probabs)
  Inp_names_list_key.append(Inp_name_key)
  MI_values_list_key.append(Percentiles_for_n_neighbors[1])
  MI_lowersofrange_list_key.append(Percentiles_for_n_neighbors[0])
  MI_uppersofrange_list_key.append(Percentiles_for_n_neighbors[2])
  MI_ranges_list_key.append(Percentiles_for_n_neighbors[2]-Percentiles_for_n_neighbors[0])
  sample_sizes_list_key.append(YY.size)
  Entropy_list_key.append(Entropyy)
  RelMI_values_list_key.append(Percentiles_for_n_neighbors[1]/Entropyy)
  RelMI_lowersofrange_list_key.append(Percentiles_for_n_neighbors[0]/Entropyy)
  RelMI_uppersofrange_list_key.append(Percentiles_for_n_neighbors[2]/Entropyy)

  return Inp_names_list_key, MI_values_list_key, MI_lowersofrange_list_key, MI_uppersofrange_list_key, MI_ranges_list_key, sample_sizes_list_key, Entropy_list_key, RelMI_values_list_key, RelMI_lowersofrange_list_key, RelMI_uppersofrange_list_key
#end of def calc_MI_info

def calc_MI_1ValueForMultiFeatures(Inp_array_key, Targ_array_key, If_discrete_features_key, Num_random_states_key, n_neighbors_key):
  XX = np.copy(Inp_array_key)
  YY = Targ_array_key[:,0:1]
#  Idxs = np.where((~np.isnan(XX)) & (~np.isnan(YY)))
  Idxs = np.where( ( np.reshape(np.all( ~np.isnan(XX) & ~np.isnan(YY), axis = 1 ), (-1, 1)) ) )
  XX = XX[Idxs[0]]
  YY = YY[Idxs[0]]
  YY = YY[:,0]
  Percentiles_for_n_neighbors = np.empty((3,))
  Percentiles_for_n_neighbors[:] = np.NaN
  MIs_this_n_neighbors = np.empty((Num_random_states_key,))
  MIs_this_n_neighbors[:] = np.NaN
  for Which_Random_state_value in range(Num_random_states_key):
    Random_state_value = 3 + Which_Random_state_value*100
#    MIs_this_n_neighbors[Which_Random_state_value] = mutual_info_classif(XX,YY,discrete_features=If_discrete_features_key, n_neighbors=n_neighbors_key, copy=True, random_state = Random_state_value)
    MIs_this_n_neighbors[Which_Random_state_value] = MI_classif_1ValueForMultiFeatures(XX,YY,discrete_features=If_discrete_features_key, n_neighbors=n_neighbors_key, copy=True, random_state = Random_state_value)
  Percentiles_for_n_neighbors[0] = np.percentile(MIs_this_n_neighbors, 5)
  Percentiles_for_n_neighbors[1] = np.percentile(MIs_this_n_neighbors, 50)
  Percentiles_for_n_neighbors[2] = np.percentile(MIs_this_n_neighbors, 95)
  print("All-features-together : median MI ", Percentiles_for_n_neighbors[1], ", MI 90-perc range ",Percentiles_for_n_neighbors[2]-Percentiles_for_n_neighbors[0], ", sample size ", YY.size)
  Unique_YY_values, unique_counts = np.unique(YY, return_counts=True)
  YY_probabs = unique_counts / sum(unique_counts)
  Entropyy = entropy(YY_probabs)
  MI_value = Percentiles_for_n_neighbors[1]
  MI_lowerofrange = Percentiles_for_n_neighbors[0]
  MI_upperofrange = Percentiles_for_n_neighbors[2]
  MI_range = Percentiles_for_n_neighbors[2]-Percentiles_for_n_neighbors[0]
  sample_size = YY.size
  RelMI_value = Percentiles_for_n_neighbors[1]/Entropyy
  RelMI_lowerofrange = Percentiles_for_n_neighbors[0]/Entropyy
  RelMI_upperofrange = Percentiles_for_n_neighbors[2]/Entropyy

  print ('MI_value is ',MI_value)
  print ('MI_lowerofrange is ',MI_lowerofrange)
  print ('MI_upperofrange is ',MI_upperofrange)
  print ('MI_range is ',MI_range)
  print ('sample_size is ',sample_size)
  print ('Entropyy is ',Entropyy)
  print ('RelMI_value is ',RelMI_value)
  print ('RelMI_lowerofrange is ',RelMI_lowerofrange)
  print ('RelMI_upperofrange is ',RelMI_upperofrange)

  return MI_value, MI_lowerofrange, MI_upperofrange, MI_range, sample_size, Entropyy, RelMI_value, RelMI_lowerofrange, RelMI_upperofrange
#end of def calc_MI_1ValueForMultiFeatures

Inp_names_list = []

if SelectCols.size == 1:

  MI_values_list = []
  MI_lowersofrange_list = []
  MI_uppersofrange_list = []
  MI_ranges_list = []
  sample_sizes_list = []
  Entropy_list = []
  RelMI_values_list = []
  RelMI_lowersofrange_list = []
  RelMI_uppersofrange_list = []

  Inp_names_list, MI_values_list, MI_lowersofrange_list, MI_uppersofrange_list, MI_ranges_list, sample_sizes_list, Entropy_list, RelMI_values_list, RelMI_lowersofrange_list, RelMI_uppersofrange_list = calc_MI_info(Inp_name_key = DictofNumNamePairs_Channels[SelectCols[0]+1], Targ_name_key = TargetVariable, Inp_array_key = All_Inputs_Mat, Targ_array_key = All_Target_Array, If_discrete_features_key = False, Num_random_states_key = Num_random_states, n_neighbors_key = n_neighbors, Inp_names_list_key = Inp_names_list, MI_values_list_key = MI_values_list, MI_lowersofrange_list_key = MI_lowersofrange_list, MI_uppersofrange_list_key = MI_uppersofrange_list, MI_ranges_list_key = MI_ranges_list, sample_sizes_list_key = sample_sizes_list, Entropy_list_key = Entropy_list, RelMI_values_list_key = RelMI_values_list, RelMI_lowersofrange_list_key = RelMI_lowersofrange_list, RelMI_uppersofrange_list_key = RelMI_uppersofrange_list)

  print ('Inp_names_list is ',Inp_names_list)
  print ('MI_values_list is ',MI_values_list)
  print ('MI_lowersofrange_list is ',MI_lowersofrange_list)
  print ('MI_uppersofrange_list is ',MI_uppersofrange_list)
  print ('MI_ranges_list is ',MI_ranges_list)
  print ('sample_sizes_list is ',sample_sizes_list)
  print('len(MI_values_list) is ',len(MI_values_list))
  print ('Entropy_list is ',Entropy_list)
  print ('RelMI_values_list is ',RelMI_values_list)
  print ('RelMI_lowersofrange_list is ',RelMI_lowersofrange_list)
  print ('RelMI_uppersofrange_list is ',RelMI_uppersofrange_list)

  RelMI_value = RelMI_values_list[0]

else: # else of if SelectCols.size == 1

  if NumInpLayers >= 0:
    for ii in range(SelectCols.size):
      Inp_names_list.append(DictofNumNamePairs_Channels[SelectCols[ii]+1])
    print ('Inp_names_list is ',Inp_names_list)
  else:
    print ('Inp_names_list is ', InpLayersCombination)

  MI_value, MI_lowerofrange, MI_upperofrange, MI_range, sample_size, Entropyy, RelMI_value, RelMI_lowerofrange, RelMI_upperofrange = calc_MI_1ValueForMultiFeatures(Inp_array_key = All_Inputs_Mat, Targ_array_key = All_Target_Array, If_discrete_features_key = False, Num_random_states_key = Num_random_states, n_neighbors_key = n_neighbors)

#end of if SelectCols.size == 1

RelMI_value = np.array([RelMI_value])
np.savetxt(FracI_ClimDivs_AllValid_NDFeat_FileName, RelMI_value)

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")

