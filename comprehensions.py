#Task 1:  1 Create Greeting Strings (LIST)
#Task 2: 4 Increment Even Numbers (LIST)
#Task 3: 8 Switch Name and ID (Dict)
#Task 4: 11 Find Average Games (Dict)
#ßTask 5: 12 Get Unique Departments (SET)


# Task 1: Create Greeting Strings

## Instructions
"""
First, we will take a look at **list comprehensions**!

In the file `01_list_exercises.py`, you will find the function `create_greeting_strings`.

The function should accept a list of names and return a list of greetings. It should work in the following way:

```py
create_greeting_strings('Simon') # [ 'Hello Simon!' ]
create_greeting_strings('Cat', 'Danika') # [ 'Hello Cat!', 'Hello Danika!' ]
```

This function is currently working exactly as it should. However, it could be much more concise.

Please refactor `create_greeting_strings` to use a **list comprehension**.

> To run the tests you will need to run the file with `python` like so: `python 01_list_exercises.py`

**The later tests are currently being skipped. Once you have fixed each test, you can move onto the next by changing the `@skip_test` line to be `@run_test` instead**


For example:

```py
@skip_test
def test_nested_lists():
  ...
```

becomes

```py
@run_test
def test_nested_lists():
  ...
```
"""