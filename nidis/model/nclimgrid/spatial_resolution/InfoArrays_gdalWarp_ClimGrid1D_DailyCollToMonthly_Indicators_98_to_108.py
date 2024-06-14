#!/usr/bin/env python
from __future__ import division
import numpy as np
import os
import rasterio
from rasterio.features import shapes
import geopandas as gpd
from datetime import datetime, timedelta, date
import sys
import pandas as pd
import glob
import os
from calendar import monthrange
from osgeo import gdal
import shapely.speedups
import fiona
import logging
from pathlib import Path
from multiprocessing import Pool, cpu_count

shapely.speedups.enable()

def main(ArgYearInt: int, ArgMonthInt: int):

  # NOTE: sys.argv indices start at 1, not 0
  # Python arguments to this program will be (for now):
  #        ArgYearInt ArgMonthInt 
  # ArgNum   1          2          

  ssstart_Overall = datetime.now()

  #######BEGIN ANY EDITS REQUIRED#######

  ClimGrid1DShpFile = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/nClimGrid_as_poly_NoNans.shp'

  # ArgYearInt = int(round(float(sys.argv[1])))
  # ArgMonthInt = int(round(float(sys.argv[2])))

  # cmd = 'mkdir -p /discover/nobackup/projects/nca/syatheen/IMERG_Npzs/daily_Final_V06/'
  # os.system(cmd)
  path_to_save_data = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/IMERG_Npzs/daily_Final_V06'
  os.makedirs(path_to_save_data, exist_ok=True)

  ArrayFileName = os.path.join(
     path_to_save_data, 'IMERG_' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + '_ClimGrid1D.npz')

  SourceFileBasePath = '/discover/nobackup/projects/nca/syatheen/IMERG/daily_Final_V06_Tifs'
  SourceFileBasePathWrite = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/IMERG/daily_Final_V06_Tifs'

  os.makedirs(os.path.join(SourceFileBasePathWrite, 'TempCreatedFiles'), exist_ok=True)

  # IMERG_daily_LowerLimit = 0.
  # IMERG_daily_UpperLimit = 272478720.000000

  xres=0.125000000000/3
  yres=0.125000000000/3
  resample_alg = 'near'
  Width = 1385
  Height = 596
  output_bounds = [-124 - 17*xres, 24 + 13*yres, -67, 49 + 9*yres]

  #######END ANY EDITS REQUIRED#########

  #BEGIN GETTING PxlRowCol ETC SHAPEFILE DATA
  ClimGrid1DShp = gpd.read_file(ClimGrid1DShpFile)
  PxlRowCol_SortedList_FrmShpFile = sorted(ClimGrid1DShp.PxlRowCol.values.tolist())
  PxlRowCol_SortedArr_FrmShpFile = np.array(PxlRowCol_SortedList_FrmShpFile)
  PxlRow_SortedArr_FrmShpFile = (np.around(PxlRowCol_SortedArr_FrmShpFile // 10000)).astype(int)
  PxlCol_SortedArr_FrmShpFile = (np.around(PxlRowCol_SortedArr_FrmShpFile % 10000)).astype(int)
  #END GETTING PxlRowCol ETC SHAPEFILE DATA

  NumDaysInMonth = int(round(float(monthrange(ArgYearInt, ArgMonthInt)[1]))) 

  YYYYMMDD_Of_RefArrayForPrcntl = np.empty((NumDaysInMonth, 1), dtype=np.int32)
  YYYYMMDD_Of_RefArrayForPrcntl[:] = -9999
  RefArrayForPrcntl = np.empty((NumDaysInMonth, len(PxlRowCol_SortedList_FrmShpFile)))
  RefArrayForPrcntl[:] = np.NaN

  for WhichDayInMonth in range(1, NumDaysInMonth+1):

    YYYYMMDD_Of_RefArrayForPrcntl[WhichDayInMonth-1] = 10000*ArgYearInt + 100*ArgMonthInt + WhichDayInMonth 
    SourceFile = os.path.join(SourceFileBasePath, 'IMERG' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + format(WhichDayInMonth,'02') + '.tif')

    IfTifFileExists = os.path.exists(SourceFile)
    if IfTifFileExists:

      BaseFileName =  'IMERG' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + format(WhichDayInMonth,'02') 

      outfn = os.path.join(SourceFileBasePathWrite, 'TempCreatedFiles/' + BaseFileName + '_upsampTo_nCG.tif')

      try:
          os.remove(outfn)
      except OSError:
          pass

      ds = gdal.Warp(outfn, SourceFile, options = gdal.WarpOptions(resampleAlg=resample_alg, width=Width, height=Height, outputBounds=output_bounds, dstNodata = np.NaN))
      ds = None

      with rasterio.Env():
        with rasterio.open(outfn) as SrcInfo:
          ImageInfo = SrcInfo.read()

          ImageInfo = np.flip(ImageInfo, axis = 1)

          RefArrayForPrcntl[WhichDayInMonth-1, :] = ImageInfo[0, PxlRow_SortedArr_FrmShpFile, PxlCol_SortedArr_FrmShpFile]

        #end of with rasterio.open(..
      #end of with rasterio.Env()

    #end of if IfTifFileExists

    try:
        os.remove(outfn)
    except OSError:
        pass

  #end of for WhichDayInMonth in range(1, NumDaysInMonth+1)

  print("YYYYMMDD_Of_RefArrayForPrcntl.shape is ",YYYYMMDD_Of_RefArrayForPrcntl.shape)
  print("YYYYMMDD_Of_RefArrayForPrcntl is ",YYYYMMDD_Of_RefArrayForPrcntl)
  print("RefArrayForPrcntl.shape is ",RefArrayForPrcntl.shape)
  print("RefArrayForPrcntl is ",RefArrayForPrcntl)
  print("np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amin(np.isnan(RefArrayForPrcntl).sum(axis=0)))
  print("np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)) is ",np.amax(np.isnan(RefArrayForPrcntl).sum(axis=0)))
  print("np.amin(np.isnan(RefArrayForPrcntl).sum(axis=1)) is ",np.amin(np.isnan(RefArrayForPrcntl).sum(axis=1)))
  print("np.amax(np.isnan(RefArrayForPrcntl).sum(axis=1)) is ",np.amax(np.isnan(RefArrayForPrcntl).sum(axis=1)))
  print('overall min is ',np.nanmin(RefArrayForPrcntl),', overall max is ',np.nanmax(RefArrayForPrcntl))

  np.savez_compressed(ArrayFileName,
                      YYYYMMDD_Of_RefArrayForPrcntl = YYYYMMDD_Of_RefArrayForPrcntl,
                      RefArrayForPrcntl = RefArrayForPrcntl)

  eeend_Overall = datetime.now()
  eeelapsed_Overall = eeend_Overall - ssstart_Overall
  print(eeelapsed_Overall.seconds,"sec:",eeelapsed_Overall.microseconds,"microsec")

  return


def main_wrapper(args):
  return main(*args)


def main_multiprocessing(
            StartDate,
            EndDate,
            n_processes: int = 100
        ):

  logging.info("Inside main multiprocessing")

  # Generate date combinations
  date_list = pd.date_range(start=StartDate, end=EndDate, freq='MS')

  # Generating combination of parameters
  multiprocessing_arguments = []
  for mdate in date_list:
    multiprocessing_arguments.append([mdate.year, mdate.month])

  # Start processing
  logging.info(f'Initiating {len(multiprocessing_arguments)} processes.')

  # temporary for testing
  # multiprocessing_arguments = multiprocessing_arguments[:1]
  # logging.info(f'Only processing {multiprocessing_arguments}')

  p = Pool(processes=n_processes)
  p.starmap(
    main_wrapper,
    zip(multiprocessing_arguments)
  )

  return
