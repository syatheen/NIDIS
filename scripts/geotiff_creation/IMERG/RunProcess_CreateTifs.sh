#!/bin/bash
args=("$@")
echo ${args[0]} ${args[1]} ${args[2]} 
module load python/GEOSpyD/Min4.8.3_py3.8
ulimit -s unlimited
cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG
source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU
#which python
python CreateTifs_V2.py ${args[0]} ${args[1]} ${args[2]} >& /discover/nobackup/projects/nca/syatheen/IMERG_Outs/daily_Final_V06/CreateTifs_V2_${args[0]}${args[1]}${args[2]}.out
conda deactivate

