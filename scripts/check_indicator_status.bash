#!/bin/bash

nPixels="469758"
FAME_PATH="/discover/nobackup/projects/fame/jacaraba/NIDIS_Runs"
NCA_PATH="/discover/nobackup/projects/nca/jacaraba/NIDIS_Runs"

echo "Indicator: $1"
for fileSystem in "fame" "nca"; do
    PATH_INDICATOR="/discover/nobackup/projects/${fileSystem}/jacaraba/NIDIS_Runs/indicator_${1}"
    if [ -d "${PATH_INDICATOR}" ]; then
        echo "${PATH_INDICATOR}"
        for season in A P U F W; do
            seasonStatus=`ls $PATH_INDICATOR/${season} |wc -l`
            if [ "$seasonStatus" = "$nPixels" ]; then
                status="Done"
            else
                status="Progress"
            fi
            echo "${season} - ${seasonStatus} - ${status}"
        done
    fi
done

#FAME_PATH_INDICATOR="${FAME_PATH}/indicator_${1}"
#if [ -d "${FAME_PATH_INDICATOR}" ]; then
    #P_STATUS=`ls $FAME_PATH_INDICATOR/P |wc -l`
    #U_STATUS=`ls $FAME_PATH_INDICATOR/U |wc -l`
    #echo "P: `ls $FAME_PATH_INDICATOR/P |wc -l`"
    #echo "U: `ls $FAME_PATH_INDICATOR/U |wc -l`"
    #echo "F: `ls $FAME_PATH_INDICATOR/F |wc -l`"
    #echo "W: `ls $FAME_PATH_INDICATOR/W |wc -l`"
    
#fi
