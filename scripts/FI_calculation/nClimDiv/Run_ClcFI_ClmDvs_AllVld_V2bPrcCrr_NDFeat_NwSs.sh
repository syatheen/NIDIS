#!/bin/bash
args=("$@")
echo ${args[0]} ${args[1]} ${args[2]} ${args[3]} ${args[4]} ${args[5]} ${args[6]} ${args[7]} ${args[8]} ${args[9]}
source /usr/share/modules/init/bash
module load python/GEOSpyD/Min23.5.2-0_py3.11
ulimit -s unlimited
source /usr/local/other/GEOSpyD/23.5.2-0_py3.11/2023-11-02/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU_mil
which python
python /discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS/ClcFI_ClmDvs_AllVld_V2bPrcCrr_NDFeat_NwSs.py ${args[0]} ${args[1]} ${args[2]} ${args[3]} ${args[4]} ${args[5]} ${args[6]} ${args[7]} ${args[8]} ${args[9]} >& /discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS/MI_results/ClcFI_ClmDvs_AllVld_V2bPrcCrr_NDFeat_NwSs_${args[0]}${args[1]}${args[2]}${args[4]}${args[5]}_${args[6]}_${args[7]}_${args[8]}_${args[9]}.out
conda deactivate

