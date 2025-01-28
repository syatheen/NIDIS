#!/bin/bash
args=("$@")
echo ${args[0]} 
source /usr/share/modules/init/bash
module load python/GEOSpyD/Min4.8.3_py3.8
ulimit -s unlimited
source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU
which python
python PrepRefArraysFromInfoArrays_nClimGrid_At_nCGRes_WArg.py ${args[0]} >& Outs/PrepRefArraysFromInfoArrays_nClimGrid_At_nCGRes_${args[0]}.out
conda deactivate

