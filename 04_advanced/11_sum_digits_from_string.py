"""
Write a function that takes a `string` and `adds` all the numbers in the string together. 
The function should then return this total as an integer. 

Consecutive numbers should be treated as individual digits (e.g. '123' is the same as 1, 2, 3 and not 123).

sum_digits_from_string('1') # returns 1

sum_digits_from_string('168') # returns 15

sum_digits_from_string('he12ll3') # returns 6

sum_digits_from_string('northcoders') # returns 0

"""

def sum_digits_from_string(string):
    # Your code here
    pass


def test_empty_string():
    assert sum_digits_from_string('') == 0


def test_single_non_numeric_digit():
    assert sum_digits_from_string('a') == 0


def test_single_numeral():
    assert sum_digits_from_string('5') == 5
    assert sum_digits_from_string('8') == 8
    assert sum_digits_from_string('0') == 0


def test_numeral_string():
    assert sum_digits_from_string('168') == 15
    assert sum_digits_from_string('25580') == 20


def test_mixed_string():
    assert sum_digits_from_string('he12ll3') == 6
    assert sum_digits_from_string('We always play 4-4-2') == 10


def test_string_with_no_numbers():
    assert sum_digits_from_string('northcoders') == 0
    assert sum_digits_from_string('A fine bootcamp') == 0
