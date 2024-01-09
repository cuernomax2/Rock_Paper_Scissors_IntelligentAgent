import random
from enum import IntEnum
import json


class GameAction(IntEnum):

    Rock = 0
    Paper = 1
    Scissors = 2


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


Victories = {
    GameAction.Rock: GameAction.Paper,
    GameAction.Paper: GameAction.Scissors,
    GameAction.Scissors: GameAction.Rock
}

def assess_game(user_action, computer_action):

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

#--------------------------------
def get_computer_action():
    computer_selection = random.randint(0, len(GameAction) - 1)
    computer_action = GameAction(computer_selection)
    print(f"Computer picked {computer_action.name}.")

    return computer_action


def get_computer_action(selection_num):
    selection_map = {0: 1,  1: lambda: random.randint(0, 1),  2: 1}

    selection = selection_map.get(selection_num, None)

    if callable(selection):
        selection = selection()
    
    # If selection is not None, call the predetermined_computer_actions function
    if selection <=2:
        computer_action = selection
    else:
        computer_action = get_computer_action()

    return computer_action
#-------------------------------------------

def get_user_action():
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}) --> "))
    user_action = GameAction(user_selection)

    return user_action


def play_another_round():
    another_round = input("\nAnother round? (y/n) --> ")
    while (another_round != "y") and (another_round != "n"):
        another_round = input("\nInvalid selection. Please insert yes (y) or no (n) or press CTRL+C to exit --> ")
    return another_round.lower() == 'y'


def main():

    selection_num = 0 #variable used to read the selection_map on get_computer_action()

    while True:
        try:
            player1 = get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        try:
            with open('result.json', 'r') as f:
                match_history = json.load(f)
        except FileNotFoundError:
            match_history = {"history": []}

        player2 = get_computer_action(selection_num)
        result = assess_game(player1, player2)

        selection_num += 1

        match_info = {"player1": player1, "player2": player2, "result": result}

        match_history = ["historial"].append(match_info)

        # Save the results to a file
        with open('result.json', 'w') as f:
            json.dump(match_history, f, indent=4)

        if not play_another_round():
            break


if __name__ == "__main__":
    main()
