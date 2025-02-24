#Task 1:  1 Create Greeting Strings (LIST) ✅
#Task 2: 4 Increment Even Numbers (LIST)✅
#Task 3: 8 Switch Name and ID (Dict)✅
#Task 4: 11 Find Average Games (Dict)
#ßTask 5: 12 Get Unique Departments (SET)

from test_api.checks import run_test, skip_test, format_err_msg

"""
### create_greeting_strings ###

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


"""
### increment_even_numbers ###

This function should accept a list of numbers. It should increment **only** the even numbers and return the list with those changes:

```py
increment_even_numbers([ 2, 4, 6 ]) # [ 3, 5, 7 ]
increment_even_numbers([ 1, 3, 5 ]) # [ 1, 3, 5 ]
increment_even_numbers([ 1, 2, 3, 4, 5 ]) # [ 1, 3, 3, 5, 5 ]
```
There is no existing code for you to refactor, instead you should solve `increment_even_numbers` using a **list comprehension**.

"""

def increment_even_numbers(number_list):
    pass


@skip_test
def test_increment_even_numbers_return_empty_list():
    assert increment_even_numbers([]) == [], format_err_msg(
        [], increment_even_numbers([])
    )


@skip_test
def test_increment_even_numbers_increments_even_numbers():
    assert increment_even_numbers([2, 4, 6]) == [3, 5, 7], format_err_msg(
        [3, 5, 7], increment_even_numbers([2, 4, 6])
    )


@skip_test
def test_increment_even_numbers_ignores_odd_numbers():
    assert increment_even_numbers([1, 3, 5]) == [1, 3, 5], format_err_msg(
        [1, 3, 5], increment_even_numbers([1, 3, 5])
    )


@skip_test
def test_increment_even_numbers_mixed_even_and_odd():
    assert increment_even_numbers([1, 2, 3, 4, 5]) == [
        1,
        3,
        3,
        5,
        5,
    ], format_err_msg([1, 3, 3, 5, 5], increment_even_numbers([1, 2, 3, 4, 5]))

"""
### switch_name_and_id ###
The function should accept a dictionary. In this dictionary, each key is a staff member's name and the value will be their ID number. The function should return a dictionary with the keys and values switched around. It should work in the following way:

```py
switch_name_and_id({"Alex": "a7d29w"}) # {"a7d29w": "Alex"}
switch_name_and_id({"Kyle": "a7d29w", "Danika": "z2r51e", "Liam": "p3f44m"}) 

# {"a7d29w": "Kyle", "z2r51e": "Danika", "p3f44m": "Liam"}
```

This function is currently working exactly as it should, but it could be much more concise.

Please refactor `switch_name_and_id` to use a **dictionary comprehension**.

"""

def switch_name_and_id(data):
    switched_data = {}

    for record in data.items():
        switched_data[record[1]] = record[0]

    return switched_data


@skip_test
def test_switch_name_and_id_passed_empty_dict_returns_empty_dict_():
    assert switch_name_and_id({}) == {}, format_err_msg(
        {}, switch_name_and_id({})
    )


@skip_test
def test_switch_name_and_id_returns_dict_with_single_swapped_key_and_value():
    assert switch_name_and_id({"Alex": "a7d29w"}) == {
        "a7d29w": "Alex"
    }, format_err_msg(
        {"a7d29w": "Alex"}, switch_name_and_id({"Alex": "a7d29w"})
    )
    assert switch_name_and_id({"Chon": "z2r51e"}) == {
        "z2r51e": "Chon"
    }, format_err_msg(
        {"z2r51e": "Chon"}, switch_name_and_id({"Chon": "z2r51e"})
    )
    assert switch_name_and_id({"Cat": "p3f44m"}) == {
        "p3f44m": "Cat"
    }, format_err_msg({"p3f44m": "Cat"}, switch_name_and_id({"Cat": "p3f44m"}))


@skip_test
def test_switch_name_and_id_returns_dict_with_swapped_keys_and_values():
    assert switch_name_and_id({"Alex": "a7d29w", "Chon": "z2r51e"}) == {
        "a7d29w": "Alex",
        "z2r51e": "Chon",
    }, format_err_msg(
        {"a7d29w": "Alex", "z2r51e": "Chon"},
        switch_name_and_id({"Alex": "a7d29w", "Chon": "z2r51e"}),
    )
    assert switch_name_and_id(
        {"Simon": "a7d29w", "Joe": "z2r51e", "Paul": "p3f44m"}
    ) == {
        "a7d29w": "Simon",
        "z2r51e": "Joe",
        "p3f44m": "Paul",
    }, format_err_msg(
        {"a7d29w": "Simon", "z2r51e": "Joe", "p3f44m": "Paul"},
        switch_name_and_id(
            {"Simon": "a7d29w", "Joe": "z2r51e", "Paul": "p3f44m"}
        ),
    )
    assert switch_name_and_id(
        {
            "Kyle": "a7d29w",
            "Danika": "z2r51e",
            "Liam": "p3f44m",
            "Cat": "q4r55t",
        }
    ) == {
        "a7d29w": "Kyle",
        "z2r51e": "Danika",
        "p3f44m": "Liam",
        "q4r55t": "Cat",
    }, format_err_msg(
        {
            "a7d29w": "Kyle",
            "z2r51e": "Danika",
            "p3f44m": "Liam",
            "q4r55t": "Cat",
        },
        switch_name_and_id(
            {
                "Kyle": "a7d29w",
                "Danika": "z2r51e",
                "Liam": "p3f44m",
                "Cat": "q4r55t",
            }
        ),
    )

if __name__ == "__main__":
    test_create_greeting_strings_return_empty_list()
    test_create_greeting_strings_greets_single_name_in_list()
    test_create_greeting_strings_greets_all_names_in_list()
    test_increment_even_numbers_return_empty_list()
    test_increment_even_numbers_increments_even_numbers()
    test_increment_even_numbers_ignores_odd_numbers()
    test_increment_even_numbers_mixed_even_and_odd()
    test_switch_name_and_id_passed_empty_dict_returns_empty_dict_()
    test_switch_name_and_id_returns_dict_with_single_swapped_key_and_value()
    test_switch_name_and_id_returns_dict_with_swapped_keys_and_values()
