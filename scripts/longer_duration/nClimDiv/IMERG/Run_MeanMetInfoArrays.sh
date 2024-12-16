#####!/bin/bash
####
####module load python/GEOSpyD/Min4.8.3_py3.8
####ulimit -s unlimited
####cd /discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/IMERG
####source /usr/local/other/python/GEOSpyD/4.8.3_py3.8/2020-08-11/etc/profile.d/conda.sh
####conda activate newearthmlnew_noGPU

###python MeanMetInfoArrays.py 1 >& Outs/MeanMetInfoArrays.1Day.out
python MeanMetInfoArrays.py 30 >& Outs/MeanMetInfoArrays.1Month.out
python MeanMetInfoArrays.py 60 >& Outs/MeanMetInfoArrays.2Months.out
python MeanMetInfoArrays.py 90 >& Outs/MeanMetInfoArrays.3Months.out
python MeanMetInfoArrays.py 180 >& Outs/MeanMetInfoArrays.6Months.out
python MeanMetInfoArrays.py 270 >& Outs/MeanMetInfoArrays.9Months.out
python MeanMetInfoArrays.py 365 >& Outs/MeanMetInfoArrays.12Months.out
python MeanMetInfoArrays.py 730 >& Outs/MeanMetInfoArrays.24Months.out
python MeanMetInfoArrays.py 1095 >& Outs/MeanMetInfoArrays.36Months.out
python MeanMetInfoArrays.py 1461 >& Outs/MeanMetInfoArrays.48Months.out
python MeanMetInfoArrays.py 1826 >& Outs/MeanMetInfoArrays.60Months.out
python MeanMetInfoArrays.py 2191 >& Outs/MeanMetInfoArrays.72Months.out

####conda deactivate 
####exit 0


