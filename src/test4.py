import json

with open('result.json', 'r') as file:
    data = json.load(file)

game_history = data['history']

count = {0: 0, 1: 0, 2: 0}

for game in game_history:
    player1_input = game['player1']
    if player1_input in count:
        count[player1_input] += 1

total_inputs = sum(count.values())
percentages = {k: (v / total_inputs) * 100 for k, v in count.items()}

print(percentages)
