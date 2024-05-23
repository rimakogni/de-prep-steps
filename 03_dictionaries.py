from test_api.checks import Check, SkipCheck

"""
### add_price_to_product ###

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


Check(
    add_price_to_product, "returns empty dictionary when there is no product"
).when_called_with({}, 2.20).returns({})

Check(
    add_price_to_product, "adds price to single product in dictionary"
).when_called_with({"type": "Tofu slices"}, 2.20).returns(
    {"type": "Tofu slices", "price": 2.20}
)

Check(
    add_price_to_product, "adds price to single product with multiple fields"
).when_called_with(
    {"type": "Tofu slices", "flavour": "chocolate"}, 2.50
).returns(
    {"type": "Tofu slices", "flavour": "chocolate", "price": 2.50}
)

product = {"type": "Tofu slices"}
Check(
    add_price_to_product, "should return the *original* product dictionary"
).when_called_with(product, 2.20).is_same_as(product)


"""
### add_property_to_product ###

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

NOTE: Only certain types of data are able to be set a dictionary key. Your
function should take this into consideration and only allow the following data
types to be set as a key:
- string
- integer
- float
- boolean

If the given `property` argument is not one of these types then it should be
ignored and the product returned unchanged!
"""


def add_property_to_product(product, property, value):
    # Your code here
    pass


# ❗ Remember to change SkipCheck to Check!
SkipCheck(
    add_property_to_product, "empty product gains a single property"
).when_called_with({}, "length", "2h 36m").returns({"length": "2h 36m"})

SkipCheck(
    add_property_to_product, "string property added to product"
).when_called_with(
    {"type": "Terminator 2: Judgement Day", "price": "£6.99", "quantity": 1},
    "length",
    "2h 36m",
).returns(
    {
        "type": "Terminator 2: Judgement Day",
        "price": "£6.99",
        "quantity": 1,
        "length": "2h 36m",
    }
)

SkipCheck(
    add_property_to_product, "integer property added to product"
).when_called_with(
    {"type": "Terminator 2: Judgement Day", "price": "£6.99", "quantity": 1},
    36,
    42,
).returns(
    {
        "type": "Terminator 2: Judgement Day",
        "price": "£6.99",
        "quantity": 1,
        36: 42,
    }
)

SkipCheck(
    add_property_to_product, "float property added to product"
).when_called_with(
    {"type": "Terminator 2: Judgement Day", "price": "£6.99", "quantity": 1},
    36.1,
    "dave",
).returns(
    {
        "type": "Terminator 2: Judgement Day",
        "price": "£6.99",
        "quantity": 1,
        36.1: "dave",
    }
)

SkipCheck(
    add_property_to_product, "boolean property added to product"
).when_called_with(
    {"type": "Terminator 2: Judgement Day", "price": "£6.99", "quantity": 1},
    True,
    False,
).returns(
    {
        "type": "Terminator 2: Judgement Day",
        "price": "£6.99",
        "quantity": 1,
        True: False,
    }
)

SkipCheck(
    add_property_to_product, "list property NOT added to product"
).when_called_with(
    {"type": "Terminator 2: Judgement Day", "price": "£6.99", "quantity": 1},
    [1, 2, 3],
    "a",
).returns(
    {"type": "Terminator 2: Judgement Day", "price": "£6.99", "quantity": 1}
)

SkipCheck(
    add_property_to_product, "dictionary property NOT added to product"
).when_called_with(
    {"type": "Terminator 2: Judgement Day", "price": "£6.99", "quantity": 1},
    {"a": "b"},
    "a",
).returns(
    {"type": "Terminator 2: Judgement Day", "price": "£6.99", "quantity": 1}
)

product = {
    "type": "Terminator 2: Judgement Day",
    "price": "£6.99",
    "quantity": 1,
}

SkipCheck(
    add_property_to_product, "should return the *original* product dictionary"
).when_called_with(product, "length", "2h 36m").is_same_as(product)


"""
### create_northcoder ###

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


SkipCheck(
    create_northcoder, "creates northcoder with correct age"
).when_called_with("Joe", 2002).returns(
    {"name": "Joe", "age": 21, "language": "Python"}
)

SkipCheck(create_northcoder, "2023 baby is 0 years old").when_called_with(
    "Paul", 2023
).returns({"name": "Paul", "age": 0, "language": "Python"})

SkipCheck(create_northcoder, "2123 baby is shows age error").when_called_with(
    "Zarkon", 2123
).returns({"name": "Zarkon", "age": "error", "language": "Python"})


"""
### delete_many_passwords ###

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


SkipCheck(delete_many_passwords, "changes single password").when_called_with(
    [{"name": "Barry", "password": "ilovetea", "department": "Tea"}]
).returns([{"name": "Barry", "department": "Tea"}])

SkipCheck(
    delete_many_passwords, "does not change user without password"
).when_called_with([{"name": "Sandeep", "favourite_drink": "Coffee"}]).returns(
    [{"name": "Sandeep", "favourite_drink": "Coffee"}]
)

SkipCheck(delete_many_passwords, "changes many users").when_called_with(
    [
        {"name": "Barry", "password": "ilovetea", "department": "Tea"},
        {
            "name": "Sandeep",
            "password": "ilovecoffee",
            "favourite_drink": "Coffee",
        },
        {"name": "Kavita", "password": "ilovepie", "weakness": "Pie"},
    ]
).returns(
    [
        {"name": "Barry", "department": "Tea"},
        {"name": "Sandeep", "favourite_drink": "Coffee"},
        {"name": "Kavita", "weakness": "Pie"},
    ]
)

SkipCheck(
    delete_many_passwords, "changes many users when some do not have passwords"
).when_called_with(
    [
        {"name": "Barry", "password": "ilovetea", "department": "Tea"},
        {
            "name": "Sandeep",
            "password": "ilovecoffee",
            "favourite_drink": "Coffee",
        },
        {"name": "Kavita", "weakness": "Pie"},
    ]
).returns(
    [
        {"name": "Barry", "department": "Tea"},
        {"name": "Sandeep", "favourite_drink": "Coffee"},
        {"name": "Kavita", "weakness": "Pie"},
    ]
)

SkipCheck(
    delete_many_passwords, "returns empty list when no users present"
).when_called_with([]).returns([])


"""
### get_northcoders_names ###

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


SkipCheck(
    get_northcoders_names, "returns empty list if input is empty"
).when_called_with([]).returns([])

SkipCheck(get_northcoders_names, "gets names of northcoders").when_called_with(
    [
        {"name": "Callum", "age": 31, "language": "JavaScript"},
        {"name": "Carrie", "age": 32, "language": "Python"},
    ]
).returns(["Callum", "Carrie"])

SkipCheck(
    get_northcoders_names, "returns empty list if name is omitted"
).when_called_with([{"age": 32, "language": "Python"}]).returns([])


"""
### get_user_pet_age ###

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


SkipCheck(get_user_pet_age, "returns pet age").when_called_with(
    {
        "name": "Carrie",
        "age": 26,
        "pet": {"name": "Pixie", "age": 4, "type": "gremlin"},
    }
).returns(4)

SkipCheck(get_user_pet_age, "returns none if no pet").when_called_with(
    {"name": "Carrie", "age": 26}
).returns(None)

SkipCheck(get_user_pet_age, "returns none if no pet age").when_called_with(
    {"name": "Carrie", "age": 26, "pet": {"name": "Pixie", "type": "gremlin"}}
).returns(None)
