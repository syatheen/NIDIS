#!/bin/sh

###SBATCH --time=05:04:00
#SBATCH --time=11:59:59
##SBATCH --time=00:24:00
#SBATCH --nodes=19
####SBATCH --nodes=1
#SBATCH --account=s1189
#SBATCH --constraint=mil
#SBATCH --ntasks=570
###SBATCH --ntasks=33
#SBATCH --ntasks-per-node=30
####SBATCH --ntasks-per-node=32
#SBATCH --job-name=Test
#SBATCH --no-requeue

cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/VegDRI

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
module list

srun -N 19 -n 570 --ntasks-per-node=30 --multi-prog RefArraysForPrcntl_ClimGrid_tasks_1.conf
###srun -N 1 -n 33 --ntasks-per-node=33 --multi-prog RefArraysForPrcntl_ClimGrid_tasks_test.conf
wait

