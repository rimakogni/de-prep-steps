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


def exclude_words(text):
    return re.sub(r'\b(north|coders)\b', '', text, flags=re.IGNORECASE).replace('  ', ' ').strip()


@run_test
def test_exclude_words_excludes_separate_words_only():
    assert exclude_words(
        "I visited the north pole last year") == "I visited the pole last year", \
        format_err_msg("I visited the pole last year",
                       exclude_words("I visited the north pole last year"))
    assert exclude_words("I study at Northcoders") == "I study at Northcoders", \
        format_err_msg(
            "I study at Northcoders", exclude_words("I study at Northcoders"))
    assert exclude_words(
        "IBM hired a lot of coders lately") == "IBM hired a lot of lately", \
        format_err_msg(
        "IBM hired a lot of lately",
        exclude_words("IBM hired a lot of coders lately"))


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == '__main__':
    test_exclude_words_excludes_separate_words_only()
