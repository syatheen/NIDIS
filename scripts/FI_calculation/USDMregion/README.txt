Scripts for ALL indicators:
---------------------------

-> nidis/nidis/model/USDMregion/FI_calculation/CalcFracMI_ClimDivs_AllValid_V2b_NDFeat_NewSeas.py is called by RunProc_ClcFrcMI_ClmDvs_AllVld_V2b_NDFeat_NewSeas.sh;
   RunProc_ClcFrcMI_ClmDvs_AllVld_V2b_NDFeat_NewSeas.sh is in turn called by the files Execfile_ClcFrcMI_ClmDvs_AllVld_V2b_1DFeat_NewSeas_?;
   & finally Execfile_ClcFrcMI_ClmDvs_AllVld_V2b_1DFeat_NewSeas_? are in turn called by sbatchpods_NClcFrcMI_ClmDvs_AllVld_V2b_1DFeatSeas_?.sh;
   Note that the scripts here calling nidis/nidis/model/USDMregion/FI_calculation/CalcFracMI_ClimDivs_AllValid_V2b_NDFeat_NewSeas.py are the initial code structure, I have to change this to final structure.

-> nidis/nidis/model/USDMregion/FI_calculation/CalcFracMI_ClimDivs_V2b_NDFeat_NewSeas.py is called by RunProc_ClcFrcMI_ClmDvs_V2b_NDFeat_NewSeas.sh;
   RunProc_ClcFrcMI_ClmDvs_V2b_NDFeat_NewSeas.sh is in turn called by the files Execfile_ClcFrcMI_ClmDvs_V2b_1DFeat_NewSeas_?;
   & finally Execfile_ClcFrcMI_ClmDvs_V2b_1DFeat_NewSeas_? are in turn called by sbatchpods_NClcFrcMI_ClmDvs_V2b_1DFeatSeas_?.sh;
   Note that the scripts here calling nidis/nidis/model/USDMregion/FI_calculation/CalcFracMI_ClimDivs_V2b_NDFeat_NewSeas.py are the initial code structure, I have to change this to final structure.

