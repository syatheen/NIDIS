Scripts and corresponding indicator numbers/names:
------------------------------------------------------

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
       Note that the scripts here calling /nidis/nidis/model/nclimdiv/spatial_resolution/NCEI/InfoArrays_ClimDivs.py are the initial code structure, have to change this to final structure.
       InfoArrays_ClimDivs.py is called by RunProcess_InfoArrays_ClimDivs.sh;
       This RunProcess_InfoArrays_ClimDivs.sh is in turn called by one of : 
         --> Execfile_InfoArrays_ClimDivs_petNprcp (for 'prcp_??_nCG' indicators), in turn called by sbatchpods_InfoArrays_ClimDivs_petNprcp.sh;
         --> Execfile_InfoArrays_ClimDivs_spi-?? (for 'SPI_gamma_??_nCG' indicators), in turn called by sbatchpods_InfoArrays_ClimDivs_spi-??.sh; 
         --> Execfile_InfoArrays_ClimDivs_spei-?? (for 'SPEI_pear_??_nCG' indicators), in turn called by sbatchpods_InfoArrays_ClimDivs_spei-??.sh 
         --> Execfile_InfoArrays_ClimDivs_tavgNtmax (for 'tavg_01_nCG' and 'tmax_01_nCG' indicators), in turn called by sbatchpods_InfoArrays_ClimDivs_tavgNtmax.sh; 

-> GRACEDA directory : 17: 'GRACE_DA_gw',
                       18: 'GRACE_DA_sfsm',
                       19: 'GRACE_DA_rtzsm'
       Note that the scripts here calling nidis/nidis/model/nclimdiv/spatial_resolution/GRACEDA/RefPrcntlArrays_ClimDivs.py are the initial code structure, have to change this to final structure. 
       RefPrcntlArrays_ClimDivs.py is called by DoRefArrays_gws.sh; 
 
-> EDDI directory :   20: 'EDDI_1wk',
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
                      43: 'EDDI_12mn',
       Note that the scripts here calling nidis/nidis/model/nclimdiv/spatial_resolution/EDDI/RefPrcntlArrays_ClimDivs_V2.py is the initial code structure, I have to change this to final structure.
       RefPrcntlArrays_ClimDivs_V2.py called by RunProcess.sh;
       RunProcess.sh is in turn called by the example file Execfile_06wk_1Test;
       & finally Execfile_06wk_1Test is in turn called by sbatchpods_RefPrcntlArrays_ClimDivs.sh; 

-> NLDAS2 directory :    44: 'NLDAS2D_1MSM_Mosaic',
                         45: 'NLDAS2D_1MSM_Noah',
                         46: 'NLDAS2D_1MSM_SAC',
                         47: 'NLDAS2D_1MSM_VIC',
                         48: 'NLDAS2D_TCSM_Mosaic',
                         49: 'NLDAS2D_TCSM_Noah',
                         50: 'NLDAS2D_TCSM_SAC',
                         51: 'NLDAS2D_TCSM_VIC',
                         52: 'NLDAS2D_EVAP_Mosaic',
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
                         63: 'NLDAS2D_RUN_VIC',
                         64: 'NLDAS2D_STRMH04_Mosaic',
                         65: 'NLDAS2D_STRMH04_Noah',
                         66: 'NLDAS2D_STRMH04_SAC',
                         67: 'NLDAS2D_STRMH04_VIC',
       Note that the scripts here calling nidis/nidis/model/nclimdiv/spatial_resolution/NLDAS2/InfoArrays_ClimDivs_*.py are the initial code structure, have to change this to final structure.
         -->  InfoArrays_ClimDivs_DailyCollToMonthly.py (for 'NLDAS2D_1MSM_*' & 'NLDAS2D_TCSM_*' indicators):
           ---> This InfoArrays_ClimDivs_DailyCollToMonthly.py is called by RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.sh; 
           ---> this RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.sh is in turn called by  Execfile_InfoArrays_ClmDvs_DlyCllToMnthly_[1/2];
           ---> & these Execfile_InfoArrays_ClmDvs_DlyCllToMnthly_[1/2] in turn are called by sbatchpods_InfArrs_ClmDvs_DlyCllToMnthly_[1/2].sh;  
         -->  InfoArrays_ClimDivs_DailyCollToMonthly_50AdjustTo0.py (for 'NLDAS2D_EVAP_*', 'NLDAS2D_SWE_*' & 'NLDAS2D_RUN_*' indicators):
           ---> This InfoArrays_ClimDivs_DailyCollToMonthly_50AdjustTo0.py is called by RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh; 
           ---> this RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.50AdjustTo0.sh is in turn called by Execfile_InfoArrays_ClmDvs_DlyCllToMnthly_[3/4/5/6]_50AdjustTo0;
           ---> & these Execfile_InfoArrays_ClmDvs_DlyCllToMnthly_[3/4/5/6]_50AdjustTo0 in turn are called by sbatchpods_InfArrs_ClmDvs_DlyCllToMnthly_?_50AdjustTo0.sh;  
         -->  InfoArrays_ClimDivs_DyCollToMnth_50AdjTo0_HUCAvg.py (for 'NLDAS2D_STRMH04_*' indicators):
           ---> This InfoArrays_ClimDivs_DyCollToMnth_50AdjTo0_HUCAvg.py is called by RunProcess_InfoArrs_ClmDvs_DyCllToMnth.50AdjTo0_HUCAvg.sh; 
           ---> this RunProcess_InfoArrs_ClmDvs_DyCllToMnth.50AdjTo0_HUCAvg.sh is in turn called by Execfile_InfoArrays_ClmDvs_DyCllToMnth_[1/2]_50AdjTo0_HUCAvg;
           ---> & these Execfile_InfoArrays_ClmDvs_DyCllToMnth_[1/2]_50AdjTo0_HUCAvg in turn are called by sbatchpods_InfArrs_ClmDvs_DyCllToMnth_[1/2]_50AdjTo0_HUCAvg.sh;  

-> VegDRI directory : 68: 'VegDRI'
       Note that the script here calling nidis/nidis/model/nclimdiv/spatial_resolution/VegDRI/RefArrays_ClimDivs_V3.py is the initial code structure, have to change this to final structure.
       This RefArrays_ClimDivs_V3.py is called by RunProcess.sh;

-> QuickDRI directory : 69: 'QuickDRI'
       Note that the script here calling nidis/nidis/model/nclimdiv/spatial_resolution/QuickDRI/InfoArrays_ClimDivs_V3.py is the initial code structure, have to change this to final structure.
       This InfoArrays_ClimDivs_V3.py is called by RunProcess.sh;
       This RunProcess.sh is in turn called by Execfile_All_*;
       & finally Execfile_All_* are in turn called by sbatchpods_InfoArrays_ClimDivs_V3.sh; 

-> ESIs directory : 70: 'ESI_4wk',
                    71: 'ESI_12wk',
       Note that the script here calling nidis/nidis/model/nclimdiv/spatial_resolution/ESIs/InfoArrays_ClimDivs_V2.py is the initial code structure, have to change this to final structure.
       This InfoArrays_ClimDivs_V2.py is called by RunProcess.sh;
       This RunProcess.sh is in turn called by Execfile_All;
       & finally Execfile_All are in turn called by sbatchpods_RefArrays_ClimDivs.sh; 

-> SNODAS directory : 96: 'SNODAS'
       Note that the script here calling nidis/nidis/model/nclimdiv/spatial_resolution/SNODAS/InfoArrays_ClimDivsSplit_V3.py is the initial code structure, have to change this to final structure.
       This InfoArrays_ClimDivsSplit_V3.py is called by RunProcess_InfoArrays_ClimDivsSplit.sh;
       This RunProcess_InfoArrays_ClimDivsSplit.sh is in turn called by Execfile_InfoArrays_ClimDivsSplit_?Of4;
       & finally Execfile_InfoArrays_ClimDivsSplit_?Of4 are in turn called by sbatchpods_InfoArrays_ClimDivsSplit_?Of4.sh; 

-> ESA_CCI directory : 97: 'ESA_CCI'
       Note that the script here calling nidis/nidis/model/nclimdiv/spatial_resolution/ESA_CCI/InfoArrays_ClimDivs_DailyCollToMonthly.py is the initial code structure, have to change this to final structure.
       This InfoArrays_ClimDivs_DailyCollToMonthly.py is called by RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.sh;
       This RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.sh is in turn called by Execfile_InfoArrays_ClmDvs_DlyCllToMnthly;
       & finally Execfile_InfoArrays_ClmDvs_DlyCllToMnthly in turn called by sbatchpods_InfArrs_ClmDvs_DlyCllToMnthly.sh; 

-> IMERG directory :  98: 'IMERG_01',
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
       Note that the script here calling nidis/nidis/model/nclimdiv/spatial_resolution/IMERG/InfoArrays_ClimDivs_DailyCollToMonthly.py is the initial code structure, have to change this to final structure.
       This InfoArrays_ClimDivs_DailyCollToMonthly.py is called by RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.sh;
       This RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.sh is in turn called by Execfile_InfoArrays_ClimDivs_DailyCollToMonthly;
       & finally Execfile_InfoArrays_ClimDivs_DailyCollToMonthly in turn called by sbatchpods_InfArrs_ClmDvs_DlyCllToMnthly.sh; 

-> BlendedVHP directory  :  109: 'SmNDVI_BlendedVHP',
                            110: 'TCI_BlendedVHP',
                            111: 'VCI_BlendedVHP',
                            112: 'VHI_BlendedVHP'
       Note that the script here calling nidis/nidis/model/nclimdiv/spatial_resolution/BlendedVHP/InfoArrays_ClimDivsSplit_V3_b.py is the initial code structure, have to change this to final structure.
       This InfoArrays_ClimDivsSplit_V3_b.py is called by RunProcess_InfoArrays_ClimDivsSplit.sh;
       This RunProcess_InfoArrays_ClimDivsSplit.sh is in turn called by  Execfile_InfoArrays_ClimDivsSplit_?Of6;
       & finally  Execfile_InfoArrays_ClimDivsSplit_?Of6 in turn called by sbatchpods_InfoArrays_ClimDivsSplit_; 

-> GlobSnow3 directory :  113: 'GlobSnow3'
       Note that the script here calling nidis/nidis/model/nclimdiv/spatial_resolution/GlobSnow3/InfoArrays_ClimDivs.py is the initial code structure, have to change this to final structure.
       This GlobSnow3/InfoArrays_ClimDivs.py is called by RunProcess_InfoArrays_ClimDivs.sh;
       This RunProcess_InfoArrays_ClimDivs.sh is in turn called by Execfile_InfoArrays_ClimDivs_Part?;
       & finally Execfile_InfoArrays_ClimDivs_Part? in turn called by sbatchpods_InfoArrays_ClimDivs_Part?.sh; 




