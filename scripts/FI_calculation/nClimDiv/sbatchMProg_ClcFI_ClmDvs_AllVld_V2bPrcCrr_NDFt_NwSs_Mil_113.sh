#!/bin/sh

#SBATCH --time=00:45:00
#SBATCH --nodes=5
#SBATCH --account=s1189
#SBATCH --constraint=mil
#SBATCH --ntasks=5
#SBATCH --ntasks-per-node=1
#SBATCH --job-name=CA113
#SBATCH --no-requeue

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
module list

srun -N 5 -n 5 --ntasks-per-node=1 --multi-prog Run_ClcFI_ClmDvs_AllVld_V2bPrcCrr_NDFeat_NwSs_Cnf_e.conf


  


