#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.
def buscar_palabra(frase, palabra):
frase="A quién madruga Dios ayuda."
palabras=["A", "quién", "Dios", "ayuda", "madruga"]
palabra=input("Introduce una palabra para buscar en la frase: ")
if buscar_palabra(frase, palabra):
    print(f"La palabra '{palabra}' está en la frase.")
else:
    print(f"La palabra '{palabra}' NO está en la frase.")