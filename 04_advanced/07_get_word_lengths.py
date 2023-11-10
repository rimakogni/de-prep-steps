"""
Write a function that takes a `string` and returns a list containing the
length of each word in that string.
If passed an empty string, the function should return an empty list.
Words will be separated by a single space.


get_word_lengths('hello') # returns [5]

get_word_lengths('hello everyone') # returns [5, 8]

get_word_lengths('this is a sentence') # returns [4, 2, 1, 8]

get_word_lengths('') # returns []

"""


def get_word_lengths(string):
    # Your code here
    pass


def test_empty_string():
    assert get_word_lengths('') == []


def test_single_word():
    assert get_word_lengths('hello') == [5]
    assert get_word_lengths('sesquipedalian') == [14]


def test_two_words():
    assert get_word_lengths('hello everyone') == [5, 8]


def test_many_words():
    assert get_word_lengths('this is a sentence') == [4, 2, 1, 8]
