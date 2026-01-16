#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y no deben almacenarse en la lista
letras = []
repetir = "s"

while repetir == "s":
    letra = input("Introduce una letra: ")

    while not len(letra) == 1 or not letra.isalpha():
        letra = input("Introduce una letra: ")

    letra.lower()

    if letra == "á":
        letra == "a"

    if letra == "à":
        letra == "a"
    
    if letra == "é":
        letra == "e"

    if letra == "è":
        letra == "e"
    
    if letra == "í":
        letra == "i"

    if letra == "ì":
        letra == "i"

    if letra == "ó":
        letra == "o"

    if letra == "ò":
        letra == "o"

    if letra == "ú":
        letra == "u"

    if letra == "ù":
        letra == "u"

    letras.append(letra)

    repetir = input("¿Deseas repetir? s/n ")

    while not repetir == "s" and not repetir == "n":
        repetir = input("¿Deseas repetir? s/n ")

letras = list(set(letras))
letras.sort()
print(letras)