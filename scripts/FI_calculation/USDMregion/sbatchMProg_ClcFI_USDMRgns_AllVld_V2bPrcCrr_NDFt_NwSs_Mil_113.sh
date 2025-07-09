#!/bin/sh

##SBATCH --time=01:30:00
##SBATCH --time=04:00:00
#SBATCH --time=10:00:00
##SBATCH --nodes=15
##SBATCH --nodes=6
#SBATCH --nodes=2
#SBATCH --account=s1189
#SBATCH --constraint=mil
##SBATCH --ntasks=30
##SBATCH --ntasks=6
#SBATCH --ntasks=2
##SBATCH --ntasks-per-node=2
#SBATCH --ntasks-per-node=1
#SBATCH --job-name=UA113
#SBATCH --no-requeue

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
module list

#srun -N 15 -n 30 --ntasks-per-node=2 --multi-prog Run_ClcFI_USDMRgns_AllVld_V2bPrcCrr_NDFeat_NwSs_Cnf_b.conf
#srun -N 6 -n 6 --ntasks-per-node=1 --multi-prog Run_ClcFI_USDMRgns_AllVld_V2bPrcCrr_NDFeat_NwSs_Cnf_b_Rest.conf
srun -N 2 -n 2 --ntasks-per-node=1 --multi-prog Run_ClcFI_USDMRgns_AllVld_V2bPrcCrr_NDFeat_NwSs_Cnf_b_Rest.conf


  


