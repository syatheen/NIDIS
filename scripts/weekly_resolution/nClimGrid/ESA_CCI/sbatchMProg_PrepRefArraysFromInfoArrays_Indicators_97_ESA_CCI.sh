#!/bin/sh

#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --account=s1189
#SBATCH --constraint=mil
#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --job-name=ESACCI
#SBATCH --no-requeue

cd /discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
module list

srun -N 1 -n 1 --ntasks-per-node=1 --multi-prog PrepRefArraysFromInfoArrays_Indicators_97_ESA_CCI_Conf.conf
wait



