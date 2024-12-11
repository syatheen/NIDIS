#!/bin/sh

##SBATCH --time=11:59:59
#SBATCH --time=06:00:00
#SBATCH --nodes=1
#SBATCH --account=s1189
#SBATCH --constraint=mil
#SBATCH --ntasks=2
#SBATCH --ntasks-per-node=2
#SBATCH --job-name=ESI
#SBATCH --no-requeue

# For ntasks-per-node=1 : "Pct CPU Utilization : .05%" and "Max Pct Memory Used : 0.00%"

cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/ESI

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
module list

srun -N 1 -n 2 --ntasks-per-node=2 --multi-prog MeanMetInfoArrays_InclNans_ClimGrid1D_Conf.conf
wait


