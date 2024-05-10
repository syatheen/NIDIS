#!/bin/bash
#SBATCH --time=2:00:00
#SBATCH --constraint=mil
#SBATCH --ntasks-per-node=126
#SBATCH --nodes=1
#SBATCH --no-requeue
#SBATCH --qos=admin
#SBATCH -J NID_Perc
#SBATCH --output=weekly_%x_%j.out      # Output file
#SBATCH --error=weekly_%x_%j.err       # Error file
#SBATCH --mail-user=jordan.a.caraballo-vega@nasa.gov

module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
source activate /home/syatheen/.conda/envs/newearthmlnew_noGPU

# $1 - indicator
export PYTHONPATH="/discover/nobackup/jacaraba/development/nidis"

echo "Indicator: $1"
srun -n1 python /discover/nobackup/jacaraba/development/nidis/nidis/view/nclimgrid/PercentileCreation_CLI.py \
    --indicator $1
