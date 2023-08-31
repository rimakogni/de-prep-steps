"""
Write a function that takes a list of dictionaries with the format from create_northcoder (`northcoders`), and returns a new list of the users' names as strings.

northcoders = [
  {
    'name': 'Callum',
    'age': 31,
    'language': 'JavaScript'
  },
  {
    'name': 'Carrie',
    'age': 32,
    'language': 'Python'
  }
]

get_northcoders_names(northcoders) # returns ['Callum', 'Carrie']
"""

def get_northcoders_names(northcoders):
    # Your code here
    pass


def test_returns_empty_list_if_input_empty():
    assert get_northcoders_names([]) == []


def test_northcoders_missing_names_omitted():
    northcoders = [
        {
            'age': 32,
            'language': 'Python'
        }
    ]
    assert get_northcoders_names(northcoders) == []


def test_gets_names_of_northcoders():
    northcoders = [
        {
            'name': 'Callum',
            'age': 31,
            'language': 'JavaScript'
        },
        {
            'name': 'Carrie',
            'age': 32,
            'language': 'Python'
        }
    ]
    assert get_northcoders_names(northcoders) == ['Callum', 'Carrie']