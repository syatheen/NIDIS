#!/bin/sh

#SBATCH --time=04:05:00
#SBATCH --nodes=1
#SBATCH --account=s1189
#SBATCH --constraint=mil
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --job-name=TestMil
#SBATCH --no-requeue

cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/CPCsoilmoisture/total/daily/private/QC_test

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
module list

srun -N 1 -n 1 --ntasks-per-node=1 --multi-prog tasks.conf
wait



