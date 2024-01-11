from enum import IntEnum
import json

with open('result.json', 'r') as file:
    data = json.load(file)
    
game_history = data['history']

for game in game_history:
    game_number = game['game number']
    player1 = game['player1']
    player2 = game['player2']
    result = game['result']

    print (player1)