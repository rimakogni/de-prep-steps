"""
Uh-oh! We've got some voters who've registered their addresses incorrectly!
The `voter` dictionary looks like this:

{
  'name': "Alex",
  'age': 39,
  'address': {
    'house_number': 2,
    'street': "Old St",
    'city: "Chester"
  }
}

Let's help them fix those typos by writing a function that will take two
arguments (`voter` and `correct_house_number`) and change the
`voter`'s  `house_number` to be the `correct_house_number`.

** Note - The function should NOT return anything **

voter = {
  'name': "Alex",
  'age': 39,
  'address': {
    'house_number': 2,
    'street': "Old St",
    'city': "Chester"
  }
}

update_voter_address(voter, 50)

print(voter) # will log:
    {
      'name': "Alex",
      'age': 39,
      'address': {
        'house_number': 50,
        'street': "Old St",
        'city': "Chester"
      }
    }
"""


def update_voter_address(voter, correct_house_number):
    # Your code here
    pass


def test_updates_address():
    voter = {
        'name': "Alex",
        'age': 39,
        'address': {
            'house_number': 2,
            'street': "Old St",
            'city': "Chester"
        }
    }
    update_voter_address(voter, 50)
    assert voter['address']['house_number'] == 50


def test_does_not_return_value():
    voter = {
        'name': "Alex",
        'age': 39,
        'address': {
            'house_number': 2,
            'street': "Old St",
            'city': "Chester"
        }
    }
    assert update_voter_address(voter, 50) is None
