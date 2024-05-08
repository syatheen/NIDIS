import argparse


def spatial_resolution_api():

    # Process command-line args.
    desc = 'Use this application to perform spatial resolution fixes.'
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help=desc)

    # Subparser for NLDAS2
    nldas2_parser = subparsers.add_parser("NLDAS2")

    nldas2_parser.add_argument(
        '-i',
        '--indicator',
        type=int,
        required=True,
        default=None,
        dest='indicator',
        help='Indicator to process (goes from 1-113).')

    nldas2_parser.add_argument(
        '-l',
        '--lsm',
        type=str,
        nargs='*',
        required=True,
        dest='lsm_list',
        help='LSM to process',
        default=['Mosaic', 'Noah', 'SAC', 'VIC'],
        choices=['Mosaic', 'Noah', 'SAC', 'VIC'])

    nldas2_parser.add_argument(
        '-v',
        '--variable',
        type=str,
        nargs='*',
        required=True,
        dest='variable_list',
        help='Variable to process',
        default=['EVAP', 'SWE', 'RUN', 'STRM'],
        choices=['EVAP', 'SWE', 'RUN', 'STRM'])

    nldas2_parser.add_argument(
        '-sd',
        '--start-date',
        type=str,
        required=False,
        default='19800101',
        dest='start_date',
        help='Date to start processing from.')

    nldas2_parser.add_argument(
        '-ed',
        '--end-date',
        type=str,
        required=False,
        default='20210831',
        dest='end_date',
        help='Date to end processing at.')

    return parser.parse_args()
