#!/bin/bash
args=("$@")
echo ${args[0]} ${args[1]} 
source /usr/share/modules/init/bash
module load python/GEOSpyD/Min4.8.3_py3.8
ulimit -s unlimited
source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU
which python
python MeanMetInfoArrays_ClimGrid1D.py ${args[0]} ${args[1]} >& Outs/MeanMetInfoArrays_ClimGrid1D.${args[0]}.${args[1]}.out
conda deactivate

