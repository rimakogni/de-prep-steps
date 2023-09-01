"""
This function takes a list of fruit (`orchard`) in the format:


['apple', 'apple', 'apple', 'apple', 'elppa', 'apple']


The fruit will all be the 'right way round' apart from one fruit!

Your function should return its zero-based index position. So in this example, the function should return 4.

Note: The fruit will not always be apple, but it will always be an orchard of the same kind of fruit.


find_wrong_way_fruit(['apple', 'apple', 'elppa']) # returns 2

find_wrong_way_fruit(['apple', 'elppa', 'apple']) # returns 1

find_wrong_way_fruit(['banana', 'ananab', 'banana', 'banana']) # returns 1

find_wrong_way_fruit(['apple', 'elppa']) # returns 0 as we can't tell which one is the right way round

"""

def find_wrong_way_fruit(orchard):
    # Your code here
    pass


def test_returns_zero_for_singleton_list():
    assert find_wrong_way_fruit(['apple']) == 0


def test_returns_zero_for_list_length_two():
    assert find_wrong_way_fruit(['grape', 'eparg']) == 0


def test_finds_last_item_if_reversed():
    assert find_wrong_way_fruit(['apple', 'apple', 'elppa']) == 2


def test_finds_first_item_if_reversed():
    assert find_wrong_way_fruit(['elppa', 'apple', 'apple']) == 0


def test_finds_intermediate_reversed_item():
    assert find_wrong_way_fruit(['banana', 'ananab', 'banana', 'banana']) == 1