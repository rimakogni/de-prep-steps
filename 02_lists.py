"""
Write a function, get_even_nums, that takes an list of numbers (nums) and
returns a list of only the even numbers.

get_even_nums([1, 2, 3]) # returns [2]
"""


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


"""
Write a function, get_items_longer_than, that takes a list of strings (strs)
and a length (max_len).
It should return an list of only the items longer than the given length.

get_items_longer_than(['a','bb','ccc'], 1) # returns ['bb', 'ccc'];

get_items_longer_than(['a','bb','ccc'], 2) # returns ['ccc'];

get_items_longer_than(['a','bb','ccc'], 4) # returns [];
"""


def get_items_longer_than(strs, max_len):
    # your code here
    pass


def test_returns_an_empty_list_for_no_strings():
    return_value = get_items_longer_than([], 1)
    assert return_value == []


def test_includes_strings_longer_than_the_max_len():
    return_value = get_items_longer_than(["a", "bb"], 0)
    assert return_value == ["a", "bb"]


def test_excludes_strings_shorter_than_the_max_len():
    return_value = get_items_longer_than(["a", "bb"], 3)
    assert return_value == []


def test_excludes_strings_equal_to_the_max_len():
    return_value = get_items_longer_than(["a", "bb", "ccc"], 2)
    assert return_value == ["ccc"]


"""
Write a function, get_sandwich_filling, that takes a list of sandwich
ingredients (sandwich).
This list represents the ingredients used to make a sandwich, it's first and
last items will be the 'bread'
Return a list containing only the filling of the sandwich.

get_sandwich_filling(['bread', 'bacon', 'bread']) # returns ['bacon']

get_sandwich_filling(['bread', 'halluomi', 'lettuce', 'bread']) # returns
['halluomi', 'lettuce']

get_sandwich_filling(['a', 'b', 'c', 'd']) # returns ['b', 'c']
"""


def get_sandwich_filling(sandwich):
    # your code here
    pass


def test_returns_a_list_with_a_single_filling():
    cheese_sandwich = ["bread", "lonely slice of cheese", "bread"]
    return_value = get_sandwich_filling(cheese_sandwich)
    assert return_value == ["lonely slice of cheese"]


def test_returns_a_list_of_fillings():
    burger = ["bread", "tomato", "lettuce", "cheese", "patty", "bread"]
    return_value = get_sandwich_filling(burger)
    assert return_value == ["tomato", "lettuce", "cheese", "patty"]


def test_returns_an_empty_list_when_no_fillings():
    bread_sandwich = ["bread", "bread"]
    return_value = get_sandwich_filling(bread_sandwich)
    assert return_value == []


"""
Write a function, remove_item, that takes a list (items) and a number (n).
Return a new list without the item at position n. This should be a new list and
the item should still exist in the original list

remove_item([1, 2, 3], 1) # returns [1, 3]

remove_item([3], 0) # returns []
"""


def remove_item(items, n):
    # your code here
    pass


def test_returns_a_list_without_the_specified_element():
    return_value = remove_item([1], 0)
    assert return_value == []


def test_returns_a_list_including_other_elements():
    return_value = remove_item([1, 2, 3, 4, 5], 2)
    assert return_value == [1, 2, 4, 5]


def test_only_removes_the_specified_element():
    return_value = remove_item([1, 2, 1, 2, 1], 2)
    assert return_value == [1, 2, 2, 1]


def test_returns_a_new_list():
    nums = [1, 2, 3]
    return_value = remove_item(nums, 2)
    assert (
        return_value is not nums
    ), "Returned list should not be the same one that was passed in"  # noqa


def test_element_is_still_included_in_original_list():
    nums = [1, 2, 3]
    remove_item(nums, 2)
    assert nums == [1, 2, 3], "Item should not be removed from original list"


"""
Write a function that takes two lists (list1 and list2) and
returns a new list with all of the elements of list1 followed by all of the
elements of list2.

The function should return a new list and both original lists should remain
unchanged.

merge_lists([1, 2], [3, 4]) # returns [1, 2, 3, 4]
"""


def merge_lists(list1, list2):
    # your code here
    pass


def test_returns_two_single_elements_merged():
    return_value = merge_lists([1], [2])
    assert return_value == [1, 2]


def test_returns_two_multiple_elements_lists_merged_together():
    return_value = merge_lists([1, 2, 3], [4, 5, 6])
    assert return_value == [1, 2, 3, 4, 5, 6]


def test_merges_empty_lists():
    return_value = merge_lists([1, 2, 3], [])
    assert return_value == [1, 2, 3]


def test_returns_an_empty_list_if_both_are_empty():
    return_value = merge_lists([], [])
    assert return_value == []


def test_original_lists_are_unchanged():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    merge_lists(list1, list2)
    assert list1 == [1, 2, 3], "list1 should not be changed"
    assert list2 == [4, 5, 6], "list2 should not be changed"


"""
Write a function that takes an list of nested lists (lists) and an item to
check for (item).
It should return True if the passed item is present in every list inside lists.
Otherwise, it should return False.

is_item_omnipresent([[1,2,3], [2,3,4], [3,4,5]], 3) # returns True, present in
all

is_item_omnipresent([[1,2,3], [2,3,4], [3,4,5]], 9) # returns False, not
present in any

is_item_omnipresent([[1,2,3], [2,3,4], [3,4,5]], 4) # returns False, only
present in two lists
"""


def is_item_omnipresent(lists, item):
    # your code here
    pass


def test_returns_false_if_item_missing_from_all():
    return_value = is_item_omnipresent([[1], [2]], 3)
    assert return_value == False  # noqa


def test_returns_false_if_item_missing_from_one():
    return_value = is_item_omnipresent([[1], [2]], 1)
    assert return_value == False  # noqa


def test_returns_true_if_item_present_in_all():
    return_value = is_item_omnipresent([[1], [1], [1]], 1)
    assert return_value == True  # noqa


def test_returns_true_if_item_included_amongst_other_elements():
    return_value = is_item_omnipresent([[1, 2], [2, 3], [2, 2]], 2)
    assert return_value == True  # noqa


"""
Write a function, flatten_list_by_one, that when given a list with one or more
nested lists (nested_lists) returns a new list with one less level of nesting.

All the elements of all the original nested lists must be kept in their
original order.

flatten_list_by_one([[1], [2], [3]])  # returns [1, 2, 3]

flatten_list_by_one([[1], [2], [[3, 4]]])  # returns [1, 2, [3, 4]]
"""


def flatten_list_by_one(nested_lists):
    # your code here
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
