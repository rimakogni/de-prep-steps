'''
Write a function, get_items_longer_than, that takes a list of strings (strs) and a length (max_len). 
It should return an list of only the items longer than the given length.

get_items_longer_than(['a','bb','ccc'], 1) # returns ['bb', 'ccc'];

get_items_longer_than(['a','bb','ccc'], 2) # returns ['ccc'];

get_items_longer_than(['a','bb','ccc'], 4) # returns [];
'''


def get_items_longer_than(strs, max_len):
    # your code here
    pass


def test_returns_an_empty_list_for_no_strings():
    return_value = get_items_longer_than([], 1)
    assert return_value == []


def test_includes_strings_longer_than_the_max_len():
    return_value = get_items_longer_than(['a', 'bb'], 0)
    assert return_value == ['a', 'bb']


def test_excludes_strings_shorter_than_the_max_len():
    return_value = get_items_longer_than(['a', 'bb'], 3)
    assert return_value == []


def test_excludes_strings_equal_to_the_max_len():
    return_value = get_items_longer_than(['a', 'bb', 'ccc'], 2)
    assert return_value == ['ccc']
