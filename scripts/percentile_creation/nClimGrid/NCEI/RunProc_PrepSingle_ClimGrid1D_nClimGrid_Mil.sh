#!/bin/bash
args=("$@")
echo ${args[0]} 
source /usr/share/modules/init/bash
module load python/GEOSpyD/Min23.5.2-0_py3.11
ulimit -s unlimited
source /usr/local/other/GEOSpyD/23.5.2-0_py3.11/2023-11-02/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU_mil
which python
python /discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS/PrepSingle_ClimGrid1D_nClimGrid.py ${args[0]} >& /discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS/Outs/PrepSingle_nClimGrid_nClimGrid_${args[0]}.out
conda deactivate

