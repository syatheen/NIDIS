#!/bin/sh

#SBATCH --time=11:59:59
#SBATCH --nodes=1
#SBATCH --account=s1189
#SBATCH --constraint=mil
#SBATCH --ntasks=16
#SBATCH --ntasks-per-node=16
#SBATCH --job-name=SNODAS
#SBATCH --no-requeue

## For ntasks-per-node=30, "Max Pct Memory Used : 5.85%" and "Pct CPU Utilization : .79%"

cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/SNODAS_later

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
module list

srun -N 1 -n 16 --ntasks-per-node=16 --multi-prog InfoArrays_ClimGrid1D_TestConf.conf
wait


