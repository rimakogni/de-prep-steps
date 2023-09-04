"""
is_sweet_enough is a function that takes a list of food items and returns either True or False depending on whether every food in the array has a sweet flavour.

Refactor is_sweet_enough to use a for comprehension that includes an if statement. See here for details: https://speedsheet.io/s/python#hCe5

Alternatively, perhaps you can use a for comprehension with the `all` function: https://speedsheet.io/s/python#PEU2

The food items look like this: {'name': 'chocolate', 'flavour': 'sweet'}

If you run pytest on this file, all tests should pass. 
"""

def is_sweet_enough(food_items):
    for i in range(len(food_items)):
        if food_items[i]['flavour'] != 'sweet':
            return False
    return True


# Do not change any code below this line

def test_true_when_all_sweet():
    food_items = [
        { 'name': 'chocolate', 'flavour': 'sweet' },
        { 'name': 'banana', 'flavour': 'sweet' },
        { 'name': 'barfi', 'flavour': 'sweet' }
    ]
    assert is_sweet_enough(food_items)


def test_false_if_none_are_sweet():
    food_items = [
        { 'name': 'samosa', 'flavour': 'savoury' },
        { 'name': 'lemon', 'flavour': 'sour' },
        { 'name': 'olive', 'flavour': 'bitter' }
    ]
    assert not is_sweet_enough(food_items)


def test_false_if_any_are_not_sweet():
    food_items = [
      { 'name': 'stollen', 'flavour': 'sweet' },
      { 'name': 'cranberries', 'flavour': 'sour' },
      { 'name': 'mince pie', 'flavour': 'sweet' },
    ]
    assert not is_sweet_enough(food_items)


