#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.
def buscar_palabra(frase, palabra):
    palabras = frase.replace('.', '').split()
    if palabra in palabras:
        return palabras.index(palabra)
    else:
        return -1
frase = "A quién madruga Dios ayuda."
palabra = input("Introduce una palabra para buscar en la frase: ")
indice = buscar_palabra(frase, palabra)
if indice != -1:
    print(f"La palabra '{palabra}' está en la frase en la posición {indice}.")
else:
    print(f"La palabra '{palabra}' NO está en la frase.")