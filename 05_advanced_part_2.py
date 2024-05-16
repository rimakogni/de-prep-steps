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
