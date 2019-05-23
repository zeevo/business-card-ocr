import logging
import re

import nltk
from nltk.corpus import stopwords


def only_digits(phone_number):
    """Remove all non-digits from the input phone_number string

    Args:
        phone_number (str): A phone number string

    Returns:
        str: The phone number without non-digits
    """
    return re.sub('[^0-9]', '', phone_number)


def has_substrings(candidate, comparison):
    """Returns all words in candidate that are a substring of comparison

    Args:
        candidate (str): any string
        email (str): a valid email string

    Returns:
        list[str]: All words that are substrings of the left half of the email
    """
    words = candidate.split(' ')
    comparison = comparison.lower()
    return [word for word in words if word.lower() in comparison]


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
        logging.info('Preparing NLTK dictionary')
        nltk.download('stopwords', quiet=True)
        self.phone_reg = re.compile(r'.*?(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4}).*?')
        self.email_reg = re.compile(r'.*?([^@|\s]+@[^@]+\.[^@|\s]+).*?')
        self.stopwords = stopwords.words('english')

    def get_contact_info(self, ocr_input):
        """Parse input to capture Name, Email, and Phone.

        Args:
            input (str): the Business Card OCR string to be parsed.

        return contact_info (ContactInfo): the ContactInfo extracted.
        """
        contact_info = ContactInfo()

        candidates = [line for line in ocr_input.split('\n') if line]  # remove blank lines

        phone_or_fax = {line: self.phone_reg.match(line) for line in candidates}  # map line to a candidate phone
        phone_or_fax = {line: match for line, match in phone_or_fax.items() if match}  # filter out non matches

        # find phone number among potential fax numbers
        phone = [match for line, match in phone_or_fax.items() if line.lower()[0] != 'f']
        phone = phone[0] if phone else None  # Get the first match

        if phone:
            logging.debug('Found Phone number [{0}] from candidate line [{1}]'.format(phone.group(1), phone.string))
            contact_info.phone_number = only_digits(phone.string)
            candidates.remove(phone.string)
        else:
            logging.debug('Did not find a Phone Number')

        # find email among candidates
        email = [self.email_reg.match(line) for line in candidates]
        email = [match for match in email if match]
        email = email[0] if email else None

        match_with_email = []
        if email:
            logging.debug('Found Email [{0}] from candidate line [{1}]'.format(email.group(1), email.string))
            contact_info.email_address = email.string
            candidates.remove(email.string)
            split = email.string.split('@')
            left_half = split[0]
            right_half = split[1]
            potential_company = [candidate for candidate in candidates if has_substrings(candidate, right_half)]
            if potential_company:
                candidates.remove(potential_company[0])
            match_with_email = [candidate for candidate in candidates if has_substrings(candidate, left_half)]
        else:
            logging.debug('Did not find an Email Address')

        if match_with_email:
            name = match_with_email[0]
        else:
            # fall back to our best guess based on removing common non-name words
            potential_names = [candidate for candidate in candidates if not self.contains_stopwords(candidate)]
            name = potential_names[0] if potential_names else None

        contact_info.name = name
        return contact_info

    def contains_stopwords(self, candidate_line):
        """Helper function to help bring more confidence to identifying names.

        Stopwords are simple english words like "the", "then", "a", 'etc".

        We can make the assumption that names do not contain stopwords. So by identifying if there are
        any stopwords in a line, we immediately know it is not a name.

        Note:
            wordnet from nltk contains a subset of english words and is not an exhaustive list.

        Args:
            input (str): the Business Card OCR string to be parsed

        return contact_info (ContactInfo): the ContactInfo extracted
        """
        return any(word in self.stopwords for word in candidate_line.split(' '))


class ContactInfo(object):
    """Wrapper around contact information parsed by a BusinessCardParser

    This allows us to select just the name, email, or phone number when needed,
    and not mix things up again.

    Args:
        name (str): a parsed name 
        email_address (str): a parsed email address
        phone_number (str): a parsed phone number

    Attributes:
        name (str): 
        email (str):
        phone (str):
    """

    def __init__(self, name=None, email_address=None, phone_number=None):
        self.name = name
        self.email_address = email_address
        self.phone_number = phone_number

    def __str__(self):
        return '\n'.join([
            'Name: {}'.format(self.name),
            'Email Address: {}'.format(self.email_address),
            'Phone Number: {}'.format(self.phone_number)
        ])

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
        return self.email_address

    def get_phone_number(self):
        """Returns the phone number formatted as a sequence of digits

        Returns:
            str: The parsed phone number
        """
        return self.phone_number
