"""
Write a function that takes a list of booleans (`bools`) and returns a `list` with all of their values swapped 
such that `True` becomes `False` and `False` becomes `True`.


flip_booleans([True, True, True]) # returns [False, False, False]

flip_booleans([False, False, False]) # returns [True, True, True]

flip_booleans([True, False, False, True]) # returns [False, True, True, False]

flip_booleans([]) # returns []

"""

def flip_booleans(bools):
    # Your code here
    pass


def test_empty_list_returns_empty_list():
    assert flip_booleans([]) == []


def test_single_true_returns_single_false():
    assert flip_booleans([True]) ==[False]


def test_single_false_returns_single_true():
    assert flip_booleans([False]) == [True]


def test_all_falses_returns_all_true():
    assert flip_booleans([False, False, False]) == [True, True, True]


def test_all_trues_returns_all_falses():
    assert flip_booleans([True, True, True]) == [False, False, False]


def test_mixed_trues_and_falses_flipped_correctly():
    assert flip_booleans([True, False, False, True]) == [False, True, True, False]