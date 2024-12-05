#!/bin/bash
args=("$@")
echo ${args[0]} ${args[1]} ${args[2]} ${args[3]} ${args[4]}
module load python/GEOSpyD/Min4.8.3_py3.8
ulimit -s unlimited
cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/NLDAS_2_daily
source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU
#which python
python InfoArrays_ClimDivs_DyCollToMnth_50AdjTo0_HUCAvg.py ${args[0]} ${args[1]} ${args[2]} ${args[3]} ${args[4]} >& /discover/nobackup/projects/nca/syatheen/NLDAS_2_daily_Outs/InfoArrs_ClmDvs_DyCllToMnth_${args[0]}_${args[1]}_${args[2]}${args[3]}_${args[4]}Avg_50AdjTo0.out
conda deactivate

