"""
`get_excited` is a function that takes a piece of text and returns it with all
of the full stops (.) replaced by exclamation marks (!).

Refactor get_excited to use a string method. All of this code can be rewritten
in just one line with one string method...

If you run pytest on this file, all tests should pass.
"""


def get_excited(text):
    new_text = ''
    for char in text:
        if char == '.':
            new_text += '!'
        else:
            new_text += char
    return new_text


def test_empty_string_returns_empty_string():
    assert get_excited('') == ''


def test_no_full_stops_means_text_unchanged():
    text = 'the quick brown fox jumps over the lazy dog'
    assert get_excited(text) == text


def test_replaces_full_stops_with_excalamation_marks():
    text = 'Today is a great day.'
    expected = 'Today is a great day!'
    assert get_excited(text) == expected
    text = "We're gonna need a bigger boat."
    expected = "We're gonna need a bigger boat!"
    assert get_excited(text) == expected
    text = 'Woo. Woo. Woo. Who\'s ready to code?'
    expected = 'Woo! Woo! Woo! Who\'s ready to code?'
