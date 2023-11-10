"""
Write a function that takes a `user` dictionary that looks like this:

{
  'name': "Tom",
  'age': 26,
  'pet': {
    'name': "Barney",
    'age': 6,
    'type': "good boy"
  }
}

The dictionary is nested; there are dictionaries paired to keys on the user
dictionary.

The function should the access the age property in the nested pet dictionary
and return the value.
If the user doesn't have an age for their pet the function should return None.

user = {
  'name': "Carrie",
  'age': 26,
  'pet': {
    'name': "Pixie",
    'age': 4,
    'type': "gremlin"
  }
}

get_user_pet_age(user) # returns 4
"""


def get_user_pet_age(user):
    # Your code here
    pass


def test_gets_pet_age():
    user = {
        'name': "Carrie",
        'age': 26,
        'pet': {
            'name': "Pixie",
            'age': 4,
            'type': "gremlin"
        }
    }
    assert get_user_pet_age(user) == 4


def test_returns_none_if_no_pet():
    user = {
        'name': "Carrie",
        'age': 26
    }
    assert get_user_pet_age(user) is None


def test_returns_none_if_no_pet_age():
    user = {
        'name': "Carrie",
        'age': 26,
        'pet': {
            'name': "Pixie",
            'type': "gremlin"
        }
    }
    assert get_user_pet_age(user) is None
