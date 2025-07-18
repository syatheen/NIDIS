#!/bin/sh

#SBATCH --time=00:45:00
#SBATCH --nodes=10
#SBATCH --account=s1189
#SBATCH --constraint=mil
#SBATCH --ntasks=20
#SBATCH --ntasks-per-node=2
#SBATCH --job-name=Tst
#SBATCH --no-requeue

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
module list

srun -N 10 -n 20 --ntasks-per-node=2 --multi-prog Run_ClcFI_ClmDvs_AllVld_V2bPrcCrr_NDFeat_NwSs_Cnf_f.conf


  


