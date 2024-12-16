#!/bin/bash
args=("$@")
echo ${args[0]}} ${args[1]}
module load python/GEOSpyD/Min4.8.3_py3.8
ulimit -s unlimited
cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/BlendedVHP
source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU
python InfoArrays_ClimDivsSplit_V3_b.py ${args[0]} ${args[1]} >& /discover/nobackup/projects/nca/syatheen/BlendedVHP_Outs/InfoArrays_ClimDivsSplit_${args[0]}${args[1]}.out
conda deactivate

