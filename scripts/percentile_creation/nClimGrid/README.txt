Scripts and corresponding indicator numbers/names:
------------------------------------------------------

-> PalmerIndices directory : 3: 'PMDI',
                             4: 'PHDI'
       Note that the scripts here calling nidis/nidis/model/nclimgrid/percentile_creation/PrepTrainNEval_ClimGrid_Indicators_3_to_4.py are the initial code format, have to convert this to final format.
       This PrepTrainNEval_ClimGrid_Indicators_3_to_4.py is called by PalmerIndices/Run_PrepTrainNEval_ClimGrid_Indicators_3_to_4_mil.sh;
       This PalmerIndices/Run_PrepTrainNEval_ClimGrid_Indicators_3_to_4_mil.sh is in turn called by PalmerIndices/PrepTrainNEval_ClimGrid_Indicators_3_to_4_Conf.conf: 
       And finally this PalmerIndices/PrepTrainNEval_ClimGrid_Indicators_3_to_4_Conf.conf in turn called by PalmerIndices/sbatchMultiProg_PrepTrainNEval_ClimGrid_Indicators_3_to_4.sh .

-> NCEI directory :  5: 'prcp_01_nCG',
                     6: 'prcp_02_nCG',
                     7: 'prcp_03_nCG',
                     8: 'prcp_06_nCG',
                     9: 'prcp_09_nCG',
                    10: 'prcp_12_nCG',
                    11: 'prcp_24_nCG',
                    12: 'prcp_36_nCG',
                    13: 'prcp_48_nCG',
                    14: 'prcp_60_nCG',
                    15: 'prcp_72_nCG',
                    72: 'SPI_gamma_01_nCG',
                    73: 'SPI_gamma_02_nCG',
                    74: 'SPI_gamma_03_nCG',
                    75: 'SPI_gamma_06_nCG',
                    76: 'SPI_gamma_09_nCG',
                    77: 'SPI_gamma_12_nCG',
                    78: 'SPI_gamma_24_nCG',
                    79: 'SPI_gamma_36_nCG',
                    80: 'SPI_gamma_48_nCG',
                    81: 'SPI_gamma_60_nCG',
                    82: 'SPI_gamma_72_nCG',
                    83: 'SPEI_pear_01_nCG',
                    84: 'SPEI_pear_02_nCG',
                    85: 'SPEI_pear_03_nCG',
                    86: 'SPEI_pear_06_nCG',
                    87: 'SPEI_pear_09_nCG',
                    88: 'SPEI_pear_12_nCG',
                    89: 'SPEI_pear_24_nCG',
                    90: 'SPEI_pear_36_nCG',
                    91: 'SPEI_pear_48_nCG',
                    92: 'SPEI_pear_60_nCG',
                    93: 'SPEI_pear_72_nCG',
                    94: 'tavg_01_nCG',
                    95: 'tmax_01_nCG'
       Note that the scripts here calling /nidis/nidis/model/nclimgrid/percentile_creation/NCEI/PrepSingle_ClimGrid1D_nClimGrid.py are the initial code format, have to convert this to final format.
       This PrepSingle_ClimGrid1D_nClimGrid.py is called by NCEI/RunProc_PrepSingle_ClimGrid1D_nClimGrid_Mil.sh;
       This NCEI/RunProc_PrepSingle_ClimGrid1D_nClimGrid_Mil.sh is in turn called by NCEI/PrepSingle_ClimGrid1D_nClimGrid_prcp.conf: 
       And finally this NCEI/PrepSingle_ClimGrid1D_nClimGrid_prcp.conf in turn called by NCEI/sbatchMultiProg_dummy_Mil.sh .

-> EDDI directory : 20: 'EDDI_1wk',
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
       Note that the scripts here calling nidis/nidis/model/nclimgrid/percentile_creation/EDDI/PrepSingle_ClimGrid1D_EDDI_CorrToMonthlyPerc.py are the initial code structure, have to change this to final structure.
       This PrepSingle_ClimGrid1D_EDDI_CorrToMonthlyPerc.py is called by EDDI/RunProc_PrepSingle_ClmGrd1D_EDDI_CrrToMnthlyPrc_Mil.sh;
       EDDI/RunProc_PrepSingle_ClmGrd1D_EDDI_CrrToMnthlyPrc_Mil.sh is in turn called by EDDI/PrepSingle_ClmGrd1D_EDDI_CrrToMnthlyPrc_Conf.conf;
       & EDDI/PrepSingle_ClmGrd1D_EDDI_CrrToMnthlyPrc_Conf.conf is in turn called by EDDI/sbatchpods_PrepSingle_ClmGrd1D_EDDI_CrrToMnthlyPrc_Mil.sh; 

-> EDDI directory :  43: 'EDDI_12mn',
       Note that the scripts here calling nidis/nidis/model/nclimgrid/percentile_creation/EDDI/PrepSingle_ClimGrid1D_EDDI.py are the initial code structure, have to change this to final structure.
       This PrepSingle_ClimGrid1D_EDDI.py is called by EDDI/RunProc_PrepSingle_ClimGrid1D_EDDI_Mil.sh;
       EDDI/RunProc_PrepSingle_ClimGrid1D_EDDI_Mil.sh is in turn called by EDDI/PrepSingle_ClimGrid1D_EDDI_Conf.conf;
       & EDDI/PrepSingle_ClimGrid1D_EDDI_Conf.conf is in turn called by EDDI/sbatchpods_PrepSingle_ClmGrd1D_EDDI_Mil.sh; 
?????

-> VegDRI directory : 68: 'VegDRI'
       Note that the scripts here calling nidis/nidis/model/nclimgrid/weekly_resolution/VegDRI/PrepRefArraysFromInfoArrays_VegDRI_ClimGrid1D.py are the initial code structure, have to change this to final structure.
       This PrepRefArraysFromInfoArrays_VegDRI_ClimGrid1D.py is called by VegDRI/RunProc_PrepRefArraysFromInfoArrays_VegDRI_ClimGrid1D.sh;
       VegDRI/RunProc_PrepRefArraysFromInfoArrays_VegDRI_ClimGrid1D.sh is in turn called by VegDRI/PrepRefArraysFromInfoArrays_VegDRI_ClimGrid1DTask.conf;
       & VegDRI/PrepRefArraysFromInfoArrays_VegDRI_ClimGrid1DTask.conf is in turn called by VegDRI/sbatchMultiProg_PrepRefArraysFromInfoArrays_VegDRI_ClimGrid1D.sh; 

-> QuickDRI directory : 69: 'QuickDRI'
       Note that the scripts here calling nidis/nidis/model/nclimgrid/weekly_resolution/QuickDRI/PrepRefArraysFromInfoArrays_QuickDRI_ClimGrid1D.py are the initial code structure, have to change this to final structure.
       This PrepRefArraysFromInfoArrays_QuickDRI_ClimGrid1D.py is called by QuickDRI/RunProc_PrepRefArraysFromInfoArrays_QuickDRI_ClimGrid1D.sh;
       QuickDRI/RunProc_PrepRefArraysFromInfoArrays_QuickDRI_ClimGrid1D.sh is in turn called by QuickDRI/PrepRefArraysFromInfoArrays_QuickDRI_ClimGrid1DTask.conf;
       & QuickDRI/PrepRefArraysFromInfoArrays_QuickDRI_ClimGrid1DTask.conf are in turn called by QuickDRI/sbatchMultiProg_PrepRefArraysFromInfoArrays_QuickDRI_ClimGrid1D.sh; 

-> ESIs directory :  70: 'ESI_4wk',
                     71: 'ESI_12wk'
       Note that the scripts here calling nidis/nidis/model/nclimgrid/weekly_resolution/ESIs/PrepRefArraysFromInfoArrays_ESI_Multiweek_ClimGrid1D.py are the initial code structure, have to change this to final structure.
       This PrepRefArraysFromInfoArrays_ESI_Multiweek_ClimGrid1D.py is called by ESIs/Run_PrepRefArraysFromInfoArrays_ESI_Multiweek_ClimGrid1D_Mil.sh;
       ESIs/Run_PrepRefArraysFromInfoArrays_ESI_Multiweek_ClimGrid1D_Mil.sh is in turn called by ESIs/PrepRefArraysFromInfoArrays_ESI_Multiweek_ClimGrid1D_Conf.conf;
       & ESIs/PrepRefArraysFromInfoArrays_ESI_Multiweek_ClimGrid1D_Conf.conf is in turn called by ESIs/sbatchMProg_PrepRefArraysFromInfoArrays_ESI_Multiweek_ClimGrid1D.sh; 

-> SNODAS directory  : 96: 'SNODAS'
       Note that the scripts here calling nidis/nidis/model/nclimgrid/weekly_resolution/SNODAS/PrepRefArraysFromInfoArrays_SNODAS_ClimGrid1D.py are the initial code structure, have to change this to final structure.
       This PrepRefArraysFromInfoArrays_SNODAS_ClimGrid1D.py is called by SNODAS/RunProc_PrepRefArraysFromInfoArrays_SNODAS_ClimGrid1D_Mil.sh;
       SNODAS/RunProc_PrepRefArraysFromInfoArrays_SNODAS_ClimGrid1D_Mil.sh is in turn called by SNODAS/PrepRefArraysFromInfoArrays_SNODAS_ClimGrid1D_Conf.conf;
       & SNODAS/PrepRefArraysFromInfoArrays_SNODAS_ClimGrid1D_Conf.conf is in turn called by SNODAS/sbatchMProg_PrepRefArraysFromInfoArrays_SNODAS_ClimGrid1D_Mil.sh; 

-> ESA_CCI directory  :  97: 'ESA_CCI'
       Note that the scripts here calling nidis/nidis/model/nclimgrid/weekly_resolution/ESA_CCI/PrepRefArraysFromInfoArrays_Indicators_97_ESA_CCI.py are the initial code structure, have to change this to final structure.
       This PrepRefArraysFromInfoArrays_Indicators_97_ESA_CCI.py is called by ESA_CCI/Run_PrepRefArraysFromInfoArrays_Indicators_97_ESA_CCI_Mil.sh;
       ESA_CCI/Run_PrepRefArraysFromInfoArrays_Indicators_97_ESA_CCI_Mil.sh is in turn called by ESA_CCI/PrepRefArraysFromInfoArrays_Indicators_97_ESA_CCI_Conf.conf;
       & ESA_CCI/PrepRefArraysFromInfoArrays_Indicators_97_ESA_CCI_Conf.conf is in turn called by ESA_CCI/sbatchMProg_PrepRefArraysFromInfoArrays_Indicators_97_ESA_CCI.sh; 

-> BlendedVHP directory : 109: 'SmNDVI_BlendedVHP',
                          110: 'TCI_BlendedVHP',
                          111: 'VCI_BlendedVHP',
                          112: 'VHI_BlendedVHP'
       Note that the scripts here calling nidis/nidis/model/nclimgrid/weekly_resolution/BlendedVHP/PrepRefArraysFromInfoArrays_BlendedVHP_ClimGrid1D.py are the initial code structure, have to change this to final structure.
       This PrepRefArraysFromInfoArrays_BlendedVHP_ClimGrid1D.py is called by BlendedVHP/RunProc_PrepRefArraysFromInfoArrays_BlendedVHP_ClimGrid1D.sh;
       BlendedVHP/RunProc_PrepRefArraysFromInfoArrays_BlendedVHP_ClimGrid1D.sh is in turn called by BlendedVHP/Execfile_PrepRefArraysFromInfoArrays_BlendedVHP_ClimGrid1D;
       & BlendedVHP/Execfile_PrepRefArraysFromInfoArrays_BlendedVHP_ClimGrid1D is in turn called by BlendedVHP/sbatchpods_PrepRefArraysFromInfoArrays_BlendedVHP_ClimGrid1D.sh; 

-> GlobSnow3 directory  :  113: 'GlobSnow3'
       Note that the scripts here calling nidis/nidis/model/nclimgrid/weekly_resolution/PrepRefArraysFromInfoArrays_GlobSnow3_nClimGrid_Indicator113.py are the initial code structure, have to change this to final structure.
       This PrepRefArraysFromInfoArrays_GlobSnow3_nClimGrid_Indicator113.py is called by GlobSnow3/RunProc_InfoArrays_ArcMap_ClimGrid1D_DailyCollToMonthly.sh;
       GlobSnow3/RunProc_InfoArrays_ArcMap_ClimGrid1D_DailyCollToMonthly.sh is in turn called by GlobSnow3/InfoArrays_ArcMap_ClimGrid1D_DailyCollToMonthlyTasks*.conf;
       & GlobSnow3/InfoArrays_ArcMap_ClimGrid1D_DailyCollToMonthlyTasks*.conf is in turn called by GlobSnow3/sbatchMultiProg_InfoArrays_ClimGrid1D_DailyCollToMonthlyTasks_Mil.sh; 


