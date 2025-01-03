#!/bin/bash

#SBATCH -G1 -t 50 -n1 -N1 -J Classified --export=ALL
module load anaconda
conda activate earthmlnew

srun -G1 -n1 python PrepRefArraysFromInfoArrays_GRACEDA.py >& Outs/PrepRefArrFromInfo_GRACEDA.sfsm_inst.20020402To20201020.out

conda deactivate

