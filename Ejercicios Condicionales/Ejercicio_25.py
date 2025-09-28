#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
nota=float(input("Introduce el valor de la nota de tu último examen: "))
if nota<0 or nota>10:
    print("La nota que has introducido no está entre 0 y 10.")
else:
    if nota<5:
        print("Tu nota es un ", nota, ", has sacado un insuficiente.")
    else:
        if nota>=5 and nota<6.5:
            print("Tu nota es un ", nota, ", has sacado un sufuciente.")
        else:
            if nota>=6.5 and nota<8.5:
                print("Tu nota es un ", nota, ", has sacado un notable.")
            else:
                print("Tu nota es un ", nota, ", has sacado un excelente.")