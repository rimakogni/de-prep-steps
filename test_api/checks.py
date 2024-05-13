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

        try:
            assert self.return_value is not original_data
            print(f"Test {self.title}, {self.func.__name__}(): Test passed")
        except AssertionError:
            print('Return value should be a new object')
            raise
 

    def is_type(self, data_type):
        # make use of _set_return_value?
        # print here
        pass

    def _set_return_value(self):
        if (hasattr(self, "args")):
            self.return_value = self.func(*self.args)
        else:
            self.return_value = self.func()


    def returns(self):
        # print here
        pass