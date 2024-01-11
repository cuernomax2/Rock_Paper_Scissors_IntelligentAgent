from enum import IntEnum
import json

#Read the result.json data from the file
with open('result.json', 'r') as file:
    data = json.load(file)

#Accessing the 'historial' key from the dictionary
game_history = data['history']

#Processing the game history
for game in game_history:
    game_number = game['game number']
    player1 = game['player1']
    player2 = game['player2']
    result = game['result']

    print (player1)