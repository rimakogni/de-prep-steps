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
    result = add_price_to_product({'type': 'Tofu slices'}, 2.20)
    assert result == {'type': 'Tofu slices', 'price': 2.20}


def test_same_dictionary_is_returned():
    product = {'type': 'Tofu slices'}
    result = add_price_to_product(product, 2.20)
    assert product == {'type': 'Tofu slices', 'price': 2.20}
    assert result is product


def test_product_can_have_many_fields():
    product = {'type': 'Tofu slices', 'flavour': 'chocolate'}
    result = add_price_to_product(product, 2.50)
    assert result == {'type': 'Tofu slices',
                      'flavour': 'chocolate', 'price': 2.50}
