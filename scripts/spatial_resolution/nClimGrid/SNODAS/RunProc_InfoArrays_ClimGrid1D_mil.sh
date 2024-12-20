#!/bin/bash
args=("$@")
echo ${args[0]} ${args[1]} ${args[2]}  
source /usr/share/modules/init/bash
module load python/GEOSpyD/Min23.5.2-0_py3.11
ulimit -s unlimited
source /usr/local/other/GEOSpyD/23.5.2-0_py3.11/2023-11-02/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU_mil
which python
python /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/SNODAS_later/InfoArrays_ClimGrid1D.py ${args[0]} ${args[1]} ${args[2]} >& /discover/nobackup/projects/nca/syatheen/SNODAS_Outs/New/InfoArrays_ClimGrid1D_${args[0]}_${args[1]}_${args[2]}.out
conda deactivate
