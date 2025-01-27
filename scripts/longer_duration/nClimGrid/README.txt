Scripts and corresponding indicator numbers/names:
------------------------------------------------------

-> NCEI directory :  6: 'prcp_02_nCG',
                     7: 'prcp_03_nCG',
                     8: 'prcp_06_nCG',
                     9: 'prcp_09_nCG',
                    10: 'prcp_12_nCG',
                    11: 'prcp_24_nCG',
                    12: 'prcp_36_nCG',
                    13: 'prcp_48_nCG',
                    14: 'prcp_60_nCG',
                    15: 'prcp_72_nCG',
       Note that the script here calling nidis/nidis/model/nclimgrid/longer_duration/NCEI/MeanMetInfoArrays_ClimGrid1D.py is the initial code structure, have to change this to final structure.
       MeanMetInfoArrays_ClimGrid1D.py is called ExecPoDS_CreateMeanMetInfoArrays_ClimGrid1D, in turn called by sbatchpods_CreateMeanMetInfoArrays_ClimGrid1D.sh;

-> ESIs directory :  70: 'ESI_4wk',
                     71: 'ESI_12wk'
       Note that the script here calling nidis/nidis/model/nclimgrid/longer_duration/ESIs/MeanMetInfoArrays_InclNans_ClimGrid1D.py is the initial code structure, have to change this to final structure.
       This MeanMetInfoArrays_InclNans_ClimGrid1D.py is called by MeanMetInfoArrays_InclNans_ClimGrid1D_Conf.conf;
       this MeanMetInfoArrays_InclNans_ClimGrid1D_Conf.conf is in turn called by Run_MeanMetInfoArrays_InclNans_ClimGrid1D.sh;
       & finally this Run_MeanMetInfoArrays_InclNans_ClimGrid1D.sh is in turn called by bsbatchMultiProg_MeanMetInfoArrays_InclNans_ClimGrid1D_mil.sh

