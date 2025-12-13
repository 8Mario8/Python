#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa debe controlar si el usuario introduce un número no comprendido entre 1 y 5

import random
numero_aleatorio = random.randint(1, 5)
numero_usuario = 0

while numero_usuario < 1 or numero_usuario > 5:
    numero_usuario = int(input("Introduce un número entre 1 y 5: "))

    if numero_usuario < 1 or numero_usuario > 5:
        print("Número no válido. Por favor, inténtalo de nuevo.")
        
if numero_usuario == numero_aleatorio:
    print("¡Felicidades! Has adivinado el número.")
else:
    print("Lo siento, el número era", numero_aleatorio)