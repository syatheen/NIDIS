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

-> 
 
 
