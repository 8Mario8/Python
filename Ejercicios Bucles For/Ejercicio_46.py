#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.
palabra=input("Introduce una palabra: ")
vocales="aeiou"
consonantes="bcdfghjklmnñpqrstvwxyz"
for i in range(len(palabra.lower())):
    if vocales in palabra:
        print("Las vocales de la palabra ", palabra, "son: ", vocales)
    if consonantes in palabra:
        print("Las consonantes de la palabra ", palabra, "son: ", consonantes)