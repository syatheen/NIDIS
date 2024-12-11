#!/bin/bash
args=("$@")
echo ${args[0]} ${args[1]} ${args[2]}
source /usr/share/modules/init/bash
module load python/GEOSpyD/Min23.5.2-0_py3.11
ulimit -s unlimited
source /usr/local/other/GEOSpyD/23.5.2-0_py3.11/2023-11-02/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU_mil
which python
python InfoArrays_gdalWarp_ClimGrid1D_V2.py ${args[0]} ${args[1]} ${args[2]}  >& /discover/nobackup/projects/nca/syatheen/ESI_Outs/InfoArrays_gdalWarp_ClimGrid1D_V2_${args[0]}_${args[1]}.out
conda deactivate

