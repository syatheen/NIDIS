#!/bin/sh

#SBATCH --time=00:05:00
#SBATCH --nodes=5
#SBATCH --account=s1189
#SBATCH --constraint=mil
#SBATCH --ntasks=150
#SBATCH --ntasks-per-node=30
#SBATCH --job-name=UA2
#SBATCH --no-requeue

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
module list

srun -N 5 -n 150 --ntasks-per-node=30 --multi-prog Run_ClcFI_USDMRgns_AllVld_V2bPrcCrr_NDFeat_NwSs_Cnf_7.conf


  


