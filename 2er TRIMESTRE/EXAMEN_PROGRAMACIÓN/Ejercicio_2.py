import random

print("TEST MULTIPLICACIONES")
multiplicaciones = 0

# a) Numero de multiplicaciones en el test
num_multi = input("Introduce el número de multiplicaciones que quieres que haya en el test: ")

while not num_multi > 0:
    num_multi = input("Introduce el número de multiplicaciones que quieres que haya en el test: ")

# c) Rango de números aleatorios para la multiplicación
rango_num = input("Introduce los dos numeros que marcaran el rango de los numeros de las multiplicación: ")

while not len(rango_num) == 2:
    rango_num = input("Introduce los dos numeros que marcaran el rango de los numeros de las multiplicación: ")

rango_num.split(",")

# f) Numero de factores de las multiplicaciones
num_factores = input("Introduce el numero de factores en la multiplicación (2 o 3): ")

while not num_factores == 2 and not num_factores == 3:
    num_factores = input("Introduce el numero de factores en la multiplicación (2 o 3): ")


while multiplicaciones < num_multi:
    num1 = random.randint(rango_num)
    num2 = random.randint(rango_num)
    
    if num_factores == 3:
        num3 = random.randint(rango_num)