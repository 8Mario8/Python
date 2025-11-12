#45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string distinguiendo vocales y las consonantes:
palabra=input("Introduce una palabra: ")
vocales="aeiou"
consonantes="bcdfghjklmnñpqrstvwxyz"
for i in range(len(palabra)):
    if vocales in palabra:
        print("Las vocales de la palabra ", palabra, "son: ", vocales)
    if consonantes in palabra:
        print("Las consonantes de la palabra ", palabra, "son: ", consonantes)