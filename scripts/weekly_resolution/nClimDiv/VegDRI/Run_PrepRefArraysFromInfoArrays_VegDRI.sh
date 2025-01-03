#!/bin/bash

#SBATCH -G1 -t 50 -n1 -N1 -J VegDRI --export=ALL
module load anaconda
conda activate earthmlnew

srun -G1 -n1 python PrepRefArraysFromInfoArrays_VegDRI.py >& Outs/PrepRefArraysFromInfoArrays_VegDRI.20090428To20200804.out

conda deactivate

