#!/bin/bash

#SBATCH --account=s1189
#SBATCH --constraint=hasw
##SBATCH --qos=long
#SBATCH --time=11:55:00
#SBATCH --output="slurm_outp_%x_%j.out"
#SBATCH --error="slurm_err_%x_%j.out"
##SBATCH --ntasks=1092 --ntasks-per-node=14
#SBATCH --ntasks=546 --ntasks-per-node=14
#SBATCH --job-name=QDRI

module load python/GEOSpyD/Min4.8.3_py3.8
ulimit -s unlimited
cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/QuickDRI
source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU
which python
##/usr/local/other/PoDS/PoDS/pods.py -x /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/QuickDRI/Execfile_All -n 14
/usr/local/other/PoDS/PoDS/pods.py -x /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/QuickDRI/Execfile_All_2 -n 14
conda deactivate 
exit 0


