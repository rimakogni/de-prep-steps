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


def extract_repo_name(text):
    match = re.search(r'github\.com/[^/]+/([^/]+)', text)
    if match:
        return match.group(1)


@run_test
def test_extract_repo_name_returns_repo_name():
    test_url_1 = "https://github.com/northcoders/intro-week"
    test_url_2 = "https://github.com/northcoders/remote-git-workshop"
    test_url_3 = "https://github.com/myAccount/notes"
    test_url_4 = "https://github.com/myAccount/notes/settings"
    assert extract_repo_name(test_url_1) == "intro-week", \
        format_err_msg("intro-week", extract_repo_name(test_url_1))
    assert extract_repo_name(test_url_2) == "remote-git-workshop", \
        format_err_msg("remote-git-workshop", extract_repo_name(test_url_2))
    assert extract_repo_name(test_url_3) == "notes", \
        format_err_msg("notes", extract_repo_name(test_url_3))
    assert extract_repo_name(test_url_4) == "notes", \
        format_err_msg("notes", extract_repo_name(test_url_4))


# DO NOT CHANGE CODE BELOW THIS LINE
if __name__ == '__main__':
    test_extract_repo_name_returns_repo_name()
