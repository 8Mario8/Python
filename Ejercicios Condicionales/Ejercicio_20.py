#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10
var1=float(input("Introduce un número: "))
var2=float(input("Introduce otro número: "))
if var1<0 or var1>10:
    if var2<0 or var2>10:
        print("Ambos números están fuera del rango permitido (0 a 10).")
    else:
        print("El primer número está fuera del rango permitido.")
elif var2<0 or var2>10:
    print("El segundo número está fuera del rango permitido.")
else:
    if var1>var2:
        print("El número", var1, "es mayor que el número", var2)
    elif var1<var2:
        print("El número", var1, "es menor que el número", var2)
    else:
        print("El número", var1, "es igual que el número", var2)
