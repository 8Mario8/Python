#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas
frase="A quién madruga Dios ayuda.".lower()
palabras=["quién", "Dios", "ayuda", "madruga", "tarde"]
palabra=input("Introduce una palabra para buscar en la frase: ").lower()
for palabra in palabras:
    indice=frase.find(palabra.lower())
    if indice!=-1:
        print(f"La palabra '{palabra}' se encuentra en el índice {indice}.")
    else:
        print(f"La palabra '{palabra}' no se encuentra en la frase.")