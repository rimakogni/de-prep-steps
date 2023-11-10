"""
In this function, you will be provided with a dictionary. That dictionary is
storing information on keys:

{
    'name': 'Tom',
    'job': ['writing katas', 'marking'],
    'favourite_shop': [
        "Paul's Donkey University",
        "Shaq's Taxidermy Shack",
        "Sam's Pet Shop"
    ]
}

In some cases, however, the keys have been very badly named. Good naming
convention tells us that the __keys containing lists__ should have
plural names.
This function should return a new dictionary that is a copy of the input but
with any keys that contain lists pluralised (an 's' added to the end.)

{
    'name': 'Tom',
    'jobs': ['writing katas', 'marking'],
    'favourite_shops': [
        "Paul's Donkey University",
        "Shaq's Taxidermy Shack",
        "Sam's Pet Shop"
    ]
}
"""


def pluralise_keys(dictionary):
    # Your code here
    pass


def test_empty_dictionary():
    assert pluralise_keys({}) == {}


def test_dictionary_with_no_arrays_returns_copy():
    data = {'a': 1, 'b': 2, 'c': 3}
    assert pluralise_keys(data) == {'a': 1, 'b': 2, 'c': 3}
    assert pluralise_keys(data) is not data


def test_dictionary_with_nested_dicts_returns_copy():
    data = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}}
    assert pluralise_keys(data) == {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}}
    assert pluralise_keys(data) is not data


def test_dictionary_with_one_nested_list():
    data = {'a': 1, 'b': 2, 'num': [3, 4]}
    assert pluralise_keys(data) == {'a': 1, 'b': 2, 'nums': [3, 4]}
    assert pluralise_keys(data) is not data


def test_dictionary_with_several_lists():
    data = {
        'name': 'Tom',
        'job': ['writing katas', 'marking'],
        'favourite_shop': [
            "Paul's Donkey University",
            "Shaq's Taxidermy Shack",
            "Sam's Pet Shop"
        ]
    }
    result = pluralise_keys(data)
    assert result == {
        'name': 'Tom',
        'jobs': ['writing katas', 'marking'],
        'favourite_shops': [
            "Paul's Donkey University",
            "Shaq's Taxidermy Shack",
            "Sam's Pet Shop"
        ]
    }
    assert result is not data
