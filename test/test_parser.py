from bcocr.parser import (
    only_digits,
    has_substrings,
    BusinessCardParser,
    ContactInfo
)


def test_only_digits():
    digits = only_digits('213abc456')
    assert digits == '213456'


def test_only_digits_again():
    digits = only_digits('asdbdas')
    assert digits == ''


def test_has_substrings():
    line = 'The quick brown fox'
    comparison = 'quick'
    assert has_substrings(line, comparison)


def test_does_not_have_substrings():
    line = 'Foo bar'
    comparison = 'quick'
    assert not has_substrings(line, comparison)


def test_get_contact_info():
    parser = BusinessCardParser()
    mock_input = '\n'.join([
        'Arthur Wilson',
        'Software Engineer',
        'Decision & Security Technologies',
        'ABC Technologies',
        '123 North 11th Street',
        'Suite 229',
        'Arlington, VA 22209',
        'Tel: +1 (703) 555-1259',
        'Fax: +1 (703) 555-1200',
        'awilson@abctech.com',
    ])

    info = parser.get_contact_info(mock_input)

    assert info.name == 'Arthur Wilson'
    assert info.email_address == 'awilson@abctech.com'
    assert info.phone_number == '17035551259'


def test_get_contact_info_again():
    parser = BusinessCardParser()
    mock_input = '\n'.join([
        'Foobar Technologies',
        'Analytic Developer',
        'Lisa Haung',
        '1234 Sentry Road',
        'Columbia, MD 12345',
        'Phone: 410-555-1234',
        'Fax: 410-555-4321',
        'lisa.haung@foobartech.com',
    ])

    info = parser.get_contact_info(mock_input)

    assert info.name == 'Lisa Haung'
    assert info.email_address == 'lisa.haung@foobartech.com'
    assert info.phone_number == '4105551234'


def test_get_contact_info_no_input():
    parser = BusinessCardParser()
    mock_input = ''

    info = parser.get_contact_info(mock_input)

    assert info.name == None
    assert info.email_address == None
    assert info.phone_number == None


def test_get_contact_info_junk_data():
    parser = BusinessCardParser()
    mock_input = '\n\n\n\n'

    info = parser.get_contact_info(mock_input)
    assert info.name == None
    assert info.email_address == None
    assert info.phone_number == None
