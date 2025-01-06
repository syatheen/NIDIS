#!/bin/bash

#SBATCH -G1 -t 150 -n1 -N1 -J QuickDRI --export=ALL
module load anaconda
conda activate earthmlnew

srun -G1 -n1 python PrepTrainNEval_ClimDivs_QuickDRI_MonthlyPerc.py >& Outs/PrepTrainNEval_ClimDivs_QuickDRI_MonthlyPerc.20060103To20191231.out

conda deactivate

