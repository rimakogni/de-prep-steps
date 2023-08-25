'''
Write a function, get_even_nums, that takes an list of numbers (nums) and returns a list of only the even numbers.

get_even_nums([1, 2, 3]) # returns [2]
'''


def get_even_nums(nums):
    # your code here
    pass


def test_returns_an_empty_list_for_no_numbers():
    return_value = get_even_nums([])
    assert return_value == []


def test_includes_even_numbers():
    return_value = get_even_nums([2, 4, 6])
    assert return_value == [2, 4, 6]


def test_excludes_odd_numbers():
    return_value = get_even_nums([1, 3, 5])
    assert return_value == []


def test_includes_even_numbers_and_removes_odds():
    return_value = get_even_nums([1, 2, 3])
    assert return_value == [2]
