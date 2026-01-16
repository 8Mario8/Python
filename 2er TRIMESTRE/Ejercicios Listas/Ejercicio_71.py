#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas.
letras = []
repetir = "s"

while repetir == "s":
    letra = input("Introduce una letra: ")

    while not len(letra) == 1 or not letra.isalpha():
        letra = input("Introduce una letra: ")

    letras.append(letra)

    repetir = input("¿Deseas repetir? s/n ")

    while not repetir == "s" and not repetir == "n":
        repetir = input("¿Deseas repetir? s/n ")

letras = list(set(letras))
letras.sort()
print(letras)