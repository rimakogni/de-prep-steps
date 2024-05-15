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


"""
Write a function that takes a string of a mobile number (`mobile_number`).
It should return `True` if the number is a valid UK number and `False` if not.

A valid mobile number may begin with:

1. '07' followed by 9 more digits.
2. '+447' followed by 9 more digits.
3. '00447' followed by 9 more digits.

Anything else is `invalid`.

is_valid_mobile_number('07726') # returns False

is_valid_mobile_number('07123456789') # returns True

is_valid_mobile_number('+447123456789') # returns True

is_valid_mobile_number('00447123456789') # returns True

is_valid_mobile_number('0712345678!') # returns False
"""


def is_valid_mobile_number(mobile_number):
    # Your code here
    pass


def test_empty_string_invalid():
    assert not is_valid_mobile_number("")


def test_length_less_than_eleven_is_false():
    assert not is_valid_mobile_number("0754321")


def test_length_more_than_fourteen_invalid():
    assert not is_valid_mobile_number("004471234567890")


def test_valid_examples_length_eleven():
    assert is_valid_mobile_number("07123456789")
    assert is_valid_mobile_number("07284619462")


def test_invalid_examples_length_eleven():
    assert not is_valid_mobile_number("+4471234567")
    assert not is_valid_mobile_number("00447876543")


def test_length_twelve_invalid():
    assert not is_valid_mobile_number("071234567890")


def test_valid_examples_length_thirteen():
    assert is_valid_mobile_number("+447123456789")
    assert is_valid_mobile_number("+447395612859")


def test_invalid_examples_length_thirteen():
    assert not is_valid_mobile_number("0044712345678")
    assert not is_valid_mobile_number("0739561285901")


def test_valid_examples_length_fourteen():
    assert is_valid_mobile_number("00447123456789")
    assert is_valid_mobile_number("00447654297190")


def test_invalid_examples_length_fourteen():
    assert not is_valid_mobile_number("+4471234567890")
    assert not is_valid_mobile_number("07102938475610")


def test_invalid_if_contains_non_numeric_characters_other_than_first():
    assert not is_valid_mobile_number("0728461a462")
    assert not is_valid_mobile_number("+4473956+2859")
    assert not is_valid_mobile_number("00447123!56789")


"""
Write a function that takes a `string` and `adds` all the numbers in the
string together.
The function should then return this total as an integer.

Consecutive numbers should be treated as individual digits
(e.g. '123' is the same as 1, 2, 3 and not 123).

sum_digits_from_string('1') # returns 1

sum_digits_from_string('168') # returns 15

sum_digits_from_string('he12ll3') # returns 6

sum_digits_from_string('northcoders') # returns 0

"""


def sum_digits_from_string(string):
    # Your code here
    pass


def test_empty_string():
    assert sum_digits_from_string("") == 0


def test_single_non_numeric_digit():
    assert sum_digits_from_string("a") == 0


def test_single_numeral():
    assert sum_digits_from_string("5") == 5
    assert sum_digits_from_string("8") == 8
    assert sum_digits_from_string("0") == 0


def test_numeral_string():
    assert sum_digits_from_string("168") == 15
    assert sum_digits_from_string("25580") == 20


def test_mixed_string():
    assert sum_digits_from_string("he12ll3") == 6
    assert sum_digits_from_string("We always play 4-4-2") == 10


def test_string_with_no_numbers():
    assert sum_digits_from_string("northcoders") == 0
    assert sum_digits_from_string("A fine bootcamp") == 0


"""
Write a function that takes a list of `names` representing a person's full
name and returns a list
of each person whose last name is 'Williams'.


get_williams(['David Williams']) # returns ['David Williams']

get_williams(['David Williams', 'Sarah Williams'])
# returns ['David Williams', 'Sarah Williams']

get_williams(['Kirsty February']) # returns []

get_williams(['Kirsty February', 'Sam Williams']) # returns ['Sam Williams']

get_williams(['William David', 'Cole Williamson']) # returns []

"""


def get_williams(names):
    # Your code here
    pass


def test_empty_list():
    assert get_williams([]) == []


def test_single_invalid_item():
    assert get_williams(["Kirsty February"]) == []


def test_single_valid_item():
    assert get_williams(["David Williams"]) == ["David Williams"]


def test_several_valid_items():
    assert get_williams(["David Williams", "Sarah Williams"]) == [
        "David Williams",
        "Sarah Williams",
    ]


def test_mixed_items():
    assert get_williams(["Kirsty February", "Sam Williams"]) == [
        "Sam Williams"
    ]


def test_rogue_williams():
    assert get_williams(["William David", "Cole Williamson"]) == []


"""
Write a function that takes a list of `numbers` and returns a list containing
the factorial of each number in the list.

The factorial of a number is the product of that number and all the integers
below it.
E.g. the factorial of 4 is 4 * 3 * 2 * 1 = 24


get_factorials([3]) # returns [6]

get_factorials([3, 4]) # returns [6, 24]

get_factorials([1, 5, 2]) # returns [1, 120, 2]

get_factorials([]) # returns []

"""


def get_factorials(numbers):
    # Your code here
    pass


def test_empty_list_generates_empty_list():
    assert get_factorials([]) == []


def test_one_item():
    assert get_factorials([3]) == [6]


def test_number_one():
    assert get_factorials([1]) == [1]


def test_two_items():
    assert get_factorials([3, 4]) == [6, 24]


"""
Write a function that takes a `number` and returns the largest number that can
be made by rearranging the digits.

largest_number(3) # returns 3

largest_number(123) # returns 321

largest_number(937846) # returns 987643

largest_number(43) # returns 43

"""


def largest_number(number):
    pass


def test_single_digit():
    assert largest_number(3) == 3
    assert largest_number(9) == 9


def test_double_digits_correct_order():
    assert largest_number(43) == 43


def test_double_digits_incorrect_order():
    assert largest_number(34) == 43


def test_double_digits_repeated():
    assert largest_number(44) == 44


def test_triple_digits_correct_order():
    assert largest_number(321) == 321


def test_triple_digits_incorrect_order():
    assert largest_number(213) == 321


def test_triple_digits_two_repeated():
    assert largest_number(233) == 332


def test_lots_of_digits():
    assert largest_number(937846) == 987643
    assert largest_number(8456329456) == 9866554432


"""
Write a function that takes a `number` and returns a matrix of nested lists
equal to the number passed.
Each element in each sublist should be set to a value of `None`.


generate_matrix(1) # returns [[None]]

generate_matrix(2) # returns [[None, None], [None, None]]

generate_matrix(3) # returns [
    [None, None, None],
    [None, None, None],
    [None, None, None]
    ]

"""


def generate_matrix(number):
    # Your code here
    pass


def test_zero_generates_empty_list():
    assert generate_matrix(0) == []


def test_one():
    assert generate_matrix(1) == [[None]]


def test_two():
    assert generate_matrix(2) == [[None, None], [None, None]]


def test_three():
    assert generate_matrix(3) == [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def test_arbitrary():
    import random

    number = random.randint(4, 20)
    result = generate_matrix(number)
    assert len(result) == number
    for j in range(number):
        assert len(result[j]) == number
        for k in range(number):
            assert result[j][k] == None  # noqa


"""
This function takes a list of fruit (`orchard`) in the format:


['apple', 'apple', 'apple', 'apple', 'elppa', 'apple']


The fruit will all be the 'right way round' apart from one fruit!

Your function should return its zero-based index position.
So in this example, the function should return 4.

Note: The fruit will not always be apple, but it will always be an orchard
of the same kind of fruit.


find_wrong_way_fruit(['apple', 'apple', 'elppa']) # returns 2

find_wrong_way_fruit(['apple', 'elppa', 'apple']) # returns 1

find_wrong_way_fruit(['banana', 'ananab', 'banana', 'banana']) # returns 1

find_wrong_way_fruit(['apple', 'elppa']) # returns 0 as we can't tell which
one is the right way round with less than 3 pieces of fruit

"""


def find_wrong_way_fruit(orchard):
    # Your code here
    pass


def test_returns_zero_for_singleton_list():
    assert find_wrong_way_fruit(["apple"]) == 0


def test_returns_zero_for_list_length_two():
    assert find_wrong_way_fruit(["grape", "eparg"]) == 0


def test_finds_last_item_if_reversed():
    assert find_wrong_way_fruit(["apple", "apple", "elppa"]) == 2


def test_finds_first_item_if_reversed():
    assert find_wrong_way_fruit(["elppa", "apple", "apple"]) == 0


def test_finds_intermediate_reversed_item():
    assert find_wrong_way_fruit(["banana", "ananab", "banana", "banana"]) == 1


"""
This function takes a string of DNA, such as 'GTCA', and returns a list
containing correctly matched DNA pairs.

The pairs are as follows:

'G' -> 'C'
'C' -> 'G'
'T' -> 'A'
'A' -> 'T'

The function should ignore any letters that are not valid DNA pairs
(e.g. not 'G', 'C', 'T' or 'A').
However, it should also work for lowercase and uppercase letters.

dna_pairs('G') # returns ['GC']
dna_pairs('GAT') # returns ['GC', 'AT', 'TA']
dna_pairs('GYTC') # returns ['GC', 'TA', 'CG']
dna_pairs('gat') # returns ['GC', 'AT', 'TA']

"""


def dna_pairs(dna_string):
    # Your code here
    pass


def test_empty_string_produces_empty_list():
    assert dna_pairs("") == []


def test_invalid_letters_ignored():
    assert dna_pairs("B") == []
    assert dna_pairs("z") == []


def test_single_valid_uppercase_returns_correct_pair():
    assert dna_pairs("G") == ["GC"]
    assert dna_pairs("C") == ["CG"]
    assert dna_pairs("T") == ["TA"]
    assert dna_pairs("A") == ["AT"]


def test_single_valid_lowercase_returns_correct_uppercase_results():
    assert dna_pairs("g") == ["GC"]
    assert dna_pairs("c") == ["CG"]
    assert dna_pairs("t") == ["TA"]
    assert dna_pairs("a") == ["AT"]


def test_long_valid_uppercase_string_returns_valid_list():
    assert dna_pairs("GAT") == ["GC", "AT", "TA"]


def test_long_uppercase_with_invalid_chars_returns_valid_list():
    assert dna_pairs("GYTC") == ["GC", "TA", "CG"]


def test_mixed_string_returns_valid_list():
    assert dna_pairs("CGauTzgAcj") == [
        "CG",
        "GC",
        "AT",
        "TA",
        "GC",
        "AT",
        "CG",
    ]


"""
This function receives a `tweet` that will contain a number of mentions and
hashtags as on Twitter, sorry 'X'.
A hashtag is marked by `#` and a mention is marked by `@`.

The function should return a dictionary describing the number of hashtags and
mentions found in the string:
Example:
tweet = "So excited to start at @northcoders on Monday!
#learntocode #codingbootcamp"

tally_hashtags_and_mentions(tweet) # returns {'hashtags': 2, 'mentions': 1}
"""


def tally_hashtags_and_mentions(tweet):
    # Your code here
    pass


def test_empty_tweet():
    assert tally_hashtags_and_mentions("") == {"hashtags": 0, "mentions": 0}


def test_single_hashtag():
    assert tally_hashtags_and_mentions("#omg") == {
        "hashtags": 1,
        "mentions": 0,
    }


def test_single_mention():
    assert tally_hashtags_and_mentions("@paul_c") == {
        "hashtags": 0,
        "mentions": 1,
    }


def test_tweet_containing_single_hashtag():
    tweet = "Best place to learn #python?"
    assert tally_hashtags_and_mentions(tweet) == {"hashtags": 1, "mentions": 0}


def test_tweet_containing_single_mention():
    tweet = "Need coding help, paging @Danika ..."
    assert tally_hashtags_and_mentions(tweet) == {"hashtags": 0, "mentions": 1}


def test_tweet_containing_several_hashtags_and_mentions():
    tweet1 = "So excited to start at @northcoders on Monday! #learntocode #codingbootcamp"  # noqa
    assert tally_hashtags_and_mentions(tweet1) == {
        "hashtags": 2,
        "mentions": 1,
    }
    tweet2 = "Thanks to @Alex and @Cat for helping with my #python #coding"
    assert tally_hashtags_and_mentions(tweet2) == {
        "hashtags": 2,
        "mentions": 2,
    }
