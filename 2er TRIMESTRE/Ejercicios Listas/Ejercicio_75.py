#75. Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por pantalla los siguientes resultados:
#      a. Cantidad total de valores
#      b. Cantidad de números
#      c. Cantidad de letras
#      d. Cantidad de mayúsculas
#      e. Suma de los valores numéricos
lista_1 = ["a", "b", "D", "x", "r", "X", "3", "h", "w", "2", "i"]

cantidad_total_valores = len(lista_1)
cantidad_numeros = 0
cantidad_letras = 0
cantidad_mayusculas = 0
valores_numericos = []
suma_valores_numericos = 0

for x in lista_1:
    if x.isnumeric():
        cantidad_numeros = cantidad_numeros + 1

        valores_numericos.append(int(x))
    
    if x.isalpha():
        cantidad_letras = cantidad_letras + 1

        if x.isupper():
            cantidad_mayusculas = cantidad_mayusculas + 1

suma_valores_numericos = sum(valores_numericos)

print("Número de valores: ", cantidad_total_valores)
print("Cantidad de números: ", cantidad_numeros)
print("Cantidad de letras: ", cantidad_letras)
print("Cantidad de mayúsculas: ", cantidad_mayusculas)
print("Suma total de números: ", suma_valores_numericos)