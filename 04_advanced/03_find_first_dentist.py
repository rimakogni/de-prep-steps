"""
Write a function that takes a list of people dictionaries (`people`) and
returns the first person dictionary in the list that has the `'is_dentist'`
property set to `True`. If no dentists are included in the `people` list,
the function should return `None`.

find_first_dentist([]) # returns None

find_first_dentist([{'name': 'Callum', 'is_dentist': False}]) # returns None

find_first_dentist([{'name': 'Callum', 'is_dentist': False},
{'name': 'Carrie', 'is_dentist': True}])
# returns {'name': 'Carrie', 'is_dentist': True}

find_first_dentist([{'name': 'Callum', 'is_dentist': True},
{'name': 'Carrie', 'is_dentist': True}])
# returns {'name': 'Callum', 'is_dentist': True}

"""


def find_first_dentist(people):
    # Your code here
    pass


def test_empty_list_returns_none():
    assert find_first_dentist([]) is None


def test_returns_none_if_person_not_dentist():
    assert find_first_dentist(
        [{'name': 'Callum', 'is_dentist': False}]) is None


def test_returns_person_if_dentist():
    dentist = {'name': 'Callum', 'is_dentist': True}
    assert find_first_dentist(
        [{'name': 'Callum', 'is_dentist': True}]) == dentist


def test_returns_first_dentist():
    first_dentist = {'name': 'Carrie', 'is_dentist': True}
    dentists = [{'name': 'Callum', 'is_dentist': False},
                {'name': 'Carrie', 'is_dentist': True}]
    assert find_first_dentist(dentists) == first_dentist


def test_returns_first_dentist_of_many():
    dentist = {'name': 'Callum', 'is_dentist': True}
    dentists = [{'name': 'Callum', 'is_dentist': True},
                {'name': 'Carrie', 'is_dentist': True}]
    assert find_first_dentist(dentists) == dentist
