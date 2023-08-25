'''
Write a function, get_sandwich_filling, that takes a list of sandwich ingredients (sandwich).

This list represents the ingredients used to make a sandwich, it's first and last items will be the 'bread'

Return a list containing only the filling of the sandwich.

get_sandwich_filling(['bread', 'bacon', 'bread']) //returns ['bacon']

get_sandwich_filling(['bread', 'halluomi', 'lettuce', 'bread']) //returns ['halluomi', 'lettuce']

get_sandwich_filling(['a', 'b', 'c', 'd']) //returns ['b', 'c']
'''


def get_sandwich_filling(sandwich):
    # your code here
    pass


def test_returns_a_list_with_a_single_filling():
    cheese_sandwich = ['bread', 'lonely slice of cheese', 'bread']
    return_value = get_sandwich_filling(cheese_sandwich)
    assert return_value == ['lonely slice of cheese']


def test_returns_a_list_of_fillings():
    burger = ['bread', 'tomato', 'lettuce', 'cheese', 'patty', 'bread']
    return_value = get_sandwich_filling(burger)
    assert return_value == ['tomato', 'lettuce', 'cheese', 'patty']


def test_returns_an_empty_list_when_no_fillings():
    bread_sandwich = ['bread', 'bread']
    return_value = get_sandwich_filling(bread_sandwich)
    assert return_value == []
