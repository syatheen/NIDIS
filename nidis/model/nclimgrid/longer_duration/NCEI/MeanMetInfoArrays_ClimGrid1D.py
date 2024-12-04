from __future__ import division
import sys
import numpy as np
from datetime import datetime
#import os

#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        ArgVariable ArgNumMonthsMean
#ArgNum   1           2          
 
#######BEGIN ANY EDITS REQUIRED#######

BeginYear = 1895
BeginMonth = 1
EndYear = 2021
EndMonth = 7

VariabStr = sys.argv[1] # possible values are 'prcp', 'pet', 'tavg', 'tmax'

NumMonthsMean = int(round(float(sys.argv[2]))) # Choices are 2, 3, 6, 9, 12, 24, 36, 48, 72

OutFilePath = 'InfoArrsNMonthsMean/ClimGrid1D/'

#######END ANY EDITS REQUIRED#########

ssstart_Overall = datetime.now()

WhetherRead1stFile = False
for WhichYear in range(BeginYear, EndYear+1):

  if WhichYear == BeginYear:
    BeginMonth_ThisYear = BeginMonth
  else:
    BeginMonth_ThisYear = 1

  if WhichYear == EndYear:
    EndMonth_ThisYear = EndMonth
  else:
    EndMonth_ThisYear = 12

  for WhichMonth in range(BeginMonth_ThisYear, EndMonth_ThisYear+1):

    InfoArrayFile_Info = np.load('/discover/nobackup/projects/nca/syatheen/nClimGrid_ClimGrid1D_Npzs/' + VariabStr + '_' + format(WhichYear,'04') + format(WhichMonth,'02') + '_1DClimGrid.npz')
 
    This_YYYYMM_Of_RefArrayForPrcntl = InfoArrayFile_Info['YYYYMM_Of_RefArrayForPrcntl']
    This_RefArrayForPrcntl = InfoArrayFile_Info['RefArrayForPrcntl']
    
    if not WhetherRead1stFile:
      YYYYMM_Of_InfoArrayForPrcntl = np.copy(This_YYYYMM_Of_RefArrayForPrcntl)
      InfoArrayForPrcntl = np.copy(This_RefArrayForPrcntl)
      WhetherRead1stFile = True
    else:
      YYYYMM_Of_InfoArrayForPrcntl = np.concatenate((YYYYMM_Of_InfoArrayForPrcntl, This_YYYYMM_Of_RefArrayForPrcntl), axis = 0)
      InfoArrayForPrcntl = np.concatenate((InfoArrayForPrcntl, This_RefArrayForPrcntl), axis = 0)
    #end of if not WhetherRead1stFile

  #end of for WhichMonth in range(BeginMonth_ThisYear, EndMonth_ThisYear+1)

#end of for WhichYear in range(BeginYear, EndYear+1)

aa = np.isnan(InfoArrayForPrcntl).sum()
print("aa is ", aa)

if (np.isnan(InfoArrayForPrcntl).sum() != 0):

  print("ERROR: Null/NaN values imply we cannot use current cumsum technique!!!")
  sys.exit(0)

else:

  print("Initial YYYYMM_Of_InfoArrayForPrcntl.shape is ", YYYYMM_Of_InfoArrayForPrcntl.shape)
  print("Initial YYYYMM_Of_InfoArrayForPrcntl is ", YYYYMM_Of_InfoArrayForPrcntl)
  print("Initial InfoArrayForPrcntl.shape is ", InfoArrayForPrcntl.shape)
  print("Initial InfoArrayForPrcntl is ", InfoArrayForPrcntl)
  print('Initial overall min is ',np.amin(InfoArrayForPrcntl),', overall max is ',np.amax(InfoArrayForPrcntl))

  #Begin for n-month accum
  InfoArrayForPrcntl = InfoArrayForPrcntl / NumMonthsMean
  InfoArrayForPrcntl = InfoArrayForPrcntl.cumsum(axis=0)
  InfoArrayForPrcntl[NumMonthsMean:] = InfoArrayForPrcntl[NumMonthsMean:] - InfoArrayForPrcntl[:-NumMonthsMean]
  YYYYMM_Of_InfoArrayForPrcntl = YYYYMM_Of_InfoArrayForPrcntl[NumMonthsMean-1:]
  InfoArrayForPrcntl = InfoArrayForPrcntl[NumMonthsMean-1:]
  #End for n-month mean

  print("\nAFTER MEAN:")
  print("=============")
  print("Final YYYYMM_Of_InfoArrayForPrcntl.shape is ", YYYYMM_Of_InfoArrayForPrcntl.shape)
  print("Final YYYYMM_Of_InfoArrayForPrcntl is ", YYYYMM_Of_InfoArrayForPrcntl)
  print("Final InfoArrayForPrcntl.shape is ", InfoArrayForPrcntl.shape)
  print("Final InfoArrayForPrcntl is ", InfoArrayForPrcntl)
  print('Final overall min is ',np.amin(InfoArrayForPrcntl),', overall max is ',np.amax(InfoArrayForPrcntl))

  BeginYear = int(round(YYYYMM_Of_InfoArrayForPrcntl[0,0] // 100))
  BeginMonth = int(round(YYYYMM_Of_InfoArrayForPrcntl[0,0] - 100 * BeginYear))
  EndYear = int(round(YYYYMM_Of_InfoArrayForPrcntl[-1,0] // 100))
  EndMonth = int(round(YYYYMM_Of_InfoArrayForPrcntl[-1,0] - 100 * EndYear))

  np.savez_compressed(OutFilePath + VariabStr + str(int(round(NumMonthsMean))) + 'MonthsMean_'  + format(BeginYear, '04') + format(BeginMonth, '02') + 'To' + format(EndYear, '04') + format(EndMonth, '02') + '.npz', YYYYMM_Of_InfoArrayForPrcntl = YYYYMM_Of_InfoArrayForPrcntl, InfoArrayForPrcntl = InfoArrayForPrcntl) 

#end of if (np.isnan(InfoArrayForPrcntl).sum() != 0)

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")


