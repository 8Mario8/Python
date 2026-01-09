#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.
letra=input("Introduce una letra: ")
es_mayuscula=False
if letra.isalpha():
    if letra==letra.upper():
        es_mayuscula=True
if es_mayuscula:
    print("La letra es mayúscula.")
elif not es_mayuscula and letra.isalpha():
        print("La letra es minúscula.")
else:
    if letra.isdigit():
        print("El valor introducido es un número.")
    else:
        print("El valor introducido es un símbolo.")