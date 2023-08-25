'''
Write a function that takes two lists (list1 and list2) and 
returns a new list with all of the elements of list1 followed by all of the elements of list2.

The function should return a new list and both original lists should remain unchanged.

merge_arrays([1, 2], [3, 4]) # returns [1, 2, 3, 4]
'''


def merge_arrays(list1, list2):
    # your code here
    pass


def test_returns_two_single_elements_merged():
    return_value = merge_arrays([1], [2])
    assert return_value == [1, 2]


def test_returns_two_multiple_elements_lists_merged_together():
    return_value = merge_arrays([1, 2, 3], [4, 5, 6])
    assert return_value == [1, 2, 3, 4, 5, 6]


def test_merges_empty_lists():
    return_value = merge_arrays([1, 2, 3], [])
    assert return_value == [1, 2, 3]


def test_returns_an_empty_list_if_both_are_empty():
    return_value = merge_arrays([], [])
    assert return_value == []


def test_original_lists_are_unchanged():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    merge_arrays(list1, list2)
    assert list1 == [1, 2, 3], "list1 should not be changed"
    assert list2 == [4, 5, 6], "list2 should not be changed"
