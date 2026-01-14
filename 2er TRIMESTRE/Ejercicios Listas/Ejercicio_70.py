#70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el formato de entrada y salida tal y como se muestra en el testeo.
lista_1 = []
lista_2 = []
cantidad_palabras_introducidas = 0
palabra = 0

cantidad_palabras = int(input("Introduce la cantidad de palabras que quieres introducir: "))

while cantidad_palabras_introducidas < cantidad_palabras:
    palabra = input("Introduce una palabra para añadir a la lista: ")

    lista_1.append(palabra)
    lista_2.append(palabra)

    cantidad_palabras_introducidas = cantidad_palabras_introducidas + 1

lista_1.sort()
lista_2.sort(reverse = True)
print("La lista 1 contiene:", lista_1)
print("La lista 2 contiene:", lista_2)