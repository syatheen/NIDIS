import os
import sys
import time
import logging
import argparse
import numpy as np
from glob import glob
from datetime import datetime
from multiprocessing import Pool, cpu_count
from nidis.model.Parsers import percentile_creation_api

from nidis.model.Metadata import DictofSpatialAndWeeklyResolutionMapping
from nidis.model.nclimgrid.percentile_creation import \
    PrepSingle_ClimGrid1D_NLDAS_2_daily_CorrToMonthlyPerc_Indicators_44_to_55 \
    as indicators_44_to_55
from nidis.model.nclimgrid.percentile_creation import \
    PrepSingle_ClimGrid1D_NLDAS_2_daily_Indicators_56_to_67 \
    as indicators_56_to_67


def main():

    # measure time of execution
    start_time = time.time()

    # gather arguments
    args = percentile_creation_api()

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
    if indicator >= 44 and indicator <= 55:
        indicators_44_to_55.main(
            DictofSpatialAndWeeklyResolutionMapping[indicator]['ArgLSM'],
            DictofSpatialAndWeeklyResolutionMapping[indicator]['ArgVariable'],
            'NA'
        )
    elif indicator >= 56 and indicator <= 63:
        indicators_56_to_67.main(
            DictofSpatialAndWeeklyResolutionMapping[indicator]['ArgLSM'],
            DictofSpatialAndWeeklyResolutionMapping[indicator]['ArgVariable'],
            'NA'
        )
    elif indicator >= 64 and indicator <= 67:
        indicators_56_to_67.main(
            DictofSpatialAndWeeklyResolutionMapping[indicator]['ArgLSM'],
            DictofSpatialAndWeeklyResolutionMapping[indicator]['ArgVariable'],
            DictofSpatialAndWeeklyResolutionMapping[indicator]['ArgHUC'],
        )

    logging.info(f'End time: {time.time() - start_time}')
    return


# -----------------------------------------------------------------------------
# Invoke the main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
