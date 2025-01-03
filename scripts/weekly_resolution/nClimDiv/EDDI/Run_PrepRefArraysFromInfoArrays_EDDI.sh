#!/bin/bash

#SBATCH -G1 -t 120 -n1 -N1 -J EDDI --export=ALL
module load anaconda
conda activate earthmlnew

#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 01wk >& Outs/PrepRefArrFromInfo_EDDI.01wk.19800108To20200825.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 02wk >& Outs/PrepRefArrFromInfo_EDDI.02wk.19800108To20200825.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 03wk >& Outs/PrepRefArrFromInfo_EDDI.03wk.19800108To20200825.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 04wk >& Outs/PrepRefArrFromInfo_EDDI.04wk.19800108To20200825.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 05wk >& Outs/PrepRefArrFromInfo_EDDI.05wk.19800108To20200825.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 06wk >& Outs/PrepRefArrFromInfo_EDDI.06wk.19800108To20200825.out

#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 02mn >& Outs/PrepRefArrFromInfo_EDDI.02mn.19800108To20200825.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 03mn >& Outs/PrepRefArrFromInfo_EDDI.03mn.19800108To20200825.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 04mn >& Outs/PrepRefArrFromInfo_EDDI.04mn.19800108To20200825.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 06mn >& Outs/PrepRefArrFromInfo_EDDI.06mn.19800108To20200825.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 07mn >& Outs/PrepRefArrFromInfo_EDDI.07mn.19800108To20200825.out

srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 01wk >& Outs/PrepRefArrFromInfo_EDDI.01wk.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 02wk >& Outs/PrepRefArrFromInfo_EDDI.02wk.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 03wk >& Outs/PrepRefArrFromInfo_EDDI.03wk.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 04wk >& Outs/PrepRefArrFromInfo_EDDI.04wk.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 05wk >& Outs/PrepRefArrFromInfo_EDDI.05wk.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 06wk >& Outs/PrepRefArrFromInfo_EDDI.06wk.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 07wk >& Outs/PrepRefArrFromInfo_EDDI.07wk.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 08wk >& Outs/PrepRefArrFromInfo_EDDI.08wk.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 09wk >& Outs/PrepRefArrFromInfo_EDDI.09wk.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 10wk >& Outs/PrepRefArrFromInfo_EDDI.10wk.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 11wk >& Outs/PrepRefArrFromInfo_EDDI.11wk.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 12wk >& Outs/PrepRefArrFromInfo_EDDI.12wk.19800108To20201229.out
#
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 01mn >& Outs/PrepRefArrFromInfo_EDDI.01mn.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 02mn >& Outs/PrepRefArrFromInfo_EDDI.02mn.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 03mn >& Outs/PrepRefArrFromInfo_EDDI.03mn.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 04mn >& Outs/PrepRefArrFromInfo_EDDI.04mn.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 05mn >& Outs/PrepRefArrFromInfo_EDDI.05mn.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 06mn >& Outs/PrepRefArrFromInfo_EDDI.06mn.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 07mn >& Outs/PrepRefArrFromInfo_EDDI.07mn.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 08mn >& Outs/PrepRefArrFromInfo_EDDI.08mn.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 09mn >& Outs/PrepRefArrFromInfo_EDDI.09mn.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 10mn >& Outs/PrepRefArrFromInfo_EDDI.10mn.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 11mn >& Outs/PrepRefArrFromInfo_EDDI.11mn.19800108To20201229.out
#srun -G1 -n1 python PrepRefArraysFromInfoArrays_EDDI.py 12mn >& Outs/PrepRefArrFromInfo_EDDI.12mn.19800108To20201229.out

conda deactivate

