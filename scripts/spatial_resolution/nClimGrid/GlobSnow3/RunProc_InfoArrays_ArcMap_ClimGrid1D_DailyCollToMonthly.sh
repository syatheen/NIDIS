#!/bin/bash
args=("$@")
echo ${args[0]} ${args[1]} ${args[2]} ${args[3]} ${args[4]} 
source /usr/share/modules/init/bash
module load python/GEOSpyD/Min23.5.2-0_py3.11
ulimit -s unlimited
source /usr/local/other/GEOSpyD/23.5.2-0_py3.11/2023-11-02/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU_mil
which python
python /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/GlobSnow3/InfoArrays_ArcMap_ClimGrid1D_DailyCollToMonthly.py ${args[0]} ${args[1]} ${args[2]} ${args[3]} ${args[4]} >& /discover/nobackup/projects/nca/syatheen/GlobSnow3_Outs/InfoArrs_ArcMp_ClmGrd1D_DlyCllToMnthly_${args[1]}${args[2]}_${args[3]}_${args[4]}.out 
conda deactivate

