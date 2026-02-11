numeros = input().split()
<<<<<<< HEAD
if len(numeros) == 1:
    numeros = numeros.append(input())
numeros.split()
=======
if len(numeros) < 2:
    numeros.append(input())
>>>>>>> a3a7f64b99588c89d83d0060d0e91d8ed1d01289
numeros = [int(numero) for numero in numeros]
suma = sum(numeros)
print(suma)