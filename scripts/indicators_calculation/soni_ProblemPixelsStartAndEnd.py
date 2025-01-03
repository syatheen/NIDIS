#!/usr/bin/env python
# Coded by Soni Yatheendradas
#         on Dec 31, 2024
import sys
import os
import copy
import numpy as np
#NOTE: sys.argv indices start at 1, not 0
#Python arguments to this program will be (for now):
#        indicator season begin_pixel_of_range end_pixel_of_range
#ArgNum   1         2      3                    4

indicator = int(round(float(sys.argv[1])))
season = sys.argv[2]
begin_pixel_of_range = int(round(float(sys.argv[3])))
end_pixel_of_range = int(round(float(sys.argv[4])))
FI_dir = f'/discover/nobackup/projects/fame/syatheen/NIDIS_Runs/indicator_{indicator}/{season}'

for WhichPixel in range(begin_pixel_of_range, end_pixel_of_range + 1):
    FI_filename = os.path.join(
            FI_dir,
            'NN_U_C_' + str(WhichPixel) + '_In113_' + str(indicator - 1) + '_' + season + '.txt'
        )
    if not os.path.exists(FI_filename):
        begin_problemPixel = copy.deepcopy(WhichPixel)
        break 
    #end of if not os.path.exists(output_filename)
#end of for WhichPixel in range(begin_pixel_of_range, end_pixel_of_range + 1)

for WhichPixel in range(end_pixel_of_range, begin_pixel_of_range - 1, -1):
    FI_filename = os.path.join(
            FI_dir,
            'NN_U_C_' + str(WhichPixel) + '_In113_' + str(indicator - 1) + '_' + season + '.txt'
        )
    if not os.path.exists(FI_filename):
        end_problemPixel = copy.deepcopy(WhichPixel)
        break 
    #end of if not os.path.exists(output_filename)
#end of for WhichPixel in range(end_pixel_of_range, begin_pixel_of_range - 1, -1)

print("Problem pixels range: ")
if ( ('begin_problemPixel' in locals()) or ('begin_problemPixel' in globals()) ):
    print(begin_problemPixel, " to ")
if ( ('end_problemPixel' in locals()) or ('end_problemPixel' in globals()) ):
    print(end_problemPixel)

            
