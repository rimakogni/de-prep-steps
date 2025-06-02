import os
import sys
import re

sys.path.append(os.getcwd())

from test_api.checks import run_test, skip_test, format_err_msg

# DO NOT CHANGE CODE ABOVE THIS LINE

# This challenge is more advanced.
# Again, please do not change the tests
# For the function, delete the `pass` keyword and write code that makes the
#  tests pass


def sum_nums(text):
    
    numbers = re.findall(r'\d+', text)
    return sum(int(n) for n in numbers)

@run_test
def test_sum_nums_totals_all_numbers_in_string():
    assert sum_nums("hello") == 0, \
        format_err_msg(0, sum_nums("hello"))
    assert sum_nums("1") == 1, \
        format_err_msg(1, sum_nums("1"))
    assert sum_nums("12") == 12, \
        format_err_msg(12, sum_nums("12"))
    assert sum_nums("1hello2") == 3, \
        format_err_msg(3, sum_nums("1hello2"))
    assert sum_nums("12hiya!3") == 15, \
        format_err_msg(15, sum_nums("12hiya!3"))


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == '__main__':
    test_sum_nums_totals_all_numbers_in_string()
