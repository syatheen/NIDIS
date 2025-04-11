# Coded by Soni Yatheendradas
#          on Dec 9, 2022
# Modified by Jordan A. Caraballo-Vega
#          on April 15, 2024
# Updated by Soni Yatheendradas
#          on Dec 28, 2024

from __future__ import division

import os
import sys
import copy
import time
import logging
import numpy as np
import geopandas as gpd

from pathlib import Path
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
    WhichSeason, # Choices are 'P' for sPring (Mar-May), 'U' for sUmmer (Jun-Aug), 'F' for Fall (Sep-Nov), 'W' for Winter (Dec-Feb), 'A' for all-seasons-together
    OutputDir
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
    OutputDir = sys.argv[12]
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

    # Addition for better processing, do not process
    # if output file already exists, this is not elegant,
    # but is a quick fix based on the current time limitations
    if SpatialDomain in ['CONUS']:
        if TargetVariable == 'USDM':
            TargetVariable_ShortStr = 'U'
            SpatialDomain_ShortStr = 'C'
        else:
            TargetVariable_ShortStr = ''
            SpatialDomain_ShortStr = ''

    # set filename name
    FracI_ClmGrd1D_AllValid_NDFeat_FileName = \
        'FI1X1_ClmGrd1D_V2b_New/' + NumInpsForNDFracMI + '/' + IfMakeTargetBinary + \
        IfIncludeD0AsDrought + '_' + TargetVariable_ShortStr + '_' + \
        SpatialDomain_ShortStr + '_' + str(Which_1D_Pixel)
    if NumInpLayers >= 0:
        FracI_ClmGrd1D_AllValid_NDFeat_FileName = \
            FracI_ClmGrd1D_AllValid_NDFeat_FileName + '_In' + str(NumInpLayers)
    elif NumInpLayers < 0:
        FracI_ClmGrd1D_AllValid_NDFeat_FileName = \
            FracI_ClmGrd1D_AllValid_NDFeat_FileName + '_InM' + str(-NumInpLayers)

    FracI_ClmGrd1D_AllValid_NDFeat_FileName = \
        FracI_ClmGrd1D_AllValid_NDFeat_FileName + '_' + \
        str(WhichInpCombinForNDFracMI) + '_' + WhichSeason + '.txt'

    # filename for the final output of this function
    OutputArrayFilename = os.path.join(
        OutputDir,
        f'{Path(FracI_ClmGrd1D_AllValid_NDFeat_FileName).stem}.txt'
    )
    if os.path.exists(OutputArrayFilename):
        logging.info(f'Skipping, filename already exists: {OutputArrayFilename}')
        return

    ClimGrid1DShpFile = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/nClimGrid_as_poly_NoNans.shp'

    print("Defined ClimGrid1DShpFile filename")

    MinimumWindowSize = 1
    #MaximumWindowSize = 35
    MaximumWindowSize = 1
    #MinSamplesForFracI = 100
    MinSamplesForFracI = 6

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
    # TODO: this needs its own flexible path
    if NumInpLayers >= 0:
        ColCombinations = np.loadtxt(
            os.path.join(
              ##'/discover/nobackup/projects/nca/jacaraba/NIDIS_Runs/Inputs',
              '/discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS',
              'Combinations' + NumInpsForNDFracMI + 'of' + str(NumInpLayers) + '.txt'
            ),
            dtype='int',
            ndmin=2
        )
    else: #of if NumInpLayers >= 0:
        ColCombinations = np.loadtxt(
            os.path.join(
              ##'/discover/nobackup/projects/nca/jacaraba/NIDIS_Runs/Inputs',
              '/discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS',
              'Combinations' + NumInpsForNDFracMI + 'of' + str(NumInpsForNDFracMI) + '.txt'
            ),
            dtype='int',
            ndmin=2
        )
    #end of if NumInpLayers >= 0:
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

            # data generated by Jordan and Soni respectively
            temp_path_npz_Soni = '/discover/nobackup/syatheen/Sujay/DeepLearning/ExampleTries/NIDIS'
            temp_path2_npz_Soni = '/discover/nobackup/projects/nca/syatheen/NIDIS_Data'
            temp_path_npz_Jordan = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data'

            NameKeys_FilenameValues = ( (('Target',), f'/discover/nobackup/projects/nca/syatheen/USDM/InfoArrsBatchFrmWeekly_New_20000104To20220621.npz'),  
                                        (('Z_index', 
                                          'Z_index_60_month'), f'{temp_path_npz_Jordan}/Indicators_1_to_4/percentile_output/PreppedTrainNEvalNpzs/indicators_1_to_2/SingleUnified_20060103To20191231.npz'),
                                        (('PMDI', 
                                          'PHDI'), f'{temp_path2_npz_Soni}/Indicators_1_to_4/percentile_output/PreppedTrainNEvalNpzs/indicators_3_to_4/SingleUnified_Corr2OverallPerc_20060103To20191231.npz'),
                                        (('prcp_01_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_prcp_01_20060103To20191231.npz'),
                                        (('prcp_02_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_prcp_02_20060103To20191231.npz'),
                                        (('prcp_03_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_prcp_03_20060103To20191231.npz'),
                                        (('prcp_06_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_prcp_06_20060103To20191231.npz'),
                                        (('prcp_09_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_prcp_09_20060103To20191231.npz'),
                                        (('prcp_12_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_prcp_12_20060103To20191231.npz'),
                                        (('prcp_24_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_prcp_24_20060103To20191231.npz'),
                                        (('prcp_36_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_prcp_36_20060103To20191231.npz'),
                                        (('prcp_48_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_prcp_48_20060103To20191231.npz'),
                                        (('prcp_60_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_prcp_60_20060103To20191231.npz'),
                                        (('prcp_72_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_prcp_72_20060103To20191231.npz'),
                                        (('CPC_soil_moisture',), f'{temp_path_npz_Jordan}/Indicator_16/percentile_creation/PreppedTrainNEvalNpzs/SingleUnified_20060103To20191231.npz'),
                                        (('GRACE_DA_gw',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_GRACEDA_20060103To20191231.npz'),
                                        (('GRACE_DA_sfsm', 
                                          'GRACE_DA_rtzsm'), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_GRACEDA_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_1wk',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI01wk_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_2wk',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI02wk_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_3wk',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI03wk_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_4wk',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI04wk_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_5wk',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI05wk_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_6wk',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI06wk_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_7wk',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI07wk_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_8wk',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI08wk_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_9wk',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI09wk_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_10wk',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI10wk_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_11wk',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI11wk_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_12wk',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI12wk_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_1mn',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI01mn_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_2mn',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI02mn_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_3mn',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI03mn_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_4mn',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI04mn_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_5mn',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI05mn_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_6mn',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI06mn_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_7mn',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI07mn_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_8mn',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI08mn_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_9mn',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI09mn_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_10mn',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI10mn_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_11mn',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI11mn_Corr2MonthlyPerc_20060103To20191231.npz'),
                                        (('EDDI_12mn',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_EDDI12mn_20060103To20191231.npz'),
                                        (('NLDAS2D_1MSM_Mosaic',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_Mosaic_1MSM_Crr2MnthlyPrc_20060103To20191231.npz'),
                                        (('NLDAS2D_1MSM_Noah',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_Noah_1MSM_Crr2MnthlyPrc_20060103To20191231.npz'),
                                        (('NLDAS2D_1MSM_SAC',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_SAC_1MSM_Crr2MnthlyPrc_20060103To20191231.npz'),
                                        (('NLDAS2D_1MSM_VIC',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_VIC_1MSM_Crr2MnthlyPrc_20060103To20191231.npz'),
                                        (('NLDAS2D_TCSM_Mosaic',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_Mosaic_TCSM_Crr2MnthlyPrc_20060103To20191231.npz'),
                                        (('NLDAS2D_TCSM_Noah',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_Noah_TCSM_Crr2MnthlyPrc_20060103To20191231.npz'),
                                        (('NLDAS2D_TCSM_SAC',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_SAC_TCSM_Crr2MnthlyPrc_20060103To20191231.npz'),
                                        (('NLDAS2D_TCSM_VIC',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_VIC_TCSM_Crr2MnthlyPrc_20060103To20191231.npz'),
                                        (('NLDAS2D_EVAP_Mosaic',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_Mosaic_EVAP_Crr2MnthlyPrc_20060103To20191231.npz'),
                                        (('NLDAS2D_EVAP_Noah',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_Noah_EVAP_Crr2MnthlyPrc_20060103To20191231.npz'),
                                        (('NLDAS2D_EVAP_SAC',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_SAC_EVAP_Crr2MnthlyPrc_20060103To20191231.npz'),
                                        (('NLDAS2D_EVAP_VIC',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_VIC_EVAP_Crr2MnthlyPrc_20060103To20191231.npz'),
                                        (('NLDAS2D_SWE_Mosaic',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_Mosaic_SWE_20060103To20191231.npz'),
                                        (('NLDAS2D_SWE_Noah',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_Noah_SWE_20060103To20191231.npz'),
                                        (('NLDAS2D_SWE_SAC',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_SAC_SWE_20060103To20191231.npz'),
                                        (('NLDAS2D_SWE_VIC',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_VIC_SWE_20060103To20191231.npz'),
                                        (('NLDAS2D_RUN_Mosaic',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_Mosaic_RUN_20060103To20191231.npz'),
                                        (('NLDAS2D_RUN_Noah',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_Noah_RUN_20060103To20191231.npz'),
                                        (('NLDAS2D_RUN_SAC',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_SAC_RUN_20060103To20191231.npz'),
                                        (('NLDAS2D_RUN_VIC',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_VIC_RUN_20060103To20191231.npz'),
                                        (('NLDAS2D_STRMH04_Mosaic',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_Mosaic_STRM_H04_20060103To20191231.npz'),
                                        (('NLDAS2D_STRMH04_Noah',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_Noah_STRM_H04_20060103To20191231.npz'),
                                        (('NLDAS2D_STRMH04_SAC',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_SAC_STRM_H04_20060103To20191231.npz'),
                                        (('NLDAS2D_STRMH04_VIC',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_NLDAS_2_dly_VIC_STRM_H04_20060103To20191231.npz'),
                                        (('VegDRI',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_VegDRI_20060103To20191231.npz'),
                                        (('QuickDRI',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_QuickDRI_20060103To20191231.npz'),
                                        (('ESI_4wk',
                                          'ESI_12wk'), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_ESImultiWeek_MonthlyPerc_20060103To20191231.npz'),
                                        (('SPI_gamma_01_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spi_gamma_01_20060103To20191231.npz'),
                                        (('SPI_gamma_02_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spi_gamma_02_20060103To20191231.npz'),
                                        (('SPI_gamma_03_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spi_gamma_03_20060103To20191231.npz'),
                                        (('SPI_gamma_06_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spi_gamma_06_20060103To20191231.npz'),
                                        (('SPI_gamma_09_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spi_gamma_09_20060103To20191231.npz'),
                                        (('SPI_gamma_12_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spi_gamma_12_20060103To20191231.npz'),
                                        (('SPI_gamma_24_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spi_gamma_24_20060103To20191231.npz'),
                                        (('SPI_gamma_36_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spi_gamma_36_20060103To20191231.npz'),
                                        (('SPI_gamma_48_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spi_gamma_48_20060103To20191231.npz'),
                                        (('SPI_gamma_60_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spi_gamma_60_20060103To20191231.npz'),
                                        (('SPI_gamma_72_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spi_gamma_72_20060103To20191231.npz'),
                                        (('SPEI_pear_01_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spei_pearson_01_20060103To20191231.npz'),
                                        (('SPEI_pear_02_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spei_pearson_02_20060103To20191231.npz'),
                                        (('SPEI_pear_03_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spei_pearson_03_20060103To20191231.npz'),
                                        (('SPEI_pear_06_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spei_pearson_06_20060103To20191231.npz'),
                                        (('SPEI_pear_09_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spei_pearson_09_20060103To20191231.npz'),
                                        (('SPEI_pear_12_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spei_pearson_12_20060103To20191231.npz'),
                                        (('SPEI_pear_24_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spei_pearson_24_20060103To20191231.npz'),
                                        (('SPEI_pear_36_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spei_pearson_36_20060103To20191231.npz'),
                                        (('SPEI_pear_48_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spei_pearson_48_20060103To20191231.npz'),
                                        (('SPEI_pear_60_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spei_pearson_60_20060103To20191231.npz'),
                                        (('SPEI_pear_72_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_spei_pearson_72_20060103To20191231.npz'),
                                        (('tavg_01_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_tavg_01_20060103To20191231.npz'),
                                        (('tmax_01_nCG',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_nCG_tmax_01_20060103To20191231.npz'),
                                        (('SNODAS',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_SNODAS_20060103To20191231.npz'),
                                        (('ESA_CCI',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_ESA_CCI_20060103To20191231.npz'),
                                        (('IMERG_01',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG1Month_20060103To20191231.npz'),
                                        (('IMERG_02',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG2Month_20060103To20191231.npz'),
                                        (('IMERG_03',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG3Month_20060103To20191231.npz'),
                                        (('IMERG_06',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG6Month_20060103To20191231.npz'),
                                        (('IMERG_09',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG9Month_20060103To20191231.npz'),
                                        (('IMERG_12',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG12Month_20060103To20191231.npz'),
                                        (('IMERG_24',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG24Month_20060103To20191231.npz'),
                                        (('IMERG_36',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG36Month_20060103To20191231.npz'),
                                        (('IMERG_48',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG48Month_20060103To20191231.npz'),
                                        (('IMERG_60',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG60Month_20060103To20191231.npz'),
                                        (('IMERG_72',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_IMERG72Month_20060103To20191231.npz'),
                                        (('SmNDVI_BlendedVHP', 
                                          'TCI_BlendedVHP', 
                                          'VCI_BlendedVHP', 
                                          'VHI_BlendedVHP'), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_BlendedVHP_Corr2MonthlyPerc_20030930To20191231.npz'),
                                        (('GlobSnow3',), f'{temp_path_npz_Soni}/PreppedTrainNEvalNpzs/ClimGrid1D/SingleUnified_GlobSnow3_20060103To20191231.npz')     )

            Dict_of_Name_Filename_Pairs = { key : value for keys, value in NameKeys_FilenameValues for key in keys }
            
            NameKeys_RefArrayKeyValues = ( (('Target',), 'InfoArray'),
                                           (('Z_index',), 'ZIndex_PrcntlArray'),
                                           (('Z_index_60_month',), 'ZIndex60month_PrcntlArray'),
                                           (('PMDI',), 'PMDI_PrcntlArray'),
                                           (('PHDI',), 'PHDI_PrcntlArray'),
                                           (('prcp_01_nCG', 
                                             'prcp_02_nCG', 
                                             'prcp_03_nCG', 
                                             'prcp_06_nCG', 
                                             'prcp_09_nCG', 
                                             'prcp_12_nCG', 
                                             'prcp_24_nCG', 
                                             'prcp_36_nCG', 
                                             'prcp_48_nCG', 
                                             'prcp_60_nCG', 
                                             'prcp_72_nCG',
                                             # beginning indicators inserted here out of sequence from further below
                                             'SPI_gamma_01_nCG', 
                                             'SPI_gamma_02_nCG', 
                                             'SPI_gamma_03_nCG', 
                                             'SPI_gamma_06_nCG', 
                                             'SPI_gamma_09_nCG', 
                                             'SPI_gamma_12_nCG', 
                                             'SPI_gamma_24_nCG', 
                                             'SPI_gamma_36_nCG', 
                                             'SPI_gamma_48_nCG', 
                                             'SPI_gamma_60_nCG', 
                                             'SPI_gamma_72_nCG', 
                                             'SPEI_pear_01_nCG', 
                                             'SPEI_pear_02_nCG', 
                                             'SPEI_pear_03_nCG', 
                                             'SPEI_pear_06_nCG', 
                                             'SPEI_pear_09_nCG', 
                                             'SPEI_pear_12_nCG', 
                                             'SPEI_pear_24_nCG', 
                                             'SPEI_pear_36_nCG', 
                                             'SPEI_pear_48_nCG', 
                                             'SPEI_pear_60_nCG', 
                                             'SPEI_pear_72_nCG', 
                                             'tavg_01_nCG', 
                                             'tmax_01_nCG'), 'Variable_PrcntlArray'),
                                             # ending indicators inserted here out of sequence from further below
                                           (('CPC_soil_moisture',), 'CPCsoilmoist_PrcntlArray'),
                                           (('GRACE_DA_gw',), 'GRACEDA_gws_inst_PrcntlArray'),
                                           (('GRACE_DA_sfsm',), 'GRACEDA_sfsm_inst_PrcntlArray'),
                                           (('GRACE_DA_rtzsm',), 'GRACEDA_rtzsm_inst_PrcntlArray'),
                                           (('EDDI_1wk', 
                                             'EDDI_2wk', 
                                             'EDDI_3wk', 
                                             'EDDI_4wk', 
                                             'EDDI_5wk', 
                                             'EDDI_6wk', 
                                             'EDDI_7wk', 
                                             'EDDI_8wk', 
                                             'EDDI_9wk', 
                                             'EDDI_10wk', 
                                             'EDDI_11wk', 
                                             'EDDI_12wk', 
                                             'EDDI_1mn', 
                                             'EDDI_2mn', 
                                             'EDDI_3mn', 
                                             'EDDI_4mn', 
                                             'EDDI_5mn', 
                                             'EDDI_6mn', 
                                             'EDDI_7mn', 
                                             'EDDI_8mn', 
                                             'EDDI_9mn', 
                                             'EDDI_10mn', 
                                             'EDDI_11mn', 
                                             'EDDI_12mn'), 'EDDI_PrcntlArray'),
                                           (('NLDAS2D_1MSM_Mosaic', 
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
                                             'NLDAS2D_STRMH04_VIC'), 'NLDAS_2_daily_PrcntlArray'),
                                           (('VegDRI',), 'VegDRI_PrcntlArray'),
                                           (('QuickDRI',), 'QuickDRI_PrcntlArray'),
                                           (('ESI_4wk',), 'ESI4Week_PrcntlArray'),
                                           (('ESI_12wk',), 'ESI12Week_PrcntlArray'),
                                           #'SPI_gamma_01_nCG',  # this now moved out of sequence to further up
                                           #'SPI_gamma_02_nCG',  # this now moved out of sequence to further up
                                           #'SPI_gamma_03_nCG',  # this now moved out of sequence to further up
                                           #'SPI_gamma_06_nCG',  # this now moved out of sequence to further up
                                           #'SPI_gamma_09_nCG',  # this now moved out of sequence to further up
                                           #'SPI_gamma_12_nCG',  # this now moved out of sequence to further up
                                           #'SPI_gamma_24_nCG',  # this now moved out of sequence to further up
                                           #'SPI_gamma_36_nCG',  # this now moved out of sequence to further up
                                           #'SPI_gamma_48_nCG',  # this now moved out of sequence to further up
                                           #'SPI_gamma_60_nCG',  # this now moved out of sequence to further up
                                           #'SPI_gamma_72_nCG',  # this now moved out of sequence to further up
                                           #'SPEI_pear_01_nCG',  # this now moved out of sequence to further up
                                           #'SPEI_pear_02_nCG',  # this now moved out of sequence to further up
                                           #'SPEI_pear_03_nCG',  # this now moved out of sequence to further up
                                           #'SPEI_pear_06_nCG',  # this now moved out of sequence to further up
                                           #'SPEI_pear_09_nCG',  # this now moved out of sequence to further up
                                           #'SPEI_pear_12_nCG',  # this now moved out of sequence to further up
                                           #'SPEI_pear_24_nCG',  # this now moved out of sequence to further up
                                           #'SPEI_pear_36_nCG',  # this now moved out of sequence to further up
                                           #'SPEI_pear_48_nCG',  # this now moved out of sequence to further up
                                           #'SPEI_pear_60_nCG',  # this now moved out of sequence to further up
                                           #'SPEI_pear_72_nCG',  # this now moved out of sequence to further up
                                           #'tavg_01_nCG',  # this now moved out of sequence to further up
                                           #'tmax_01_nCG', # this now moved out of sequence to further up
                                           (('SNODAS',), 'SNODAS_PrcntlArray'),
                                           (('ESA_CCI',), 'ESA_CCI_PrcntlArray'),
                                           (('IMERG_01', 
                                             'IMERG_02', 
                                             'IMERG_03', 
                                             'IMERG_06', 
                                             'IMERG_09', 
                                             'IMERG_12', 
                                             'IMERG_24', 
                                             'IMERG_36', 
                                             'IMERG_48', 
                                             'IMERG_60', 
                                             'IMERG_72'), 'IMERG_nMonth_PrcntlArray'),
                                           (('SmNDVI_BlendedVHP',), 'BlendedVHP_SMN_PrcntlArray'),
                                           (('TCI_BlendedVHP',), 'BlendedVHP_TCI_PrcntlArray'),
                                           (('VCI_BlendedVHP',), 'BlendedVHP_VCI_PrcntlArray'),
                                           (('VHI_BlendedVHP',), 'BlendedVHP_VHI_PrcntlArray'),
                                           (('GlobSnow3',), 'GlobSnow3_PrcntlArray')    )
            
            Dict_of_Name_RefArrayKey_Pairs = { key : value for keys, value in NameKeys_RefArrayKeyValues for key in keys }

        else: # if TargetVariable == 'USDM'

            sys.exit("Invalid TargetVariable choice, add relevant code lines!!!")

        # end of if TargetVariable == 'USDM'

        SpatialDomain_ShortStr = 'C'
    else:
        sys.exit("Invalid SpatialDomain choice, add relevant code lines!!!")
    #end of if SpatialDomain in ['CONUS']

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

    def GetInpAndTargArraysFromFile_ClmGrd1D_V2(Dict_of_Name_Filename_Pairs, Dict_of_Name_RefArrayKey_Pairs, InpLayersCombination, IfMakeTargetBinary, IfIncludeD0AsDrought, WhichSeason, MinimumWindowSize, MaximumWindowSize, MinSamplesForFracI, ThisPxlRow, ThisPxlCol, PxlRow_SortedArr_FrmShpFile, PxlCol_SortedArr_FrmShpFile):

    #  print("In GetInpAndTargArraysFromFile_ClmGrd1D, InpLayersCombination is ", InpLayersCombination)

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

            TargetFileObj = np.load(Dict_of_Name_Filename_Pairs['Target']) 

            # SY: ExtractArraysOfNpz_And_TimeSliceStrict function further below not used for the following few lines of target because we're not changing the array dtype to float32 as is done in that function
            YYYYMMDD_Of_Array = TargetFileObj['YYYYMMDD_Of_InfoArray']
            Target_Array = TargetFileObj['InfoArray'] # Target data array

            YYYYMMDD_Of_Array, Target_Array = TimeSliceStrict_YYYYMMDDAndRefArrays(YYYYMMDD_Of_Array, Target_Array, BeginYYYYMMDD, EndYYYYMMDD, 'USDM') 

            YYYY_Of_Array = YYYYMMDD_Of_Array // 10000
            MM_Of_Array = (YYYYMMDD_Of_Array - YYYY_Of_Array * 10000) // 100
            del YYYYMMDD_Of_Array
            del YYYY_Of_Array
    
            if WhichSeason == 'P':
                WhichRows = np.where( (MM_Of_Array >= 3) & (MM_Of_Array <= 5) )
            elif WhichSeason == 'U':
                WhichRows = np.where( (MM_Of_Array >= 6) & (MM_Of_Array <= 8) )
            elif WhichSeason == 'F':
                WhichRows = np.where( (MM_Of_Array >= 9) & (MM_Of_Array <= 11) )
            elif WhichSeason == 'W':
                WhichRows = np.where( (MM_Of_Array >= 12) | (MM_Of_Array <= 2) )
            del MM_Of_Array

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
    
            Target_Array = Target_Array[:, Idxs_In_PxlRowCols[0]]
            if WhichSeason in ['P', 'U', 'F', 'W']:
                Target_Array = Target_Array[WhichRows[0], :]
            Target_Array = np.reshape(Target_Array, (Target_Array.size, 1))

            Inputs_Mat = np.copy(Target_Array) # REMEMBER to remove this 1st column below
        
            for ThisFromInpLayersCombination in InpLayersCombination:

                ThisIndicatorFileObj = np.load(Dict_of_Name_Filename_Pairs[ThisFromInpLayersCombination])

                #input percentile array
                YYYYMMDD_Of_Array, ThisIndicator_PrcntlArray = ExtractArraysOfNpz_And_TimeSliceStrict(BeginYYYYMMDD, EndYYYYMMDD, ThisFromInpLayersCombination, ThisIndicatorFileObj, 'YYYYMMDD_Of_Array', Dict_of_Name_RefArrayKey_Pairs[ThisFromInpLayersCombination])

                del YYYYMMDD_Of_Array

                ThisIndicator_PrcntlArray = ThisIndicator_PrcntlArray[:, Idxs_In_PxlRowCols[0]]

                if WhichSeason in ['P', 'U', 'F', 'W']:
                    ThisIndicator_PrcntlArray = ThisIndicator_PrcntlArray[WhichRows[0], :]

                ThisIndicator_PrcntlArray = np.reshape(ThisIndicator_PrcntlArray, (ThisIndicator_PrcntlArray.size, 1))
                Inputs_Mat = np.concatenate( (Inputs_Mat, ThisIndicator_PrcntlArray ), axis = 1)
                del ThisIndicator_PrcntlArray

            #end of for ThisFromInpLayersCombination in InpLayersCombination

            del Idxs_In_PxlRowCols      
        
            if WhichSeason in ['P', 'U', 'F', 'W']:
                del WhichRows

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

        return Target_Array, Inputs_Mat, ThisWindowSize_prev

    #end of def GetInpAndTargArraysFromFile_ClmGrd1D_V2(Dict_of_Name_Filename_Pairs, Dict_of_Name_RefArrayKey_Pairs, InpLayersCombination, IfMakeTargetBinary, IfIncludeD0AsDrought, WhichSeason, MinimumWindowSize, MaximumWindowSize, MinSamplesForFracI, ThisPxlRow, ThisPxlCol, PxlRow_SortedArr_FrmShpFile, PxlCol_SortedArr_FrmShpFile)

    All_Target_Array, All_Inputs_Mat, WindowSize_prev = GetInpAndTargArraysFromFile_ClmGrd1D_V2(Dict_of_Name_Filename_Pairs, Dict_of_Name_RefArrayKey_Pairs, InpLayersCombination, IfMakeTargetBinary, IfIncludeD0AsDrought, WhichSeason, MinimumWindowSize, MaximumWindowSize, MinSamplesForFracI, ThisPxlRow, ThisPxlCol, PxlRow_SortedArr_FrmShpFile, PxlCol_SortedArr_FrmShpFile)

    del PxlRow_SortedArr_FrmShpFile 
    del PxlCol_SortedArr_FrmShpFile 

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

    def calc_MI_info(Inp_name_key, Targ_name_key, Inp_array_key, Targ_array_key, If_discrete_features_key, Num_random_states_key, n_neighbors_key, Inp_names_list_key, MI_values_list_key, MI_lowersofrange_list_key, MI_uppersofrange_list_key, MI_ranges_list_key, sample_sizes_list_key, Entropy_list_key, RelMI_values_list_key, RelMI_lowersofrange_list_key, RelMI_uppersofrange_list_key, MinSamplesForFracI_key):
        XX = Inp_array_key[:,0:1]
        YY = Targ_array_key[:,0:1]
        Idxs = np.where((~np.isnan(XX)) & (~np.isnan(YY)))
        Percentiles_for_n_neighbors = np.empty((3,), dtype=np.float32)
        Percentiles_for_n_neighbors[:] = np.NaN
        if len(Idxs[0]) > MinSamplesForFracI_key:
            XX = XX[Idxs[0]]
            YY = YY[Idxs[0]]
            YY = YY[:,0]
            MIs_this_n_neighbors = np.empty((Num_random_states_key,), dtype=np.float32)
            MIs_this_n_neighbors[:] = np.NaN
            for Which_Random_state_value in range(Num_random_states_key):
                Random_state_value = 3 + Which_Random_state_value*100
                MIs_this_n_neighbors[Which_Random_state_value] = mutual_info_classif(XX,YY,discrete_features=If_discrete_features_key, n_neighbors=n_neighbors_key, copy=True, random_state = Random_state_value)
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
            RelMI_values_list_key.append(Percentiles_for_n_neighbors[1]/Entropyy)
            RelMI_lowersofrange_list_key.append(Percentiles_for_n_neighbors[0]/Entropyy)
            RelMI_uppersofrange_list_key.append(Percentiles_for_n_neighbors[2]/Entropyy)
        else: # if len(Idxs[0]) > MinSamplesForFracI_key
            MI_ranges_list_key.append(np.NaN)
            sample_sizes_list_key.append(0.0)
            Entropyy = np.NaN
            RelMI_values_list_key.append(np.NaN)
            RelMI_lowersofrange_list_key.append(np.NaN)
            RelMI_uppersofrange_list_key.append(np.NaN)
        #end of if len(Idxs[0]) > MinSamplesForFracI_key
        del XX 
        del YY
        del Idxs
        Inp_names_list_key.append(Inp_name_key)
        MI_values_list_key.append(Percentiles_for_n_neighbors[1])
        MI_lowersofrange_list_key.append(Percentiles_for_n_neighbors[0])
        MI_uppersofrange_list_key.append(Percentiles_for_n_neighbors[2])
        Entropy_list_key.append(Entropyy)

        return Inp_names_list_key, MI_values_list_key, MI_lowersofrange_list_key, MI_uppersofrange_list_key, MI_ranges_list_key, sample_sizes_list_key, Entropy_list_key, RelMI_values_list_key, RelMI_lowersofrange_list_key, RelMI_uppersofrange_list_key
    #end of def calc_MI_info

    def calc_MI_1ValueForMultiFeatures(Inp_array_key, Targ_array_key, If_discrete_features_key, Num_random_states_key, n_neighbors_key, MinSamplesForFracI_key):
        XX = np.copy(Inp_array_key)
        YY = Targ_array_key[:,0:1]
    #  Idxs = np.where((~np.isnan(XX)) & (~np.isnan(YY)))
        Idxs = np.where( ( np.reshape(np.all( ~np.isnan(XX) & ~np.isnan(YY), axis = 1 ), (-1, 1)) ) )
        Percentiles_for_n_neighbors = np.empty((3,), dtype=np.float32)
        Percentiles_for_n_neighbors[:] = np.NaN
        if len(Idxs[0]) > MinSamplesForFracI_key:
            XX = XX[Idxs[0]]
            YY = YY[Idxs[0]]
            YY = YY[:,0]
            MIs_this_n_neighbors = np.empty((Num_random_states_key,), dtype=np.float32)
            MIs_this_n_neighbors[:] = np.NaN
            for Which_Random_state_value in range(Num_random_states_key):
                Random_state_value = 3 + Which_Random_state_value*100
        #        MIs_this_n_neighbors[Which_Random_state_value] = mutual_info_classif(XX,YY,discrete_features=If_discrete_features_key, n_neighbors=n_neighbors_key, copy=True, random_state = Random_state_value)
                MIs_this_n_neighbors[Which_Random_state_value] = MI_classif_1ValueForMultiFeatures(XX,YY,discrete_features=If_discrete_features_key, n_neighbors=n_neighbors_key, copy=True, random_state = Random_state_value)
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
            MI_range = Percentiles_for_n_neighbors[2]-Percentiles_for_n_neighbors[0]
            sample_size = YY.size
            RelMI_value = Percentiles_for_n_neighbors[1]/Entropyy
            RelMI_lowerofrange = Percentiles_for_n_neighbors[0]/Entropyy
            RelMI_upperofrange = Percentiles_for_n_neighbors[2]/Entropyy
        else: # of if len(Idxs[0]) > MinSamplesForFracI_key
            MI_range = np.NaN
            sample_size = 0
            Entropyy = np.NaN
            RelMI_value = np.NaN
            RelMI_lowerofrange = np.NaN
            RelMI_upperofrange = np.NaN
        #end of if len(Idxs[0]) > MinSamplesForFracI_key
        del XX
        del YY
        del Idxs
        MI_value = Percentiles_for_n_neighbors[1]
        MI_lowerofrange = Percentiles_for_n_neighbors[0]
        MI_upperofrange = Percentiles_for_n_neighbors[2]

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

        Inp_names_list, MI_values_list, MI_lowersofrange_list, MI_uppersofrange_list, MI_ranges_list, sample_sizes_list, Entropy_list, RelMI_values_list, RelMI_lowersofrange_list, RelMI_uppersofrange_list = calc_MI_info(Inp_name_key = DictofNumNamePairs_Channels[SelectCols[0]+1], Targ_name_key = TargetVariable, Inp_array_key = All_Inputs_Mat, Targ_array_key = All_Target_Array, If_discrete_features_key = False, Num_random_states_key = Num_random_states, n_neighbors_key = n_neighbors, Inp_names_list_key = Inp_names_list, MI_values_list_key = MI_values_list, MI_lowersofrange_list_key = MI_lowersofrange_list, MI_uppersofrange_list_key = MI_uppersofrange_list, MI_ranges_list_key = MI_ranges_list, sample_sizes_list_key = sample_sizes_list, Entropy_list_key = Entropy_list, RelMI_values_list_key = RelMI_values_list, RelMI_lowersofrange_list_key = RelMI_lowersofrange_list, RelMI_uppersofrange_list_key = RelMI_uppersofrange_list, MinSamplesForFracI_key = MinSamplesForFracI)

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

        MI_value, MI_lowerofrange, MI_upperofrange, MI_range, sample_size, Entropyy, RelMI_value, RelMI_lowerofrange, RelMI_upperofrange = calc_MI_1ValueForMultiFeatures(Inp_array_key = All_Inputs_Mat, Targ_array_key = All_Target_Array, If_discrete_features_key = False, Num_random_states_key = Num_random_states, n_neighbors_key = n_neighbors, MinSamplesForFracI_key = MinSamplesForFracI)

    #end of if SelectCols.size == 1

    del All_Target_Array 
    del All_Inputs_Mat

    # This will merge outputs into a single file

    # RelMI_value = np.array([RelMI_value], dtype=np.float32)
    # np.savetxt(FracI_ClmGrd1D_AllValid_NDFeat_FileName, RelMI_value)

    # sample_size = np.array([sample_size], dtype=np.float32)
    # np.savetxt(SampSiz_ClmGrd1D_AllValid_NDFeat_FileName, sample_size)

    # WindowSize_prev = np.array([WindowSize_prev], dtype=np.float32)
    # np.savetxt(WindowSiz_ClmGrd1D_AllValid_NDFeat_FileName, WindowSize_prev)

    # save output into array, order is alphabetical
    OutputArray = np.array(
        [RelMI_value, sample_size, WindowSize_prev], dtype=np.float32)
    np.savetxt(OutputArrayFilename, OutputArray)

    eeend_Overall = datetime.now()
    eeelapsed_Overall = eeend_Overall - ssstart_Overall

    print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")

    print("End time", time.time())
    return

if __name__ == "__main__":
    main()
