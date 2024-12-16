#!/bin/sh

##SBATCH --time=00:30:00
#SBATCH --time=00:10:00
##SBATCH --nodes=3
#SBATCH --nodes=1
#SBATCH --account=s1189
#SBATCH --constraint=mil
##SBATCH --ntasks=360
#SBATCH --ntasks=113
##SBATCH --ntasks=1
##SBATCH --ntasks-per-node=120
#SBATCH --ntasks-per-node=113
#SBATCH --job-name=GlobSnow3
#SBATCH --no-requeue

# For ntasks-per-node=1, "Pct CPU Utilization : .29%" and "Max Pct Memory Used : 0.00%"
# For ntasks-per-node=32, "Pct CPU Utilization : 7.57%" and "Max Pct Memory Used : 0.00%"
# For ntasks-per-node=120, "Pct CPU Utilization : 9.87%" and "Max Pct Memory Used : 0.00%"

cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/GlobSnow3

source /usr/share/modules/init/bash
module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
module list

##srun -N 3 -n 360 --ntasks-per-node=120 --multi-prog InfoArrays_ArcMap_ClimGrid1D_DailyCollToMonthlyTasks_1.conf
srun -N 1 -n 113 --ntasks-per-node=113 --multi-prog InfoArrays_ArcMap_ClimGrid1D_DailyCollToMonthlyTasks_2.conf
wait 


