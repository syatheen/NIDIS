# Coded by Soni Yatheendradas
#          on Dec 9, 2022
# Modified by Jordan A. Caraballo-Vega
#          on April 15, 2024

from __future__ import division

import sys
import copy
import time
import logging
import numpy as np
import geopandas as gpd

from datetime import datetime
from scipy.stats import entropy
from sklearn.feature_selection import mutual_info_classif
from nidis.model.MI_classif_1ValueForMultiFeatures_Code \
    import MI_classif_1ValueForMultiFeatures
from nidis.model.Split_YYYYMMDD_To_Components_File \
    import Split_YYYYMMDD_To_Components
from nidis.model.TimeSliceStrict_YYYYMMDDAndRefArrays_File \
    import TimeSliceStrict_YYYYMMDDAndRefArrays

__all__ = [
    "Split_YYYYMMDD_To_Components",
    "TimeSliceStrict_YYYYMMDDAndRefArrays"
]

# NOTE: sys.argv indices start at 1, not 0
# Python arguments to this program will be (for now):
# IfMakeTargetBinary IfIncludeD0AsDrought BeginYYYYMMDD_Str EndYYYYMMDD_Str TargetVariable SpatialDomain NumInpLayers NumInpsForNDFracMI WhichInpCombinForNDFracMI Which_1D_Pixel WhichSeason
# ArgNum     1                                    2                                      3                                   4                               5                            6                       7                      8                                    9                                               10                         11


def main(
    IfMakeTargetBinary, # Choices are 'Y' for yes, and 'N' for no
    IfIncludeD0AsDrought, # Choices are 'Y' for yes, and 'N' for no
    BeginYYYYMMDD_Str, # Beginning YYYYMMDD, this is also a Tuesday
    EndYYYYMMDD_Str, # Ending YYYYMMDD, this is also a Tuesday
    TargetVariable, # Choices are 'USDM', 'CPC_S' (for short-term), 'CPC_LE' (for long-term Eastern), and 'CPC_LW' (for long-term Western)  
    SpatialDomain, # Choices are 'CONUS'
    WhichArgForNumInpLayers, # Which argument has info about number of input layers
    NumInpLayers, # 113 for all input channels, 0 for All CPC Blend input channels, -10 for remotely-sensed, -11 for modeled, -12 for modeled+PrecipObs, -50 for all NDMC Blend input channels
    NumInpsForNDFracMI,
    WhichInpCombinForNDFracMI, # 0-start
    Which_1D_Pixel, # Which 1D number of nClimGrid pixels # 0-start
    WhichSeason # Choices are 'P' for sPring (Mar-May), 'U' for sUmmer (Jun-Aug), 'F' for Fall (Sep-Nov), 'W' for Winter (Dec-Feb), 'A' for all-seasons-together
):
    print("Start time: ", time.time())

    """
    IfMakeTargetBinary = sys.argv[1] # Choices are 'Y' for yes, and 'N' for no
    IfIncludeD0AsDrought = sys.argv[2] # Choices are 'Y' for yes, and 'N' for no
    BeginYYYYMMDD_Str = sys.argv[3] # Beginning YYYYMMDD, this is also a Tuesday
    EndYYYYMMDD_Str = sys.argv[4] # Ending YYYYMMDD, this is also a Tuesday
    TargetVariable = sys.argv[5] # Choices are 'USDM', 'CPC_S' (for short-term), 'CPC_LE' (for long-term Eastern), and 'CPC_LW' (for long-term Western)  
    SpatialDomain = sys.argv[6] # Choices are 'CONUS'
    WhichArgForNumInpLayers = 7 # Which argument has info about number of input layers
    NumInpLayers = int(round(float(sys.argv[WhichArgForNumInpLayers]))) # 113 for all input channels, 0 for All CPC Blend input channels, -10 for remotely-sensed, -11 for modeled, -12 for modeled+PrecipObs, -50 for all NDMC Blend input channels
    NumInpsForNDFracMI = sys.argv[8]
    WhichInpCombinForNDFracMI = int(round(float(sys.argv[9]))) # 0-start
    Which_1D_Pixel = int(round(float(sys.argv[10]))) # Which 1D number of nClimGrid pixels # 0-start
    WhichSeason = sys.argv[11] # Choices are 'P' for sPring (Mar-May), 'U' for sUmmer (Jun-Aug), 'F' for Fall (Sep-Nov), 'W' for Winter (Dec-Feb), 'A' for all-seasons-together
    """

    Num_random_states = 101
    n_neighbors = 3

    BeginYYYYMMDD = int(round(float(BeginYYYYMMDD_Str)))
    EndYYYYMMDD = int(round(float(EndYYYYMMDD_Str)))

    # BEGIN code arguments / editable section

    if WhichSeason not in ['P', 'U', 'F', 'W', 'A']:
        sys.exit("Invalid WhichSeason Choice: should be 'P, 'U', 'F', 'W' or 'A'!!!")

    if IfMakeTargetBinary not in ['Y', 'N']:
        sys.exit("Invalid IfMakeTargetBinary Choice: should be 'Y' or 'N'!!!")

    if IfIncludeD0AsDrought not in ['Y', 'N']:
        sys.exit("Invalid IfIncludeD0AsDrought Choice: should be 'Y' or 'N'!!!")

    if ( (TargetVariable == 'USDM') and (SpatialDomain == 'CONUS') and
            (not NumInpLayers in [113, 0, -10, -11, -12, -50]) ):
        #sys.exit("NumInpLayers needs to be 113, 0, -10, -11, -12, or -50!!!")
        print("***********************NumInpLayers needs to be 113, 0, -10, -11, -12, or -50!!!***************")

    ClimGrid1DShpFile = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/nClimGrid_as_poly_NoNans.shp'

    print("Defined ClimGrid1DShpFile filename")

    MinimumWindowSize = 1
    MaximumWindowSize = 35

    MinSamplesForFracI = 100

    # Inp channel info. 
        # 1: Z-index ;
        # 2: 60-month Z-index ;
        # 3: PMDI; 
        # 4: PHDI; 
        # 5: 1-month nCG precip;
        # 6: 2-month nCG precip;
        # 7: 3-month nCG precip;
        # 8: 6-month nCG precip;
        # 9: 9-month nCG precip;
        # 10: 12-month nCG precip;
        # 11: 24-month nCG precip;
        # 12: 36-month nCG precip;
        # 13: 48-month nCG precip;
        # 14: 60-month nCG precip;
        # 15: 72-month nCG precip;
        # 16: CPC soil moisture;
        # 17: GRACE DA gw
        # 18: GRACE DA sfsm
        # 19: GRACE DA rtzsm
        # 20: EDDI 1-wk
        # 21: EDDI 2-wk
        # 22: EDDI 3-wk
        # 23: EDDI 4-wk
        # 24: EDDI 5-wk
        # 25: EDDI 6-wk
        # 26: EDDI 7-wk
        # 27: EDDI 8-wk
        # 28: EDDI 9-wk
        # 29: EDDI 10-wk
        # 30: EDDI 11-wk
        # 31: EDDI 12-wk
        # 32: EDDI 1-mn
        # 33: EDDI 2-mn
        # 34: EDDI 3-mn
        # 35: EDDI 4-mn
        # 36: EDDI 5-mn
        # 37: EDDI 6-mn
        # 38: EDDI 7-mn
        # 39: EDDI 8-mn
        # 40: EDDI 9-mn
        # 41: EDDI 10-mn
        # 42: EDDI 11-mn
        # 43: EDDI 12-mn
        # 44: NLDAS-2 daily 1-m SM (Mosaic)
        # 45: NLDAS-2 daily 1-m SM (Noah)
        # 46: NLDAS-2 daily 1-m SM (SAC)
        # 47: NLDAS-2 daily 1-m SM (VIC)
        # 48: NLDAS-2 daily Total Column SM (Mosaic)
        # 49: NLDAS-2 daily Total Column SM (Noah)
        # 50: NLDAS-2 daily Total Column SM (SAC)
        # 51: NLDAS-2 daily Total Column SM (VIC)
        # 52: NLDAS-2 daily Evap (Mosaic)
        # 53: NLDAS-2 daily Evap (Noah)
        # 54: NLDAS-2 daily Evap (SAC)
        # 55: NLDAS-2 daily Evap (VIC)
        # 56: NLDAS-2 daily SWE (Mosaic)
        # 57: NLDAS-2 daily SWE (Noah)
        # 58: NLDAS-2 daily SWE (SAC)
        # 59: NLDAS-2 daily SWE (VIC)
        # 60: NLDAS-2 daily Runoff (Mosaic)
        # 61: NLDAS-2 daily Runoff (Noah)
        # 62: NLDAS-2 daily Runoff (SAC)
        # 63: NLDAS-2 daily Runoff (VIC)
        # 64: NLDAS-2 daily HUC04-level streamflow (Mosaic)
        # 65: NLDAS-2 daily HUC04-level streamflow (Noah)
        # 66: NLDAS-2 daily HUC04-level streamflow (SAC)
        # 67: NLDAS-2 daily HUC04-level streamflow (VIC)
        # 68: VegDRI
        # 69: QuickDRI
        # 70: 4-week ESI
        # 71: 12-week ESI
        # 72: 1-month nCG SPI gamma
        # 73: 2-month nCG SPI gamma
        # 74: 3-month nCG SPI gamma
        # 75: 6-month nCG SPI gamma
        # 76: 9-month nCG SPI gamma
        # 77: 12-month nCG SPI gamma
        # 78: 24-month nCG SPI gamma
        # 79: 36-month nCG SPI gamma
        # 80: 48-month nCG SPI gamma
        # 81: 60-month nCG SPI gamma
        # 82: 72-month nCG SPI gamma
        # 83: 1-month nCG SPEI Pearson
        # 84: 2-month nCG SPEI Pearson
        # 85: 3-month nCG SPEI Pearson
        # 86: 6-month nCG SPEI Pearson
        # 87: 9-month nCG SPEI Pearson
        # 88: 12-month nCG SPEI Pearson
        # 89: 24-month nCG SPEI Pearson
        # 90: 36-month nCG SPEI Pearson
        # 91: 48-month nCG SPEI Pearson
        # 92: 60-month nCG SPEI Pearson
        # 93: 72-month nCG SPEI Pearson
        # 94: 1-month nCG mean air temperature
        # 95: 1-month nCG max air temperature 
        # 96: SNODAS
        # 97: ESA-CCI
        # 98: 1-month IMERG;
        # 99: 2-month IMERG;
        # 100: 3-month IMERG;
        # 101: 6-month IMERG;
        # 102: 9-month IMERG;
        # 103: 12-month IMERG;
        # 104: 24-month IMERG;
        # 105: 36-month IMERG;
        # 106: 48-month IMERG;
        # 107: 60-month IMERG;
        # 108: 72-month IMERG;
        # 109: Smoothed NDVI (BlendedVHP)
        # 110: TCI (BlendedVHP)
        # 111: VCI (BlendedVHP)
        # 112: VHI (BlendedVHP)
        # 113: GlobSnow3

    if NumInpLayers > 0: # All input channels
        InpLayerNumsCombination = list(range(1,NumInpLayers+1))
    elif NumInpLayers == 0: # All CPC Blend input channels
        InpLayerNumsCombination = [1, 2, 3, 4, 5, 7, 8, 10, 11, 14, 16]
    elif NumInpLayers < 0: # Predecided Groupings of input channels
        if NumInpLayers == -10: # Remotely-sensed
            InpLayerNumsCombination = [*range(68, 72), *range(97, 114)]
        elif NumInpLayers == -11: # Modeled
            InpLayerNumsCombination = [*range(16, 68), 96]
        elif NumInpLayers == -12: # Modeled+PrecipObs
            InpLayerNumsCombination = [*range(5, 68), 96]
        elif NumInpLayers == -50: # All NDMC Blend input channels
            InpLayerNumsCombination = [45, 49, 72, *range(74, 79), 81, 83, 87, 92]
        else:
            sys.exit("Invalid choice in NumInpLayers < 0!!!")
        #end of if NumInpLayers == -10
    #end of if NumInpLayers > 0

    DictofNumNamePairs_Channels = {
        1: 'Z_index',
        2: 'Z_index_60_month',
        3: 'PMDI',
        4: 'PHDI',
        5: 'prcp_01_nCG',
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
        16: 'CPC_soil_moisture',
        17: 'GRACE_DA_gw',
        18: 'GRACE_DA_sfsm',
        19: 'GRACE_DA_rtzsm',
        20: 'EDDI_1wk',
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
        44: 'NLDAS2D_1MSM_Mosaic',
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
        68: 'VegDRI',
        69: 'QuickDRI',
        70: 'ESI_4wk',
        71: 'ESI_12wk',
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
        95: 'tmax_01_nCG',
        96: 'SNODAS',
        97: 'ESA_CCI',
        98: 'IMERG_01',
        99: 'IMERG_02',
        100: 'IMERG_03',
        101: 'IMERG_06',
        102: 'IMERG_09',
        103: 'IMERG_12',
        104: 'IMERG_24',
        105: 'IMERG_36',
        106: 'IMERG_48',
        107: 'IMERG_60',
        108: 'IMERG_72',
        109: 'SmNDVI_BlendedVHP',
        110: 'TCI_BlendedVHP',
        111: 'VCI_BlendedVHP',
        112: 'VHI_BlendedVHP',
        113: 'GlobSnow3'
    }

    #SY: Begin partially moved portion from that commented further below
    ColCombinations = np.loadtxt(
        'Combinations' + NumInpsForNDFracMI + 'of' + str(NumInpLayers) + '.txt',
        dtype='int', ndmin=2)
    SelectCols = ColCombinations[WhichInpCombinForNDFracMI, :]
    SelectCols = SelectCols - 1
    # SY: End partially moved portion from that commented further below

    # SY: Begin partially moved portion from that commented further below
    Inp_names_list = []
    if NumInpLayers >= 0:
        for ii in range(SelectCols.size):
            Inp_names_list.append(DictofNumNamePairs_Channels[SelectCols[ii]+1])
    # SY: End partially moved portion from that commented further below
        InpLayersCombination = copy.deepcopy(Inp_names_list)
    else: # if NumInpLayers >= 0
        InpLayersCombination = []
        for WhichInpLayer in range(1,len(InpLayerNumsCombination)+1):
            InpLayersCombination.append( DictofNumNamePairs_Channels[InpLayerNumsCombination[WhichInpLayer-1]] )
    # end of if NumInpLayers >= 0

    # print("len(InpLayersCombination) is ", len(InpLayersCombination))
    logging.info(f"InpLayersCombination is {InpLayersCombination}")

    if SpatialDomain in ['CONUS']:

        if TargetVariable == 'USDM':

            TargetVariable_ShortStr = 'U'

            SingleUnifiedDataFilename_USDM = '/discover/nobackup/projects/nca/syatheen/USDM/InfoArrsBatchFrmWeekly_New_20000104To20220621.npz'  #YYYYMMDD_Of_InfoArray, InfoArray

            SingleUnifiedDataFilename = 'Placeholder.npz'

            SingleUnifiedDataFilename_OverallPerc = 'Placeholder.npz'

            if ( ('prcp_01_nCG' in InpLayersCombination) or
                    ('prcp_02_nCG' in InpLayersCombination) or
                    ('prcp_03_nCG' in InpLayersCombination) or
                    ('prcp_06_nCG' in InpLayersCombination) or
                    ('prcp_09_nCG' in InpLayersCombination) or
                    ('prcp_12_nCG' in InpLayersCombination) or
                    ('prcp_24_nCG' in InpLayersCombination) or
                    ('prcp_36_nCG' in InpLayersCombination) or
                    ('prcp_48_nCG' in InpLayersCombination) or
                    ('prcp_60_nCG' in InpLayersCombination) or
                    ('prcp_72_nCG' in InpLayersCombination) or
                    ('SPI_gamma_01_nCG' in InpLayersCombination) or
                    ('SPI_gamma_02_nCG' in InpLayersCombination) or
                    ('SPI_gamma_03_nCG' in InpLayersCombination) or
                    ('SPI_gamma_06_nCG' in InpLayersCombination) or
                    ('SPI_gamma_09_nCG' in InpLayersCombination) or
                    ('SPI_gamma_12_nCG' in InpLayersCombination) or
                    ('SPI_gamma_24_nCG' in InpLayersCombination) or
                    ('SPI_gamma_36_nCG' in InpLayersCombination) or
                    ('SPI_gamma_48_nCG' in InpLayersCombination) or
                    ('SPI_gamma_60_nCG' in InpLayersCombination) or
                    ('SPI_gamma_72_nCG' in InpLayersCombination) or
                    ('SPEI_pear_01_nCG' in InpLayersCombination) or
                    ('SPEI_pear_02_nCG' in InpLayersCombination) or
                    ('SPEI_pear_03_nCG' in InpLayersCombination) or
                    ('SPEI_pear_06_nCG' in InpLayersCombination) or
                    ('SPEI_pear_09_nCG' in InpLayersCombination) or
                    ('SPEI_pear_12_nCG' in InpLayersCombination) or
                    ('SPEI_pear_24_nCG' in InpLayersCombination) or
                    ('SPEI_pear_36_nCG' in InpLayersCombination) or
                    ('SPEI_pear_48_nCG' in InpLayersCombination) or
                    ('SPEI_pear_60_nCG' in InpLayersCombination) or
                    ('SPEI_pear_72_nCG' in InpLayersCombination) or
                    ('tavg_01_nCG' in InpLayersCombination) or
                    ('tmax_01_nCG' in InpLayersCombination) ):

                nCG_PossibleInpLayerNamesList = ['prcp_01_nCG', 'prcp_02_nCG','prcp_03_nCG',
                                    'prcp_06_nCG', 'prcp_09_nCG', 'prcp_12_nCG', 'prcp_24_nCG',
                                    'prcp_36_nCG', 'prcp_48_nCG', 'prcp_60_nCG', 'prcp_72_nCG',
                                    'SPI_gamma_01_nCG', 'SPI_gamma_02_nCG', 'SPI_gamma_03_nCG',
                                    'SPI_gamma_06_nCG', 'SPI_gamma_09_nCG', 'SPI_gamma_12_nCG', 'SPI_gamma_24_nCG',
                                    'SPI_gamma_36_nCG', 'SPI_gamma_48_nCG', 'SPI_gamma_60_nCG', 'SPI_gamma_72_nCG',
                                    'SPEI_pear_01_nCG', 'SPEI_pear_02_nCG', 'SPEI_pear_03_nCG',
                                    'SPEI_pear_06_nCG', 'SPEI_pear_09_nCG', 'SPEI_pear_12_nCG', 'SPEI_pear_24_nCG',
                                    'SPEI_pear_36_nCG', 'SPEI_pear_48_nCG', 'SPEI_pear_60_nCG', 'SPEI_pear_72_nCG',
                                    'tavg_01_nCG', 'tmax_01_nCG']

                Num_InpLayersCombination_In_nCG_Inps = len([iInp for iInp in InpLayersCombination if iInp in nCG_PossibleInpLayerNamesList]) 

                if Num_InpLayersCombination_In_nCG_Inps > 1:
                    sys.exit("Num_InpLayersCombination_In_nCG_Inps > 1, need to add/change code!!!")
                
                Dict_nCG_Keys_And_Values = { 'prcp_01_nCG': 'prcp_01', 
                                                                        'prcp_02_nCG': 'prcp_02',
                                                                        'prcp_03_nCG': 'prcp_03',
                                                                        'prcp_06_nCG': 'prcp_06',
                                                                        'prcp_09_nCG': 'prcp_09',
                                                                        'prcp_12_nCG': 'prcp_12',
                                                                        'prcp_24_nCG': 'prcp_24',
                                                                        'prcp_36_nCG': 'prcp_36',
                                                                        'prcp_48_nCG': 'prcp_48',
                                                                        'prcp_60_nCG': 'prcp_60',
                                                                        'prcp_72_nCG': 'prcp_72',
                                                                        'SPI_gamma_01_nCG': 'spi_gamma_01', 
                                                                        'SPI_gamma_02_nCG': 'spi_gamma_02',
                                                                        'SPI_gamma_03_nCG': 'spi_gamma_03',
                                                                        'SPI_gamma_06_nCG': 'spi_gamma_06',
                                                                        'SPI_gamma_09_nCG': 'spi_gamma_09',
                                                                        'SPI_gamma_12_nCG': 'spi_gamma_12',
                                                                        'SPI_gamma_24_nCG': 'spi_gamma_24',
                                                                        'SPI_gamma_36_nCG': 'spi_gamma_36',
                                                                        'SPI_gamma_48_nCG': 'spi_gamma_48',
                                                                        'SPI_gamma_60_nCG': 'spi_gamma_60',
                                                                        'SPI_gamma_72_nCG': 'spi_gamma_72',
                                                                        'SPEI_pear_01_nCG': 'spei_pearson_01', 
                                                                        'SPEI_pear_02_nCG': 'spei_pearson_02',
                                                                        'SPEI_pear_03_nCG': 'spei_pearson_03',
                                                                        'SPEI_pear_06_nCG': 'spei_pearson_06',
                                                                        'SPEI_pear_09_nCG': 'spei_pearson_09',
                                                                        'SPEI_pear_12_nCG': 'spei_pearson_12',
                                                                        'SPEI_pear_24_nCG': 'spei_pearson_24',
                                                                        'SPEI_pear_36_nCG': 'spei_pearson_36',
                                                                        'SPEI_pear_48_nCG': 'spei_pearson_48',
                                                                        'SPEI_pear_60_nCG': 'spei_pearson_60',
                                                                        'SPEI_pear_72_nCG': 'spei_pearson_72',
                                                                        'tavg_01_nCG': 'tavg_01', 
                                                                        'tmax_01_nCG': 'tmax_01' }

                # Jordan: adding temporary path
                temp_path_npz = '/discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS'

                for ThisFromInpLayersCombination in InpLayersCombination: #SY: NOTE THAT THIS NEEDS TO BE CHANGED FOR MULTI_INPUT!!!
                    SingleUnifiedDataFilename_AllnCG = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_' + Dict_nCG_Keys_And_Values[ThisFromInpLayersCombination] + '_20060103To20210727.npz'

            #end of if ( ('prcp_01_nCG' in InpLayersCombination) or...
            # Jordan: adding temporary path
            temp_path_npz = '/discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS'

            SingleUnifiedDataFilename_GRACEDA = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_GRACEDA_20020402To20201020.npz'

            SingleUnifiedDataFilename_GRACEDA_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_GRACEDA_Corr2MonthlyPerc_20020402To20201020.npz'

            SingleUnifiedDataFilename_EDDI1wk_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI01wk_Corr2MonthlyPerc_20060103To20220412.npz'   #YYYYMMDD_Of_Array, EDDI_PrcntlArray
            SingleUnifiedDataFilename_EDDI2wk_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI02wk_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI3wk_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI03wk_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI4wk_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI04wk_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI5wk_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI05wk_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI6wk_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI06wk_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI7wk_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI07wk_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI8wk_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI08wk_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI9wk_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI09wk_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI10wk_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI10wk_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI11wk_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI11wk_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI12wk_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI12wk_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI1mn_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI01mn_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI2mn_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI02mn_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI3mn_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI03mn_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI4mn_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI04mn_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI5mn_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI05mn_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI6mn_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI06mn_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI7mn_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI07mn_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI8mn_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI08mn_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI9mn_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI09mn_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI10mn_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI10mn_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI11mn_MonthlyPerc = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI11mn_Corr2MonthlyPerc_20060103To20220412.npz'
            SingleUnifiedDataFilename_EDDI12mn = f'{temp_path_npz}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI12mn_20060103To20220412.npz'

            if ( ('NLDAS2D_1MSM_Mosaic' in InpLayersCombination) or
                    ('NLDAS2D_1MSM_Noah' in InpLayersCombination) or
                    ('NLDAS2D_1MSM_SAC' in InpLayersCombination) or
                    ('NLDAS2D_1MSM_VIC' in InpLayersCombination) or
                    ('NLDAS2D_TCSM_Mosaic' in InpLayersCombination) or
                    ('NLDAS2D_TCSM_Noah' in InpLayersCombination) or
                    ('NLDAS2D_TCSM_SAC' in InpLayersCombination) or
                    ('NLDAS2D_TCSM_VIC' in InpLayersCombination) or
                    ('NLDAS2D_EVAP_Mosaic' in InpLayersCombination) or
                    ('NLDAS2D_EVAP_Noah' in InpLayersCombination) or
                    ('NLDAS2D_EVAP_SAC' in InpLayersCombination) or
                    ('NLDAS2D_EVAP_VIC' in InpLayersCombination) or
                    ('NLDAS2D_SWE_Mosaic' in InpLayersCombination) or
                    ('NLDAS2D_SWE_Noah' in InpLayersCombination) or
                    ('NLDAS2D_SWE_SAC' in InpLayersCombination) or
                    ('NLDAS2D_SWE_VIC' in InpLayersCombination) or
                    ('NLDAS2D_RUN_Mosaic' in InpLayersCombination) or
                    ('NLDAS2D_RUN_Noah' in InpLayersCombination) or
                    ('NLDAS2D_RUN_SAC' in InpLayersCombination) or
                    ('NLDAS2D_RUN_VIC' in InpLayersCombination) or
                    ('NLDAS2D_STRMH04_Mosaic' in InpLayersCombination) or
                    ('NLDAS2D_STRMH04_Noah' in InpLayersCombination) or
                    ('NLDAS2D_STRMH04_SAC' in InpLayersCombination) or
                    ('NLDAS2D_STRMH04_VIC' in InpLayersCombination) ):

                NLDAS_2_daily_PossibleInpLayerNamesList = [ 'NLDAS2D_1MSM_Mosaic',
                                    'NLDAS2D_1MSM_Noah',
                                    'NLDAS2D_1MSM_SAC',
                                    'NLDAS2D_1MSM_VIC',
                                    'NLDAS2D_TCSM_Mosaic',
                                    'NLDAS2D_TCSM_Noah',
                                    'NLDAS2D_TCSM_SAC',
                                    'NLDAS2D_TCSM_VIC',
                                    'NLDAS2D_EVAP_Mosaic',
                                    'NLDAS2D_EVAP_Noah',
                                    'NLDAS2D_EVAP_SAC',
                                    'NLDAS2D_EVAP_VIC',
                                    'NLDAS2D_SWE_Mosaic',
                                    'NLDAS2D_SWE_Noah',
                                    'NLDAS2D_SWE_SAC',
                                    'NLDAS2D_SWE_VIC',
                                    'NLDAS2D_RUN_Mosaic',
                                    'NLDAS2D_RUN_Noah',
                                    'NLDAS2D_RUN_SAC',
                                    'NLDAS2D_RUN_VIC',
                                    'NLDAS2D_STRMH04_Mosaic',
                                    'NLDAS2D_STRMH04_Noah',
                                    'NLDAS2D_STRMH04_SAC',
                                    'NLDAS2D_STRMH04_VIC']

                Num_InpLayersCombination_In_NLDAS_2_daily_Inps = len([iInp for iInp in InpLayersCombination if iInp in NLDAS_2_daily_PossibleInpLayerNamesList]) 

                if Num_InpLayersCombination_In_NLDAS_2_daily_Inps > 1:
                    sys.exit("Num_InpLayersCombination_In_NLDAS_2_daily_Inps > 1, need to add/change code!!!")
                
                Dict_NLDAS_2_daily_Keys_And_Values = { 'NLDAS2D_1MSM_Mosaic': ['Mosaic', '1MSM', 'NA'], 
                                                                        'NLDAS2D_1MSM_Noah': ['Noah', '1MSM', 'NA'], 
                                                                        'NLDAS2D_1MSM_SAC': ['SAC', '1MSM', 'NA'], 
                                                                        'NLDAS2D_1MSM_VIC': ['VIC', '1MSM', 'NA'], 
                                                                        'NLDAS2D_TCSM_Mosaic': ['Mosaic', 'TCSM', 'NA'], 
                                                                        'NLDAS2D_TCSM_Noah': ['Noah', 'TCSM', 'NA'], 
                                                                        'NLDAS2D_TCSM_SAC': ['SAC', 'TCSM', 'NA'], 
                                                                        'NLDAS2D_TCSM_VIC': ['VIC', 'TCSM', 'NA'], 
                                                                        'NLDAS2D_EVAP_Mosaic': ['Mosaic', 'EVAP', 'NA'], 
                                                                        'NLDAS2D_EVAP_Noah': ['Noah', 'EVAP', 'NA'], 
                                                                        'NLDAS2D_EVAP_SAC': ['SAC', 'EVAP', 'NA'], 
                                                                        'NLDAS2D_EVAP_VIC': ['VIC', 'EVAP', 'NA'], 
                                                                        'NLDAS2D_SWE_Mosaic': ['Mosaic', 'SWE', 'NA'], 
                                                                        'NLDAS2D_SWE_Noah': ['Noah', 'SWE', 'NA'], 
                                                                        'NLDAS2D_SWE_SAC': ['SAC', 'SWE', 'NA'], 
                                                                        'NLDAS2D_SWE_VIC': ['VIC', 'SWE', 'NA'], 
                                                                        'NLDAS2D_RUN_Mosaic': ['Mosaic', 'RUN', 'NA'], 
                                                                        'NLDAS2D_RUN_Noah': ['Noah', 'RUN', 'NA'], 
                                                                        'NLDAS2D_RUN_SAC': ['SAC', 'RUN', 'NA'], 
                                                                        'NLDAS2D_RUN_VIC': ['VIC', 'RUN', 'NA'], 
                                                                        'NLDAS2D_STRMH04_Mosaic': ['Mosaic', 'STRM', 'H04'], 
                                                                        'NLDAS2D_STRMH04_Noah': ['Noah', 'STRM', 'H04'], 
                                                                        'NLDAS2D_STRMH04_SAC': ['SAC', 'STRM', 'H04'], 
                                                                        'NLDAS2D_STRMH04_VIC': ['VIC', 'STRM', 'H04'] }

                for ThisFromInpLayersCombination in InpLayersCombination: #SY: NOTE THAT THIS NEEDS TO BE CHANGED FOR MULTI_INPUT!!!
                    if Dict_NLDAS_2_daily_Keys_And_Values[ThisFromInpLayersCombination][2] == 'NA':
                        SingleUnifiedDataFilename_NLDAS_2_daily = 'PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_' + Dict_NLDAS_2_daily_Keys_And_Values[ThisFromInpLayersCombination][0] + '_' + Dict_NLDAS_2_daily_Keys_And_Values[ThisFromInpLayersCombination][1] + '_Crr2MnthlyPrc_20060103To20210831.npz'
                    else:
                        SingleUnifiedDataFilename_NLDAS_2_daily = 'PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_' + Dict_NLDAS_2_daily_Keys_And_Values[ThisFromInpLayersCombination][0] + '_' + Dict_NLDAS_2_daily_Keys_And_Values[ThisFromInpLayersCombination][1] + '_' + Dict_NLDAS_2_daily_Keys_And_Values[ThisFromInpLayersCombination][2] + '_Crr2MnthlyPrc_20060103To20210831.npz'
                    #end of if Dict_NLDAS_2_daily_Keys_And_Values[ThisFromInpLayersCombination][2] == 'NA'
                #end of for ThisFromInpLayersCombination in InpLayersCombination: #SY: NOTE THAT THIS NEEDS TO BE CHANGED FOR MULTI_INPUT!!!

            #end of if ( ('NLDAS2D_1MSM_Mosaic' in InpLayersCombination) or....

            #SingleUnifiedDataFilename_NLDAS_2_daily = 'Placeholder.npz'

            SingleUnifiedDataFilename_VegDRI_MonthlyPerc = 'Placeholder.npz'

            SingleUnifiedDataFilename_QuickDRI_MonthlyPerc = 'Placeholder.npz'

            SingleUnifiedDataFilename_ESImultiWeek_MonthlyPerc = 'Placeholder.npz'

            #SingleUnifiedDataFilename_SNODASnESACCI = 'Placeholder.npz'
            SingleUnifiedDataFilename_SNODAS = 'PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_SNODAS_20030930To20201229.npz'

            SingleUnifiedDataFilename_IMERG_01 = 'PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG1Month_20000704To20210525.npz'
            SingleUnifiedDataFilename_IMERG_02 = 'PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG2Month_20000801To20210525.npz'
            SingleUnifiedDataFilename_IMERG_03 = 'PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG3Month_20000829To20210525.npz'
            SingleUnifiedDataFilename_IMERG_06 = 'PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG6Month_20001128To20210525.npz'
            SingleUnifiedDataFilename_IMERG_09 = 'PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG9Month_20010227To20210525.npz'
            SingleUnifiedDataFilename_IMERG_12 = 'PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG12Month_20010605To20210525.npz'
            SingleUnifiedDataFilename_IMERG_24 = 'PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG24Month_20020604To20210525.npz'
            SingleUnifiedDataFilename_IMERG_36 = 'PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG36Month_20030603To20210525.npz'
            SingleUnifiedDataFilename_IMERG_48 = 'PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG48Month_20040601To20210525.npz'
            SingleUnifiedDataFilename_IMERG_60 = 'PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG60Month_20050531To20210525.npz'
            SingleUnifiedDataFilename_IMERG_72 = 'PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG72Month_20060606To20210525.npz'

            SingleUnifiedDataFilename_BlendedVHP_MonthlyPerc = 'PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_BlendedVHP_Corr2MonthlyPerc_20030930To20201229.npz'

            SingleUnifiedDataFilename_GlobSnow3_OverallPerc = 'Placeholder.npz'

        else: # if TargetVariable == 'USDM'

            sys.exit("Invalid TargetVariable choice, add relevant code lines!!!")

        # end of if TargetVariable == 'USDM'

        SpatialDomain_ShortStr = 'C'
    else:
        sys.exit("Invalid SpatialDomain choice, add relevant code lines!!!")
    #end of if SpatialDomain in ['CONUS']

    FracI_ClmGrd1D_AllValid_NDFeat_FileName = 'FI1X1_ClmGrd1D_V2b_New/' + NumInpsForNDFracMI + '/' + IfMakeTargetBinary + IfIncludeD0AsDrought + '_' + TargetVariable_ShortStr + '_' + SpatialDomain_ShortStr + '_' + str(Which_1D_Pixel) 
    if NumInpLayers >= 0:
        FracI_ClmGrd1D_AllValid_NDFeat_FileName = FracI_ClmGrd1D_AllValid_NDFeat_FileName + '_In' + str(NumInpLayers)
    elif NumInpLayers < 0:
        FracI_ClmGrd1D_AllValid_NDFeat_FileName = FracI_ClmGrd1D_AllValid_NDFeat_FileName + '_InM' + str(-NumInpLayers)
    #end of if NumInpLayers >= 0
    FracI_ClmGrd1D_AllValid_NDFeat_FileName = FracI_ClmGrd1D_AllValid_NDFeat_FileName + '_' + str(WhichInpCombinForNDFracMI) + '_' + WhichSeason + '.txt'

    SampSiz_ClmGrd1D_AllValid_NDFeat_FileName = 'SSiz1X1_ClmGrd1D_V2b_New/' + NumInpsForNDFracMI + '/' + IfMakeTargetBinary + IfIncludeD0AsDrought + '_' + TargetVariable_ShortStr + '_' + SpatialDomain_ShortStr + '_' + str(Which_1D_Pixel) 
    if NumInpLayers >= 0:
        SampSiz_ClmGrd1D_AllValid_NDFeat_FileName = SampSiz_ClmGrd1D_AllValid_NDFeat_FileName + '_In' + str(NumInpLayers)
    elif NumInpLayers < 0:
        SampSiz_ClmGrd1D_AllValid_NDFeat_FileName = SampSiz_ClmGrd1D_AllValid_NDFeat_FileName + '_InM' + str(-NumInpLayers)
    #end of if NumInpLayers >= 0
    SampSiz_ClmGrd1D_AllValid_NDFeat_FileName = SampSiz_ClmGrd1D_AllValid_NDFeat_FileName + '_' + str(WhichInpCombinForNDFracMI) + '_' + WhichSeason + '.txt'

    WindowSiz_ClmGrd1D_AllValid_NDFeat_FileName = 'WSiz1X1_ClmGrd1D_V2b_New/' + NumInpsForNDFracMI + '/' + IfMakeTargetBinary + IfIncludeD0AsDrought + '_' + TargetVariable_ShortStr + '_' + SpatialDomain_ShortStr + '_' + str(Which_1D_Pixel) 
    if NumInpLayers >= 0:
        WindowSiz_ClmGrd1D_AllValid_NDFeat_FileName = WindowSiz_ClmGrd1D_AllValid_NDFeat_FileName + '_In' + str(NumInpLayers)
    elif NumInpLayers < 0:
        WindowSiz_ClmGrd1D_AllValid_NDFeat_FileName = WindowSiz_ClmGrd1D_AllValid_NDFeat_FileName + '_InM' + str(-NumInpLayers)
    #end of if NumInpLayers >= 0
    WindowSiz_ClmGrd1D_AllValid_NDFeat_FileName = WindowSiz_ClmGrd1D_AllValid_NDFeat_FileName + '_' + str(WhichInpCombinForNDFracMI) + '_' + WhichSeason + '.txt'

    #ActualNumInpLayers = len(InpLayersCombination)
    #if ActualNumInpLayers < 2:
    #  sys.exit("Minimum of 2 actual input layers enforced for now!!!")

    # END code arguments / editable section

    ssstart_Overall = datetime.now()

    # Jordan: Good through here

    ClimGrid1DShp = gpd.read_file(ClimGrid1DShpFile)
    PxlRowCol_SortedList_FrmShpFile = sorted(ClimGrid1DShp.PxlRowCol.values.tolist())
    PxlRowCol_SortedArr_FrmShpFile = np.array(PxlRowCol_SortedList_FrmShpFile)
    PxlRow_SortedArr_FrmShpFile = (np.around(PxlRowCol_SortedArr_FrmShpFile // 10000)).astype(int)
    PxlCol_SortedArr_FrmShpFile = (np.around(PxlRowCol_SortedArr_FrmShpFile % 10000)).astype(int)
    del ClimGrid1DShp 
    del PxlRowCol_SortedList_FrmShpFile 
    del PxlRowCol_SortedArr_FrmShpFile 

    ThisPxlRow = PxlRow_SortedArr_FrmShpFile[Which_1D_Pixel]
    ThisPxlCol = PxlCol_SortedArr_FrmShpFile[Which_1D_Pixel]

    SingleUnifiedDatas = {}

    SingleUnifiedData_USDM = np.load(SingleUnifiedDataFilename_USDM)
    SingleUnifiedDatas['XYData_USDM'] = SingleUnifiedData_USDM
    del SingleUnifiedData_USDM

    # #if ( ('Z_index' in InpLayersCombination) or
    # #       ('Z_index_60_month' in InpLayersCombination) or
    # #       ('CPC_soil_moisture' in InpLayersCombination) ):
    # SingleUnifiedData = np.load(SingleUnifiedDataFilename)
    # SingleUnifiedDatas['XYData'] = SingleUnifiedData
    # #end of if ( ('Z_index' in InpLayersCombination) or....
    #
    # if ( ('PMDI' in InpLayersCombination) or
    #           ('PHDI' in InpLayersCombination) ):
    #  SingleUnifiedData_OverallPerc = np.load(SingleUnifiedDataFilename_OverallPerc)
    #  SingleUnifiedDatas['XYData_OverallPerc'] = SingleUnifiedData_OverallPerc
    # #end of if ( ('PMDI' in InpLayersCombination) or....
    #
    if ( ('prcp_01_nCG' in InpLayersCombination) or
            ('prcp_02_nCG' in InpLayersCombination) or
            ('prcp_03_nCG' in InpLayersCombination) or
            ('prcp_06_nCG' in InpLayersCombination) or
            ('prcp_09_nCG' in InpLayersCombination) or
            ('prcp_12_nCG' in InpLayersCombination) or
            ('prcp_24_nCG' in InpLayersCombination) or
            ('prcp_36_nCG' in InpLayersCombination) or
            ('prcp_48_nCG' in InpLayersCombination) or
            ('prcp_60_nCG' in InpLayersCombination) or
            ('prcp_72_nCG' in InpLayersCombination) or
            ('SPI_gamma_01_nCG' in InpLayersCombination) or
            ('SPI_gamma_02_nCG' in InpLayersCombination) or
            ('SPI_gamma_03_nCG' in InpLayersCombination) or
            ('SPI_gamma_06_nCG' in InpLayersCombination) or
            ('SPI_gamma_09_nCG' in InpLayersCombination) or
            ('SPI_gamma_12_nCG' in InpLayersCombination) or
            ('SPI_gamma_24_nCG' in InpLayersCombination) or
            ('SPI_gamma_36_nCG' in InpLayersCombination) or
            ('SPI_gamma_48_nCG' in InpLayersCombination) or
            ('SPI_gamma_60_nCG' in InpLayersCombination) or
            ('SPI_gamma_72_nCG' in InpLayersCombination) or
            ('SPEI_pear_01_nCG' in InpLayersCombination) or
            ('SPEI_pear_02_nCG' in InpLayersCombination) or
            ('SPEI_pear_03_nCG' in InpLayersCombination) or
            ('SPEI_pear_06_nCG' in InpLayersCombination) or
            ('SPEI_pear_09_nCG' in InpLayersCombination) or
            ('SPEI_pear_12_nCG' in InpLayersCombination) or
            ('SPEI_pear_24_nCG' in InpLayersCombination) or
            ('SPEI_pear_36_nCG' in InpLayersCombination) or
            ('SPEI_pear_48_nCG' in InpLayersCombination) or
            ('SPEI_pear_60_nCG' in InpLayersCombination) or
            ('SPEI_pear_72_nCG' in InpLayersCombination) or
            ('tavg_01_nCG' in InpLayersCombination) or
            ('tmax_01_nCG' in InpLayersCombination) ):
        SingleUnifiedData_AllnCG = np.load(SingleUnifiedDataFilename_AllnCG)
        SingleUnifiedDatas['XYData_AllnCG'] = SingleUnifiedData_AllnCG
        del SingleUnifiedData_AllnCG
    #end of if ( ('prcp_01_nCG' in InpLayersCombination) or...

    if ('GRACE_DA_gw' in InpLayersCombination):
        SingleUnifiedData_GRACEDA = np.load(SingleUnifiedDataFilename_GRACEDA)
        SingleUnifiedDatas['XYData_GRACEDA'] = SingleUnifiedData_GRACEDA
    #end of if ('GRACE_DA_gw' in InpLayersCombination)

    if ( ('GRACE_DA_sfsm' in InpLayersCombination) or
            ('GRACE_DA_rtzsm' in InpLayersCombination) ):
        SingleUnifiedData_GRACEDA_MonthlyPerc = np.load(SingleUnifiedDataFilename_GRACEDA_MonthlyPerc)
        SingleUnifiedDatas['XYData_GRACEDA_MonthlyPerc'] = SingleUnifiedData_GRACEDA_MonthlyPerc
    #end of if ( ('GRACE_DA_sfsm' in InpLayersCombination) or...

    if ('EDDI_1wk' in InpLayersCombination):
        SingleUnifiedData_EDDI1wk_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI1wk_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI1wk_MonthlyPerc'] = SingleUnifiedData_EDDI1wk_MonthlyPerc
        del SingleUnifiedData_EDDI1wk_MonthlyPerc
    #end of if ('EDDI_1wk' in InpLayersCombination)

    if ('EDDI_2wk' in InpLayersCombination):
        SingleUnifiedData_EDDI2wk_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI2wk_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI2wk_MonthlyPerc'] = SingleUnifiedData_EDDI2wk_MonthlyPerc
        del SingleUnifiedData_EDDI2wk_MonthlyPerc
    #end of if ('EDDI_2wk' in InpLayersCombination)

    if ('EDDI_3wk' in InpLayersCombination):
        SingleUnifiedData_EDDI3wk_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI3wk_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI3wk_MonthlyPerc'] = SingleUnifiedData_EDDI3wk_MonthlyPerc
        del SingleUnifiedData_EDDI3wk_MonthlyPerc
    #end of if ('EDDI_3wk' in InpLayersCombination)

    if ('EDDI_4wk' in InpLayersCombination):
        SingleUnifiedData_EDDI4wk_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI4wk_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI4wk_MonthlyPerc'] = SingleUnifiedData_EDDI4wk_MonthlyPerc
        del SingleUnifiedData_EDDI4wk_MonthlyPerc
    #end of if ('EDDI_4wk' in InpLayersCombination)

    if ('EDDI_5wk' in InpLayersCombination):
        SingleUnifiedData_EDDI5wk_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI5wk_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI5wk_MonthlyPerc'] = SingleUnifiedData_EDDI5wk_MonthlyPerc
        del SingleUnifiedData_EDDI5wk_MonthlyPerc
    #end of if ('EDDI_5wk' in InpLayersCombination)

    if ('EDDI_6wk' in InpLayersCombination):
        SingleUnifiedData_EDDI6wk_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI6wk_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI6wk_MonthlyPerc'] = SingleUnifiedData_EDDI6wk_MonthlyPerc
        del SingleUnifiedData_EDDI6wk_MonthlyPerc
    #end of if ('EDDI_6wk' in InpLayersCombination)

    if ('EDDI_7wk' in InpLayersCombination):
        SingleUnifiedData_EDDI7wk_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI7wk_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI7wk_MonthlyPerc'] = SingleUnifiedData_EDDI7wk_MonthlyPerc
        del SingleUnifiedData_EDDI7wk_MonthlyPerc
    #end of if ('EDDI_7wk' in InpLayersCombination)

    if ('EDDI_8wk' in InpLayersCombination):
        SingleUnifiedData_EDDI8wk_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI8wk_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI8wk_MonthlyPerc'] = SingleUnifiedData_EDDI8wk_MonthlyPerc
        del SingleUnifiedData_EDDI8wk_MonthlyPerc
    #end of if ('EDDI_8wk' in InpLayersCombination)

    if ('EDDI_9wk' in InpLayersCombination):
        SingleUnifiedData_EDDI9wk_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI9wk_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI9wk_MonthlyPerc'] = SingleUnifiedData_EDDI9wk_MonthlyPerc
        del SingleUnifiedData_EDDI9wk_MonthlyPerc
    #end of if ('EDDI_9wk' in InpLayersCombination)

    if ('EDDI_10wk' in InpLayersCombination):
        SingleUnifiedData_EDDI10wk_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI10wk_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI10wk_MonthlyPerc'] = SingleUnifiedData_EDDI10wk_MonthlyPerc
        del SingleUnifiedData_EDDI10wk_MonthlyPerc
    #end of if ('EDDI_10wk' in InpLayersCombination)

    if ('EDDI_11wk' in InpLayersCombination):
        SingleUnifiedData_EDDI11wk_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI11wk_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI11wk_MonthlyPerc'] = SingleUnifiedData_EDDI11wk_MonthlyPerc
        del SingleUnifiedData_EDDI11wk_MonthlyPerc
    #end of if ('EDDI_11wk' in InpLayersCombination)

    if ('EDDI_12wk' in InpLayersCombination):
        SingleUnifiedData_EDDI12wk_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI12wk_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI12wk_MonthlyPerc'] = SingleUnifiedData_EDDI12wk_MonthlyPerc
        del SingleUnifiedData_EDDI12wk_MonthlyPerc
    #end of if ('EDDI_12wk' in InpLayersCombination)

    if ('EDDI_1mn' in InpLayersCombination):
        SingleUnifiedData_EDDI1mn_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI1mn_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI1mn_MonthlyPerc'] = SingleUnifiedData_EDDI1mn_MonthlyPerc
        del SingleUnifiedData_EDDI1mn_MonthlyPerc
    #end of if ('EDDI_1mn' in InpLayersCombination)

    if ('EDDI_2mn' in InpLayersCombination):
        SingleUnifiedData_EDDI2mn_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI2mn_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI2mn_MonthlyPerc'] = SingleUnifiedData_EDDI2mn_MonthlyPerc
        del SingleUnifiedData_EDDI2mn_MonthlyPerc
    #end of if ('EDDI_2mn' in InpLayersCombination)

    if ('EDDI_3mn' in InpLayersCombination):
        SingleUnifiedData_EDDI3mn_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI3mn_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI3mn_MonthlyPerc'] = SingleUnifiedData_EDDI3mn_MonthlyPerc
        del SingleUnifiedData_EDDI3mn_MonthlyPerc
    #end of if ('EDDI_3mn' in InpLayersCombination)

    if ('EDDI_4mn' in InpLayersCombination):
        SingleUnifiedData_EDDI4mn_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI4mn_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI4mn_MonthlyPerc'] = SingleUnifiedData_EDDI4mn_MonthlyPerc
        del SingleUnifiedData_EDDI4mn_MonthlyPerc
    #end of if ('EDDI_4mn' in InpLayersCombination)

    if ('EDDI_5mn' in InpLayersCombination):
        SingleUnifiedData_EDDI5mn_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI5mn_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI5mn_MonthlyPerc'] = SingleUnifiedData_EDDI5mn_MonthlyPerc
        del SingleUnifiedData_EDDI5mn_MonthlyPerc
    #end of if ('EDDI_5mn' in InpLayersCombination)

    if ('EDDI_6mn' in InpLayersCombination):
        SingleUnifiedData_EDDI6mn_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI6mn_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI6mn_MonthlyPerc'] = SingleUnifiedData_EDDI6mn_MonthlyPerc
        del SingleUnifiedData_EDDI6mn_MonthlyPerc
    #end of if ('EDDI_6mn' in InpLayersCombination)

    if ('EDDI_7mn' in InpLayersCombination):
        SingleUnifiedData_EDDI7mn_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI7mn_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI7mn_MonthlyPerc'] = SingleUnifiedData_EDDI7mn_MonthlyPerc
        del SingleUnifiedData_EDDI7mn_MonthlyPerc
    #end of if ('EDDI_7mn' in InpLayersCombination)

    if ('EDDI_8mn' in InpLayersCombination):
        SingleUnifiedData_EDDI8mn_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI8mn_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI8mn_MonthlyPerc'] = SingleUnifiedData_EDDI8mn_MonthlyPerc
        del SingleUnifiedData_EDDI8mn_MonthlyPerc
    #end of if ('EDDI_8mn' in InpLayersCombination)

    if ('EDDI_9mn' in InpLayersCombination):
        SingleUnifiedData_EDDI9mn_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI9mn_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI9mn_MonthlyPerc'] = SingleUnifiedData_EDDI9mn_MonthlyPerc
        del SingleUnifiedData_EDDI9mn_MonthlyPerc
    #end of if ('EDDI_9mn' in InpLayersCombination)

    if ('EDDI_10mn' in InpLayersCombination):
        SingleUnifiedData_EDDI10mn_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI10mn_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI10mn_MonthlyPerc'] = SingleUnifiedData_EDDI10mn_MonthlyPerc
        del SingleUnifiedData_EDDI10mn_MonthlyPerc
    #end of if ('EDDI_10mn' in InpLayersCombination)

    if ('EDDI_11mn' in InpLayersCombination):
        SingleUnifiedData_EDDI11mn_MonthlyPerc = np.load(SingleUnifiedDataFilename_EDDI11mn_MonthlyPerc)
        SingleUnifiedDatas['XYData_EDDI11mn_MonthlyPerc'] = SingleUnifiedData_EDDI11mn_MonthlyPerc
        del SingleUnifiedData_EDDI11mn_MonthlyPerc
    #end of if ('EDDI_11mn' in InpLayersCombination)

    if ('EDDI_12mn' in InpLayersCombination):
        SingleUnifiedData_EDDI12mn = np.load(SingleUnifiedDataFilename_EDDI12mn)
        SingleUnifiedDatas['XYData_EDDI12mn'] = SingleUnifiedData_EDDI12mn
        del SingleUnifiedData_EDDI12mn
    #end of if ('EDDI_12mn' in InpLayersCombination)

    if ( ('NLDAS2D_1MSM_Mosaic' in InpLayersCombination) or
            ('NLDAS2D_1MSM_Noah' in InpLayersCombination) or
            ('NLDAS2D_1MSM_SAC' in InpLayersCombination) or
            ('NLDAS2D_1MSM_VIC' in InpLayersCombination) or
            ('NLDAS2D_TCSM_Mosaic' in InpLayersCombination) or
            ('NLDAS2D_TCSM_Noah' in InpLayersCombination) or
            ('NLDAS2D_TCSM_SAC' in InpLayersCombination) or
            ('NLDAS2D_TCSM_VIC' in InpLayersCombination) or
            ('NLDAS2D_EVAP_Mosaic' in InpLayersCombination) or
            ('NLDAS2D_EVAP_Noah' in InpLayersCombination) or
            ('NLDAS2D_EVAP_SAC' in InpLayersCombination) or
            ('NLDAS2D_EVAP_VIC' in InpLayersCombination) or
            ('NLDAS2D_SWE_Mosaic' in InpLayersCombination) or
            ('NLDAS2D_SWE_Noah' in InpLayersCombination) or
            ('NLDAS2D_SWE_SAC' in InpLayersCombination) or
            ('NLDAS2D_SWE_VIC' in InpLayersCombination) or
            ('NLDAS2D_RUN_Mosaic' in InpLayersCombination) or
            ('NLDAS2D_RUN_Noah' in InpLayersCombination) or
            ('NLDAS2D_RUN_SAC' in InpLayersCombination) or
            ('NLDAS2D_RUN_VIC' in InpLayersCombination) or
            ('NLDAS2D_STRMH04_Mosaic' in InpLayersCombination) or
            ('NLDAS2D_STRMH04_Noah' in InpLayersCombination) or
            ('NLDAS2D_STRMH04_SAC' in InpLayersCombination) or
            ('NLDAS2D_STRMH04_VIC' in InpLayersCombination) ):
        SingleUnifiedData_NLDAS_2_daily = np.load(SingleUnifiedDataFilename_NLDAS_2_daily)
        SingleUnifiedDatas['XYData_NLDAS_2_daily'] = SingleUnifiedData_NLDAS_2_daily
        del SingleUnifiedData_NLDAS_2_daily
    #end of if ( ('NLDAS2D_1MSM_Mosaic' in InpLayersCombination) or...

    #if ('VegDRI' in InpLayersCombination):
    #  SingleUnifiedData_VegDRI_MonthlyPerc = np.load(SingleUnifiedDataFilename_VegDRI_MonthlyPerc)
    #  SingleUnifiedDatas['XYData_VegDRI_MonthlyPerc'] = SingleUnifiedData_VegDRI_MonthlyPerc
    ##end of if ('VegDRI' in InpLayersCombination)
    #
    #if ('QuickDRI' in InpLayersCombination):
    #  SingleUnifiedData_QuickDRI_MonthlyPerc = np.load(SingleUnifiedDataFilename_QuickDRI_MonthlyPerc)
    #  SingleUnifiedDatas['XYData_QuickDRI_MonthlyPerc'] = SingleUnifiedData_QuickDRI_MonthlyPerc
    ##end of if ('QuickDRI' in InpLayersCombination)
    #
    #if ( ('ESI_4wk' in InpLayersCombination) or
    #           ('ESI_12wk' in InpLayersCombination) ):
    #  SingleUnifiedData_ESImultiWeek_MonthlyPerc = np.load(SingleUnifiedDataFilename_ESImultiWeek_MonthlyPerc)
    #  SingleUnifiedDatas['XYData_ESImultiWeek_MonthlyPerc'] = SingleUnifiedData_ESImultiWeek_MonthlyPerc
    ##end of if ('ESI' in InpLayersCombination)
    #
    #if ( ('SNODAS' in InpLayersCombination) or
    #           ('ESA_CCI' in InpLayersCombination) ):
    #  SingleUnifiedData_SNODASnESACCI = np.load(SingleUnifiedDataFilename_SNODASnESACCI)
    #  SingleUnifiedDatas['XYData_SNODASnESACCI'] = SingleUnifiedData_SNODASnESACCI
    ##end of if ( ('SNODAS' in InpLayersCombination) or...

    if ( 'SNODAS' in InpLayersCombination ): 
        SingleUnifiedData_SNODAS = np.load(SingleUnifiedDataFilename_SNODAS)
        SingleUnifiedDatas['XYData_SNODAS'] = SingleUnifiedData_SNODAS
    #end of if ( 'SNODAS' in InpLayersCombination )

    if ('IMERG_01' in InpLayersCombination):
        SingleUnifiedData_IMERG_01 = np.load(SingleUnifiedDataFilename_IMERG_01)
        SingleUnifiedDatas['XYData_IMERG_01'] = SingleUnifiedData_IMERG_01
    #end of if ('IMERG_01' in InpLayersCombination)
    if ('IMERG_02' in InpLayersCombination):
        SingleUnifiedData_IMERG_02 = np.load(SingleUnifiedDataFilename_IMERG_02)
        SingleUnifiedDatas['XYData_IMERG_02'] = SingleUnifiedData_IMERG_02
    #end of if ('IMERG_02' in InpLayersCombination)
    if ('IMERG_03' in InpLayersCombination):
        SingleUnifiedData_IMERG_03 = np.load(SingleUnifiedDataFilename_IMERG_03)
        SingleUnifiedDatas['XYData_IMERG_03'] = SingleUnifiedData_IMERG_03
    #end of if ('IMERG_03' in InpLayersCombination)
    if ('IMERG_06' in InpLayersCombination):
        SingleUnifiedData_IMERG_06 = np.load(SingleUnifiedDataFilename_IMERG_06)
        SingleUnifiedDatas['XYData_IMERG_06'] = SingleUnifiedData_IMERG_06
    #end of if ('IMERG_06' in InpLayersCombination)
    if ('IMERG_09' in InpLayersCombination):
        SingleUnifiedData_IMERG_09 = np.load(SingleUnifiedDataFilename_IMERG_09)
        SingleUnifiedDatas['XYData_IMERG_09'] = SingleUnifiedData_IMERG_09
    #end of if ('IMERG_09' in InpLayersCombination)
    if ('IMERG_12' in InpLayersCombination):
        SingleUnifiedData_IMERG_12 = np.load(SingleUnifiedDataFilename_IMERG_12)
        SingleUnifiedDatas['XYData_IMERG_12'] = SingleUnifiedData_IMERG_12
    #end of if ('IMERG_12' in InpLayersCombination)
    if ('IMERG_24' in InpLayersCombination):
        SingleUnifiedData_IMERG_24 = np.load(SingleUnifiedDataFilename_IMERG_24)
        SingleUnifiedDatas['XYData_IMERG_24'] = SingleUnifiedData_IMERG_24
    #end of if ('IMERG_24' in InpLayersCombination)
    if ('IMERG_36' in InpLayersCombination):
        SingleUnifiedData_IMERG_36 = np.load(SingleUnifiedDataFilename_IMERG_36)
        SingleUnifiedDatas['XYData_IMERG_36'] = SingleUnifiedData_IMERG_36
    #end of if ('IMERG_36' in InpLayersCombination)
    if ('IMERG_48' in InpLayersCombination):
        SingleUnifiedData_IMERG_48 = np.load(SingleUnifiedDataFilename_IMERG_48)
        SingleUnifiedDatas['XYData_IMERG_48'] = SingleUnifiedData_IMERG_48
    #end of if ('IMERG_48' in InpLayersCombination)
    if ('IMERG_60' in InpLayersCombination):
        SingleUnifiedData_IMERG_60 = np.load(SingleUnifiedDataFilename_IMERG_60)
        SingleUnifiedDatas['XYData_IMERG_60'] = SingleUnifiedData_IMERG_60
    #end of if ('IMERG_60' in InpLayersCombination)
    if ('IMERG_72' in InpLayersCombination):
        SingleUnifiedData_IMERG_72 = np.load(SingleUnifiedDataFilename_IMERG_72)
        SingleUnifiedDatas['XYData_IMERG_72'] = SingleUnifiedData_IMERG_72
    #end of if ('IMERG_72' in InpLayersCombination)

    if ( ('SmNDVI_BlendedVHP' in InpLayersCombination) or
            ('TCI_BlendedVHP' in InpLayersCombination) or
            ('VCI_BlendedVHP' in InpLayersCombination) or
            ('VHI_BlendedVHP' in InpLayersCombination) ):
        SingleUnifiedData_BlendedVHP_MonthlyPerc = np.load(SingleUnifiedDataFilename_BlendedVHP_MonthlyPerc)
        SingleUnifiedDatas['XYData_BlendedVHP_MonthlyPerc'] = SingleUnifiedData_BlendedVHP_MonthlyPerc
    #end of if ('SmNDVI_BlendedVHP' in InpLayersCombination) or...

    #if ('GlobSnow3' in InpLayersCombination):
    #  SingleUnifiedData_GlobSnow3_OverallPerc = np.load(SingleUnifiedDataFilename_GlobSnow3_OverallPerc)
    #  SingleUnifiedDatas['XYData_GlobSnow3_OverallPerc'] = SingleUnifiedData_GlobSnow3_OverallPerc
    ##end of if ('GlobSnow3' in InpLayersCombination)

    def GetInpAndTargArraysFromFile_ClmGrd1D(XYDatas, InpLayersCombination, IfMakeTargetBinary, IfIncludeD0AsDrought, WhichSeason, MinimumWindowSize, MaximumWindowSize, MinSamplesForFracI, ThisPxlRow, ThisPxlCol, PxlRow_SortedArr_FrmShpFile, PxlCol_SortedArr_FrmShpFile):

    #  print("In GetInpAndTargArraysFromFile_ClmGrd1D, InpLayersCombination is ", InpLayersCombination)

        XYData_USDM = XYDatas['XYData_USDM']

    ##if ( ('Z_index' in InpLayersCombination) or
    ##       ('Z_index_60_month' in InpLayersCombination) or
    ##       ('CPC_soil_moisture' in InpLayersCombination) ):
    #  XYData = XYDatas['XYData']
    ##end of if ( ('PMDI' in InpLayersCombination) or....
    #
    #  if ( ('PMDI' in InpLayersCombination) or
    #               ('PHDI' in InpLayersCombination) ):
    #        XYData_OverallPerc = XYDatas['XYData_OverallPerc']
    #  #end of if ( ('PMDI' in InpLayersCombination) or....

        if ( ('prcp_01_nCG' in InpLayersCombination) or
                ('prcp_02_nCG' in InpLayersCombination) or
                ('prcp_03_nCG' in InpLayersCombination) or
                ('prcp_06_nCG' in InpLayersCombination) or
                ('prcp_09_nCG' in InpLayersCombination) or
                ('prcp_12_nCG' in InpLayersCombination) or
                ('prcp_24_nCG' in InpLayersCombination) or
                ('prcp_36_nCG' in InpLayersCombination) or
                ('prcp_48_nCG' in InpLayersCombination) or
                ('prcp_60_nCG' in InpLayersCombination) or
                ('prcp_72_nCG' in InpLayersCombination) or
                ('SPI_gamma_01_nCG' in InpLayersCombination) or
                ('SPI_gamma_02_nCG' in InpLayersCombination) or
                ('SPI_gamma_03_nCG' in InpLayersCombination) or
                ('SPI_gamma_06_nCG' in InpLayersCombination) or
                ('SPI_gamma_09_nCG' in InpLayersCombination) or
                ('SPI_gamma_12_nCG' in InpLayersCombination) or
                ('SPI_gamma_24_nCG' in InpLayersCombination) or
                ('SPI_gamma_36_nCG' in InpLayersCombination) or
                ('SPI_gamma_48_nCG' in InpLayersCombination) or
                ('SPI_gamma_60_nCG' in InpLayersCombination) or
                ('SPI_gamma_72_nCG' in InpLayersCombination) or
                ('SPEI_pear_01_nCG' in InpLayersCombination) or
                ('SPEI_pear_02_nCG' in InpLayersCombination) or
                ('SPEI_pear_03_nCG' in InpLayersCombination) or
                ('SPEI_pear_06_nCG' in InpLayersCombination) or
                ('SPEI_pear_09_nCG' in InpLayersCombination) or
                ('SPEI_pear_12_nCG' in InpLayersCombination) or
                ('SPEI_pear_24_nCG' in InpLayersCombination) or
                ('SPEI_pear_36_nCG' in InpLayersCombination) or
                ('SPEI_pear_48_nCG' in InpLayersCombination) or
                ('SPEI_pear_60_nCG' in InpLayersCombination) or
                ('SPEI_pear_72_nCG' in InpLayersCombination) or
                ('tavg_01_nCG' in InpLayersCombination) or
                ('tmax_01_nCG' in InpLayersCombination) ):
            XYData_AllnCG = XYDatas['XYData_AllnCG']
        #end of if ( ('prcp_01_nCG' in InpLayersCombination) or...

        if ('GRACE_DA_gw' in InpLayersCombination):
            XYData_GRACEDA = XYDatas['XYData_GRACEDA']
        #end of if ('GRACE_DA_gw' in InpLayersCombination)

        if ( ('GRACE_DA_sfsm' in InpLayersCombination) or
                ('GRACE_DA_rtzsm' in InpLayersCombination) ):
            XYData_GRACEDA_MonthlyPerc = XYDatas['XYData_GRACEDA_MonthlyPerc']
        #end of if ( ('GRACE_DA_sfsm' in InpLayersCombination) or...
    
        if ('EDDI_1wk' in InpLayersCombination):
            XYData_EDDI1wk_MonthlyPerc = XYDatas['XYData_EDDI1wk_MonthlyPerc']
        #end of if ('EDDI_1wk' in InpLayersCombination)

        if ('EDDI_2wk' in InpLayersCombination):
            XYData_EDDI2wk_MonthlyPerc = XYDatas['XYData_EDDI2wk_MonthlyPerc']
        #end of if ('EDDI_2wk' in InpLayersCombination)

        if ('EDDI_3wk' in InpLayersCombination):
            XYData_EDDI3wk_MonthlyPerc = XYDatas['XYData_EDDI3wk_MonthlyPerc']
        #end of if ('EDDI_3wk' in InpLayersCombination)

        if ('EDDI_4wk' in InpLayersCombination):
            XYData_EDDI4wk_MonthlyPerc = XYDatas['XYData_EDDI4wk_MonthlyPerc']
        #end of if ('EDDI_4wk' in InpLayersCombination)

        if ('EDDI_5wk' in InpLayersCombination):
            XYData_EDDI5wk_MonthlyPerc = XYDatas['XYData_EDDI5wk_MonthlyPerc']
        #end of if ('EDDI_5wk' in InpLayersCombination)

        if ('EDDI_6wk' in InpLayersCombination):
            XYData_EDDI6wk_MonthlyPerc = XYDatas['XYData_EDDI6wk_MonthlyPerc']
        #end of if ('EDDI_6wk' in InpLayersCombination)

        if ('EDDI_7wk' in InpLayersCombination):
            XYData_EDDI7wk_MonthlyPerc = XYDatas['XYData_EDDI7wk_MonthlyPerc']
        #end of if ('EDDI_7wk' in InpLayersCombination)

        if ('EDDI_8wk' in InpLayersCombination):
            XYData_EDDI8wk_MonthlyPerc = XYDatas['XYData_EDDI8wk_MonthlyPerc']
        #end of if ('EDDI_8wk' in InpLayersCombination)

        if ('EDDI_9wk' in InpLayersCombination):
            XYData_EDDI9wk_MonthlyPerc = XYDatas['XYData_EDDI9wk_MonthlyPerc']
        #end of if ('EDDI_9wk' in InpLayersCombination)

        if ('EDDI_10wk' in InpLayersCombination):
            XYData_EDDI10wk_MonthlyPerc = XYDatas['XYData_EDDI10wk_MonthlyPerc']
        #end of if ('EDDI_10wk' in InpLayersCombination)

        if ('EDDI_11wk' in InpLayersCombination):
            XYData_EDDI11wk_MonthlyPerc = XYDatas['XYData_EDDI11wk_MonthlyPerc']
        #end of if ('EDDI_11wk' in InpLayersCombination)

        if ('EDDI_12wk' in InpLayersCombination):
            XYData_EDDI12wk_MonthlyPerc = XYDatas['XYData_EDDI12wk_MonthlyPerc']
        #end of if ('EDDI_12wk' in InpLayersCombination)

        if ('EDDI_1mn' in InpLayersCombination):
            XYData_EDDI1mn_MonthlyPerc = XYDatas['XYData_EDDI1mn_MonthlyPerc']
        #end of if ('EDDI_1mn' in InpLayersCombination)

        if ('EDDI_2mn' in InpLayersCombination):
            XYData_EDDI2mn_MonthlyPerc = XYDatas['XYData_EDDI2mn_MonthlyPerc']
        #end of if ('EDDI_2mn' in InpLayersCombination)

        if ('EDDI_3mn' in InpLayersCombination):
            XYData_EDDI3mn_MonthlyPerc = XYDatas['XYData_EDDI3mn_MonthlyPerc']
        #end of if ('EDDI_3mn' in InpLayersCombination)

        if ('EDDI_4mn' in InpLayersCombination):
            XYData_EDDI4mn_MonthlyPerc = XYDatas['XYData_EDDI4mn_MonthlyPerc']
        #end of if ('EDDI_4mn' in InpLayersCombination)

        if ('EDDI_5mn' in InpLayersCombination):
            XYData_EDDI5mn_MonthlyPerc = XYDatas['XYData_EDDI5mn_MonthlyPerc']
        #end of if ('EDDI_5mn' in InpLayersCombination)

        if ('EDDI_6mn' in InpLayersCombination):
            XYData_EDDI6mn_MonthlyPerc = XYDatas['XYData_EDDI6mn_MonthlyPerc']
        #end of if ('EDDI_6mn' in InpLayersCombination)

        if ('EDDI_7mn' in InpLayersCombination):
            XYData_EDDI7mn_MonthlyPerc = XYDatas['XYData_EDDI7mn_MonthlyPerc']
        #end of if ('EDDI_7mn' in InpLayersCombination)

        if ('EDDI_8mn' in InpLayersCombination):
            XYData_EDDI8mn_MonthlyPerc = XYDatas['XYData_EDDI8mn_MonthlyPerc']
        #end of if ('EDDI_8mn' in InpLayersCombination)

        if ('EDDI_9mn' in InpLayersCombination):
            XYData_EDDI9mn_MonthlyPerc = XYDatas['XYData_EDDI9mn_MonthlyPerc']
        #end of if ('EDDI_9mn' in InpLayersCombination)

        if ('EDDI_10mn' in InpLayersCombination):
            XYData_EDDI10mn_MonthlyPerc = XYDatas['XYData_EDDI10mn_MonthlyPerc']
        #end of if ('EDDI_10mn' in InpLayersCombination)

        if ('EDDI_11mn' in InpLayersCombination):
            XYData_EDDI11mn_MonthlyPerc = XYDatas['XYData_EDDI11mn_MonthlyPerc']
        #end of if ('EDDI_11mn' in InpLayersCombination)

        if ('EDDI_12mn' in InpLayersCombination):
            XYData_EDDI12mn = XYDatas['XYData_EDDI12mn']
        #end of if ('EDDI_12mn' in InpLayersCombination)

        if ( ('NLDAS2D_1MSM_Mosaic' in InpLayersCombination) or
                ('NLDAS2D_1MSM_Noah' in InpLayersCombination) or
                ('NLDAS2D_1MSM_SAC' in InpLayersCombination) or
                ('NLDAS2D_1MSM_VIC' in InpLayersCombination) or
                ('NLDAS2D_TCSM_Mosaic' in InpLayersCombination) or
                ('NLDAS2D_TCSM_Noah' in InpLayersCombination) or
                ('NLDAS2D_TCSM_SAC' in InpLayersCombination) or
                ('NLDAS2D_TCSM_VIC' in InpLayersCombination) or
                ('NLDAS2D_EVAP_Mosaic' in InpLayersCombination) or
                ('NLDAS2D_EVAP_Noah' in InpLayersCombination) or
                ('NLDAS2D_EVAP_SAC' in InpLayersCombination) or
                ('NLDAS2D_EVAP_VIC' in InpLayersCombination) or
                ('NLDAS2D_SWE_Mosaic' in InpLayersCombination) or
                ('NLDAS2D_SWE_Noah' in InpLayersCombination) or
                ('NLDAS2D_SWE_SAC' in InpLayersCombination) or
                ('NLDAS2D_SWE_VIC' in InpLayersCombination) or
                ('NLDAS2D_RUN_Mosaic' in InpLayersCombination) or
                ('NLDAS2D_RUN_Noah' in InpLayersCombination) or
                ('NLDAS2D_RUN_SAC' in InpLayersCombination) or
                ('NLDAS2D_RUN_VIC' in InpLayersCombination) or
                ('NLDAS2D_STRMH04_Mosaic' in InpLayersCombination) or
                ('NLDAS2D_STRMH04_Noah' in InpLayersCombination) or
                ('NLDAS2D_STRMH04_SAC' in InpLayersCombination) or
                ('NLDAS2D_STRMH04_VIC' in InpLayersCombination) ):
                XYData_NLDAS_2_daily = XYDatas['XYData_NLDAS_2_daily']
        #end of if ( ('NLDAS2D_1MSM_Mosaic' in InpLayersCombination) or...

    #  if ('VegDRI' in InpLayersCombination):
    #        XYData_VegDRI_MonthlyPerc = XYDatas['XYData_VegDRI_MonthlyPerc']
    #  #end of if ('VegDRI' in InpLayersCombination)
    #  
    #  if ('QuickDRI' in InpLayersCombination):
    #        XYData_QuickDRI_MonthlyPerc = XYDatas['XYData_QuickDRI_MonthlyPerc']
    #  #end of if ('QuickDRI' in InpLayersCombination)
    #  
    #  if ( ('ESI_4wk' in InpLayersCombination) or
    #               ('ESI_12wk' in InpLayersCombination) ):
    #        XYData_ESImultiWeek_MonthlyPerc = XYDatas['XYData_ESImultiWeek_MonthlyPerc']
    #  #end of if ('ESI_4wk' in InpLayersCombination)
    #  
    #  if ( ('SNODAS' in InpLayersCombination) or
    #               ('ESA_CCI' in InpLayersCombination) ):
    #        XYData_SNODASnESACCI = XYDatas['XYData_SNODASnESACCI']
    #  #end of if ( ('SNODAS' in InpLayersCombination) or...

        if ('SNODAS' in InpLayersCombination):
            XYData_SNODAS = XYDatas['XYData_SNODAS']
        #end of if ('SNODAS' in InpLayersCombination)

        if ('IMERG_01' in InpLayersCombination):
            XYData_IMERG_01 = XYDatas['XYData_IMERG_01']
        #end of if ('IMERG_01' in InpLayersCombination)
        if ('IMERG_02' in InpLayersCombination):
            XYData_IMERG_02 = XYDatas['XYData_IMERG_02']
        #end of if ('IMERG_02' in InpLayersCombination)
        if ('IMERG_03' in InpLayersCombination):
            XYData_IMERG_03 = XYDatas['XYData_IMERG_03']
        #end of if ('IMERG_03' in InpLayersCombination)
        if ('IMERG_06' in InpLayersCombination):
            XYData_IMERG_06 = XYDatas['XYData_IMERG_06']
        #end of if ('IMERG_06' in InpLayersCombination)
        if ('IMERG_09' in InpLayersCombination):
            XYData_IMERG_09 = XYDatas['XYData_IMERG_09']
        #end of if ('IMERG_09' in InpLayersCombination)
        if ('IMERG_12' in InpLayersCombination):
            XYData_IMERG_12 = XYDatas['XYData_IMERG_12']
        #end of if ('IMERG_12' in InpLayersCombination)
        if ('IMERG_24' in InpLayersCombination):
            XYData_IMERG_24 = XYDatas['XYData_IMERG_24']
        #end of if ('IMERG_24' in InpLayersCombination)
        if ('IMERG_36' in InpLayersCombination):
            XYData_IMERG_36 = XYDatas['XYData_IMERG_36']
        #end of if ('IMERG_36' in InpLayersCombination)
        if ('IMERG_48' in InpLayersCombination):
            XYData_IMERG_48 = XYDatas['XYData_IMERG_48']
        #end of if ('IMERG_48' in InpLayersCombination)
        if ('IMERG_60' in InpLayersCombination):
            XYData_IMERG_60 = XYDatas['XYData_IMERG_60']
        #end of if ('IMERG_60' in InpLayersCombination)
        if ('IMERG_72' in InpLayersCombination):
            XYData_IMERG_72 = XYDatas['XYData_IMERG_72']
        #end of if ('IMERG_72' in InpLayersCombination)

        if ( ('SmNDVI_BlendedVHP' in InpLayersCombination) or
                ('TCI_BlendedVHP' in InpLayersCombination) or
                ('VCI_BlendedVHP' in InpLayersCombination) or
                ('VHI_BlendedVHP' in InpLayersCombination) ):
            XYData_BlendedVHP_MonthlyPerc = XYDatas['XYData_BlendedVHP_MonthlyPerc']
        #end of if ( ('SmNDVI_BlendedVHP' in InpLayersCombination) or...

    #  if ('GlobSnow3' in InpLayersCombination):
    #        XYData_GlobSnow3_OverallPerc = XYDatas['XYData_GlobSnow3_OverallPerc']
    #  #end of if ('GlobSnow3' in InpLayersCombination)

        YYYYMMDD_Of_Array = XYData_USDM['YYYYMMDD_Of_InfoArray']
        Target_Array = XYData_USDM['InfoArray'] # Target data array

        YYYYMMDD_Of_Array, Target_Array = TimeSliceStrict_YYYYMMDDAndRefArrays(YYYYMMDD_Of_Array, Target_Array, BeginYYYYMMDD, EndYYYYMMDD, 'USDM') # SY: replacing this by the following few lines
    #  # Begin replacement lines
    #  BeginIdx = list(YYYYMMDD_Of_Array).index(BeginYYYYMMDD)
    #  EndIdx = list(YYYYMMDD_Of_Array).index(EndYYYYMMDD)
    #  YYYYMMDD_Of_Array = YYYYMMDD_Of_Array[ BeginIdx : EndIdx+1 ]
    #  Target_Array = Target_Array[ BeginIdx : EndIdx+1 ]
    #  # End replacement lines
    #  print("YYYYMMDD_Of_Array.shape is ", YYYYMMDD_Of_Array.shape)
    #  print("Target_Array.shape is ", Target_Array.shape)

        YYYY_Of_Array = YYYYMMDD_Of_Array // 10000
        MM_Of_Array = (YYYYMMDD_Of_Array - YYYY_Of_Array * 10000) // 100
        del YYYYMMDD_Of_Array
        del YYYY_Of_Array

        if IfMakeTargetBinary == 'Y':

            if IfIncludeD0AsDrought == 'Y':
                DroughtValues_LowerLimit = 0
            else:
                DroughtValues_LowerLimit = 1
            Drought_Idxs = np.where(Target_Array >= DroughtValues_LowerLimit)
            NoDrought_Idxs = np.where(Target_Array < DroughtValues_LowerLimit)
            Target_Array[Drought_Idxs] = 1
            Target_Array[NoDrought_Idxs] = 0
            del Drought_Idxs 
            del NoDrought_Idxs

        else:

            Target_Array = Target_Array + 1 # Since currently it's -1-start for drought categories, not 0-start

        #end of if IfMakeTargetBinary == 'Y':

        def ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD_Arg, EndYYYYMMDD_Arg, VariableArg, XYDataObj, KeyInObj_YYYYMMDD_Of_RefArray, KeyInObj_RefArray):
            This_RefArray = (XYDataObj[KeyInObj_RefArray]).astype('float32')
            This_YYYYMMDD_Of_RefArray = XYDataObj[KeyInObj_YYYYMMDD_Of_RefArray]
            This_YYYYMMDD_Of_RefArray, This_RefArray = TimeSliceStrict_YYYYMMDDAndRefArrays(This_YYYYMMDD_Of_RefArray, This_RefArray, BeginYYYYMMDD_Arg, EndYYYYMMDD_Arg, VariableArg)
            return This_YYYYMMDD_Of_RefArray, This_RefArray
        #end of def ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD_Arg, EndYYYYMMDD_Arg, VariableArg, XYDataObj, KeyInObj_YYYYMMDD_Of_RefArray, KeyInObj_RefArray)
    
        #Begin input percentile arrays
        if 'Z_index' in InpLayersCombination:
    #        YYYYMMDD_Of_Array, ZIndex_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'Z_index', XYData, 'YYYYMMDD_Of_Array', 'ZIndex_PrcntlArray')
            ZIndex_PrcntlArray = np.ones(Target_Array.shape, dtype=np.float32)
        if 'Z_index_60_month' in InpLayersCombination:
    #        YYYYMMDD_Of_Array, ZIndex60month_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'Z_index_60_month', XYData, 'YYYYMMDD_Of_Array', 'ZIndex60month_PrcntlArray')
            ZIndex60month_PrcntlArray = np.ones(Target_Array.shape, dtype=np.float32)
        if 'PMDI' in InpLayersCombination:
    #        YYYYMMDD_Of_Array, PMDI_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'PMDI', XYData_OverallPerc, 'YYYYMMDD_Of_Array', 'PMDI_PrcntlArray')
            PMDI_PrcntlArray = np.ones(Target_Array.shape, dtype=np.float32)
        if 'PHDI' in InpLayersCombination:
    #        YYYYMMDD_Of_Array, PHDI_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'PHDI', XYData_OverallPerc, 'YYYYMMDD_Of_Array', 'PHDI_PrcntlArray')
            PHDI_PrcntlArray = np.ones(Target_Array.shape, dtype=np.float32)
        if 'prcp_01_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, prcp_01_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'prcp_01_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'prcp_02_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, prcp_02_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'prcp_02_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'prcp_03_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, prcp_03_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'prcp_03_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'prcp_06_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, prcp_06_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'prcp_06_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'prcp_09_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, prcp_09_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'prcp_09_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'prcp_12_nCG' in InpLayersCombination: 
            YYYYMMDD_Of_Array, prcp_12_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'prcp_12_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'prcp_24_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, prcp_24_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'prcp_24_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'prcp_36_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, prcp_36_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'prcp_36_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'prcp_48_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, prcp_48_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'prcp_48_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'prcp_60_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, prcp_60_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'prcp_60_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'prcp_72_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, prcp_72_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'prcp_72_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'CPC_soil_moisture' in InpLayersCombination:
    #        YYYYMMDD_Of_Array, CPCsoilmoist_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'CPC_soil_moisture', XYData, 'YYYYMMDD_Of_Array', 'CPCsoilmoist_PrcntlArray')
            CPCsoilmoist_PrcntlArray = np.ones(Target_Array.shape, dtype=np.float32)
        if 'GRACE_DA_gw' in InpLayersCombination:
            YYYYMMDD_Of_Array, GRACE_DA_gw_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'GRACE_DA_gw', XYData_GRACEDA, 'YYYYMMDD_Of_Array', 'GRACEDA_gws_inst_PrcntlArray')
        if 'GRACE_DA_sfsm' in InpLayersCombination:
            YYYYMMDD_Of_Array, GRACE_DA_sfsm_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'GRACE_DA_sfsm', XYData_GRACEDA_MonthlyPerc, 'YYYYMMDD_Of_Array', 'GRACEDA_sfsm_inst_PrcntlArray')
        if 'GRACE_DA_rtzsm' in InpLayersCombination:
            YYYYMMDD_Of_Array, GRACE_DA_rtzsm_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'GRACE_DA_rtzsm', XYData_GRACEDA_MonthlyPerc, 'YYYYMMDD_Of_Array', 'GRACEDA_rtzsm_inst_PrcntlArray')
        if 'EDDI_1wk' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI1wk_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_1wk', XYData_EDDI1wk_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_2wk' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI2wk_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_2wk', XYData_EDDI2wk_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_3wk' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI3wk_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_3wk', XYData_EDDI3wk_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_4wk' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI4wk_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_4wk', XYData_EDDI4wk_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_5wk' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI5wk_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_5wk', XYData_EDDI5wk_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_6wk' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI6wk_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_6wk', XYData_EDDI6wk_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_7wk' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI7wk_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_7wk', XYData_EDDI7wk_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_8wk' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI8wk_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_8wk', XYData_EDDI8wk_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_9wk' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI9wk_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_9wk', XYData_EDDI9wk_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_10wk' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI10wk_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_10wk', XYData_EDDI10wk_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_11wk' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI11wk_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_11wk', XYData_EDDI11wk_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_12wk' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI12wk_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_12wk', XYData_EDDI12wk_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_1mn' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI1mn_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_1mn', XYData_EDDI1mn_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_2mn' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI2mn_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_2mn', XYData_EDDI2mn_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_3mn' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI3mn_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_3mn', XYData_EDDI3mn_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_4mn' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI4mn_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_4mn', XYData_EDDI4mn_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_5mn' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI5mn_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_5mn', XYData_EDDI5mn_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_6mn' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI6mn_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_6mn', XYData_EDDI6mn_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray') 
        if 'EDDI_7mn' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI7mn_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_7mn', XYData_EDDI7mn_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_8mn' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI8mn_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_8mn', XYData_EDDI8mn_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_9mn' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI9mn_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_9mn', XYData_EDDI9mn_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_10mn' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI10mn_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_10mn', XYData_EDDI10mn_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_11mn' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI11mn_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_11mn', XYData_EDDI11mn_MonthlyPerc, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'EDDI_12mn' in InpLayersCombination:
            YYYYMMDD_Of_Array, EDDI12mn_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'EDDI_12mn', XYData_EDDI12mn, 'YYYYMMDD_Of_Array', 'EDDI_PrcntlArray')
        if 'NLDAS2D_1MSM_Mosaic' in InpLayersCombination:
            YYYYMMDD_Of_Array, Mosaic_1MSM_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_1MSM_Mosaic', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_1MSM_Noah' in InpLayersCombination:
            YYYYMMDD_Of_Array, Noah_1MSM_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_1MSM_Noah', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_1MSM_SAC' in InpLayersCombination:
            YYYYMMDD_Of_Array, SAC_1MSM_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_1MSM_SAC', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_1MSM_VIC' in InpLayersCombination:
            YYYYMMDD_Of_Array, VIC_1MSM_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_1MSM_VIC', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_TCSM_Mosaic' in InpLayersCombination:
            YYYYMMDD_Of_Array, Mosaic_TCSM_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_TCSM_Mosaic', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_TCSM_Noah' in InpLayersCombination:
            YYYYMMDD_Of_Array, Noah_TCSM_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_TCSM_Noah', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_TCSM_SAC' in InpLayersCombination:
            YYYYMMDD_Of_Array, SAC_TCSM_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_TCSM_SAC', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_TCSM_VIC' in InpLayersCombination:
            YYYYMMDD_Of_Array, VIC_TCSM_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_TCSM_VIC', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_EVAP_Mosaic' in InpLayersCombination:
            YYYYMMDD_Of_Array, Mosaic_EVAP_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_EVAP_Mosaic', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_EVAP_Noah' in InpLayersCombination:
            YYYYMMDD_Of_Array, Noah_EVAP_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_EVAP_Noah', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_EVAP_SAC' in InpLayersCombination:
            YYYYMMDD_Of_Array, SAC_EVAP_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_EVAP_SAC', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_EVAP_VIC' in InpLayersCombination:
            YYYYMMDD_Of_Array, VIC_EVAP_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_EVAP_VIC', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_SWE_Mosaic' in InpLayersCombination:
            YYYYMMDD_Of_Array, Mosaic_SWE_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_SWE_Mosaic', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_SWE_Noah' in InpLayersCombination:
            YYYYMMDD_Of_Array, Noah_SWE_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_SWE_Noah', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_SWE_SAC' in InpLayersCombination:
            YYYYMMDD_Of_Array, SAC_SWE_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_SWE_SAC', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_SWE_VIC' in InpLayersCombination:
            YYYYMMDD_Of_Array, VIC_SWE_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_SWE_VIC', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_RUN_Mosaic' in InpLayersCombination:
            YYYYMMDD_Of_Array, Mosaic_RUN_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_RUN_Mosaic', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_RUN_Noah' in InpLayersCombination:
            YYYYMMDD_Of_Array, Noah_RUN_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_RUN_Noah', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_RUN_SAC' in InpLayersCombination:
            YYYYMMDD_Of_Array, SAC_RUN_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_RUN_SAC', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_RUN_VIC' in InpLayersCombination:
            YYYYMMDD_Of_Array, VIC_RUN_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_RUN_VIC', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_STRMH04_Mosaic' in InpLayersCombination:
            YYYYMMDD_Of_Array, Mosaic_STRM_H04_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_STRMH04_Mosaic', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_STRMH04_Noah' in InpLayersCombination:
            YYYYMMDD_Of_Array, Noah_STRM_H04_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_STRMH04_Noah', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_STRMH04_SAC' in InpLayersCombination:
            YYYYMMDD_Of_Array, SAC_STRM_H04_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_STRMH04_SAC', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'NLDAS2D_STRMH04_VIC' in InpLayersCombination:
            YYYYMMDD_Of_Array, VIC_STRM_H04_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'NLDAS2D_STRMH04_VIC', XYData_NLDAS_2_daily, 'YYYYMMDD_Of_Array', 'NLDAS_2_daily_PrcntlArray')
        if 'VegDRI' in InpLayersCombination:
    #        YYYYMMDD_Of_Array, VegDRI_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'VegDRI', XYData_VegDRI_MonthlyPerc, 'YYYYMMDD_Of_Array', 'VegDRI_PrcntlArray')
            VegDRI_PrcntlArray = np.ones(Target_Array.shape, dtype=np.float32)
        if 'QuickDRI' in InpLayersCombination:
    #        YYYYMMDD_Of_Array, QuickDRI_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'QuickDRI', XYData_QuickDRI_MonthlyPerc, 'YYYYMMDD_Of_Array', 'QuickDRI_PrcntlArray')
            QuickDRI_PrcntlArray = np.ones(Target_Array.shape, dtype=np.float32)
        if 'ESI_4wk' in InpLayersCombination:
    #        YYYYMMDD_Of_Array, ESI4Week_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'ESI_4wk', XYData_ESImultiWeek_MonthlyPerc, 'YYYYMMDD_Of_Array', 'ESI4Week_PrcntlArray')
            ESI4Week_PrcntlArray = np.ones(Target_Array.shape, dtype=np.float32)
        if 'ESI_12wk' in InpLayersCombination:
    #        YYYYMMDD_Of_Array, ESI12Week_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'ESI_12wk', XYData_ESImultiWeek_MonthlyPerc, 'YYYYMMDD_Of_Array', 'ESI12Week_PrcntlArray')
            ESI12Week_PrcntlArray = np.ones(Target_Array.shape, dtype=np.float32)
        if 'SPI_gamma_01_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spi_gamma_01_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPI_gamma_01_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SPI_gamma_02_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spi_gamma_02_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPI_gamma_02_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SPI_gamma_03_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spi_gamma_03_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPI_gamma_03_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SPI_gamma_06_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spi_gamma_06_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPI_gamma_06_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SPI_gamma_09_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spi_gamma_09_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPI_gamma_09_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SPI_gamma_12_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spi_gamma_12_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPI_gamma_12_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SPI_gamma_24_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spi_gamma_24_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPI_gamma_24_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SPI_gamma_36_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spi_gamma_36_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPI_gamma_36_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SPI_gamma_48_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spi_gamma_48_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPI_gamma_48_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SPI_gamma_60_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spi_gamma_60_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPI_gamma_60_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SPI_gamma_72_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spi_gamma_72_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPI_gamma_72_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SPEI_pear_01_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spei_pearson_01_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPEI_pear_01_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SPEI_pear_02_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spei_pearson_02_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPEI_pear_02_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SPEI_pear_03_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spei_pearson_03_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPEI_pear_03_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SPEI_pear_06_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spei_pearson_06_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPEI_pear_06_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SPEI_pear_09_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spei_pearson_09_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPEI_pear_09_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SPEI_pear_12_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spei_pearson_12_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPEI_pear_12_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SPEI_pear_24_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spei_pearson_24_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPEI_pear_24_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SPEI_pear_36_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spei_pearson_36_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPEI_pear_36_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SPEI_pear_48_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spei_pearson_48_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPEI_pear_48_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SPEI_pear_60_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spei_pearson_60_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPEI_pear_60_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SPEI_pear_72_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, spei_pearson_72_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SPEI_pear_72_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'tavg_01_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, tavg_01_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'tavg_01_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'tmax_01_nCG' in InpLayersCombination:
            YYYYMMDD_Of_Array, tmax_01_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'tmax_01_nCG', XYData_AllnCG, 'YYYYMMDD_Of_Array', 'Variable_PrcntlArray')
        if 'SNODAS' in InpLayersCombination:
            YYYYMMDD_Of_Array, SNODAS_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SNODAS', XYData_SNODAS, 'YYYYMMDD_Of_Array', 'SNODAS_PrcntlArray')
        if 'ESA_CCI' in InpLayersCombination:
    #        YYYYMMDD_Of_Array, ESA_CCI_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'ESA_CCI', XYData_SNODASnESACCI, 'YYYYMMDD_Of_Array', 'ESA_CCI_PrcntlArray')
            ESA_CCI_PrcntlArray = np.ones(Target_Array.shape, dtype=np.float32)
        if 'IMERG_01' in InpLayersCombination:
            YYYYMMDD_Of_Array, IMERG_01_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'IMERG_01', XYData_IMERG_01, 'YYYYMMDD_Of_Array', 'IMERG_nMonth_PrcntlArray')
        if 'IMERG_02' in InpLayersCombination:
            YYYYMMDD_Of_Array, IMERG_02_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'IMERG_02', XYData_IMERG_02, 'YYYYMMDD_Of_Array', 'IMERG_nMonth_PrcntlArray')
        if 'IMERG_03' in InpLayersCombination:
            YYYYMMDD_Of_Array, IMERG_03_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'IMERG_03', XYData_IMERG_03, 'YYYYMMDD_Of_Array', 'IMERG_nMonth_PrcntlArray')
        if 'IMERG_06' in InpLayersCombination:
            YYYYMMDD_Of_Array, IMERG_06_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'IMERG_06', XYData_IMERG_06, 'YYYYMMDD_Of_Array', 'IMERG_nMonth_PrcntlArray')
        if 'IMERG_09' in InpLayersCombination:
            YYYYMMDD_Of_Array, IMERG_09_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'IMERG_09', XYData_IMERG_09, 'YYYYMMDD_Of_Array', 'IMERG_nMonth_PrcntlArray')
        if 'IMERG_12' in InpLayersCombination:
            YYYYMMDD_Of_Array, IMERG_12_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'IMERG_12', XYData_IMERG_12, 'YYYYMMDD_Of_Array', 'IMERG_nMonth_PrcntlArray')
        if 'IMERG_24' in InpLayersCombination:
            YYYYMMDD_Of_Array, IMERG_24_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'IMERG_24', XYData_IMERG_24, 'YYYYMMDD_Of_Array', 'IMERG_nMonth_PrcntlArray')
        if 'IMERG_36' in InpLayersCombination:
            YYYYMMDD_Of_Array, IMERG_36_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'IMERG_36', XYData_IMERG_36, 'YYYYMMDD_Of_Array', 'IMERG_nMonth_PrcntlArray')
        if 'IMERG_48' in InpLayersCombination:
            YYYYMMDD_Of_Array, IMERG_48_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'IMERG_48', XYData_IMERG_48, 'YYYYMMDD_Of_Array', 'IMERG_nMonth_PrcntlArray')
        if 'IMERG_60' in InpLayersCombination:
            YYYYMMDD_Of_Array, IMERG_60_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'IMERG_60', XYData_IMERG_60, 'YYYYMMDD_Of_Array', 'IMERG_nMonth_PrcntlArray')
        if 'IMERG_72' in InpLayersCombination:
            YYYYMMDD_Of_Array, IMERG_72_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'IMERG_72', XYData_IMERG_72, 'YYYYMMDD_Of_Array', 'IMERG_nMonth_PrcntlArray')
        if 'SmNDVI_BlendedVHP' in InpLayersCombination:
            YYYYMMDD_Of_Array, SmNDVI_BlendedVHP_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'SmNDVI_BlendedVHP', XYData_BlendedVHP_MonthlyPerc, 'YYYYMMDD_Of_Array', 'BlendedVHP_SMN_PrcntlArray')
    #        SmNDVI_BlendedVHP_PrcntlArray = np.ones(Target_Array.shape, dtype=np.float32)
        if 'TCI_BlendedVHP' in InpLayersCombination:
            YYYYMMDD_Of_Array, TCI_BlendedVHP_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'TCI_BlendedVHP', XYData_BlendedVHP_MonthlyPerc, 'YYYYMMDD_Of_Array', 'BlendedVHP_TCI_PrcntlArray')
    #        TCI_BlendedVHP_PrcntlArray = np.ones(Target_Array.shape, dtype=np.float32)
        if 'VCI_BlendedVHP' in InpLayersCombination:
            YYYYMMDD_Of_Array, VCI_BlendedVHP_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'VCI_BlendedVHP', XYData_BlendedVHP_MonthlyPerc, 'YYYYMMDD_Of_Array', 'BlendedVHP_VCI_PrcntlArray')
    #        VCI_BlendedVHP_PrcntlArray = np.ones(Target_Array.shape, dtype=np.float32)
        if 'VHI_BlendedVHP' in InpLayersCombination:
            YYYYMMDD_Of_Array, VHI_BlendedVHP_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'VHI_BlendedVHP', XYData_BlendedVHP_MonthlyPerc, 'YYYYMMDD_Of_Array', 'BlendedVHP_VHI_PrcntlArray')
    #        VHI_BlendedVHP_PrcntlArray = np.ones(Target_Array.shape, dtype=np.float32)
        if 'GlobSnow3' in InpLayersCombination:
    #        YYYYMMDD_Of_Array, GlobSnow3_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, 'GlobSnow3', XYData_GlobSnow3_OverallPerc, 'YYYYMMDD_Of_Array', 'GlobSnow3_PrcntlArray')
            GlobSnow3_PrcntlArray = np.ones(Target_Array.shape, dtype=np.float32)
        #End input percentile arrays
        del YYYYMMDD_Of_Array

        #Begin creating backup arrays to be accessed during the while loop of WindowSize increase
        Target_Array_Backup = np.copy(Target_Array)
        if 'Z_index' in InpLayersCombination:
            ZIndex_PrcntlArray_Backup = np.copy(ZIndex_PrcntlArray)
        if 'Z_index_60_month' in InpLayersCombination:
            ZIndex60month_PrcntlArray_Backup = np.copy(ZIndex60month_PrcntlArray)
        if 'PMDI' in InpLayersCombination:
            PMDI_PrcntlArray_Backup = np.copy(PMDI_PrcntlArray)
        if 'PHDI' in InpLayersCombination:
            PHDI_PrcntlArray_Backup = np.copy(PHDI_PrcntlArray)
        if 'prcp_01_nCG' in InpLayersCombination:
            prcp_01_PrcntlArray_Backup = np.copy(prcp_01_PrcntlArray)
        if 'prcp_02_nCG' in InpLayersCombination:
            prcp_02_PrcntlArray_Backup = np.copy(prcp_02_PrcntlArray)
        if 'prcp_03_nCG' in InpLayersCombination:
            prcp_03_PrcntlArray_Backup = np.copy(prcp_03_PrcntlArray)
        if 'prcp_06_nCG' in InpLayersCombination:
            prcp_06_PrcntlArray_Backup = np.copy(prcp_06_PrcntlArray)
        if 'prcp_09_nCG' in InpLayersCombination:
            prcp_09_PrcntlArray_Backup = np.copy(prcp_09_PrcntlArray)
        if 'prcp_12_nCG' in InpLayersCombination:
            prcp_12_PrcntlArray_Backup = np.copy(prcp_12_PrcntlArray)
        if 'prcp_24_nCG' in InpLayersCombination:
            prcp_24_PrcntlArray_Backup = np.copy(prcp_24_PrcntlArray)
        if 'prcp_36_nCG' in InpLayersCombination:
            prcp_36_PrcntlArray_Backup = np.copy(prcp_36_PrcntlArray)
        if 'prcp_48_nCG' in InpLayersCombination:
            prcp_48_PrcntlArray_Backup = np.copy(prcp_48_PrcntlArray)
        if 'prcp_60_nCG' in InpLayersCombination:
            prcp_60_PrcntlArray_Backup = np.copy(prcp_60_PrcntlArray)
        if 'prcp_72_nCG' in InpLayersCombination:
            prcp_72_PrcntlArray_Backup = np.copy(prcp_72_PrcntlArray)
        if 'CPC_soil_moisture' in InpLayersCombination:
            CPCsoilmoist_PrcntlArray_Backup = np.copy(CPCsoilmoist_PrcntlArray)
        if 'GRACE_DA_gw' in InpLayersCombination:
            GRACE_DA_gw_PrcntlArray_Backup = np.copy(GRACE_DA_gw_PrcntlArray)
        if 'GRACE_DA_sfsm' in InpLayersCombination:
            GRACE_DA_sfsm_PrcntlArray_Backup = np.copy(GRACE_DA_sfsm_PrcntlArray)
        if 'GRACE_DA_rtzsm' in InpLayersCombination:
            GRACE_DA_rtzsm_PrcntlArray_Backup = np.copy(GRACE_DA_rtzsm_PrcntlArray)
        if 'EDDI_1wk' in InpLayersCombination:
            EDDI1wk_PrcntlArray_Backup = np.copy(EDDI1wk_PrcntlArray)
        if 'EDDI_2wk' in InpLayersCombination:
            EDDI2wk_PrcntlArray_Backup = np.copy(EDDI2wk_PrcntlArray)
        if 'EDDI_3wk' in InpLayersCombination:
            EDDI3wk_PrcntlArray_Backup = np.copy(EDDI3wk_PrcntlArray)
        if 'EDDI_4wk' in InpLayersCombination:
            EDDI4wk_PrcntlArray_Backup = np.copy(EDDI4wk_PrcntlArray)
        if 'EDDI_5wk' in InpLayersCombination:
            EDDI5wk_PrcntlArray_Backup = np.copy(EDDI5wk_PrcntlArray)
        if 'EDDI_6wk' in InpLayersCombination:
            EDDI6wk_PrcntlArray_Backup = np.copy(EDDI6wk_PrcntlArray)
        if 'EDDI_7wk' in InpLayersCombination:
            EDDI7wk_PrcntlArray_Backup = np.copy(EDDI7wk_PrcntlArray)
        if 'EDDI_8wk' in InpLayersCombination:
            EDDI8wk_PrcntlArray_Backup = np.copy(EDDI8wk_PrcntlArray)
        if 'EDDI_9wk' in InpLayersCombination:
            EDDI9wk_PrcntlArray_Backup = np.copy(EDDI9wk_PrcntlArray)
        if 'EDDI_10wk' in InpLayersCombination:
            EDDI10wk_PrcntlArray_Backup = np.copy(EDDI10wk_PrcntlArray)
        if 'EDDI_11wk' in InpLayersCombination:
            EDDI11wk_PrcntlArray_Backup = np.copy(EDDI11wk_PrcntlArray)
        if 'EDDI_12wk' in InpLayersCombination:
            EDDI12wk_PrcntlArray_Backup = np.copy(EDDI12wk_PrcntlArray)
        if 'EDDI_1mn' in InpLayersCombination:
            EDDI1mn_PrcntlArray_Backup = np.copy(EDDI1mn_PrcntlArray)
        if 'EDDI_2mn' in InpLayersCombination:
            EDDI2mn_PrcntlArray_Backup = np.copy(EDDI2mn_PrcntlArray)
        if 'EDDI_3mn' in InpLayersCombination:
            EDDI3mn_PrcntlArray_Backup = np.copy(EDDI3mn_PrcntlArray)
        if 'EDDI_4mn' in InpLayersCombination:
            EDDI4mn_PrcntlArray_Backup = np.copy(EDDI4mn_PrcntlArray)
        if 'EDDI_5mn' in InpLayersCombination:
            EDDI5mn_PrcntlArray_Backup = np.copy(EDDI5mn_PrcntlArray)
        if 'EDDI_6mn' in InpLayersCombination:
            EDDI6mn_PrcntlArray_Backup = np.copy(EDDI6mn_PrcntlArray)
        if 'EDDI_7mn' in InpLayersCombination:
            EDDI7mn_PrcntlArray_Backup = np.copy(EDDI7mn_PrcntlArray)
        if 'EDDI_8mn' in InpLayersCombination:
            EDDI8mn_PrcntlArray_Backup = np.copy(EDDI8mn_PrcntlArray)
        if 'EDDI_9mn' in InpLayersCombination:
            EDDI9mn_PrcntlArray_Backup = np.copy(EDDI9mn_PrcntlArray)
        if 'EDDI_10mn' in InpLayersCombination:
            EDDI10mn_PrcntlArray_Backup = np.copy(EDDI10mn_PrcntlArray)
        if 'EDDI_11mn' in InpLayersCombination:
            EDDI11mn_PrcntlArray_Backup = np.copy(EDDI11mn_PrcntlArray)
        if 'EDDI_12mn' in InpLayersCombination:
            EDDI12mn_PrcntlArray_Backup = np.copy(EDDI12mn_PrcntlArray)
        if 'NLDAS2D_1MSM_Mosaic' in InpLayersCombination:
            Mosaic_1MSM_PrcntlArray_Backup = np.copy(Mosaic_1MSM_PrcntlArray)
        if 'NLDAS2D_1MSM_Noah' in InpLayersCombination:
            Noah_1MSM_PrcntlArray_Backup = np.copy(Noah_1MSM_PrcntlArray)
        if 'NLDAS2D_1MSM_SAC' in InpLayersCombination:
            SAC_1MSM_PrcntlArray_Backup = np.copy(SAC_1MSM_PrcntlArray)
        if 'NLDAS2D_1MSM_VIC' in InpLayersCombination:
            VIC_1MSM_PrcntlArray_Backup = np.copy(VIC_1MSM_PrcntlArray)
        if 'NLDAS2D_TCSM_Mosaic' in InpLayersCombination:
            Mosaic_TCSM_PrcntlArray_Backup = np.copy(Mosaic_TCSM_PrcntlArray)
        if 'NLDAS2D_TCSM_Noah' in InpLayersCombination:
            Noah_TCSM_PrcntlArray_Backup = np.copy(Noah_TCSM_PrcntlArray)
        if 'NLDAS2D_TCSM_SAC' in InpLayersCombination:
            SAC_TCSM_PrcntlArray_Backup = np.copy(SAC_TCSM_PrcntlArray)
        if 'NLDAS2D_TCSM_VIC' in InpLayersCombination:
            VIC_TCSM_PrcntlArray_Backup = np.copy(VIC_TCSM_PrcntlArray)
        if 'NLDAS2D_EVAP_Mosaic' in InpLayersCombination:
            Mosaic_EVAP_PrcntlArray_Backup = np.copy(Mosaic_EVAP_PrcntlArray)
        if 'NLDAS2D_EVAP_Noah' in InpLayersCombination:
            Noah_EVAP_PrcntlArray_Backup = np.copy(Noah_EVAP_PrcntlArray)
        if 'NLDAS2D_EVAP_SAC' in InpLayersCombination:
            SAC_EVAP_PrcntlArray_Backup = np.copy(SAC_EVAP_PrcntlArray)
        if 'NLDAS2D_EVAP_VIC' in InpLayersCombination:
            VIC_EVAP_PrcntlArray_Backup = np.copy(VIC_EVAP_PrcntlArray)
        if 'NLDAS2D_SWE_Mosaic' in InpLayersCombination:
            Mosaic_SWE_PrcntlArray_Backup = np.copy(Mosaic_SWE_PrcntlArray)
        if 'NLDAS2D_SWE_Noah' in InpLayersCombination:
            Noah_SWE_PrcntlArray_Backup = np.copy(Noah_SWE_PrcntlArray)
        if 'NLDAS2D_SWE_SAC' in InpLayersCombination:
            SAC_SWE_PrcntlArray_Backup = np.copy(SAC_SWE_PrcntlArray)
        if 'NLDAS2D_SWE_VIC' in InpLayersCombination:
            VIC_SWE_PrcntlArray_Backup = np.copy(VIC_SWE_PrcntlArray)
        if 'NLDAS2D_RUN_Mosaic' in InpLayersCombination:
            Mosaic_RUN_PrcntlArray_Backup = np.copy(Mosaic_RUN_PrcntlArray)
        if 'NLDAS2D_RUN_Noah' in InpLayersCombination:
            Noah_RUN_PrcntlArray_Backup = np.copy(Noah_RUN_PrcntlArray)
        if 'NLDAS2D_RUN_SAC' in InpLayersCombination:
            SAC_RUN_PrcntlArray_Backup = np.copy(SAC_RUN_PrcntlArray)
        if 'NLDAS2D_RUN_VIC' in InpLayersCombination:
            VIC_RUN_PrcntlArray_Backup = np.copy(VIC_RUN_PrcntlArray)
        if 'NLDAS2D_STRMH04_Mosaic' in InpLayersCombination:
            Mosaic_STRM_H04_PrcntlArray_Backup = np.copy(Mosaic_STRM_H04_PrcntlArray)
        if 'NLDAS2D_STRMH04_Noah' in InpLayersCombination:
            Noah_STRM_H04_PrcntlArray_Backup = np.copy(Noah_STRM_H04_PrcntlArray)
        if 'NLDAS2D_STRMH04_SAC' in InpLayersCombination:
            SAC_STRM_H04_PrcntlArray_Backup = np.copy(SAC_STRM_H04_PrcntlArray)
        if 'NLDAS2D_STRMH04_VIC' in InpLayersCombination:
            VIC_STRM_H04_PrcntlArray_Backup = np.copy(VIC_STRM_H04_PrcntlArray)
        if 'VegDRI' in InpLayersCombination:
            VegDRI_PrcntlArray_Backup = np.copy(VegDRI_PrcntlArray)
        if 'QuickDRI' in InpLayersCombination:
            QuickDRI_PrcntlArray_Backup = np.copy(QuickDRI_PrcntlArray)
        if 'ESI_4wk' in InpLayersCombination:
            ESI4Week_PrcntlArray_Backup = np.copy(ESI4Week_PrcntlArray)
        if 'ESI_12wk' in InpLayersCombination:
            ESI12Week_PrcntlArray_Backup = np.copy(ESI12Week_PrcntlArray)
        if 'SPI_gamma_01_nCG' in InpLayersCombination:
            spi_gamma_01_PrcntlArray_Backup = np.copy(spi_gamma_01_PrcntlArray)
        if 'SPI_gamma_02_nCG' in InpLayersCombination:
            spi_gamma_02_PrcntlArray_Backup = np.copy(spi_gamma_02_PrcntlArray)
        if 'SPI_gamma_03_nCG' in InpLayersCombination:
            spi_gamma_03_PrcntlArray_Backup = np.copy(spi_gamma_03_PrcntlArray)
        if 'SPI_gamma_06_nCG' in InpLayersCombination:
            spi_gamma_06_PrcntlArray_Backup = np.copy(spi_gamma_06_PrcntlArray)
        if 'SPI_gamma_09_nCG' in InpLayersCombination:
            spi_gamma_09_PrcntlArray_Backup = np.copy(spi_gamma_09_PrcntlArray)
        if 'SPI_gamma_12_nCG' in InpLayersCombination:
            spi_gamma_12_PrcntlArray_Backup = np.copy(spi_gamma_12_PrcntlArray)
        if 'SPI_gamma_24_nCG' in InpLayersCombination:
            spi_gamma_24_PrcntlArray_Backup = np.copy(spi_gamma_24_PrcntlArray)
        if 'SPI_gamma_36_nCG' in InpLayersCombination:
            spi_gamma_36_PrcntlArray_Backup = np.copy(spi_gamma_36_PrcntlArray)
        if 'SPI_gamma_48_nCG' in InpLayersCombination:
            spi_gamma_48_PrcntlArray_Backup = np.copy(spi_gamma_48_PrcntlArray)
        if 'SPI_gamma_60_nCG' in InpLayersCombination:
            spi_gamma_60_PrcntlArray_Backup = np.copy(spi_gamma_60_PrcntlArray)
        if 'SPI_gamma_72_nCG' in InpLayersCombination:
            spi_gamma_72_PrcntlArray_Backup = np.copy(spi_gamma_72_PrcntlArray)
        if 'SPEI_pear_01_nCG' in InpLayersCombination:
            spei_pearson_01_PrcntlArray_Backup = np.copy(spei_pearson_01_PrcntlArray)
        if 'SPEI_pear_02_nCG' in InpLayersCombination:
            spei_pearson_02_PrcntlArray_Backup = np.copy(spei_pearson_02_PrcntlArray)
        if 'SPEI_pear_03_nCG' in InpLayersCombination:
            spei_pearson_03_PrcntlArray_Backup = np.copy(spei_pearson_03_PrcntlArray)
        if 'SPEI_pear_06_nCG' in InpLayersCombination:
            spei_pearson_06_PrcntlArray_Backup = np.copy(spei_pearson_06_PrcntlArray)
        if 'SPEI_pear_09_nCG' in InpLayersCombination:
            spei_pearson_09_PrcntlArray_Backup = np.copy(spei_pearson_09_PrcntlArray)
        if 'SPEI_pear_12_nCG' in InpLayersCombination:
            spei_pearson_12_PrcntlArray_Backup = np.copy(spei_pearson_12_PrcntlArray)
        if 'SPEI_pear_24_nCG' in InpLayersCombination:
            spei_pearson_24_PrcntlArray_Backup = np.copy(spei_pearson_24_PrcntlArray)
        if 'SPEI_pear_36_nCG' in InpLayersCombination:
            spei_pearson_36_PrcntlArray_Backup = np.copy(spei_pearson_36_PrcntlArray)
        if 'SPEI_pear_48_nCG' in InpLayersCombination:
            spei_pearson_48_PrcntlArray_Backup = np.copy(spei_pearson_48_PrcntlArray)
        if 'SPEI_pear_60_nCG' in InpLayersCombination:
            spei_pearson_60_PrcntlArray_Backup = np.copy(spei_pearson_60_PrcntlArray)
        if 'SPEI_pear_72_nCG' in InpLayersCombination:
            spei_pearson_72_PrcntlArray_Backup = np.copy(spei_pearson_72_PrcntlArray)
        if 'tavg_01_nCG' in InpLayersCombination:
            tavg_01_PrcntlArray_Backup = np.copy(tavg_01_PrcntlArray) 
        if 'tmax_01_nCG' in InpLayersCombination:
            tmax_01_PrcntlArray_Backup = np.copy(tmax_01_PrcntlArray)
        if 'SNODAS' in InpLayersCombination:
            SNODAS_PrcntlArray_Backup = np.copy(SNODAS_PrcntlArray)
        if 'ESA_CCI' in InpLayersCombination:
            ESA_CCI_PrcntlArray_Backup = np.copy(ESA_CCI_PrcntlArray)
        if 'IMERG_01' in InpLayersCombination:
            IMERG_01_PrcntlArray_Backup = np.copy(IMERG_01_PrcntlArray)
        if 'IMERG_02' in InpLayersCombination:
            IMERG_02_PrcntlArray_Backup = np.copy(IMERG_02_PrcntlArray)
        if 'IMERG_03' in InpLayersCombination:
            IMERG_03_PrcntlArray_Backup = np.copy(IMERG_03_PrcntlArray)
        if 'IMERG_06' in InpLayersCombination:
            IMERG_06_PrcntlArray_Backup = np.copy(IMERG_06_PrcntlArray)
        if 'IMERG_09' in InpLayersCombination:
            IMERG_09_PrcntlArray_Backup = np.copy(IMERG_09_PrcntlArray)
        if 'IMERG_12' in InpLayersCombination:
            IMERG_12_PrcntlArray_Backup = np.copy(IMERG_12_PrcntlArray)
        if 'IMERG_24' in InpLayersCombination:
            IMERG_24_PrcntlArray_Backup = np.copy(IMERG_24_PrcntlArray)
        if 'IMERG_36' in InpLayersCombination:
            IMERG_36_PrcntlArray_Backup = np.copy(IMERG_36_PrcntlArray)
        if 'IMERG_48' in InpLayersCombination:
            IMERG_48_PrcntlArray_Backup = np.copy(IMERG_48_PrcntlArray)
        if 'IMERG_60' in InpLayersCombination:
            IMERG_60_PrcntlArray_Backup = np.copy(IMERG_60_PrcntlArray)
        if 'IMERG_72' in InpLayersCombination:
            IMERG_72_PrcntlArray_Backup = np.copy(IMERG_72_PrcntlArray)
        if 'SmNDVI_BlendedVHP' in InpLayersCombination:
            SmNDVI_BlendedVHP_PrcntlArray_Backup = np.copy(SmNDVI_BlendedVHP_PrcntlArray)
        if 'TCI_BlendedVHP' in InpLayersCombination:
            TCI_BlendedVHP_PrcntlArray_Backup = np.copy(TCI_BlendedVHP_PrcntlArray)
        if 'VCI_BlendedVHP' in InpLayersCombination:
            VCI_BlendedVHP_PrcntlArray_Backup = np.copy(VCI_BlendedVHP_PrcntlArray)
        if 'VHI_BlendedVHP' in InpLayersCombination:
            VHI_BlendedVHP_PrcntlArray_Backup = np.copy(VHI_BlendedVHP_PrcntlArray)
        if 'GlobSnow3' in InpLayersCombination:
            GlobSnow3_PrcntlArray_Backup = np.copy(GlobSnow3_PrcntlArray)
        #End creating backup arrays to be accessed during the while loop of WindowSize increase

        if WhichSeason == 'P':
            WhichRows = np.where( (MM_Of_Array >= 3) & (MM_Of_Array <= 5) )
        elif WhichSeason == 'U':
            WhichRows = np.where( (MM_Of_Array >= 6) & (MM_Of_Array <= 8) )
        elif WhichSeason == 'F':
            WhichRows = np.where( (MM_Of_Array >= 9) & (MM_Of_Array <= 11) )
        elif WhichSeason == 'W':
            WhichRows = np.where( (MM_Of_Array >= 12) | (MM_Of_Array <= 2) )
        del MM_Of_Array

        ThisWindowSize = copy.deepcopy(MinimumWindowSize)
        SamplesForFracI = copy.deepcopy(MinSamplesForFracI) - 1

        while ((ThisWindowSize <= MaximumWindowSize) and (SamplesForFracI < MinSamplesForFracI)): 
        
            ThisWindowSize_prev = copy.deepcopy(ThisWindowSize)
            #SamplesForFracI_prev = copy.deepcopy(SamplesForFracI)
    
            Window_Thickness_CenterToEgde = (ThisWindowSize - 1) / 2
            Idxs_In_PxlRowCols = np.where( ( PxlRow_SortedArr_FrmShpFile >= ThisPxlRow - Window_Thickness_CenterToEgde ) &
                                                                        ( PxlRow_SortedArr_FrmShpFile <= ThisPxlRow + Window_Thickness_CenterToEgde ) &
                                                                        ( PxlCol_SortedArr_FrmShpFile >= ThisPxlCol - Window_Thickness_CenterToEgde ) &
                                                                        ( PxlCol_SortedArr_FrmShpFile <= ThisPxlCol + Window_Thickness_CenterToEgde ) )

            Target_Array = Target_Array_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'Z_index' in InpLayersCombination:
                ZIndex_PrcntlArray = ZIndex_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'Z_index_60_month' in InpLayersCombination:
                ZIndex60month_PrcntlArray = ZIndex60month_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'PMDI' in InpLayersCombination:
                PMDI_PrcntlArray = PMDI_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'PHDI' in InpLayersCombination:
                PHDI_PrcntlArray = PHDI_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'prcp_01_nCG' in InpLayersCombination:
                prcp_01_PrcntlArray = prcp_01_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'prcp_02_nCG' in InpLayersCombination:
                prcp_02_PrcntlArray = prcp_02_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'prcp_03_nCG' in InpLayersCombination:
                prcp_03_PrcntlArray = prcp_03_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'prcp_06_nCG' in InpLayersCombination:
                prcp_06_PrcntlArray = prcp_06_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'prcp_09_nCG' in InpLayersCombination:
                prcp_09_PrcntlArray = prcp_09_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'prcp_12_nCG' in InpLayersCombination:
                prcp_12_PrcntlArray = prcp_12_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'prcp_24_nCG' in InpLayersCombination:
                prcp_24_PrcntlArray = prcp_24_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'prcp_36_nCG' in InpLayersCombination:
                prcp_36_PrcntlArray = prcp_36_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'prcp_48_nCG' in InpLayersCombination:
                prcp_48_PrcntlArray = prcp_48_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'prcp_60_nCG' in InpLayersCombination:
                prcp_60_PrcntlArray = prcp_60_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'prcp_72_nCG' in InpLayersCombination:
                prcp_72_PrcntlArray = prcp_72_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'CPC_soil_moisture' in InpLayersCombination:
                CPCsoilmoist_PrcntlArray = CPCsoilmoist_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'GRACE_DA_gw' in InpLayersCombination:
                GRACE_DA_gw_PrcntlArray = GRACE_DA_gw_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'GRACE_DA_sfsm' in InpLayersCombination:
                GRACE_DA_sfsm_PrcntlArray = GRACE_DA_sfsm_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'GRACE_DA_rtzsm' in InpLayersCombination:
                GRACE_DA_rtzsm_PrcntlArray = GRACE_DA_rtzsm_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_1wk' in InpLayersCombination:
                EDDI1wk_PrcntlArray = EDDI1wk_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_2wk' in InpLayersCombination:
                EDDI2wk_PrcntlArray = EDDI2wk_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_3wk' in InpLayersCombination:
                EDDI3wk_PrcntlArray = EDDI3wk_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_4wk' in InpLayersCombination:
                EDDI4wk_PrcntlArray = EDDI4wk_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_5wk' in InpLayersCombination:
                EDDI5wk_PrcntlArray = EDDI5wk_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_6wk' in InpLayersCombination:
                EDDI6wk_PrcntlArray = EDDI6wk_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_7wk' in InpLayersCombination:
                EDDI7wk_PrcntlArray = EDDI7wk_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_8wk' in InpLayersCombination:
                EDDI8wk_PrcntlArray = EDDI8wk_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_9wk' in InpLayersCombination:
                EDDI9wk_PrcntlArray = EDDI9wk_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_10wk' in InpLayersCombination:
                EDDI10wk_PrcntlArray = EDDI10wk_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_11wk' in InpLayersCombination:
                EDDI11wk_PrcntlArray = EDDI11wk_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_12wk' in InpLayersCombination:
                EDDI12wk_PrcntlArray = EDDI12wk_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_1mn' in InpLayersCombination:
                EDDI1mn_PrcntlArray = EDDI1mn_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_2mn' in InpLayersCombination:
                EDDI2mn_PrcntlArray = EDDI2mn_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_3mn' in InpLayersCombination:
                EDDI3mn_PrcntlArray = EDDI3mn_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_4mn' in InpLayersCombination:
                EDDI4mn_PrcntlArray = EDDI4mn_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_5mn' in InpLayersCombination:
                EDDI5mn_PrcntlArray = EDDI5mn_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_6mn' in InpLayersCombination:
                EDDI6mn_PrcntlArray = EDDI6mn_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_7mn' in InpLayersCombination:
                EDDI7mn_PrcntlArray = EDDI7mn_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_8mn' in InpLayersCombination:
                EDDI8mn_PrcntlArray = EDDI8mn_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_9mn' in InpLayersCombination:
                EDDI9mn_PrcntlArray = EDDI9mn_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_10mn' in InpLayersCombination:
                EDDI10mn_PrcntlArray = EDDI10mn_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_11mn' in InpLayersCombination:
                EDDI11mn_PrcntlArray = EDDI11mn_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'EDDI_12mn' in InpLayersCombination:
                EDDI12mn_PrcntlArray = EDDI12mn_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_1MSM_Mosaic' in InpLayersCombination:
                Mosaic_1MSM_PrcntlArray = Mosaic_1MSM_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_1MSM_Noah' in InpLayersCombination:
                Noah_1MSM_PrcntlArray = Noah_1MSM_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_1MSM_SAC' in InpLayersCombination:
                SAC_1MSM_PrcntlArray = SAC_1MSM_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_1MSM_VIC' in InpLayersCombination:
                VIC_1MSM_PrcntlArray = VIC_1MSM_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_TCSM_Mosaic' in InpLayersCombination:
                Mosaic_TCSM_PrcntlArray = Mosaic_TCSM_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_TCSM_Noah' in InpLayersCombination:
                Noah_TCSM_PrcntlArray = Noah_TCSM_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_TCSM_SAC' in InpLayersCombination:
                SAC_TCSM_PrcntlArray = SAC_TCSM_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_TCSM_VIC' in InpLayersCombination:
                VIC_TCSM_PrcntlArray = VIC_TCSM_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_EVAP_Mosaic' in InpLayersCombination:
                Mosaic_EVAP_PrcntlArray = Mosaic_EVAP_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_EVAP_Noah' in InpLayersCombination:
                Noah_EVAP_PrcntlArray = Noah_EVAP_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_EVAP_SAC' in InpLayersCombination:
                SAC_EVAP_PrcntlArray = SAC_EVAP_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_EVAP_VIC' in InpLayersCombination:
                VIC_EVAP_PrcntlArray = VIC_EVAP_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_SWE_Mosaic' in InpLayersCombination:
                Mosaic_SWE_PrcntlArray = Mosaic_SWE_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_SWE_Noah' in InpLayersCombination:
                Noah_SWE_PrcntlArray = Noah_SWE_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_SWE_SAC' in InpLayersCombination:
                SAC_SWE_PrcntlArray = SAC_SWE_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_SWE_VIC' in InpLayersCombination:
                VIC_SWE_PrcntlArray = VIC_SWE_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_RUN_Mosaic' in InpLayersCombination:
                Mosaic_RUN_PrcntlArray = Mosaic_RUN_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_RUN_Noah' in InpLayersCombination:
                Noah_RUN_PrcntlArray = Noah_RUN_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_RUN_SAC' in InpLayersCombination:
                SAC_RUN_PrcntlArray = SAC_RUN_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_RUN_VIC' in InpLayersCombination:
                VIC_RUN_PrcntlArray = VIC_RUN_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_STRMH04_Mosaic' in InpLayersCombination:
                Mosaic_STRM_H04_PrcntlArray = Mosaic_STRM_H04_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_STRMH04_Noah' in InpLayersCombination:
                Noah_STRM_H04_PrcntlArray = Noah_STRM_H04_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_STRMH04_SAC' in InpLayersCombination:
                SAC_STRM_H04_PrcntlArray = SAC_STRM_H04_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'NLDAS2D_STRMH04_VIC' in InpLayersCombination:
                VIC_STRM_H04_PrcntlArray = VIC_STRM_H04_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'VegDRI' in InpLayersCombination:
                VegDRI_PrcntlArray = VegDRI_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'QuickDRI' in InpLayersCombination:
                QuickDRI_PrcntlArray = QuickDRI_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'ESI_4wk' in InpLayersCombination:
                ESI4Week_PrcntlArray = ESI4Week_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'ESI_12wk' in InpLayersCombination:
                ESI12Week_PrcntlArray = ESI12Week_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPI_gamma_01_nCG' in InpLayersCombination:
                spi_gamma_01_PrcntlArray = spi_gamma_01_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPI_gamma_02_nCG' in InpLayersCombination:
                spi_gamma_02_PrcntlArray = spi_gamma_02_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPI_gamma_03_nCG' in InpLayersCombination:
                spi_gamma_03_PrcntlArray = spi_gamma_03_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPI_gamma_06_nCG' in InpLayersCombination:
                spi_gamma_06_PrcntlArray = spi_gamma_06_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPI_gamma_09_nCG' in InpLayersCombination:
                spi_gamma_09_PrcntlArray = spi_gamma_09_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPI_gamma_12_nCG' in InpLayersCombination:
                spi_gamma_12_PrcntlArray = spi_gamma_12_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPI_gamma_24_nCG' in InpLayersCombination:
                spi_gamma_24_PrcntlArray = spi_gamma_24_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPI_gamma_36_nCG' in InpLayersCombination:
                spi_gamma_36_PrcntlArray = spi_gamma_36_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPI_gamma_48_nCG' in InpLayersCombination:
                spi_gamma_48_PrcntlArray = spi_gamma_48_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPI_gamma_60_nCG' in InpLayersCombination:
                spi_gamma_60_PrcntlArray = spi_gamma_60_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPI_gamma_72_nCG' in InpLayersCombination:
                spi_gamma_72_PrcntlArray = spi_gamma_72_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPEI_pear_01_nCG' in InpLayersCombination:
                spei_pearson_01_PrcntlArray = spei_pearson_01_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPEI_pear_02_nCG' in InpLayersCombination:
                spei_pearson_02_PrcntlArray = spei_pearson_02_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPEI_pear_03_nCG' in InpLayersCombination:
                spei_pearson_03_PrcntlArray = spei_pearson_03_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPEI_pear_06_nCG' in InpLayersCombination:
                spei_pearson_06_PrcntlArray = spei_pearson_06_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPEI_pear_09_nCG' in InpLayersCombination:
                spei_pearson_09_PrcntlArray = spei_pearson_09_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPEI_pear_12_nCG' in InpLayersCombination:
                spei_pearson_12_PrcntlArray = spei_pearson_12_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPEI_pear_24_nCG' in InpLayersCombination:
                spei_pearson_24_PrcntlArray = spei_pearson_24_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPEI_pear_36_nCG' in InpLayersCombination:
                spei_pearson_36_PrcntlArray = spei_pearson_36_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPEI_pear_48_nCG' in InpLayersCombination:
                spei_pearson_48_PrcntlArray = spei_pearson_48_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPEI_pear_60_nCG' in InpLayersCombination:
                spei_pearson_60_PrcntlArray = spei_pearson_60_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SPEI_pear_72_nCG' in InpLayersCombination:
                spei_pearson_72_PrcntlArray = spei_pearson_72_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'tavg_01_nCG' in InpLayersCombination:
                tavg_01_PrcntlArray = tavg_01_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]] 
            if 'tmax_01_nCG' in InpLayersCombination:
                tmax_01_PrcntlArray = tmax_01_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SNODAS' in InpLayersCombination:
                SNODAS_PrcntlArray = SNODAS_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'ESA_CCI' in InpLayersCombination:
                ESA_CCI_PrcntlArray = ESA_CCI_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'IMERG_01' in InpLayersCombination:
                IMERG_01_PrcntlArray = IMERG_01_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'IMERG_02' in InpLayersCombination:
                IMERG_02_PrcntlArray = IMERG_02_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'IMERG_03' in InpLayersCombination:
                IMERG_03_PrcntlArray = IMERG_03_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'IMERG_06' in InpLayersCombination:
                IMERG_06_PrcntlArray = IMERG_06_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'IMERG_09' in InpLayersCombination:
                IMERG_09_PrcntlArray = IMERG_09_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'IMERG_12' in InpLayersCombination:
                IMERG_12_PrcntlArray = IMERG_12_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'IMERG_24' in InpLayersCombination:
                IMERG_24_PrcntlArray = IMERG_24_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'IMERG_36' in InpLayersCombination:
                IMERG_36_PrcntlArray = IMERG_36_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'IMERG_48' in InpLayersCombination:
                IMERG_48_PrcntlArray = IMERG_48_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'IMERG_60' in InpLayersCombination:
                IMERG_60_PrcntlArray = IMERG_60_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'IMERG_72' in InpLayersCombination:
                IMERG_72_PrcntlArray = IMERG_72_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'SmNDVI_BlendedVHP' in InpLayersCombination:
                SmNDVI_BlendedVHP_PrcntlArray = SmNDVI_BlendedVHP_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'TCI_BlendedVHP' in InpLayersCombination:
                TCI_BlendedVHP_PrcntlArray = TCI_BlendedVHP_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'VCI_BlendedVHP' in InpLayersCombination:
                VCI_BlendedVHP_PrcntlArray = VCI_BlendedVHP_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'VHI_BlendedVHP' in InpLayersCombination:
                VHI_BlendedVHP_PrcntlArray = VHI_BlendedVHP_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            if 'GlobSnow3' in InpLayersCombination:
                GlobSnow3_PrcntlArray = GlobSnow3_PrcntlArray_Backup[:, Idxs_In_PxlRowCols[0]]
            del Idxs_In_PxlRowCols      
        
            if WhichSeason in ['P', 'U', 'F', 'W']:
                Target_Array = Target_Array[WhichRows[0], :]
                if 'Z_index' in InpLayersCombination:
                    ZIndex_PrcntlArray = ZIndex_PrcntlArray[WhichRows[0], :]
                if 'Z_index_60_month' in InpLayersCombination:
                    ZIndex60month_PrcntlArray = ZIndex60month_PrcntlArray[WhichRows[0], :]
                if 'PMDI' in InpLayersCombination:
                    PMDI_PrcntlArray = PMDI_PrcntlArray[WhichRows[0], :]
                if 'PHDI' in InpLayersCombination:
                    PHDI_PrcntlArray = PHDI_PrcntlArray[WhichRows[0], :]
                if 'prcp_01_nCG' in InpLayersCombination:
                    prcp_01_PrcntlArray = prcp_01_PrcntlArray[WhichRows[0], :]
                if 'prcp_02_nCG' in InpLayersCombination:
                    prcp_02_PrcntlArray = prcp_02_PrcntlArray[WhichRows[0], :]
                if 'prcp_03_nCG' in InpLayersCombination:
                    prcp_03_PrcntlArray = prcp_03_PrcntlArray[WhichRows[0], :]
                if 'prcp_06_nCG' in InpLayersCombination:
                    prcp_06_PrcntlArray = prcp_06_PrcntlArray[WhichRows[0], :]
                if 'prcp_09_nCG' in InpLayersCombination:
                    prcp_09_PrcntlArray = prcp_09_PrcntlArray[WhichRows[0], :]
                if 'prcp_12_nCG' in InpLayersCombination:
                    prcp_12_PrcntlArray = prcp_12_PrcntlArray[WhichRows[0], :]
                if 'prcp_24_nCG' in InpLayersCombination:
                    prcp_24_PrcntlArray = prcp_24_PrcntlArray[WhichRows[0], :]
                if 'prcp_36_nCG' in InpLayersCombination:
                    prcp_36_PrcntlArray = prcp_36_PrcntlArray[WhichRows[0], :]
                if 'prcp_48_nCG' in InpLayersCombination:
                    prcp_48_PrcntlArray = prcp_48_PrcntlArray[WhichRows[0], :]
                if 'prcp_60_nCG' in InpLayersCombination:
                    prcp_60_PrcntlArray = prcp_60_PrcntlArray[WhichRows[0], :]
                if 'prcp_72_nCG' in InpLayersCombination:
                    prcp_72_PrcntlArray = prcp_72_PrcntlArray[WhichRows[0], :]
                if 'CPC_soil_moisture' in InpLayersCombination:
                    CPCsoilmoist_PrcntlArray = CPCsoilmoist_PrcntlArray[WhichRows[0], :]
                if 'GRACE_DA_gw' in InpLayersCombination:
                    GRACE_DA_gw_PrcntlArray = GRACE_DA_gw_PrcntlArray[WhichRows[0], :]
                if 'GRACE_DA_sfsm' in InpLayersCombination:
                    GRACE_DA_sfsm_PrcntlArray = GRACE_DA_sfsm_PrcntlArray[WhichRows[0], :]
                if 'GRACE_DA_rtzsm' in InpLayersCombination:
                    GRACE_DA_rtzsm_PrcntlArray = GRACE_DA_rtzsm_PrcntlArray[WhichRows[0], :]
                if 'EDDI_1wk' in InpLayersCombination:
                    EDDI1wk_PrcntlArray = EDDI1wk_PrcntlArray[WhichRows[0], :]
                if 'EDDI_2wk' in InpLayersCombination:
                    EDDI2wk_PrcntlArray = EDDI2wk_PrcntlArray[WhichRows[0], :]
                if 'EDDI_3wk' in InpLayersCombination:
                    EDDI3wk_PrcntlArray = EDDI3wk_PrcntlArray[WhichRows[0], :]
                if 'EDDI_4wk' in InpLayersCombination:
                    EDDI4wk_PrcntlArray = EDDI4wk_PrcntlArray[WhichRows[0], :]
                if 'EDDI_5wk' in InpLayersCombination:
                    EDDI5wk_PrcntlArray = EDDI5wk_PrcntlArray[WhichRows[0], :]
                if 'EDDI_6wk' in InpLayersCombination:
                    EDDI6wk_PrcntlArray = EDDI6wk_PrcntlArray[WhichRows[0], :]
                if 'EDDI_7wk' in InpLayersCombination:
                    EDDI7wk_PrcntlArray = EDDI7wk_PrcntlArray[WhichRows[0], :]
                if 'EDDI_8wk' in InpLayersCombination:
                    EDDI8wk_PrcntlArray = EDDI8wk_PrcntlArray[WhichRows[0], :]
                if 'EDDI_9wk' in InpLayersCombination:
                    EDDI9wk_PrcntlArray = EDDI9wk_PrcntlArray[WhichRows[0], :]
                if 'EDDI_10wk' in InpLayersCombination:
                    EDDI10wk_PrcntlArray = EDDI10wk_PrcntlArray[WhichRows[0], :]
                if 'EDDI_11wk' in InpLayersCombination:
                    EDDI11wk_PrcntlArray = EDDI11wk_PrcntlArray[WhichRows[0], :]
                if 'EDDI_12wk' in InpLayersCombination:
                    EDDI12wk_PrcntlArray = EDDI12wk_PrcntlArray[WhichRows[0], :]
                if 'EDDI_1mn' in InpLayersCombination:
                    EDDI1mn_PrcntlArray = EDDI1mn_PrcntlArray[WhichRows[0], :]
                if 'EDDI_2mn' in InpLayersCombination:
                    EDDI2mn_PrcntlArray = EDDI2mn_PrcntlArray[WhichRows[0], :]
                if 'EDDI_3mn' in InpLayersCombination:
                    EDDI3mn_PrcntlArray = EDDI3mn_PrcntlArray[WhichRows[0], :]
                if 'EDDI_4mn' in InpLayersCombination:
                    EDDI4mn_PrcntlArray = EDDI4mn_PrcntlArray[WhichRows[0], :]
                if 'EDDI_5mn' in InpLayersCombination:
                    EDDI5mn_PrcntlArray = EDDI5mn_PrcntlArray[WhichRows[0], :]
                if 'EDDI_6mn' in InpLayersCombination:
                    EDDI6mn_PrcntlArray = EDDI6mn_PrcntlArray[WhichRows[0], :]
                if 'EDDI_7mn' in InpLayersCombination:
                    EDDI7mn_PrcntlArray = EDDI7mn_PrcntlArray[WhichRows[0], :]
                if 'EDDI_8mn' in InpLayersCombination:
                    EDDI8mn_PrcntlArray = EDDI8mn_PrcntlArray[WhichRows[0], :]
                if 'EDDI_9mn' in InpLayersCombination:
                    EDDI9mn_PrcntlArray = EDDI9mn_PrcntlArray[WhichRows[0], :]
                if 'EDDI_10mn' in InpLayersCombination:
                    EDDI10mn_PrcntlArray = EDDI10mn_PrcntlArray[WhichRows[0], :]
                if 'EDDI_11mn' in InpLayersCombination:
                    EDDI11mn_PrcntlArray = EDDI11mn_PrcntlArray[WhichRows[0], :]
                if 'EDDI_12mn' in InpLayersCombination:
                    EDDI12mn_PrcntlArray = EDDI12mn_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_1MSM_Mosaic' in InpLayersCombination:
                    Mosaic_1MSM_PrcntlArray = Mosaic_1MSM_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_1MSM_Noah' in InpLayersCombination:
                    Noah_1MSM_PrcntlArray = Noah_1MSM_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_1MSM_SAC' in InpLayersCombination:
                    SAC_1MSM_PrcntlArray = SAC_1MSM_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_1MSM_VIC' in InpLayersCombination:
                    VIC_1MSM_PrcntlArray = VIC_1MSM_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_TCSM_Mosaic' in InpLayersCombination:
                    Mosaic_TCSM_PrcntlArray = Mosaic_TCSM_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_TCSM_Noah' in InpLayersCombination:
                    Noah_TCSM_PrcntlArray = Noah_TCSM_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_TCSM_SAC' in InpLayersCombination:
                    SAC_TCSM_PrcntlArray = SAC_TCSM_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_TCSM_VIC' in InpLayersCombination:
                    VIC_TCSM_PrcntlArray = VIC_TCSM_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_EVAP_Mosaic' in InpLayersCombination:
                    Mosaic_EVAP_PrcntlArray = Mosaic_EVAP_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_EVAP_Noah' in InpLayersCombination:
                    Noah_EVAP_PrcntlArray = Noah_EVAP_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_EVAP_SAC' in InpLayersCombination:
                    SAC_EVAP_PrcntlArray = SAC_EVAP_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_EVAP_VIC' in InpLayersCombination:
                    VIC_EVAP_PrcntlArray = VIC_EVAP_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_SWE_Mosaic' in InpLayersCombination:
                    Mosaic_SWE_PrcntlArray = Mosaic_SWE_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_SWE_Noah' in InpLayersCombination:
                    Noah_SWE_PrcntlArray = Noah_SWE_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_SWE_SAC' in InpLayersCombination:
                    SAC_SWE_PrcntlArray = SAC_SWE_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_SWE_VIC' in InpLayersCombination:
                    VIC_SWE_PrcntlArray = VIC_SWE_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_RUN_Mosaic' in InpLayersCombination:
                    Mosaic_RUN_PrcntlArray = Mosaic_RUN_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_RUN_Noah' in InpLayersCombination:
                    Noah_RUN_PrcntlArray = Noah_RUN_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_RUN_SAC' in InpLayersCombination:
                    SAC_RUN_PrcntlArray = SAC_RUN_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_RUN_VIC' in InpLayersCombination:
                    VIC_RUN_PrcntlArray = VIC_RUN_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_STRMH04_Mosaic' in InpLayersCombination:
                    Mosaic_STRM_H04_PrcntlArray = Mosaic_STRM_H04_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_STRMH04_Noah' in InpLayersCombination:
                    Noah_STRM_H04_PrcntlArray = Noah_STRM_H04_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_STRMH04_SAC' in InpLayersCombination:
                    SAC_STRM_H04_PrcntlArray = SAC_STRM_H04_PrcntlArray[WhichRows[0], :]
                if 'NLDAS2D_STRMH04_VIC' in InpLayersCombination:
                    VIC_STRM_H04_PrcntlArray = VIC_STRM_H04_PrcntlArray[WhichRows[0], :]
                if 'VegDRI' in InpLayersCombination:
                    VegDRI_PrcntlArray = VegDRI_PrcntlArray[WhichRows[0], :]
                if 'QuickDRI' in InpLayersCombination:
                    QuickDRI_PrcntlArray = QuickDRI_PrcntlArray[WhichRows[0], :]
                if 'ESI_4wk' in InpLayersCombination:
                    ESI4Week_PrcntlArray = ESI4Week_PrcntlArray[WhichRows[0], :]
                if 'ESI_12wk' in InpLayersCombination:
                    ESI12Week_PrcntlArray = ESI12Week_PrcntlArray[WhichRows[0], :]
                if 'SPI_gamma_01_nCG' in InpLayersCombination:
                    spi_gamma_01_PrcntlArray = spi_gamma_01_PrcntlArray[WhichRows[0], :]
                if 'SPI_gamma_02_nCG' in InpLayersCombination:
                    spi_gamma_02_PrcntlArray = spi_gamma_02_PrcntlArray[WhichRows[0], :]
                if 'SPI_gamma_03_nCG' in InpLayersCombination:
                    spi_gamma_03_PrcntlArray = spi_gamma_03_PrcntlArray[WhichRows[0], :]
                if 'SPI_gamma_06_nCG' in InpLayersCombination:
                    spi_gamma_06_PrcntlArray = spi_gamma_06_PrcntlArray[WhichRows[0], :]
                if 'SPI_gamma_09_nCG' in InpLayersCombination:
                    spi_gamma_09_PrcntlArray = spi_gamma_09_PrcntlArray[WhichRows[0], :]
                if 'SPI_gamma_12_nCG' in InpLayersCombination:
                    spi_gamma_12_PrcntlArray = spi_gamma_12_PrcntlArray[WhichRows[0], :]
                if 'SPI_gamma_24_nCG' in InpLayersCombination:
                    spi_gamma_24_PrcntlArray = spi_gamma_24_PrcntlArray[WhichRows[0], :]
                if 'SPI_gamma_36_nCG' in InpLayersCombination:
                    spi_gamma_36_PrcntlArray = spi_gamma_36_PrcntlArray[WhichRows[0], :]
                if 'SPI_gamma_48_nCG' in InpLayersCombination:
                    spi_gamma_48_PrcntlArray = spi_gamma_48_PrcntlArray[WhichRows[0], :]
                if 'SPI_gamma_60_nCG' in InpLayersCombination:
                    spi_gamma_60_PrcntlArray = spi_gamma_60_PrcntlArray[WhichRows[0], :]
                if 'SPI_gamma_72_nCG' in InpLayersCombination:
                    spi_gamma_72_PrcntlArray = spi_gamma_72_PrcntlArray[WhichRows[0], :]
                if 'SPEI_pear_01_nCG' in InpLayersCombination:
                    spei_pearson_01_PrcntlArray = spei_pearson_01_PrcntlArray[WhichRows[0], :]
                if 'SPEI_pear_02_nCG' in InpLayersCombination:
                    spei_pearson_02_PrcntlArray = spei_pearson_02_PrcntlArray[WhichRows[0], :]
                if 'SPEI_pear_03_nCG' in InpLayersCombination:
                    spei_pearson_03_PrcntlArray = spei_pearson_03_PrcntlArray[WhichRows[0], :]
                if 'SPEI_pear_06_nCG' in InpLayersCombination:
                    spei_pearson_06_PrcntlArray = spei_pearson_06_PrcntlArray[WhichRows[0], :]
                if 'SPEI_pear_09_nCG' in InpLayersCombination:
                    spei_pearson_09_PrcntlArray = spei_pearson_09_PrcntlArray[WhichRows[0], :]
                if 'SPEI_pear_12_nCG' in InpLayersCombination:
                    spei_pearson_12_PrcntlArray = spei_pearson_12_PrcntlArray[WhichRows[0], :]
                if 'SPEI_pear_24_nCG' in InpLayersCombination:
                    spei_pearson_24_PrcntlArray = spei_pearson_24_PrcntlArray[WhichRows[0], :]
                if 'SPEI_pear_36_nCG' in InpLayersCombination:
                    spei_pearson_36_PrcntlArray = spei_pearson_36_PrcntlArray[WhichRows[0], :]
                if 'SPEI_pear_48_nCG' in InpLayersCombination:
                    spei_pearson_48_PrcntlArray = spei_pearson_48_PrcntlArray[WhichRows[0], :]
                if 'SPEI_pear_60_nCG' in InpLayersCombination:
                    spei_pearson_60_PrcntlArray = spei_pearson_60_PrcntlArray[WhichRows[0], :]
                if 'SPEI_pear_72_nCG' in InpLayersCombination:
                    spei_pearson_72_PrcntlArray = spei_pearson_72_PrcntlArray[WhichRows[0], :]
                if 'tavg_01_nCG' in InpLayersCombination:
                    tavg_01_PrcntlArray = tavg_01_PrcntlArray[WhichRows[0], :]
                if 'tmax_01_nCG' in InpLayersCombination:
                    tmax_01_PrcntlArray = tmax_01_PrcntlArray[WhichRows[0], :]
                if 'SNODAS' in InpLayersCombination:
                    SNODAS_PrcntlArray = SNODAS_PrcntlArray[WhichRows[0], :]
                if 'ESA_CCI' in InpLayersCombination:
                    ESA_CCI_PrcntlArray = ESA_CCI_PrcntlArray[WhichRows[0], :]
                if 'IMERG_01' in InpLayersCombination:
                    IMERG_01_PrcntlArray = IMERG_01_PrcntlArray[WhichRows[0], :]
                if 'IMERG_02' in InpLayersCombination:
                    IMERG_02_PrcntlArray = IMERG_02_PrcntlArray[WhichRows[0], :]
                if 'IMERG_03' in InpLayersCombination:
                    IMERG_03_PrcntlArray = IMERG_03_PrcntlArray[WhichRows[0], :]
                if 'IMERG_06' in InpLayersCombination:
                    IMERG_06_PrcntlArray = IMERG_06_PrcntlArray[WhichRows[0], :]
                if 'IMERG_09' in InpLayersCombination:
                    IMERG_09_PrcntlArray = IMERG_09_PrcntlArray[WhichRows[0], :]
                if 'IMERG_12' in InpLayersCombination:
                    IMERG_12_PrcntlArray = IMERG_12_PrcntlArray[WhichRows[0], :]
                if 'IMERG_24' in InpLayersCombination:
                    IMERG_24_PrcntlArray = IMERG_24_PrcntlArray[WhichRows[0], :]
                if 'IMERG_36' in InpLayersCombination:
                    IMERG_36_PrcntlArray = IMERG_36_PrcntlArray[WhichRows[0], :]
                if 'IMERG_48' in InpLayersCombination:
                    IMERG_48_PrcntlArray = IMERG_48_PrcntlArray[WhichRows[0], :]
                if 'IMERG_60' in InpLayersCombination:
                    IMERG_60_PrcntlArray = IMERG_60_PrcntlArray[WhichRows[0], :]
                if 'IMERG_72' in InpLayersCombination:
                    IMERG_72_PrcntlArray = IMERG_72_PrcntlArray[WhichRows[0], :]
                if 'SmNDVI_BlendedVHP' in InpLayersCombination:
                    SmNDVI_BlendedVHP_PrcntlArray = SmNDVI_BlendedVHP_PrcntlArray[WhichRows[0], :]
                if 'TCI_BlendedVHP' in InpLayersCombination:
                    TCI_BlendedVHP_PrcntlArray = TCI_BlendedVHP_PrcntlArray[WhichRows[0], :]
                if 'VCI_BlendedVHP' in InpLayersCombination:
                    VCI_BlendedVHP_PrcntlArray = VCI_BlendedVHP_PrcntlArray[WhichRows[0], :]
                if 'VHI_BlendedVHP' in InpLayersCombination:
                    VHI_BlendedVHP_PrcntlArray = VHI_BlendedVHP_PrcntlArray[WhichRows[0], :]
                if 'GlobSnow3' in InpLayersCombination:
                    GlobSnow3_PrcntlArray = GlobSnow3_PrcntlArray[WhichRows[0], :]
        
            #end of if WhichSeason in ['P', 'U', 'F', 'W']
        
            Target_Array = np.reshape(Target_Array, (Target_Array.size, 1))
        
            Inputs_Mat = np.copy(Target_Array) # REMEMBER to remove this 1st column below
        
            if 'Z_index' in InpLayersCombination:
                ZIndex_PrcntlArray = np.reshape(ZIndex_PrcntlArray, (ZIndex_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, ZIndex_PrcntlArray ), axis = 1)
                del ZIndex_PrcntlArray
            if 'Z_index_60_month' in InpLayersCombination:
                ZIndex60month_PrcntlArray = np.reshape(ZIndex60month_PrcntlArray, (ZIndex60month_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, ZIndex60month_PrcntlArray ), axis = 1)
                del ZIndex60month_PrcntlArray
            if 'PMDI' in InpLayersCombination:
                PMDI_PrcntlArray = np.reshape(PMDI_PrcntlArray, (PMDI_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, PMDI_PrcntlArray ), axis = 1)
                del PMDI_PrcntlArray
            if 'PHDI' in InpLayersCombination:
                PHDI_PrcntlArray = np.reshape(PHDI_PrcntlArray, (PHDI_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, PHDI_PrcntlArray ), axis = 1)
                del PHDI_PrcntlArray
            if 'prcp_01_nCG' in InpLayersCombination:
                prcp_01_PrcntlArray = np.reshape(prcp_01_PrcntlArray, (prcp_01_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_01_PrcntlArray ), axis = 1)
                del prcp_01_PrcntlArray
            if 'prcp_02_nCG' in InpLayersCombination:
                prcp_02_PrcntlArray = np.reshape(prcp_02_PrcntlArray, (prcp_02_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_02_PrcntlArray ), axis = 1)
                del prcp_02_PrcntlArray
            if 'prcp_03_nCG' in InpLayersCombination:
                prcp_03_PrcntlArray = np.reshape(prcp_03_PrcntlArray, (prcp_03_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_03_PrcntlArray ), axis = 1)
                del prcp_03_PrcntlArray
            if 'prcp_06_nCG' in InpLayersCombination:
                prcp_06_PrcntlArray = np.reshape(prcp_06_PrcntlArray, (prcp_06_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_06_PrcntlArray ), axis = 1)
                del prcp_06_PrcntlArray
            if 'prcp_09_nCG' in InpLayersCombination:
                prcp_09_PrcntlArray = np.reshape(prcp_09_PrcntlArray, (prcp_09_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_09_PrcntlArray ), axis = 1)
                del prcp_09_PrcntlArray
            if 'prcp_12_nCG' in InpLayersCombination:
                prcp_12_PrcntlArray = np.reshape(prcp_12_PrcntlArray, (prcp_12_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_12_PrcntlArray ), axis = 1)
                del prcp_12_PrcntlArray
            if 'prcp_24_nCG' in InpLayersCombination:
                prcp_24_PrcntlArray = np.reshape(prcp_24_PrcntlArray, (prcp_24_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_24_PrcntlArray ), axis = 1)
                del prcp_24_PrcntlArray
            if 'prcp_36_nCG' in InpLayersCombination:
                prcp_36_PrcntlArray = np.reshape(prcp_36_PrcntlArray, (prcp_36_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_36_PrcntlArray ), axis = 1)
                del prcp_36_PrcntlArray
            if 'prcp_48_nCG' in InpLayersCombination:
                prcp_48_PrcntlArray = np.reshape(prcp_48_PrcntlArray, (prcp_48_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_48_PrcntlArray ), axis = 1)
                del prcp_48_PrcntlArray
            if 'prcp_60_nCG' in InpLayersCombination:
                prcp_60_PrcntlArray = np.reshape(prcp_60_PrcntlArray, (prcp_60_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_60_PrcntlArray ), axis = 1)
                del prcp_60_PrcntlArray
            if 'prcp_72_nCG' in InpLayersCombination:
                prcp_72_PrcntlArray = np.reshape(prcp_72_PrcntlArray, (prcp_72_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, prcp_72_PrcntlArray ), axis = 1)
                del prcp_72_PrcntlArray
            if 'CPC_soil_moisture' in InpLayersCombination:
                CPCsoilmoist_PrcntlArray = np.reshape(CPCsoilmoist_PrcntlArray, (CPCsoilmoist_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, CPCsoilmoist_PrcntlArray ), axis = 1)
                del CPCsoilmoist_PrcntlArray
            if 'GRACE_DA_gw' in InpLayersCombination:
                GRACE_DA_gw_PrcntlArray = np.reshape(GRACE_DA_gw_PrcntlArray, (GRACE_DA_gw_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, GRACE_DA_gw_PrcntlArray ), axis = 1)
                del GRACE_DA_gw_PrcntlArray
            if 'GRACE_DA_sfsm' in InpLayersCombination:
                GRACE_DA_sfsm_PrcntlArray = np.reshape(GRACE_DA_sfsm_PrcntlArray, (GRACE_DA_sfsm_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, GRACE_DA_sfsm_PrcntlArray ), axis = 1)
                del GRACE_DA_sfsm_PrcntlArray
            if 'GRACE_DA_rtzsm' in InpLayersCombination:
                GRACE_DA_rtzsm_PrcntlArray = np.reshape(GRACE_DA_rtzsm_PrcntlArray, (GRACE_DA_rtzsm_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, GRACE_DA_rtzsm_PrcntlArray ), axis = 1)
                del GRACE_DA_rtzsm_PrcntlArray
            if 'EDDI_1wk' in InpLayersCombination:
                EDDI1wk_PrcntlArray = np.reshape(EDDI1wk_PrcntlArray, (EDDI1wk_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI1wk_PrcntlArray ), axis = 1)
                del EDDI1wk_PrcntlArray
            if 'EDDI_2wk' in InpLayersCombination:
                EDDI2wk_PrcntlArray = np.reshape(EDDI2wk_PrcntlArray, (EDDI2wk_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI2wk_PrcntlArray ), axis = 1)
                del EDDI2wk_PrcntlArray
            if 'EDDI_3wk' in InpLayersCombination:
                EDDI3wk_PrcntlArray = np.reshape(EDDI3wk_PrcntlArray, (EDDI3wk_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI3wk_PrcntlArray ), axis = 1)
                del EDDI3wk_PrcntlArray
            if 'EDDI_4wk' in InpLayersCombination:
                EDDI4wk_PrcntlArray = np.reshape(EDDI4wk_PrcntlArray, (EDDI4wk_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI4wk_PrcntlArray ), axis = 1)
                del EDDI4wk_PrcntlArray
            if 'EDDI_5wk' in InpLayersCombination:
                EDDI5wk_PrcntlArray = np.reshape(EDDI5wk_PrcntlArray, (EDDI5wk_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI5wk_PrcntlArray ), axis = 1)
                del EDDI5wk_PrcntlArray
            if 'EDDI_6wk' in InpLayersCombination:
                EDDI6wk_PrcntlArray = np.reshape(EDDI6wk_PrcntlArray, (EDDI6wk_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI6wk_PrcntlArray ), axis = 1)
                del EDDI6wk_PrcntlArray
            if 'EDDI_7wk' in InpLayersCombination:
                EDDI7wk_PrcntlArray = np.reshape(EDDI7wk_PrcntlArray, (EDDI7wk_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI7wk_PrcntlArray ), axis = 1)
                del EDDI7wk_PrcntlArray
            if 'EDDI_8wk' in InpLayersCombination:
                EDDI8wk_PrcntlArray = np.reshape(EDDI8wk_PrcntlArray, (EDDI8wk_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI8wk_PrcntlArray ), axis = 1)
                del EDDI8wk_PrcntlArray
            if 'EDDI_9wk' in InpLayersCombination:
                EDDI9wk_PrcntlArray = np.reshape(EDDI9wk_PrcntlArray, (EDDI9wk_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI9wk_PrcntlArray ), axis = 1)
                del EDDI9wk_PrcntlArray
            if 'EDDI_10wk' in InpLayersCombination:
                EDDI10wk_PrcntlArray = np.reshape(EDDI10wk_PrcntlArray, (EDDI10wk_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI10wk_PrcntlArray ), axis = 1)
                del EDDI10wk_PrcntlArray
            if 'EDDI_11wk' in InpLayersCombination:
                EDDI11wk_PrcntlArray = np.reshape(EDDI11wk_PrcntlArray, (EDDI11wk_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI11wk_PrcntlArray ), axis = 1)
                del EDDI11wk_PrcntlArray
            if 'EDDI_12wk' in InpLayersCombination:
                EDDI12wk_PrcntlArray = np.reshape(EDDI12wk_PrcntlArray, (EDDI12wk_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI12wk_PrcntlArray ), axis = 1)
                del EDDI12wk_PrcntlArray    
            if 'EDDI_1mn' in InpLayersCombination:
                EDDI1mn_PrcntlArray = np.reshape(EDDI1mn_PrcntlArray, (EDDI1mn_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI1mn_PrcntlArray ), axis = 1)
                del EDDI1mn_PrcntlArray
            if 'EDDI_2mn' in InpLayersCombination:
                EDDI2mn_PrcntlArray = np.reshape(EDDI2mn_PrcntlArray, (EDDI2mn_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI2mn_PrcntlArray ), axis = 1)
                del EDDI2mn_PrcntlArray  
            if 'EDDI_3mn' in InpLayersCombination:
                EDDI3mn_PrcntlArray = np.reshape(EDDI3mn_PrcntlArray, (EDDI3mn_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI3mn_PrcntlArray ), axis = 1)
                del EDDI3mn_PrcntlArray
            if 'EDDI_4mn' in InpLayersCombination:
                EDDI4mn_PrcntlArray = np.reshape(EDDI4mn_PrcntlArray, (EDDI4mn_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI4mn_PrcntlArray ), axis = 1)
                del EDDI4mn_PrcntlArray
            if 'EDDI_5mn' in InpLayersCombination:
                EDDI5mn_PrcntlArray = np.reshape(EDDI5mn_PrcntlArray, (EDDI5mn_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI5mn_PrcntlArray ), axis = 1)
                del EDDI5mn_PrcntlArray
            if 'EDDI_6mn' in InpLayersCombination:
                EDDI6mn_PrcntlArray = np.reshape(EDDI6mn_PrcntlArray, (EDDI6mn_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI6mn_PrcntlArray ), axis = 1)
                del EDDI6mn_PrcntlArray
            if 'EDDI_7mn' in InpLayersCombination:
                EDDI7mn_PrcntlArray = np.reshape(EDDI7mn_PrcntlArray, (EDDI7mn_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI7mn_PrcntlArray ), axis = 1)
                del EDDI7mn_PrcntlArray
            if 'EDDI_8mn' in InpLayersCombination:
                EDDI8mn_PrcntlArray = np.reshape(EDDI8mn_PrcntlArray, (EDDI8mn_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI8mn_PrcntlArray ), axis = 1)
                del EDDI8mn_PrcntlArray
            if 'EDDI_9mn' in InpLayersCombination:
                EDDI9mn_PrcntlArray = np.reshape(EDDI9mn_PrcntlArray, (EDDI9mn_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI9mn_PrcntlArray ), axis = 1)
                del EDDI9mn_PrcntlArray
            if 'EDDI_10mn' in InpLayersCombination:
                EDDI10mn_PrcntlArray = np.reshape(EDDI10mn_PrcntlArray, (EDDI10mn_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI10mn_PrcntlArray ), axis = 1)
                del EDDI10mn_PrcntlArray
            if 'EDDI_11mn' in InpLayersCombination:
                EDDI11mn_PrcntlArray = np.reshape(EDDI11mn_PrcntlArray, (EDDI11mn_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI11mn_PrcntlArray ), axis = 1)
                del EDDI11mn_PrcntlArray
            if 'EDDI_12mn' in InpLayersCombination:
                EDDI12mn_PrcntlArray = np.reshape(EDDI12mn_PrcntlArray, (EDDI12mn_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, EDDI12mn_PrcntlArray ), axis = 1)
                del EDDI12mn_PrcntlArray
            if 'NLDAS2D_1MSM_Mosaic' in InpLayersCombination:
                Mosaic_1MSM_PrcntlArray = np.reshape(Mosaic_1MSM_PrcntlArray, (Mosaic_1MSM_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, Mosaic_1MSM_PrcntlArray ), axis = 1)
                del Mosaic_1MSM_PrcntlArray
            if 'NLDAS2D_1MSM_Noah' in InpLayersCombination:
                Noah_1MSM_PrcntlArray = np.reshape(Noah_1MSM_PrcntlArray, (Noah_1MSM_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, Noah_1MSM_PrcntlArray ), axis = 1)
                del Noah_1MSM_PrcntlArray
            if 'NLDAS2D_1MSM_SAC' in InpLayersCombination:
                SAC_1MSM_PrcntlArray = np.reshape(SAC_1MSM_PrcntlArray, (SAC_1MSM_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, SAC_1MSM_PrcntlArray ), axis = 1)
                del SAC_1MSM_PrcntlArray
            if 'NLDAS2D_1MSM_VIC' in InpLayersCombination:
                VIC_1MSM_PrcntlArray = np.reshape(VIC_1MSM_PrcntlArray, (VIC_1MSM_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, VIC_1MSM_PrcntlArray ), axis = 1)
                del VIC_1MSM_PrcntlArray
            if 'NLDAS2D_TCSM_Mosaic' in InpLayersCombination:
                Mosaic_TCSM_PrcntlArray = np.reshape(Mosaic_TCSM_PrcntlArray, (Mosaic_TCSM_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, Mosaic_TCSM_PrcntlArray ), axis = 1)
                del Mosaic_TCSM_PrcntlArray
            if 'NLDAS2D_TCSM_Noah' in InpLayersCombination:
                Noah_TCSM_PrcntlArray = np.reshape(Noah_TCSM_PrcntlArray, (Noah_TCSM_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, Noah_TCSM_PrcntlArray ), axis = 1)
                del Noah_TCSM_PrcntlArray
            if 'NLDAS2D_TCSM_SAC' in InpLayersCombination:
                SAC_TCSM_PrcntlArray = np.reshape(SAC_TCSM_PrcntlArray, (SAC_TCSM_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, SAC_TCSM_PrcntlArray ), axis = 1)
                del SAC_TCSM_PrcntlArray
            if 'NLDAS2D_TCSM_VIC' in InpLayersCombination:
                VIC_TCSM_PrcntlArray = np.reshape(VIC_TCSM_PrcntlArray, (VIC_TCSM_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, VIC_TCSM_PrcntlArray ), axis = 1)
                del VIC_TCSM_PrcntlArray
            if 'NLDAS2D_EVAP_Mosaic' in InpLayersCombination:
                Mosaic_EVAP_PrcntlArray = np.reshape(Mosaic_EVAP_PrcntlArray, (Mosaic_EVAP_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, Mosaic_EVAP_PrcntlArray ), axis = 1)
                del Mosaic_EVAP_PrcntlArray
            if 'NLDAS2D_EVAP_Noah' in InpLayersCombination:
                Noah_EVAP_PrcntlArray = np.reshape(Noah_EVAP_PrcntlArray, (Noah_EVAP_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, Noah_EVAP_PrcntlArray ), axis = 1)
                del Noah_EVAP_PrcntlArray
            if 'NLDAS2D_EVAP_SAC' in InpLayersCombination:
                SAC_EVAP_PrcntlArray = np.reshape(SAC_EVAP_PrcntlArray, (SAC_EVAP_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, SAC_EVAP_PrcntlArray ), axis = 1)
                del SAC_EVAP_PrcntlArray
            if 'NLDAS2D_EVAP_VIC' in InpLayersCombination:
                VIC_EVAP_PrcntlArray = np.reshape(VIC_EVAP_PrcntlArray, (VIC_EVAP_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, VIC_EVAP_PrcntlArray ), axis = 1)
                del VIC_EVAP_PrcntlArray
            if 'NLDAS2D_SWE_Mosaic' in InpLayersCombination:
                Mosaic_SWE_PrcntlArray = np.reshape(Mosaic_SWE_PrcntlArray, (Mosaic_SWE_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, Mosaic_SWE_PrcntlArray ), axis = 1)
                del Mosaic_SWE_PrcntlArray
            if 'NLDAS2D_SWE_Noah' in InpLayersCombination:
                Noah_SWE_PrcntlArray = np.reshape(Noah_SWE_PrcntlArray, (Noah_SWE_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, Noah_SWE_PrcntlArray ), axis = 1)
                del Noah_SWE_PrcntlArray
            if 'NLDAS2D_SWE_SAC' in InpLayersCombination:
                SAC_SWE_PrcntlArray = np.reshape(SAC_SWE_PrcntlArray, (SAC_SWE_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, SAC_SWE_PrcntlArray ), axis = 1)
                del SAC_SWE_PrcntlArray
            if 'NLDAS2D_SWE_VIC' in InpLayersCombination:
                VIC_SWE_PrcntlArray = np.reshape(VIC_SWE_PrcntlArray, (VIC_SWE_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, VIC_SWE_PrcntlArray ), axis = 1)
                del VIC_SWE_PrcntlArray
            if 'NLDAS2D_RUN_Mosaic' in InpLayersCombination:
                Mosaic_RUN_PrcntlArray = np.reshape(Mosaic_RUN_PrcntlArray, (Mosaic_RUN_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, Mosaic_RUN_PrcntlArray ), axis = 1)
                del Mosaic_RUN_PrcntlArray
            if 'NLDAS2D_RUN_Noah' in InpLayersCombination:
                Noah_RUN_PrcntlArray = np.reshape(Noah_RUN_PrcntlArray, (Noah_RUN_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, Noah_RUN_PrcntlArray ), axis = 1)
                del Noah_RUN_PrcntlArray 
            if 'NLDAS2D_RUN_SAC' in InpLayersCombination:
                SAC_RUN_PrcntlArray = np.reshape(SAC_RUN_PrcntlArray, (SAC_RUN_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, SAC_RUN_PrcntlArray ), axis = 1)
                del SAC_RUN_PrcntlArray
            if 'NLDAS2D_RUN_VIC' in InpLayersCombination:
                VIC_RUN_PrcntlArray = np.reshape(VIC_RUN_PrcntlArray, (VIC_RUN_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, VIC_RUN_PrcntlArray ), axis = 1)
                del VIC_RUN_PrcntlArray
            if 'NLDAS2D_STRMH04_Mosaic' in InpLayersCombination:
                Mosaic_STRM_H04_PrcntlArray = np.reshape(Mosaic_STRM_H04_PrcntlArray, (Mosaic_STRM_H04_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, Mosaic_STRM_H04_PrcntlArray ), axis = 1)
                del Mosaic_STRM_H04_PrcntlArray
            if 'NLDAS2D_STRMH04_Noah' in InpLayersCombination:
                Noah_STRM_H04_PrcntlArray = np.reshape(Noah_STRM_H04_PrcntlArray, (Noah_STRM_H04_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, Noah_STRM_H04_PrcntlArray ), axis = 1)
                del Noah_STRM_H04_PrcntlArray
            if 'NLDAS2D_STRMH04_SAC' in InpLayersCombination:
                SAC_STRM_H04_PrcntlArray = np.reshape(SAC_STRM_H04_PrcntlArray, (SAC_STRM_H04_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, SAC_STRM_H04_PrcntlArray ), axis = 1)
                del SAC_STRM_H04_PrcntlArray
            if 'NLDAS2D_STRMH04_VIC' in InpLayersCombination:
                VIC_STRM_H04_PrcntlArray = np.reshape(VIC_STRM_H04_PrcntlArray, (VIC_STRM_H04_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, VIC_STRM_H04_PrcntlArray ), axis = 1)
                del VIC_STRM_H04_PrcntlArray
            if 'VegDRI' in InpLayersCombination:
                VegDRI_PrcntlArray = np.reshape(VegDRI_PrcntlArray, (VegDRI_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, VegDRI_PrcntlArray ), axis = 1)
                del VegDRI_PrcntlArray
            if 'QuickDRI' in InpLayersCombination:
                QuickDRI_PrcntlArray = np.reshape(QuickDRI_PrcntlArray, (QuickDRI_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, QuickDRI_PrcntlArray ), axis = 1)
                del QuickDRI_PrcntlArray
            if 'ESI_4wk' in InpLayersCombination:
                ESI4Week_PrcntlArray = np.reshape(ESI4Week_PrcntlArray, (ESI4Week_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, ESI4Week_PrcntlArray ), axis = 1)
                del ESI4Week_PrcntlArray
            if 'ESI_12wk' in InpLayersCombination:
                ESI12Week_PrcntlArray = np.reshape(ESI12Week_PrcntlArray, (ESI12Week_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, ESI12Week_PrcntlArray ), axis = 1)
                del ESI12Week_PrcntlArray
            if 'SPI_gamma_01_nCG' in InpLayersCombination:
                spi_gamma_01_PrcntlArray = np.reshape(spi_gamma_01_PrcntlArray, (spi_gamma_01_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_01_PrcntlArray ), axis = 1)
                del spi_gamma_01_PrcntlArray
            if 'SPI_gamma_02_nCG' in InpLayersCombination:
                spi_gamma_02_PrcntlArray = np.reshape(spi_gamma_02_PrcntlArray, (spi_gamma_02_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_02_PrcntlArray ), axis = 1)
                del spi_gamma_02_PrcntlArray
            if 'SPI_gamma_03_nCG' in InpLayersCombination:
                spi_gamma_03_PrcntlArray = np.reshape(spi_gamma_03_PrcntlArray, (spi_gamma_03_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_03_PrcntlArray ), axis = 1)
                del spi_gamma_03_PrcntlArray
            if 'SPI_gamma_06_nCG' in InpLayersCombination:
                spi_gamma_06_PrcntlArray = np.reshape(spi_gamma_06_PrcntlArray, (spi_gamma_06_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_06_PrcntlArray ), axis = 1)
                del spi_gamma_06_PrcntlArray
            if 'SPI_gamma_09_nCG' in InpLayersCombination:
                spi_gamma_09_PrcntlArray = np.reshape(spi_gamma_09_PrcntlArray, (spi_gamma_09_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_09_PrcntlArray ), axis = 1)
                del spi_gamma_09_PrcntlArray
            if 'SPI_gamma_12_nCG' in InpLayersCombination:
                spi_gamma_12_PrcntlArray = np.reshape(spi_gamma_12_PrcntlArray, (spi_gamma_12_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_12_PrcntlArray ), axis = 1)
                del spi_gamma_12_PrcntlArray
            if 'SPI_gamma_24_nCG' in InpLayersCombination:
                spi_gamma_24_PrcntlArray = np.reshape(spi_gamma_24_PrcntlArray, (spi_gamma_24_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_24_PrcntlArray ), axis = 1)
                del spi_gamma_24_PrcntlArray
            if 'SPI_gamma_36_nCG' in InpLayersCombination:
                spi_gamma_36_PrcntlArray = np.reshape(spi_gamma_36_PrcntlArray, (spi_gamma_36_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_36_PrcntlArray ), axis = 1)
                del spi_gamma_36_PrcntlArray
            if 'SPI_gamma_48_nCG' in InpLayersCombination:
                spi_gamma_48_PrcntlArray = np.reshape(spi_gamma_48_PrcntlArray, (spi_gamma_48_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_48_PrcntlArray ), axis = 1)
                del spi_gamma_48_PrcntlArray
            if 'SPI_gamma_60_nCG' in InpLayersCombination:
                spi_gamma_60_PrcntlArray = np.reshape(spi_gamma_60_PrcntlArray, (spi_gamma_60_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_60_PrcntlArray ), axis = 1)
                del spi_gamma_60_PrcntlArray
            if 'SPI_gamma_72_nCG' in InpLayersCombination:
                spi_gamma_72_PrcntlArray = np.reshape(spi_gamma_72_PrcntlArray, (spi_gamma_72_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spi_gamma_72_PrcntlArray ), axis = 1)
                del spi_gamma_72_PrcntlArray
            if 'SPEI_pear_01_nCG' in InpLayersCombination:
                spei_pearson_01_PrcntlArray = np.reshape(spei_pearson_01_PrcntlArray, (spei_pearson_01_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_01_PrcntlArray ), axis = 1)
                del spei_pearson_01_PrcntlArray
            if 'SPEI_pear_02_nCG' in InpLayersCombination:
                spei_pearson_02_PrcntlArray = np.reshape(spei_pearson_02_PrcntlArray, (spei_pearson_02_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_02_PrcntlArray ), axis = 1)
                del spei_pearson_02_PrcntlArray
            if 'SPEI_pear_03_nCG' in InpLayersCombination:
                spei_pearson_03_PrcntlArray = np.reshape(spei_pearson_03_PrcntlArray, (spei_pearson_03_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_03_PrcntlArray ), axis = 1)
                del spei_pearson_03_PrcntlArray
            if 'SPEI_pear_06_nCG' in InpLayersCombination:
                spei_pearson_06_PrcntlArray = np.reshape(spei_pearson_06_PrcntlArray, (spei_pearson_06_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_06_PrcntlArray ), axis = 1)
                del spei_pearson_06_PrcntlArray
            if 'SPEI_pear_09_nCG' in InpLayersCombination:
                spei_pearson_09_PrcntlArray = np.reshape(spei_pearson_09_PrcntlArray, (spei_pearson_09_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_09_PrcntlArray ), axis = 1)
                del spei_pearson_09_PrcntlArray
            if 'SPEI_pear_12_nCG' in InpLayersCombination:
                spei_pearson_12_PrcntlArray = np.reshape(spei_pearson_12_PrcntlArray, (spei_pearson_12_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_12_PrcntlArray ), axis = 1)
                del spei_pearson_12_PrcntlArray
            if 'SPEI_pear_24_nCG' in InpLayersCombination:
                spei_pearson_24_PrcntlArray = np.reshape(spei_pearson_24_PrcntlArray, (spei_pearson_24_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_24_PrcntlArray ), axis = 1)
                del spei_pearson_24_PrcntlArray
            if 'SPEI_pear_36_nCG' in InpLayersCombination:
                spei_pearson_36_PrcntlArray = np.reshape(spei_pearson_36_PrcntlArray, (spei_pearson_36_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_36_PrcntlArray ), axis = 1)
                del spei_pearson_36_PrcntlArray
            if 'SPEI_pear_48_nCG' in InpLayersCombination:
                spei_pearson_48_PrcntlArray = np.reshape(spei_pearson_48_PrcntlArray, (spei_pearson_48_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_48_PrcntlArray ), axis = 1)
                del spei_pearson_48_PrcntlArray
            if 'SPEI_pear_60_nCG' in InpLayersCombination:
                spei_pearson_60_PrcntlArray = np.reshape(spei_pearson_60_PrcntlArray, (spei_pearson_60_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_60_PrcntlArray ), axis = 1)
                del spei_pearson_60_PrcntlArray
            if 'SPEI_pear_72_nCG' in InpLayersCombination:
                spei_pearson_72_PrcntlArray = np.reshape(spei_pearson_72_PrcntlArray, (spei_pearson_72_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, spei_pearson_72_PrcntlArray ), axis = 1)
                del spei_pearson_72_PrcntlArray
            if 'tavg_01_nCG' in InpLayersCombination:
                tavg_01_PrcntlArray = np.reshape(tavg_01_PrcntlArray, (tavg_01_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, tavg_01_PrcntlArray ), axis = 1)
                del tavg_01_PrcntlArray
            if 'tmax_01_nCG' in InpLayersCombination:
                tmax_01_PrcntlArray = np.reshape(tmax_01_PrcntlArray, (tmax_01_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, tmax_01_PrcntlArray ), axis = 1)
                del tmax_01_PrcntlArray
            if 'SNODAS' in InpLayersCombination:
                SNODAS_PrcntlArray = np.reshape(SNODAS_PrcntlArray, (SNODAS_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, SNODAS_PrcntlArray ), axis = 1)
                del SNODAS_PrcntlArray
            if 'ESA_CCI' in InpLayersCombination:
                ESA_CCI_PrcntlArray = np.reshape(ESA_CCI_PrcntlArray, (ESA_CCI_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, ESA_CCI_PrcntlArray ), axis = 1)
                del ESA_CCI_PrcntlArray
            if 'IMERG_01' in InpLayersCombination:
                IMERG_01_PrcntlArray = np.reshape(IMERG_01_PrcntlArray, (IMERG_01_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_01_PrcntlArray ), axis = 1)
                del IMERG_01_PrcntlArray
            if 'IMERG_02' in InpLayersCombination:
                IMERG_02_PrcntlArray = np.reshape(IMERG_02_PrcntlArray, (IMERG_02_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_02_PrcntlArray ), axis = 1)
                del IMERG_02_PrcntlArray
            if 'IMERG_03' in InpLayersCombination:
                IMERG_03_PrcntlArray = np.reshape(IMERG_03_PrcntlArray, (IMERG_03_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_03_PrcntlArray ), axis = 1)
                del IMERG_03_PrcntlArray
            if 'IMERG_06' in InpLayersCombination:
                IMERG_06_PrcntlArray = np.reshape(IMERG_06_PrcntlArray, (IMERG_06_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_06_PrcntlArray ), axis = 1)
                del IMERG_06_PrcntlArray
            if 'IMERG_09' in InpLayersCombination:
                IMERG_09_PrcntlArray = np.reshape(IMERG_09_PrcntlArray, (IMERG_09_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_09_PrcntlArray ), axis = 1)
                del IMERG_09_PrcntlArray
            if 'IMERG_12' in InpLayersCombination:
                IMERG_12_PrcntlArray = np.reshape(IMERG_12_PrcntlArray, (IMERG_12_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_12_PrcntlArray ), axis = 1)
                del IMERG_12_PrcntlArray
            if 'IMERG_24' in InpLayersCombination:
                IMERG_24_PrcntlArray = np.reshape(IMERG_24_PrcntlArray, (IMERG_24_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_24_PrcntlArray ), axis = 1)
                del IMERG_24_PrcntlArray
            if 'IMERG_36' in InpLayersCombination:
                IMERG_36_PrcntlArray = np.reshape(IMERG_36_PrcntlArray, (IMERG_36_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_36_PrcntlArray ), axis = 1)
                del IMERG_36_PrcntlArray
            if 'IMERG_48' in InpLayersCombination:
                IMERG_48_PrcntlArray = np.reshape(IMERG_48_PrcntlArray, (IMERG_48_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_48_PrcntlArray ), axis = 1)
                del IMERG_48_PrcntlArray
            if 'IMERG_60' in InpLayersCombination:
                IMERG_60_PrcntlArray = np.reshape(IMERG_60_PrcntlArray, (IMERG_60_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_60_PrcntlArray ), axis = 1)
                del IMERG_60_PrcntlArray
            if 'IMERG_72' in InpLayersCombination:
                IMERG_72_PrcntlArray = np.reshape(IMERG_72_PrcntlArray, (IMERG_72_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, IMERG_72_PrcntlArray ), axis = 1)
                del IMERG_72_PrcntlArray
            if 'SmNDVI_BlendedVHP' in InpLayersCombination:
                SmNDVI_BlendedVHP_PrcntlArray = np.reshape(SmNDVI_BlendedVHP_PrcntlArray, (SmNDVI_BlendedVHP_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, SmNDVI_BlendedVHP_PrcntlArray ), axis = 1)
                del SmNDVI_BlendedVHP_PrcntlArray
            if 'TCI_BlendedVHP' in InpLayersCombination:
                TCI_BlendedVHP_PrcntlArray = np.reshape(TCI_BlendedVHP_PrcntlArray, (TCI_BlendedVHP_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, TCI_BlendedVHP_PrcntlArray ), axis = 1)
                del TCI_BlendedVHP_PrcntlArray
            if 'VCI_BlendedVHP' in InpLayersCombination:
                VCI_BlendedVHP_PrcntlArray = np.reshape(VCI_BlendedVHP_PrcntlArray, (VCI_BlendedVHP_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, VCI_BlendedVHP_PrcntlArray ), axis = 1)
                del VCI_BlendedVHP_PrcntlArray
            if 'VHI_BlendedVHP' in InpLayersCombination:
                VHI_BlendedVHP_PrcntlArray = np.reshape(VHI_BlendedVHP_PrcntlArray, (VHI_BlendedVHP_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, VHI_BlendedVHP_PrcntlArray ), axis = 1)
                del VHI_BlendedVHP_PrcntlArray
            if 'GlobSnow3' in InpLayersCombination:
                GlobSnow3_PrcntlArray = np.reshape(GlobSnow3_PrcntlArray, (GlobSnow3_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, GlobSnow3_PrcntlArray ), axis = 1)
                del GlobSnow3_PrcntlArray
            #end of if 'Z_index' in InpLayersCombination
        
            Inputs_Mat = Inputs_Mat[:, 1:] # PER 'REMEMBER' comment above

        #  ValidRows = np.where( ~np.isnan(np.sum(Inputs_Mat, axis = 1)) )
        #  Target_Array = Target_Array[ ValidRows[0], :]
        #  Inputs_Mat = Inputs_Mat[ ValidRows[0], :]

            ThisWindowSize = ThisWindowSize + 2

            XX0 = Inputs_Mat[:,0:1]
            YY0 = Target_Array[:,0:1]
            Idxs0 = np.where((~np.isnan(XX0)) & (~np.isnan(YY0)))
            #SamplesForFracI = Inputs_Mat.shape[0]      
            del XX0 
            del YY0
            SamplesForFracI = (Idxs0[0]).shape[0]        
            del Idxs0

        #end of while ((ThisWindowSize <= MaximumWindowSize) and (SamplesForFracI < MinSamplesForFracI))

        del Target_Array_Backup
        if 'Z_index' in InpLayersCombination:
            del ZIndex_PrcntlArray_Backup
        if 'Z_index_60_month' in InpLayersCombination:
            del ZIndex60month_PrcntlArray_Backup
        if 'PMDI' in InpLayersCombination:
            del PMDI_PrcntlArray_Backup
        if 'PHDI' in InpLayersCombination:
            del PHDI_PrcntlArray_Backup
        if 'prcp_01_nCG' in InpLayersCombination:
            del prcp_01_PrcntlArray_Backup
        if 'prcp_02_nCG' in InpLayersCombination:
            del prcp_02_PrcntlArray_Backup
        if 'prcp_03_nCG' in InpLayersCombination:
            del prcp_03_PrcntlArray_Backup
        if 'prcp_06_nCG' in InpLayersCombination:
            del prcp_06_PrcntlArray_Backup
        if 'prcp_09_nCG' in InpLayersCombination:
            del prcp_09_PrcntlArray_Backup
        if 'prcp_12_nCG' in InpLayersCombination:
            del prcp_12_PrcntlArray_Backup
        if 'prcp_24_nCG' in InpLayersCombination:
            del prcp_24_PrcntlArray_Backup
        if 'prcp_36_nCG' in InpLayersCombination:
            del prcp_36_PrcntlArray_Backup
        if 'prcp_48_nCG' in InpLayersCombination:
            del prcp_48_PrcntlArray_Backup
        if 'prcp_60_nCG' in InpLayersCombination:
            del prcp_60_PrcntlArray_Backup
        if 'prcp_72_nCG' in InpLayersCombination:
            del prcp_72_PrcntlArray_Backup
        if 'CPC_soil_moisture' in InpLayersCombination:
            del CPCsoilmoist_PrcntlArray_Backup
        if 'GRACE_DA_gw' in InpLayersCombination:
            del GRACE_DA_gw_PrcntlArray_Backup
        if 'GRACE_DA_sfsm' in InpLayersCombination:
            del GRACE_DA_sfsm_PrcntlArray_Backup
        if 'GRACE_DA_rtzsm' in InpLayersCombination:
            del GRACE_DA_rtzsm_PrcntlArray_Backup
        if 'EDDI_1wk' in InpLayersCombination:
            del EDDI1wk_PrcntlArray_Backup
        if 'EDDI_2wk' in InpLayersCombination:
            del EDDI2wk_PrcntlArray_Backup
        if 'EDDI_3wk' in InpLayersCombination:
            del EDDI3wk_PrcntlArray_Backup
        if 'EDDI_4wk' in InpLayersCombination:
            del EDDI4wk_PrcntlArray_Backup
        if 'EDDI_5wk' in InpLayersCombination:
            del EDDI5wk_PrcntlArray_Backup
        if 'EDDI_6wk' in InpLayersCombination:
            del EDDI6wk_PrcntlArray_Backup
        if 'EDDI_7wk' in InpLayersCombination:
            del EDDI7wk_PrcntlArray_Backup
        if 'EDDI_8wk' in InpLayersCombination:
            del EDDI8wk_PrcntlArray_Backup
        if 'EDDI_9wk' in InpLayersCombination:
            del EDDI9wk_PrcntlArray_Backup
        if 'EDDI_10wk' in InpLayersCombination:
            del EDDI10wk_PrcntlArray_Backup
        if 'EDDI_11wk' in InpLayersCombination:
            del EDDI11wk_PrcntlArray_Backup
        if 'EDDI_12wk' in InpLayersCombination:
            del EDDI12wk_PrcntlArray_Backup
        if 'EDDI_1mn' in InpLayersCombination:
            del EDDI1mn_PrcntlArray_Backup
        if 'EDDI_2mn' in InpLayersCombination:
            del EDDI2mn_PrcntlArray_Backup
        if 'EDDI_3mn' in InpLayersCombination:
            del EDDI3mn_PrcntlArray_Backup
        if 'EDDI_4mn' in InpLayersCombination:
            del EDDI4mn_PrcntlArray_Backup
        if 'EDDI_5mn' in InpLayersCombination:
            del EDDI5mn_PrcntlArray_Backup
        if 'EDDI_6mn' in InpLayersCombination:
            del EDDI6mn_PrcntlArray_Backup
        if 'EDDI_7mn' in InpLayersCombination:
            del EDDI7mn_PrcntlArray_Backup
        if 'EDDI_8mn' in InpLayersCombination:
            del EDDI8mn_PrcntlArray_Backup
        if 'EDDI_9mn' in InpLayersCombination:
            del EDDI9mn_PrcntlArray_Backup
        if 'EDDI_10mn' in InpLayersCombination:
            del EDDI10mn_PrcntlArray_Backup
        if 'EDDI_11mn' in InpLayersCombination:
            del EDDI11mn_PrcntlArray_Backup
        if 'EDDI_12mn' in InpLayersCombination:
            del EDDI12mn_PrcntlArray_Backup
        if 'NLDAS2D_1MSM_Mosaic' in InpLayersCombination:
            del Mosaic_1MSM_PrcntlArray_Backup
        if 'NLDAS2D_1MSM_Noah' in InpLayersCombination:
            del Noah_1MSM_PrcntlArray_Backup
        if 'NLDAS2D_1MSM_SAC' in InpLayersCombination:
            del SAC_1MSM_PrcntlArray_Backup
        if 'NLDAS2D_1MSM_VIC' in InpLayersCombination:
            del VIC_1MSM_PrcntlArray_Backup
        if 'NLDAS2D_TCSM_Mosaic' in InpLayersCombination:
            del Mosaic_TCSM_PrcntlArray_Backup
        if 'NLDAS2D_TCSM_Noah' in InpLayersCombination:
            del Noah_TCSM_PrcntlArray_Backup
        if 'NLDAS2D_TCSM_SAC' in InpLayersCombination:
            del SAC_TCSM_PrcntlArray_Backup
        if 'NLDAS2D_TCSM_VIC' in InpLayersCombination:
            del VIC_TCSM_PrcntlArray_Backup
        if 'NLDAS2D_EVAP_Mosaic' in InpLayersCombination:
            del Mosaic_EVAP_PrcntlArray_Backup
        if 'NLDAS2D_EVAP_Noah' in InpLayersCombination:
            del Noah_EVAP_PrcntlArray_Backup
        if 'NLDAS2D_EVAP_SAC' in InpLayersCombination:
            del SAC_EVAP_PrcntlArray_Backup
        if 'NLDAS2D_EVAP_VIC' in InpLayersCombination:
            del VIC_EVAP_PrcntlArray_Backup
        if 'NLDAS2D_SWE_Mosaic' in InpLayersCombination:
            del Mosaic_SWE_PrcntlArray_Backup
        if 'NLDAS2D_SWE_Noah' in InpLayersCombination:
            del Noah_SWE_PrcntlArray_Backup
        if 'NLDAS2D_SWE_SAC' in InpLayersCombination:
            del SAC_SWE_PrcntlArray_Backup
        if 'NLDAS2D_SWE_VIC' in InpLayersCombination:
            del VIC_SWE_PrcntlArray_Backup
        if 'NLDAS2D_RUN_Mosaic' in InpLayersCombination:
            del Mosaic_RUN_PrcntlArray_Backup
        if 'NLDAS2D_RUN_Noah' in InpLayersCombination:
            del Noah_RUN_PrcntlArray_Backup
        if 'NLDAS2D_RUN_SAC' in InpLayersCombination:
            del SAC_RUN_PrcntlArray_Backup
        if 'NLDAS2D_RUN_VIC' in InpLayersCombination:
            del VIC_RUN_PrcntlArray_Backup
        if 'NLDAS2D_STRMH04_Mosaic' in InpLayersCombination:
            del Mosaic_STRM_H04_PrcntlArray_Backup
        if 'NLDAS2D_STRMH04_Noah' in InpLayersCombination:
            del Noah_STRM_H04_PrcntlArray_Backup
        if 'NLDAS2D_STRMH04_SAC' in InpLayersCombination:
            del SAC_STRM_H04_PrcntlArray_Backup
        if 'NLDAS2D_STRMH04_VIC' in InpLayersCombination:
            del VIC_STRM_H04_PrcntlArray_Backup
        if 'VegDRI' in InpLayersCombination:
            del VegDRI_PrcntlArray_Backup
        if 'QuickDRI' in InpLayersCombination:
            del QuickDRI_PrcntlArray_Backup
        if 'ESI_4wk' in InpLayersCombination:
            del ESI4Week_PrcntlArray_Backup
        if 'ESI_12wk' in InpLayersCombination:
            del ESI12Week_PrcntlArray_Backup
        if 'SPI_gamma_01_nCG' in InpLayersCombination:
            del spi_gamma_01_PrcntlArray_Backup
        if 'SPI_gamma_02_nCG' in InpLayersCombination:
            del spi_gamma_02_PrcntlArray_Backup
        if 'SPI_gamma_03_nCG' in InpLayersCombination:
            del spi_gamma_03_PrcntlArray_Backup
        if 'SPI_gamma_06_nCG' in InpLayersCombination:
            del spi_gamma_06_PrcntlArray_Backup
        if 'SPI_gamma_09_nCG' in InpLayersCombination:
            del spi_gamma_09_PrcntlArray_Backup
        if 'SPI_gamma_12_nCG' in InpLayersCombination:
            del spi_gamma_12_PrcntlArray_Backup
        if 'SPI_gamma_24_nCG' in InpLayersCombination:
            del spi_gamma_24_PrcntlArray_Backup
        if 'SPI_gamma_36_nCG' in InpLayersCombination:
            del spi_gamma_36_PrcntlArray_Backup
        if 'SPI_gamma_48_nCG' in InpLayersCombination:
            del spi_gamma_48_PrcntlArray_Backup
        if 'SPI_gamma_60_nCG' in InpLayersCombination:
            del spi_gamma_60_PrcntlArray_Backup
        if 'SPI_gamma_72_nCG' in InpLayersCombination:
            del spi_gamma_72_PrcntlArray_Backup
        if 'SPEI_pear_01_nCG' in InpLayersCombination:
            del spei_pearson_01_PrcntlArray_Backup
        if 'SPEI_pear_02_nCG' in InpLayersCombination:
            del spei_pearson_02_PrcntlArray_Backup
        if 'SPEI_pear_03_nCG' in InpLayersCombination:
            del spei_pearson_03_PrcntlArray_Backup
        if 'SPEI_pear_06_nCG' in InpLayersCombination:
            del spei_pearson_06_PrcntlArray_Backup
        if 'SPEI_pear_09_nCG' in InpLayersCombination:
            del spei_pearson_09_PrcntlArray_Backup
        if 'SPEI_pear_12_nCG' in InpLayersCombination:
            del spei_pearson_12_PrcntlArray_Backup
        if 'SPEI_pear_24_nCG' in InpLayersCombination:
            del spei_pearson_24_PrcntlArray_Backup
        if 'SPEI_pear_36_nCG' in InpLayersCombination:
            del spei_pearson_36_PrcntlArray_Backup
        if 'SPEI_pear_48_nCG' in InpLayersCombination:
            del spei_pearson_48_PrcntlArray_Backup
        if 'SPEI_pear_60_nCG' in InpLayersCombination:
            del spei_pearson_60_PrcntlArray_Backup
        if 'SPEI_pear_72_nCG' in InpLayersCombination:
            del spei_pearson_72_PrcntlArray_Backup
        if 'tavg_01_nCG' in InpLayersCombination:
            del tavg_01_PrcntlArray_Backup
        if 'tmax_01_nCG' in InpLayersCombination:
            del tmax_01_PrcntlArray_Backup
        if 'SNODAS' in InpLayersCombination:
            del SNODAS_PrcntlArray_Backup
        if 'ESA_CCI' in InpLayersCombination:
            del ESA_CCI_PrcntlArray_Backup
        if 'IMERG_01' in InpLayersCombination:
            del IMERG_01_PrcntlArray_Backup
        if 'IMERG_02' in InpLayersCombination:
            del IMERG_02_PrcntlArray_Backup
        if 'IMERG_03' in InpLayersCombination:
            del IMERG_03_PrcntlArray_Backup
        if 'IMERG_06' in InpLayersCombination:
            del IMERG_06_PrcntlArray_Backup
        if 'IMERG_09' in InpLayersCombination:
            del IMERG_09_PrcntlArray_Backup
        if 'IMERG_12' in InpLayersCombination:
            del IMERG_12_PrcntlArray_Backup
        if 'IMERG_24' in InpLayersCombination:
            del IMERG_24_PrcntlArray_Backup
        if 'IMERG_36' in InpLayersCombination:
            del IMERG_36_PrcntlArray_Backup
        if 'IMERG_48' in InpLayersCombination:
            del IMERG_48_PrcntlArray_Backup
        if 'IMERG_60' in InpLayersCombination:
            del IMERG_60_PrcntlArray_Backup
        if 'IMERG_72' in InpLayersCombination:
            del IMERG_72_PrcntlArray_Backup
        if 'SmNDVI_BlendedVHP' in InpLayersCombination:
            del SmNDVI_BlendedVHP_PrcntlArray_Backup
        if 'TCI_BlendedVHP' in InpLayersCombination:
            del TCI_BlendedVHP_PrcntlArray_Backup
        if 'VCI_BlendedVHP' in InpLayersCombination:
            del VCI_BlendedVHP_PrcntlArray_Backup
        if 'VHI_BlendedVHP' in InpLayersCombination:
            del VHI_BlendedVHP_PrcntlArray_Backup
        if 'GlobSnow3' in InpLayersCombination:
            del GlobSnow3_PrcntlArray_Backup

        if WhichSeason in ['P', 'U', 'F', 'W']:
            del WhichRows

        return Target_Array, Inputs_Mat, ThisWindowSize_prev

    #end of def GetInpAndTargArraysFromFile_ClmGrd1D(XYDatas, InpLayersCombination, IfMakeTargetBinary, IfIncludeD0AsDrought, WhichSeason, MinimumWindowSize, MaximumWindowSize, MinSamplesForFracI, ThisPxlRow, ThisPxlCol, PxlRow_SortedArr_FrmShpFile, PxlCol_SortedArr_FrmShpFile)

    All_Target_Array, All_Inputs_Mat, WindowSize_prev = GetInpAndTargArraysFromFile_ClmGrd1D(SingleUnifiedDatas, InpLayersCombination, IfMakeTargetBinary, IfIncludeD0AsDrought, WhichSeason, MinimumWindowSize, MaximumWindowSize, MinSamplesForFracI, ThisPxlRow, ThisPxlCol, PxlRow_SortedArr_FrmShpFile, PxlCol_SortedArr_FrmShpFile)

    del PxlRow_SortedArr_FrmShpFile 
    del PxlCol_SortedArr_FrmShpFile 
    del SingleUnifiedDatas

    ##All_Target_Array = All_Target_Array[:, 0]

    print("All_Inputs_Mat.shape is ", All_Inputs_Mat.shape)
    print("All_Target_Array.shape is ", All_Target_Array.shape)
    print("np.unique(All_Target_Array) is ", np.unique(All_Target_Array))

    #SY: Begin portion commented now and only partially moved further above
    #ColCombinations = np.loadtxt('Combinations' + NumInpsForNDFracMI + 'of' + str(NumInpLayers) + '.txt', dtype = 'int', ndmin = 2)
    #SelectCols = ColCombinations[WhichInpCombinForNDFracMI, :]
    #SelectCols = SelectCols - 1
    #All_Inputs_Mat = All_Inputs_Mat[:, SelectCols] 
    #SY: End portion commented now and only partially moved further above

    def calc_MI_info(Inp_name_key, Targ_name_key, Inp_array_key, Targ_array_key, If_discrete_features_key, Num_random_states_key, n_neighbors_key, Inp_names_list_key, MI_values_list_key, MI_lowersofrange_list_key, MI_uppersofrange_list_key, MI_ranges_list_key, sample_sizes_list_key, Entropy_list_key, RelMI_values_list_key, RelMI_lowersofrange_list_key, RelMI_uppersofrange_list_key):
        XX = Inp_array_key[:,0:1]
        YY = Targ_array_key[:,0:1]
        Idxs = np.where((~np.isnan(XX)) & (~np.isnan(YY)))
        Percentiles_for_n_neighbors = np.empty((3,), dtype=np.float32)
        Percentiles_for_n_neighbors[:] = np.NaN
        if len(Idxs[0]) > 0:
            XX = XX[Idxs[0]]
            YY = YY[Idxs[0]]
            YY = YY[:,0]
            MIs_this_n_neighbors = np.empty((Num_random_states_key,), dtype=np.float32)
            MIs_this_n_neighbors[:] = np.NaN
            for Which_Random_state_value in range(Num_random_states_key):
                Random_state_value = 3 + Which_Random_state_value*100
                MIs_this_n_neighbors[Which_Random_state_value] = mutual_info_classif(XX,YY,discrete_features=If_discrete_features_key, n_neighbors=n_neighbors_key, copy=True, random_state = Random_state_value)
            del XX 
            Percentiles_for_n_neighbors[0] = np.percentile(MIs_this_n_neighbors, 5)
            Percentiles_for_n_neighbors[1] = np.percentile(MIs_this_n_neighbors, 50)
            Percentiles_for_n_neighbors[2] = np.percentile(MIs_this_n_neighbors, 95)
            print(Inp_name_key,": median MI ", Percentiles_for_n_neighbors[1], ", MI 90-perc range ",Percentiles_for_n_neighbors[2]-Percentiles_for_n_neighbors[0], ", sample size ", YY.size)
            Unique_YY_values, unique_counts = np.unique(YY, return_counts=True)
            del Unique_YY_values
            YY_probabs = unique_counts / sum(unique_counts)
            del unique_counts
            Entropyy = entropy(YY_probabs)
            del YY_probabs
            if Entropyy == 0.0:
                Percentiles_for_n_neighbors[0] = 0.0
                Percentiles_for_n_neighbors[1] = 0.0
                Percentiles_for_n_neighbors[2] = 0.0
            #end of if Entropyy == 0.0
            MI_ranges_list_key.append(Percentiles_for_n_neighbors[2]-Percentiles_for_n_neighbors[0])
            sample_sizes_list_key.append(YY.size)
            del YY
            RelMI_values_list_key.append(Percentiles_for_n_neighbors[1]/Entropyy)
            RelMI_lowersofrange_list_key.append(Percentiles_for_n_neighbors[0]/Entropyy)
            RelMI_uppersofrange_list_key.append(Percentiles_for_n_neighbors[2]/Entropyy)
        else: # if len(Idxs[0]) > 0
            MI_ranges_list_key.append(np.NaN)
            sample_sizes_list_key.append(0.0)
            Entropyy = np.copy(np.NaN)
            RelMI_values_list_key.append(np.NaN)
            RelMI_lowersofrange_list_key.append(np.NaN)
            RelMI_uppersofrange_list_key.append(np.NaN)
        #end of if len(Idxs[0]) > 0
        del Idxs
        Inp_names_list_key.append(Inp_name_key)
        MI_values_list_key.append(Percentiles_for_n_neighbors[1])
        MI_lowersofrange_list_key.append(Percentiles_for_n_neighbors[0])
        MI_uppersofrange_list_key.append(Percentiles_for_n_neighbors[2])
        Entropy_list_key.append(Entropyy)

        return Inp_names_list_key, MI_values_list_key, MI_lowersofrange_list_key, MI_uppersofrange_list_key, MI_ranges_list_key, sample_sizes_list_key, Entropy_list_key, RelMI_values_list_key, RelMI_lowersofrange_list_key, RelMI_uppersofrange_list_key
    #end of def calc_MI_info

    def calc_MI_1ValueForMultiFeatures(Inp_array_key, Targ_array_key, If_discrete_features_key, Num_random_states_key, n_neighbors_key):
        XX = np.copy(Inp_array_key)
        YY = Targ_array_key[:,0:1]
    #  Idxs = np.where((~np.isnan(XX)) & (~np.isnan(YY)))
        Idxs = np.where( ( np.reshape(np.all( ~np.isnan(XX) & ~np.isnan(YY), axis = 1 ), (-1, 1)) ) )
        XX = XX[Idxs[0]]
        YY = YY[Idxs[0]]
        del Idxs
        YY = YY[:,0]
        Percentiles_for_n_neighbors = np.empty((3,), dtype=np.float32)
        Percentiles_for_n_neighbors[:] = np.NaN
        MIs_this_n_neighbors = np.empty((Num_random_states_key,), dtype=np.float32)
        MIs_this_n_neighbors[:] = np.NaN
        for Which_Random_state_value in range(Num_random_states_key):
            Random_state_value = 3 + Which_Random_state_value*100
    #        MIs_this_n_neighbors[Which_Random_state_value] = mutual_info_classif(XX,YY,discrete_features=If_discrete_features_key, n_neighbors=n_neighbors_key, copy=True, random_state = Random_state_value)
            MIs_this_n_neighbors[Which_Random_state_value] = MI_classif_1ValueForMultiFeatures(XX,YY,discrete_features=If_discrete_features_key, n_neighbors=n_neighbors_key, copy=True, random_state = Random_state_value)
        del XX
        Percentiles_for_n_neighbors[0] = np.percentile(MIs_this_n_neighbors, 5)
        Percentiles_for_n_neighbors[1] = np.percentile(MIs_this_n_neighbors, 50)
        Percentiles_for_n_neighbors[2] = np.percentile(MIs_this_n_neighbors, 95)
        print("All-features-together : median MI ", Percentiles_for_n_neighbors[1], ", MI 90-perc range ",Percentiles_for_n_neighbors[2]-Percentiles_for_n_neighbors[0], ", sample size ", YY.size)
        Unique_YY_values, unique_counts = np.unique(YY, return_counts=True)
        del Unique_YY_values
        YY_probabs = unique_counts / sum(unique_counts)
        del unique_counts
        Entropyy = entropy(YY_probabs)
        del YY_probabs
        if Entropyy == 0.0:
            Percentiles_for_n_neighbors[0] = 0.0
            Percentiles_for_n_neighbors[1] = 0.0
            Percentiles_for_n_neighbors[2] = 0.0
        #end of if Entropyy == 0.0
        MI_value = Percentiles_for_n_neighbors[1]
        MI_lowerofrange = Percentiles_for_n_neighbors[0]
        MI_upperofrange = Percentiles_for_n_neighbors[2]
        MI_range = Percentiles_for_n_neighbors[2]-Percentiles_for_n_neighbors[0]
        sample_size = YY.size
        del YY
        RelMI_value = Percentiles_for_n_neighbors[1]/Entropyy
        RelMI_lowerofrange = Percentiles_for_n_neighbors[0]/Entropyy
        RelMI_upperofrange = Percentiles_for_n_neighbors[2]/Entropyy

        print ('MI_value is ',MI_value)
        print ('MI_lowerofrange is ',MI_lowerofrange)
        print ('MI_upperofrange is ',MI_upperofrange)
        print ('MI_range is ',MI_range)
        print ('sample_size is ',sample_size)
        print ('Entropyy is ',Entropyy)
        print ('RelMI_value is ',RelMI_value)
        print ('RelMI_lowerofrange is ',RelMI_lowerofrange)
        print ('RelMI_upperofrange is ',RelMI_upperofrange)

        return MI_value, MI_lowerofrange, MI_upperofrange, MI_range, sample_size, Entropyy, RelMI_value, RelMI_lowerofrange, RelMI_upperofrange
    #end of def calc_MI_1ValueForMultiFeatures

    #Inp_names_list = []

    if SelectCols.size == 1:

        Inp_names_list = []
        MI_values_list = []
        MI_lowersofrange_list = []
        MI_uppersofrange_list = []
        MI_ranges_list = []
        sample_sizes_list = []
        Entropy_list = []
        RelMI_values_list = []
        RelMI_lowersofrange_list = []
        RelMI_uppersofrange_list = []

        Inp_names_list, MI_values_list, MI_lowersofrange_list, MI_uppersofrange_list, MI_ranges_list, sample_sizes_list, Entropy_list, RelMI_values_list, RelMI_lowersofrange_list, RelMI_uppersofrange_list = calc_MI_info(Inp_name_key = DictofNumNamePairs_Channels[SelectCols[0]+1], Targ_name_key = TargetVariable, Inp_array_key = All_Inputs_Mat, Targ_array_key = All_Target_Array, If_discrete_features_key = False, Num_random_states_key = Num_random_states, n_neighbors_key = n_neighbors, Inp_names_list_key = Inp_names_list, MI_values_list_key = MI_values_list, MI_lowersofrange_list_key = MI_lowersofrange_list, MI_uppersofrange_list_key = MI_uppersofrange_list, MI_ranges_list_key = MI_ranges_list, sample_sizes_list_key = sample_sizes_list, Entropy_list_key = Entropy_list, RelMI_values_list_key = RelMI_values_list, RelMI_lowersofrange_list_key = RelMI_lowersofrange_list, RelMI_uppersofrange_list_key = RelMI_uppersofrange_list)

    #  print ('Inp_names_list is ',Inp_names_list)
        print ('MI_values_list is ',MI_values_list)
        print ('MI_lowersofrange_list is ',MI_lowersofrange_list)
        print ('MI_uppersofrange_list is ',MI_uppersofrange_list)
        print ('MI_ranges_list is ',MI_ranges_list)
    #  print ('sample_sizes_list is ',sample_sizes_list)
    #  print('len(MI_values_list) is ',len(MI_values_list))
        print ('Entropy_list is ',Entropy_list)
        print ('RelMI_values_list is ',RelMI_values_list)
        print ('RelMI_lowersofrange_list is ',RelMI_lowersofrange_list)
        print ('RelMI_uppersofrange_list is ',RelMI_uppersofrange_list)

        RelMI_value = RelMI_values_list[0]
        sample_size = sample_sizes_list[0]

    else: # else of if SelectCols.size == 1

    #SY: Begin portion commented now and only partially moved further above
    #  if NumInpLayers >= 0:
    #        for ii in range(SelectCols.size):
    #            Inp_names_list.append(DictofNumNamePairs_Channels[SelectCols[ii]+1])
    #        print ('Inp_names_list is ',Inp_names_list)
    #  else:
    #        print ('Inp_names_list is ', InpLayersCombination)
    #SY: End portion commented now and only partially moved further above

        MI_value, MI_lowerofrange, MI_upperofrange, MI_range, sample_size, Entropyy, RelMI_value, RelMI_lowerofrange, RelMI_upperofrange = calc_MI_1ValueForMultiFeatures(Inp_array_key = All_Inputs_Mat, Targ_array_key = All_Target_Array, If_discrete_features_key = False, Num_random_states_key = Num_random_states, n_neighbors_key = n_neighbors)

    #end of if SelectCols.size == 1

    del All_Target_Array 
    del All_Inputs_Mat

    # ------------------------------------------
    # TODO: THIS WE WILL MERGE INTO A SINGLE FILE

    RelMI_value = np.array([RelMI_value], dtype=np.float32)
    np.savetxt(FracI_ClmGrd1D_AllValid_NDFeat_FileName, RelMI_value)

    sample_size = np.array([sample_size], dtype=np.float32)
    np.savetxt(SampSiz_ClmGrd1D_AllValid_NDFeat_FileName, sample_size)

    WindowSize_prev = np.array([WindowSize_prev], dtype=np.float32)
    np.savetxt(WindowSiz_ClmGrd1D_AllValid_NDFeat_FileName, WindowSize_prev)

    # TODO: THIS WE WILL MERGE INTO A SINGLE FILE
    # ------------------------------------------

    eeend_Overall = datetime.now()
    eeelapsed_Overall = eeend_Overall - ssstart_Overall

    print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")

    print("End time", time.time())
    return

if __name__ == "__main__":
    main()
