#!/bin/bash
#SBATCH --time=12:00:00
#SBATCH --constraint=mil
#SBATCH --ntasks-per-node=100
#SBATCH --nodes=1
#SBATCH --job-name=TestMil
#SBATCH --no-requeue
#SBATCH --output=%x_%j.out      # Output file
#SBATCH --error=%x_%j.err       # Error file
#SBATCH --mail-user=jordan.a.caraballo-vega@nasa.gov

module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
source activate /home/jacaraba/.conda/envs/amy-rf

srun -n1 python CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_CLI.py $1 $2 $3

