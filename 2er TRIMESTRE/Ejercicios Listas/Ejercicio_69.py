#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números ordenados de menor a mayor.
numeros = []
cantidad_numeros_introducidos = 0
num = 0

cantidad_numeros = int(input("Introduce la cantidad de números que quieres introducir: "))

while cantidad_numeros_introducidos < cantidad_numeros:
    num = int(input("Introduce un número entero para añadir a la lista: "))

    numeros.append(int(num))
    
    cantidad_numeros_introducidos = cantidad_numeros_introducidos + 1

numeros.sort()
print(numeros)