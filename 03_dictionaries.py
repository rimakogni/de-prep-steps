"""
Write a function that takes a dictionary (`product`) that looks like this:
`{ 'type': 'Tofu slices' }`,
and a number (`price`). Add a price property to this dictionary and set its
value to the `price`.
Then, return the dictionary.

e.g.

add_price_to_product({ 'type': 'Tofu slices' }, 2.20) # returns
{ 'type': 'Tofu slices', 'price': 2.20 }
"""


def add_price_to_product(product, price):
    # Your code here
    pass


def test_empty_product_produces_no_output():
    result = add_price_to_product({}, 2.20)
    assert result == {}


def test_single_product_has_price_added():
    result = add_price_to_product({"type": "Tofu slices"}, 2.20)
    assert result == {"type": "Tofu slices", "price": 2.20}


def test_same_dictionary_is_returned():
    product = {"type": "Tofu slices"}
    result = add_price_to_product(product, 2.20)
    assert product == {"type": "Tofu slices", "price": 2.20}
    assert result is product


def test_product_can_have_many_fields():
    product = {"type": "Tofu slices", "flavour": "chocolate"}
    result = add_price_to_product(product, 2.50)
    assert result == {
        "type": "Tofu slices",
        "flavour": "chocolate",
        "price": 2.50,
    }


"""
Write a function that takes three arguments:

 - a dictionary (`product`) that looks like this: `{'type': 'Terminator 2:
 Judgement Day', 'price': '£6.99', 'quantity': 1 }`
 - a `property` to add
 - a `value` corresponding to the property

It should then update the `product` to include this new property and return
the updated `product`.

add_property_to_product(
    {'type': 'Terminator 2: Judgement Day', 'price': '£6.99', 'quantity': 1 },
    'length', '2h 36m'
    )
#returns {
    # 'type': 'Terminator 2: Judgement Day',
    # 'price': '£6.99',
    # 'quantity': 1,
    # 'length': '2h 36m'
    # }
"""


def add_property_to_product(product, property, value):
    # Your code here
    pass


def test_empty_product_gains_single_property():
    result = add_property_to_product({}, "length", "2h 36m")
    assert result == {"length": "2h 36m"}


def test_string_property_added_to_product():
    product = {
        "type": "Terminator 2: Judgement Day",
        "price": "£6.99",
        "quantity": 1,
    }
    result = add_property_to_product(product, "length", "2h 36m")
    assert result == {
        "type": "Terminator 2: Judgement Day",
        "price": "£6.99",
        "quantity": 1,
        "length": "2h 36m",
    }


def test_integer_property_added_to_product():
    product = {
        "type": "Terminator 2: Judgement Day",
        "price": "£6.99",
        "quantity": 1,
    }
    result = add_property_to_product(product, 36, 42)
    assert result == {
        "type": "Terminator 2: Judgement Day",
        "price": "£6.99",
        "quantity": 1,
        36: 42,
    }


def test_float_property_added_to_product():
    product = {
        "type": "Terminator 2: Judgement Day",
        "price": "£6.99",
        "quantity": 1,
    }
    result = add_property_to_product(product, 36.1, "dave")
    assert result == {
        "type": "Terminator 2: Judgement Day",
        "price": "£6.99",
        "quantity": 1,
        36.1: "dave",
    }


def test_boolean_property_added_to_product():
    product = {
        "type": "Terminator 2: Judgement Day",
        "price": "£6.99",
        "quantity": 1,
    }
    result = add_property_to_product(product, True, False)
    assert result == {
        "type": "Terminator 2: Judgement Day",
        "price": "£6.99",
        "quantity": 1,
        True: False,
    }


def test_list_property_not_added_to_product():
    product = {
        "type": "Terminator 2: Judgement Day",
        "price": "£6.99",
        "quantity": 1,
    }
    result = add_property_to_product(product, [1, 2, 3], "a")
    assert result == {
        "type": "Terminator 2: Judgement Day",
        "price": "£6.99",
        "quantity": 1,
    }


def test_dictionary_property_not_added_to_product():
    product = {
        "type": "Terminator 2: Judgement Day",
        "price": "£6.99",
        "quantity": 1,
    }
    result = add_property_to_product(product, {"a": "b"}, "a")
    assert result == {
        "type": "Terminator 2: Judgement Day",
        "price": "£6.99",
        "quantity": 1,
    }


def test_same_dictionary_returned():
    product = {
        "type": "Terminator 2: Judgement Day",
        "price": "£6.99",
        "quantity": 1,
    }
    result = add_property_to_product(product, "length", "2h 36m")
    assert result is product
    assert product["length"] == "2h 36m"


"""
Write a function that takes a string (name) and a number (year_of_birth) and
returns an object with:

 - a name property set to the value of the name parameter
 - an age property set to whatever the age of the northcoder would be in the
 year 2023
 - a language property set to 'Python'

If the year is after 2023, show 'error' for the age.

create_northcoder('Joe', 2002)

returns
{
  'name': 'Joe',
  'age': 21,
  'language': 'Python'
}
"""


def create_northcoder(name, year_of_birth):
    # Your code here
    pass


def test_creates_northcoder_with_correct_age():
    result = create_northcoder("Joe", 2002)
    expected = {"name": "Joe", "age": 21, "language": "Python"}
    assert result == expected


def test_2023_baby_is_0_years_old():
    result = create_northcoder("Paul", 2023)
    expected = {"name": "Paul", "age": 0, "language": "Python"}
    assert result == expected


def test_2123_baby_shows_age_error():
    result = create_northcoder("Zarkon", 2123)
    expected = {"name": "Zarkon", "age": "error", "language": "Python"}
    assert result == expected


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
    users = [{"name": "Barry", "password": "ilovetea", "department": "Tea"}]
    result = delete_many_passwords(users)
    assert result == [{"name": "Barry", "department": "Tea"}]


def test_changes_many_users():
    users1 = [
        {"name": "Barry", "password": "ilovetea", "department": "Tea"},
        {
            "name": "Sandeep",
            "password": "ilovecoffee",
            "favourite_drink": "Coffee",
        },
        {"name": "Kavita", "password": "ilovepie", "weakness": "Pie"},
    ]
    result1 = delete_many_passwords(users1)
    expected = [
        {"name": "Barry", "department": "Tea"},
        {"name": "Sandeep", "favourite_drink": "Coffee"},
        {"name": "Kavita", "weakness": "Pie"},
    ]
    assert result1 == expected
    users2 = [
        {"name": "Barry", "password": "ilovetea", "department": "Tea"},
        {
            "name": "Sandeep",
            "password": "ilovecoffee",
            "favourite_drink": "Coffee",
        },
        {"name": "Kavita", "weakness": "Pie"},
    ]
    result2 = delete_many_passwords(users2)
    assert result2 == expected


def test_empty_list_is_returned():
    users = []
    result = delete_many_passwords(users)
    assert result == []


def test_does_not_change_any_object_without_password():
    users = [{"name": "Sandeep", "favourite_drink": "Coffee"}]
    result = delete_many_passwords(users)
    assert result == [{"name": "Sandeep", "favourite_drink": "Coffee"}]


"""
Write a function that takes a list of dictionaries with the format from
create_northcoder (`northcoders`), and returns a new list of the users' names
as strings.
Any northcoders who are missing names should be omitted from the returned list.

northcoders = [
  {
    'name': 'Callum',
    'age': 31,
    'language': 'JavaScript'
  },
  {
    'name': 'Carrie',
    'age': 32,
    'language': 'Python'
  }
]

get_northcoders_names(northcoders) # returns ['Callum', 'Carrie']
"""


def get_northcoders_names(northcoders):
    # Your code here
    pass


def test_returns_empty_list_if_input_empty():
    assert get_northcoders_names([]) == []


def test_gets_names_of_northcoders():
    northcoders = [
        {"name": "Callum", "age": 31, "language": "JavaScript"},
        {"name": "Carrie", "age": 32, "language": "Python"},
    ]
    assert get_northcoders_names(northcoders) == ["Callum", "Carrie"]


def test_northcoders_missing_names_omitted():
    northcoders = [{"age": 32, "language": "Python"}]
    assert get_northcoders_names(northcoders) == []


"""
Write a function that takes a `user` dictionary that looks like this:

{
  'name': "Tom",
  'age': 26,
  'pet': {
    'name': "Barney",
    'age': 6,
    'type': "good boy"
  }
}

The dictionary is nested; there are dictionaries paired to keys on the user
dictionary.

The function should access the age property in the nested pet dictionary
and return the value.
If the user doesn't have an age for their pet the function should return None.

user = {
  'name': "Carrie",
  'age': 26,
  'pet': {
    'name': "Pixie",
    'age': 4,
    'type': "gremlin"
  }
}

get_user_pet_age(user) # returns 4
"""


def get_user_pet_age(user):
    # Your code here
    pass


def test_gets_pet_age():
    user = {
        "name": "Carrie",
        "age": 26,
        "pet": {"name": "Pixie", "age": 4, "type": "gremlin"},
    }
    assert get_user_pet_age(user) == 4


def test_returns_none_if_no_pet():
    user = {"name": "Carrie", "age": 26}
    assert get_user_pet_age(user) is None


def test_returns_none_if_no_pet_age():
    user = {
        "name": "Carrie",
        "age": 26,
        "pet": {"name": "Pixie", "type": "gremlin"},
    }
    assert get_user_pet_age(user) is None


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
        "name": "Alex",
        "age": 39,
        "address": {"house_number": 2, "street": "Old St", "city": "Chester"},
    }
    update_voter_address(voter, 50)
    assert voter["address"]["house_number"] == 50


def test_does_not_return_value():
    voter = {
        "name": "Alex",
        "age": 39,
        "address": {"house_number": 2, "street": "Old St", "city": "Chester"},
    }
    assert update_voter_address(voter, 50) is None
