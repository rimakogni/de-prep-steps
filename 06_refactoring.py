"""
`triple_nums` is a function that takes a list of numbers and returns a list
containing the result of multiplying each of those numbers by 3.

Refactor triple_nums to use a _list comprehension_ instead of a for loop.

For advice on how to do this, check out the following:
https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions:~:text=5.1.3.%20List%20Comprehensions-,%C2%B6,-List%20comprehensions%20provide

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


"""
`shout_names` is a function that takes a list of names and returns a list
containing all of the names in capital letters followed by an
exclamation mark "!".

Refactor `shout_names` to use a list comprehension.

If you run pytest on this file, all tests should pass.
"""


def shout_names(names):
    shouted_names = []
    for name in names:
        shouted_names.append(name.upper() + "!")
    return shouted_names


# Do not change any code below this line


def test_returns_a_list():
    assert type(shout_names([])) == list


def test_no_names_produces_empty_list():
    assert shout_names([]) == []


def test_shouts_names():
    names = ["Carrie", "Diya", "Kyle", "Christian"]
    expected = ["CARRIE!", "DIYA!", "KYLE!", "CHRISTIAN!"]
    assert shout_names(names) == expected
    names = ["Maddie", "Bethan", "Andrea", "Jade"]
    expected = ["MADDIE!", "BETHAN!", "ANDREA!", "JADE!"]
    assert shout_names(names) == expected


"""
is_sweet_enough is a function that takes a list of food items and returns
either True or False depending on whether every food in the array has a
sweet flavour.

Refactor is_sweet_enough to use a for comprehension with the `all` function:
https://speedsheet.io/s/python#PEU2

The food items look like this: {'name': 'chocolate', 'flavour': 'sweet'}

If you run pytest on this file, all tests should pass.
"""


def is_sweet_enough(food_items):
    for i in range(len(food_items)):
        if food_items[i]["flavour"] != "sweet":
            return False
    return True


# Do not change any code below this line


def test_true_when_all_sweet():
    food_items = [
        {"name": "chocolate", "flavour": "sweet"},
        {"name": "banana", "flavour": "sweet"},
        {"name": "barfi", "flavour": "sweet"},
    ]
    assert is_sweet_enough(food_items)


def test_false_if_none_are_sweet():
    food_items = [
        {"name": "samosa", "flavour": "savoury"},
        {"name": "lemon", "flavour": "sour"},
        {"name": "olive", "flavour": "bitter"},
    ]
    assert not is_sweet_enough(food_items)


def test_false_if_any_are_not_sweet():
    food_items = [
        {"name": "stollen", "flavour": "sweet"},
        {"name": "cranberries", "flavour": "sour"},
        {"name": "mince pie", "flavour": "sweet"},
    ]
    assert not is_sweet_enough(food_items)


"""
`get_excited` is a function that takes a piece of text and returns it with all
of the full stops (.) replaced by exclamation marks (!).

Refactor get_excited to use a string method. All of this code can be rewritten
in just one line with one string method...

If you run pytest on this file, all tests should pass.
"""


def get_excited(text):
    new_text = ""
    for char in text:
        if char == ".":
            new_text += "!"
        else:
            new_text += char
    return new_text


def test_empty_string_returns_empty_string():
    assert get_excited("") == ""


def test_no_full_stops_means_text_unchanged():
    text = "the quick brown fox jumps over the lazy dog"
    assert get_excited(text) == text


def test_replaces_full_stops_with_excalamation_marks():
    text = "Today is a great day."
    expected = "Today is a great day!"
    assert get_excited(text) == expected
    text = "We're gonna need a bigger boat."
    expected = "We're gonna need a bigger boat!"
    assert get_excited(text) == expected
    text = "Woo. Woo. Woo. Who's ready to code?"
    expected = "Woo! Woo! Woo! Who's ready to code?"


"""
shrek_characters is a function that takes a list of movie characters and
returns a list of only the characters from the film franchise, Shrek.

Refactor shrek_characters to use a comprehension.

If you run pytest on this file, all tests should pass.
"""


def shrek_characters(characters):
    shreks = []
    for character in characters:
        if "Shrek" in character["movie"]:
            shreks.append(character["name"])
    return shreks


# Do not change any code below this line


def test_empty_list_of_characters_produces_empty_list():
    assert shrek_characters([]) == []


def test_returns_empty_list_if_no_characters_from_shrek():
    characters = [
        {
            "name": "Cedric Diggory",
            "movie": "Harry Potter and the Goblet of Fire",
        },
        {"name": "Elle Woods", "movie": "Legally Blonde"},
        {"name": "Paddington Bear", "movie": "Paddington 2"},
    ]
    assert shrek_characters(characters) == []


def test_all_characters_if_all_in_shrek():
    characters = [
        {
            "name": "Shrek",
            "movie": "Shrek",
        },
        {"name": "Lord Farquaad", "movie": "Shrek"},
        {"name": "Magic Mirror", "movie": "Shrek"},
    ]
    assert shrek_characters(characters) == [
        "Shrek",
        "Lord Farquaad",
        "Magic Mirror",
    ]
