#!/bin/sh

##SBATCH -N 75
#SBATCH -N 20
#SBATCH --account=s1189
#SBATCH --constraint="hasw|sky|cas"
##SBATCH --constraint="hasw|sky"
##SBATCH --constraint=sky
##SBATCH --qos=debug
#SBATCH --qos=long
##SBATCH --time=23:50:00
##SBATCH --time=11:59:00
##SBATCH --time=01:00:00
#SBATCH --time=12:30:00
#SBATCH -o slurm_outp_%j.out
#SBATCH -e slurm_err_%j.out
#SBATCH --job-name=nCG

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min4.11.0_py3.9
module list

##/usr/local/other/PoDS/PoDS/pods.py -n 15 -l Y -s Y  -x /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/Execfile_InfoArrays_ClimGrid1D_spei-01
##/usr/local/other/PoDS/PoDS/pods.py -n 15 -l Y -s Y  -x /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/Execfile_InfoArrays_ClimGrid1D_speisExcept01
##/usr/local/other/PoDS/PoDS/pods.py -n 15 -l Y -s Y  -x /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/Execfile_InfoArrays_ClimGrid1D_spis
/usr/local/other/PoDS/PoDS/pods.py -n 15 -l Y -s Y  -x /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/Execfile_InfoArrays_ClimGrid1D_petNprcpNtavgNtmax


