"""The defined class for calculator with basic arithmetic operations functions like
add(), subtract(), multiply(), and divide()"""

# OOP Structure:
# 1) Define a class
# 2) Define global variables or class properties -> Properties defined outside methods
# 3) Define the __init__(self, *args, **kwargs) Method
#    (initialize variables or instance properties -> *args, and **kwargs variables)
#    self.args = args -> initialize positional arguments
#    self.kwargs = kwargs -> initialize keyword arguments
#    super().__init__(*args, **kwargs) -> (Optional) Passes values to the parent or base class
# 4) Define Instance Methods
# 5) Create an Object (Instantiate the Class)


# ******* Solution ********


# 1) Define a class
class Calculator:
    """This is a class with different custom math operation methods
    like add(), subtract(), multiply(), and divide()

    Instances:
        add() - Performs Addition Operation
        subtract() - Performs Subtraction Operation
        multiply() - Performs Multiplication Operation
        divide() - Performs Division Operation

    Attributes:
        total_result - Stores the total final result of the calculation
        default_round_off_value - Sets the default round off digit
    """

    # 2) Define class properties -> Properties defined outside methods
    DEFAULT_ROUND_OFF_DIGIT = 2

    # 3) Define the __init__(self, *args, **kwargs) Method
    #    (initialize variables or instance properties -> *args, and **kwargs variables)

    def __init__(self):
        """Initializes the calculator with a default result 0.0"""
        self.total_result = 0.0

    # 4) Define Instance Methods

    def add(self, *numbers, round_off_digit):
        """Add multiple numbers

        Arguments:
            numbers (tuple) - *args: List of input numbers for calculation

        Keyword Arguments:
            round_off_digit (int) - Number of decimal places to round the result to (default is 2)

        Errors:
            TypeError - Raised when the input is not a number

        Returns:
            result (float) - The sum of all input numbers
        """

        try:
            # Initialize result with the first number
            result = numbers[0]

            for index, number in enumerate(numbers):
                # Debugging line to show the current index and number
                print(f"Number {index + 1} : {number}")

                # Skip the first number since it's already assigned to result
                if index != 0:
                    result += number

            round_off_digit = (
                self.DEFAULT_ROUND_OFF_DIGIT if not round_off_digit else round_off_digit
            )

            print(f"Round off to: {round_off_digit} digits")

            self.total_result += round(result, round_off_digit)

            return round(result, round_off_digit)

        except TypeError as e:

            raise ValueError(
                f"Error: {e}. \nPlease provide valid numbers for addition."
            ) from e

    def subtract(self, *numbers, round_off_digit):
        """Subtract multiple numbers

        Arguments:
            numbers (tuple) - *args: List of input numbers for calculation

        Keyword Arguments:
            round_off_digit (int) - Number of decimal places to round the result to (default is 2)

        Errors:
            TypeError - Raised when the input is not a number

        Returns:
            result (float) - The difference of all input numbers
        """

        try:
            # Initialize result with the first number
            result = numbers[0]

            for index, number in enumerate(numbers):
                # Debugging line to show the current index and number
                print(f"Number {index + 1} : {number}")

                # Skip the first number since it's already assigned to result
                if index != 0:
                    result -= number

            round_off_digit = (
                self.DEFAULT_ROUND_OFF_DIGIT if not round_off_digit else round_off_digit
            )

            print(f"Round off to: {round_off_digit} digits")

            self.total_result += round(result, round_off_digit)

            return round(result, round_off_digit)

        except TypeError as e:

            raise ValueError(
                f"Error: {e}. \nPlease provide valid numbers for subtraction."
            ) from e

    def multiply(self, *numbers, round_off_digit):
        """Multiply multiple numbers

        Arguments:
            numbers (tuple) - *args: List of input numbers for calculation

        Keyword Arguments:
            round_off_digit (int) - Number of decimal places to round the result to (default is 2)

        Errors:
            TypeError - Raised when the input is not a number

        Returns:
            result (float) - The product of all input numbers
        """

        try:
            # Initialize result with the first number
            result = numbers[0]

            for index, number in enumerate(numbers):
                # Debugging line to show the current index and number
                print(f"Number {index + 1} : {number}")

                # Skip the first number since it's already assigned to result
                if index != 0:
                    result *= number

            round_off_digit = (
                self.DEFAULT_ROUND_OFF_DIGIT if not round_off_digit else round_off_digit
            )

            print(f"Round off to: {round_off_digit} digits")

            self.total_result += round(result, round_off_digit)

            return round(result, round_off_digit)

        except TypeError as e:

            raise ValueError(
                f"Error: {e}. \nPlease provide valid numbers for multiplication."
            ) from e

    def divide(self, *numbers, round_off_digit):
        """Divide multiple numbers

        Arguments:
            numbers (tuple) - *args: List of input numbers for calculation

        Keyword Arguments:
            round_off_digit (int) - Number of decimal places to round the result to (default is 2)

        Errors:
            TypeError - Raised when the input is not a number
            ZeroDivisionError - Raised when attempting to divide by zero

        Returns:
            result (float) - The quotient of all input numbers
        """

        try:
            # Initialize result with the first number
            result = numbers[0]

            # Catch Division by zero
            if 0 in numbers[1:]:
                print("Error: Division by zero is not allowed. Try again.")
                return

            for index, number in enumerate(numbers):
                # Debugging line to show the current index and number
                print(f"Number {index + 1} : {number}")

                # Skip the first number since it's already assigned to result
                if index != 0:
                    result /= number

            round_off_digit = (
                self.DEFAULT_ROUND_OFF_DIGIT if not round_off_digit else round_off_digit
            )

            print(f"Round off to: {round_off_digit} digits")

            self.total_result += round(result, round_off_digit)

            return round(result, round_off_digit)

        except TypeError as e:

            raise ValueError(
                f"Error: {e}. \nPlease provide valid numbers for division."
            ) from e

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


# 5) Create an instance (object) of the Calculator class
calculator = Calculator()
