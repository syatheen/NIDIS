#!/bin/sh

#SBATCH --time=00:15:00
#SBATCH --nodes=5
#SBATCH --account=s1189
#SBATCH --constraint=mil
#SBATCH --ntasks=245
#SBATCH --ntasks-per-node=49
#SBATCH --job-name=TestMil
#SBATCH --no-requeue

cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/ESI

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
module list

srun -N 5 -n 245 --ntasks-per-node=49 --multi-prog Task_InfoArrays_gdalWarp_ClimGrid1D_V2.conf
wait



