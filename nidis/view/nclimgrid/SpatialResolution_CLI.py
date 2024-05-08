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

#from nidis.model.CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas \
#    import main as CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_Main
#from nidis.model.Metadata import \
#    DictofNumNamePairs_Channels, DictofInitialToWord_Seasons
#from nidis.model.CombineMultipleFilesIntoSingle import \
#    CombineMultipleFilesIntoSingle, ArrayToNetCDF




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

    """
    # set filename output
    log_filename = \
        f'{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}' + \
        f'Indicator_{indicator}.log'
    logs_output_dir = os.path.join(args.output_dir, 'Logs')
    os.makedirs(logs_output_dir, exist_ok=True)
    fh = logging.FileHandler(
        os.path.join(logs_output_dir, log_filename))
    fh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    if len(logger.handlers) > 2:
        # remove the root logger
        logger.handlers.pop(0)

    # generate output directory for indicator
    indicator_output_dir = os.path.join(
        args.output_dir, f'indicator_{indicator}')
    os.makedirs(indicator_output_dir, exist_ok=True)

    # set and generate output directory for postprocessing
    postprocessed_output_dir = os.path.join(
        args.output_dir, 'Outputs')
    os.makedirs(postprocessed_output_dir, exist_ok=True)
    """
    # replaced when we developed the single file per 3 indicators
    # os.makedirs('FI1X1_ClmGrd1D_V2b_New/1/', exist_ok=True)
    # os.makedirs('SSiz1X1_ClmGrd1D_V2b_New/1/', exist_ok=True)
    # os.makedirs('WSiz1X1_ClmGrd1D_V2b_New/1/', exist_ok=True)

    """
    if 'train' in args.pipeline_step:
        run_training(
            indicator,
            seasons_list=args.season_list,
            init_task=args.init_task,
            end_task=args.end_task,
            start_date=args.start_date,
            end_date=args.end_date,
            output_dir=indicator_output_dir,
            n_processes=args.n_processes
        )

    if 'postprocess' in args.pipeline_step:
        logging.info(
            f'Running postprocessing for {indicator}, seasons {args.season_list}')
        run_postprocessing(
            indicator,
            seasons_list=args.season_list,
            indicator_output_dir=indicator_output_dir,
            postprocessed_output_dir=postprocessed_output_dir
        )

    if 'delete' in args.pipeline_step:
        logging.info('I am supposed to delete on this step')

    print("End time: ", time.time() - start_time)
    return
    """

# -----------------------------------------------------------------------------
# Invoke the main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
