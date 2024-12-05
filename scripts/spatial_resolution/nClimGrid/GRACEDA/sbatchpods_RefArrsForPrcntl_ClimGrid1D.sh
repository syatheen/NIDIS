#!/bin/sh

#SBATCH -N 19
#SBATCH --account=s1189
###SBATCH --constraint="hasw|sky|cas"
#SBATCH --constraint="sky|cas"
##SBATCH --constraint=sky
##SBATCH --qos=debug
##SBATCH --qos=long
##SBATCH --time=23:50:00
##SBATCH --time=11:59:00
#SBATCH --time=03:06:00
#SBATCH -o slurm_outp_%j.out
#SBATCH -e slurm_err_%j.out
#SBATCH --job-name=Test

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min4.11.0_py3.9
module list

/usr/local/other/PoDS/PoDS/pods.py -n 3 -l Y -s Y  -x /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/GRACE/Execfile_GRACE_ClimGrid1D
  


