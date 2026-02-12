import math
numero_real = str(input())
if not numero_real.isdecimal():
    numero_real = float(numero_real)
    numero_sin_decimales_inferior = int(numero_real)
    numero_sin_decimales_superior = int(numero_real) + 1
    entera = int(numero_real)
    decimal = numero_real - entera
    if decimal >= 0.5:
        numero_redondeado = entera + 1
    else:
        numero_redondeado = entera
else:
    numero_sin_decimales_inferior = int(numero_real)
    numero_sin_decimales_superior = int(numero_real)
    numero_redondeado = int(numero_real)
print(numero_sin_decimales_inferior, numero_sin_decimales_superior, numero_redondeado)