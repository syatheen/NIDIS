import os
import sys
import time
import logging
import argparse
import numpy as np
from glob import glob
from datetime import datetime
from multiprocessing import Pool, cpu_count
from nidis.model.Parsers import spatial_resolution_api

from nidis.model.nclimgrid.spatial_resolution import \
    InfoArrays_gdalWarp_ClimGrid1D_DailyCollToMonthly_Indicators_52_to_63 as indicators_52_to_63
from nidis.model.nclimgrid.spatial_resolution import \
    InfoArrays_gdalWarp_ClimGrid1D_DailyCollToMonthly_Indicators_64_to_67 as indicators_64_to_67
from nidis.model.nclimgrid.spatial_resolution import \
    InfoArrays_gdalWarp_ClimGrid1D_DailyCollToMonthly_Indicators_98_to_108 as indicators_98_to_108


def main():

    # measure time of execution
    start_time = time.time()

    # gather arguments
    args = spatial_resolution_api()

    # set indicator
    # training script expects them in the 0-112 format, we
    # will substract 1 just to keep it in line with spread sheet
    indicator = args.indicator

    # set logging
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s; %(levelname)s; %(message)s", "%Y-%m-%d %H:%M:%S"
    )

    # set console output
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # processing indicator
    logging.info(f'Processing indicator: {indicator}')

    # select indicator to process
    if indicator >= 52 and indicator <= 63:
        indicators_52_to_63.main_multiprocessing(
            args.lsm_list, args.variable_list,
            args.start_date, args.end_date)
    elif indicator >= 64 and indicator <= 67:
        indicators_64_to_67.main_multiprocessing(
            args.lsm_list, args.variable_list,
            args.start_date, args.end_date, args.huc_value)
    elif indicator >= 98 and indicator <= 108:
        indicators_98_to_108.main_multiprocessing(
            args.start_date, args.end_date
        )
    logging.info(f'End time: {time.time() - start_time}')
    return


# -----------------------------------------------------------------------------
# Invoke the main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
