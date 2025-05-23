Python codes and corresponding indicator numbers/names:
------------------------------------------------------
-> NO Python code because no spatial resolution to nClimDiv resolution done for : 
                             1. 'Z_index',
                             2: 'Z_index_60_month'
     Because original tabular format were already at nClimDiv resolution, and reading + accumulation + first conversion to Npz format done only in the next step of 'longer_duration' for these indicators  

-> PalmerIndices/RefArraysForPrcntls_ClimDivs_PhdOrPdi.py: 3: 'PMDI',
                                                           4: 'PHDI' 
     for conversion from original CSV format were already at nClimDiv resolution to Npz format 

-> NCEI/InfoArrays_ClimDivs.py :  5: 'prcp_01_nCG',
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
     Note that this NCEI/InfoArrays_ClimDivs.py is the initial code structure, have to convert this to final structure.

-> CPC_soil_moisture/RefArraysForPrcntls_ClimDivs.py: 16: 'CPC_soil_moisture'
      Note that this CPC_soil_moisture/RefArraysForPrcntls_ClimDivs.py is the initial code structure, have to change this to final structure.

-> GRACEDA/RefPrcntlArrays_ClimDivs.py :  17: 'GRACE_DA_gw',
                                          18: 'GRACE_DA_sfsm',
                                          19: 'GRACE_DA_rtzsm'
     Note that this GRACEDA/RefPrcntlArrays_ClimDivs.py is the initial code structure, I have to change this to final structure.

-> EDDI/RefPrcntlArrays_ClimDivs_V2.py :   20: 'EDDI_1wk',
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
                                           43: 'EDDI_12mn'
     Note that this EDDI/RefPrcntlArrays_ClimDivs_V2.py is the initial code structure, I have to change this to final structure.

-> NLDAS2/InfoArrays_ClimDivs_DailyCollToMonthly.py :    44: 'NLDAS2D_1MSM_Mosaic',
                                                         45: 'NLDAS2D_1MSM_Noah',
                                                         46: 'NLDAS2D_1MSM_SAC',
                                                         47: 'NLDAS2D_1MSM_VIC',
                                                         48: 'NLDAS2D_TCSM_Mosaic',
                                                         49: 'NLDAS2D_TCSM_Noah',
                                                         50: 'NLDAS2D_TCSM_SAC',
                                                         51: 'NLDAS2D_TCSM_VIC'
     Note that this NLDAS2/InfoArrays_ClimDivs_DailyCollToMonthly.py is the initial code structure, I have to change this to final structure.


-> NLDAS2/InfoArrays_ClimDivs_DailyCollToMonthly_50AdjustTo0.py :    52: 'NLDAS2D_EVAP_Mosaic',
                                                                     53: 'NLDAS2D_EVAP_Noah',
                                                                     54: 'NLDAS2D_EVAP_SAC',
                                                                     55: 'NLDAS2D_EVAP_VIC',
                                                                     56: 'NLDAS2D_SWE_Mosaic',
                                                                     57: 'NLDAS2D_SWE_Noah',
                                                                     58: 'NLDAS2D_SWE_SAC',
                                                                     59: 'NLDAS2D_SWE_VIC',
                                                                     60: 'NLDAS2D_RUN_Mosaic',
                                                                     61: 'NLDAS2D_RUN_Noah',
                                                                     62: 'NLDAS2D_RUN_SAC',
                                                                     63: 'NLDAS2D_RUN_VIC'
     Note that this NLDAS2/InfoArrays_ClimDivs_DailyCollToMonthly_50AdjustTo0.py is the initial code structure, I have to change this to final structure.

-> NLDAS2/InfoArrays_ClimDivs_DyCollToMnth_50AdjTo0_HUCAvg.py:      64: 'NLDAS2D_STRMH04_Mosaic',
                                                                     65: 'NLDAS2D_STRMH04_Noah',
                                                                     66: 'NLDAS2D_STRMH04_SAC',
                                                                     67: 'NLDAS2D_STRMH04_VIC'
     Note that this NLDAS2/InfoArrays_ClimDivs_DyCollToMnth_50AdjTo0_HUCAvg.py is the initial code structure, have to change this to final structure.

-> VegDRI/RefArrays_ClimDivs_V3.py : 68: 'VegDRI'
     Note that this VegDRI/RefArrays_ClimDivs_V3.py is the initial code structure, have to change this to final structure.

-> QuickDRI/InfoArrays_ClimDivs_V3.py : 69: 'QuickDRI'
     Note that this QuickDRI/InfoArrays_ClimDivs_V3.py is the initial code structure, have to change this to final structure.

-> ESIs/InfoArrays_ClimDivs_V2.py :  70: 'ESI_4wk',
                                     71: 'ESI_12wk',
     Note that this ESIs/InfoArrays_ClimDivs_V2.py is the initial code structure, have to change this to final structure.

-> SNODAS/InfoArrays_ClimDivsSplit_V3.py  : 96: 'SNODAS'
     Note that this SNODAS/InfoArrays_ClimDivsSplit_V3.py is the initial code structure, have to change this to final structure.

-> ESA_CCI/InfoArrays_ClimDivs_DailyCollToMonthly.py  :  97: 'ESA_CCI'
     Note that this ESA_CCI/InfoArrays_ClimDivs_DailyCollToMonthly.py is the initial code structure, have to change this to final structure.
 
-> IMERG/InfoArrays_ClimDivs_DailyCollToMonthly.py :    98: 'IMERG_01',
                                                        99: 'IMERG_02',
                                                       100: 'IMERG_03',
                                                       101: 'IMERG_06',
                                                       102: 'IMERG_09',
                                                       103: 'IMERG_12',
                                                       104: 'IMERG_24',
                                                       105: 'IMERG_36',
                                                       106: 'IMERG_48',
                                                       107: 'IMERG_60',
                                                       108: 'IMERG_72'
     Note that this IMERG/InfoArrays_ClimDivs_DailyCollToMonthly.py is the initial code structure, have to change this to final structure.

-> BlendedVHP/InfoArrays_ClimDivsSplit_V3_b.py :  109: 'SmNDVI_BlendedVHP',
                                                  110: 'TCI_BlendedVHP',
                                                  111: 'VCI_BlendedVHP',
                                                  112: 'VHI_BlendedVHP' 
     Note that this BlendedVHP/InfoArrays_ClimDivsSplit_V3_b.py is the initial code structure, have to change this to final structure.

-> GlobSnow3/InfoArrays_ClimDivs.py :  113: 'GlobSnow3'
     Note that this GlobSnow3/InfoArrays_ClimDivs.py is the initial code structure, have to change this to final structure.



