#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla
letra=input("Introduce una letra: ")
es_mayuscula=False
if letra.isalpha():
    if letra==letra.upper():
        es_mayuscula=True
if es_mayuscula:
    print("La letra es mayúscula.")
else:
    if not es_mayuscula and letra.isalpha():
        print("La letra es minúscula.")
    else:
        if letra.isdigit():
            print("El valor introducido es un número.")
        else:
            if not letra.isalpha() and not letra.isdigit():
                print("La letra es mayúscula ¿?.")