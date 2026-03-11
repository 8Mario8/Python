valores = input("Introduce los valores en una línea: ")
lista = valores.split("-")

# Valores numéricos dentro de la lista
valores_numericos = []

for x in lista:
    if x.isnumeric():
        valores_numericos.append(x)

print("Valores numéricos antes de eliminar duplicados:", valores_numericos)

# Suma total
suma_total = 0
valores_numericos = [int(j) for j in valores_numericos]

suma_total = sum(valores_numericos)
print("Suma total antes de eliminar duplicados:", suma_total)

# Valores numéricos sin duplicados
valores_numericos_sinduplicados = set(valores_numericos)
valores_numericos_sinduplicados = sorted(valores_numericos_sinduplicados)

print("Valores numéricos después de eliminar duplicados:", valores_numericos_sinduplicados)

# Suma total sin duplicados
suma_total_sinduplicados = sum(valores_numericos_sinduplicados)
print("Suma total después de eliminar duplicados:", suma_total_sinduplicados)

# Valores no numéricos dentro de la lista
valores_no_numéricos = []

for i in lista:
    if not i.isnumeric():
        valores_no_numéricos.append(i)

print("Valores no numéricos antes de eliminar duplicados:", valores_no_numéricos)

# Valores no numéricos después de eliminar duplicados
valores_no_numéricos_sinduplicados = set(valores_no_numéricos)
valores_no_numéricos_sinduplicados = sorted(valores_no_numéricos_sinduplicados)

print("Valores no numéricos después de eliminar duplicados:", valores_no_numéricos_sinduplicados)