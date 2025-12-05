#60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. Utiliza únicamente el while
numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
contador = 1
while contador <= 10:
    resultado = numero * contador
    print(numero, "x", contador, "=", resultado)
    contador += 1