#!/bin/bash
#SBATCH --time=2:00:00
#SBATCH --constraint=mil
#SBATCH --ntasks-per-node=126
#SBATCH --nodes=1
#SBATCH --no-requeue
#SBATCH --qos=admin
#SBATCH -J NIDIS_POST
#SBATCH --output=postprocess_%x_%j.out      # Output file
#SBATCH --error=postprocess_%x_%j.err       # Error file
#SBATCH --mail-user=jordan.a.caraballo-vega@nasa.gov

module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
source activate /home/syatheen/.conda/envs/newearthmlnew_noGPU

# srun -n1 python CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_CLI.py $1 $2 $3

# $1 - indicator
# $2 - season, one of A, P, F, U, W
# $3 - space, nca or fame
export PYTHONPATH="/discover/nobackup/jacaraba/development/nidis"

echo "Indicator: $1"
for fileSystem in "fame" "nca"; do
    PATH_INDICATOR="/discover/nobackup/projects/${fileSystem}/jacaraba/NIDIS_Runs/indicator_${1}"
    if [ -d "${PATH_INDICATOR}" ]; then
        echo "Processing ${PATH_INDICATOR}"
        srun -n1 python /discover/nobackup/jacaraba/development/nidis/nidis/view/CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_CLI.py \
            --indicator $1 --season $2 --output-dir /discover/nobackup/projects/$fileSystem/jacaraba/NIDIS_Runs --step postprocess
    fi
done
