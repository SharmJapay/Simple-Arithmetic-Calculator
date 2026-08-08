"""The is the defined class for calculator with basic arithmetic operations functions like
add(), subtract(), multiply(), divide(), and get_total_of_all_computations()"""

# OOP Structure:
# 1) Define a class
# 2) Define class properties (global variables and constants) -> Properties defined outside methods
# 3) Define the __init__(self, *args, **kwargs) Method
#    (initialize variables or instance properties -> *args, and **kwargs variables)
#    self.args = args -> initialize positional arguments
#    self.kwargs = kwargs -> initialize keyword arguments
#    super().__init__(*args, **kwargs) -> (Optional) Passes values to the parent or base class
# 4) Define Instance Methods (private and public methods)
# 5) Create an Object (Instantiate the Class)


# ******* Solution ********


# 1) Define a class
class Calculator:
    """This is a class with different custom math operation methods
    like add(), subtract(), multiply(), divide(), and get_total_of_all_computations()

    Instances Methods:
        add() - Performs Addition Operation
        subtract() - Performs Subtraction Operation
        multiply() - Performs Multiplication Operation
        divide() - Performs Division Operation
        get_total_of_all_computations() - Performs the total computations of all calculations

    Attributes:
        __round_off_digit - Stores the round of digit to be used in the computation results
        __number_of_computations - Stores the number of computation done when calculator is started
        __total_result - Stores the total final result of the calculation
        DEFAULT_ROUND_OFF_DIGIT - Constant value of the default round off digit
    """

    # 2) Define class properties (global variables and constants)
    #    -> Properties defined outside methods

    DEFAULT_ROUND_OFF_DIGIT = 2

    # 3) Define the __init__(self, *args, **kwargs) Method
    #    (initialize variables or instance properties -> *args, and **kwargs variables)

    def __init__(self):
        """Initializes the public and private instance properties"""
        self.__round_off_digit = 0
        self.__number_of_computations = 0
        self.__total_result = 0.0

    # 4) Define Instance Methods (private and public methods)

    def __get_number_of_computations(self):
        """Returns the number of computations done

        Returns
            __number_of_computations (int) - Property for the number of computations done
        """

        return self.__number_of_computations

    def __add_to_number_of_computations(self, number):
        """Sets the value of the number of computations done

        Returns
            NoneType
        """
        no_of_computations = self.__number_of_computations + number
        self.__number_of_computations = no_of_computations

    def __get_round_off_digit(self):
        """Returns the value of the round off digit

        Returns
            __round_off_digit (int) - Property for the round off digit used for computation results
        """

        return self.__round_off_digit

    def __set_round_off_digit(self, round_off_digit):
        """Sets the value of the round off digit

        Keyword Arguments
            round_off_digit (int) - Number of decimal places to round the result to (default is 2)

        Returns
            NoneType
        """

        self.__round_off_digit = (
            self.DEFAULT_ROUND_OFF_DIGIT if not round_off_digit else round_off_digit
        )

    def __get_total_result(self):
        """Returns the number of computations done

        Returns
            __number_of_computations (int) - Private property for the number of computations done
        """

        return self.__total_result

    def add(self, *numbers, round_off_digit):
        """Add multiple numbers

        Arguments
            numbers (tuple) - *args: List of input numbers for calculation

        Keyword Arguments:
            round_off_digit (int) - Number of decimal places to round the result to (default is 2)

        Errors
            TypeError - Raised when the input is not a number

        Returns
            result (float) - The sum of all input numbers
        """

        try:
            # Initialize result with the first number
            result = numbers[0]

            # Set the round of digit based from the input value
            self.__set_round_off_digit(round_off_digit)
            round_off_digit = self.__get_round_off_digit()

            for index, number in enumerate(numbers):
                # Debugging line to show the current index and number
                print(f"Number {index + 1} : {number}")

                # Skip the first number since it's already assigned to result
                if index != 0:
                    result += number

            print(f"Round off to: {round_off_digit} digits")

            # Set the values of these private properties:
            # __add_to_number_of_computations & __total_result
            self.__add_to_number_of_computations(1)
            self.__total_result += round(result, round_off_digit)

            return round(result, round_off_digit)

        except TypeError as e:

            raise ValueError(
                f"Error: {e}. \nPlease provide valid numbers for addition."
            ) from e

    def subtract(self, *numbers, round_off_digit):
        """Subtract multiple numbers

        Arguments
            numbers (tuple) - *args: List of input numbers for calculation

        Keyword Arguments
            round_off_digit (int) - Number of decimal places to round the result to (default is 2)

        Errors
            TypeError - Raised when the input is not a number

        Returns
            result (float) - The difference of all input numbers
        """

        try:
            # Initialize result with the first number
            result = numbers[0]

            # Set the round of digit based from the input value
            self.__set_round_off_digit(round_off_digit)
            round_off_digit = self.__get_round_off_digit()

            for index, number in enumerate(numbers):
                # Debugging line to show the current index and number
                print(f"Number {index + 1} : {number}")

                # Skip the first number since it's already assigned to result
                if index != 0:
                    result -= number

            print(f"Round off to: {round_off_digit} digits")

            # Set the values of these private properties:
            # __add_to_number_of_computations & __total_result
            self.__add_to_number_of_computations(1)
            self.__total_result += round(result, round_off_digit)

            return round(result, round_off_digit)

        except TypeError as e:

            raise ValueError(
                f"Error: {e}. \nPlease provide valid numbers for subtraction."
            ) from e

    def multiply(self, *numbers, round_off_digit):
        """Multiply multiple numbers

        Arguments
            numbers (tuple) - *args: List of input numbers for calculation

        Keyword Arguments
            round_off_digit (int) - Number of decimal places to round the result to (default is 2)

        Errors
            TypeError - Raised when the input is not a number

        Returns
            result (float) - The product of all input numbers
        """

        try:
            # Initialize result with the first number
            result = numbers[0]

            # Set the round of digit based from the input value
            self.__set_round_off_digit(round_off_digit)
            round_off_digit = self.__get_round_off_digit()

            for index, number in enumerate(numbers):
                # Debugging line to show the current index and number
                print(f"Number {index + 1} : {number}")

                # Skip the first number since it's already assigned to result
                if index != 0:
                    result *= number

            print(f"Round off to: {round_off_digit} digits")

            # Set the values of these private properties:
            # __add_to_number_of_computations & __total_result
            self.__add_to_number_of_computations(1)
            self.__total_result += round(result, round_off_digit)

            return round(result, round_off_digit)

        except TypeError as e:

            raise ValueError(
                f"Error: {e}. \nPlease provide valid numbers for multiplication."
            ) from e

    def divide(self, *numbers, round_off_digit):
        """Divide multiple numbers

        Arguments
            numbers (tuple) - *args: List of input numbers for calculation

        Keyword Arguments
            round_off_digit (int) - Number of decimal places to round the result to (default is 2)

        Errors
            TypeError - Raised when the input is not a number
            ZeroDivisionError - Raised when attempting to divide by zero

        Returns
            result (float) - The quotient of all input numbers
        """

        try:
            # Initialize result with the first number
            result = numbers[0]

            # Set the round of digit based from the input value
            self.__set_round_off_digit(round_off_digit)
            round_off_digit = self.__get_round_off_digit()

            # Catch Division by zero
            if 0 in numbers[1:]:
                print("Error: Division by zero is not allowed. Try again.")
                self.get_total_of_all_computations(round_off_digit)
                return

            for index, number in enumerate(numbers):
                # Debugging line to show the current index and number
                print(f"Number {index + 1} : {number}")

                # Skip the first number since it's already assigned to result
                if index != 0:
                    result /= number

            print(f"Round off to: {round_off_digit} digits")

            # Set the values of these private properties:
            # __add_to_number_of_computations & __total_result
            self.__add_to_number_of_computations(1)
            self.__total_result += round(result, round_off_digit)

            return round(result, round_off_digit)

        except TypeError as e:

            raise ValueError(
                f"Error: {e}. \nPlease provide valid numbers for division."
            ) from e

    def get_total_of_all_computations(self, round_off_digit):
        """Get the total result of all computations done

        Returns
            str - Displays the total result of all computations done
        """

        # Set the round of digit based from the input value
        self.__set_round_off_digit(round_off_digit)
        round_off_digit = self.__get_round_off_digit()

        # Display the overall total of all computations done
        print("\nDisplaying the summation of all computations done...")
        print(
            f"The overall total of {self.__get_number_of_computations()} computations is: ",
            end="",
        )
        print(round(self.__get_total_result(), round_off_digit))


# 5) Create an instance (object) of the Calculator class
calculator = Calculator()
