#!/bin/bash
args=("$@")
echo ${args[0]} ${args[1]} ${args[2]} ${args[2]}${args[3]}
source /usr/share/modules/init/bash
module load python/GEOSpyD/Min4.8.3_py3.8
ulimit -s unlimited
source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU
which python
python InfoArrays_ClimDivsSplit_V3.py ${args[0]} ${args[1]} ${args[2]} ${args[3]} >& /discover/nobackup/projects/nca/syatheen/SNODAS_Outs/InfoArrays_ClimDivsSplit_${args[0]}${args[1]}${args[2]}_${args[3]}.out
conda deactivate

