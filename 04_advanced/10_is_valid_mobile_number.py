"""
Write a function that takes a string of a mobile number (`mobile_number`). It should return `True` if the number is a valid UK number and `False` if not.

A valid mobile number may begin with:

1. '07' followed by 9 more digits.
2. '+447' followed by 9 more digits.
3. '00447' followed by 9 more digits.

Anything else is `invalid`.

is_valid_mobile_number('07726') # returns False

is_valid_mobile_number('07123456789') # returns True

is_valid_mobile_number('+447123456789') # returns True

is_valid_mobile_number('00447123456789') # returns True

is_valid_mobile_number('0712345678!') # returns False
"""

def is_valid_mobile_number(mobile_number):
    # Your code here
    pass


def test_empty_string_invalid():
    assert not is_valid_mobile_number('')


def test_length_less_than_eleven_is_false():
    assert not is_valid_mobile_number('0754321')


def test_length_more_than_fourteen_invalid():
    assert not is_valid_mobile_number('004471234567890')


def test_valid_examples_length_eleven():
    assert is_valid_mobile_number('07123456789')
    assert is_valid_mobile_number('07284619462')


def test_invalid_examples_length_eleven():
    assert not is_valid_mobile_number('+4471234567')
    assert not is_valid_mobile_number('00447876543')


def test_length_twelve_invalid():
    assert not is_valid_mobile_number('071234567890')


def test_valid_examples_length_thirteen():
    assert is_valid_mobile_number('+447123456789')
    assert is_valid_mobile_number('+447395612859')


def test_invalid_examples_length_thirteen():
    assert not is_valid_mobile_number('0044712345678')
    assert not is_valid_mobile_number('0739561285901')


def test_valid_examples_length_fourteen():
    assert is_valid_mobile_number('00447123456789')
    assert is_valid_mobile_number('00447654297190')


def test_invalid_examples_length_fourteen():
    assert not is_valid_mobile_number('+4471234567890')
    assert not is_valid_mobile_number('07102938475610')


def test_invalid_if_contains_non_numeric_characters_other_than_first():
    assert not is_valid_mobile_number('0728461a462')
    assert not is_valid_mobile_number('+4473956+2859')
    assert not is_valid_mobile_number('00447123!56789')
