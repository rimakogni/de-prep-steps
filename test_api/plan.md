# Test API plan:

## Outline

2 classes: `Check` and `SkipCheck`
- mirrored classes, skip only returns a print to terminal saying skipping.

## Methods:

- `when_called_with`
    - For passing in args. Creates attribute if needed. Returns self. 
- `returns`
    - Should check for args attribute. Either runs the function with args or without. If passes returns GREEN text. If fails returns formatted RED text with error to terminal.
- `is_not`
    - Should check for mutation of the original data. Returns a GREEN / RED text for passing / failing. RED text should state the func is mutating original data.
- `is_type`
    - Should check the type of the return_value. Returns a GREEN / RED text for passing / failing. RED text should state that type is incorrect and print type with assert.

## Output:

Use colours for stdout

- Incorrect result: helpful string with function name, expected return vs actual return. Also include assert error
- Correct result: Success string


## Extras: 

- typing? (for the type checking tasks might be a bit strange, unless we use the pydantic type error)
- Move all katas into root(?) and move testing into the .py files(same files as katas). 
- leave data in tests. 

- Use if statements with custom errors instead of asserting in code (appaz shouldnt use assert in prod code)