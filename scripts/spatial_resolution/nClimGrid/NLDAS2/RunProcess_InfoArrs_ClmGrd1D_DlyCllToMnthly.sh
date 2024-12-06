#!/bin/bash
args=("$@")
echo ${args[0]} ${args[1]} ${args[2]} ${args[3]}
source /usr/share/modules/init/bash
module load python/GEOSpyD/Min4.8.3_py3.8
ulimit -s unlimited
source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU
#which python
python InfoArrays_gdalWarp_ClimGrid1D_DailyCollToMonthly_Indicators_44_to_51.py ${args[0]} ${args[1]} ${args[2]} ${args[3]} >& /discover/nobackup/projects/nca/syatheen/NLDAS_2_daily_Outs/InfoArrs_ClmGrd1D_DlyCllToMnthly_${args[0]}_${args[1]}_${args[2]}${args[3]}.out
conda deactivate

