#33. Programa un código que permita contar el número de vocales de la siguiente frase: No hay mal que dure cien años
def contar_vocales_individual(frase):
    vocales = "aeiou"
    conteo = {v: 0 for v in vocales}
    for char in frase.lower():
        if char in conteo:
            conteo[char] += 1
    return conteo 
frase = "No hay mal que dure cien años"
conteo = contar_vocales_individual(frase)
print(f"El número de a es {conteo['a']} el número de e es {conteo['e']} el número de i es {conteo['i']} el número de o es {conteo['o']} y el número de u es {conteo['u']}")