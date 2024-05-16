from test_api.checks import Check, SkipCheck

"""
### get_first_item ###

get_first_item is a function that takes an list and returns the first element.

Unfortunately, it looks like the function is currently throwing a NameError.

Can you work out what needs to be changed to make the function pass all the
tests?
"""


def get_first_item(my_list):
    first_item = my_list[0]
    return firstitem


# Do not change tests!

Check(get_first_item, 'gets first number item').when_called_with([1, 2, 3, 4]).returns(1)
Check(get_first_item, 'gets first string item').when_called_with(['black', 'khaki', 'cyan']).returns('black')


"""
### split_string ###

split_string is a function that takes a string and returns a list containing
all of the individual characters as separate elements.

Unfortunately, it looks like the function is currently throwing a TypeError.

Can you work out what needs changing to make the function pass all the tests?
"""


def split_string():
    return list(str)


# Do not change tests!

Check(split_string, 'splits lowercase string').when_called_with('string').returns(['s', 't', 'r', 'i', 'n', 'g'])
Check(split_string, 'splits titlecase string').when_called_with('Northcoders').returns(['N', 'o', 'r', 't', 'h', 'c', 'o', 'd', 'e', 'r', 's'])


"""
add_bread is a function that takes a dictionary describing a `person`
and a string of their favourite bread, and returns that object with a
new property (`fave_bread`) set to a value of their favourite bread.

If no favourite bread is given then the default fave_bread is 'granary'.

Unfortunately, it looks like the function has a couple of issues with
the way it's written.

Can you work out what needs changing to make the function pass all the tests?
"""


def add_bread(person, loaf):
    person['loaf'] == loaf
    return


# Do not change tests!

Check(add_bread, "adds favourite bread - rye").when_called_with({'name': 'Joe'}, 'rye').returns({'name': 'Joe', 'fave_bread': 'rye'})
Check(add_bread, "adds favourite bread - granary").when_called_with({'name': 'Paul'}, 'granary').returns({'name': 'Paul', 'fave_bread': 'granary'})
