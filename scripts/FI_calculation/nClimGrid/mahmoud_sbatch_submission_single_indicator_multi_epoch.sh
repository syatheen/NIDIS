#!/bin/bash
#SBATCH --time=12:00:00
#SBATCH --constraint=mil
#SBATCH --ntasks-per-node=126
#SBATCH --nodes=1
#SBATCH --no-requeue
#SBATCH --output=%x_%j.out      # Output file
#SBATCH --error=%x_%j.err       # Error file

# module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
##source activate /discover/nobackup/jacaraba/.conda/envs/amy-rf
ulimit -s unlimited
source /usr/local/other/GEOSpyD/23.5.2-0_py3.11/2023-11-02/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU_mil

# srun -n1 python CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_CLI.py $1 $2 $3

# $1 - indicator
# $2 - season, one of A, P, F, U, W
# $3 - space, nca or fame
export PYTHONPATH="/discover/nobackup/mosman1/development/nidis"
srun -n1 python /discover/nobackup/mosman1/development/nidis/nidis/view/CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_CLI.py \
    --indicator $1 --season $2 --output-dir /discover/nobackup/projects/$3/syatheen/NIDIS_Runs --step train --init-task $4 --end-task $5 --n-processes $6
wait
conda deactivate

