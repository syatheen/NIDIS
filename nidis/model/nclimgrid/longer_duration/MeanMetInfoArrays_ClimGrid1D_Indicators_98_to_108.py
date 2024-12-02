#!/usr/bin/env python
from __future__ import division
import sys
import numpy as np
from datetime import datetime
import os
from calendar import monthrange

#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        ArgNumDaysMean
#ArgNum   1          

#######BEGIN ANY EDITS REQUIRED#######

def main():

  BeginYYYYMM = [2000, 6]
  EndYYYYMM = [2021, 5]

  # int(round(float(sys.argv[1])))
  NumDaysMean = 2191 # indicator 108

  if NumDaysMean == 30:
    NumMonthsMean = 1
  elif NumDaysMean == 60:
    NumMonthsMean = 2
  elif NumDaysMean == 90:
    NumMonthsMean = 3
  elif NumDaysMean == 180:
    NumMonthsMean = 6
  elif NumDaysMean == 270:
    NumMonthsMean = 9
  elif NumDaysMean == 365:
    NumMonthsMean = 12
  elif NumDaysMean == 730:
    NumMonthsMean = 24
  elif NumDaysMean == 1095:
    NumMonthsMean = 36
  elif NumDaysMean == 1461:
    NumMonthsMean = 48
  elif NumDaysMean == 1826:
    NumMonthsMean = 60
  elif NumDaysMean == 2191:
    NumMonthsMean = 72

  OutFilePath = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/IMERG_Npzs/InfoArrsDailyMean/ClimGrid1D'
  os.makedirs(OutFilePath, exist_ok=True)

  #######END ANY EDITS REQUIRED#########

  ssstart_Overall = datetime.now()

  WhetherRead1stFile = False
  for WhichYear in range(BeginYYYYMM[0], EndYYYYMM[0]+1):

    if WhichYear == BeginYYYYMM[0]:
      BeginMonth = BeginYYYYMM[1]
    else:
      BeginMonth = 1
    #end of if WhichYear == BeginYYYYMM[0]

    if WhichYear == EndYYYYMM[0]:
      EndMonth = EndYYYYMM[1]
    else:
      EndMonth = 12
    #end of if WhichYear == EndYYYYMM[0]

    for WhichMonth in range(BeginMonth, EndMonth+1):

      InfoArrayFile_Info = np.load('/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/IMERG_Npzs/daily_Final_V06/IMERG_' + format(WhichYear,'04') + format(WhichMonth,'02') + '_ClimGrid1D.npz')
  
      This_YYYYMMDD_Of_RefArrayForPrcntl = InfoArrayFile_Info['YYYYMMDD_Of_RefArrayForPrcntl']
      This_RefArrayForPrcntl = InfoArrayFile_Info['RefArrayForPrcntl']
      
      if not WhetherRead1stFile:
        YYYYMMDD_Of_InfoArrayForPrcntl = np.copy(This_YYYYMMDD_Of_RefArrayForPrcntl)
        InfoArrayForPrcntl = np.copy(This_RefArrayForPrcntl)
        WhetherRead1stFile = True
      else:
        YYYYMMDD_Of_InfoArrayForPrcntl = np.concatenate((YYYYMMDD_Of_InfoArrayForPrcntl, This_YYYYMMDD_Of_RefArrayForPrcntl), axis = 0)
        InfoArrayForPrcntl = np.concatenate((InfoArrayForPrcntl, This_RefArrayForPrcntl), axis = 0)
      #end of if not WhetherRead1stFile

    #end of for WhichMonth in range(BeginMonth, EndMonth+1)

  #end of for WhichYear in range(BeginYYYYMM[0], EndYYYYMM[0]+1)

  aa = np.isnan(InfoArrayForPrcntl).sum()
  print("aa is ", aa)

  if (np.isnan(InfoArrayForPrcntl).sum() != 0):

    print("ERROR: Null/NaN values mean we cannot use current cumsum technique!!!")
    sys.exit(0)

  else:

    print("YYYYMMDD_Of_InfoArrayForPrcntl.shape is ", YYYYMMDD_Of_InfoArrayForPrcntl.shape)
    print("YYYYMMDD_Of_InfoArrayForPrcntl is ", YYYYMMDD_Of_InfoArrayForPrcntl)
    print("InfoArrayForPrcntl.shape is ", InfoArrayForPrcntl.shape)
    print("InfoArrayForPrcntl is ", InfoArrayForPrcntl)
    print('overall min is ',np.amin(InfoArrayForPrcntl),', overall max is ',np.amax(InfoArrayForPrcntl))

    #Begin for n-month mean
    InfoArrayForPrcntl = InfoArrayForPrcntl / NumDaysMean
    InfoArrayForPrcntl = InfoArrayForPrcntl.cumsum(axis=0)
    InfoArrayForPrcntl[NumDaysMean:] = InfoArrayForPrcntl[NumDaysMean:] - InfoArrayForPrcntl[:-NumDaysMean]
    YYYYMMDD_Of_InfoArrayForPrcntl = YYYYMMDD_Of_InfoArrayForPrcntl[NumDaysMean-1:]
    InfoArrayForPrcntl = InfoArrayForPrcntl[NumDaysMean-1:]
    #End for n-month mean

    print("\nAFTER MEAN:")
    print("=============")
    print("YYYYMMDD_Of_InfoArrayForPrcntl.shape is ", YYYYMMDD_Of_InfoArrayForPrcntl.shape)
    print("YYYYMMDD_Of_InfoArrayForPrcntl is ", YYYYMMDD_Of_InfoArrayForPrcntl)
    print("InfoArrayForPrcntl.shape is ", InfoArrayForPrcntl.shape)
    print("InfoArrayForPrcntl is ", InfoArrayForPrcntl)
    print('overall min is ',np.amin(InfoArrayForPrcntl),', overall max is ',np.amax(InfoArrayForPrcntl))

    BeginYear = int(np.round(YYYYMMDD_Of_InfoArrayForPrcntl[0] // 10000))
    BeginMonth = int(np.round((YYYYMMDD_Of_InfoArrayForPrcntl[0] - 10000 * BeginYear) // 100))
    BeginDayOfMonth = int(np.round(YYYYMMDD_Of_InfoArrayForPrcntl[0] % 100))
    EndYear = int(np.round(YYYYMMDD_Of_InfoArrayForPrcntl[-1] // 10000))
    EndMonth = int(np.round((YYYYMMDD_Of_InfoArrayForPrcntl[-1] - 10000 * EndYear) // 100))
    EndDayOfMonth = int(np.round(YYYYMMDD_Of_InfoArrayForPrcntl[-1] % 100))

    np.savez_compressed(
      os.path.join(OutFilePath, 'IMERG' + str(int(round(NumMonthsMean))) + 'MonthsMean_'  + format(BeginYear, '04') + format(BeginMonth, '02') + format(BeginDayOfMonth, '02') + 'To' + format(EndYear, '04') + format(EndMonth, '02') + format(EndDayOfMonth, '02') + '.npz'),
      YYYYMMDD_Of_InfoArrayForPrcntl = YYYYMMDD_Of_InfoArrayForPrcntl, InfoArrayForPrcntl = InfoArrayForPrcntl
    )

  #end of if (np.isnan(InfoArrayForPrcntl).sum() != 0)

  eeend_Overall = datetime.now()
  eeelapsed_Overall = eeend_Overall - ssstart_Overall
  print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")

  return



# -----------------------------------------------------------------------------
# Invoke the main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
