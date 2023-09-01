"""
Write a function takes a list of dictionaries describing `dogs` and returns a list of the names of all the pug owners.


get_pug_owners([
      {'name': 'Beatrice', 'breed': 'Lurcher', 'owner': 'Tom'},
      {'name': 'Max', 'breed': 'Pug', 'owner': 'Izzi'},
      {'name': 'Poppy', 'breed': 'Pug', 'owner': 'Anat'}
    ]) // returns ['Izzi', 'Anat']

get_pug_owners([
      {'name': 'Beatrice', 'breed': 'Lurcher', 'owner': 'Tom'},
    ]) // returns []

get_pug_owners([]) // returns []

"""

def get_pug_owners(dogs):
    # Your code here
    pass


def test_empty_list():
    assert get_pug_owners([]) == []


def test_single_invalid_dog():
    assert get_pug_owners([
      {'name': 'Beatrice', 'breed': 'Lurcher', 'owner': 'Tom'},
    ]) == []


def test_single_valid_dog():
    assert get_pug_owners([
      {'name': 'Beatrice', 'breed': 'Pug', 'owner': 'Tom'},
    ]) == ['Tom']


def test_many_invalid_dogs():
    dogs = [
      {'name': 'Beatrice', 'breed': 'Lurcher', 'owner': 'Tom'},
      {'name': 'Max', 'breed': 'Dalmation', 'owner': 'Izzi'},
      {'name': 'Poppy', 'breed': 'Alsatian', 'owner': 'Anat'}
    ]
    assert get_pug_owners(dogs) == []


def test_mixed_list():
    dogs = [
      {'name': 'Beatrice', 'breed': 'Lurcher', 'owner': 'Tom'},
      {'name': 'Max', 'breed': 'Pug', 'owner': 'Izzi'},
      {'name': 'Poppy', 'breed': 'Pug', 'owner': 'Anat'}
    ]
    assert get_pug_owners(dogs) == ['Izzi', 'Anat']
