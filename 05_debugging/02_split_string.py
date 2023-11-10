"""
split_string is a function that takes a string and returns a list containing
all of the individual characters as separate elements.

Unfortunately, it looks like the function is currently throwing a TypeError.

Can you work out what needs changing to make the function pass all the tests?
"""


def split_string():
    return list(str)


# Do not change code below this line

def test_it_splits_strings():
    assert split_string('string') == ['s', 't', 'r', 'i', 'n', 'g']
    assert split_string('help') == ['h', 'e', 'l', 'p']
    assert split_string('Northcoders') == [
        'N', 'o', 'r', 't', 'h', 'c', 'o', 'd', 'e', 'r', 's']
