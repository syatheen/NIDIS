#!/bin/bash

#SBATCH --account=s1189
#SBATCH --constraint=hasw
######SBATCH --constraint=cas
##SBATCH --qos=long
#SBATCH --time=11:52:00
#SBATCH --output="slurm_outp_%x_%j.out"
#SBATCH --error="slurm_err_%x_%j.out"
#SBATCH --ntasks=1008 --ntasks-per-node=14
#####SBATCH --ntasks=1008 --ntasks-per-node=24
#SBATCH --job-name=I6_RnS

module load python/GEOSpyD/Min4.8.3_py3.8
ulimit -s unlimited
cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/NLDAS_2_daily
source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU
#which python
/usr/local/other/PoDS/PoDS/pods.py -x /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/NLDAS_2_daily/Execfile_InfoArrays_ClmDvs_DlyCllToMnthly_6_50AdjustTo0 -n 14
#####/usr/local/other/PoDS/PoDS/pods.py -x /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/NLDAS_2_daily/Execfile_InfoArrays_ClmDvs_DlyCllToMnthly_4_50AdjustTo0 -n 24
conda deactivate 
exit 0

