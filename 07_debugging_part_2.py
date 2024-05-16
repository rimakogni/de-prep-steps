from test_api.checks import Check, SkipCheck

"""
### count_occurrences ###

`count_occurrences` is a function that takes a list and a value.
It should return a number representing 
the total number of times that the value appears in the list.

Unfortunately, it looks like the function isn't working.

Can you work out what needs changing to make the function pass all the tests?
"""


def count_occurrences(list_to_check, value):
    count = 0
    for i in range(list_to_check):
        if list_to_check[i] = value:
            count + 1
            return count


# Do not change tests!

Check(count_occurrences, 'returns 0 if no match - empty list').when_called_with([], 'a').returns(0)
Check(count_occurrences, 'returns 0 if no match - non empty list').when_called_with(['a', 'b', 'c'], 'd').returns(0)
Check(count_occurrences, 'counts occurrences in simple list').when_called_with(['a', 'b', 'c'], 'b').returns(1)
Check(count_occurrences, 'counts occurrences in mixed list').when_called_with(['1', 'a', 2, '2', 'b', 1, 'a', '1', '2', 'c', 3, '2', 2], 2).returns(2)


"""
### add_guests_to_party ###

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


# Do not change tests!

Check(add_guests_to_party, 'returns a list').when_called_with([]).is_type(list)
Check(add_guests_to_party, 'returns unchanged guestlist if no invitees').when_called_with([]).returns([{'name': 'Cat'}, {'name': 'Kyle'}])
Check(add_guests_to_party, 'returns unchanged guestlist if NO RSVPs').when_called_with([{'name': 'Chon', 'RSVP': 'no'}, {'name': 'Verity', 'RSVP': 'no'}]).returns([{'name': 'Cat'}, {'name': 'Kyle'}])
Check(add_guests_to_party, 'returns new guests if ALL RSVP yes')\
    .when_called_with([{'name': 'Liam', 'RSVP': 'yes'}, {'name': 'Haz', 'RSVP': 'yes'}])\
    .returns([{'name': 'Cat'}, {'name': 'Kyle'}, {'name': 'Liam'}, {'name': 'Haz'}])
Check(add_guests_to_party, 'returns new guests if SOME RSVP yes')\
    .when_called_with([
        {'name': 'Sarah', 'RSVP': 'yes'},
        {'name': 'Jim', 'RSVP': 'no'},
        {'name': 'Emily', 'RSVP': 'yes'},
        {'name': 'Dominic', 'RSVP': 'yes'},
    ])\
    .returns([
        {'name': 'Cat'},
        {'name': 'Kyle'},
        {'name': 'Sarah'},
        {'name': 'Emily'},
        {'name': 'Dominic'}
    ])
