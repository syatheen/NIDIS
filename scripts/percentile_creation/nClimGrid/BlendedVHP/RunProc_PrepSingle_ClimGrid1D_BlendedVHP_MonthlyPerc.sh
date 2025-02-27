#!/bin/bash
source /usr/share/modules/init/bash
module load python/GEOSpyD/Min4.8.3_py3.8
ulimit -s unlimited
source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU
which python
python PrepSingle_ClimGrid1D_BlendedVHP_MonthlyPerc.py >& Outs/PrepSingle_ClimGrid1D_BlendedVHP_MonthlyPerc.out
conda deactivate

