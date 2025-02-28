from test_api.checks import Check, SkipCheck

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
    pass


Check(is_valid_mobile_number, "empty string is invalid").when_called_with(
    ""
).returns(False)

Check(
    is_valid_mobile_number, "length less than eleven is false"
).when_called_with("0754321").returns(False)

Check(
    is_valid_mobile_number, "length more than eleven is false"
).when_called_with("004471234567890").returns(False)

Check(is_valid_mobile_number, "valid eleven digit number").when_called_with(
    "07123456789"
).returns(True)

Check(is_valid_mobile_number, "invalid eleven digit number").when_called_with(
    "+4471234567"
).returns(False)

Check(is_valid_mobile_number, "invalid twelve digit number").when_called_with(
    "071234567890"
).returns(False)

Check(is_valid_mobile_number, "valid thirteen digit number").when_called_with(
    "+447123456789"
).returns(True)

Check(
    is_valid_mobile_number, "invalid thirteen digit number"
).when_called_with("0044712345678").returns(False)

Check(is_valid_mobile_number, "valid fourteen digit number").when_called_with(
    "00447123456789"
).returns(True)

Check(
    is_valid_mobile_number, "invalid fourteen digit number"
).when_called_with("+4471234567890").returns(False)

Check(
    is_valid_mobile_number,
    "invalid if contains non-numeric characters other than first",
).when_called_with("0728461a462").returns(False)


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
    pass


SkipCheck(sum_digits_from_string, "empty string returns 0").when_called_with(
    ""
).returns(0)

SkipCheck(sum_digits_from_string, "non numeric returns 0").when_called_with(
    "a"
).returns(0)

SkipCheck(
    sum_digits_from_string, "single digit returns integer"
).when_called_with("5").returns(5)

SkipCheck(sum_digits_from_string, "two digits returns sum").when_called_with(
    "16"
).returns(7)

SkipCheck(sum_digits_from_string, "three digits returns sum").when_called_with(
    "255"
).returns(12)

SkipCheck(sum_digits_from_string, "mixed string returns sum").when_called_with(
    "he12ll3"
).returns(6)

SkipCheck(sum_digits_from_string, "no numbers returns 0").when_called_with(
    "northcoders"
).returns(0)


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
    pass


SkipCheck(get_williams, "empty list").when_called_with([]).returns([])

SkipCheck(get_williams, "single invalid item").when_called_with(
    ["Kirsty February"]
).returns([])

SkipCheck(get_williams, "single valid item").when_called_with(
    ["David Williams"]
).returns(["David Williams"])

SkipCheck(get_williams, "several valid items").when_called_with(
    ["David Williams", "Sarah Williams"]
).returns(["David Williams", "Sarah Williams"])

SkipCheck(get_williams, "mixed items").when_called_with(
    ["Kirsty February", "Sam Williams"]
).returns(["Sam Williams"])

SkipCheck(get_williams, "mixed items with rogue Williams").when_called_with(
    ["William David", "Cole Williamson"]
).returns([])


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
    pass


SkipCheck(get_factorials, "empty list generates empty list").when_called_with(
    []
).returns([])

SkipCheck(get_factorials, "single item").when_called_with([3]).returns([6])


SkipCheck(get_factorials, "two items").when_called_with([3, 4]).returns(
    [6, 24]
)

SkipCheck(get_factorials, "The infamous number 1").when_called_with(
    [1]
).returns([1])


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


SkipCheck(largest_number, "single digit").when_called_with(3).returns(3)

SkipCheck(largest_number, "double digits correct order").when_called_with(
    43
).returns(43)


SkipCheck(largest_number, "double digits incorrect order").when_called_with(
    34
).returns(43)


SkipCheck(largest_number, "double digits repeated").when_called_with(
    44
).returns(44)


SkipCheck(largest_number, "triple digits correct order").when_called_with(
    321
).returns(321)


SkipCheck(largest_number, "triple digits incorrect order").when_called_with(
    213
).returns(321)


SkipCheck(largest_number, "triple digits two repeated").when_called_with(
    233
).returns(332)


SkipCheck(largest_number, "lots of digits").when_called_with(
    8456329456
).returns(9866554432)

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
    pass


SkipCheck(generate_matrix, "zero generates empty list").when_called_with(
    0
).returns([])

SkipCheck(
    generate_matrix, "single digit generates single nested list"
).when_called_with(1).returns([[None]])

SkipCheck(
    generate_matrix, "two digits generates two nested lists"
).when_called_with(2).returns([[None, None], [None, None]])


SkipCheck(
    generate_matrix, "three digits generates three nested lists"
).when_called_with(3).returns(
    [[None, None, None], [None, None, None], [None, None, None]]
)


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
    pass


SkipCheck(
    find_wrong_way_fruit, "returns zero for singleton list"
).when_called_with(["apple"]).returns(0)

SkipCheck(
    find_wrong_way_fruit, "returns zero for list length two"
).when_called_with(["grape", "eparg"]).returns(0)

SkipCheck(
    find_wrong_way_fruit, "finds last item if reversed"
).when_called_with(["apple", "apple", "elppa"]).returns(2)

SkipCheck(
    find_wrong_way_fruit, "finds first item if reversed"
).when_called_with(["elppa", "apple", "apple"]).returns(0)

SkipCheck(
    find_wrong_way_fruit, "finds intermediate reversed item"
).when_called_with(["banana", "ananab", "banana", "banana"]).returns(1)


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
    pass


SkipCheck(dna_pairs, "empty string produces empty list").when_called_with(
    ""
).returns([])

SkipCheck(
    dna_pairs, "single invalid letter produces empty list"
).when_called_with("B").returns([])

SkipCheck(dna_pairs, "single valid uppercase letter G").when_called_with(
    "G"
).returns(["GC"])

SkipCheck(dna_pairs, "single valid uppercase letter C").when_called_with(
    "C"
).returns(["CG"])

SkipCheck(dna_pairs, "single valid uppercase letter T").when_called_with(
    "T"
).returns(["TA"])

SkipCheck(dna_pairs, "single valid uppercase letter A").when_called_with(
    "A"
).returns(["AT"])

SkipCheck(dna_pairs, "single valid lowercase letter g").when_called_with(
    "g"
).returns(["GC"])

SkipCheck(dna_pairs, "single valid lowercase letter c").when_called_with(
    "c"
).returns(["CG"])

SkipCheck(dna_pairs, "single valid lowercase letter t").when_called_with(
    "t"
).returns(["TA"])

SkipCheck(dna_pairs, "single valid lowercase letter a").when_called_with(
    "a"
).returns(["AT"])

SkipCheck(
    dna_pairs, "long valid uppercase string returns valid list"
).when_called_with("GAT").returns(["GC", "AT", "TA"])

SkipCheck(
    dna_pairs, "long uppercase string with invalid chars returns valid list"
).when_called_with("GYTC").returns(["GC", "TA", "CG"])

SkipCheck(dna_pairs, "mixed string returns valid list").when_called_with(
    "CGauTzgAcj"
).returns(
    [
        "CG",
        "GC",
        "AT",
        "TA",
        "GC",
        "AT",
        "CG",
    ]
)


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


SkipCheck(tally_hashtags_and_mentions, "test empty tweet").when_called_with(
    ""
).returns({"hashtags": 0, "mentions": 0})

SkipCheck(tally_hashtags_and_mentions, "test single hashtag").when_called_with(
    "#omg"
).returns({"hashtags": 1, "mentions": 0})

SkipCheck(tally_hashtags_and_mentions, "test single mention").when_called_with(
    "@paul_c"
).returns({"hashtags": 0, "mentions": 1})

SkipCheck(
    tally_hashtags_and_mentions, "test tweet containing single hashtag"
).when_called_with("Best place to learn #python?").returns(
    {"hashtags": 1, "mentions": 0}
)

SkipCheck(
    tally_hashtags_and_mentions, "test tweet containing single mention"
).when_called_with("Need coding help, paging @Danika ...").returns(
    {"hashtags": 0, "mentions": 1}
)

SkipCheck(
    tally_hashtags_and_mentions,
    "test tweet containing several hashtags and mentions",
).when_called_with(
    "So excited to start at @northcoders on Monday! #learntocode #codingbootcamp"
).returns(
    {"hashtags": 2, "mentions": 1}
)

SkipCheck(
    tally_hashtags_and_mentions,
    "test tweet containing several hashtags and mentions",
).when_called_with(
    "Thanks to @Alex and @Cat for helping with my #python #coding"
).returns(
    {"hashtags": 2, "mentions": 2}
)
