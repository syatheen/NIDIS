#!/usr/bin/env python
from __future__ import division
import numpy as np
import os
import logging
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
from pathlib import Path
from multiprocessing import Pool, cpu_count

shapely.speedups.enable()



def main(ArgLSM, ArgVariable, ArgYearInt, ArgMonthInt, ArgHUC):

    # NOTE: sys.argv indices start at 1, not 0
    # Python arguments to this program will be (for now):
    #        ArgLSM ArgVariable ArgYearInt ArgMonthInt ArgHUC
    # ArgNum   1      2           3          4         5
    logging.info(f'{ArgLSM}, {ArgVariable}, {ArgYearInt}, {ArgMonthInt}')

    ssstart_Overall = datetime.now()

    # new addition from climdiv
    # Options are H02 (for HUC02), H04 (for HUC04), H06 (for HUC06), H08 (for HUC08)
    if ArgHUC == 'H02':
        HUC_FileNameBase = 'test02'
    elif ArgHUC == 'H04':
        HUC_FileNameBase = 'test04'
    elif ArgHUC == 'H06':
        HUC_FileNameBase = 'test06'
    elif ArgHUC == 'H08':
        HUC_FileNameBase = 'test08'

    HUC_FileNameBase = os.path.join(
        '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/NLDAS_2_daily',
        HUC_FileNameBase
    )

    #######BEGIN ANY EDITS REQUIRED#######

    ClimGrid1DShpFile = '/discover/nobackup/syatheen/Sujay/DeepLearning/Data/ML_Testcases/Drought_USDM/nClimGrid/nClimGrid_as_poly_NoNans.shp'

    # This are now defined from the wrapper script
    # ArgLSM = sys.argv[1]
    # ArgVariable = sys.argv[2]
    # ArgYearInt = int(round(float(sys.argv[3])))
    # ArgMonthInt = int(round(float(sys.argv[4])))

    # cmd = 'mkdir -p /discover/nobackup/projects/nca/syatheen/NLDAS_2_daily_Npzs/'
    # os.system(cmd)

    path_to_save_data = '/discover/nobackup/projects/nca/jacaraba/NIDIS_Data/NLDAS_2_daily_Npzs'
    os.makedirs(path_to_save_data, exist_ok=True)

    ArrayFileName = os.path.join(
        path_to_save_data,
        f'{ArgLSM}_{ArgVariable}_{format(ArgYearInt, "04")}{format(ArgMonthInt,"02")}_{ArgHUC}_ClimGrid1D.PERW.npz'
    )

    SourceFileBasePath = '/discover/nobackup/projects/nca/syatheen/'

    # NLDAS_2_daily_LowerLimit = 0.
    # NLDAS_2_daily_UpperLimit = 100.

    NLDAS_2_daily_LowerLimit = 0.
    NLDAS_2_daily_ZerosLowerLimit = 50.49504470825193 # 50.495044708251945
    #                                50.49504470825195312500 in Python
    NLDAS_2_daily_ZerosUpperLimit = 50.49504470825198 # 50.49504470825197
    NLDAS_2_daily_UpperLimit = 100.

    xres = 0.125000000000/3
    yres = 0.125000000000/3
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

    # new addition from climdiv
    # TODO: What is this looking for????
    IfHUCTifFileExists = os.path.exists(HUC_FileNameBase + '.tif')

    for WhichDayInMonth in range(1, NumDaysInMonth+1):

        YYYYMMDD_Of_RefArrayForPrcntl[WhichDayInMonth-1] = 10000*ArgYearInt + 100*ArgMonthInt + WhichDayInMonth 
        SourceFile = SourceFileBasePath + 'NLDAS_2_daily/' + ArgLSM + '_' + ArgVariable + '/' + ArgLSM + '.' + ArgVariable + '.' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + format(WhichDayInMonth,'02') + '.PERW.tif'
        logging.info(f'SourceFile {SourceFile}')
        logging.info(f'HUC File {HUC_FileNameBase}.tif')

        # check for file existance
        assert os.path.exists(SourceFile), \
            f'{SourceFile} does not exist, decompress the original data?'

        # check for file permissions
        assert os.access(SourceFile, os.R_OK), \
            f'Cannot read {SourceFile}, make sure permissions are correct.'

        BaseFileName = ArgLSM + '.' + ArgVariable + '.' + format(ArgYearInt,'04') + format(ArgMonthInt,'02') + format(WhichDayInMonth,'02') + '.PERW' 
        # outfn = SourceFileBasePath + 'NLDAS_2_daily/TempCreatedFiles/' + BaseFileName + '_upsampTo_nCG.tif'
        outfn = os.path.join(path_to_save_data, 'NLDAS_2_daily/TempCreatedFiles/', BaseFileName + '_upsampTo_nCG.tif')
        os.makedirs(Path(outfn).parent, exist_ok=True)

        IfTifFileExists = os.path.exists(SourceFile)
        # if IfTifFileExists:
        # new addition from climdiv
        if IfTifFileExists and IfHUCTifFileExists:

            try:
                # os.remove('/discover/nobackup/projects/nca/syatheen/NLDAS_2_daily/TempCreatedFiles/{}_upsampTo_nCG.tif'.format(BaseFileName))
                os.remove(outfn)
            except OSError:
                pass

            ds = gdal.Warp(outfn, SourceFile, options = gdal.WarpOptions(resampleAlg=resample_alg, width=Width, height=Height, outputBounds=output_bounds, dstNodata = np.NaN))
            ds = None

            with rasterio.Env():
                with rasterio.open(outfn) as SrcInfo:
                    with rasterio.open(HUC_FileNameBase + '.tif') as HUCSrcInfo:

                        # with rasterio.open('/discover/nobackup/projects/nca/syatheen/NLDAS_2_daily/TempCreatedFiles/{}_upsampTo_nCG.tif'.format(BaseFileName)) as SrcInfo:
                        #with rasterio.open(outfn) as SrcInfo:
                        ImageInfo = SrcInfo.read()
                        HUCImageInfo = HUCSrcInfo.read()
                        print("SIZES OF IMAGE AND HUC", ImageInfo.shape, HUCImageInfo.shape)

                        # new addition from nclimdiv script
                        # Idxs = np.where((ImageInfo >= NLDAS_2_daily_ZerosLowerLimit) & (ImageInfo <= NLDAS_2_daily_ZerosUpperLimit))
                        # ImageInfo[Idxs] = 0.0

                        # ImageInfo = np.flip(ImageInfo, axis = 1)
                        # HUCImageInfo = np.flip(HUCImageInfo, axis = 1)

                        # Idxs = np.where( (HUCImageInfo < 0.) & (~np.isnan(ImageInfo)) )
                        # ImageInfo[Idxs] = np.NaN

                        # Uniq_PosHUCs = np.unique(HUCImageInfo[np.where( HUCImageInfo > 0.5)])

                        # for ThisUniq_PosHUCs in Uniq_PosHUCs:
                        #    Idxs = np.where(HUCImageInfo == ThisUniq_PosHUCs)
                        #    if (np.isnan(np.nanmean(ImageInfo[Idxs]))):
                        #        print(WhichDayInMonth, ' ', ThisUniq_PosHUCs, ' : All NaNs!')
                        #    ImageInfo[Idxs] = np.nanmean(ImageInfo[Idxs])

                        # ImageInfo = ImageInfo.astype(np.float32) 

                        # RefArrayForPrcntl[WhichDayInMonth-1, :] = ImageInfo[0, PxlRow_SortedArr_FrmShpFile, PxlCol_SortedArr_FrmShpFile]

        try:
            # os.remove('/discover/nobackup/projects/nca/syatheen/NLDAS_2_daily/TempCreatedFiles/{}_upsampTo_nCG.tif'.format(BaseFileName))
            os.remove(outfn)
        except OSError:
            pass

    #end of for WhichDayInMonth in range(1, NumDaysInMonth+1)

    print("YYYYMMDD_Of_RefArrayForPrcntl.shape is ",YYYYMMDD_Of_RefArrayForPrcntl.shape)
    # print("YYYYMMDD_Of_RefArrayForPrcntl is ",YYYYMMDD_Of_RefArrayForPrcntl)
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
            ArgLSMList,
            ArgVariableList,
            StartDate,
            EndDate,
            ArgHUC,
            n_processes: int = 100
        ):

    logging.info("Inside main multiprocessing")

    # Generate date combinations
    date_list = pd.date_range(start=StartDate, end=EndDate, freq='MS')

    # Generating combination of parameters
    multiprocessing_arguments = []
    for lsm in ArgLSMList:
        for variable in ArgVariableList:
            for mdate in date_list:
                multiprocessing_arguments.append(
                    [lsm, variable, mdate.year, mdate.month, ArgHUC])

    # Start processing
    logging.info(f'Initiating {len(multiprocessing_arguments)} processes.')

    # temporary for testing
    multiprocessing_arguments = multiprocessing_arguments[:1]
    logging.info(f'Only processing {multiprocessing_arguments}')

    p = Pool(processes=n_processes)
    p.starmap(
        main_wrapper,
        zip(multiprocessing_arguments)
    )

    return
