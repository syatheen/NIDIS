#!/bin/bash
args=("$@")
echo ${args[0]} 
module load python/GEOSpyD/Min4.8.3_py3.8
ulimit -s unlimited
cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/BlendedVHP
source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU
python CreateTifs.py ${args[0]} >& /discover/nobackup/projects/nca/syatheen/BlendedVHP_Outs/CreateTifs_${args[0]}.out
conda deactivate

