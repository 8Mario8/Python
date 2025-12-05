#62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el último número: "))

if num1 < num2:
    inicio = num1
    fin = num2
elif num2 < num1:
    inicio = num2
    fin = num1
else:
    inicio = num1
    fin = num2

print("Números pares en el rango:")
pares = [str(i) for i in range(inicio, fin + 1) if i % 2 == 0]
print("-".join(pares))

print("\nNúmeros impares en el rango:")
impares = [str(i) for i in range(inicio, fin + 1) if i % 2 != 0]
print("-".join(impares))