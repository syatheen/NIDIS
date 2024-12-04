# Coded by Soni Yatheendradas
#         on May 30, 2024
from __future__ import division
import numpy as np
from shapely.geometry import Polygon, Point
import geopandas as gpd
from datetime import datetime, timedelta

# BEGIN code arguments / editable section

ClimDivShpFile = '/discover/nobackup/syatheen/NIDIS/Data/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS_EPSG4326.shp'
ClimGrid1DShpFile = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/nClimGrid_as_poly_NoNans_wClimDiv.shp'

ZIndex_InfoFilename = 'RefArr_1MonthAccumzndx_193201To202001.npz'
ZIndex60month_InfoFilename = 'RefArr_60MonthAccumzndx_193201To202001.npz'

ZIndex_Info = np.load(ZIndex_InfoFilename)
ZIndex60month_Info = np.load(ZIndex60month_InfoFilename)

ZIndex_YYYYMM_Of_InfoArray  = ZIndex_Info['YYYYMM_Of_RefArrayForPrcntl']
#print("ZIndex_YYYYMM_Of_InfoArray.shape is ", ZIndex_YYYYMM_Of_InfoArray.shape)
ZIndex_InfoArray  = ZIndex_Info['RefArrayForPrcntl']
#print("ZIndex_InfoArray.shape is ", ZIndex_InfoArray.shape)
ZIndex60month_YYYYMM_Of_InfoArray  = ZIndex60month_Info['YYYYMM_Of_RefArrayForPrcntl']
#print("ZIndex60month_YYYYMM_Of_InfoArray.shape is ", ZIndex60month_YYYYMM_Of_InfoArray.shape)
ZIndex60month_InfoArray  = ZIndex60month_Info['RefArrayForPrcntl']
#print("ZIndex60month_InfoArray.shape is ", ZIndex60month_InfoArray.shape)

ZIndex_ArrayFileName = '/discover/nobackup/projects/nca/syatheen/Palmer_monthly_Npzs/RefArr_1MonthAccumzndx_193201To202001_ClmGrd1D.npz'
ZIndex60month_ArrayFileName = '/discover/nobackup/projects/nca/syatheen/Palmer_monthly_Npzs/RefArr_60MonthAccumzndx_193201To202001_ClmGrd1D.npz' 

# END code arguments / editable section

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

#print("CLIMDIV_SortedArray_FrmShpFile.shape is ", CLIMDIV_SortedArray_FrmShpFile.shape)
#print("CLIMDIV_Array_FrmGrdShpFile.shape is ", CLIMDIV_Array_FrmGrdShpFile.shape)

Idxs = np.nonzero(CLIMDIV_Array_FrmGrdShpFile[:,None] == CLIMDIV_SortedArray_FrmShpFile)[1]
#print("Idxs is ", Idxs)
#print("Idxs.shape is ", Idxs.shape)

ZIndex_InfoArray_Grd1D = ZIndex_InfoArray[:, Idxs]
#print("ZIndex_InfoArray_Grd1D.shape is ", ZIndex_InfoArray_Grd1D.shape)
ZIndex60month_InfoArray_Grd1D = ZIndex60month_InfoArray[:, Idxs]
#print("ZIndex60month_InfoArray_Grd1D.shape is ", ZIndex60month_InfoArray_Grd1D.shape)

np.savez_compressed(ZIndex_ArrayFileName, 
                    YYYYMM_Of_RefArrayForPrcntl = ZIndex_YYYYMM_Of_InfoArray, 
                    RefArrayForPrcntl = ZIndex_InfoArray_Grd1D)
np.savez_compressed(ZIndex60month_ArrayFileName, 
                    YYYYMM_Of_RefArrayForPrcntl = ZIndex60month_YYYYMM_Of_InfoArray, 
                    RefArrayForPrcntl = ZIndex60month_InfoArray_Grd1D)

