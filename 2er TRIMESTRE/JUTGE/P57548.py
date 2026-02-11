numeros = input().split()
if len(numeros) == 1:
    numeros = numeros.append(input())
numeros.split()
numeros = [int(numero) for numero in numeros]
suma = sum(numeros)
print(suma)