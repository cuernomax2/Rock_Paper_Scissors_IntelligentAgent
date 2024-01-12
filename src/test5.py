import json

with open('result.json', 'r') as file:
    data = json.load(file)

game_history = data['history']

count = {0: 0, 1: 0, 2: 0}

for game in game_history:
    result_input = game['result']
    if result_input in count:
        count[result_input] += 1

total_inputs = sum(count.values())
percentages = {k: (v / total_inputs) * 100 for k, v in count.items()}

print(percentages) #{0 = user wins, 1 = computer wins, 2 = draw}
#Print the percentages of win/lose/draw