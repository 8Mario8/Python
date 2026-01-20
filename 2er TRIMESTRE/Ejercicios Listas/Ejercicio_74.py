#73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se repiten y cuales no
lista_1 = ["casa", "mesa", "sal", "sol", "agua"]
lista_2 = ["casa", "luz", "tres", "tren", "sol", "pan"]
lista_2_copy = []
repetidas = []
no_repetidas = []
lista_total = []
lista_total_sin_duplicados = []

lista_total = lista_1.copy()
lista_2_copy = lista_2.copy()

lista_total.extend(lista_2)

for x in lista_total:
    if x in lista_1 and x in lista_2:
        repetidas.append(x)
    
    if x in lista_2 and x not in lista_1:
        no_repetidas.append(x)
    
    if x in lista_1 and x not in lista_2:
        no_repetidas.append(x)

repetidas = list(set(repetidas))
repetidas.sort()
no_repetidas.sort()
print("Están repetidas: ", repetidas)
print("No están repetidas: ", no_repetidas)