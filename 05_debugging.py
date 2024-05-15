"""
get_first_item is a function that takes an list and returns the first element.

Unfortunately, it looks like the function is currently throwing a NameError.

Can you work out what needs to be changed to make the function pass all the
tests?
"""


def get_first_item(my_list):
    first_item = my_list[0]
    return firstitem


# Do not change code below this line

def test_gets_fist_number_item():
    assert get_first_item([1, 2, 3, 4]) == 1


def test_gets_first_string_item():
    assert get_first_item(['black', 'khaki', 'cyan']) == 'black'


"""
split_string is a function that takes a string and returns a list containing
all of the individual characters as separate elements.

Unfortunately, it looks like the function is currently throwing a TypeError.

Can you work out what needs changing to make the function pass all the tests?
"""


def split_string():
    return list(str)


# Do not change code below this line

def test_it_splits_strings():
    assert split_string('string') == ['s', 't', 'r', 'i', 'n', 'g']
    assert split_string('help') == ['h', 'e', 'l', 'p']
    assert split_string('Northcoders') == [
        'N', 'o', 'r', 't', 'h', 'c', 'o', 'd', 'e', 'r', 's']


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


# Do not change code below this line

def test_adds_favourite_bread():
    person_1 = {'name': 'Joe'}
    person_2 = {'name': 'Paul'}
    assert add_bread(person_1, 'rye') == {'name': 'Joe', 'fave_bread': 'rye'}
    assert add_bread(person_2, 'granary') == {
        'name': 'Paul', 'fave_bread': 'granary'}


"""
`count_the_chars` is a function that takes a list of values and a character.
It should return a number representing 
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
    assert count_the_chars(char_list, '6') == 3


def test_counts_the_occurrences_in_mixed_lists():
    char_list = ['a', 1, 'b', 2, 'c', 3]
    assert count_the_chars(char_list, 'b') == 1
    char_list = ['1', 'a', 2, '2', 'b', 1, 'a', '1', '2', 'c', 3, '2', 2]
    assert count_the_chars(char_list, '2') == 3
    assert count_the_chars(char_list, 1) == 1
    
    
    """
`add_guests_to_party` is a function that takes
a list of `invitee` dictionaries.

It should check whether each of these objects has an
'RSVP' key with a value of 'yes'.

If the invitee has RSVP'd, then we should add them to the `guests` list on the
`party` dictionary in our function,and then return the `guests` list.

Unfortunately, it looks like the function isn't working.

Can you work out what needs changing to make the function pass all the tests?

(An `invitee` might look like this: `{'name': 'Simon', 'RSVP': 'no'}`).
"""


def add_guests_to_party(invitees):
    party = {
        'host': 'Paul Copley Esq',
        'venue': 'The Ritzy Bar',
        'theme': 'Heroes of Code',
        'guests': [
            {
                'name': 'Cat'
            },
            {
                'name': 'Kyle'
            }
        ]
    }
    for invitee in invitees:
        if invitee['RSVP']:
            party.append({'name': invitee['nome']})
    return party


# Do not change code below this line

def test_returns_a_guest_list():
    invitees = []
    assert type(add_guests_to_party(invitees)) is list


def test_returns_guest_list_unchanged_if_no_invitees():
    invitees = []
    expected = [{'name': 'Cat'}, {'name': 'Kyle'}]
    assert add_guests_to_party(invitees) == expected


def test_returns_guest_list_unchanged_if_no_RSVP_yes():
    invitees = [
        {'name': 'Chon', 'RSVP': 'no'},
        {'name': 'Verity', 'RSVP': 'no'}
    ]
    expected = [{'name': 'Cat'}, {'name': 'Kyle'}]
    assert add_guests_to_party(invitees) == expected


def test_returns_new_guests_if_all_RSVP_yes():
    invitees = [
        {'name': 'Liam', 'RSVP': 'yes'},
        {'name': 'Haz', 'RSVP': 'yes'}
    ]
    expected = [
        {'name': 'Cat'},
        {'name': 'Kyle'},
        {'name': 'Liam'},
        {'name': 'Haz'}
    ]
    assert add_guests_to_party(invitees) == expected


def test_returns_new_guests_if_some_RSVP_yes():
    invitees = [
        {'name': 'Sarah', 'RSVP': 'yes'},
        {'name': 'Jim', 'RSVP': 'no'},
        {'name': 'Emily', 'RSVP': 'yes'},
        {'name': 'Dominic', 'RSVP': 'yes'},
    ]
    expected = [
        {'name': 'Cat'},
        {'name': 'Kyle'},
        {'name': 'Sarah'},
        {'name': 'Emily'},
        {'name': 'Dominic'}
    ]
    assert add_guests_to_party(invitees) == expected


