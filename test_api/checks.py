class SkipCheck:
    def __init__(self, func, title):
        self.func = func
        self.title = title

    def when_called_with(self, *args):
        pass

    def is_not(self, original_data):
        pass

    def is_type(self, data_type):
        pass

    def returns(self, return_value):
        print(f"Test {self.title}, {self.func.__name__}(): skipping test...")


class Check:
    def __init__(self, func, title):
        self.func = func
        self.title = title

    def when_called_with(self, *args):
        self.args = args
        return self

    def is_not(self, original_data):
        self._set_return_value()

        if self.return_value is not original_data:
            print(f"Test {self.title}, {self.func.__name__}(): Test passed")
        else:
            print("Return value should be a new object")

    def is_type(self, data_type):
        self._set_return_value()
        if isinstance(self.return_value, data_type):
            print(f"Test {self.title}, {self.func.__name__}(): Test passed")
        else:
            print(
                f"""Return value should be of type {self.return_value.__class__.__name__}"""
            )

    def _set_return_value(self):
        if hasattr(self, "args"):
            self.return_value = self.func(*self.args)
        else:
            self.return_value = self.func()

    def returns(self, expected_return_value):
        self._set_return_value()
        if self.return_value == expected_return_value:
            print(f"Test {self.title}, {self.func.__name__}(): Test passed")
        else:
            print(
                f"""{self.func.__name__}: expected {expected_return_value}, but received {self.return_value}"""
            )
