Scripts and corresponding indicator numbers/names:
------------------------------------------------------

-> EDDI/Run_PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.sh :   20: 'EDDI_1wk',
                                                                  21: 'EDDI_2wk',
                                                                  22: 'EDDI_3wk',
                                                                  23: 'EDDI_4wk',
                                                                  24: 'EDDI_5wk',
                                                                  25: 'EDDI_6wk',
                                                                  26: 'EDDI_7wk',
                                                                  27: 'EDDI_8wk',
                                                                  28: 'EDDI_9wk',
                                                                  29: 'EDDI_10wk',
                                                                  30: 'EDDI_11wk',
                                                                  31: 'EDDI_12wk',
                                                                  32: 'EDDI_1mn',
                                                                  33: 'EDDI_2mn',
                                                                  34: 'EDDI_3mn',
                                                                  35: 'EDDI_4mn',
                                                                  36: 'EDDI_5mn',
                                                                  37: 'EDDI_6mn',
                                                                  38: 'EDDI_7mn',
                                                                  39: 'EDDI_8mn',
                                                                  40: 'EDDI_9mn',
                                                                  41: 'EDDI_10mn',
                                                                  42: 'EDDI_11mn',
       Note that the script here calling nidis/nidis/model/nclimdiv/percentile_creation/EDDI/PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py is the initial code structure, I have to change this to final structure.
       This PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.py is called by EDDI/Run_PrepTrainNEval_ClimDivs_EDDI_CorrToMonthlyPerc.sh;

-> EDDI/Run_PrepTrainNEval_ClimDivs_EDDI.sh :   43: 'EDDI_12mn',
       Note that the script here calling nidis/nidis/model/nclimdiv/percentile_creation/EDDI/PrepTrainNEval_ClimDivs_EDDI.py is the initial code structure, I have to change this to final structure.
       This PrepTrainNEval_ClimDivs_EDDI.py is called by EDDI/Run_PrepTrainNEval_ClimDivs_EDDI.sh;

?????
-> VegDRI directory : 68: 'VegDRI'
       Note that the script here calling nidis/nidis/model/nclimdiv/percentile_creation/VegDRI/PrepRefArraysFromInfoArrays_VegDRI.py is the initial code structure, have to change this to final structure.
       This PrepRefArraysFromInfoArrays_VegDRI.py is called by VegDRI/Run_PrepRefArraysFromInfoArrays_VegDRI.sh;

-> QuickDRI directory : 69: 'QuickDRI'
       Note that the script here calling nidis/nidis/model/nclimdiv/percentile_creation/QuickDRI/PrepRefArraysFromInfoArrays_QuickDRI.py is the initial code structure, have to change this to final structure.
       This PrepRefArraysFromInfoArrays_QuickDRI.py is called by QuickDRI/Run_PrepRefArraysFromInfoArrays_QuickDRI.sh;

