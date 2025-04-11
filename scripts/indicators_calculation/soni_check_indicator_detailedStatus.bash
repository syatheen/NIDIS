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

                    echo "Doing 10 to 99"
                    if (( $1 < 0 )); then
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_??_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                    else
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_??_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                    fi
                    desiredPixelsStatus=$((90 * 3))
                    if [ "$desiredPixelsStatus" != "$pixelsStatus" ]; then
                        if (( $1 < 0 )); then
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_??_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                        else
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_??_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                        fi
                        pixelsStatus3=$(($pixelsStatus / 3))
                        if [ "$pixelsStatus3" != "$pixelsStatus2" ]; then
                            echo "Problem in pixels 10 to 99! # Values desired: ${desiredPixelsStatus}, obtained: ${pixelsStatus}. # Pixel files printed : ${pixelsStatus2}, but obtained # values seem to indicate : ${pixelsStatus3}" 
                        else    
                            desiredPixelsStatus2=90
                            remainingPixelsStatus2=$(($desiredPixelsStatus2 - $pixelsStatus2))
                            echo "Problem in pixels 10 to 99! # Pixel files finished : ${pixelsStatus2}, remaining : ${remainingPixelsStatus2}"
                        fi
                    fi

                    echo "Doing 100 to 999"
                    if (( $1 < 0 )); then
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_???_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                    else
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_???_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                    fi
                    desiredPixelsStatus=$((900 * 3))
                    if [ "$desiredPixelsStatus" != "$pixelsStatus" ]; then
                        if (( $1 < 0 )); then
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_???_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                        else
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_???_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                        fi
                        pixelsStatus3=$(($pixelsStatus / 3))
                        if [ "$pixelsStatus3" != "$pixelsStatus2" ]; then
                            echo "Problem in pixels 100 to 999! # Values desired: ${desiredPixelsStatus}, obtained: ${pixelsStatus}. # Pixel files printed : ${pixelsStatus2}, but obtained # values seem to indicate : ${pixelsStatus3}" 
                        else    
                            desiredPixelsStatus2=900
                            remainingPixelsStatus2=$(($desiredPixelsStatus2 - $pixelsStatus2))
                            echo "Problem in pixels 100 to 999! # Pixel files finished : ${pixelsStatus2}, remaining : ${remainingPixelsStatus2}"
                        fi
                    fi

                    echo "Doing 1000 to 9999"
                    if (( $1 < 0 )); then
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                    else
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                    fi
                    desiredPixelsStatus=$((9000 * 3))
                    if [ "$desiredPixelsStatus" != "$pixelsStatus" ]; then
                        if (( $1 < 0 )); then
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                        else
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                        fi
                        pixelsStatus3=$(($pixelsStatus / 3))
                        if [ "$pixelsStatus3" != "$pixelsStatus2" ]; then
                            echo "Problem in pixels 1000 to 9999! # Values desired: ${desiredPixelsStatus}, obtained: ${pixelsStatus}. # Pixel files printed : ${pixelsStatus2}, but obtained # values seem to indicate : ${pixelsStatus3}" 
                        else    
                            desiredPixelsStatus2=9000
                            remainingPixelsStatus2=$(($desiredPixelsStatus2 - $pixelsStatus2))
                            echo "Problem in pixels 1000 to 9999! # Pixel files finished : ${pixelsStatus2}, remaining : ${remainingPixelsStatus2}"
                        fi
                    fi

                    echo "Doing 10000 to 49999"
                    if (( $1 < 0 )); then
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_[1-4]????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                    else
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_[1-4]????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                    fi
                    desiredPixelsStatus=$((40000 * 3))
                    if [ "$desiredPixelsStatus" != "$pixelsStatus" ]; then
                        if (( $1 < 0 )); then
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_[1-4]????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                        else
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_[1-4]????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                        fi
                        pixelsStatus3=$(($pixelsStatus / 3))
                        if [ "$pixelsStatus3" != "$pixelsStatus2" ]; then
                            echo "Problem in pixels 10000 to 49999! # Values desired: ${desiredPixelsStatus}, obtained: ${pixelsStatus}. # Pixel files printed : ${pixelsStatus2}, but obtained # values seem to indicate : ${pixelsStatus3}" 
                        else    
                            desiredPixelsStatus2=40000
                            remainingPixelsStatus2=$(($desiredPixelsStatus2 - $pixelsStatus2))
                            echo "Problem in pixels 10000 to 49999! # Pixel files finished : ${pixelsStatus2}, remaining : ${remainingPixelsStatus2}"
                        fi
                    fi

                    echo "Doing 50000 to 99999"
                    if (( $1 < 0 )); then
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_[5-9]????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                    else
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_[5-9]????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                    fi
                    desiredPixelsStatus=$((50000 * 3))
                    if [ "$desiredPixelsStatus" != "$pixelsStatus" ]; then
                        if (( $1 < 0 )); then
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_[5-9]????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                        else
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_[5-9]????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                        fi
                        pixelsStatus3=$(($pixelsStatus / 3))
                        if [ "$pixelsStatus3" != "$pixelsStatus2" ]; then
                            echo "Problem in pixels 50000 to 99999! # Values desired: ${desiredPixelsStatus}, obtained: ${pixelsStatus}. # Pixel files printed : ${pixelsStatus2}, but obtained # values seem to indicate : ${pixelsStatus3}" 
                        else    
                            desiredPixelsStatus2=50000
                            remainingPixelsStatus2=$(($desiredPixelsStatus2 - $pixelsStatus2))
                            echo "Problem in pixels 50000 to 99999! # Pixel files finished : ${pixelsStatus2}, remaining : ${remainingPixelsStatus2}"
                        fi
                    fi

                    echo "Doing 100000 to 149999"
                    if (( $1 < 0 )); then
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_1[0-4]????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                    else
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_1[0-4]????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                    fi
                    desiredPixelsStatus=$((50000 * 3))
                    if [ "$desiredPixelsStatus" != "$pixelsStatus" ]; then
                        if (( $1 < 0 )); then
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_1[0-4]????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                        else
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_1[0-4]????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                        fi
                        pixelsStatus3=$(($pixelsStatus / 3))
                        if [ "$pixelsStatus3" != "$pixelsStatus2" ]; then
                            echo "Problem in pixels 100000 to 149999! # Values desired: ${desiredPixelsStatus}, obtained: ${pixelsStatus}. # Pixel files printed : ${pixelsStatus2}, but obtained # values seem to indicate : ${pixelsStatus3}" 
                        else    
                            desiredPixelsStatus2=50000
                            remainingPixelsStatus2=$(($desiredPixelsStatus2 - $pixelsStatus2))
                            echo "Problem in pixels 100000 to 149999! # Pixel files finished : ${pixelsStatus2}, remaining : ${remainingPixelsStatus2}"
                        fi
                    fi

                    echo "Doing 150000 to 199999"
                    if (( $1 < 0 )); then
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_1[5-9]????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                    else
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_1[5-9]????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                    fi
                    desiredPixelsStatus=$((50000 * 3))
                    if [ "$desiredPixelsStatus" != "$pixelsStatus" ]; then
                        if (( $1 < 0 )); then
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_1[5-9]????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                        else
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_1[5-9]????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                        fi
                        pixelsStatus3=$(($pixelsStatus / 3))
                        if [ "$pixelsStatus3" != "$pixelsStatus2" ]; then
                            echo "Problem in pixels 150000 to 199999! # Values desired: ${desiredPixelsStatus}, obtained: ${pixelsStatus}. # Pixel files printed : ${pixelsStatus2}, but obtained # values seem to indicate : ${pixelsStatus3}" 
                        else    
                            desiredPixelsStatus2=50000
                            remainingPixelsStatus2=$(($desiredPixelsStatus2 - $pixelsStatus2))
                            echo "Problem in pixels 150000 to 199999! # Pixel files finished : ${pixelsStatus2}, remaining : ${remainingPixelsStatus2}"
                        fi
                    fi

                    echo "Doing 200000 to 249999"
                    if (( $1 < 0 )); then
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_2[0-4]????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                    else
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_2[0-4]????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                    fi
                    desiredPixelsStatus=$((50000 * 3))
                    if [ "$desiredPixelsStatus" != "$pixelsStatus" ]; then
                        if (( $1 < 0 )); then
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_2[0-4]????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                        else
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_2[0-4]????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                        fi
                        pixelsStatus3=$(($pixelsStatus / 3))
                        if [ "$pixelsStatus3" != "$pixelsStatus2" ]; then
                            echo "Problem in pixels 200000 to 249999! # Values desired: ${desiredPixelsStatus}, obtained: ${pixelsStatus}. # Pixel files printed : ${pixelsStatus2}, but obtained # values seem to indicate : ${pixelsStatus3}" 
                        else    
                            desiredPixelsStatus2=50000
                            remainingPixelsStatus2=$(($desiredPixelsStatus2 - $pixelsStatus2))
                            echo "Problem in pixels 200000 to 249999! # Pixel files finished : ${pixelsStatus2}, remaining : ${remainingPixelsStatus2}"
                        fi
                    fi

                    echo "Doing 250000 to 299999"
                    if (( $1 < 0 )); then
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_2[5-9]????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                    else
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_2[5-9]????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                    fi
                    desiredPixelsStatus=$((50000 * 3))
                    if [ "$desiredPixelsStatus" != "$pixelsStatus" ]; then
                        if (( $1 < 0 )); then
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_2[5-9]????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                        else
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_2[5-9]????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                        fi
                        pixelsStatus3=$(($pixelsStatus / 3))
                        if [ "$pixelsStatus3" != "$pixelsStatus2" ]; then
                            echo "Problem in pixels 250000 to 299999! # Values desired: ${desiredPixelsStatus}, obtained: ${pixelsStatus}. # Pixel files printed : ${pixelsStatus2}, but obtained # values seem to indicate : ${pixelsStatus3}" 
                        else    
                            desiredPixelsStatus2=50000
                            remainingPixelsStatus2=$(($desiredPixelsStatus2 - $pixelsStatus2))
                            echo "Problem in pixels 250000 to 299999! # Pixel files finished : ${pixelsStatus2}, remaining : ${remainingPixelsStatus2}"
                        fi
                    fi

                    echo "Doing 300000 to 349999"
                    if (( $1 < 0 )); then
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_3[0-4]????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                    else
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_3[0-4]????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                    fi
                    desiredPixelsStatus=$((50000 * 3))
                    if [ "$desiredPixelsStatus" != "$pixelsStatus" ]; then
                        if (( $1 < 0 )); then
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_3[0-4]????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                        else
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_3[0-4]????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                        fi
                        pixelsStatus3=$(($pixelsStatus / 3))
                        if [ "$pixelsStatus3" != "$pixelsStatus2" ]; then
                            echo "Problem in pixels 300000 to 349999! # Values desired: ${desiredPixelsStatus}, obtained: ${pixelsStatus}. # Pixel files printed : ${pixelsStatus2}, but obtained # values seem to indicate : ${pixelsStatus3}" 
                        else    
                            desiredPixelsStatus2=50000
                            remainingPixelsStatus2=$(($desiredPixelsStatus2 - $pixelsStatus2))
                            echo "Problem in pixels 300000 to 349999! # Pixel files finished : ${pixelsStatus2}, remaining : ${remainingPixelsStatus2}"
                        fi
                    fi

                    echo "Doing 350000 to 399999"
                    if (( $1 < 0 )); then
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_3[5-9]????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                    else
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_3[5-9]????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                    fi
                    desiredPixelsStatus=$((50000 * 3))
                    if [ "$desiredPixelsStatus" != "$pixelsStatus" ]; then
                        if (( $1 < 0 )); then
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_3[5-9]????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                        else
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_3[5-9]????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                        fi
                        pixelsStatus3=$(($pixelsStatus / 3))
                        if [ "$pixelsStatus3" != "$pixelsStatus2" ]; then
                            echo "Problem in pixels 350000 to 399999! # Values desired: ${desiredPixelsStatus}, obtained: ${pixelsStatus}. # Pixel files printed : ${pixelsStatus2}, but obtained # values seem to indicate : ${pixelsStatus3}" 
                        else    
                            desiredPixelsStatus2=50000
                            remainingPixelsStatus2=$(($desiredPixelsStatus2 - $pixelsStatus2))
                            echo "Problem in pixels 350000 to 399999! # Pixel files finished : ${pixelsStatus2}, remaining : ${remainingPixelsStatus2}"
                        fi
                    fi

                    echo "Doing 400000 to 449999"
                    if (( $1 < 0 )); then
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_4[0-4]????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                    else
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_4[0-4]????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                    fi
                    desiredPixelsStatus=$((50000 * 3))
                    if [ "$desiredPixelsStatus" != "$pixelsStatus" ]; then
                        if (( $1 < 0 )); then
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_4[0-4]????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                        else
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_4[0-4]????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                        fi
                        pixelsStatus3=$(($pixelsStatus / 3))
                        if [ "$pixelsStatus3" != "$pixelsStatus2" ]; then
                            echo "Problem in pixels 400000 to 449999! # Values desired: ${desiredPixelsStatus}, obtained: ${pixelsStatus}. # Pixel files printed : ${pixelsStatus2}, but obtained # values seem to indicate : ${pixelsStatus3}" 
                        else    
                            desiredPixelsStatus2=50000
                            remainingPixelsStatus2=$(($desiredPixelsStatus2 - $pixelsStatus2))
                            echo "Problem in pixels 400000 to 449999! # Pixel files finished : ${pixelsStatus2}, remaining : ${remainingPixelsStatus2}"
                        fi
                    fi

                    echo "Doing 450000 to 469757"
                    if (( $1 < 0 )); then
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_4[5-9]????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                    else
                        pixelsStatus=`cat $PATH_INDICATOR/${season}/NN_U_C_4[5-9]????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                    fi
                    desiredPixelsStatus=$((19758 * 3))
                    if [ "$desiredPixelsStatus" != "$pixelsStatus" ]; then
                        if (( $1 < 0 )); then
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_4[5-9]????_InM${IndicatorMinus1}_0_${season}.txt | wc -l`
                        else
                            pixelsStatus2=`ls $PATH_INDICATOR/${season}/NN_U_C_4[5-9]????_In113_${IndicatorMinus1}_${season}.txt | wc -l`
                        fi
                        pixelsStatus3=$(($pixelsStatus / 3))
                        if [ "$pixelsStatus3" != "$pixelsStatus2" ]; then
                            echo "Problem in pixels 450000 to 469757! # Values desired: ${desiredPixelsStatus}, obtained: ${pixelsStatus}. # Pixel files printed : ${pixelsStatus2}, but obtained # values seem to indicate : ${pixelsStatus3}" 
                        else    
                            desiredPixelsStatus2=19758
                            remainingPixelsStatus2=$(($desiredPixelsStatus2 - $pixelsStatus2))
                            echo "Problem in pixels 450000 to 469757! # Pixel files finished : ${pixelsStatus2}, remaining : ${remainingPixelsStatus2}"
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
