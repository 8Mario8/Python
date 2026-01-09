#65. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayo y cuál el menor.
mayor = None
menor = None
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
    
    if mayor is None or numero > mayor:
        mayor = numero
    
    if menor is None or numero < menor:
        menor = numero

if mayor is not None and menor is not None:
    print("El número mayor introducido es:", mayor)
    print("El número menor introducido es:", menor)

print("Total de números pares:", pares)
print("Total de números impares:", impares)
print("Total de números positivos:", positivos)
print("Total de números negativos:", negativos)
print("Total de ceros:", ceros)
print("Suma total de todos los números introducidos:", suma_total)
