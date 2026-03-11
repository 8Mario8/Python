cadena_de_texto = input("Introduce una cadena de texto: ")
lista_palabras = cadena_de_texto.split()
lista_palabras = [str(x) for x in lista_palabras]

# Imprimir la lista de palabras
print("Lista de palabras:", lista_palabras)

# Palabra introducida por el usuario para buscar dentro de la lista de palabras y contar cuántas veces aparece
veces_aparece = 0
palabra_buscada = input("Introduce una palabra para buscar dentro de la lista: ")

for j in lista_palabras:
    if j == palabra_buscada:
        veces_aparece += 1

print("La palabra", palabra_buscada, "aparece", veces_aparece, "veces")

# Unir la lista en un string separada por comas
lista_string = str(lista_palabras)

print(lista_string)