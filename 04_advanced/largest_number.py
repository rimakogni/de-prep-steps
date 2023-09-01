"""
Write a function that takes a `number` and returns the largest number that can be made by rearranging the digits.

largest_number(3) # returns 3

largest_number(123) # returns 321

largest_number(937846) # returns 987643

largest_number(43) # returns 43

"""

def largest_number(number):
    pass


def test_single_digit():
    assert largest_number(3) == 3
    assert largest_number(9) == 9


def test_double_digits_correct_order():
    assert largest_number(43) == 43


def test_double_digits_incorrect_order():
    assert largest_number(34) == 43


def test_double_digits_repeated():
    assert largest_number(44) == 44


def test_triple_digits_correct_order():
    assert largest_number(321) == 321


def test_triple_digits_incorrect_order():
    assert largest_number(213) == 321


def test_triple_digits_two_repeated():
    assert largest_number(233) == 332


def test_lots_of_digits():
    assert largest_number(937846) == 987643
    assert largest_number(8456329456) == 9866554432