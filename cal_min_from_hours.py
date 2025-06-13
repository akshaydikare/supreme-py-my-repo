# prompt: Write me python code to run on Console or terminal, which taken user input as number and calculate the number of minutes with given input number. Create python functions,  Add try except blocks, write neat and clean. Add validation for if input number is 0 or negative or text of float. The input number must be a number.

def calculate_minutes(hours):
    """
    Calculates the number of minutes in a given number of hours.

    Args:
        hours: The number of hours (must be a positive number).

    Returns:
        The number of minutes in the given hours.
    """
    return hours * 60

def get_valid_hours_input():
    """
    Prompts the user to enter a number of hours and validates the input.

    Returns:
        A valid positive number representing hours.
    """
    while True:
        try:
            user_input = input("Enter the number of hours: ")
            hours = float(user_input)

            if hours <= 0:
                print("Input must be a positive number.")
            else:
                return hours
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    # This block runs only when the script is executed directly (not imported)
    print("--- Hours to Minutes Converter ---")

    valid_hours = get_valid_hours_input()
    minutes = calculate_minutes(valid_hours)

    # Format output to handle potential floating point minutes
    if minutes.is_integer():
        print(f"{valid_hours} hours is equal to {int(minutes)} minutes.")
    else:
        print(f"{valid_hours} hours is equal to {minutes} minutes.")
