#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.
nota=float(input("Introduce el valor de la nota de tu último examen: "))
if nota<0 or nota>10:
    print("La nota que has introducido no está entre 0 y 10.")
else:
    if nota<5:
        print("Tu nota es un ", nota, ", has sacado un insuficiente.")
    else:
        if nota<6.5 or nota==5:
            print("Tu nota es un ", nota, ", has sacado un sufuciente.")
        else:
            if nota>=6.5 or nota<8.5:
                print("Tu nota es un ", nota, ", has sacado un notable.")
            else:
                print("Tu nota es un ", nota, ", has sacado un excelente.")