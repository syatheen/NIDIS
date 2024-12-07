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
       Note that the scripts here calling /nidis/nidis/model/nclimgrid/spatial_resolution/NCEI/InfoArrays_ClimGrid1D.py are the initial code format, have to convert this to final format.
       InfoArrays_ClimGrid1D.py is called by RunProcess_InfoArrays_ClimGrid1D.sh;
       This RunProcess_InfoArrays_ClimGrid1D.sh is in turn called by one of : 
         --> Execfile_InfoArrays_ClimGrid1D_petNprcpNtavgNtmax (for 'prcp_??_nCG', 'tavg_01_nCG', and 'tmax_01_nCG' indicators);
         --> Execfile_InfoArrays_ClimGrid1D_spis (for 'SPI_gamma_??_nCG' indicators);
         --> Execfile_InfoArrays_ClimGrid1D_spei-01 (for 'SPEI_pear_01_nCG' indicator);
         --> Execfile_InfoArrays_ClimGrid1D_speisExcept01 (for 'SPEI_pear_??_nCG' indicators except 'SPEI_pear_01_nCG');  
       And finally these Execfile_* are in turn called by sbatchpods_InfoArrays_ClimGrid1D.sh

-> CPC_soil_moisture directory : 16: 'CPC_soil_moisture'
       Note that the scripts here calling /nidis/nidis/model/nclimgrid/spatial_resolution/CPC_soil_moisture/RefArraysForPrcntls_gdalWarp_ClimGrid1D.py are the initial code structure., have to change this to final structure.
       RefArraysForPrcntls_gdalWarp_ClimGrid1D.py is called by RunProc_RefArraysForPrcntls_gdalWarp_ClimGrid1D_mil.sh;
       RunProc_RefArraysForPrcntls_gdalWarp_ClimGrid1D_mil.sh is in turn called by tasks.conf;
       & finally tasks.conf is in turn called by sbatchMultiProg_RefArraysForPrcntls_gdalWarp_ClimGrid1D.sh; 

-> GRACEDA directory : 17: 'GRACE_DA_gw',
                       18: 'GRACE_DA_sfsm',
                       19: 'GRACE_DA_rtzsm'
       Note that the scripts here calling nidis/nidis/model/nclimgrid/spatial_resolution/GRACEDA/RefArrsForPrcntl_gdalWarp_ClimGrid1D.py are the initial code structure, have to change this to final structure.
       RefArrsForPrcntl_gdalWarp_ClimGrid1D.py is called by RunProcess_RefArrsForPrcntl_ClimGrid1D.sh;
       RunProcess_RefArrsForPrcntl_ClimGrid1D.sh is in turn called by Execfile_GRACE_ClimGrid1D;
       & finally Execfile_GRACE_ClimGrid1D is in turn called by sbatchpods_RefArrsForPrcntl_ClimGrid1D.sh; 

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
                    43: 'EDDI_12mn',
       Note that the scripts here calling nidis/nidis/model/nclimgrid/spatial_resolution/EDDI/InfoArrays_gdalWarp_ClimGrid1D.py are the initial code structure, have to change this to final structure.
       InfoArrays_gdalWarp_ClimGrid1D.py is called by RunProc_InfoArrays_gdalWarp_ClimGrid1D.sh;
       RunProc_InfoArrays_gdalWarp_ClimGrid1D.sh is in turn called by Execfile_InfoArrays_gdalWarp_ClimGrid1D;
       & Execfile_InfoArrays_gdalWarp_ClimGrid1D is in turn called by sbatchpods_InfoArrays_gdalWarp_ClimGrid1D.sh; 

-> NLDAS2 directory : 44: 'NLDAS2D_1MSM_Mosaic',
                      45: 'NLDAS2D_1MSM_Noah',
                      46: 'NLDAS2D_1MSM_SAC',
                      47: 'NLDAS2D_1MSM_VIC',
                      48: 'NLDAS2D_TCSM_Mosaic',
                      49: 'NLDAS2D_TCSM_Noah',
                      50: 'NLDAS2D_TCSM_SAC',
                      51: 'NLDAS2D_TCSM_VIC'
       Note that the scripts here calling nidis/nidis/model/nclimgrid/spatial_resolution/InfoArrays_gdalWarp_ClimGrid1D_DailyCollToMonthly_Indicators_44_to_51.py are the initial code structure, have to change this to final structure.
       InfoArrays_gdalWarp_ClimGrid1D_DailyCollToMonthly_Indicators_44_to_51.py is called by RunProcess_InfoArrs_ClmGrd1D_DlyCllToMnthly.sh;
       RunProcess_InfoArrs_ClmGrd1D_DlyCllToMnthly.sh is in turn called by Execfile_InfoArrays_ClmGrd1D_DlyCllToMnthly_1;
       & Execfile_InfoArrays_ClmGrd1D_DlyCllToMnthly_1 is in turn called by sbatchpods_InfArrs_ClmGrd1D_DlyCllToMnthly_1.sh; 

-> VegDRI directory : 68: 'VegDRI'
       Note that the scripts here calling nidis/nidis/model/nclimgrid/spatial_resolution/VegDRI/RefArraysForPrcntl_ClimGrid.py are the initial code structure, have to change this to final structure.
       RefArraysForPrcntl_ClimGrid.py is called by RunProc_RefArraysForPrcntl_ClimGrid_mil.sh;
       RunProc_RefArraysForPrcntl_ClimGrid_mil.sh is in turn called by RefArraysForPrcntl_ClimGrid_tasks_*.conf;
       & RefArraysForPrcntl_ClimGrid_tasks_*.conf are in turn called by sbatchpods_RefArraysForPrcntl_ClimGrid_mil.sh; 






