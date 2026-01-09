#61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es superior o igual a 40.

numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
contador = 1

while contador <= 10:
    resultado = numero * contador
    print(numero, "x", contador, "=", resultado)
    contador += 1
    
    if resultado >= 40:
        print("El resultado ha superado o igualado 40, fin del programa.")
        contador = 11  # Ajustar el contador para salir del bucle