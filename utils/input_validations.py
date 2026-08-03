"""Functions for the calculator program."""

# Create a function "get_user_choice" with parameter "message".
# Add an error exception to catch errors for non Yes/No responses


def get_user_choice(message):
    """Repeatedly prompts user until a valid yes/no response is given

    Arguments:
        message (str) - The prompt message to display to the user

    Errors:
        ValueError - Raised when the input is not a valid Yes/No response

    Returns:
        answer (str) - A valid Yes or No response entered by the user
    """

    while True:
        try:
            # Check if the answer is "Yes" or "No" value
            answer = input(message).strip().lower()

            if answer in ["yes", "no"]:
                return answer

            raise ValueError(
                "Invalid response. Please answer with 'Yes' or 'No' only!\n"
            )

        except ValueError as e:
            # If a ValueError is caught (invalid input), print an error message
            print(e)


# Create a function "get_operation" with parameter "message".
# Add an error exception to catch errors for invalid operations (+, -, *, /) responses


def get_operation(message):
    """Repeatedly prompts user until a valid operation input is given

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
                "Invalid operation. Please enter one of these operations (+, -, *, /) only.\n"
            )

        except ValueError as e:
            # If a ValueError is caught (invalid input), print an error message
            print(e)


# Create a function "get_number_list_input" with parameter "message".
# Add an error exception to catch errors for non-numeric input


def get_number_list_input(message):
    """Repeatedly prompts user until a valid list of numeric inputs are given

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

            # If the str to float conversion succeeds, return the list
            return number_list

        except ValueError:
            # If a ValueError is caught (non-numeric input), print an error message
            print(
                "Invalid input. Please enter only valid numeric numbers separated by commas."
            )


# Create a function "get_round_off_digit" with parameter "message".
# Add an error exception to catch errors for non-integer input


def get_round_off_digit(message):
    """Repeatedly prompts user until a valid integer input is given.
    Accepts empty value and use the default value of the round of digit.

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
            user_input = input(message)

            if user_input == "":
                return user_input

            round_off_digit = int(user_input)

            # If the str to integer conversion succeeds, return the integer
            return round_off_digit

        except ValueError:
            # If a ValueError is caught (non-integer input), print an error message
            print("Invalid input. Please enter a valid integer for round off digit.")
