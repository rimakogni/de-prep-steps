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
    # Your code here
    pass


def test_empty_list_returns_empty_list():
    assert flip_booleans([]) == []


def test_single_true_returns_single_false():
    assert flip_booleans([True]) == [False]


def test_single_false_returns_single_true():
    assert flip_booleans([False]) == [True]


def test_all_falses_returns_all_true():
    assert flip_booleans([False, False, False]) == [True, True, True]


def test_all_trues_returns_all_falses():
    assert flip_booleans([True, True, True]) == [False, False, False]


def test_mixed_trues_and_falses_flipped_correctly():
    assert flip_booleans([True, False, False, True]) == [
        False,
        True,
        True,
        False,
    ]


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
    # Your code here
    pass


def test_return_copy_of_empty_data_unchanged():
    student = {}
    assert translate_key(student, "prénom", "first_name") == {}
    assert translate_key(student, "prénom", "first_name") is not student


def test_return_unchanged_if_key_not_present():
    student = {"first_name": "Carla", "surname": "Bruni", "job": "Artist"}
    assert translate_key(student, "prénom", "first_name") == student
    assert translate_key(student, "prénom", "first_name") is not student


def test_translate_key_if_required():
    student1 = {"prénom": "Carla", "surname": "Bruni", "job": "Artist"}
    expected1 = {"first_name": "Carla", "surname": "Bruni", "job": "Artist"}
    result1 = translate_key(student1, "prénom", "first_name")

    assert result1 == expected1
    assert result1 is not student1

    student2 = {"first_name": "Jean", "surname": "Reno", "emploi": "Actor"}
    expected2 = {"first_name": "Jean", "surname": "Reno", "job": "Actor"}
    result2 = translate_key(student2, "emploi", "job")

    assert result2 == expected2
    assert result2 is not student2


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
    # Your code here
    pass


def test_empty_list_returns_none():
    assert find_first_dentist([]) is None


def test_returns_none_if_person_not_dentist():
    assert (
        find_first_dentist([{"name": "Callum", "is_dentist": False}]) is None
    )


def test_returns_person_if_dentist():
    dentist = {"name": "Callum", "is_dentist": True}
    assert (
        find_first_dentist([{"name": "Callum", "is_dentist": True}]) == dentist
    )


def test_returns_first_dentist():
    first_dentist = {"name": "Carrie", "is_dentist": True}
    dentists = [
        {"name": "Callum", "is_dentist": False},
        {"name": "Carrie", "is_dentist": True},
    ]
    assert find_first_dentist(dentists) == first_dentist


def test_returns_first_dentist_of_many():
    dentist = {"name": "Callum", "is_dentist": True}
    dentists = [
        {"name": "Callum", "is_dentist": True},
        {"name": "Carrie", "is_dentist": True},
    ]
    assert find_first_dentist(dentists) == dentist


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
    # Your code here
    pass


def test_empty_list():
    assert tally_people_in_manchester([]) == 0


def test_single_person_not_in_manchester():
    people = [
        {
            "name": "Carrie",
            "lives": {"country": "UK", "city": "Leeds"},
            "age": 32,
        }
    ]
    assert tally_people_in_manchester(people) == 0


def test_single_person_in_manchester():
    people = [
        {
            "name": "Emmeline",
            "lives": {"country": "UK", "city": "Manchester"},
            "age": 32,
        }
    ]
    assert tally_people_in_manchester(people) == 1


def test_several_people():
    people = [
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
    assert tally_people_in_manchester(people) == 3


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
    # Your code here
    pass


def test_empty_list():
    assert get_pug_owners([]) == []


def test_single_invalid_dog():
    assert (
        get_pug_owners(
            [
                {"name": "Beatrice", "breed": "Lurcher", "owner": "Tom"},
            ]
        )
        == []
    )


def test_single_valid_dog():
    assert get_pug_owners(
        [
            {"name": "Beatrice", "breed": "Pug", "owner": "Tom"},
        ]
    ) == ["Tom"]


def test_many_invalid_dogs():
    dogs = [
        {"name": "Beatrice", "breed": "Lurcher", "owner": "Tom"},
        {"name": "Max", "breed": "Dalmation", "owner": "Izzi"},
        {"name": "Poppy", "breed": "Alsatian", "owner": "Anat"},
    ]
    assert get_pug_owners(dogs) == []


def test_mixed_list():
    dogs = [
        {"name": "Beatrice", "breed": "Lurcher", "owner": "Tom"},
        {"name": "Max", "breed": "Pug", "owner": "Izzi"},
        {"name": "Poppy", "breed": "Pug", "owner": "Anat"},
    ]
    assert get_pug_owners(dogs) == ["Izzi", "Anat"]


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
    # Your code here
    pass


def test_empty_dictionary():
    assert pluralise_keys({}) == {}


def test_dictionary_with_no_arrays_returns_copy():
    data = {"a": 1, "b": 2, "c": 3}
    assert pluralise_keys(data) == {"a": 1, "b": 2, "c": 3}
    assert pluralise_keys(data) is not data


def test_dictionary_with_nested_dicts_returns_copy():
    data = {"a": 1, "b": 2, "c": {"d": 3, "e": 4}}
    assert pluralise_keys(data) == {"a": 1, "b": 2, "c": {"d": 3, "e": 4}}
    assert pluralise_keys(data) is not data


def test_dictionary_with_one_nested_list():
    data = {"a": 1, "b": 2, "num": [3, 4]}
    assert pluralise_keys(data) == {"a": 1, "b": 2, "nums": [3, 4]}
    assert pluralise_keys(data) is not data


def test_dictionary_with_several_lists():
    data = {
        "name": "Tom",
        "job": ["writing katas", "marking"],
        "favourite_shop": [
            "Paul's Donkey University",
            "Shaq's Taxidermy Shack",
            "Sam's Pet Shop",
        ],
    }
    result = pluralise_keys(data)
    assert result == {
        "name": "Tom",
        "jobs": ["writing katas", "marking"],
        "favourite_shops": [
            "Paul's Donkey University",
            "Shaq's Taxidermy Shack",
            "Sam's Pet Shop",
        ],
    }
    assert result is not data


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
    # Your code here
    pass


def test_empty_string():
    assert get_word_lengths("") == []


def test_single_word():
    assert get_word_lengths("hello") == [5]
    assert get_word_lengths("sesquipedalian") == [14]


def test_two_words():
    assert get_word_lengths("hello everyone") == [5, 8]


def test_many_words():
    assert get_word_lengths("this is a sentence") == [4, 2, 1, 8]


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
    # Your code here
    pass


def test_empty_list():
    assert get_palindromes([]) == []


def test_single_invalid_item():
    assert get_palindromes(["boom"]) == []


def test_single_valid_item():
    assert get_palindromes(["racecar"]) == ["racecar"]


def test_several_items():
    assert get_palindromes(["dog", "dud", "car", "mum"]) == ["dud", "mum"]


def test_several_invalid_items():
    assert get_palindromes(["apple", "orange", "banana"]) == []


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
    # Your code here
    pass


def test_empty_string():
    assert replace_letters_with_x("") == ""


def test_single_non_letter_character():
    assert replace_letters_with_x("5") == "5"
    assert replace_letters_with_x("&") == "&"


def test_single_letter():
    assert replace_letters_with_x("a") == "X"
    assert replace_letters_with_x("K") == "X"


def test_several_letters():
    assert replace_letters_with_x("Kaboom") == "XXXXXX"
    assert replace_letters_with_x("Northcoders") == "XXXXXXXXXXX"


def test_several_characters():
    assert replace_letters_with_x("Kaboom!") == "XXXXXX!"
    assert replace_letters_with_x("Northcoders?") == "XXXXXXXXXXX?"


def test_several_words():
    assert (
        replace_letters_with_x("Do you like coding?") == "XX XXX XXXX XXXXXX?"
    )


