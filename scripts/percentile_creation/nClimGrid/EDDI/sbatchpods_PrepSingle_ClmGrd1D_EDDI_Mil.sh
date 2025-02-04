#!/bin/sh

#SBATCH --time=00:12:00
#SBATCH --nodes=2
#SBATCH --account=s1189
#SBATCH --constraint=mil
#SBATCH --ntasks=24
#SBATCH --ntasks-per-node=12
#SBATCH --job-name=PercEDDI
#SBATCH --no-requeue

##SY: For --ntasks-per-node=12, "Max Pct Memory Used : .82%" & "Pct CPU Utilization : 8.42%"

cd /discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
module list

srun -N 2 -n 24 --ntasks-per-node=12 --multi-prog PrepSingle_ClimGrid1D_EDDI_Conf.conf
wait

