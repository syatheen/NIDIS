#!/bin/bash
args=("$@")
echo ${args[0]} ${args[1]} ${args[2]} ${args[3]} 
module load python/GEOSpyD/Min4.8.3_py3.8
ulimit -s unlimited
cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/NLDAS_2_daily
source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU
#which python
python CreateTifs_V2_2.py ${args[0]} ${args[1]} ${args[2]} ${args[3]} >& /discover/nobackup/projects/nca/syatheen/NLDAS_2_daily_Outs/CreateTifs_V2_2.${args[0]}.${args[1]}.${args[2]}${args[3]}.out
conda deactivate

