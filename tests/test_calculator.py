"""Testing the class Calculator and its methods"""

import pytest

from utils.calculator import Calculator

calculator = Calculator()


def test_add_multiple_numbers():
    """Test that adding multiple integers and floats returns valid result."""

    number_list = [4, 6.05, 33.333, 10, 140]
    round_off_number = 3

    result = calculator.add(*number_list, round_off_digit=round_off_number)

    assert result == pytest.approx(193.383)


def test_subtract_multiple_numbers():
    """Test that subtracting multiple integers and floats returns valid result."""

    number_list = [4, 6.05, 33.333, 10, 140]
    round_off_number = 1

    result = calculator.subtract(*number_list, round_off_digit=round_off_number)

    assert result == pytest.approx(-185.4)


def test_multiply_multiple_numbers():
    """Test that multiplying multiple integers and floats returns valid result."""

    number_list = [4, 6.05, -33.333, -10, -140.7]
    round_off_number = 4

    result = calculator.multiply(*number_list, round_off_digit=round_off_number)

    assert result == pytest.approx(-1134968.6502)


def test_division_by_zero():
    """Test dividing a number into zero triggers a ValueError."""

    number_list = [400, 0, -3.333, -10, -14.7]
    round_off_number = 2

    # Expect a ValueError because the production code converts ZeroDivisionError
    with pytest.raises(ValueError) as exc_info:
        calculator.divide(*number_list, round_off_digit=round_off_number)

    # Optional: Verify your custom error message is present
    assert "Division by zero is not allowed" in str(exc_info.value)
