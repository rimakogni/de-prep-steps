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


def is_valid_sort_code(text):
   return bool(re.fullmatch(r'\d{2}-\d{2}-\d{2}', text))


@run_test
def test_is_valid_sort_code_returns_true_if_sort_code_in_the_correct_format():
    assert is_valid_sort_code("10-34-67"), \
        format_err_msg(True, is_valid_sort_code("10-34-67"))
    assert is_valid_sort_code("51-34-58"), \
        format_err_msg(True, is_valid_sort_code("51-34-58"))
    assert is_valid_sort_code("85-16-23"), \
        format_err_msg(True, is_valid_sort_code("85-16-23"))


@run_test
def test_is_valid_sort_code_returns_false_if_sort_code_NOT_in_the_correct_format():
    assert not is_valid_sort_code("51-349-67"), \
        format_err_msg(False, is_valid_sort_code("51-349-67"))
    assert not is_valid_sort_code("7980-34-67"), \
        format_err_msg(False, is_valid_sort_code("7980-34-67"))
    assert not is_valid_sort_code("34-12-899"), \
        format_err_msg(False, is_valid_sort_code("34-12-899"))
    assert not is_valid_sort_code("a8-78-10"), \
        format_err_msg(False, is_valid_sort_code("a8-78-10"))
    assert not is_valid_sort_code("45_78_10"), \
        format_err_msg(False, is_valid_sort_code("45_78_10"))


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == '__main__':
    test_is_valid_sort_code_returns_true_if_sort_code_in_the_correct_format()
    test_is_valid_sort_code_returns_false_if_sort_code_NOT_in_the_correct_format()
