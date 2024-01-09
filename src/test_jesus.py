import random

def obtener_numero_aleatorio(escenario):
    num_aleatorio = random.randint(1, 100)
    limite_inferior = 0

    for numero, probabilidad in escenario.items():
        limite_superior = limite_inferior + probabilidad
        if limite_inferior < num_aleatorio <= limite_superior:
            return numero
        limite_inferior = limite_superior

#Definir escenarios con sus respectivos porcentajes
partidas_probabilidades = [
    {1: 40, 2: 30, 3: 30},  # Escenario 1
    {1: 50, 2: 20, 3: 30},  # Escenario 2
    {1: 20, 2: 40, 3: 40},  # Escenario 3
]

#Obtener el número aleatorio basado en el escenario elegido
numero_elegido = obtener_numero_aleatorio(escenarios[0])

print(f"Escenario elegido: {escenarios[0]}")
print(f"El número aleatorio es {numero_elegido}")
