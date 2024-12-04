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

-> ESIs script bash_submission_indicators_70_to_71.sh :   70: 'ESI_4wk',
                                                          71: 'ESI_12wk',
   
 
 
