#!/bin/bash
args=("$@")
echo ${args[0]} ${args[1]}
source /usr/share/modules/init/bash
module load python/GEOSpyD/Min23.5.2-0_py3.11
ulimit -s unlimited
source /usr/local/other/GEOSpyD/23.5.2-0_py3.11/2023-11-02/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU_mil
which python
python /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/ESA_CCI/InfoArrays_gdalWarp_ClimGrid1D_DailyCollToMonthly.py ${args[0]} ${args[1]} >& /discover/nobackup/projects/nca/syatheen/ESA_CCI_Outs/InfoArrays_gdalWarp_ClimGrid1D_DailyCollToMonthly_${args[0]}${args[1]}.out 
conda deactivate

