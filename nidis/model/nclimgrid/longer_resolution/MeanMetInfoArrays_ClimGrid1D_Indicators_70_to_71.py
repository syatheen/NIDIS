from __future__ import division
import sys
import numpy as np
from datetime import datetime
import os
from calendar import monthrange

#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        NumDaysMean
#ArgNum   1          

#######BEGIN ANY EDITS REQUIRED#######

def main():

  BeginYYYYMM = [2000, 1]
  EndYYYYMM = [2020, 5]

  # TODO: will change based on the indicator number
  # find how it was called
  # 28 or 84
  NumDaysMean = int(round(float(sys.argv[1])))

  if NumDaysMean == 28:
    NumWeeksMean = 4
  elif NumDaysMean == 84:
    NumWeeksMean = 12
  
  OutFilePath = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/ESI_Npzs/InfoArrsDailyMean/ClimGrid1D/'
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

      # TODO: I LEFT HERE FIXING THE PATHS
      # where is the spatial resolution stuff for here
      InfoArrayFile_Info = np.load('/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/Indicators_70_to_71/spatial_resolution/InfoArrsDaily/' + format(WhichYear,'04') + format(WhichMonth,'02') + '.npz')
  
      # TODO: double check because the other one has YYYYMMDD_Of_RefArrayForPrcntl
      This_YYYYMMDD_Of_RefArrayForPrcntl = InfoArrayFile_Info['YYYYMMDD_Of_RefPrcntlArray']

      # TODO: double check because the other one has RefArrayForPrcntl
      This_RefArrayForPrcntl = InfoArrayFile_Info['RefPrcntlArray']
      
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

  # ADDED FROM THE 98 to 108 indicators
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
    print('overall min is ',np.nanmin(InfoArrayForPrcntl),', overall max is ',np.nanmax(InfoArrayForPrcntl))

    # DIFFERENCES STARTING HERE BETWEEN 98 to 108 and 70 to 71

    #Begin for n-week mean
    InfoArrayForPrcntl_ncs = np.nancumsum(InfoArrayForPrcntl, axis=0)
    InfoArrayForPrcntl_ncs[NumDaysMean:] = InfoArrayForPrcntl_ncs[NumDaysMean:] - InfoArrayForPrcntl_ncs[:-NumDaysMean]
    IsNans = np.array(~np.isnan(InfoArrayForPrcntl), dtype = int)
    IsNans_ncs = np.nancumsum(IsNans, axis=0)
    IsNans_ncs[NumDaysMean:] = IsNans_ncs[NumDaysMean:] - IsNans_ncs[:-NumDaysMean]
    InfoArrayForPrcntl = np.divide(InfoArrayForPrcntl_ncs, IsNans_ncs)
    #End for n-week mean

    print("\nAFTER MEAN:")
    print("=============")
    print("YYYYMMDD_Of_InfoArrayForPrcntl.shape is ", YYYYMMDD_Of_InfoArrayForPrcntl.shape)
    print("YYYYMMDD_Of_InfoArrayForPrcntl is ", YYYYMMDD_Of_InfoArrayForPrcntl)
    print("InfoArrayForPrcntl.shape is ", InfoArrayForPrcntl.shape)
    print("InfoArrayForPrcntl is ", InfoArrayForPrcntl)
    print('overall min is ',np.nanmin(InfoArrayForPrcntl),', overall max is ',np.nanmax(InfoArrayForPrcntl))

    BeginYear = int(round(BeginYYYYMM[0]))
    BeginMonth = int(round(BeginYYYYMM[1]))
    BeginDayOfMonth = int(round((YYYYMMDD_Of_InfoArrayForPrcntl[0] % 100)[0]))
    print("BeginDayOfMonth is ", BeginDayOfMonth)
    #print("(YYYYMMDD_Of_InfoArrayForPrcntl[0] % 100).shape is ", (YYYYMMDD_Of_InfoArrayForPrcntl[0] % 100).shape)
    EndYear = int(round(EndYYYYMM[0]))
    EndMonth = int(round(EndYYYYMM[1]))
    EndDayOfMonth = int(round((YYYYMMDD_Of_InfoArrayForPrcntl[-1] % 100)[0]))
    print("EndDayOfMonth is ", EndDayOfMonth)
    #print("(YYYYMMDD_Of_InfoArrayForPrcntl[-1] % 100).shape is ", (YYYYMMDD_Of_InfoArrayForPrcntl[-1] % 100).shape)

    np.savez_compressed(
      OutFilePath + 'ESI' + str(int(round(NumWeeksMean))) + 'WeeksMean_'  \
        + format(BeginYear, '04') + format(BeginMonth, '02') + format(BeginDayOfMonth, '02') + \
        'To' + format(EndYear, '04') + format(EndMonth, '02') + format(EndDayOfMonth, '02') \
          + '.npz', YYYYMMDD_Of_InfoArrayForPrcntl = YYYYMMDD_Of_InfoArrayForPrcntl, InfoArrayForPrcntl = InfoArrayForPrcntl
    )

  eeend_Overall = datetime.now()
  eeelapsed_Overall = eeend_Overall - ssstart_Overall
  print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")

  return

# -----------------------------------------------------------------------------
# Invoke the main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()