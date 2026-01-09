#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas
def buscar_palabra(frase, palabra):
    palabras = frase.replace('.', '').lower().split()
    palabra = palabra.lower()
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