#!/bin/bash

#SBATCH --account=s1189
#SBATCH --constraint="hasw|sky|cas"
##SBATCH --qos=long
##SBATCH --time=23:50:00
#SBATCH --time=11:50:00
#SBATCH --output="slurm_outp_%x_%j.out"
#SBATCH --error="slurm_err_%x_%j.out"
#SBATCH --ntasks=24 --ntasks-per-node=1
#SBATCH --job-name=RefEDDI

module load python/GEOSpyD/Min4.8.3_py3.8
ulimit -s unlimited
cd /discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS
source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU
#which python
/usr/local/other/PoDS/PoDS/pods.py -x /discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS/Execfile_PrepRefArrsFromInfoArrs_EDDI_ClmGrd1D -n 1
conda deactivate 
exit 0


