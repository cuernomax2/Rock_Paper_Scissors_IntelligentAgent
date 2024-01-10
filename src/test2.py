import random

def predetermined_computer_action(selection_num):
    game_chances = [
        {0: 26, 1: 51, 2: 23},  # Chances of Game 1
        {0: 36, 1: 36, 2: 28},  # Chances of Game 2
        {0: 32, 1: 37, 2: 30},  # Chances of Game 3
    ]

    if 0 <= selection_num < len(game_chances):
        # Get the probabilities for the corresponding game
        probabilities = game_chances[selection_num]

        # Generate a random action based on these probabilities
        actions, weights = zip(*probabilities.items())
        selection = random.choices(actions, weights=weights, k=1)[0]
    else:
        # If selection_num is not a valid game number, return a default action or handle error
        selection = 0  # Or any other default action or error handling

    # Assuming GameAction is a class or enum you have defined elsewhere
    print (selection)
    print (probabilities)
    return selection

# Example usage
predetermined_computer_action(0)  # For the first game
predetermined_computer_action(1)  # For the second game
predetermined_computer_action(2)  # For the third game
