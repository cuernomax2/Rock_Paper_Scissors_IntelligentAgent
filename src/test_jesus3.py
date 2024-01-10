def get_computer_action(partida):
    
    if partida == 0 or partida == 1 or partida == 2:

        computer_selection = obtener_numero_aleatorio(partidas_probabilidades[partida])
        computer_action = GameAction(computer_selection)
        print(f"Computer picked 1 {computer_action.name}.")
        
    else:

        # Path to your JSON file 
        json_file_path = 'result.json'

        # Read the JSON data 
        with open(json_file_path, 'r') as file: 
            data = json.load(file)
        
        game_record = data['record']
        
        # Resultado última partida
        for game in game_record:
            player1 = game['player1']
            player2 = game['player2']
            result = game['result']

        if result == 0:
            computer_action = GameAction(random.randint(0, 1))
            print(f"Computer picked {computer_action.name}.")
        else:
            if player1 == 0:
                computer_action = GameAction(1)
            elif player1 == 1:
                computer_action = GameAction(2)
            elif player1 == 2:
                computer_action = GameAction(0)
            print(f"Computer picked {computer_action.name}.")

    return computer_action