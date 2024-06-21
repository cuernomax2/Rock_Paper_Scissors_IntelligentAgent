import random
from enum import IntEnum
import json
import os


class GameAction(IntEnum): #Unchanged Class
    Rock = 0
    Paper = 1
    Scissors = 2


class GameResult(IntEnum): #Unchanged Class
    Victory = 0
    Defeat = 1
    Tie = 2


Victories = { #Unchanged Dictionary
    GameAction.Rock: GameAction.Paper,
    GameAction.Paper: GameAction.Scissors,
    GameAction.Scissors: GameAction.Rock
}

def assess_game(user_action, computer_action): #Unchanged Function
    game_result = None

    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        game_result = GameResult.Tie

    # You picked Rock
    elif user_action == GameAction.Rock:
        if computer_action == GameAction.Scissors:
            print("Rock smashes scissors. You won!")
            game_result = GameResult.Victory
        else:
            print("Paper covers rock. You lost!")
            game_result = GameResult.Defeat

    # You picked Paper
    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock:
            print("Paper covers rock. You won!")
            game_result = GameResult.Victory
        else:
            print("Scissors cuts paper. You lost!")
            game_result = GameResult.Defeat

    # You picked Scissors
    elif user_action == GameAction.Scissors:
        if computer_action == GameAction.Rock:
            print("Rock smashes scissors. You lost!")
            game_result = GameResult.Defeat
        else:
            print("Scissors cuts paper. You won!")
            game_result = GameResult.Victory

    return game_result

#------------------------------- Algorithm used by the computer -------------------------
def predetermined_computer_action(selection_num):
    game_chances = [ #Probabilities for each action based on the model to counter the most common first actions from user
        {0: 26, 1: 51, 2: 23},  # Chances of Game 1
        {0: 36, 1: 36, 2: 28},  # Chances of Game 2
        {0: 32, 1: 37, 2: 30},  # Chances of Game 3
    ]

    if selection_num <= 2:
        #Get the probabilities for the corresponding game
        probabilities = game_chances[selection_num]

        #Generate a random action based on these probabilities
        actions, weights = zip(*probabilities.items())
        user_action = random.choices(actions, weights=weights, k=1)[0]

        #Print what action the computer picked
        computer_action = GameAction(user_action)
        print(f"Computer picked {computer_action.name}.")
    else:
        #Call random selection script get_computer_action()
        user_action = get_computer_action()

    return user_action


def get_computer_action():
    data = json_read()
    match_history = data['history']

    #Initialize a counter for each user1 input value
    actions_count = {0: 0, 1: 0, 2: 0}

    #Count how many times each individual value has appeared
    for game in match_history:
        player1_input = game['player1']
        if player1_input in actions_count:
            actions_count[player1_input] += 1

    total_games = sum(actions_count.values())

    #Probability for each choice
    probabilities = {choice: actions_count[choice]/total_games for choice in actions_count}

    #Decide the computer's action based on "probabilities"
    computer_action = random.choices(
        population=[(key + 1) % 3 for key in actions_count],  #Next action in the sequence
        weights=probabilities.values(),
        k=1
    )[0]

    computer_action = GameAction(computer_action)
    print(f"Computer picked {computer_action.name}.")

    return computer_action
#------------------------------- End of the algorithm used by the computer ----------------

def get_user_action():
    #Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}) --> "))
    user_action = GameAction(user_selection)
    print(f"You picked {user_action.name}.")

    return user_action


def play_another_round(): #
    another_round = input("\nAnother round? (y/n) --> ")
    while (another_round != "y") and (another_round != "n"):
        another_round = input("\nInvalid selection. Please insert yes (y) or no (n) or press CTRL+C to exit --> ")
    return another_round.lower() == 'y'


def json_read(): #Reads result.json. If it doesn't exist, creates it. Returns a dictionary
    try:
        with open('result.json', 'r') as f:
            match_history = json.load(f)
            if not isinstance(match_history, dict) or "history" not in match_history:
                match_history = {"history": []}
    except (FileNotFoundError):
        match_history = {"history": []}
    return match_history


def json_dump(match_history): #Retrieves the "match_history" dictionary and dumps it into result.json
        with open('result.json', 'w') as f:
            json.dump(match_history, f, indent=4)


def main():
    selection_num = 0 #Variable used to read the selection_map on function get_computer_action() (This is done in order to check what game the user is currently in)

    while True:
        try: #Gets user input
            player1 = get_user_action()
        except ValueError: #If input was incorrect do not continue until input is correct
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        player2 = predetermined_computer_action(selection_num) #Call predetermined_computer_action() and store it in "player2"
        result = assess_game(player1, player2) #Call assess_game() using "player1 and player2" and store it in "result"

        selection_num += 1 #After all the choices (both user's and bot's) are done add +1 (match nº1, nº2, etc)

        match_info = {"game number": selection_num, "player1": player1, "player2": player2, "result": result} #Save the results of each individual game in a dictionary

        match_history = json_read() #Call json_read() and store the dictionary returned by the function into "match_history"

        match_history["history"].append(match_info) #Insert the match_info dictionary into match_history cariable

        json_dump(match_history) #Call json_dump using "match_history" as a parameter

        if not play_another_round(): #Call play_another_round(). If return is False ("n") then break and exit
            print("Thanks for playing :) Goodbye user")
            break


if __name__ == "__main__":
    main()
