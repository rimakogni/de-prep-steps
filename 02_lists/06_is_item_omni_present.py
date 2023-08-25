'''
Write a function that takes an list of nested lists (lists) and an item to check for (item).
It should return True if the passed item is present in every list inside lists. Otherwise, it should return False.

is_item_omnipresent([[1,2,3], [2,3,4], [3,4,5]], 3) # returns True, present in all

is_item_omnipresent([[1,2,3], [2,3,4], [3,4,5]], 9) # returns False, not present in any

is_item_omnipresent([[1,2,3], [2,3,4], [3,4,5]], 4) # returns False, only present in two lists
'''


def is_item_omnipresent(lists, item):
    # your code here
    pass


def test_returns_false_if_item_missing_from_all():
    return_value = is_item_omnipresent([[1], [2]], 3)
    assert return_value == False


def test_returns_false_if_item_missing_from_one():
    return_value = is_item_omnipresent([[1], [2]], 1)
    assert return_value == False


def test_returns_true_if_item_present_in_all():
    return_value = is_item_omnipresent([[1], [1], [1]], 1)
    assert return_value == True


def test_returns_true_if_item_included_amongst_other_elements():
    return_value = is_item_omnipresent([[1, 2], [2, 3], [2, 2]], 2)
    assert return_value == True
