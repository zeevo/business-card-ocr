"""Business Card OCR, or bcocr, is a tool to parse Business Card OCR strings to extract names, email addresses, and phone numbers
"""
import logging

from .args import args
from .parser import BusinessCardParser
import os

if args.file:
    if not os.path.isfile(args.file):
        logging.info('Could not find file {0}. Does it exist? Is it a directory?'.format(args.file))
        exit(1)
    with open(args.file, 'r') as f:
        ocr_input = f.read()
else:
    ocr_input = args.input

logging.debug('Received input:\n\n{}\n\n'.format(ocr_input))
parser = BusinessCardParser()
contact_info = parser.get_contact_info(ocr_input)
logging.info('Finished')
logging.info('Contact Info:\n\n{}'.format(contact_info))
