#!/bin/bash

nPixels="469758"
#FAME_PATH="/discover/nobackup/projects/fame/syatheen/NIDIS_Runs"
#NCA_PATH="/discover/nobackup/projects/nca/syatheen/NIDIS_Runs"

echo "Indicator: $1"
if (( $1 < 0 )); then
    theString="$1"
    IndicatorMinus1="${theString:1:2}"
else
    IndicatorMinus1=$((${1} - 1))
fi

for fileSystem in "fame" "nca"; do
    PATH_INDICATOR="/discover/nobackup/projects/${fileSystem}/syatheen/NIDIS_Runs/indicator_${1}"
    if [ -d "${PATH_INDICATOR}" ]; then
        echo "${PATH_INDICATOR}"
        echo "------------------------------------------------"
        for season in A P U F W; do
            if [ -d "$PATH_INDICATOR/${season}" ]; then
                echo "Starting season ${season}"

                seasonStatus=`ls $PATH_INDICATOR/${season} |wc -l`
                seasonRemainingStatus=$(($nPixels - $seasonStatus))
                if [ "$seasonStatus" = "$nPixels" ]; then
                    status="Done"
                else
                    status="Progress"

                    echo "Doing 0 to 9"
                    if (( $1 < 0 )); then
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_?_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                    else
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_?_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                    fi
                    desiredPixelsStatus=$((10 * 3))
                    if [ "$desiredPixelsStatus" != "$pixelsStatus" ]; then
                        if (( $1 < 0 )); then
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_?_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                        else
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_?_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                        fi
                        pixelsStatus3=$(($pixelsStatus / 3))
                        if [ "$pixelsStatus3" != "$pixelsStatus2" ]; then
                            echo "Problem in pixels 0 to 9! # Values desired: ${desiredPixelsStatus}, obtained: ${pixelsStatus}. # Pixel files printed : ${pixelsStatus2}, but obtained # values seem to indicate : ${pixelsStatus3}" 
                        else    
                            desiredPixelsStatus2=10
                            remainingPixelsStatus2=$(($desiredPixelsStatus2 - $pixelsStatus2))
                            echo "Problem in pixels 0 to 9! # Pixel files finished : ${pixelsStatus2}, remaining : ${remainingPixelsStatus2}"
                        fi
                    fi

                fi
                echo "${season} - ${seasonStatus} - ${status}; Remaining ${seasonRemainingStatus}"
                echo "------------------------------------------------"
            fi
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
