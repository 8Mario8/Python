#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while

import random

numero_aleatorio = random.randint(1, 5)
numero_usuario = 0
intentos = 0

while numero_usuario != numero_aleatorio and intentos < 3:
    numero_usuario = int(input("Introduce un número entre 1 y 5: "))
    
    if numero_usuario < 1 or numero_usuario > 5:
        print("Número no válido. Por favor, inténtalo de nuevo.")
    elif numero_usuario == numero_aleatorio:
        print("¡Felicidades! Has adivinado el número.")
    else:
        intentos += 1
        
        if intentos < 3:
            print("Número incorrecto. Inténtalo de nuevo.")
        elif intentos == 3:
            print("Lo siento, has agotado tus intentos. El número era", numero_aleatorio)