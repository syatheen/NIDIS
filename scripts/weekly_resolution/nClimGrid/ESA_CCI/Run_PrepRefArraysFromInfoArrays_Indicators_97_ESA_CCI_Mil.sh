#!/bin/bash
source /usr/share/modules/init/bash
module load python/GEOSpyD/Min23.5.2-0_py3.11
ulimit -s unlimited
source /usr/local/other/GEOSpyD/23.5.2-0_py3.11/2023-11-02/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU_mil
which python
python /discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS/PrepRefArraysFromInfoArrays_Indicators_97_ESA_CCI.py >& /discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS/Outs/PrepRefArraysFromInfoArrays_Indicators_97_ESA_CCI.out
conda deactivate



