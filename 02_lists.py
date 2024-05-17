from test_api.checks import Check, SkipCheck


"""
### get_even_nums ###

Write a function, get_even_nums, that takes an list of numbers (nums) and
returns a list of only the even numbers.

get_even_nums([1, 2, 3]) # returns [2]
"""


def get_even_nums(nums):
    # your code here
    pass


Check(
    get_even_nums,
    "returns an empty list when there are no numbers"
).when_called_with([]).returns([])

Check(
    get_even_nums,
    "returns given list when all numbers are even"
).when_called_with([2, 4, 6]).returns([2, 4, 6])

Check(
    get_even_nums,
    "returns empty list when all numbers are odd"
).when_called_with([1, 3, 5]).returns([])

Check(
    get_even_nums,
    "returns empty list when numbers are mixed, even and odd"
).when_called_with([1, 3, 5]).returns([])


"""
### get_items_longer_than ###

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


# ❗ Remember to change SkipCheck to Check!
SkipCheck(
    get_items_longer_than, "returns an empty list when there are no strings"
).when_called_with([], 1).returns([])

SkipCheck(
    get_items_longer_than, "returns all strings longer than the max len"
).when_called_with(["a", "bb"], 0).returns(["a", "bb"])

SkipCheck(
    get_items_longer_than, "excludes strings shorter than the max len"
).when_called_with(["a", "bb"], 3).returns([])

SkipCheck(
    get_items_longer_than, "excludes strings equal to the max len"
).when_called_with(["a", "bb", "ccc"], 2).returns(["ccc"])


"""
### get_sandwich_filling ###

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


SkipCheck(
    get_sandwich_filling, "returns a list with a single filling"
).when_called_with(
    ["bread", "lonely slice of cheese", "bread"]
).returns(["lonely slice of cheese"])

SkipCheck(
    get_sandwich_filling, "returns a list with a multiple fillings"
).when_called_with(
    ["bread", "tomato", "lettuce", "cheese", "patty", "bread"]
).returns(["tomato", "lettuce", "cheese", "patty"])

SkipCheck(
    get_sandwich_filling, "returns an empty list when there are no fillings"
).when_called_with(
    ["bread", "bread"]
).returns([])


"""
### remove_item ###

Write a function, remove_item, that takes a list (items) and a number (n).
Return a new list without the item at position n. This should be a new list and
the item should still exist in the original list

remove_item([1, 2, 3], 1) # returns [1, 3]

remove_item([3], 0) # returns []
"""


def remove_item(items, n):
    # your code here
    pass


SkipCheck(
    remove_item, "returns a list with specified element removed"
).when_called_with([1], 0).returns([])

SkipCheck(
    remove_item,
    "returns a list containing all elements that haven't been removed"
).when_called_with([1, 2, 3, 4, 5], 2).returns([1, 2, 4, 5])

SkipCheck(
    remove_item,
    "only removes the value at the specified index"
).when_called_with([1, 2, 1, 2, 1], 2).returns([1, 2, 2, 1])

test_list = [1, 2, 3]
SkipCheck(
    remove_item,
    "returns a new list"
).when_called_with(test_list, 2).is_not_same_as(test_list)


# TODO: THIS TEST NEEDS CHANGING!
def test_element_is_still_included_in_original_list():
    nums = [1, 2, 3]
    remove_item(nums, 2)
    assert nums == [1, 2, 3], "Item should not be removed from original list"


"""
### merge_lists ###

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


SkipCheck(
    merge_lists, 'merges two single element lists together'
).when_called_with([1], [2]).returns([1, 2])

SkipCheck(
    merge_lists, 'merges two multi element lists together'
).when_called_with([1, 2, 3], [4, 5, 6]).returns([1, 2, 3, 4, 5, 6])

SkipCheck(
    merge_lists, 'merges two lists when one is empty'
).when_called_with([1, 2, 3], []).returns([1, 2, 3])

SkipCheck(
    merge_lists, 'merges two lists when both are empty'
).when_called_with([], []).returns([])


# TODO: THIS TEST NEEDS CHANGING!
def test_original_lists_are_unchanged():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    merge_lists(list1, list2)
    assert list1 == [1, 2, 3], "list1 should not be changed"
    assert list2 == [4, 5, 6], "list2 should not be changed"


"""
### is_item_omnipresent ###

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


SkipCheck(
    is_item_omnipresent, "returns false if item is missing from all lists"
).when_called_with([[1], [2]], 3).returns(False)

SkipCheck(
    is_item_omnipresent, "returns false if item is missing from a single list"
).when_called_with([[1], [2]], 1).returns(False)

SkipCheck(
    is_item_omnipresent, "returns True if item is present in all lists"
).when_called_with([[1], [1], [1]], 1).returns(True)

SkipCheck(
    is_item_omnipresent,
    "returns True if item is present amongst other elements in mixed lists"
).when_called_with([[1], [1], [1]], 1).returns(True)


"""
### flatten_lists ###

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


SkipCheck(
    flatten_list_by_one, 'removes single layer of nesting'
).when_called_with([[1], [2]]).returns([1, 2])

SkipCheck(
    flatten_list_by_one, 'subsequent layers of nesting are preserved'
).when_called_with([[[1, 2]], [[3, 4]]]).returns([[1, 2], [3, 4]])

SkipCheck(
    flatten_list_by_one, 'combines levels of nesting'
).when_called_with([[1, 2], [3, [4, 5]]]).returns([1, 2, 3, [4, 5]])
