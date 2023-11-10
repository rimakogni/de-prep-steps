"""
`add_guests_to_party` is a function that takes
a list of `invitee` dictionaries.

It should check whether each of these objects has an
'RSVP' key with a value of 'yes'.

If the invitee has RSVP'd, then we should add them to the `guests` list on the
`party` dictionary in our function,and then return the `guests` list.

Unfortunately, it looks like the function isn't working.

Can you work out what needs changing to make the function pass all the tests?

(An `invitee` might look like this: `{'name': 'Simon', 'RSVP': 'No'}`).
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
