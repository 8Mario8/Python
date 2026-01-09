#39.  Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0.
num_numeros = float(input("Introduce el número de números que deseas introducir: "))
if num_numeros != int(num_numeros):
    print("Error")
else:
    positivos = 0
    negativos = 0
    ceros = 0
    for i in range(int(num_numeros)):
        numero = float(input("Introduce un número: "))
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            ceros += 1
    print("Números positivos: ", positivos)
    print("Números negativos: ", negativos)
    print("Números cero: ", ceros)