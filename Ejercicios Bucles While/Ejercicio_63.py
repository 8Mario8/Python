#63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número de veces que se repite cada número.

import random

tiradas = 0
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0
contador6 = 0

while tiradas < 100:
    dado = random.randint(1, 6)
    tiradas += 1
    
    if dado == 1:
        contador1 += 1
    elif dado == 2:
        contador2 += 1
    elif dado == 3:
        contador3 += 1
    elif dado == 4:
        contador4 += 1
    elif dado == 5:
        contador5 += 1
    elif dado == 6:
        contador6 += 1

print("El número 1 ha salido", contador1, "veces.")
print("El número 2 ha salido", contador2, "veces.")
print("El número 3 ha salido", contador3, "veces.")
print("El número 4 ha salido", contador4, "veces.")
print("El número 5 ha salido", contador5, "veces.")
print("El número 6 ha salido", contador6, "veces.")