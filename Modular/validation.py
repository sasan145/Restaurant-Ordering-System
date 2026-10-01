def get_valid_yes_no(message):
    """Gets a valid yes/no response from the user."""

    while True:
        answer = input(message).strip().lower()

        if answer == "yes":
            return True

        if answer == "no":
            return False

        print("Invalid input. Please enter yes or no.")
