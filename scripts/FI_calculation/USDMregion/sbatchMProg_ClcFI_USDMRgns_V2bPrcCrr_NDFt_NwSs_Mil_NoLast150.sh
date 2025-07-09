#!/bin/sh

#SBATCH --time=00:15:00
#SBATCH --nodes=18
#SBATCH --account=s1189
#SBATCH --constraint=mil
#SBATCH --ntasks=540
#SBATCH --ntasks-per-node=30
#SBATCH --job-name=U
#SBATCH --no-requeue

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
module list

srun -N 18 -n 540 --ntasks-per-node=30 --multi-prog Run_ClcFI_USDMRgns_V2bPrcCrr_NDFeat_NwSs_Cnf_1.conf
echo "1 finished"
srun -N 18 -n 540 --ntasks-per-node=30 --multi-prog Run_ClcFI_USDMRgns_V2bPrcCrr_NDFeat_NwSs_Cnf_2.conf
echo "2 finished"
srun -N 18 -n 540 --ntasks-per-node=30 --multi-prog Run_ClcFI_USDMRgns_V2bPrcCrr_NDFeat_NwSs_Cnf_3.conf
echo "3 finished"
srun -N 18 -n 540 --ntasks-per-node=30 --multi-prog Run_ClcFI_USDMRgns_V2bPrcCrr_NDFeat_NwSs_Cnf_4.conf
echo "4 finished"
srun -N 18 -n 540 --ntasks-per-node=30 --multi-prog Run_ClcFI_USDMRgns_V2bPrcCrr_NDFeat_NwSs_Cnf_5.conf
echo "5 finished"
srun -N 18 -n 540 --ntasks-per-node=30 --multi-prog Run_ClcFI_USDMRgns_V2bPrcCrr_NDFeat_NwSs_Cnf_6.conf
echo "6 finished"


  


