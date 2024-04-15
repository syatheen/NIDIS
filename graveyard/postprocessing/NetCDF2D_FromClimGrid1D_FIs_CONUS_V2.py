# Coded by Soni Yatheendradas
#         on Jul 31, 2022
from __future__ import division
import numpy as np
from netCDF4 import Dataset    # Note: python is case-sensitive!
from datetime import datetime, timedelta
import rioxarray
import xarray as xr
import geopandas as gpd

###BEGIN ANY EDITS HERE#########

NumInpLayers = 113
WhichSeason_ShortStr = 'W'
InputNum_0Start = 39

DictofInitialToWord_Seasons = {'P': 'Spring',
                               'U': 'Summer',
                               'F': 'Fall',
                               'W': 'Winter',
                               'A': 'All-season'}

DictofNumNamePairs_Channels = {1: 'Z_index',
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
                               113: 'GlobSnow3'}

#FI_InNpzFile = 'FI_ClmGrd1D_V2b_New/1/NN_U_C_0To469757_In' + str(NumInpLayers)  + '_' + str(InputNum_0Start) + '_' + WhichSeason_ShortStr + '.npz'
#FI_InNpzFile = 'FI_InpPCnv_ClmGrd1D_V2b_New/1/NN5_U_C_0To469757_In' + str(NumInpLayers)  + '_' + str(InputNum_0Start) + '_' + WhichSeason_ShortStr + '.npz'
#FI_InNpzFile = 'FI_PrcPCnv_ClmGrd1D_V2b_New/1/NN3_U_C_0To469757_In' + str(NumInpLayers)  + '_' + str(InputNum_0Start) + '_' + WhichSeason_ShortStr + '.npz'
FI_InNpzFile = 'FI1X1_ClmGrd1D_V2b_New/1/Npzs/NN_U_C_0To469757_In' + str(NumInpLayers)  + '_' + str(InputNum_0Start) + '_' + WhichSeason_ShortStr + '.npz'
#FI_InNpzFile = 'FI1X1_ClmGrd1D_V2b_New/1/Smth3_NN_U_C_0To469757_In' + str(NumInpLayers)  + '_' + str(InputNum_0Start) + '_' + WhichSeason_ShortStr + '.npz'
#SSiz_InNpzFile = 'SSiz_ClmGrd1D_V2b_New/1/NN_U_C_0To469757_In' + str(NumInpLayers)  + '_' + str(InputNum_0Start) + '_' + WhichSeason_ShortStr + '.npz'
#SSiz_InNpzFile = 'SSiz_InpPCnv_ClmGrd1D_V2b_New/1/NN5_U_C_0To469757_In' + str(NumInpLayers)  + '_' + str(InputNum_0Start) + '_' + WhichSeason_ShortStr + '.npz'
#SSiz_InNpzFile = 'SSiz_PrcPCnv_ClmGrd1D_V2b_New/1/NN3_U_C_0To469757_In' + str(NumInpLayers)  + '_' + str(InputNum_0Start) + '_' + WhichSeason_ShortStr + '.npz'
SSiz_InNpzFile = 'SSiz1X1_ClmGrd1D_V2b_New/1/Npzs/NN_U_C_0To469757_In' + str(NumInpLayers)  + '_' + str(InputNum_0Start) + '_' + WhichSeason_ShortStr + '.npz'
#WSiz_InNpzFile = 'WSiz_ClmGrd1D_V2b_New/1/NN_U_C_0To469757_In' + str(NumInpLayers)  + '_' + str(InputNum_0Start) + '_' + WhichSeason_ShortStr + '.npz'
#WSiz_InNpzFile = 'WSiz_InpPCnv_ClmGrd1D_V2b_New/1/NN5_U_C_0To469757_In' + str(NumInpLayers)  + '_' + str(InputNum_0Start) + '_' + WhichSeason_ShortStr + '.npz'
#WSiz_InNpzFile = 'WSiz_PrcPCnv_ClmGrd1D_V2b_New/1/NN3_U_C_0To469757_In' + str(NumInpLayers)  + '_' + str(InputNum_0Start) + '_' + WhichSeason_ShortStr + '.npz'
WSiz_InNpzFile = 'WSiz1X1_ClmGrd1D_V2b_New/1/Npzs/NN_U_C_0To469757_In' + str(NumInpLayers)  + '_' + str(InputNum_0Start) + '_' + WhichSeason_ShortStr + '.npz'

#OutNcFile = 'NcFiles/NC2D_From_nCG1D_FIsEtc_' + str(NumInpLayers) + '_' + WhichSeason_ShortStr + '_' + DictofNumNamePairs_Channels[InputNum_0Start+1] + '_V2.nc'
#OutNcFile = 'NcFiles/NC2D_InpPCnv5_From_nCG1D_FIsEtc_' + str(NumInpLayers) + '_' + WhichSeason_ShortStr + '_' + DictofNumNamePairs_Channels[InputNum_0Start+1] + '_V2.nc'
#OutNcFile = 'NcFiles/NC2D_PrcPCnv3_From_nCG1D_FIsEtc_' + str(NumInpLayers) + '_' + WhichSeason_ShortStr + '_' + DictofNumNamePairs_Channels[InputNum_0Start+1] + '_V2.nc'
OutNcFile = 'NcFiles/NC2D_From_nCG1D_FIs1X1Etc_' + str(NumInpLayers) + '_' + WhichSeason_ShortStr + '_' + DictofNumNamePairs_Channels[InputNum_0Start+1] + '_V2.nc'
#OutNcFile = 'NcFiles/NC2D_From_nCG1D_FIs1X1Etc_Smth3_' + str(NumInpLayers) + '_' + WhichSeason_ShortStr + '_' + DictofNumNamePairs_Channels[InputNum_0Start+1] + '_V2.nc'

nClimGrid_NC_File = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/monthly_spei_gamma/nclimgrid-spei-gamma-01.nc'

ClimGrid1DShpFile = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/nClimGrid_as_poly_NoNans.shp'

ncfile_title_EndingSubstr = ' Pixel-specific Fractional Info of USDM (2006-01-03 To 2019-12-31)'
#ncfile_title_EndingSubstr = ' Pixel-specific Fractional Info of USDM (2006-06-06 To 2019-12-31)'

###END ANY EDITS HERE#########

nClimGrid_All = xr.open_dataset(nClimGrid_NC_File)

lats = nClimGrid_All['lat'].values
lons = nClimGrid_All['lon'].values

FI_InNpz = np.load(FI_InNpzFile)
FracIs = FI_InNpz['ArrayForSingleFile']
Idxs = np.where((~np.isnan(FracIs)) & (FracIs > 1.0))
FracIs[Idxs] = 1.0
Idxs = np.where((~np.isnan(FracIs)) & (FracIs < 0.0))
FracIs[Idxs] = 0.0

SSiz_InNpz = np.load(SSiz_InNpzFile)
SampleSizes = SSiz_InNpz['ArrayForSingleFile']

WSiz_InNpz = np.load(WSiz_InNpzFile)
WindowSizes = WSiz_InNpz['ArrayForSingleFile']

ClimGrid1DShp = gpd.read_file(ClimGrid1DShpFile)
PxlRowCol_SortedList_FrmShpFile = sorted(ClimGrid1DShp.PxlRowCol.values.tolist())
PxlRowCols = np.array(PxlRowCol_SortedList_FrmShpFile)
PxlRows = (np.around(PxlRowCols // 10000)).astype(int)
PxlCols = (np.around(PxlRowCols % 10000)).astype(int)

# create 2D arrays
FI_Arr2D = np.empty((len(lats), len(lons)))
FI_Arr2D[:] = np.NaN
FI_Arr2D[PxlRows, PxlCols] = FracIs
SSiz_Arr2D = np.empty((len(lats), len(lons)))
SSiz_Arr2D[:] = np.NaN
SSiz_Arr2D[PxlRows, PxlCols] = SampleSizes
WSiz_Arr2D = np.empty((len(lats), len(lons)))
WSiz_Arr2D[:] = np.NaN
WSiz_Arr2D[PxlRows, PxlCols] = WindowSizes

try: ncfile.close()  # just to be safe, make sure dataset is not already open.
except: pass
ncfile = Dataset(OutNcFile, mode='w', format='NETCDF4_CLASSIC')
print(ncfile)

lat_dim = ncfile.createDimension('lat', len(lats))     # latitude axis
lon_dim = ncfile.createDimension('lon', len(lons))    # longitude axis

ncfile.title = DictofNumNamePairs_Channels[InputNum_0Start+1] + ' ' + DictofInitialToWord_Seasons[WhichSeason_ShortStr] + ncfile_title_EndingSubstr 


# Define two variables with the same names as dimensions,
# a conventional way to define "coordinate variables".
lat = ncfile.createVariable('lat', np.float32, ('lat',))
lat.units = 'degrees_north'
lat.long_name = 'latitude'
lon = ncfile.createVariable('lon', np.float32, ('lon',))
lon.units = 'degrees_east'
lon.long_name = 'longitude'
# Define 2D variables to hold the data
FracI = ncfile.createVariable('FracI',np.float64,('lat','lon')) 
FracI.units = '-' 
SampleSize = ncfile.createVariable('SampleSize',np.float64,('lat','lon')) 
SampleSize.units = '-' 
WindowSize = ncfile.createVariable('WindowSize',np.float64,('lat','lon')) 
WindowSize.units = '-' 

# Write latitudes, longitudes.
# Note: the ":" is necessary in these "write" statements
lat[:] = lats # south to north
lon[:] = lons # Greenwich meridian eastward
# Write the data.  This writes the whole 2D netCDF variable all at once.
FracI[:,:] = FI_Arr2D
SampleSize[:,:] = SSiz_Arr2D  
WindowSize[:,:] = WSiz_Arr2D  

# first print the Dataset object to see what we've got
print(ncfile)
# close the Dataset.
ncfile.close(); print('Dataset is closed!')



