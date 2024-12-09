#!/bin/bash

#SBATCH --account=s1189
#SBATCH --constraint=hasw
#SBATCH --qos=long
#SBATCH --time=23:58:00
#SBATCH --output="slurm_outp_%x_%j.out"
#SBATCH --error="slurm_err_%x_%j.out"
#SBATCH --ntasks=252 --ntasks-per-node=28
#SBATCH --job-name=ESI

module load python/GEOSpyD/Min4.8.3_py3.8
ulimit -s unlimited
cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/ESI
source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU
which python
/usr/local/other/PoDS/PoDS/pods.py -x /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/ESI/Execfile_All -n 28
conda deactivate 
exit 0


