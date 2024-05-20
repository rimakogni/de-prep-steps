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

    def test_is_not_same_as_should_print_skip_test_message(self, capsys):
        def add(num):
            return num + num

        test_title = "add func"
        skip = SkipCheck(add, test_title)

        skip.is_not_same_as({"lucky_number": 13})

        captured = capsys.readouterr()
        log_message = f"Test {test_title}: skipping test..."

        assert f"{add.__name__}()" in captured.out
        assert log_message in captured.out

    def test_is_type_should_print_skip_test_message(self, capsys):
        def add(num):
            return num + num

        test_title = "add func"

        skip = SkipCheck(add, test_title)

        skip.is_type(str)

        captured = capsys.readouterr()
        log_message = f"Test {test_title}: skipping test..."

        assert f"{add.__name__}()" in captured.out
        assert log_message in captured.out

    def test_returns_should_print_skip_test_message(self, capsys):
        test_title = "returns 8"

        def add(num):
            return num + num

        skip = SkipCheck(add, test_title)
        skip.returns(4)

        captured = capsys.readouterr()
        log_message = f"Test {test_title}: skipping test..."

        assert f"{add.__name__}()" in captured.out
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

    def test_is_not_same_as_prints_helpful_message_when_return_value_IS_the_given_object(
        self, capsys
    ):
        def return_list(some_list):
            return some_list

        test_title = "returns different list"

        check = Check(return_list, test_title)

        test_list = [1, 2, 3]

        check.when_called_with(test_list).is_not_same_as(test_list)

        captured = capsys.readouterr()
        log_message = (
            f"Test {test_title}: Test failed, return value should be a new list"
        )

        assert f"{return_list.__name__}()" in captured.out
        assert log_message in captured.out

    def test_is_not_same_as_prints_helpful_message_when_return_value_IS_NOT_same_as_the_given_object(
        self, capsys
    ):
        def return_list(some_list):
            return [el for el in some_list]

        test_title = "returns different list"
        check = Check(return_list, test_title)

        test_list = [1, 2, 3]

        check.when_called_with(test_list).is_not_same_as(test_list)

        captured = capsys.readouterr()
        log_message = f"Test {
            test_title}: Test passed, new Python object returned"

        assert f"{return_list.__name__}()" in captured.out
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
        log_message = f"Test {
            test_title}: Test passed, correct data type returned"

        assert f"{return_list.__name__}()" in captured.out
        assert log_message in captured.out

    def test_is_type_prints_helpful_message_when_return_value_IS_NOT_same_as_correct_type(
        self, capsys
    ):
        def return_list(some_list):
            return some_list

        test_title = "returns list"
        check = Check(return_list, test_title)

        test_list = [1, 2, 3]

        check.when_called_with(test_list).is_type(str)

        captured = capsys.readouterr()

        log_message = (
            f"Test {test_title}: Return value should "
            f"be of type {test_list.__class__.__name__}"
        )

        assert f"{return_list.__name__}()" in captured.out
        assert log_message in captured.out

    def test_returns_should_print_test_passed_message(self, capsys):
        test_title = "returns 8"

        def add(num_1, num_2):
            return num_1 + num_2

        check = Check(add, test_title)
        check.when_called_with(4, 4).returns(8)

        captured = capsys.readouterr()
        log_message = f"Test {test_title}: Test passed"

        assert f"{add.__name__}()" in captured.out
        assert log_message in captured.out

    def test_returns_prints_message_when_return_value_is_not_same_as_expected(
        self, capsys
    ):
        test_title = "returns 8"

        def add(num_1, num_2):
            return num_1 + num_2 + 1

        check = Check(add, test_title)
        check.when_called_with(4, 4).returns(8)

        captured = capsys.readouterr()
        log_message = f"Test {test_title}: expected '8', but received '9'"

        assert f"{add.__name__}()" in captured.out
        assert log_message in captured.out

    def test_is_same_as_should_print_test_passed_message(self, capsys):
        def return_list(some_list):
            return some_list

        test_title = "same object returned"
        check = Check(return_list, test_title)

        test_list = [1, 2, 3]

        check.when_called_with(test_list).is_same_as(test_list)

        captured = capsys.readouterr()
        log_message = f"Test {test_title}: Test passed, same object returned"

        assert f"{return_list.__name__}()" in captured.out
        assert log_message in captured.out

    def test_is_same_as_should_print_test_failed_message(self, capsys):
        def return_list(some_list):
            return [el for el in some_list]

        test_title = "same object returned"
        check = Check(return_list, test_title)

        test_list = [1, 2, 3]

        check.when_called_with(test_list).is_same_as(test_list)

        captured = capsys.readouterr()
        log_message = (
            f"Test {test_title}: Test failed, "
            "return value should be the same object"
        )

        assert f"{return_list.__name__}()" in captured.out
        assert log_message in captured.out

    def test_mutates_input_should_print_test_passed_message(self, capsys):
        def add_one_to_list(some_list):
            some_list.append(1)

        test_title = "mutates input"
        check = Check(add_one_to_list, test_title)

        test_list = [1, 2, 3]

        check.when_called_with(test_list).mutates_input("frogs")

        captured = capsys.readouterr()
        log_message = (
            f"Test {test_title}: Test passed, "
            "frogs successfully mutated"
        )

        assert f"{add_one_to_list.__name__}()" in captured.out
        assert log_message in captured.out

    def test_mutates_input_should_print_test_failed_message(self, capsys):
        def add_one_to_list(some_list):
            return some_list

        test_title = "mutates input"
        check = Check(add_one_to_list, test_title)

        test_list = [1, 2, 3]

        check.when_called_with(test_list).mutates_input("bananas")

        captured = capsys.readouterr()
        log_message = (
            f"Test {test_title}: Test failed, "
            "bananas has not been mutated"
        )

        assert f"{add_one_to_list.__name__}()" in captured.out
        assert log_message in captured.out
