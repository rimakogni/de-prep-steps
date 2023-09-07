"""
`triple_nums` is a function that takes a list of numbers and returns a list containing the result of multiplying each of those numbers by 3.

Refactor tripl_nums to use a _list comprehension_ instead of a for loop.

For advice on how to do this, check out the following: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions:~:text=5.1.3.%20List%20Comprehensions-,%C2%B6,-List%20comprehensions%20provide

Or the following guide on SpeedSheet: https://speedsheet.io/s/python#gL31

If you run pytest on this file, all tests should pass.
"""

def triple_nums(nums):
    tripled = []
    for i in range(len(nums)):
        tripled.append(3 * nums[i])
    return tripled


# Do not change any code below this line


def test_returns_list():
    assert type(triple_nums([])) is list


def test_empty_input_produces_empty_output():
    assert triple_nums([]) == []

def test_returns_list_of_all_numbers_multiplied_by_three():
    nums = [1, 2, 3, 4]
    assert triple_nums(nums) == [3, 6, 9, 12]
    nums = [10, 25, 30, 40]
    assert triple_nums(nums) == [30, 75, 90, 120]
