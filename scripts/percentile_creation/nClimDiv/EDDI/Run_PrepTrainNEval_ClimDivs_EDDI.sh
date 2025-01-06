#!/bin/bash

#SBATCH -G1 -t 150 -n1 -N1 -J EDDI --export=ALL
module load anaconda
conda activate earthmlnew

srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 01wk >& Outs/PrepTrainNEval_ClimDivs_EDDI.01wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 02wk >& Outs/PrepTrainNEval_ClimDivs_EDDI.02wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 03wk >& Outs/PrepTrainNEval_ClimDivs_EDDI.03wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 04wk >& Outs/PrepTrainNEval_ClimDivs_EDDI.04wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 05wk >& Outs/PrepTrainNEval_ClimDivs_EDDI.05wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 06wk >& Outs/PrepTrainNEval_ClimDivs_EDDI.06wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 07wk >& Outs/PrepTrainNEval_ClimDivs_EDDI.07wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 08wk >& Outs/PrepTrainNEval_ClimDivs_EDDI.08wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 09wk >& Outs/PrepTrainNEval_ClimDivs_EDDI.09wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 10wk >& Outs/PrepTrainNEval_ClimDivs_EDDI.10wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 11wk >& Outs/PrepTrainNEval_ClimDivs_EDDI.11wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 12wk >& Outs/PrepTrainNEval_ClimDivs_EDDI.12wk.20060103To20191231.out

srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 01mn >& Outs/PrepTrainNEval_ClimDivs_EDDI.01mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 02mn >& Outs/PrepTrainNEval_ClimDivs_EDDI.02mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 03mn >& Outs/PrepTrainNEval_ClimDivs_EDDI.03mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 04mn >& Outs/PrepTrainNEval_ClimDivs_EDDI.04mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 05mn >& Outs/PrepTrainNEval_ClimDivs_EDDI.05mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 06mn >& Outs/PrepTrainNEval_ClimDivs_EDDI.06mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 07mn >& Outs/PrepTrainNEval_ClimDivs_EDDI.07mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 08mn >& Outs/PrepTrainNEval_ClimDivs_EDDI.08mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 09mn >& Outs/PrepTrainNEval_ClimDivs_EDDI.09mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 10mn >& Outs/PrepTrainNEval_ClimDivs_EDDI.10mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 11mn >& Outs/PrepTrainNEval_ClimDivs_EDDI.11mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI.py 12mn >& Outs/PrepTrainNEval_ClimDivs_EDDI.12mn.20060103To20191231.out

conda deactivate

