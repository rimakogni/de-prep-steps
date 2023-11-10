"""
shrek_characters is a function that takes a list of movie characters and
returns a list of only the characters from the film franchise, Shrek.

Refactor shrek_characters to use a comprehension.

If you run pytest on this file, all tests should pass.
"""


def shrek_characters(characters):
    shreks = []
    for character in characters:
        if 'Shrek' in character['movie']:
            shreks.append(character['name'])
    return shreks


# Do not change any code below this line

def test_empty_list_of_characters_produces_empty_list():
    assert shrek_characters([]) == []


def test_returns_empty_list_if_no_characters_from_shrek():
    characters = [
        {
            'name': 'Cedric Diggory',
            'movie': 'Harry Potter and the Goblet of Fire'
        },
        {'name': 'Elle Woods', 'movie': 'Legally Blonde'},
        {'name': 'Paddington Bear', 'movie': 'Paddington 2'},
    ]
    assert shrek_characters(characters) == []


def test_all_characters_if_all_in_shrek():
    characters = [
        {
            'name': 'Shrek',
            'movie': 'Shrek',
        },
        {'name': 'Lord Farquaad', 'movie': 'Shrek'},
        {'name': 'Magic Mirror', 'movie': 'Shrek'},
    ]
    assert shrek_characters(characters) == [
        'Shrek', 'Lord Farquaad', 'Magic Mirror']


def test_returns_any_characters_that_are_in_shrek():
    characters = [
        {
            'name': 'Cher',
            'movie': 'Clueless',
        },
        {
            'name': 'Hans Gruber',
            'movie': 'Die Hard',
        },
        {
            'name': 'Donkey',
            'movie': 'Shrek',
        },
        {
            'name': 'Lola',
            'movie': 'Shark Tale',
        },
    ]
    assert shrek_characters(characters) == ['Donkey']


def test_returns_any_characters_from_shrek_franchise():
    characters = [
        {'name': 'Fiona', 'movie': 'Shrek'},
        {'name': 'Fairy Godmother', 'movie': 'Shrek 2'},
        {'name': 'Cookie', 'movie': 'Shrek 4'},
        {'name': 'Puss In Boots', 'movie': 'Shrek 2'},
        {'name': 'Han Solo', 'movie': 'Star Wars: A New Hope'},
    ]
    assert shrek_characters(characters) == [
        'Fiona', 'Fairy Godmother', 'Cookie', 'Puss In Boots']
