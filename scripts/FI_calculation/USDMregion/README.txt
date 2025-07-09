Scripts for ALL indicators:
---------------------------

FOR OLD CODE FROM JHM PAPER (Ignore the 'ClimDivs' designation in below filenames, these are indeed for USDM region scale):

-> nidis/nidis/model/USDMregion/FI_calculation/CalcFracMI_ClimDivs_AllValid_V2b_NDFeat_NewSeas.py is called by RunProc_ClcFrcMI_ClmDvs_AllVld_V2b_NDFeat_NewSeas.sh;
   RunProc_ClcFrcMI_ClmDvs_AllVld_V2b_NDFeat_NewSeas.sh is in turn called by the files Execfile_ClcFrcMI_ClmDvs_AllVld_V2b_1DFeat_NewSeas_?;
   & finally Execfile_ClcFrcMI_ClmDvs_AllVld_V2b_1DFeat_NewSeas_? are in turn called by sbatchpods_NClcFrcMI_ClmDvs_AllVld_V2b_1DFeatSeas_?.sh;
   Note that the scripts here calling nidis/nidis/model/USDMregion/FI_calculation/CalcFracMI_ClimDivs_AllValid_V2b_NDFeat_NewSeas.py are the initial code structure, I have to change this to final structure.

-> nidis/nidis/model/USDMregion/FI_calculation/CalcFracMI_ClimDivs_V2b_NDFeat_NewSeas.py is called by RunProc_ClcFrcMI_ClmDvs_V2b_NDFeat_NewSeas.sh;
   RunProc_ClcFrcMI_ClmDvs_V2b_NDFeat_NewSeas.sh is in turn called by the files Execfile_ClcFrcMI_ClmDvs_V2b_1DFeat_NewSeas_?;
   & finally Execfile_ClcFrcMI_ClmDvs_V2b_1DFeat_NewSeas_? are in turn called by sbatchpods_NClcFrcMI_ClmDvs_V2b_1DFeatSeas_?.sh;
   Note that the scripts here calling nidis/nidis/model/USDMregion/FI_calculation/CalcFracMI_ClimDivs_V2b_NDFeat_NewSeas.py are the initial code structure, I have to change this to final structure.

FOR NEW CORRECT CODE:

-> ClcFI_USDMRgns_V2bPrcCrr_NDFeat_NwSs.py
     This is the NEW correct version of the above code CalcFracMI_ClimDivs_V2b_NDFeat_NewSeas.py, and used for the final deliverables.
     Note that this ClcFI_USDMRgns_V2bPrcCrr_NDFeat_NwSs.py file  is the initial code structure, have to convert this to final structure.
********
-> nidis/nidis/model/USDMregion/FI_calculation/ClcFI_USDMRgns_AllVld_V2bPrcCrr_NDFeat_NwSs.py is called by Run_ClcFI_USDMRgns_AllVld_V2bPrcCrr_NDFeat_NwSs.sh;

  --> For single-indicator: Run_ClcFI_USDMRgns_AllVld_V2bPrcCrr_NDFeat_NwSs.sh is in turn called by the files Run_ClcFI_USDMRgns_AllVld_V2bPrcCrr_NDFeat_NwSs_Cnf_[1-7].conf, which finally are respectively in turn called by sbatchMProg_ClcFI_USDMRgns_AllVld_V2bPrcCrr_NDFt_NwSs_Mil_NoLast150.sh and sbatchMProg_ClcFI_USDMRgns_AllVld_V2bPrcCrr_NDFt_NwSs_Mil_Last150.sh;

  --> For all-113 multi-indicator: Run_ClcFI_USDMRgns_AllVld_V2bPrcCrr_NDFeat_NwSs.sh is in turn called by the file Run_ClcFI_USDMRgns_AllVld_V2bPrcCrr_NDFeat_NwSs_Cnf_b.conf, which finally is in turn called by sbatchMProg_ClcFI_USDMRgns_AllVld_V2bPrcCrr_NDFt_NwSs_Mil_113.sh;

  --> For remotely sensed and modeled multi-indicators: Run_ClcFI_ClmDvs_AllVld_V2bPrcCrr_NDFeat_NwSs.sh is in turn called by the file Run_ClcFI_USDMRgns_AllVld_V2bPrcCrr_NDFeat_NwSs_Cnf_c.conf, which finally is in turn called by sbatchMProg_ClcFI_USDMRgns_AllVld_V2bPrcCrr_NDFt_NwSs_Mil_Not1or113.sh;

   Note that the scripts here calling nidis/nidis/model/USDMregion/FI_calculation/ClcFI_USDMRgns_AllVld_V2bPrcCrr_NDFeat_NwSs.py are the initial code/calling structure, I have to change this to final structure.

-> nidis/nidis/model/USDMregion/FI_calculation/ClcFI_USDMRgns_V2bPrcCrr_NDFeat_NwSs.py is called by Run_ClcFI_USDMRgns_V2bPrcCrr_NDFeat_NwSs.sh;

  --> For single-indicator: Run_ClcFI_USDMRgns_V2bPrcCrr_NDFeat_NwSs.sh is in turn called by the files Run_ClcFI_USDMRgns_V2bPrcCrr_NDFeat_NwSs_Cnf_[1-7].conf, which finally are respectively in turn called by sbatchMProg_ClcFI_USDMRgns_V2bPrcCrr_NDFt_NwSs_Mil_NoLast150.sh and sbatchMProg_ClcFI_USDMRgns_V2bPrcCrr_NDFt_NwSs_Mil_Last150.sh;

  --> No multi-indicator run applicable for this ClcFI_USDMRgns_V2bPrcCrr_NDFeat_NwSs.p file

   Note that the scripts here calling nidis/nidis/model/USDMregion/FI_calculation/ClcFI_USDMRgns_V2bPrcCrr_NDFeat_NwSs.py are the initial code/calling structure, I have to change this to final structure.

