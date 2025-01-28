#!/bin/bash
args=("$@")
echo ${args[0]} 
module load python/GEOSpyD/Min4.8.3_py3.8
ulimit -s unlimited
cd /discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS
source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU
#which python
python PrepRefArraysFromInfoArrays_EDDI_ClimGrid1D.py ${args[0]} >& Outs/PrepRefArraysFromInfoArrays_EDDI_ClimGrid1D_${args[0]}.out
conda deactivate

