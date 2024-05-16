from test_api.checks import Check, SkipCheck

"""
### triple_nums ###

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


# Do not change tests!

Check(triple_nums, 'returns list').when_called_with([]).is_type(list)
Check(triple_nums, 'when passed empty list returns empty list').when_called_with([]).returns([])
Check(triple_nums, 'returns list of all numbers multiplied by three').when_called_with([10, 25, 30, 40]).returns([30, 75, 90, 120])


"""
### shout_names ###

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


# Do not change tests!

Check(shout_names, 'returns a list').when_called_with([]).is_type(list)
Check(shout_names, 'when passed empty list returns empty list').when_called_with([]).returns([])
Check(shout_names, 'shouts names').when_called_with(["Carrie", "Diya", "Kyle", "Christian"]).returns(["CARRIE!", "DIYA!", "KYLE!", "CHRISTIAN!"])


"""
### is_sweet_enough ###

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


# Do not change tests!

Check(is_sweet_enough, 'returns True when all foods are sweet')\
    .when_called_with([{"name": "chocolate", "flavour": "sweet"}, {"name": "banana", "flavour": "sweet"}, {"name": "barfi", "flavour": "sweet"}])\
    .returns(True)

Check(is_sweet_enough, 'returns False when no foods are sweet')\
    .when_called_with([{"name": "samosa", "flavour": "savoury"}, {"name": "lemon", "flavour": "sour"}, {"name": "olive", "flavour": "bitter"}])\
    .returns(False)

Check(is_sweet_enough, 'returns False when any foods are NOT sweet')\
    .when_called_with([{"name": "stollen", "flavour": "sweet"}, {"name": "cranberries", "flavour": "sour"}, {"name": "mince pie", "flavour": "sweet"}])\
    .returns(False)


"""
### get_excited ###

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


Check(get_excited, 'returns empty string when passed empty string').when_called_with('').returns('')
Check(get_excited, 'returns unchanged string when no full stops present')\
    .when_called_with("the quick brown fox jumps over the lazy dog")\
    .returns("the quick brown fox jumps over the lazy dog")
Check(get_excited, 'replaces full stops with exclamation marks - single full stop')\
    .when_called_with("We're gonna need a bigger boat.")\
    .returns("We're gonna need a bigger boat!")
Check(get_excited, 'replaces full stops with exclamation marks - multiple full stops')\
    .when_called_with("Woo. Woo. Woo. Who's ready to code?")\
    .returns("Woo! Woo! Woo! Who's ready to code?")


"""
### shrek_characters ###

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


# Do not change tests!

Check(shrek_characters, 'when passed an empty list returns an empty list').when_called_with([]).returns([])
Check(shrek_characters, 'returns an empty list when list that contains no Shrek characters')\
    .when_called_with([
        {
            "name": "Cedric Diggory",
            "movie": "Harry Potter and the Goblet of Fire",
        },
        {"name": "Elle Woods", "movie": "Legally Blonde"},
        {"name": "Paddington Bear", "movie": "Paddington 2"},
    ]).returns([])

Check(shrek_characters, 'returns given list when list only contains Shrek characters')\
    .when_called_with([
        {
            "name": "Shrek",
            "movie": "Shrek",
        },
        {"name": "Lord Farquaad", "movie": "Shrek"},
        {"name": "Magic Mirror", "movie": "Shrek"},
    ]).returns([
        "Shrek",
        "Lord Farquaad",
        "Magic Mirror",
    ])
