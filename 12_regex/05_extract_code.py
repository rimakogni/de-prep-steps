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


def extract_code(text):
    match = re.search(r'\d+', text)
    if match:
        return int(match.group())


@run_test
def test_extract_code_finds_number_in_single_word_string():
    assert extract_code("abcd67yuio") == 67, \
        format_err_msg(67, extract_code("abcd67yuio"))
    assert extract_code("abcd103yuio") == 103, \
        format_err_msg(67, extract_code("abcd103yuio"))
    assert extract_code("abcd4567yuio") == 4567, \
        format_err_msg(67, extract_code("abcd4567yuio"))
    assert extract_code("abcd1000289yuio") == 1000289, \
        format_err_msg(67, extract_code("abcd1000289yuio"))


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == '__main__':
    test_extract_code_finds_number_in_single_word_string()
