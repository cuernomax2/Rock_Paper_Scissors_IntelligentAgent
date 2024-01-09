import random

# Your existing GameAction class and predetermined_computer_actions function

selection_map = {
    0: 1,
    1: lambda: random.randint(0, 1),
    2: 1
}

def get_computer_action(count):
    # Get the selection or a function to determine the selection
    selection = selection_map.get(count, None)

    # Check if selection is callable (a function) and call it if it is
    if callable(selection):
        selection = selection()

    # If selection is not None, call the predetermined_computer_actions function
    if selection is not None:
        print("hola")

# Example usage
count = 1  # Replace with the actual count
get_computer_action(count)
