#4. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas: 
##  a) total de pares 
##  b) total de impares 
##  c) total de números positivos 
##  d) total de números negativos 
##  e) total de ceros 
##  f) total de la suma de todos los números introducidos

pares = 0
impares = 0
positivos = 0
negativos = 0
ceros = 0
suma_total = 0

while True:
    numero = int(input("Introduce un número (-99 para finalizar): "))

    if numero == -99:
        break
    suma_total += numero

    if numero == 0:
        ceros += 1
    elif numero > 0:
        positivos += 1

        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    else:
        negativos += 1

        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
            
print("Total de números pares:", pares)
print("Total de números impares:", impares)
print("Total de números positivos:", positivos)
print("Total de números negativos:", negativos)
print("Total de ceros:", ceros)
print("Suma total de todos los números introducidos:", suma_total)