import argparse
import logging

from . import __description__, __version__

parser = argparse.ArgumentParser(description=__description__)

group = parser.add_mutually_exclusive_group(required=True)

group.add_argument('-i', '--input', help='Pass the input directly as text', type=str, dest='input')
group.add_argument('-f', '--file', help='Pass the input as a file', type=str, dest='file')
group.add_argument('filename', nargs='?')  # So that usage can be python3 bcocr example.txt
group.add_argument('--version', action='version', version='bcocr {version}'.format(version=__version__))

parser.add_argument('-v', '--verbose', help='Increase logging output substantially', action='store_true')

args = parser.parse_args()

if not args.file and args.filename:
    args.file = args.filename

if args.verbose:
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('Verbose logging enabled.')
else:
    logging.basicConfig(level=logging.INFO)
