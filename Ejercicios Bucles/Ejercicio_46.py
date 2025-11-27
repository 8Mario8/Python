#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.
palabra=input("Introduce una palabra: ")
vocales="aeiou"
consonantes="bcdfghjklmnñpqrstvwxyz"
vocales_encontradas = []
consonantes_encontradas = []
for i in range(len(palabra)):
    if palabra[i].lower() in vocales:
        vocales_encontradas.append(palabra[i])
    if palabra[i].lower() in consonantes:
        consonantes_encontradas.append(palabra[i])
print("Las vocales de la palabra ", palabra, "son: ", vocales_encontradas)
print("Las consonantes de la palabra ", palabra, "son: ", consonantes_encontradas)