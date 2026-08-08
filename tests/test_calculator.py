"""Testing the class Calculator and its methods"""

import pytest

from utils.calculator import Calculator

calculator = Calculator()


def test_addition_of_multiple_numbers():
    """Test that adding multiple integers and floats returns valid result."""

    number_list = [4, 6.05, 33.333, 10, 140]
    round_off_number = 3

    result = calculator.add(*number_list, round_off_digit=round_off_number)

    assert result == pytest.approx(193.383)


def test_subtraction_of_multiple_numbers():
    """Test that subtracting multiple integers and floats returns valid result."""

    number_list = [4, 6.05, 33.333, 10, 140]
    round_off_number = 1

    result = calculator.subtract(*number_list, round_off_digit=round_off_number)

    assert result == pytest.approx(-185.4)


def test_multiplication_of_multiple_numbers():
    """Test that multiplying multiple integers and floats returns valid result."""

    number_list = [4, 6.05, -33.333, -10, -140.7]
    round_off_number = 4

    result = calculator.multiply(*number_list, round_off_digit=round_off_number)

    assert result == pytest.approx(-1134968.6502)


def test_division_of_multiple_numbers():
    """Test that dividing multiple integers and floats returns valid result."""

    number_list = [40520, -6.05, -33.333, -10, -14.7]
    round_off_number = 6

    result = calculator.divide(*number_list, round_off_digit=round_off_number)

    assert result == 1.366855


def test_division_by_zero():
    """Test dividing a number into zero outputs None."""

    number_list = [400, 0, -3.333, -10, -14.7]
    round_off_number = 2

    result = calculator.divide(*number_list, round_off_digit=round_off_number)

    assert result is None
