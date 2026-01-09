nombre=input("Inrtroduce tu nombre: ")
edad=int(input("Introduce tu edad: "))
if nombre.isupper():
    if edad>0 and edad<100:
        año_actual=2025
        futuro=año_actual+(100-edad)
        print("Hola",nombre,"cumplirás 100 años en el año",futuro)
    else:
        print("Edad no válida")
else:
    nombre=nombre.upper()
    if edad>0 and edad<100:
        año_actual=2025
        futuro=año_actual+(100-edad)
        print("Hola",nombre,"cumplirás 100 años en el año",futuro)
    else:
        print("Edad no válida")