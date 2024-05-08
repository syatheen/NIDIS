import os
import sys
import time
import logging
import argparse
import numpy as np
from glob import glob
from datetime import datetime
from multiprocessing import Pool, cpu_count
#from nidis.model.CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas \
#    import main as CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_Main
#from nidis.model.Metadata import \
#    DictofNumNamePairs_Channels, DictofInitialToWord_Seasons
#from nidis.model.CombineMultipleFilesIntoSingle import \
#    CombineMultipleFilesIntoSingle, ArrayToNetCDF




def main():

    # measure time of execution
    start_time = time.time()

    # Process command-line args.
    desc = 'Use this application to perform CNN segmentation.'
    parser = argparse.ArgumentParser(description=desc)

    parser.add_argument('-i',
                        '--indicator',
                        type=int,
                        required=True,
                        default=None,
                        dest='indicator',
                        help='Indicator to process (goes from 1-113).')
    """
    parser.add_argument('-se',
                        '--season',
                        type=str,
                        nargs='*',
                        required=True,
                        dest='season_list',
                        help='Season to process',
                        default=['A', 'P', 'U', 'F', 'W'],
                        choices=['A', 'P', 'U', 'F', 'W'])

    parser.add_argument('-t',
                        '--task-file',
                        type=str,
                        required=False,
                        default=None,
                        dest='task_file',
                        help='Task file from where to grab the tasks.')

    parser.add_argument('-td',
                        '--task-dir',
                        type=str,
                        required=False,
                        default=None,
                        dest='task_dir',
                        help='Task directory to iterate through.')

    parser.add_argument('-it',
                        '--init-task',
                        type=int,
                        required=False,
                        default=0,
                        dest='init_task',
                        help='First task to work from.')

    parser.add_argument('-et',
                        '--end-task',
                        type=int,
                        required=False,
                        default=469758,
                        dest='end_task',
                        help='End task to work from.')

    parser.add_argument('-sd',
                        '--start-date',
                        type=str,
                        required=False,
                        default='20060103',
                        dest='start_date',
                        help='Date to start processing from.')

    parser.add_argument('-ed',
                        '--end-date',
                        type=str,
                        required=False,
                        default='20191231',
                        dest='end_date',
                        help='Date to end processing at.')

    parser.add_argument('-o',
                        '--output-dir',
                        type=str,
                        default=None,
                        required=True,
                        dest='output_dir',
                        help='Path to output directory')

    parser.add_argument('-p',
                        '--n-processes',
                        type=int,
                        required=False,
                        default=90,
                        dest='n_processes',
                        help='Number of concurrent processes.')

    parser.add_argument('-s',
                        '--step',
                        type=str,
                        nargs='*',
                        required=True,
                        dest='pipeline_step',
                        help='Pipeline step to perform',
                        default=['train'],
                        choices=['train', 'postprocess', 'delete'])
    """
    # gather arguments
    args = parser.parse_args()

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
