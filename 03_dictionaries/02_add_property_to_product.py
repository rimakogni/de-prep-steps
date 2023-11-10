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
    result = add_property_to_product({}, 'length', '2h 36m')
    assert result == {'length': '2h 36m'}


def test_string_property_added_to_product():
    product = {'type': 'Terminator 2: Judgement Day',
               'price': '£6.99', 'quantity': 1}
    result = add_property_to_product(product, 'length', '2h 36m')
    assert result == {'type': 'Terminator 2: Judgement Day',
                      'price': '£6.99', 'quantity': 1, 'length': '2h 36m'}


def test_integer_property_added_to_product():
    product = {'type': 'Terminator 2: Judgement Day',
               'price': '£6.99', 'quantity': 1}
    result = add_property_to_product(product, 36, 42)
    assert result == {'type': 'Terminator 2: Judgement Day',
                      'price': '£6.99', 'quantity': 1, 36: 42}


def test_float_property_added_to_product():
    product = {'type': 'Terminator 2: Judgement Day',
               'price': '£6.99', 'quantity': 1}
    result = add_property_to_product(product, 36.1, 'dave')
    assert result == {'type': 'Terminator 2: Judgement Day',
                      'price': '£6.99', 'quantity': 1, 36.1: 'dave'}


def test_boolean_property_added_to_product():
    product = {'type': 'Terminator 2: Judgement Day',
               'price': '£6.99', 'quantity': 1}
    result = add_property_to_product(product, True, False)
    assert result == {'type': 'Terminator 2: Judgement Day',
                      'price': '£6.99', 'quantity': 1, True: False}


def test_list_property_not_added_to_product():
    product = {'type': 'Terminator 2: Judgement Day',
               'price': '£6.99', 'quantity': 1}
    result = add_property_to_product(product, [1, 2, 3], 'a')
    assert result == {'type': 'Terminator 2: Judgement Day',
                      'price': '£6.99', 'quantity': 1}


def test_dictionary_property_not_added_to_product():
    product = {'type': 'Terminator 2: Judgement Day',
               'price': '£6.99', 'quantity': 1}
    result = add_property_to_product(product, {'a': 'b'}, 'a')
    assert result == {'type': 'Terminator 2: Judgement Day',
                      'price': '£6.99', 'quantity': 1}


def test_same_dictionary_returned():
    product = {'type': 'Terminator 2: Judgement Day',
               'price': '£6.99', 'quantity': 1}
    result = add_property_to_product(product, 'length', '2h 36m')
    assert result is product
    assert product['length'] == '2h 36m'
