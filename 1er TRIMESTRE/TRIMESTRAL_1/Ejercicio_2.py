# Nombrar variables
suma_positivos=0
suma_negativos=0

# Bucle para que el usuario introduzca 6 números por pantalla
for i in range(6):
    num=int(input("Introduce un número: "))

# Sumar los numeros que sean positivos y los numeros que sean negativos
    if num>=0:
        suma_positivos=suma_positivos+num
    else:
        suma_negativos=suma_negativos+num

# Mostrar la solución
print("Suma de números positivos:", suma_positivos)
print("Suma de números negativos:", suma_negativos)