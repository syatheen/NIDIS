#!/bin/bash
##SBATCH --time=2:00:00
#SBATCH --time=00:18:00
#SBATCH --constraint=mil
#SBATCH --ntasks-per-node=126
#SBATCH --nodes=1
#SBATCH --no-requeue
#SBATCH -J NIDIS_POST
#SBATCH --output=postprocess_%x_%j.out      # Output file
#SBATCH --error=postprocess_%x_%j.err       # Error file
#SBATCH --mail-user=soni.yatheendradas-1@nasa.gov

module purge
module load python/GEOSpyD/Min23.5.2-0_py3.11
##source activate /discover/nobackup/jacaraba/.conda/envs/amy-rf
ulimit -s unlimited
source /usr/local/other/GEOSpyD/23.5.2-0_py3.11/2023-11-02/etc/profile.d/conda.sh
conda activate newearthmlnew_noGPU_mil

# srun -n1 python CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_CLI.py $1 $2 $3

# $1 - indicator
# $2 - season, one of A, P, F, U, W
export PYTHONPATH="/discover/nobackup/syatheen/development/nidis"

echo "Indicator: $1"
for fileSystem in "fame" "nca"; do
    PATH_INDICATOR="/discover/nobackup/projects/${fileSystem}/syatheen/NIDIS_Runs/indicator_${1}"
    if [ -d "${PATH_INDICATOR}" ]; then
        echo "Processing ${PATH_INDICATOR}"
        srun -n1 python /discover/nobackup/syatheen/development/nidis/nidis/view/CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_CLI.py \
            --indicator $1 --season $2 --output-dir /discover/nobackup/projects/$fileSystem/syatheen/NIDIS_Runs --step postprocess
    fi
done
