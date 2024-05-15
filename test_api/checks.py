class SkipCheck:
    def __init__(self, func, title):
        self.func = func
        self.title = title

    def when_called_with(self, *args):
        return self

    def is_not(self, original_data):
        print(f"{self.func.__name__}(), Test {self.title}: skipping test...")

    def is_type(self, data_type):
        print(f"{self.func.__name__}(), Test {self.title}: skipping test...")

    def returns(self, return_value):
        print(f"{self.func.__name__}(), Test {self.title}: skipping test...")

    # TODO: Add method for checking for input mutation!


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
            feedback_msg = (
                f"{self.func.__name__}(), Test {self.title}: Test passed, "
                "new object returned"
            )

        else:
            feedback_msg = (
                f"{self.func.__name__}(), Test {self.title}: Test failed, "
                "return value should be a new object"
            )

        print(feedback_msg)

    def is_type(self, data_type):
        self._set_return_value()

        if isinstance(self.return_value, data_type):
            feedback_msg = (
                f"{self.func.__name__}(), Test {self.title}: Test passed, "
                "correct data type returned"
            )
        else:
            feedback_msg = (
                f"{self.func.__name__}(), Test {self.title}: Return value "
                f"should be of type {self.return_value.__class__.__name__}"
            )

        print(feedback_msg)

    def _set_return_value(self):
        if hasattr(self, "args"):
            self.return_value = self.func(*self.args)
        else:
            self.return_value = self.func()

    def returns(self, expected_return_value):
        self._set_return_value()

        if self.return_value == expected_return_value:
            feedback_msg = (
                f"{self.func.__name__}(), Test {self.title}: Test passed"
            )
        else:
            feedback_msg = (
                f"{self.func.__name__}(), Test {self.title}: expected "
                f"{expected_return_value}, but received {self.return_value}"
            )

        print(feedback_msg)

    # TODO: Add method for checking for input mutation!
