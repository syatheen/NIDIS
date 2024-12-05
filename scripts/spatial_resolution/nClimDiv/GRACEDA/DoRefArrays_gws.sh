#!/bin/bash

###SBATCH -p gpu --gres=gpu:4 -n4 -N1 -t 8640
#####SBATCH -G1 -t 7200 -n1 -N1 -J Tif --export=ALL
#####SBATCH -G1 -t 720 -n1 -N1 --mem=750G -J SptPrf --export=ALL
#SBATCH -G1 -t 7199 -n1 -N1 -J g --export=ALL

module load anaconda

###source /opt/anaconda3/bin/activate earthml_test_try
conda activate earthmlnew

#srun -G1 -n1 python RefPrcntlArrays_ClimDivs.py gws_inst 2002 >& Outs/RefPrcntlArrays_ClimDivs_gws_inst_2002.out
#srun -G1 -n1 python RefPrcntlArrays_ClimDivs.py gws_inst 2003 >& Outs/RefPrcntlArrays_ClimDivs_gws_inst_2003.out
#srun -G1 -n1 python RefPrcntlArrays_ClimDivs.py gws_inst 2004 >& Outs/RefPrcntlArrays_ClimDivs_gws_inst_2004.out
#srun -G1 -n1 python RefPrcntlArrays_ClimDivs.py gws_inst 2005 >& Outs/RefPrcntlArrays_ClimDivs_gws_inst_2005.out
#srun -G1 -n1 python RefPrcntlArrays_ClimDivs.py gws_inst 2006 >& Outs/RefPrcntlArrays_ClimDivs_gws_inst_2006.out
#srun -G1 -n1 python RefPrcntlArrays_ClimDivs.py gws_inst 2007 >& Outs/RefPrcntlArrays_ClimDivs_gws_inst_2007.out
#srun -G1 -n1 python RefPrcntlArrays_ClimDivs.py gws_inst 2008 >& Outs/RefPrcntlArrays_ClimDivs_gws_inst_2008.out
#srun -G1 -n1 python RefPrcntlArrays_ClimDivs.py gws_inst 2009 >& Outs/RefPrcntlArrays_ClimDivs_gws_inst_2009.out
#srun -G1 -n1 python RefPrcntlArrays_ClimDivs.py gws_inst 2010 >& Outs/RefPrcntlArrays_ClimDivs_gws_inst_2010.out
#srun -G1 -n1 python RefPrcntlArrays_ClimDivs.py gws_inst 2011 >& Outs/RefPrcntlArrays_ClimDivs_gws_inst_2011.out
#srun -G1 -n1 python RefPrcntlArrays_ClimDivs.py gws_inst 2012 >& Outs/RefPrcntlArrays_ClimDivs_gws_inst_2012.out
#srun -G1 -n1 python RefPrcntlArrays_ClimDivs.py gws_inst 2013 >& Outs/RefPrcntlArrays_ClimDivs_gws_inst_2013.out
#srun -G1 -n1 python RefPrcntlArrays_ClimDivs.py gws_inst 2014 >& Outs/RefPrcntlArrays_ClimDivs_gws_inst_2014.out
#srun -G1 -n1 python RefPrcntlArrays_ClimDivs.py gws_inst 2015 >& Outs/RefPrcntlArrays_ClimDivs_gws_inst_2015.out
#srun -G1 -n1 python RefPrcntlArrays_ClimDivs.py gws_inst 2016 >& Outs/RefPrcntlArrays_ClimDivs_gws_inst_2016.out
srun -G1 -n1 python RefPrcntlArrays_ClimDivs.py gws_inst 2017 >& Outs/RefPrcntlArrays_ClimDivs_gws_inst_2017.out
srun -G1 -n1 python RefPrcntlArrays_ClimDivs.py gws_inst 2018 >& Outs/RefPrcntlArrays_ClimDivs_gws_inst_2018.out
srun -G1 -n1 python RefPrcntlArrays_ClimDivs.py gws_inst 2019 >& Outs/RefPrcntlArrays_ClimDivs_gws_inst_2019.out
srun -G1 -n1 python RefPrcntlArrays_ClimDivs.py gws_inst 2020 >& Outs/RefPrcntlArrays_ClimDivs_gws_inst_2020.out

conda deactivate 



