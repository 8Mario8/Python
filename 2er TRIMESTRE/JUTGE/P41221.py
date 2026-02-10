numeros = input().split()
if len(numeros) < 3:
    numeros.append(input())
numeros = [int(numero) for numero in numeros]
suma = sum(numeros)
print(suma)