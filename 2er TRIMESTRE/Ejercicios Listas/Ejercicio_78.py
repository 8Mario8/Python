#78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir
lista_1 = ["a", "b", "D", "x", "r", "X", "3", "h", "w", "2", "i"]
repetir = "s"

while repetir == "s":

    print(lista_1)
    
    suprimir_valor = input("Introduce el valor de la lista que deseas eliminar: ")

    if suprimir_valor.isnumeric():

        if suprimir_valor in lista_1:
            lista_1.remove(suprimir_valor)
        else:
            print("El valor tiene que estar dentro de la lista")

    if not suprimir_valor.isnumeric():
        print("El valor tiene que ser numérico")

    repetir = input("Deseas eliminar otro valor s/n: ")

    if not repetir == "s" and not repetir == "n":
        repetir = input("s/n? ")
    
    if repetir == "n":
        break