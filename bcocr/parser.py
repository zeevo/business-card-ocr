import logging
import re


class BusinessCardParser(object):
    """Parse Business Card OCR input to extract the Name, Email, and Phone Number

    Business Card OCR input example:

    FOO BAR LTD
    Mike Smith
    Senior Software Engineer
    (410)555-1234
    msmith@foobar.com

    ==> get_contact_info() ==>

    ContactInfo
        name: Mike Smith
        phone: 4105551234
        email: msmith@foobar.com

    Attributes:
        email_reg (str): Regex to match emails
    """

    def __init__(self):
        self.email_reg = re.compile('')
        pass

    def get_contact_info(self, ocr_input):
        """Parse input to capture Name, Email, and Phone

        Args:
            input (str): the Business Card OCR string to be parsed

        return contact_info (ContactInfo): the ContactInfo extracted
        """
        pass


class ContactInfo(object):
    """Wrapper around contact information parsed by a BusinessCardParser

    This allows us to select just the name, email, or phone number when needed,
    and not mix things up again.

    Args:
        name (str): a parsed name 
        email (str): a parsed email
        phone (str): a parsed phone number

    Attributes:
        name (str): 
        email (str):
        phone (str):
    """

    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def __str__(self):
        pass

    def get_name(self):
        """Returns the full name of the individual (eg. John Smith, Susan Malick)

        Returns:
            str: The parsed name
        """
        return self.name

    def get_email_address(self):
        """Returns the email address

        Returns:
            str: The parsed email
        """
        return self.email

    def get_phone_number(self):
        """Returns the phone number formatted as a sequence of digits

        Returns:
            str: The parsed phone number
        """
        return self.phone_number
