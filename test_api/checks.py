class SkipCheck:
    def __init__(self, func, title):
        self.func = func
        self.title = title

    def when_called_with(self, *args):
        pass

    def is_not(self, orginal_data):
        pass

    def is_type(self, data_type):
        pass

    def returns(self, return_value):
        print(f"Test {self.title}, {self.func.__name__}(): skipping test...")
