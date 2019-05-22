"""Business Card OCR, or bcocr, is a tool to parse Business Card OCR strings to extract names, email addresses, and phone numbers
"""
import logging

from .args import args
from .parser import BusinessCardParser

if args.test:
    # run_tests()
    pass

else:
    if args.file:
        with open(args.file, 'r') as f:
            ocr_input = f.read()
    else:
        ocr_input = args.input

    logging.debug('Received input:\n{}'.format(ocr_input))
    parser = BusinessCardParser()
    contact_info = parser.get_contact_info(ocr_input)
    print(contact_info)
