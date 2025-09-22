#10. Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.
var1=float(input("Introduce un número: "))
var2=float(input("Introduce otro número: "))
dividendo=var1
divisor=var2
cociente, resto = divmod(dividendo, divisor)
paridad = "par" if dividendo % 2 == 0 else "impar"
print("Dividendo: ", paridad)
print("Cociente: ", cociente)
print("Resto: ", resto)