#Task 1:  1 Create Greeting Strings (LIST)
#Task 2: 4 Increment Even Numbers (LIST)
#Task 3: 8 Switch Name and ID (Dict)
#Task 4: 11 Find Average Games (Dict)
#ßTask 5: 12 Get Unique Departments (SET)


# Task 1: Create Greeting Strings
from test_api.checks import run_test, skip_test, format_err_msg
## Instructions
"""
###Create Greeting Strings###

First, we will take a look at **list comprehensions**!

The function should accept a list of names and return a list of greetings. It should work in the following way:

```py
create_greeting_strings('Simon') # [ 'Hello Simon!' ]
create_greeting_strings('Cat', 'Danika') # [ 'Hello Cat!', 'Hello Danika!' ]
```

This function is currently working exactly as it should. However, it could be much more concise.

Please refactor `create_greeting_strings` to use a **list comprehension**.

"""

def create_greeting_strings(names):
    greeting = []

    for name in names:
        greeting.append(f"Hello {name}!")

    return greeting


@run_test
def test_create_greeting_strings_return_empty_list():
    assert create_greeting_strings([]) == [], format_err_msg(
        "", create_greeting_strings([])
    )


@skip_test
def test_create_greeting_strings_greets_single_name_in_list():
    assert create_greeting_strings(["Danika"]) == [
        "Hello Danika!"
    ], format_err_msg("Hello Danika!", create_greeting_strings(["Danika"]))


@skip_test
def test_create_greeting_strings_greets_all_names_in_list():
    test_list = ["Paul", "Joe", "Hannah", "Alex", "Harrison", "Simon", "Kyle"]
    expected_result = [
        "Hello Paul!",
        "Hello Joe!",
        "Hello Hannah!",
        "Hello Alex!",
        "Hello Harrison!",
        "Hello Simon!",
        "Hello Kyle!",
    ]
    assert (
        create_greeting_strings(test_list) == expected_result
    ), format_err_msg(expected_result, create_greeting_strings(test_list))

if __name__ == "__main__":
    test_create_greeting_strings_return_empty_list()
    test_create_greeting_strings_greets_single_name_in_list()
    test_create_greeting_strings_greets_all_names_in_list()
