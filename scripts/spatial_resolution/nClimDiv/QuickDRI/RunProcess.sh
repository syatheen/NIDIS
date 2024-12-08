#!/bin/bash
args=("$@")
echo ${args[0]} ${args[1]} 
module load python/GEOSpyD/Min4.8.3_py3.8
ulimit -s unlimited
cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/QuickDRI
source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU
which python
python InfoArrays_ClimDivs_V3.py ${args[0]} ${args[1]} >& Outs/InfoArrays_ClimDivs_V3_${args[0]}wk${args[1]}.out
conda deactivate

