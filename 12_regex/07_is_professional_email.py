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


def is_professional_email(text):
    return not re.search(r'[xX]+$', text)


@run_test
def test_returns_true_if_email_is_professional():
    assert is_professional_email("Dear Sir/Madam"), \
        format_err_msg(True, is_professional_email("Dear Sir/Madam"))
    assert is_professional_email("Dear Alex, How are you?"), \
        format_err_msg(True, is_professional_email("Dear Alex, How are you?"))


@run_test
def test_returns_false_if_email_ends_with_x():
    assert not is_professional_email("x"), \
        format_err_msg(False, is_professional_email("x"))
    assert not is_professional_email("i miss u xx"), \
        format_err_msg(False, is_professional_email("i miss u xx"))
    assert not is_professional_email("X_X"), \
        format_err_msg(False, is_professional_email("X_X"))


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == '__main__':
    test_returns_true_if_email_is_professional()
    test_returns_false_if_email_ends_with_x()
