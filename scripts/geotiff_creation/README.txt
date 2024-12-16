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
       Note that the scripts here calling nidis/nidis/model/nclimdiv/geotiff_creation/NCEI/CreateTifs_V2.py are the initial code structure., have to change this to final structure.
       CreateTifs_V2.py is called by RunProcess_CreateTifs_V2.sh;
       This RunProcess_CreateTifs_V2.sh is in turn called by one of : 
         --> Execfile_CreateTifs_petNprcp (for 'prcp_??_nCG' indicators) that's finally called by script sbatchpods_CreateTifs_petNprcp.sh
         --> Execfile_CreateTifs_spi-?? (for 'SPI_gamma_??_nCG' indicators) that're finally called by respective scripts sbatchpods_CreateTifs_spi-??.sh;
         --> Execfile_CreateTifs_spei-?? (for 'SPEI_pear_??_nCG' indicators) that're finally called by respective scripts sbatchpods_CreateTifs_spei-??.sh;
         --> Execfile_CreateTifs_tavgNtmax (for 'tavg_01_nCG' & 'tmax_01_nCG' indicators) that's finally called by script sbatchpods_CreateTifs_tavgNtmax.sh;  

-> NLDAS2 directory:    44: 'NLDAS2D_1MSM_Mosaic',
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
       Note that the scripts here calling nidis/nidis/model/nclimdiv/geotiff_creation/NLDAS2/CreateTifs_V2_2.py is the initial code structure, have to change this to final structure.
       CreateTifs_V2_2.py is called by RunProcess_CreateTifs_2.sh;
       This RunProcess_CreateTifs_2.sh is in turn called by one of : 
         --> Execfile_CreateTifs_1 (for 'NLDAS2D_1MSM_Mosaic', 'NLDAS2D_1MSM_Noah', 'NLDAS2D_1MSM_SAC', 'NLDAS2D_TCSM_Mosaic', 'NLDAS2D_TCSM_Noah', & 'NLDAS2D_TCSM_SAC' indicators) that's finally called by script sbatchpods_CreateTifs_1.sh
         --> Execfile_CreateTifs_2 (for 'NLDAS2D_1MSM_VIC' & 'NLDAS2D_TCSM_VIC' indicators) that's finally called by script sbatchpods_CreateTifs_2.sh
         --> Execfile_CreateTifs_3 (for 'NLDAS2D_EVAP_Mosaic', 'NLDAS2D_EVAP_Noah', 'NLDAS2D_EVAP_SAC', 'NLDAS2D_SWE_Mosaic', 'NLDAS2D_SWE_Noah', & 'NLDAS2D_SWE_SAC' indicators) 
         --> Execfile_CreateTifs_4 (for 'NLDAS2D_EVAP_VIC' & 'NLDAS2D_SWE_VIC' indicators) 
         --> Execfile_CreateTifs_5 (for 'NLDAS2D_RUN_Mosaic', 'NLDAS2D_RUN_Noah', 'NLDAS2D_RUN_SAC', 'NLDAS2D_STRMH04_Mosaic', 'NLDAS2D_STRMH04_Noah' & 'NLDAS2D_STRMH04_Noah' indicators) that's finally called by script sbatchpods_CreateTifs_5.sh
         --> Execfile_CreateTifs_6 (for 'NLDAS2D_RUN_VIC' & 'NLDAS2D_STRMH04_VIC' indicators) that's finally called by script sbatchpods_CreateTifs_6.sh
     
-> bash_submission_indicators_70_to_71.sh :   70: 'ESI_4wk',
                                              71: 'ESI_12wk'
       This bash_submission_indicators_70_to_71.sh calls nidis/nidis/model/nclimgrid/geotiff_creation/CreateTifs_ESI_Indicators_70_to_71.py;
 
-> ESA_CCI directory :   97: 'ESA_CCI'  
       Note that the scripts here calling nidis/nidis/model/nclimdiv/ESA_CCI/CreateTifs_V2_2.py is the initial code structure, have to change this to final structure.
       This CreateTifs_V2_2.py is called by RunProcess_CreateTifs_2.sh;
       RunProcess_CreateTifs_2.sh is in turn called by Execfile_CreateTifs_2;
       & finally Execfile_CreateTifs_2 is called by sbatchpods_CreateTifs_2.sh

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
       Note that the scripts here calling nidis/nidis/model/nclimdiv/IMERG/CreateTifs_V2.py is the initial code structure, have to change this to final structure.
       This CreateTifs_V2.py is called by RunProcess_CreateTifs.sh;
       RunProcess_CreateTifs.sh is in turn called by Execfile_CreateTifs;
       & finally Execfile_CreateTifs is called by sbatchpods_CreateTifs.sh

Execfile_CreateTifs  RunProcess_CreateTifs.sh  sbatchpods_CreateTifs.sh
 
 
 
