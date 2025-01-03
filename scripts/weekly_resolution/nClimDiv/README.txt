Scripts and corresponding indicator numbers/names:
------------------------------------------------------

-> GRACEDA directory : 17: 'GRACE_DA_gw',
                       18: 'GRACE_DA_sfsm',
                       19: 'GRACE_DA_rtzsm'
       Note that the script here calling nidis/nidis/model/nclimdiv/weekly_resolution/GRACEDA/PrepRefArraysFromInfoArrays_GRACEDA.py is the initial code structure, have to change this to final structure. 
       This PrepRefArraysFromInfoArrays_GRACEDA.py is called by GRACEDA/Run_PrepRefArraysFromInfoArrays_GRACEDA.sh; 
 
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
       Note that the script here calling nidis/nidis/model/nclimdiv/weekly_resolution/EDDI/PrepRefArraysFromInfoArrays_EDDI.py is the initial code structure, I have to change this to final structure.
       This PrepRefArraysFromInfoArrays_EDDI.py is called by EDDI/Run_PrepRefArraysFromInfoArrays_EDDI.sh;

-> VegDRI directory : 68: 'VegDRI'
       Note that the script here calling nidis/nidis/model/nclimdiv/weekly_resolution/VegDRI/PrepRefArraysFromInfoArrays_VegDRI.py is the initial code structure, have to change this to final structure.
       This PrepRefArraysFromInfoArrays_VegDRI.py is called by VegDRI/Run_PrepRefArraysFromInfoArrays_VegDRI.sh;

-> QuickDRI directory : 69: 'QuickDRI'
       Note that the script here calling nidis/nidis/model/nclimdiv/weekly_resolution/QuickDRI/PrepRefArraysFromInfoArrays_QuickDRI.py is the initial code structure, have to change this to final structure.
       This PrepRefArraysFromInfoArrays_QuickDRI.py is called by QuickDRI/Run_PrepRefArraysFromInfoArrays_QuickDRI.sh;

-> SNODAS directory : 96: 'SNODAS'
       Note that the script here calling nidis/nidis/model/nclimdiv/weekly_resolution/SNODAS/InfoArrays_ClimDivsSplit_V3.py is the initial code structure, have to change this to final structure.
       This InfoArrays_ClimDivsSplit_V3.py is called by RunProcess_InfoArrays_ClimDivsSplit.sh;
       This RunProcess_InfoArrays_ClimDivsSplit.sh is in turn called by Execfile_InfoArrays_ClimDivsSplit_?Of4;
       & finally Execfile_InfoArrays_ClimDivsSplit_?Of4 are in turn called by sbatchpods_InfoArrays_ClimDivsSplit_?Of4.sh; 

-> ESA_CCI directory : 97: 'ESA_CCI'
       Note that the script here calling nidis/nidis/model/nclimdiv/weekly_resolution/ESA_CCI/InfoArrays_ClimDivs_DailyCollToMonthly.py is the initial code structure, have to change this to final structure.
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
       Note that the script here calling nidis/nidis/model/nclimdiv/weekly_resolution/IMERG/InfoArrays_ClimDivs_DailyCollToMonthly.py is the initial code structure, have to change this to final structure.
       This InfoArrays_ClimDivs_DailyCollToMonthly.py is called by RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.sh;
       This RunProcess_InfoArrs_ClmDvs_DlyCllToMnthly.sh is in turn called by Execfile_InfoArrays_ClimDivs_DailyCollToMonthly;
       & finally Execfile_InfoArrays_ClimDivs_DailyCollToMonthly in turn called by sbatchpods_InfArrs_ClmDvs_DlyCllToMnthly.sh; 

-> BlendedVHP directory  :  109: 'SmNDVI_BlendedVHP',
                            110: 'TCI_BlendedVHP',
                            111: 'VCI_BlendedVHP',
                            112: 'VHI_BlendedVHP'
       Note that the script here calling nidis/nidis/model/nclimdiv/weekly_resolution/BlendedVHP/InfoArrays_ClimDivsSplit_V3_b.py is the initial code structure, have to change this to final structure.
       This InfoArrays_ClimDivsSplit_V3_b.py is called by RunProcess_InfoArrays_ClimDivsSplit.sh;
       This RunProcess_InfoArrays_ClimDivsSplit.sh is in turn called by  Execfile_InfoArrays_ClimDivsSplit_?Of6;
       & finally  Execfile_InfoArrays_ClimDivsSplit_?Of6 in turn called by sbatchpods_InfoArrays_ClimDivsSplit_; 

-> GlobSnow3 directory :  113: 'GlobSnow3'
       Note that the script here calling nidis/nidis/model/nclimdiv/weekly_resolution/GlobSnow3/InfoArrays_ClimDivs.py is the initial code structure, have to change this to final structure.
       This GlobSnow3/InfoArrays_ClimDivs.py is called by RunProcess_InfoArrays_ClimDivs.sh;
       This RunProcess_InfoArrays_ClimDivs.sh is in turn called by Execfile_InfoArrays_ClimDivs_Part?;
       & finally Execfile_InfoArrays_ClimDivs_Part? in turn called by sbatchpods_InfoArrays_ClimDivs_Part?.sh; 




