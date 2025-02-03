#!/bin/bash
#SBATCH --time=12:00:00
#SBATCH --constraint=mil
#SBATCH --ntasks-per-node=126
#SBATCH --nodes=1
#SBATCH --no-requeue
#SBATCH --output=%x_%j.out      # Output file
#SBATCH --error=%x_%j.err       # Error file
##SBATCH --mail-type=ALL
##SBATCH --mail-user=soni.yatheendradas-1@nasa.gov

# module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
source activate /discover/nobackup/jacaraba/.conda/envs/amy-rf

## srun -n1 python CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_CLI.py $1 $2 $3

# $1 - indicator
# $2 - season, one of A, P, F, U, W
# $3 - space, nca or fame
export PYTHONPATH="/discover/nobackup/syatheen/development/nidis"
srun -n1 python /discover/nobackup/syatheen/development/nidis/nidis/view/CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_CLI.py \
    --indicator $1 --season $2 --output-dir /discover/nobackup/projects/$3/syatheen/NIDIS_Runs --step train --init-task $4 --end-task $5 --n-processes $6 --start-date 20150106

