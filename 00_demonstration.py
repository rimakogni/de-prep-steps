"""
This is a demonstration problem to help you learn how to use `pytest`.

The (not very useful) function `count_to_two` should count to two, but is
going wrong. To see it
fail its tests, from the command line, type:

pytest -vvv 00_demonstration/counter.py

Then fix the code by changing the 1 on line 17 to 2.

Then run pytest using the same command and you should see all the tests pass.

"""


def count_to_two():
    counter = 0
    counter += 1  # <- change this!!
    return counter


# Do not change code below this line


def test_returns_an_integer():
    assert type(count_to_two()) is int


def test_counts_to_two():
    assert count_to_two() == 2
