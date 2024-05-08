#!/usr/bin/env python
# Coded by Soni Yatheendradas
#         on Jan 12, 2024
from __future__ import division
from datetime import datetime, timedelta, date
import os
import sys
#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        BeginningPixelInAVariableNSeason  EndingPixelInAVariableNSeason  BeginningYYYYMMDD_str  EndingYYYYMMDD_str  ZeroStartInputNum_str   WhichSeason  NumTotalTasksInConf 
#ArgNum   1                                 2                              3                      4                   5                       6            7 

# BEGIN code arguments / editable section

BeginningPixelInAVariableNSeason = int(round(float(sys.argv[1]))) 

EndingPixelInAVariableNSeason = int(round(float(sys.argv[2]))) 

BeginningYYYYMMDD_str = sys.argv[3]

EndingYYYYMMDD_str = sys.argv[4]

ZeroStartInputNum_str = sys.argv[5]

WhichSeason = sys.argv[6]

NumTotalTasksInConf = int(round(float(sys.argv[7])))

ConfFileName = f'tasks{sys.argv[8]}.conf'

# END code arguments / editable section

ssstart_Overall = datetime.now()

# Begin delete of existing exec file
if os.path.exists(ConfFileName):
  cmd = '/bin/rm ' + ConfFileName
  os.system(cmd)
# End delete of existing exec file

TaskIdx = int(0)

for ThisPixelInAVariableNSeason in range(BeginningPixelInAVariableNSeason, EndingPixelInAVariableNSeason + 1):

#2 ./RunProc_ClcFI1X1_ClmGrd1D_V2b_NDFeat_NewSeas_V2_mil.sh N N 20060606 20191231 USDM CONUS 113 1 107 400002 A

  cmd = 'echo ' + str(TaskIdx) + ' ./RunProc_ClcFI1X1_ClmGrd1D_V2b_NDFeat_NewSeas_V2_mil.sh N N ' + BeginningYYYYMMDD_str + ' ' + EndingYYYYMMDD_str + ' USDM CONUS 113 1 ' + ZeroStartInputNum_str + ' ' + str(ThisPixelInAVariableNSeason) + ' ' + WhichSeason  + '  >> ' + ConfFileName 
  os.system(cmd)

  TaskIdx = TaskIdx + 1

#end of for ThisPixelInAVariableNSeason in range(BeginningPixelInAVariableNSeason, EndingPixelInAVariableNSeason + 1)

NumFinishedTasksInConf = EndingPixelInAVariableNSeason - BeginningPixelInAVariableNSeason + 1

NumRemainingTasksInConf = NumTotalTasksInConf - NumFinishedTasksInConf 

for ThisPixelInAVariableNSeason in range(NumRemainingTasksInConf):

  cmd = 'echo ' + str(TaskIdx) + ' ./RunProc_ClcFI1X1_ClmGrd1D_V2b_NDFeat_NewSeas_V2_mil.sh N N ' + BeginningYYYYMMDD_str + ' ' + EndingYYYYMMDD_str + ' USDM CONUS 113 1 ' + ZeroStartInputNum_str + ' ' + str(ThisPixelInAVariableNSeason) + ' ' + WhichSeason  + '  >> ' + ConfFileName 
  os.system(cmd)

  TaskIdx = TaskIdx + 1

#end of for ThisPixelInAVariableNSeason in range(NumRemainingTasksInConf)

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")


