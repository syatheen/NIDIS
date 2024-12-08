#!/bin/sh

###SBATCH --time=05:04:00
##SBATCH --time=08:01:00
#SBATCH --time=11:59:59
#SBATCH --nodes=1
#SBATCH --account=s1189
#SBATCH --constraint=mil
####SBATCH --ntasks=14
#SBATCH --ntasks=20
####SBATCH --ntasks-per-node=14
#SBATCH --ntasks-per-node=20
#SBATCH --job-name=Test2
#SBATCH --no-requeue

cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/VegDRI

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
module list

srun -N 1 -n 20 --ntasks-per-node=20 --multi-prog RefArraysForPrcntl_ClimGrid_tasks_2.conf
wait

