#!/usr/bin/env python
# Coded by Soni Yatheendradas
#         on May 2, 2025

from datetime import datetime
import os
import numpy as np

# SY: BEGIN ANY EDITS REQUIRED

CommandsFilesForReruns = 'CommandsFilesForReruns_M12_U'

PixelFileName_Pre = '/discover/nobackup/projects/fame/syatheen/NIDIS_Runs/indicator_-12/U/NN_U_C_' 
PixelFileName_Post = '_InM12_0_U.txt' 

Command_Part1 = 'python /discover/nobackup/syatheen/development/nidis/nidis/view/CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_CLI.py --indicator -12 --season U --init-task ' 
Command_Part2 = ' --end-task '
Command_Part3 = ' --output-dir /discover/nobackup/projects/fame/syatheen/NIDIS_Runs --step train --n-processes 1 \n'

NumPixels = 469758

CommandsForReruns_obj = open(CommandsFilesForReruns, 'w')

# SY: END ANY EDITS REQUIRED

ssstart_Overall = datetime.now()

for WhichPixel in range(NumPixels):

    if WhichPixel%50000 == 0:
        print("At WhichPixel: ", WhichPixel)
    PixelFileName = PixelFileName_Pre + str(int(round(float(WhichPixel)))) + PixelFileName_Post

    if not os.path.exists(PixelFileName):
        CommandsForReruns_obj.write(Command_Part1 + str(int(round(float(WhichPixel)))) + Command_Part2 + str(int(round(float(WhichPixel + 1)))) + Command_Part3)
        print("Redo WhichPixel: ", WhichPixel)
    #end of if os.path.exists(PixelFileName)

#end of for WhichPixel in range(NumPixels)

CommandsForReruns_obj.close()

eeend_Overall = datetime.now()
eeelapsed_Overall = eeend_Overall - ssstart_Overall
print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")



