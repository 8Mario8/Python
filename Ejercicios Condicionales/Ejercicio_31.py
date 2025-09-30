#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.
frase="A quién madruga Dios ayuda."
palabras=["quién", "Dios", "ayuda", "madruga", "tarde"]
palabra=input("Introduce una palabra para buscar en la frase: ")

for palabra in palabras:
    indice=frase.find(palabra)
    if indice!=-1:
        print(f"La palabra '{palabra}' se encuentra en el índice {indice}.")
    else:
        print(f"La palabra '{palabra}' no se encuentra en la frase.") 