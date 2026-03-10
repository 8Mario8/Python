variable = "10, 5, 8, 12, 0, 15, 5, 8"
lista = variable.split(",")

lista = [int(x) for x in lista]
print(lista)

valormax = max(lista)
valormin = min(lista)

lista.remove(valormax)
lista.remove(valormin)

valormedia = round(sum(lista) / len(lista), 2)
print("La media es: ", valormedia)

print(lista)