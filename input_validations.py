"""Functions for the calculator program."""

# Create a function "check_answer" with parameter "message".
# Add an error exception to catch errors for non Yes/No response


def check_answer(message):
    """Checks if the user input is a valid Yes/No response

    Arguments:
        message (str) - The prompt message to display to the user

    Errors:
        ValueError - Raised when the input is not a valid operation

    Returns:
        answer (str) - A valid Yes or No response entered by the user
    """
    while True:
        try:
            # Check if the answer is "Yes" or "No" value
            answer = input(message).strip().lower()

            if answer in ["yes", "no"]:
                return answer

            raise ValueError("Invalid response. Please enter 'Yes' or 'No' only!\n")

        except ValueError as e:
            # If a ValueError is caught (invalid operation input), print an error message
            print(e)


# Create a function "check_operation" with parameter "message".
# Add an error exception to catch errors for invalid operations (+, -, *, /)


def check_operation(message):
    """Repeatedly prompts user for an operation until valid input is received

    Arguments:
        message (str) - The prompt message to display to the user

    Errors:
        ValueError - Raised when the input is not a valid operation

    Returns:
        operation (str) - A valid operation entered by the user (+, -, *, /)
    """

    while True:
        try:
            # Check if the input is a valid operation
            operation = input(message)

            if operation in ["+", "-", "*", "/"]:
                return operation

            raise ValueError(
                "Invalid operation. Please enter one of operations (+, -, *, /).\n"
            )

        except ValueError as e:
            # If a ValueError is caught (invalid operation input), print an error message
            print(e)


# Create a function "get_number_list_input" with parameter "message".
# Add an error exception to catch errors for non-numeric input


def get_number_list_input(message):
    """Repeatedly prompts user for a list of numbers until valid input is received

    Arguments:
        message (str) - The prompt message to display to the user

    Errors:
        ValueError - Raised when the input is not a valid number

    Returns:
        number_list (list) - A list of valid float and integer numbers entered by the user
    """

    while True:
        try:
            # Get user input for multiple numbers
            user_input = input(message)

            # Split the input string by commas and convert each part to a float
            number_list = [float(num.strip()) for num in user_input.split(",")]

            # If the conversion succeeds, break the loop and return the list
            return number_list

        except ValueError:
            # If a ValueError is caught (non-numeric input), print an error message
            print(
                "Invalid input. Please enter valid float and integer numbers separated by commas."
            )


# Create a function "get_round_off_digit" with parameter "message".
# Add an error exception to catch errors for non-integer input


def get_round_off_digit(message):
    """Repeatedly prompts user for a round off digit until valid input is received

    Arguments:
        message (str) - The prompt message to display to the user

    Errors:
        ValueError - Raised when the input is not a valid integer

    Returns:
        round_off_digit (int) - A valid integer input for round off digit
    """

    while True:
        try:
            # Get user input for round off digit
            round_off_digit = int(input(message))

            # If the conversion succeeds, break the loop and return the integer
            return round_off_digit

        except ValueError:
            # If a ValueError is caught (non-integer input), print an error message
            print("Invalid input. Please enter a valid integer for round off digit.")
