from datetime import datetime


def get_valid_input(prompt, optional=False):
    while True:
        user_input = input(prompt).strip()
        if optional and not user_input:
            return None
        if user_input:
            return user_input
        print("Input cannot be empty, try again.")


def get_date_input(prompt):
    while True:
        date_input = input(prompt).strip()
        if not date_input:
            return None
        try:
            datetime.strptime(date_input, '%Y-%M-%D')
            return date_input
        except ValueError:
            print("Invalid date format. Please enter in MM-DD-YYYY format.")