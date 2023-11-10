"""
Write a function that takes a list of `names` representing a person's full
name and returns a list
of each person whose last name is 'Williams'.


get_williams(['David Williams']) # returns ['David Williams']

get_williams(['David Williams', 'Sarah Williams'])
# returns ['David Williams', 'Sarah Williams']

get_williams(['Kirsty February']) # returns []

get_williams(['Kirsty February', 'Sam Williams']) # returns ['Sam Williams']

get_williams(['William David', 'Cole Williamson']) # returns []

"""


def get_williams(names):
    # Your code here
    pass


def test_empty_list():
    assert get_williams([]) == []


def test_single_invalid_item():
    assert get_williams(['Kirsty February']) == []


def test_single_valid_item():
    assert get_williams(['David Williams']) == ['David Williams']


def test_several_valid_items():
    assert get_williams(['David Williams', 'Sarah Williams']) == [
        'David Williams', 'Sarah Williams']


def test_mixed_items():
    assert get_williams(['Kirsty February', 'Sam Williams']) == [
        'Sam Williams']


def test_rogue_williams():
    assert get_williams(['William David', 'Cole Williamson']) == []
