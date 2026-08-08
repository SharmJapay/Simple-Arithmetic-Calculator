"""
Simple Arithmetic Calculator is a command-line program built to handle basic operations
like (add, subtract, multiply, divide) with strict user input validation.
This returns the list of all user input numbers, round off digit, and the
total result of all the math calculations done without exiting the program.
"""

from utils.input_validations import (
    get_yes_no_answer,
    get_operation,
    get_number_list_input,
    get_round_off_digit,
)
from utils.calculator import Calculator


def calculate_multiple_numbers(calculator):
    """Returns the result of all the number inputs of the chosen math operation"""

    print("Welcome to the Simple Arithmetic Calculator for multiple numbers!\n")

    print(
        "You can perform addition, subtraction, multiplication, and division on multiple numbers."
    )

    start_calculation = get_yes_no_answer(
        "\nDo you want to start the calculation? (Yes / No): "
    )

    while start_calculation == "yes":

        # Know what operation the user wants to perform
        operation = get_operation("\nEnter the operation (+, -, *, /): ")

        # Get user input for multiple numbers
        number_list = get_number_list_input(
            "\nEnter float and integer numbers separated by commas (e.g. 1, 2, 3.5, 4, 5.0): "
        )

        round_off_number = get_round_off_digit(
            "\nEnter the number of desired decimal digit (empty means usage of default value): "
        )

        if operation == "+":
            sum_total = calculator.add(*number_list, round_off_digit=round_off_number)
            print(f"The sum output is: {sum_total}")
            calculator.get_total_of_all_computations(round_off_number)

        elif operation == "-":
            difference_total = calculator.subtract(
                *number_list, round_off_digit=round_off_number
            )
            print(f"The difference output is: {difference_total}")
            calculator.get_total_of_all_computations(round_off_number)

        elif operation == "*":
            product_total = calculator.multiply(
                *number_list, round_off_digit=round_off_number
            )
            print(f"The product output is: {product_total}")
            calculator.get_total_of_all_computations(round_off_number)

        elif operation == "/":
            quotient_total = calculator.divide(
                *number_list, round_off_digit=round_off_number
            )

            if quotient_total or quotient_total == 0:
                print(f"The quotient output is: {quotient_total}")
                calculator.get_total_of_all_computations(round_off_number)

        else:
            print("Invalid operation. Please enter one of the operations (+, -, *, /).")

        restart_calculation = get_yes_no_answer(
            "\nDo you want to start the calculation again? (Yes / No): "
        )

        if restart_calculation == "yes":
            continue
        break

    print("\nThank you for trying this calculator...")
    print("\nThis calculator will now end.")


def main() -> None:
    """Create and run the calculator application."""

    # Create an instance of the class Calculator
    calculator = Calculator()

    # Run the calculator
    calculate_multiple_numbers(calculator)


# This Python boilerplate code ensures that the main() function
# only runs when the script is executed directly,
# rather than when it is imported as a module into another file
if __name__ == "__main__":
    main()
