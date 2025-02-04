#!/bin/sh

#SBATCH --time=01:30:00
#SBATCH --nodes=1
#SBATCH --account=s1189
#SBATCH --constraint=mil
#SBATCH --ntasks=11
#SBATCH --ntasks-per-node=11
#SBATCH --job-name=NCEI
#SBATCH --no-requeue

cd /discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
module list

#srun -N 1 -n 1 --ntasks-per-node=1 --multi-prog PrepSingle_ClimGrid1D_nClimGrid_prcp_1test.conf
#srun -N 2 -n 10 --ntasks-per-node=5 --multi-prog PrepSingle_ClimGrid1D_nClimGrid_prcp_rest.conf
srun -N 1 -n 11 --ntasks-per-node=11 --multi-prog PrepSingle_ClimGrid1D_nClimGrid_prcp.conf
wait


