from __future__ import division
import numpy as np
import sys
import os
import rasterio
from rasterio.features import shapes
import geopandas as gpd
from datetime import date, datetime, timedelta
import glob
import time
from calendar import monthrange
from osgeo import gdal
from pathlib import Path

"""
./RunProcess.sh 2000 1 -9999
./RunProcess.sh 2000 2 -9999
./RunProcess.sh 2000 3 -9999
./RunProcess.sh 2000 4 -9999
./RunProcess.sh 2000 5 -9999
./RunProcess.sh 2000 6 -9999
./RunProcess.sh 2000 7 -9999
./RunProcess.sh 2000 8 -9999
./RunProcess.sh 2000 9 -9999
./RunProcess.sh 2000 10 -9999
./RunProcess.sh 2000 11 -9999
./RunProcess.sh 2000 12 -9999
./RunProcess.sh 2020 1 -9999
./RunProcess.sh 2020 2 -9999
./RunProcess.sh 2020 3 -9999
./RunProcess.sh 2020 4 -9999
./RunProcess.sh 2020 5 30
"""

def main(ArgYearInt, ArgMonthInt, InitialNumDaysOfMonthToProcess):
  #NOTE: sys.argv indices start at 1, not 0
  #Python arguments to this program will be (for now):
  #        ThisYear ThisMonth InitialNumDaysOfMonthToProcess
  #ArgNum   1        2         3

  ssstart_Overall = datetime.now()

  #######BEGIN ANY EDITS REQUIRED#######

  #SourceFilePath = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/ESI/DailyInfoTiffs/'
  SourceFilePath = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/OriginalData/ESI/'

  #ClimDivShpFile = '/att/nobackup/syatheen/Data/ML_Testcases/Drought_USDM/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS.shp'
  # ClimDivShpFile = '/discover/nobackup/syatheen/NIDIS/Data/private/CONUS_CLIMATE_DIVISIONS/GIS.OFFICIAL_CLIM_DIVISIONS.shp'
  ClimGrid1DShpFile = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/nClimGrid_as_poly_NoNans.shp'

  mask = None

  #ArgYearInt = int(round(float(sys.argv[1])))
  #ArgMonthInt = int(round(float(sys.argv[2])))
  #InitialNumDaysOfMonthToProcess = int(round(float(sys.argv[3]))) # if -ve number like -9999, then processes all days of the month

  ArrayFileName = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/Indicators_70_to_71/spatial_resolution/InfoArrsDaily/'+format(ArgYearInt,'04')+format(ArgMonthInt,'02')+'.npz'


  xres = 0.125000000000/3
  yres = 0.125000000000/3
  resample_alg = 'near'
  Width = 1385
  Height = 596
  output_bounds = [-124 - 17*xres, 24 + 13*yres, -67, 49 + 9*yres]

  #######END ANY EDITS REQUIRED#########

  #BEGIN GETTING CLIMDIV SHAPEFILE DATA
  #ClimDivShp = gpd.read_file(ClimDivShpFile)
  #CLIMDIV_SortedList_FrmShpFile = sorted(ClimDivShp.CLIMDIV.values.tolist())

  ClimGrid1DShp = gpd.read_file(ClimGrid1DShpFile)
  PxlRowCol_SortedList_FrmShpFile = sorted(ClimGrid1DShp.PxlRowCol.values.tolist())
  PxlRowCol_SortedArr_FrmShpFile = np.array(PxlRowCol_SortedList_FrmShpFile)
  PxlRow_SortedArr_FrmShpFile = (np.around(PxlRowCol_SortedArr_FrmShpFile // 10000)).astype(int)
  PxlCol_SortedArr_FrmShpFile = (np.around(PxlRowCol_SortedArr_FrmShpFile % 10000)).astype(int)

  #END GETTING CLIMDIV SHAPEFILE DATA

  NumDaysInMonth = int(round(float(monthrange(ArgYearInt, ArgMonthInt)[1]))) 

  YYYYMMDD_Of_RefArrayForPrcntl = np.empty((NumDaysInMonth, 1), dtype=np.int32)
  YYYYMMDD_Of_RefArrayForPrcntl[:] = -9999
  RefArrayForPrcntl = np.empty((NumDaysInMonth, len(PxlRowCol_SortedList_FrmShpFile)))
  RefArrayForPrcntl[:] = np.NaN

  #if InitialNumDaysOfMonthToProcess <= 0:
  #  days_in_month = monthrange(ThisYear, ThisMonth)[1] 
  #else:
  #  days_in_month = InitialNumDaysOfMonthToProcess

  BeginDateVecList = [ ArgYearInt, ArgMonthInt, 1, 0, 0, 0]

  BeginDate = date(BeginDateVecList[0], BeginDateVecList[1], BeginDateVecList[2])

  #YYYYMMDD_Of_RefArrayForPrcntl = np.empty((days_in_month,1), dtype=np.int32)
  #YYYYMMDD_Of_RefArrayForPrcntl[:] = -9999
  #RefArrayForPrcntl = np.empty((days_in_month,len(CLIMDIV_SortedList_FrmShpFile)))
  #RefArrayForPrcntl[:] = np.NaN

  path_to_save_data = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/Indicators_70_to_71/spatial_resolution'
  os.makedirs(path_to_save_data, exist_ok=True)

  for WhichDayFromStart in range(1, NumDaysInMonth+1):

    IntermediateDate = BeginDate + timedelta(days=WhichDayFromStart)

    ThisDoM = IntermediateDate.day

    YYYYMMDD_Of_RefArrayForPrcntl[WhichDayFromStart] = 10000*ArgYearInt + 100*ArgMonthInt + ThisDoM
    
    FileNames_ESI=glob.glob(SourceFilePath+format(ArgYearInt,'04')+format(ArgMonthInt,'02')+format(ThisDoM,'02')+'.tif')
    
    if (len(FileNames_ESI) == 1):
      FileName_ESI = FileNames_ESI[0]
    
      IfTifFileExists = os.path.exists(FileName_ESI)
      if IfTifFileExists:

          BaseFileName = format(ArgYearInt,'04') + format(ArgMonthInt,'02') + format(ThisDoM,'02') 
          # outfn = SourceFileBasePath + 'NLDAS_2_daily/TempCreatedFiles/' + BaseFileName + '_upsampTo_nCG.tif'
          outfn = os.path.join(path_to_save_data, 'TempCreatedFiles/', BaseFileName + '_upsampTo_nCG.tif')
          os.makedirs(Path(outfn).parent, exist_ok=True)

          try:
              # os.remove('/discover/nobackup/projects/nca/syatheen/NLDAS_2_daily/TempCreatedFiles/{}_upsampTo_nCG.tif'.format(BaseFileName))
              os.remove(outfn)
          except OSError:
              pass

          ds = gdal.Warp(outfn, FileName_ESI, options = gdal.WarpOptions(resampleAlg=resample_alg, width=Width, height=Height, outputBounds=output_bounds, dstNodata = np.NaN))
          ds = None

          with rasterio.Env():
              # with rasterio.open('/discover/nobackup/projects/nca/syatheen/NLDAS_2_daily/TempCreatedFiles/{}_upsampTo_nCG.tif'.format(BaseFileName)) as SrcInfo:
              with rasterio.open(outfn) as SrcInfo:
                  ImageInfo = SrcInfo.read()

                  ImageInfo = np.flip(ImageInfo, axis = 1)

                  RefArrayForPrcntl[WhichDayFromStart-1, :] = ImageInfo[0, PxlRow_SortedArr_FrmShpFile, PxlCol_SortedArr_FrmShpFile]

      try:
          # os.remove('/discover/nobackup/projects/nca/syatheen/NLDAS_2_daily/TempCreatedFiles/{}_upsampTo_nCG.tif'.format(BaseFileName))
          os.remove(outfn)
      except OSError:
          pass

  print("YYYYMMDD_Of_RefArrayForPrcntl.shape is ",YYYYMMDD_Of_RefArrayForPrcntl.shape)
  print("YYYYMMDD_Of_RefArrayForPrcntl is ",YYYYMMDD_Of_RefArrayForPrcntl)
  print("RefArrayForPrcntl.shape is ",RefArrayForPrcntl.shape)
  print("RefArrayForPrcntl is ",RefArrayForPrcntl)
  print("np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)))
  print("np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)))
  print('overall min is ',np.nanmin(RefArrayForPrcntl),', overall max is ',np.nanmax(RefArrayForPrcntl))

  np.savez_compressed(ArrayFileName, YYYYMMDD_Of_RefPrcntlArray = YYYYMMDD_Of_RefArrayForPrcntl, RefPrcntlArray = RefArrayForPrcntl)

  eeend_Overall = datetime.now()
  eeelapsed_Overall = eeend_Overall - ssstart_Overall
  print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")

  return


def run_main():
   
  combinations_list = []
  for year in range(2000, 2020):
    for month in range(1, 13):
        combinations_list.append([year, month, -9999])
  #final year which is shorter
  for month in range(1, 5):
    combinations_list.append([2020, month, -9999])
  combinations_list.append([2020, 5, 30])

  print(combinations_list)

   return


if __name__ == "__main__":
   run_main()