from checks import SkipCheck


class TestSkipCheck:

    def test_skipCheck_is_initalised_with_a_function_and_title(self):
        def add(num):
            return num + num

        skip = SkipCheck(add, "add")

        assert skip.func == add
        assert skip.title == "add"

    def test_when_called_with_returns_None(self):
        def add(num):
            return num + num

        skip = SkipCheck(add, "add")

        assert skip.when_called_with(2) is None

    def test_is_not_returns_None(self):
        def add(num):
            return num + num

        skip = SkipCheck(add, "add")

        assert skip.is_not({"lucky_number": 13}) is None

    def test_is_type_returns_None(self):
        def add(num):
            return num + num

        skip = SkipCheck(add, "add")

        assert skip.is_type(str) is None

    def test_returns_should_return_skip_test_message(self, capsys):
        test_title = "returns 8"

        def add(num):
            return num + num

        skip = SkipCheck(add, test_title)
        skip.returns(4)

        captured = capsys.readouterr()
        log_message = f"Test {test_title}, {add.__name__}(): skipping test..."

        assert log_message in captured.out
