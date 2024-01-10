import random

def obtener_numero_aleatorio(escenario):
    #Número aleatorrio entre 1 y 100
    num_aleatorio = random.randint(1, 100)
    limite_inferior = 0

    
    for numero, probabilidad in escenario.items():
        limite_superior = limite_inferior + probabilidad
        # Comprueba si el número aleatorio generado está dentro del rango actual
        if limite_inferior < num_aleatorio <= limite_superior:
            print(numero)
            return numero
        # Actualiza el límite inferior para la próxima iteración
        limite_inferior = limite_superior
    
    print()

# Escenarios con sus porcentajes, tomando como referencia la imagen adjuntada en el README
game_chances = [
    {0: 26, 1: 51, 2: 23},  # Game 1
    {0: 36, 1: 36, 2: 28},  # Game 2
    {0: 32, 1: 37, 2: 30},  # Game 3
]

obtener_numero_aleatorio(partidas_probabilidades)