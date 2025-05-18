# Numbers

Type the following variables into the REPL.

```python
a = 12
b = 5
c = 0.6
d = 17.1
```

You can start the REPL by typing `python` at the command line prompt. Then type the input at the Python prompt, like this:

<img src="img/repl.png" alt="" width=609 height=120 title="Python REPL"></img>

Read through the following expressions and predict the _value_ and _data type_ of each one - e.g. is it a string, an integer, a float?

Justify your prediction and then use Python to check if you were correct. You can use the `type` command to help: eg:

```python
type(a * b)
```

Make sure you understand why you got the results you did and investigate any that surprised you. You can use the [Python documentation](https://docs.python.org/3/).
[Speedsheet](https://speedsheet.io/s/python) for Python is also useful for quick reference.

A:

```python
a * b int
```

B:

```python
b * c float
```

C:

```python
b + c float
```

D:

```python
d - a float
```

E:

```python
a % b int 
```

F:

```python
a % 5.0 float
```

G:

```python
b**2 int
```

H:

```python
a + b int
```

I:

```python
b / a float
```

J:

```python
a // b int
```

K:

```python
len('northcoders') + b int
```

# Strings

In the Python REPL, create the following string variables:

```bash
>>> tutor = 'david john bartlett'

>>> title = 'Mr'

>>> job_title = "Senior Tutor"

```

You can see what _methods_ are available for strings in the [documentation](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
but you might find it easier to check out [SpeedSheet](https://speedsheet.io/s/python?q=strings-only#T7xJ). Use _string methods_ to create:

A. A new variable called `shouty_name` with value `DAVID JOHN BARTLETT`
 shouty_name = tutor.upper() 
B. A new variable called `low_key_title` with value `mr`
low_key_title=title.lower()
C. A new variable called `low_key_job_title` with value `senior tutor`
low_key_job_title=job_title.lower()
D. A new variable called `low_key_full_honours` with value `mr david john bartlett senior tutor`
low_key_full_honours= f'{low_key_title} {tutor} {low_key_job_title}'

For getting _parts_ of strings, check out [substrings and slicing](https://speedsheet.io/s/python?q=strings-only#nXRd)

Then try to create:

E: A new variable called `first_name` with value `david`
first_name = tutor.split()[0]
F: A new variable called `surname` with value `bartlett`
surname = tutor.split()[2]
G: A new variable called `middle_name` with value `john`
middle_name = tutor.split()[1]
H: A new variable called `full_honours` with value `Mr David John Bartlett, Senior Tutor`. (Note the comma!)
full_honours = f'{title} {tutor.title()}, {job_title}'
Note: it's easy to create brand new variables by just typing them in. For example:

```python
shouty_name = 'DAVID JOHN BARTLETT'
```

Please do not do this. The purpose of this exercise is to **create new variables from the original ones**.

# Booleans

Read through the following expressions and predict the value and data type of each one.

Justify your prediction and then type them into the Python REPL to check if you were correct.

Make sure you understand why you got the results you did and investigate any that surprise you.

A:

```
30 > 12 True
```

B:

```
4 < 4 False
```

C:

```
12 == '12' False
```

D:

```
7 < 7.0 False
```

E:

```
1 == True 
```

F:

```
0.9 < True True
```

G:

```
14 > 5 and len('tree') == 8/2 True
```

H:

```
3 and 4 True 4
```

I:

```
3 and 0 False 0
```

J:

```
0 and 3 False 0
```

K:

```
3 > 4 or 5 > 2 True
```

L:

```
5 or 0.7 True 5
```

M:

```
5 > 10 or 4 True 4
```

N:

```
not 10 > 5 False
```

O:

```
not 10 < 5 True
```

P:

```
not 3 False
```
