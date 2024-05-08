import argparse


def spatial_resolution_api():

    # Process command-line args.
    desc = 'Use this application to perform spatial resolution fixes.'
    parser = argparse.ArgumentParser(description=desc)

"""
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
                        default=['train'],
                        choices=['train', 'postprocess', 'delete'])

    # gather arguments
    args = parser.parse_args()

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

    parser.add_argument('-d',
                        '--data-arguments',
                        type=str,
                        nargs='*',
                        required=True,
                        dest='data_arguments',
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
