"""A class named "Calculator" used for Basic Arithmetic Operations (+, -, * , /)"""

# OOP Structure:
# 1) Define a class
# 2) Define the __init__ Method (initialize variables -> self, *args, and other variables)
# 3) Define Instance Methods
# 4) Create an Object (Instantiate the Class)


# ******* Solution ********


# 1) Define a class
class Calculator:
    """A simple calculator class for basic arithmetic operations

    Instances:
        add() - Performs Addition Operation
        subtract() - Performs Subtraction Operation
        multiply() - Performs Multiplication Operation
        divide() - Performs Division Operation

    Attributes:
        total_result - Stores the total final result of the calculation
    """

    # 2) Define the __init__ Method (initialize variables -> self, *args, and other variables)

    def __init__(self):
        """Initializes the calculator with a default result 0.0"""
        self.total_result = 0.0

    # 3) Define Instance Methods

    def add(self, *numbers, round_off_digit=2):
        """Add multiple numbers

        Arguments:
            *numbers (tuple) - *args: List of input numbers for calculation

        Keyword Arguments:
            round_off_digit (int) - Number of decimal places to round the result to (default is 2)

        Errors:
            TypeError - Raised when the input is not a number

        Returns:
            result (float) - The sum of all input numbers
        """

        try:
            if numbers:
                # Initialize result with the first number
                result = numbers[0]

                for index, number in enumerate(numbers):
                    # Debugging line to show the current index and number
                    print(f"Number {index + 1} {type(number)}: {number}")

                    # Skip the first number since it's already assigned to result
                    if index != 0:
                        result += number

                self.total_result += result

                print(f"The sum output is: {round(result, round_off_digit)} \n")
            else:
                print("No numbers provided for addition. \n")

        except TypeError as e:
            print(f"Error: {e}. \nPlease provide valid numbers for addition.")

    def subtract(self, *numbers, round_off_digit=2):
        """Subtract multiple numbers

        Arguments:
            *numbers (tuple) - *args: List of input numbers for calculation

        Keyword Arguments:
            round_off_digit (int) - Number of decimal places to round the result to (default is 2)

        Errors:
            TypeError - Raised when the input is not a number

        Returns:
            result (float) - The difference of all input numbers
        """

        try:
            if numbers:
                # Initialize result with the first number
                result = numbers[0]

                for index, number in enumerate(numbers):
                    # Debugging line to show the current index and number
                    print(f"Number {index + 1} {type(number)}: {number}")

                    # Skip the first number since it's already assigned to result
                    if index != 0:
                        result -= number

                self.total_result += result

                print(f"The difference output is: {round(result, round_off_digit)} \n")
            else:
                print("No numbers provided for subtraction. \n")

        except TypeError as e:
            print(f"Error: {e}. \nPlease provide valid numbers for subtraction.")

    def multiply(self, *numbers, round_off_digit=2):
        """Multiply multiple numbers

        Arguments:
            *numbers (tuple) - *args: List of input numbers for calculation

        Keyword Arguments:
            round_off_digit (int) - Number of decimal places to round the result to (default is 2)

        Errors:
            TypeError - Raised when the input is not a number

        Returns:
            result (float) - The product of all input numbers
        """

        try:
            if numbers:
                # Initialize result with the first number
                result = numbers[0]

                for index, number in enumerate(numbers):
                    # Debugging line to show the current index and number
                    print(f"Number {index + 1} {type(number)}: {number}")

                    # Skip the first number since it's already assigned to result
                    if index != 0:
                        result *= number

                self.total_result += result

                print(f"The product output is: {round(result, round_off_digit)} \n")
            else:
                print("No numbers provided for multiplication. \n")

        except TypeError as e:
            print(f"Error: {e}. \nPlease provide valid numbers for multiplication.")

    def divide(self, *numbers, round_off_digit=2):
        """Divide multiple numbers

        Arguments:
            *numbers (tuple) - *args: List of input numbers for calculation

        Keyword Arguments:
            round_off_digit (int) - Number of decimal places to round the result to (default is 2)

        Errors:
            TypeError - Raised when the input is not a number
            ZeroDivisionError - Raised when attempting to divide by zero

        Returns:
            result (float) - The quotient of all input numbers
        """

        try:
            if numbers:
                # Initialize result with the first number
                result = numbers[0]

                for index, number in enumerate(numbers):
                    # Debugging line to show the current index and number
                    print(f"Number {index + 1} {type(number)}: {number}")

                    # Skip the first number since it's already assigned to result
                    if index != 0:
                        result /= number

                self.total_result += result

                print(f"The quotient output is: {round(result, round_off_digit)} \n")
            else:
                print("No numbers provided for division. \n")

        except TypeError as e:
            print(f"Error: {e}. \nPlease provide valid numbers for division.")
        except ZeroDivisionError as e:
            print(
                f"Error: {e} \nDivision by zero is not allowed. Provide valid numbers for division."
            )

    def get_total_result(self, round_off_digit=2):
        """Get the total result of all calculations

        Keyword Arguments:
            round_off_digit (int) - Number of decimal places to round the result to (default is 2)

        Returns:
            total_result (float) - The total result of all calculations
        """
        print(
            f"The total of all results is: {round(self.total_result, round_off_digit)} \n"
        )


# 4) Create an instance (object) of the Calculator class
calculator = Calculator()
