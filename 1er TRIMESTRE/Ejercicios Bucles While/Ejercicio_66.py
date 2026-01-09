#66. Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo se comporta el dado en lanzamientos producidos durante aprox 3 segundos.

import random
import time

inicio = time.time()
uno = 0
dos = 0
tres = 0
cuatro = 0
cinco = 0
seis = 0

while time.time() - inicio < 3:
    resultado = random.randint(1, 6)

    if resultado == 1:
        uno += 1
    elif resultado == 2:
        dos += 1
    elif resultado == 3:
        tres += 1
    elif resultado == 4:
        cuatro += 1
    elif resultado == 5:
        cinco += 1
    else:
        seis += 1
        
print("Tiempo:", time.time() - inicio)
print("Uno:", uno)
print("Dos:", dos)
print("Tres:", tres)
print("Cuatro:", cuatro)
print("Cinco:", cinco)
print("Seis:", seis)