#!/bin/bash
args=("$@")
echo ${args[0]} ${args[1]} 
source /usr/share/modules/init/bash
module load python/GEOSpyD/Min23.5.2-0_py3.11
ulimit -s unlimited
source /usr/local/other/GEOSpyD/23.5.2-0_py3.11/2023-11-02/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU_mil
which python
##echo "started running on " `hostname` " at time " `date`
python /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/QuickDRI/InfoArraysForPrcntl_ClimGrid.py ${args[0]} ${args[1]} >& /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/QuickDRI/Outs/InfoArraysForPrcntl_ClimGrid_mil_${args[0]}_${args[1]}.out
##echo "finished running on " `hostname` " at time " `date`
conda deactivate
