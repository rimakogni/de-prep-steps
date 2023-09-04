"""
Write a function that takes a list of `numbers` and returns a list containing the factorial of each number in the list.

The factorial of a number is the product of that number and all the integers below it.
E.g. the factorial of 4 is 4 * 3 * 2 * 1 = 24


get_factorials([3]) # returns [6]

get_factorials([3, 4]) # returns [6, 24]

get_factorials([1, 5, 2]) # returns [1, 120, 2]

get_factorials([]) # returns []

"""


def get_factorials(numbers):
    # Your code here
    pass


def test_empty_list_generates_empty_list():
    assert get_factorials([]) == []


def test_one_item():
    assert get_factorials([3]) == [6]


def test_number_one():
    assert get_factorials([1]) == [1]


def test_two_items():
    assert get_factorials([3, 4]) == [6, 24]
