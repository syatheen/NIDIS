#!/bin/sh

#SBATCH -N 1
#SBATCH --account=s1189
###SBATCH --constraint="hasw|sky|cas"
##SBATCH --constraint="hasw|sky"
##SBATCH --constraint="[sky|cas]"
#SBATCH --constraint=sky
##SBATCH --qos=debug
##SBATCH --qos=long
##SBATCH --time=23:55:00
##SBATCH --time=11:59:00
#SBATCH --time=02:00:00
#SBATCH -o slurm_outp_%j.out
##SBATCH -e slurm_err_%j.out
##SBATCH --job-name=FI_G1D_Try
#SBATCH --job-name=Test
#SBATCH --no-requeue

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min4.11.0_py3.9
module list

/usr/local/other/PoDS/PoDS/pods.py -n 1 -l Y -s Y  -x /discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS/Execfile_PrepSingle_ClimGrid1D_BlendedVHP_MonthlyPerc


