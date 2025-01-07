#!/bin/bash
args=("$@")
echo ${args[0]} ${args[1]} ${args[2]} ${args[3]} ${args[4]} ${args[5]} ${args[6]} ${args[7]} ${args[8]} ${args[9]}
module load python/GEOSpyD/Min4.8.3_py3.8
ulimit -s unlimited
cd /discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS
source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU
#which python
python CalcFracMI_ClimDivs_V2b_NDFeat_NewSeas.py ${args[0]} ${args[1]} ${args[2]} ${args[3]} ${args[4]} ${args[5]} ${args[6]} ${args[7]} ${args[8]} ${args[9]} >& MI_results/NClcFrcMI_ClmDvs_V2b_ND_${args[0]}${args[1]}${args[2]}${args[4]}${args[5]}_${args[6]}_${args[7]}_${args[8]}_${args[9]}.out
conda deactivate

