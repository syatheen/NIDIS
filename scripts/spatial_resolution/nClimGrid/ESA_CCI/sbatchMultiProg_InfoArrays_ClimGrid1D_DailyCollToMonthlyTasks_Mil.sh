#!/bin/sh

#SBATCH --time=00:10:00
##SBATCH --nodes=4
#SBATCH --nodes=1
#SBATCH --account=s1189
#SBATCH --constraint=mil
##SBATCH --ntasks=480
#SBATCH --ntasks=26
##SBATCH --ntasks-per-node=120
#SBATCH --ntasks-per-node=26
#SBATCH --job-name=ESACCI
#SBATCH --no-requeue

cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/ESA_CCI

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
module list

#srun -N 4 -n 480 --ntasks-per-node=120 --multi-prog InfoArrays_gdalWarp_ClimGrid1D_DailyCollToMonthlyTasks_A.conf
srun -N 1 -n 26 --ntasks-per-node=26 --multi-prog InfoArrays_gdalWarp_ClimGrid1D_DailyCollToMonthlyTasks_B.conf
wait 


