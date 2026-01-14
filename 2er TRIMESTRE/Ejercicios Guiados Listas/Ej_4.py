lista_numeros_1 = []
lista_numeros_2 = []
lista_no_numeros_1 = []
lista_no_numeros_2 = []
lista_todo_1 = []
lista_todo_2 = []

frase = input("Introduce valores separados por un guion: ")

lista_todo_1 = frase.split("-")
lista_todo_2 = frase.split("-")

for x in range(len(lista_todo_1)):
    if lista_todo_1 [x].isnumeric():
        lista_numeros_1.append(int(lista_todo_1 [x]))
    else:
        lista_no_numeros_1.append(lista_todo_1 [x])

print(lista_numeros_1)
print(lista_no_numeros_1)

for x in lista_todo_2:
    if x.isnumeric():
        lista_numeros_2.append(int(x))
    else:
        lista_no_numeros_2.append(x)

print(lista_numeros_2)
print(lista_no_numeros_2)

print(sum(lista_numeros_1))
print(sum(lista_numeros_2))