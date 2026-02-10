numeros = input().split()
if len(numeros) < 3:
    input_value = input()
    if input_value != "":
        numeros.append(input_value)
    else:
        numeros.append(input())
numeros = [int(numero) for numero in numeros]
suma = sum(numeros)
print(suma)