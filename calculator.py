"""A Simple Calculator for Basic Arithmetic Operations (+, -, * , /)

Next Steps:
    a) Add other operations like sqrt, squared, modulus. etc.
    b) Add more numbers to calculate instead of 2 numbers only

"""

from input_validations import (
    check_answer,
    check_operation,
    get_number_list_input,
    get_round_off_digit,
)
from calculations import Calculator

# calculator = Calculator()

# calculator.add(34, 56.234, 294, 12.356, roundOfDigit=3)

# calculator.subtract(150.23, 60.6, 45.457, -54.781, roundOfDigit=3)

# calculator.multiply(15.6, 6.5, 2.5, 3.5, roundOfDigit=3)

# calculator.divide(1500, 60, 5, 2.5, roundOfDigit=3)

# calculator.getTotalResult(roundOfDigit=3)


def calculate_multiple_numbers():
    """Runs Simple Arithmetic Calculator for multiple numbers"""

    print("Welcome to the Simple Arithmetic Calculator for multiple numbers!\n")
    print(
        "You can perform addition, subtraction, multiplication, and division on multiple numbers.\n"
    )

    start_calculation = check_answer(
        "Do you want to start the calculation? (Yes / No): "
    )

    while start_calculation == "yes":

        # Know what operation the user wants to perform
        operation = check_operation("Enter the operation (+, -, *, /): ")

        # Get user input for multiple numbers
        number_list = get_number_list_input(
            "Enter float and integer numbers separated by commas (e.g. 1, 2, 3.5, 4, 5.0): "
        )

        round_off_digit = get_round_off_digit(
            "Enter the number of decimal places to round the result to (default is 2): "
        )

        calculator = Calculator()

        if operation == "+":
            calculator.add(*number_list, round_off_digit=round_off_digit)
        elif operation == "-":
            calculator.subtract(*number_list, round_off_digit=round_off_digit)
        elif operation == "*":
            calculator.multiply(*number_list, round_off_digit=round_off_digit)
        elif operation == "/":
            calculator.divide(*number_list, round_off_digit=round_off_digit)
        else:
            print("Invalid operation. Please enter one of the operations (+, -, *, /).")

        restart_calculation = check_answer(
            "Do you want to start the calculation again? (Yes / No): "
        )

        if restart_calculation == "yes":
            continue
        break

    print("\nThank you for trying this calculator...")
    print("\nThis calculator will now end.")


calculate_multiple_numbers()
