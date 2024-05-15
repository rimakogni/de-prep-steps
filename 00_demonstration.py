from test_api.checks import Check, SkipCheck

"""
This is a demonstration problem to help you learn how to use the pre-made
tests.

The (not very useful) function `count_to_two` should count to two, but is
going wrong. To see the first test pass, from the command line, type:

python 00_demonstration.py

The second test is currently being skipped, to run this test you should change
`SkipCheck` to `Check` and run the same `python` command. This test should
fail until the code is fixed.

To fix the code, you should add 2 to the counter rather than 1.

Then run using the same `python` command in the terminal and you should see
all the tests pass.
"""


def count_to_two():
    counter = 0
    counter += 1  # <- change this!!
    return counter


Check(count_to_two, 'returns integer').is_type(int)
SkipCheck(count_to_two, 'returns 2').returns(2)  # Switch SkipCheck to Check
