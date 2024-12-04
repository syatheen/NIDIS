# Coded by Soni Yatheendradas
#         on June 19, 2024
from __future__ import division
import numpy as np
import geopandas as gpd
from datetime import datetime, timedelta

# BEGIN code arguments / editable section

ClimDivShpFile = '/discover/nobackup/syatheen/NIDIS/Data/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS_EPSG4326.shp'
ClimGrid1DShpFile = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/nClimGrid_as_poly_NoNans_wClimDiv.shp'

PMDI_ClimDiv_ArrayFileName = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/Palmer/weekly/private/pdiRefArray_20050101To20200104.npz'
PHDI_ClimDiv_ArrayFileName = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/Palmer/weekly/private/phdRefArray_20050604To20200104.npz'

PMDI_ClimDiv_ArrayObject = np.load(PMDI_ClimDiv_ArrayFileName)
PHDI_ClimDiv_ArrayObject = np.load(PHDI_ClimDiv_ArrayFileName)

PMDI_YYYYMMDD_Of_RefArrayForPrcntl  = PMDI_ClimDiv_ArrayObject['YYYYMMDD_Of_RefArrayForPrcntl']
PMDI_RefArrayForPrcntl  = PMDI_ClimDiv_ArrayObject['Palmer_RefArrayForPrcntl']
PHDI_YYYYMMDD_Of_RefArrayForPrcntl  = PHDI_ClimDiv_ArrayObject['YYYYMMDD_Of_RefArrayForPrcntl']
PHDI_RefArrayForPrcntl  = PHDI_ClimDiv_ArrayObject['Palmer_RefArrayForPrcntl']

PMDI_ClimGrid1D_ArrayFileName = '/discover/nobackup/projects/nca/syatheen/Palmer_weekly_Npzs/pdiRefArray_20050101To20200104_ClmGrd1D.npz'
PHDI_ClimGrid1D_ArrayFileName = '/discover/nobackup/projects/nca/syatheen/Palmer_weekly_Npzs/phdRefArray_20050604To20200104_ClmGrd1D.npz'

#######END ANY EDITS REQUIRED#########

ssstart_Overall = datetime.now()

ClimDivShp = gpd.read_file(ClimDivShpFile)
ClimGrid1DShp = gpd.read_file(ClimGrid1DShpFile)

CLIMDIV_Array_FrmShpFile =  ClimDivShp.CLIMDIV.values
CLIMDIV_SortedArray_FrmShpFile = np.array(sorted(CLIMDIV_Array_FrmShpFile))

if np.array_equal(CLIMDIV_SortedArray_FrmShpFile, CLIMDIV_Array_FrmShpFile):

  print('Unsorted and sorted CLIMDIV arrays equal in ClimDivShpFile!')

else: # if np.array_equal(CLIMDIV_SortedArray_FrmShpFile, CLIMDIV_Array_FrmShpFile)

  print('Unsorted and sorted CLIMDIV arrays not equal in ClimDivShpFile!')

#end of if np.array_equal(CLIMDIV_SortedArray_FrmShpFile, CLIMDIV_Array_FrmShpFile)

#ClimDivShp_sorted = ClimDivShp.iloc[ClimDivShp['CLIMDIV'].sort_values().index.values]

PxlRowCol_Array_FrmGrdShpFile =  ClimGrid1DShp.PxlRowCol.values
CLIMDIV_Array_FrmGrdShpFile =  ClimGrid1DShp.CLIMDIV.values

PxlRowCol_SortedArray_FrmGrdShpFile = np.array(sorted(PxlRowCol_Array_FrmGrdShpFile))

if np.array_equal(PxlRowCol_SortedArray_FrmGrdShpFile, PxlRowCol_Array_FrmGrdShpFile):

  print('PxlRowCol was already sorted in ClimGrid1DShpFile!')

else: # of if np.array_equal(PxlRowCol_SortedArray_FrmGrdShpFile, PxlRowCol_Array_FrmGrdShpFile)

  print('PxlRowCol was not already sorted in ClimGrid1DShpFile!')
  raise ValueError("PxlRowCol was not already sorted in ClimGrid1DShpFile!")

# end of if np.array_equal(PxlRowCol_SortedArray_FrmGrdShpFile, PxlRowCol_Array_FrmGrdShpFile)

Idxs = np.nonzero(CLIMDIV_Array_FrmGrdShpFile[:,None] == CLIMDIV_SortedArray_FrmShpFile)[1]

PMDI_RefArrayForPrcntl_ClimGrid1D = PMDI_RefArrayForPrcntl[:, Idxs]
print("PMDI_RefArrayForPrcntl_ClimGrid1D.shape is ", PMDI_RefArrayForPrcntl_ClimGrid1D.shape)
PHDI_RefArrayForPrcntl_ClimGrid1D = PHDI_RefArrayForPrcntl[:, Idxs]
print("PHDI_RefArrayForPrcntl_ClimGrid1D.shape is ", PHDI_RefArrayForPrcntl_ClimGrid1D.shape)

np.savez_compressed(PMDI_ClimGrid1D_ArrayFileName, 
                    YYYYMMDD_Of_RefArrayForPrcntl = PMDI_YYYYMMDD_Of_RefArrayForPrcntl, 
                    Palmer_RefArrayForPrcntl = PMDI_RefArrayForPrcntl_ClimGrid1D)
np.savez_compressed(PHDI_ClimGrid1D_ArrayFileName, 
                    YYYYMMDD_Of_RefArrayForPrcntl = PHDI_YYYYMMDD_Of_RefArrayForPrcntl, 
                    Palmer_RefArrayForPrcntl = PHDI_RefArrayForPrcntl_ClimGrid1D)



