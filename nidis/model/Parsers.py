import argparse


def spatial_resolution_api():

    # Process command-line args.
    desc = 'Use this application to perform spatial resolution fixes.'
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help=desc)

    # Subparser for NLDAS2
    nldas2_parser = subparsers.add_parser("NLDAS2")
    nldas2huc_parser = subparsers.add_parser("NLDAS2HUC")
    imerg_parser = subparsers.add_parser("IMERG")
    globsnow_parser = subparsers.add_parser("GlobSnow")

    for subparser in [nldas2_parser, nldas2huc_parser]:

        # make this indicators a list of things you can add
        subparser.add_argument(
            '-i',
            '--indicator',
            type=int,
            required=True,
            default=None,
            dest='indicator',
            help='Indicator to process (goes from 1-113).')

        # make this optional and map to the dict
        subparser.add_argument(
            '-l',
            '--lsm',
            type=str,
            nargs='*',
            required=True,
            dest='lsm_list',
            help='LSM to process',
            default=['Mosaic', 'Noah', 'SAC', 'VIC'],
            choices=['Mosaic', 'Noah', 'SAC', 'VIC'])

        # make this optional use mapping from dict
        subparser.add_argument(
            '-v',
            '--variable',
            type=str,
            nargs='*',
            required=True,
            dest='variable_list',
            help='Variable to process',
            default=['EVAP', 'SWE', 'RUN', 'STRM'],
            choices=['EVAP', 'SWE', 'RUN', 'STRM'])

        subparser.add_argument(
            '-sd',
            '--start-date',
            type=str,
            required=False,
            default='19800101',
            dest='start_date',
            help='Date to start processing from.')

        subparser.add_argument(
            '-ed',
            '--end-date',
            type=str,
            required=False,
            default='20210831',
            dest='end_date',
            help='Date to end processing at.')

    # general parsers
    for subparser in [imerg_parser, globsnow_parser]:

        # make this indicators a list of things you can add
        subparser.add_argument(
            '-i',
            '--indicator',
            type=int,
            required=True,
            default=None,
            dest='indicator',
            help='Indicator to process (goes from 1-113).')

        subparser.add_argument(
            '-sd',
            '--start-date',
            type=str,
            required=False,
            default='19800101',
            dest='start_date',
            help='Date to start processing from.')

        subparser.add_argument(
            '-ed',
            '--end-date',
            type=str,
            required=False,
            default='20210831',
            dest='end_date',
            help='Date to end processing at.')

    # make this optional use mapping from metadata dict
    nldas2huc_parser.add_argument(
        '-hu',
        '--huc-value',
        type=str,
        required=True,
        dest='huc_value',
        help='HUC value to process',
        default='H04',
        choices=['H02', 'H04', 'H06', 'H08'])

    return parser.parse_args()

def weekly_resolution_api():

    # Process command-line args.
    desc = 'Use this application to perform weekly resolution fixes.'
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-i',
        '--indicator',
        type=int,
        required=True,
        default=None,
        dest='indicator',
        help='Indicator to process (goes from 1-113).')

    return parser.parse_args()

def percentile_creation_api():

    # Process command-line args.
    desc = 'Use this application to perform percentile creation.'
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-i',
        '--indicator',
        type=int,
        required=True,
        default=None,
        dest='indicator',
        help='Indicator to process (goes from 1-113).')

    return parser.parse_args()
