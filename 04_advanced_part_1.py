from test_api.checks import Check, SkipCheck

"""
Write a function that takes a list of booleans (`bools`) and returns a `list`
with all of their values swapped
such that `True` becomes `False` and `False` becomes `True`.


flip_booleans([True, True, True]) # returns [False, False, False]

flip_booleans([False, False, False]) # returns [True, True, True]

flip_booleans([True, False, False, True]) # returns [False, True, True, False]

flip_booleans([]) # returns []

"""


def flip_booleans(bools):
    pass


Check(
    flip_booleans, "returns empty list when passed empty list"
).when_called_with([]).returns([])

Check(
    flip_booleans, "returns single False when passed single True"
).when_called_with([True]).returns([False])

Check(
    flip_booleans, "returns single True when passed single False"
).when_called_with([False]).returns([True])

Check(
    flip_booleans, "returns all Falses when passed all Trues"
).when_called_with([True, True, True]).returns([False, False, False])

Check(
    flip_booleans, "returns all Trues when passed all Falses"
).when_called_with([False, False, False]).returns([True, True, True])

Check(
    flip_booleans, "returns mixed Trues and Falses flipped correctly"
).when_called_with([True, False, False, True]).returns(
    [False, True, True, False]
)

"""
Northcoders is expanding to France!

Unfortunately for us, our team on the ground in Paris are patriotically
Francophone and have been providing us with student data partly in French.

Write a function that will take a dictionary representing a student's data, a
key that needs changing, and its English translation.

The function should return a new dictionary with the relevant key name changed
to its English translation.

If the key to change does not exist in the student then no changes should be
made.

student = {
    'prénom': 'Carla',
    'surname': 'Bruni',
    'job': 'Artist'
}

translate_key(student, 'prénom', 'first_name') # should return the following:

{
    'first_name': 'Carla',
    'surname': 'Bruni',
    'job': 'Artist'
}

"""


def translate_key(student, key_to_change, translation):
    pass


SkipCheck(
    translate_key,
    "returns empty dictionary unchanged when passed empty dictionary and key not present",
).when_called_with({}, "prénom", "first_name").returns({})

SkipCheck(
    translate_key, "returns unchanged if key not present"
).when_called_with(
    {"first_name": "Carla", "surname": "Bruni", "job": "Artist"},
    "prénom",
    "first_name",
).returns(
    {"first_name": "Carla", "surname": "Bruni", "job": "Artist"}
)

SkipCheck(
    translate_key, "returns new dictionary with key translated"
).when_called_with(
    {"prénom": "Carla", "surname": "Bruni", "job": "Artist"},
    "prénom",
    "first_name",
).returns(
    {"first_name": "Carla", "surname": "Bruni", "job": "Artist"}
)

SkipCheck(
    translate_key, "returns new dictionary if required"
).when_called_with(
    {"first_name": "Jean", "surname": "Reno", "emploi": "Actor"},
    "emploi",
    "job",
).returns(
    {"first_name": "Jean", "surname": "Reno", "job": "Actor"}
)


"""
Write a function that takes a list of people dictionaries (`people`) and
returns the first person dictionary in the list that has the `'is_dentist'`
property set to `True`. If no dentists are included in the `people` list,
the function should return `None`.

find_first_dentist([]) # returns None

find_first_dentist([{'name': 'Callum', 'is_dentist': False}]) # returns None

find_first_dentist([{'name': 'Callum', 'is_dentist': False},
{'name': 'Carrie', 'is_dentist': True}])
# returns {'name': 'Carrie', 'is_dentist': True}

find_first_dentist([{'name': 'Callum', 'is_dentist': True},
{'name': 'Carrie', 'is_dentist': True}])
# returns {'name': 'Callum', 'is_dentist': True}

"""


def find_first_dentist(people):
    pass


SkipCheck(
    find_first_dentist, "returns None when passed empty list"
).when_called_with([]).returns(None)

SkipCheck(
    find_first_dentist, "returns None if person not dentist"
).when_called_with([{"name": "Callum", "is_dentist": False}]).returns(None)

SkipCheck(find_first_dentist, "returns person if dentist").when_called_with(
    [{"name": "Callum", "is_dentist": True}]
).returns({"name": "Callum", "is_dentist": True})

SkipCheck(find_first_dentist, "returns first dentist").when_called_with(
    [
        {"name": "Callum", "is_dentist": False},
        {"name": "Carrie", "is_dentist": True},
    ]
).returns({"name": "Carrie", "is_dentist": True})

SkipCheck(
    find_first_dentist, "returns first dentist of many"
).when_called_with(
    [
        {"name": "Callum", "is_dentist": True},
        {"name": "Carrie", "is_dentist": True},
    ]
).returns(
    {"name": "Callum", "is_dentist": True}
)


"""
Write a function that takes a list of `people` dictionaries in the format:

[
    {
        'name': 'Emmeline',
        'lives': {
            'country': 'UK',
            'city': 'Manchester'
        },
        'age': 32
    }
]


The function should return the number of people who live in the
city of Manchester.

tally_people_in_manchester([{
    'name': 'Emmeline',
    'lives': { 'country': 'UK', 'city': 'Manchester' },
    'age': 32
    }]) # returns 1

tally_people_in_manchester([{
    'name': 'Carrie',
    'lives': { 'country': 'UK', 'city': 'Leeds' },
    'age': 32
    }]) # returns 0

tally_people_in_manchester([
    {
    'name': 'Carrie',
    'lives': { 'country': 'UK', 'city': 'Leeds' },
    'age': 32
    },
    { 'name': 'Ray',
    'lives': { 'country': 'UK', 'city': 'Manchester' },
    'age': 31
    }
    ]) # returns 1

tally_people_in_manchester([]) # returns 0

"""


def tally_people_in_manchester(people):
    pass


SkipCheck(
    tally_people_in_manchester, "returns 0 when passed empty list"
).when_called_with([]).returns(0)

SkipCheck(
    tally_people_in_manchester, "returns 0 when no one in Manchester"
).when_called_with(
    [
        {
            "name": "Carrie",
            "lives": {"country": "UK", "city": "Leeds"},
            "age": 32,
        }
    ]
).returns(
    0
)

SkipCheck(
    tally_people_in_manchester, "returns 1 when one person in Manchester"
).when_called_with(
    [
        {
            "name": "Emmeline",
            "lives": {"country": "UK", "city": "Manchester"},
            "age": 32,
        }
    ]
).returns(
    1
)

SkipCheck(
    tally_people_in_manchester,
    "returns the number of people in Manchester when passed multiple",
).when_called_with(
    [
        {
            "name": "Carrie",
            "lives": {"country": "UK", "city": "Leeds"},
            "age": 32,
        },
        {
            "name": "Ray",
            "lives": {"country": "UK", "city": "Manchester"},
            "age": 31,
        },
        {
            "name": "Simon",
            "lives": {"country": "Middle Earth", "city": "Moria"},
            "age": 275,
        },
        {
            "name": "Cat",
            "lives": {"country": "UK", "city": "Manchester"},
            "age": 42,
        },
        {
            "name": "Danika",
            "lives": {"country": "UK", "city": "Manchester"},
            "age": 22,
        },
    ]
).returns(
    3
)


"""
Write a function takes a list of dictionaries describing `dogs` and returns a
list of the names of all the pug owners.


get_pug_owners([
    {'name': 'Beatrice', 'breed': 'Lurcher', 'owner': 'Tom'},
    {'name': 'Max', 'breed': 'Pug', 'owner': 'Izzi'},
    {'name': 'Poppy', 'breed': 'Pug', 'owner': 'Anat'}
]) # returns ['Izzi', 'Anat']

get_pug_owners([
    {'name': 'Beatrice', 'breed': 'Lurcher', 'owner': 'Tom'},
]) # returns []

get_pug_owners([]) # returns []
"""


def get_pug_owners(dogs):
    pass


SkipCheck(
    get_pug_owners, "returns empty list when passed empty list"
).when_called_with([]).returns([])

SkipCheck(get_pug_owners, "returns empty list when no pugs").when_called_with(
    [
        {"name": "Beatrice", "breed": "Lurcher", "owner": "Tom"},
    ]
).returns([])

SkipCheck(get_pug_owners, "returns single pug owner").when_called_with(
    [
        {"name": "Beatrice", "breed": "Pug", "owner": "Tom"},
    ]
).returns(["Tom"])

SkipCheck(get_pug_owners, "test multiple invalid dogs").when_called_with(
    [
        {"name": "Beatrice", "breed": "Lurcher", "owner": "Tom"},
        {"name": "Max", "breed": "Dalmation", "owner": "Izzi"},
        {"name": "Poppy", "breed": "Alsatian", "owner": "Anat"},
    ]
).returns([])

SkipCheck(get_pug_owners, "test mixed list").when_called_with(
    [
        {"name": "Beatrice", "breed": "Lurcher", "owner": "Tom"},
        {"name": "Max", "breed": "Pug", "owner": "Izzi"},
        {"name": "Poppy", "breed": "Pug", "owner": "Anat"},
    ]
).returns(["Izzi", "Anat"])


"""
In this function, you will be provided with a dictionary. That dictionary is
storing information on keys:

{
    'name': 'Tom',
    'job': ['writing katas', 'marking'],
    'favourite_shop': [
        "Paul's Donkey University",
        "Shaq's Taxidermy Shack",
        "Sam's Pet Shop"
    ]
}

In some cases, however, the keys have been very badly named. Good naming
convention tells us that the __keys containing lists__ should have
plural names.
This function should return a new dictionary that is a copy of the input but
with any keys that contain lists pluralised (an 's' added to the end.)

{
    'name': 'Tom',
    'jobs': ['writing katas', 'marking'],
    'favourite_shops': [
        "Paul's Donkey University",
        "Shaq's Taxidermy Shack",
        "Sam's Pet Shop"
    ]
}
"""


def pluralise_keys(dictionary):
    pass


SkipCheck(
    pluralise_keys, "returns empty dictionary when passed empty dictionary"
).when_called_with({}).returns({})

# Test unnested dict
test_dict = {"a": 1, "b": 2, "c": 3}
SkipCheck(
    pluralise_keys, "returns unchanged dictionary when there are no lists"
).when_called_with(test_dict).returns({"a": 1, "b": 2, "c": 3})

SkipCheck(
    pluralise_keys, "returns copy of dictionary when there are no lists"
).when_called_with(test_dict).is_not_same_as(test_dict)

# Test nested dict
test_dict = {"a": 1, "b": 2, "c": {"d": 3, "e": 4}}
SkipCheck(
    pluralise_keys, "returns unchanged dictionary with nested dicts"
).when_called_with(test_dict).returns({"a": 1, "b": 2, "c": {"d": 3, "e": 4}})

SkipCheck(
    pluralise_keys, "returns copy of dictionary with nested dicts"
).when_called_with(test_dict).is_not_same_as(test_dict)

# Test dict with one list 
test_dict = {"a": 1, "b": 2, "num": [3, 4]}
SkipCheck(
    pluralise_keys, "returns dictionary with one key changed"
).when_called_with(test_dict).returns(
    {"a": 1, "b": 2, "nums": [3, 4]}
)

SkipCheck(
    pluralise_keys, "returns copy of dictionary with one nested list"
).when_called_with(test_dict).is_not_same_as(test_dict)

# Test dict with multi list 
test_dict = {
        "name": "Tom",
        "job": ["writing katas", "marking"],
        "favourite_shop": [
            "Paul's Donkey University",
            "Shaq's Taxidermy Shack",
            "Sam's Pet Shop",
        ]
    }
SkipCheck(
    pluralise_keys, "returns dictionary with several keys changed"
).when_called_with(test_dict).returns({
        "name": "Tom",
        "jobs": ["writing katas", "marking"],
        "favourite_shops": [
            "Paul's Donkey University",
            "Shaq's Taxidermy Shack",
            "Sam's Pet Shop",
        ]
    })

SkipCheck(
    pluralise_keys, "returns copy of dictionary with several lists"
).when_called_with(test_dict).is_not_same_as(test_dict)


"""
Write a function that takes a `string` and returns a list containing the
length of each word in that string.
If passed an empty string, the function should return an empty list.
Words will be separated by a single space.


get_word_lengths('hello') # returns [5]

get_word_lengths('hello everyone') # returns [5, 8]

get_word_lengths('this is a sentence') # returns [4, 2, 1, 8]

get_word_lengths('') # returns []

"""


def get_word_lengths(string):
    pass


SkipCheck(
    get_word_lengths, "returns empty list when passed empty string"
).when_called_with("").returns([])

SkipCheck(get_word_lengths, "returns single word length").when_called_with(
    "hello"
).returns([5])

SkipCheck(get_word_lengths, "returns two word lengths").when_called_with(
    "hello everyone"
).returns([5, 8])

SkipCheck(get_word_lengths, "returns multiple word lengths").when_called_with(
    "It is a pleasure to meet you new coder"
).returns([2, 2, 1, 8, 2, 4, 3, 3, 5])

"""
Write a function that takes a list of `words` and returns a list containing
all of the words that are
palindromes (the same word forwards and backwards, e.g. 'pip').


get_palindromes(['racecar']) # returns ['racecar']

get_palindromes(['dog', 'dud', 'car', 'mum']) # returns ['dud', 'mum']

get_palindromes(['apple', 'orange', 'banana']) # returns []

get_palindromes([]) # returns []

"""


def get_palindromes(words):
    pass


SkipCheck(
    get_palindromes, "returns empty list when passed empty list"
).when_called_with([]).returns([])

SkipCheck(
    get_palindromes, "returns empty list when passed invalid item"
).when_called_with(["boom"]).returns([])

SkipCheck(get_palindromes, "returns single valid item").when_called_with(
    ["racecar"]
).returns(["racecar"])

SkipCheck(get_palindromes, "returns multiple items").when_called_with(
    ["dog", "dud", "car", "mum"]
).returns(["dud", "mum"])

SkipCheck(get_palindromes, "returns no items").when_called_with(
    ["apple", "orange", "banana"]
).returns([])


"""
Write a function that takes a `string` and returns a string with all of the
letter characters replaced with an 'X'.
Any non-letter characters (e.g. punctuation, symbols) should be left as they
are.

replace_letters_with_x('a') # returns 'X'

replace_letters_with_x('A') # returns 'X'

replace_letters_with_x('hello') # returns 'XXXXX'

replace_letters_with_x('Hello!') # returns 'XXXXX!'

replace_letters_with_x('Do you like coding?') # returns 'XX XXX XXXX XXXXXX?'

"""


def replace_letters_with_x(string):
    pass


SkipCheck(
    replace_letters_with_x, "returns empty string when passed empty string"
).when_called_with("").returns("")

SkipCheck(
    replace_letters_with_x, "returns single non-letter character"
).when_called_with("5").returns("5")

SkipCheck(
    replace_letters_with_x, "returns single special character"
).when_called_with("&").returns("&")

SkipCheck(
    replace_letters_with_x, "returns single letter changed to X"
).when_called_with("a").returns("X")

SkipCheck(
    replace_letters_with_x, "returns single letter changed to X"
).when_called_with("K").returns("X")

SkipCheck(
    replace_letters_with_x, "returns single word changed to X"
).when_called_with("hello").returns("XXXXX")

SkipCheck(
    replace_letters_with_x, "returns single word changed to X"
).when_called_with("NoRtHcOdErS").returns("XXXXXXXXXXX")


SkipCheck(
    replace_letters_with_x, "returns single word changed to X with punctuation"
).when_called_with("Kaboom!").returns("XXXXXX!")

SkipCheck(
    replace_letters_with_x, "returns single word changed to X with punctuation"
).when_called_with("Northcoders?").returns("XXXXXXXXXXX?")

SkipCheck(replace_letters_with_x, "returns several words").when_called_with(
    "Do you like coding?"
).returns("XX XXX XXXX XXXXXX?")
