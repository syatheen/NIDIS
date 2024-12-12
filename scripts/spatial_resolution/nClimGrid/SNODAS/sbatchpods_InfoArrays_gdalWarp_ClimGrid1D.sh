#!/bin/sh

#SBATCH -N 2
#SBATCH --account=s1189
###SBATCH --constraint="hasw|sky|cas"
#SBATCH --constraint="sky|cas"
##SBATCH --constraint=sky
##SBATCH --qos=debug
#SBATCH --qos=long
#SBATCH --time=20:00:00
##SBATCH --time=11:59:00
##SBATCH --time=01:00:00
#SBATCH -o slurm_outp_%j.out
#SBATCH -e slurm_err_%j.out
#SBATCH --job-name=Test

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min4.11.0_py3.9
module list

/usr/local/other/PoDS/PoDS/pods.py -n 5 -l Y -s Y  -x /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/SNODAS_later/Execfile_InfoArrays_gdalWarp_ClimGrid1D


