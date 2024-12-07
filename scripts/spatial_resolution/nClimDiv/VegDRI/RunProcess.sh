#!/bin/bash
args=("$@")
echo ${args[0]} ${args[1]} ${args[2]}
module load python/GEOSpyD/Min4.8.3_py3.8
ulimit -s unlimited
cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/VegDRI
source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU
which python
python RefArrays_ClimDivs_V3.py ${args[0]} ${args[1]} ${args[2]}  >& Outs/RefArrays_ClimDivs_V3_${args[0]}_${args[1]}_${args[2]}.out
conda deactivate

