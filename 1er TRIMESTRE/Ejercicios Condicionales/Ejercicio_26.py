#26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición. 
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
        print("La letra es mayúscula ¿?.")