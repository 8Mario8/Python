#19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales
var1=float(input("Introduce un número: "))
var2=float(input("Introduce otro número: "))
if var1>var2:
    print("El número", var1, "es mayor que el número", var2)
if var1<var2:
    print("El número", var1, "es menor que el número", var2)
if var1==var2:
    print("El número", var1, "es igual que el número", var2)