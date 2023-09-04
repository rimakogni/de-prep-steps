"""
`count_the_chars` is a function that takes a list of values and a character. It should return a number representing 
the total number of times that the character appears in the list.

Unfortunately, it looks like the function isn't working.

Can you work out what needs changing to make the function pass all the tests?
"""

def count_the_chars(character_list, character):
    count = 0
    for i in range(character_list):
        if character_list[i] = character:
            count + 1
            return count
        

# Do not change code below this line

def test_returns_zero_if_no_match():
    char_list = []
    assert count_the_chars(char_list, 'a') == 0
    char_list = ['a', 'b', 'c']
    assert count_the_chars(char_list, 'd') == 0


def test_counts_the_occurrences_in_simple_list():
    char_list = ['a', 'b', 'c']
    assert count_the_chars(char_list, 'b') == 1
    char_list = ['4', '6', 'hello', '2', '6', '6']
    assert count_the_chars(char_list, '6')


def test_counts_the_occurrences_in_mixed_lists():
    char_list = ['a', 1, 'b', 2, 'c', 3]
    assert count_the_chars(char_list, 'b') == 1
    char_list = ['1', 'a', 2, '2', 'b', 1, 'a', '1', '2', 'c', 3, '2', 2]
    assert count_the_chars(char_list, '2') == 3
    assert count_the_chars(char_list, 1) == 1