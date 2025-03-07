# 02_section

## Part 1

You'll now be working on the `challenge.py` files in `02_section/01_challenges`.

For these tasks, you will need to import functions and variables from different parts of the `de-prep-steps` repository.

To do these you will need to make changes to your Python Path to make certain files and directories discoverable. This should be done by appending the appropriate file path to the in-built `sys.path` variable.

1. You will need to change the `sys.path` variable in the `01_challenges.py` file to enable it to successfully import the `print_greeting` function from `examples/file_5.py`.

2. You will need to change the `sys.path` variable in the `02_challenges.py` file. This file will need to import the `add` function from `examples/file_5.py` as well as the two numbers from `01_section/04_challenge/data/nested_data/example_numbers.py`.

## Part 2

For this part you'll **still** be working on the `challenge.py` files in `02_section/01_challenges`.

Please delete the lines that edit the `sys.path` variable, and instead set the `PYTHONPATH` environment variable and run the files with `python`.

## Part 3

You'll now be working on the `challenge.py` files in `02_section/02_challenges`.

For these tasks you will need to import from the [Python standard library](https://docs.python.org/3/library/index.html).

These libraries that are readily available to you. You will not need to install anything.

1. Run the `01_challenge.py` file, you will see that it is currently broken. You will need to write an import to allow the `math.prod` method to work as expected.

2. The `02_challenge.py` file is also broken! It is your job to write the imports that allow it to work. Run the file with `python` to find out what is currently missing from the imports.

## Part 4

You'll now be working on the `challenge.py` files in `02_section/03_challenges`.

For these tasks you will need to import from the external libraries.

These are libraries that are not included with Python, and you will need to install them in your venv.

1. `01_challenge.py` needs access to the [Faker](https://faker.readthedocs.io/en/master/) library.
2. `02_challenge.py` needs access to the [Requests](https://pypi.org/project/requests/) library.
3. `03_challenge.py` needs access to the [MatPlotLib](https://matplotlib.org/stable/) library.
