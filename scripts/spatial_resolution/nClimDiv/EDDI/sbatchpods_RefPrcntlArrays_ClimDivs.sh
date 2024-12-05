#!/bin/bash

#SBATCH --account=s1189
#SBATCH --constraint=hasw
#SBATCH --qos=long
#SBATCH --time=23:55:00
#SBATCH --output="slurm_outp_%x_%j.out"
#SBATCH --error="slurm_err_%x_%j5.out"
#SBATCH --ntasks=1 --ntasks-per-node=1
#SBATCH --job-name=1Test

module load python/GEOSpyD/Min4.8.3_py3.8
ulimit -s unlimited
cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/EDDI
source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU
which python
/usr/local/other/PoDS/PoDS/pods.py -x /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/EDDI/Execfile_06wk_1Test -n 1
conda deactivate 
exit 0


