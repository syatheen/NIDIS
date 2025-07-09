#!/bin/sh

#SBATCH --time=00:10:00
#SBATCH --nodes=18
#SBATCH --account=s1189
#SBATCH --constraint=mil
#SBATCH --ntasks=540
#SBATCH --ntasks-per-node=30
#SBATCH --job-name=Tst3
#SBATCH --no-requeue

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
module list

srun -N 18 -n 540 --ntasks-per-node=30 --multi-prog Run_ClcFI_ClmDvs_AllVld_V2bPrcCrr_NDFeat_NwSs_Cnf_d_1.conf


