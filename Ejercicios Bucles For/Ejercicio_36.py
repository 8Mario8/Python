#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario.
n = int(input("Introduce un número natural n: "))
suma = 0
for i in range(1, n + 1):
    suma += i
print("La suma de los ", n, " primeros números naturales es: ", suma)