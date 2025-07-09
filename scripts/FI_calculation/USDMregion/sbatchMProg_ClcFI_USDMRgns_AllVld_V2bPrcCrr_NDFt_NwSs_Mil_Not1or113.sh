#!/bin/sh

##SBATCH --time=02:00:00
##SBATCH --time=04:00:00
#SBATCH --time=11:30:00
##SBATCH --nodes=30
##SBATCH --nodes=8
#SBATCH --nodes=2
#SBATCH --account=s1189
#SBATCH --constraint=mil
##SBATCH --ntasks=120
##SBATCH --ntasks=8
#SBATCH --ntasks=2
##SBATCH --ntasks-per-node=4
#SBATCH --ntasks-per-node=1
#SBATCH --job-name=UA
#SBATCH --no-requeue

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
module list

#srun -N 30 -n 120 --ntasks-per-node=4 --multi-prog Run_ClcFI_USDMRgns_AllVld_V2bPrcCrr_NDFeat_NwSs_Cnf_c.conf
#srun -N 8 -n 8 --ntasks-per-node=1 --multi-prog Run_ClcFI_USDMRgns_AllVld_V2bPrcCrr_NDFeat_NwSs_Cnf_c_Rest.conf
srun -N 2 -n 2 --ntasks-per-node=1 --multi-prog Run_ClcFI_USDMRgns_AllVld_V2bPrcCrr_NDFeat_NwSs_Cnf_c_Rest.conf


  


