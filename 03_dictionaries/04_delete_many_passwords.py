"""
Write a function that takes an array of user dictionaries (`users`), and
deletes the password key value pair on each user and returns the list.
If a dictionary does not already have a password key then it should be
unchanged.

delete_many_passwords([
    {'name': 'Barry', 'password': 'ilovetea', 'department': 'Tea'},
    {
        'name': 'Sandeep',
        'password': 'ilovecoffee',
        'favourite_drink': 'Coffee'
        },
    {'name': 'Kavita', 'password': 'ilovepie', 'weakness': 'Pie'}
])

Returns
[
    { 'name': 'Barry', 'department': 'Tea'},
    { 'name': 'Sandeep', 'favourite_drink': 'Coffee' },
    { 'name': 'Kavita', 'weakness': 'Pie'}
]
"""


def delete_many_passwords(users):
    # Your code here
    pass


def test_changes_single_dict():
    users = [
        {'name': 'Barry', 'password': 'ilovetea', 'department': 'Tea'}
    ]
    result = delete_many_passwords(users)
    assert result == [
        {'name': 'Barry', 'department': 'Tea'}
    ]


def test_changes_many_users():
    users1 = [
        {'name': 'Barry', 'password': 'ilovetea', 'department': 'Tea'},
        {
            'name': 'Sandeep',
            'password': 'ilovecoffee',
            'favourite_drink': 'Coffee'
        },
        {'name': 'Kavita', 'password': 'ilovepie', 'weakness': 'Pie'}
    ]
    result1 = delete_many_passwords(users1)
    expected = [
        {'name': 'Barry', 'department': 'Tea'},
        {'name': 'Sandeep', 'favourite_drink': 'Coffee'},
        {'name': 'Kavita', 'weakness': 'Pie'}
    ]
    assert result1 == expected
    users2 = [
        {'name': 'Barry', 'password': 'ilovetea', 'department': 'Tea'},
        {
            'name': 'Sandeep',
            'password': 'ilovecoffee',
            'favourite_drink': 'Coffee'
        },
        {'name': 'Kavita', 'weakness': 'Pie'}
    ]
    result2 = delete_many_passwords(users2)
    assert result2 == expected


def test_empty_list_is_returned():
    users = []
    result = delete_many_passwords(users)
    assert result == []


def test_does_not_change_any_object_without_password():
    users = [
        {'name': 'Sandeep', 'favourite_drink': 'Coffee'}
    ]
    result = delete_many_passwords(users)
    assert result == [
        {'name': 'Sandeep', 'favourite_drink': 'Coffee'}
    ]
