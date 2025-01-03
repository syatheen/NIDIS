#!/bin/bash

#SBATCH -G1 -t 50 -n1 -N1 -J QuickDRI --export=ALL
module load anaconda
conda activate earthmlnew

srun -G1 -n1 python PrepRefArraysFromInfoArrays_QuickDRI.py >& Outs/PrepRefArraysFromInfoArrays_QuickDRI.20000125To20201229.out

conda deactivate

