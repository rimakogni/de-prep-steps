"""
Write a function that takes a list of `words` and returns a list containing all of the words that are 
palindromes (the same word forwards and backwards, e.g. 'pip').


get_palindromes(['racecar']) # returns ['racecar']

get_palindromes(['dog', 'dud', 'car', 'mum']) # returns ['dud', 'mum']

get_palindromes(['apple', 'orange', 'banana']) # returns []

get_palindromes([]) # returns []

"""

def get_palindromes(words):
    # Your code here
    pass


def test_empty_list():
    assert get_palindromes([]) == []


def test_single_invalid_item():
    assert get_palindromes(['boom']) == []


def test_single_valid_item():
    assert get_palindromes(['racecar']) == ['racecar']


def test_several_items():
    assert get_palindromes(['dog', 'dud', 'car', 'mum']) == ['dud', 'mum']


def test_several_invalid_items():
    assert get_palindromes(['apple', 'orange', 'banana']) == []