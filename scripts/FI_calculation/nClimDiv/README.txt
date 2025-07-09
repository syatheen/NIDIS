Scripts for ALL indicators:
---------------------------

-> nidis/nidis/model/nclimdiv/FI_calculation/ClcFI_ClmDvs_AllVld_V2bPrcCrr_NDFeat_NwSs.py is called by Run_ClcFI_ClmDvs_AllVld_V2bPrcCrr_NDFeat_NwSs.sh;

  --> For single-indicator: Run_ClcFI_ClmDvs_AllVld_V2bPrcCrr_NDFeat_NwSs.sh is in turn called by the files Run_ClcFI_ClmDvs_AllVld_V2bPrcCrr_NDFeat_NwSs_Cnf_d_[1/2].conf, which finally are respectively in turn called by sbatchMProg_ClcFI_ClmDvs_AllVld_V2bPrcCrr_NDFt_NwSs_Mil_d_[1/2].sh;

  --> For all-113 multi-indicator: Run_ClcFI_ClmDvs_AllVld_V2bPrcCrr_NDFeat_NwSs.sh is in turn called by the file Run_ClcFI_ClmDvs_AllVld_V2bPrcCrr_NDFeat_NwSs_Cnf_e.conf, which finally is in turn called by sbatchMProg_ClcFI_ClmDvs_AllVld_V2bPrcCrr_NDFt_NwSs_Mil_113.sh;

  --> For remotely sensed and modeled multi-indicators: Run_ClcFI_ClmDvs_AllVld_V2bPrcCrr_NDFeat_NwSs.sh is in turn called by the file Run_ClcFI_ClmDvs_AllVld_V2bPrcCrr_NDFeat_NwSs_Cnf_f.conf, which finally is in turn called by sbatchMProg_ClcFI_ClmDvs_AllVld_V2bPrcCrr_NDFt_NwSs_Mil_Not1or113.sh

   Note that the scripts here calling nidis/nidis/model/nclimdiv/FI_calculation/ClcFI_ClmDvs_AllVld_V2bPrcCrr_NDFeat_NwSs.py are the initial code/calling structure, I have to change this to final structure.

-> nidis/nidis/model/nclimdiv/FI_calculation/ClcFI_ClmDvs_V2bPrcCrr_NDFeat_NwSs.py is called by Run_ClcFI_ClmDvs_V2bPrcCrr_NDFeat_NwSs.sh;

  --> For single-indicator: Run_ClcFI_ClmDvs_V2bPrcCrr_NDFeat_NwSs.sh is in turn called by the files Run_ClcFI_ClmDvs_V2bPrcCrr_NDFeat_NwSs_Cnf_d_[1/2].conf, which finally are respectively in turn called by sbatchMProg_ClcFI_ClmDvs_V2bPrcCrr_NDFt_NwSs_Mil_d_[1/2].sh;

  --> No multi-indicator run applicable for this ClcFI_ClmDvs_V2bPrcCrr_NDFeat_NwSs.py file

   Note that the scripts here calling nidis/nidis/model/nclimdiv/FI_calculation/ClcFI_ClmDvs_V2bPrcCrr_NDFeat_NwSs.py are the initial code/calling structure, I have to change this to final structure.


