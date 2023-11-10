"""
Write a function that takes a `string` and returns a string with all of the
letter characters replaced with an 'X'.
Any non-letter characters (e.g. punctuation, symbols) should be left as they
are.

replace_letters_with_x('a') # returns 'X'

replace_letters_with_x('A') # returns 'X'

replace_letters_with_x('hello') # returns 'XXXXX'

replace_letters_with_x('Hello!') # returns 'XXXXX!'

replace_letters_with_x('Do you like coding?') # returns 'XX XXX XXXX XXXXXX?'

"""


def replace_letters_with_x(string):
    # Your code here
    pass


def test_empty_string():
    assert replace_letters_with_x('') == ''


def test_single_non_letter_character():
    assert replace_letters_with_x('5') == '5'
    assert replace_letters_with_x('&') == '&'


def test_single_letter():
    assert replace_letters_with_x('a') == 'X'
    assert replace_letters_with_x('K') == 'X'


def test_several_letters():
    assert replace_letters_with_x('Kaboom') == 'XXXXXX'
    assert replace_letters_with_x('Northcoders') == 'XXXXXXXXXXX'


def test_several_characters():
    assert replace_letters_with_x('Kaboom!') == 'XXXXXX!'
    assert replace_letters_with_x('Northcoders?') == 'XXXXXXXXXXX?'


def test_several_words():
    assert replace_letters_with_x(
        'Do you like coding?') == 'XX XXX XXXX XXXXXX?'
