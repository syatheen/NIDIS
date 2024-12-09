#!/bin/sh

#SBATCH --time=11:59:59
#SBATCH --nodes=4
#SBATCH --account=s1189
#SBATCH --constraint=mil
#SBATCH --ntasks=100
#SBATCH --ntasks-per-node=25
#SBATCH --job-name=Qk2
#SBATCH --no-requeue

cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/QuickDRI

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
module list

srun -N 4 -n 100 --ntasks-per-node=25 --multi-prog InfoArraysForPrcntl_ClimGrid_tasks_2.conf
wait

