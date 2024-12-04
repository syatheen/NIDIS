#!/bin/bash
source /usr/share/modules/init/bash
module load python/GEOSpyD/Min23.5.2-0_py3.11
ulimit -s unlimited
source /usr/local/other/GEOSpyD/23.5.2-0_py3.11/2023-11-02/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU_mil
which python
##echo "started running on " `hostname` " at time " `date`
python /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/CPCsoilmoisture/total/daily/private/QC_test/RefArraysForPrcntls_gdalWarp_ClimGrid1D.py >& /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/CPCsoilmoisture/total/daily/private/QC_test/RefArraysForPrcntls_gdalWarp_ClimGrid1D.out  
##echo "finished running on " `hostname` " at time " `date`
conda deactivate

