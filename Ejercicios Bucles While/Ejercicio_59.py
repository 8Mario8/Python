#59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe mostrarse por pantalla un mensaje y el número de intentos.
import random
numero_aleatorio = random.randint(0, 1000)
numero_usuario = -1
intentos = 0
while numero_usuario != numero_aleatorio:
    numero_usuario = int(input("Introduce un número entre 0 y 1000: "))
    intentos += 1
    if numero_usuario < numero_aleatorio:
        print("El número es mayor.")
    elif numero_usuario > numero_aleatorio:
        print("El número es menor.")
    else:
        print("¡Felicidades! Has adivinado el número en", intentos, "intentos.")