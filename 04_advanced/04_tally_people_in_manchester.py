"""
Write a function that takes a list of `people` dictionaries in the format:

[
    {
        'name': 'Emmeline',
        'lives': {
            'country': 'UK',
            'city': 'Manchester'
        },
        'age': 32
    }
]


The function should return the number of people who live in the
city of Manchester.

tally_people_in_manchester([{
    'name': 'Emmeline',
    'lives': { 'country': 'UK', 'city': 'Manchester' },
    'age': 32
    }]) # returns 1

tally_people_in_manchester([{
    'name': 'Carrie',
    'lives': { 'country': 'UK', 'city': 'Leeds' },
    'age': 32
    }]) # returns 0

tally_people_in_manchester([
    {
    'name': 'Carrie',
    'lives': { 'country': 'UK', 'city': 'Leeds' },
    'age': 32
    },
    { 'name': 'Ray',
    'lives': { 'country': 'UK', 'city': 'Manchester' },
    'age': 31
    }
    ]) # returns 1

tally_people_in_manchester([]) # returns 0

"""


def tally_people_in_manchester(people):
    # Your code here
    pass


def test_empty_list():
    assert tally_people_in_manchester([]) == 0


def test_single_person_not_in_manchester():
    people = [{'name': 'Carrie', 'lives': {
        'country': 'UK', 'city': 'Leeds'}, 'age': 32}]
    assert tally_people_in_manchester(people) == 0


def test_single_person_in_manchester():
    people = [{'name': 'Emmeline', 'lives': {
        'country': 'UK', 'city': 'Manchester'}, 'age': 32}]
    assert tally_people_in_manchester(people) == 1


def test_several_people():
    people = [
        {'name': 'Carrie',
         'lives': {'country': 'UK', 'city': 'Leeds'},
         'age': 32
         },
        {'name': 'Ray',
         'lives': {'country': 'UK', 'city': 'Manchester'},
         'age': 31
         },
        {'name': 'Simon',
         'lives': {'country': 'Middle Earth', 'city': 'Moria'},
         'age': 275
         },
        {'name': 'Cat',
         'lives': {'country': 'UK', 'city': 'Manchester'},
         'age': 42
         },
        {'name': 'Danika',
         'lives': {'country': 'UK', 'city': 'Manchester'},
         'age': 22
         }
    ]
    assert tally_people_in_manchester(people) == 3
