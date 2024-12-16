#!/bin/bash
args=("$@")
echo ${args[0]} 
module load python/GEOSpyD/Min4.8.3_py3.8
ulimit -s unlimited
cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/GlobSnow3
source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU
#which python
python CreateTifs_V2_2.py ${args[0]} >& /discover/nobackup/projects/nca/syatheen/GlobSnow3_Outs/CreateTifs_V2_2.${args[0]}.out
conda deactivate

