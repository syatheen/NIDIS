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
NUMBER_NODES=10
PATH_TO_TASKS=`pwd`
TASK_FILENAMES=(`ls ${PATH_TO_TASKS}/tasks*.conf`)
TASK_FILENAMES_COUNT=${#TASK_FILENAMES[@]}
FILES_PER_NODE=$(( (TASK_FILENAMES_COUNT / NUMBER_NODES) + (TASK_FILENAMES_COUNT % NUMBER_NODES > 0 ) ))

echo "Total number of task filenames ${#TASK_FILENAMES[@]}"
echo "Starting sbatch submission with ${NUMBER_NODES} nodes"
echo "Splitting task config files from ${PATH_TO_TASKS}"
echo "Processing ${TASK_FILENAMES_COUNT} task filenames"
echo "Tasks filenames per node ${FILES_PER_NODE}"

counter=1
for (( i=0; i < NUMBER_NODES; i++))
do
    # gather task ids
    start_task=$counter
    end_task=$((counter + FILES_PER_NODE))
    if [[ $end_task -gt $TASK_FILENAMES_COUNT ]]
    then
        end_task=$((TASK_FILENAMES_COUNT + 1))
    fi
    echo "START AND END TASK" $start_task $end_task
    counter=$((counter + FILES_PER_NODE))

    # call sbatch script
    sbatch sbatch_submission.sh $start_task $end_task $PATH_TO_TASKS

done
