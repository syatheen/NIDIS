#!/bin/bash

#SBATCH -G1 -t 150 -n1 -N1 -J EDDI --export=ALL
module load anaconda
conda activate earthmlnew

srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 01wk >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.01wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 02wk >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.02wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 03wk >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.03wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 04wk >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.04wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 05wk >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.05wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 06wk >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.06wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 07wk >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.07wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 08wk >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.08wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 09wk >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.09wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 10wk >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.10wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 11wk >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.11wk.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 12wk >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.12wk.20060103To20191231.out

srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 01mn >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.01mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 02mn >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.02mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 03mn >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.03mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 04mn >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.04mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 05mn >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.05mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 06mn >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.06mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 07mn >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.07mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 08mn >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.08mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 09mn >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.09mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 10mn >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.10mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 11mn >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.11mn.20060103To20191231.out
srun -G1 -n1 python PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py 12mn >& Outs/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.12mn.20060103To20191231.out

conda deactivate

