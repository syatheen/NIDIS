#!/bin/bash

# Version 2024.03.11
# Author: Jordan A. Caraballo-Vega, jordan.a.caraballo-vega@nasa.gov

# You can add the tasks creation script here if you would like
# to make it part of the initial submission as well. Replace
# the environment listed below with your own environment.
# This script is meant to be run from Discover's login nodes.
# The input to that script is a configuration file that includes
# the parameters in each line. For example:
#
# 467856 468368 20060103 20191231 38 P 513
# 468369 468881 20060103 20191231 38 P 513
# 468882 469394 20060103 20191231 38 P 513 
#
# To create the individual task files, uncomment the following line.
# Note that the Python environment is loaded in this file, so you will
# need to replace this Python environment. The input to that file is the
# configuration file explained above.
#
# bash 1_create_tasks_file.sh 1_NClcFI_ClmGrd1D_V2b_1DFeatSeas_Parameters.conf
#
# Once the tasks are created, we proceed to submit the individual jobs.
# Our job limit is 6000 cores at a time, this we can have a max of 
# 46 Milan nodes if we request the full nodes. Depending on our time requirements,
# we will split the task files based on the number of nodes we want to use.
# Based on benchmarking, splitting the tasks in 46 nodes finishes the entire
# process in an hour, with the challenge that we will need to wait for the jobs to
# start. For a better number, selecting 10 nodes and splitting the tasks against them
# provides acceptable performance.
#
# Provide the number of nodes you would like to use
NUMBER_NODES=40
TOTAL_NUMBER_OF_TASKS=469758

#PATH_TO_TASKS=`pwd`
#TASK_FILENAMES=(`ls ${PATH_TO_TASKS}/tasks*.conf`)
#TASK_FILENAMES_COUNT=${#TASK_FILENAMES[@]}
TASKS_PER_NODE=$(( (TOTAL_NUMBER_OF_TASKS / NUMBER_NODES) + (TOTAL_NUMBER_OF_TASKS % NUMBER_NODES > 0 ) ))

echo "Starting sbatch submission with ${NUMBER_NODES} nodes"
echo "Processing ${TOTAL_NUMBER_OF_TASKS} tasks"
echo "Tasks filenames per node ${TASKS_PER_NODE}"
echo "Running indicator: ${1}, for seasons ${2}, and saving under ${3}"

counter=0
for (( i=0; i < NUMBER_NODES; i++))
do
    # gather task ids
    start_task=$counter
    end_task=$((counter + TASKS_PER_NODE))
    if [[ $end_task -gt $TOTAL_NUMBER_OF_TASKS ]]
    then
        end_task=$((TOTAL_NUMBER_OF_TASKS))
    fi
    echo "START AND END TASK" $start_task $end_task
    counter=$((counter + TASKS_PER_NODE))

    # call sbatch script
    # 1 - indicator, 2 - seasons, 3 - filesystem
    sbatch -J "NID_${1}" sbatch_submission_single_indicator_multi_epoch.sh $1 "$2" $3 $start_task $end_task $4

done
