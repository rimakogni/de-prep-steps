# Data Engineering Prep Steps Exercises

## Purpose

These exercises are intended to give you some experience of writing simple Python code.

## Prerequisites

You need to _fork and clone_ this repository. You should already have watched
[this introduction](https://www.youtube.com/watch?v=4VjoJyqQkNQ&ab_channel=Tutor1) to forking and cloning.
When you have cloned the repository to the local machine, then open it with Visual Studio Code
(or the IDE of your choice).

Before you start, you should have the latest version of Python 3 installed. If you have not already
done so, follow the steps described in `Preparing For The Course` in the Prep Steps notes.

To test if Python is installed correctly, type at the terminal command prompt:

```bash
python --version
```

You should see something like:

```
Python 3.11.5
```

(The digits will be different depending on what exact version you installed. As long as the
version number is higher than 3.9.0, everything should be fine.)
If you don't have Python installed then go back to the `Preparing For The Course` section and
repeat the steps there. Failing that, get in touch with us in your prep-steps slack channel.

## Running tests

You will be asked to write some code in the exercise. To test whether you have got it right,
we will run some automated tests using some tests that we've pre-written for you. You will be learning a _lot_ more
about testing in general and also about a tool called `pytest` during the course. For now, please just run the files with python like so:

```bash
python PATH_TO_FILE.py
```

at the command prompt.

## Completing and testing the exercises.

There are two types of exercise included here.

### REPL Exercises

The exercises in Section `variables` are intended to be executed in the Python REPL.

The Python _REPL_ (**R**ead **E**valuate **P**rint **L**oop) is a command line tool for running Python code interactively one instruction at a time.
To start the REPL, just type

```bash
python
```

at the command prompt.

You should see a new Python prompt, like this:

![Python Prompt](./img/python_prompt.png)

Now, you can type Python code instructions, followed by the `Return` key.

The exercises invite you to type in various commands,
predicting what they might do in advance. For example, what might this command do?

```
>>> print('Hello New Northcoder!')
```

To terminate the REPL session, type `exit()` or hit `Ctrl+d`

### Function Exercises

The remaining exercises all require you to write (or rewrite) some Python _functions_. Make sure you have read the Prep Steps
notes on functions first.

To test how you coded these functions we will you the pre-written tests.

For example, the file `demonstration.py` file has a very simple function that is going wrong. You
should be able to test this by typing (at the command prompt):

```bash
python 00_start_your_journey_here/demonstration.py
```

You should see a message saying that one of the tests is passing and one is being skipped. Now, in VS Code, navigate to the `demonstration.py` file.

Change the `@skip_test` on line 35 to `@run_test`.

You should now be able to re-run `python 00_start_your_journey_here/demonstration.py` and see the second test is failing.

Now change the code to add 2 to the counter and re-run the `python` command to see the test passing. Congratulations!

In most cases, you will be asked to write or change functions to illustrate different points about Python code. Please do not change the tests themselves, which are written below the function being tested.

Happy Coding!
