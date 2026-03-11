números = input("Introduce 6 números separados por un guión: ")
lista = números.split("-")
lista = [int(x) for x in lista]

# Calcular el valor más grande de la lista y el valor más pequeño de la lista
valormax = max(lista)
valormin = min(lista)

# Calcular el valor promedio de la lista
promedio = round(sum(lista) / len(lista), 4)

# Nueva lista com los valores de la lista mayores al promedio
nueva_lista = []

for j in lista:
    if j > promedio:
        nueva_lista.append(j)

# Mostrar los diferentes resultados
print("Máximo: ", valormax)
print("Mínimo: ", valormin)
print("Promedio: ", promedio)
print("Nueva lista: ", nueva_lista)