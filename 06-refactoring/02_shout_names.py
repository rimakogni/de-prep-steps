"""
`shout_names` is a function that takes a list of names and returns a list
containing all of the names in capital letters followed by an
exclamation mark "!".

Refactor `shout_names` to use a list comprehension.

If you run pytest on this file, all tests should pass.
"""


def shout_names(names):
    shouted_names = []
    for name in names:
        shouted_names.append(name.upper() + '!')
    return shouted_names


# Do not change any code below this line

def test_returns_a_list():
    assert type(shout_names([])) == list


def test_no_names_produces_empty_list():
    assert shout_names([]) == []


def test_shouts_names():
    names = ['Carrie', 'Diya', 'Kyle', 'Christian']
    expected = ['CARRIE!', 'DIYA!', 'KYLE!', 'CHRISTIAN!']
    assert shout_names(names) == expected
    names = ['Maddie', 'Bethan', 'Andrea', 'Jade']
    expected = ['MADDIE!', 'BETHAN!', 'ANDREA!', 'JADE!']
    assert shout_names(names) == expected
