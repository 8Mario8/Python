#33. Programa un código que permita contar el número de vocales de la siguiente frase: No hay mal que dure cien años
frase="No hay mal que dure cien años"
vocales="aeiouAEIOU"
contador=0
for letra in frase:
    if letra in vocales:
        contador+=1
        print(f"El número total de vocales es {contador}")
        for v in "aeiou":
            print(f"El número de {v} es {frase.lower().count(v)}", end=" ")