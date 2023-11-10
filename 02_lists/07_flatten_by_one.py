'''
Write a function, flatten_list_by_one, that when given a list with one or more
nested lists (nested_lists) returns a new list with one less level of nesting.

All the elements of all the original nested lists must be kept in their
original order.

flatten_list_by_one([[1], [2], [3]])  # returns [1, 2, 3]

flatten_list_by_one([[1], [2], [[3, 4]]])  # returns [1, 2, [3, 4]]
'''


def flatten_list_by_one(nested_lists):
    # your code here
    flat = []
    for list in nested_lists:
        for item in list:
            flat.append(item)
    return flat
    pass


def test_removes_single_layer_of_nesting():
    return_value = flatten_list_by_one([[1], [2]])
    assert return_value == [1, 2]


def test_removes_subsequent_layers_of_nesting_are_preserved():
    return_value = flatten_list_by_one([[[1, 2]], [[3, 4]]])
    assert return_value == [[1, 2], [3, 4]]


def test_combines_levels_of_nesting():
    return_value = flatten_list_by_one([[1, 2], [3, [4, 5]]])
    assert return_value == [1, 2, 3, [4, 5]]
