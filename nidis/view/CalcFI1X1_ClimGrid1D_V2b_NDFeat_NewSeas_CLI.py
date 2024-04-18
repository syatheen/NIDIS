import os
import sys
import time
import logging
import argparse
from datetime import datetime
from multiprocessing import Pool
from nidis.model.CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas \
    import main as CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_Main


def run_calc(parameters):

    # calling a different script
    # python /discover/nobackup/jacaraba/development/benchmark-amy/CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_V2.py \
    # ${args[0]} ${args[1]} ${args[2]} ${args[3]} ${args[4]} ${args[5]} ${args[6]} ${args[7]} ${args[8]} ${args[9]} \
    # ${args[10]} >& NClcFI1X1_ClmGrd1D_V2b_ND_V2_${args[0]}${args[1]}${args[10]}${args[2]}To${args[3]}_${args[4]}${args[5]}_${args[6]}_${args[7]}_${args[8]}_${args[9]}.out
    # print(parameters)

    # ['N', 'N', '20060103', '20191231', 'USDM', 'CONUS', '113', '1', '38', '884', 'P']

    CalcFI1X1_ClimGrid1D_V2b_NDFeat_NewSeas_Main(
        IfMakeTargetBinary=parameters[0],  # Choices are 'Y' for yes, and 'N' for no
        IfIncludeD0AsDrought=parameters[1],  # Choices are 'Y' for yes, and 'N' for no
        BeginYYYYMMDD_Str=parameters[2],  # Beginning YYYYMMDD, this is also a Tuesday
        EndYYYYMMDD_Str=parameters[3],  # Ending YYYYMMDD, this is also a Tuesday
        TargetVariable=parameters[4],  # Choices are 'USDM', 'CPC_S' (for short-term), 'CPC_LE' (for long-term Eastern), and 'CPC_LW' (for long-term Western)  
        SpatialDomain=parameters[5],  # Choices are 'CONUS'
        WhichArgForNumInpLayers= 6,  # Which argument has info about number of input layers, goes to 6 since its indexing
        NumInpLayers=int(round(float(parameters[6]))), #int(round(float(sys.argv[7]))), # 113 for all input channels, 0 for All CPC Blend input channels, -10 for remotely-sensed, -11 for modeled, -12 for modeled+PrecipObs, -50 for all NDMC Blend input channels
        NumInpsForNDFracMI=parameters[7],
        WhichInpCombinForNDFracMI=int(round(float(parameters[8]))), #int(round(float(sys.argv[9]))), # 0-start
        Which_1D_Pixel=int(round(float(parameters[9]))), #int(round(float(sys.argv[10]))), # Which 1D number of nClimGrid pixels # 0-start
        WhichSeason=parameters[10], # Choices are 'P' for sPring (Mar-May), 'U' for sUmmer (Jun-Aug), 'F' for Fall (Sep-Nov), 'W' for Winter (Dec-Feb), 'A' for all-seasons-together,
        OutputDir=parameters[11]
    )
    return


def read_config(config_filename):
    """
    Read tasks[X].conf configuration file.
    """
    clean_lines = []
    file = open(config_filename, 'r')
    lines = file.readlines()
    for line in lines:
        clean_lines.append(line.strip().split(' ')[-11:])
    return clean_lines


def run_training(
            indicator,
            seasons_list,
            init_task,
            end_task,
            start_date,
            end_date,
            output_dir,
            n_processes: int = 90
        ):

    # IfMakeTargetBinary, Choices are 'Y' for yes, and 'N' for no
    # IfIncludeD0AsDrought, Choices are 'Y' for yes, and 'N' for no
    # Beginning YYYYMMDD, this is also a Tuesday
    # Ending YYYYMMDD, this is also a Tuesday
    # TargetVariable, Choices are 'USDM', 'CPC_S' (for short-term),
    #   'CPC_LE' (for long-term Eastern), and
    #   'CPC_LW' (for long-term Western)
    # SpatialDomain, Choices are 'CONUS'
    # NumInpLayers, 113 for all input channels, 0 for All CPC Blend
    #    input channels,
    #    -10 for remotely-sensed, -11 for modeled, -12 for modeled+
    # NumInpsForNDFracMI
    # WhichInpCombinForNDFracMI, 0-start
    # Which_1D_Pixel, Which 1D number of nClimGrid pixels # 0-start
    # WhichSeason, Choices are 'P' for sPring (Mar-May),
    #     'U' for sUmmer (Jun-Aug),
    #     'F' for Fall (Sep-Nov), 'W' for Winter (Dec-Feb),
    #     'A' for all-seasons-together

    # read configuration files
    all_tasks = []
    for season in seasons_list:

        output_dir_indicator = os.path.join(output_dir, season)
        os.makedirs(output_dir_indicator, exist_ok=True)

        for config_id in range(init_task, end_task):

            # general task command, go to documentation for
            # additional details on each position
            task = [
                'N',
                'N',
                start_date,
                end_date,
                'USDM',
                'CONUS',
                '113',
                '1',
                indicator - 1,
                config_id,
                season,
                output_dir_indicator
            ]
            all_tasks.append(task)

    logging.info(f'Prepared {len(all_tasks)}')

    # multiprocessing queue
    p = Pool(processes=n_processes)
    p.starmap(
        run_calc,
        zip(all_tasks)
    )
    return


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
                        default=['training', 'postprocessing', 'delete'],
                        choices=['training', 'postprocessing', 'delete'])

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

    # generate output directory
    indicator_output_dir = os.path.join(
        args.output_dir, f'indicator_{indicator}')
    os.makedirs(indicator_output_dir, exist_ok=True)

    # replaced when we developed the single file per 3 indicators
    # os.makedirs('FI1X1_ClmGrd1D_V2b_New/1/', exist_ok=True)
    # os.makedirs('SSiz1X1_ClmGrd1D_V2b_New/1/', exist_ok=True)
    # os.makedirs('WSiz1X1_ClmGrd1D_V2b_New/1/', exist_ok=True)

    if 'training' in args.pipeline_step:
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

    # if trainining
    # if postprocessing
    # if delete

    # TODO: Add postprocessing here
    # - regression testing
    # - netcdf creation
    # if netcdf file exists, do not process

    print("End time: ", time.time() - start_time)
    return


# -----------------------------------------------------------------------------
# Invoke the main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
