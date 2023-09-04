"""
get_first_item is a function that takes an list and returns the first element.

Unfortunately, it looks like the function is currently throwing a NameError.

Can you work out what needs to be changed to make the function pass all the tests?
"""

def get_first_item(my_list):
    first_item = my_list[0]
    return firstitem


# Do not change code below this line

def test_gets_fist_number_item():
    assert get_first_item([1, 2, 3, 4]) == 1

def test_gets_first_string_item():
    assert get_first_item(['black', 'khaki', 'cyan']) == 'black'