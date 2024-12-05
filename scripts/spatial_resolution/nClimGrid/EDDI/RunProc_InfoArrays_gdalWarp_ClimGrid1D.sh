#!/bin/bash
args=("$@")
echo ${args[0]} ${args[1]} ${args[2]} ${args[3]} ${args[4]} ${args[5]} ${args[6]}
module load python/GEOSpyD/Min4.8.3_py3.8
ulimit -s unlimited
cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/EDDI
source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU
#which python
python InfoArrays_gdalWarp_ClimGrid1D.py ${args[0]} ${args[1]} ${args[2]} ${args[3]} ${args[4]} ${args[5]} ${args[6]} >& /discover/nobackup/projects/nca/syatheen/EDDI_Outs/InfoArrays_gdalWarp_ClimGrid1D_${args[0]}${args[1]}${args[2]}To${args[3]}${args[4]}${args[5]}_${args[6]}.out
conda deactivate

