#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10
var1=float(input("Introduce un número: "))
var2=float(input("Introduce otro número: "))
if var1>=10:
    print("Uno de los números esta fuera de los límites.")
if var2>=10:
    print("Uno de los números esta fuera de los límites.")
if var1 and var2>=10:
    print("Los dos números estan fuera de los límites.")
if var1>var2:
    print("El número", var1, "es mayor que el número", var2)
if var1<var2:
    print("El número", var1, "es menor que el número", var2)
if var1==var2:
    print("El número", var1, "es igual que el número", var2)