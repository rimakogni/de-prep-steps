from checks import SkipCheck, Check


class TestSkipCheck:

    def test_skipCheck_is_initialised_with_a_function_and_title(self):
        def add(num):
            return num + num

        skip = SkipCheck(add, "add")

        assert skip.func == add
        assert skip.title == "add"

    def test_when_called_with_returns_self(self):
        def add(num):
            return num + num

        skip = SkipCheck(add, "add")

        assert skip.when_called_with(2) is skip

    def test_is_not_should_print_skip_test_message(self, capsys):
        def add(num):
            return num + num
        test_title = "add func"
        skip = SkipCheck(add, test_title)

        skip.is_not({"lucky_number": 13})

        captured = capsys.readouterr()
        log_message = f"{add.__name__}(), Test {test_title}: skipping test..."

        assert log_message in captured.out

    def test_is_type_should_print_skip_test_message(self, capsys):
        def add(num):
            return num + num
        test_title = "add func"

        skip = SkipCheck(add, test_title)

        skip.is_type(str)

        captured = capsys.readouterr()
        log_message = f"{add.__name__}(), Test {test_title}: skipping test..."

        assert log_message in captured.out

    def test_returns_should_print_skip_test_message(self, capsys):
        test_title = "returns 8"

        def add(num):
            return num + num

        skip = SkipCheck(add, test_title)
        skip.returns(4)

        captured = capsys.readouterr()
        log_message = f"{add.__name__}(), Test {test_title}: skipping test..."

        assert log_message in captured.out


class TestCheck:

    def test_check_is_initialised_with_a_function_and_title(self):
        def add(num):
            return num + num

        check = Check(add, "add")

        assert check.func == add
        assert check.title == "add"

    def test_when_called_with_set_args_attr_single_arg(self):
        def add(num):
            return num + num

        check = Check(add, "add")

        check.when_called_with(1)

        assert check.args == (1,)

    def test_when_called_with_set_args_attr_multi_args(self):
        def add(num_1, num_2):
            return num_1 + num_2

        check = Check(add, "add")

        check.when_called_with(1, 2)

        assert check.args == (1, 2)

    def test_when_called_with_returns_self(self):
        def add(num_1, num_2):
            return num_1 + num_2

        check = Check(add, "add")

        returned = check.when_called_with(1, 2)

        assert returned is check

    def test_set_return_value_no_args(self):
        def say_hello():
            return "hello"

        check = Check(say_hello, "says hello title")

        check._set_return_value()

        assert check.return_value == "hello"

    def test_set_return_value_with_args(self):
        def add(num_1, num_2):
            return num_1 + num_2

        check = Check(add, "add")

        check.when_called_with(1, 2)

        check._set_return_value()

        assert check.return_value == 3

    def test_is_not_prints_helpful_message_when_return_value_IS_the_given_object(
        self, capsys
    ):
        def return_list(some_list):
            return some_list
        test_title = "returns different list"

        check = Check(return_list, test_title)

        test_list = [1, 2, 3]

        check.when_called_with(test_list).is_not(test_list)

        captured = capsys.readouterr()
        log_message = (
            f"{return_list.__name__}(), Test {test_title}: Test failed, "
            "return value should be a new object")

        assert log_message in captured.out

    def test_is_not_prints_helpful_message_when_return_value_IS_NOT_the_given_object(
        self, capsys
    ):
        def return_list(some_list):
            return [el for el in some_list]

        test_title = "returns different list"
        check = Check(return_list, test_title)

        test_list = [1, 2, 3]

        check.when_called_with(test_list).is_not(test_list)

        captured = capsys.readouterr()
        log_message = (
            f"{return_list.__name__}(), Test {test_title}: Test passed, new "
            "object returned"
        )

        assert log_message in captured.out

    def test_is_type_prints_pass_message_when_value_IS_correct_type(
        self, capsys
    ):
        def return_list(some_list):
            return some_list

        test_title = "returns list"
        check = Check(return_list, test_title)

        test_list = [1, 2, 3]

        check.when_called_with(test_list).is_type(list)

        captured = capsys.readouterr()
        log_message = (
            f"{return_list.__name__}(), Test {test_title}: Test passed, "
            f"correct data type returned"
        )

        assert log_message in captured.out

    def test_is_type_prints_helpful_message_when_return_value_IS_NOT_correct_type(
        self, capsys
    ):
        def return_list(some_list):
            return some_list

        test_title = "returns list"
        check = Check(return_list, test_title)

        test_list = [1, 2, 3]

        check.when_called_with(test_list).is_type(str)

        captured = capsys.readouterr().out

        log_message = (
            f"{return_list.__name__}(), Test {test_title}: Return value should"
            f" be of type {test_list.__class__.__name__}"
        )

        assert log_message in captured

    def test_returns_should_print_test_passed_message(self, capsys):
        test_title = "returns 8"

        def add(num_1, num_2):
            return num_1 + num_2

        check = Check(add, test_title)
        check.when_called_with(4, 4).returns(8)

        captured = capsys.readouterr()
        log_message = f"{add.__name__}(), Test {test_title}: Test passed"

        assert log_message in captured.out

    def test_returns_prints_message_when_return_value_is_not_expected(
        self, capsys
    ):
        test_title = "returns 8"

        def add(num_1, num_2):
            return num_1 + num_2 + 1

        check = Check(add, test_title)
        check.when_called_with(4, 4).returns(8)

        captured = capsys.readouterr()
        log_message = (
            f"{add.__name__}(), Test {test_title}: expected 8, but received 9")

        assert log_message in captured.out
