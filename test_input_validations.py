"""Testing input validation functions for the calculator program."""

from input_validations import (
    check_answer,
    check_operation,
    get_number_list_input,
    get_round_off_digit,
)


def test_valid_different_yes_input(monkeypatch):
    """Test that entering different 'yes' returns 'yes'."""

    # Simulate typing "yes" followed by Enter
    monkeypatch.setattr("builtins.input", lambda _: "yes")

    result = check_answer("Do you want to start the calculation? (Yes / No): ")
    assert result in ["yes", "no"]

    # Simulate typing "YES" followed by Enter
    monkeypatch.setattr("builtins.input", lambda _: "YES")

    result = check_answer("Do you want to start the calculation? (Yes / No): ")
    assert result in ["yes", "no"]

    # Simulate typing "YeS " followed by Enter
    monkeypatch.setattr("builtins.input", lambda _: "YeS ")

    result = check_answer("Do you want to start the calculation? (Yes / No): ")
    assert result in ["yes", "no"]


def test_valid_different_no_input(monkeypatch):
    """Test that entering different 'no' returns 'no'."""

    # Simulate typing "no" followed by Enter
    monkeypatch.setattr("builtins.input", lambda _: "no")

    result = check_answer("Do you want to start the calculation? (Yes / No): ")
    assert result in ["yes", "no"]

    # Simulate typing "NO" followed by Enter
    monkeypatch.setattr("builtins.input", lambda _: "NO")

    result = check_answer("Do you want to start the calculation? (Yes / No): ")
    assert result in ["yes", "no"]

    # Simulate typing " nO" followed by Enter
    monkeypatch.setattr("builtins.input", lambda _: " nO")

    result = check_answer("Do you want to start the calculation? (Yes / No): ")
    assert result in ["yes", "no"]


def test_invalid_input_then_valid_yes_no(monkeypatch):
    """Test that entering invalid inputs followed by 'yes' or 'no' returns 'yes' or 'no'."""

    # Simulate typing (invalid inputs) followed by "yes"
    inputs = iter(["hello", "hi", "maybe", "yes"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = check_answer("Do you want to start the calculation? (Yes / No): ")
    assert result in ["yes", "no"]

    # Simulate typing (invalid inputs) followed by "no"
    inputs = iter(["123", "asd123", "maybe", "no"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = check_answer("Do you want to start the calculation? (Yes / No): ")
    assert result in ["yes", "no"]


def test_valid_operation_inputs(monkeypatch):
    """Test that entering either (+, -, *, /) returns (+, -, *, /)."""

    # Simulate typing "+" followed by Enter
    monkeypatch.setattr("builtins.input", lambda _: "+")

    result = check_operation("Enter the operation (+, -, *, /): ")
    assert result in ["+", "-", "*", "/"]

    # Simulate typing "-" followed by Enter
    monkeypatch.setattr("builtins.input", lambda _: "-")

    result = check_operation("Enter the operation (+, -, *, /): ")
    assert result in ["+", "-", "*", "/"]

    # Simulate typing "+" followed by Enter
    monkeypatch.setattr("builtins.input", lambda _: "*")

    result = check_operation("Enter the operation (+, -, *, /): ")
    assert result in ["+", "-", "*", "/"]

    # Simulate typing "-" followed by Enter
    monkeypatch.setattr("builtins.input", lambda _: "/")

    result = check_operation("Enter the operation (+, -, *, /): ")
    assert result in ["+", "-", "*", "/"]


def test_invalid_operation_inputs(monkeypatch):
    """Test that entering invalid inputs followed (+, -, *, /) returns (+, -, *, /)."""

    # Simulate typing "-" followed by Enter
    monkeypatch.setattr("builtins.input", lambda _: "/")

    result = check_operation("Enter the operation (+, -, *, /): ")
    assert result in ["+", "-", "*", "/"]


def test_valid_integers_and_floats_inputs(monkeypatch):
    """Test standard valid input with integers and floats."""

    number_list = iter(["12, 58.5, 100.25, 78.78"])

    # Simulate typing "-" followed by Enter
    monkeypatch.setattr("builtins.input", lambda _: next(number_list))

    result = get_number_list_input(
        "Enter float and integer numbers separated by commas (e.g. 1, 2, 3.5, 4, 5.0): "
    )
    assert result == [12, 58.5, 100.25, 78.78]


def test_valid_integers_and_floats_with_whitespaces_inputs(monkeypatch):
    """Test standard valid input with integers and floats."""

    number_list = iter([" 12 , 58.5    , 100.25  , 78.78"])

    # Simulate typing "-" followed by Enter
    monkeypatch.setattr("builtins.input", lambda _: next(number_list))

    result = get_number_list_input(
        "Enter float and integer numbers separated by commas (e.g. 1, 2, 3.5, 4, 5.0): "
    )
    assert result == [12, 58.5, 100.25, 78.78]


def test_invalid_random_inputs(monkeypatch, capsys):
    """Test that invalid input prints an error message and loops until valid input is provided."""

    number_list = iter(["12, efg, 58.5, asd, 78.78", "12, 58.5, 78.78"])

    # Simulate typing invalid input followed by valid input
    monkeypatch.setattr("builtins.input", lambda _: next(number_list))

    result = get_number_list_input(
        "Enter float and integer numbers separated by commas (e.g. 1, 2, 3.5, 4, 5.0): "
    )

    assert result == [12, 58.5, 78.78]

    # Assert the expected error message was printed to stdout
    captured = capsys.readouterr()
    assert (
        "Invalid input. Please enter valid float and integer numbers separated by commas."
        in captured.out.strip()
    )


def test_valid_round_off_integer_input(monkeypatch):
    """Test that entering valid integer returns valid result"""

    # Simulate typing "4" followed by Enter
    monkeypatch.setattr("builtins.input", lambda _: "4")

    result = get_round_off_digit(
        "Enter the number of decimal places to round the result to (default is 2): "
    )
    assert result == 4


def test_invalid_round_off_integer_input(monkeypatch):
    """Test that entering non-integer input prints an error message and loops until valid input is provided."""

    # Simulate typing (invalid inputs) followed by "yes"
    inputs = iter(["hello", "hi", "5.5", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_round_off_digit(
        "Enter the number of decimal places to round the result to (default is 2): "
    )
    assert result == 3
