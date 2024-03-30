#!/bin/bash

# This script creates the tasks needed for the next step of multiprocessing
# scripts to process. The output is a set of configuration files to
# process by the main script.

module load python/GEOSpyD/Min23.5.2-0_py3.11
source activate /home/jacaraba/.conda/envs/amy-rf

COUNTER=1
cat $1 | while read line 
do
    python Create_Tasks_Conf_file.py $line $COUNTER
    COUNTER=$(( COUNTER + 1 ))
done
