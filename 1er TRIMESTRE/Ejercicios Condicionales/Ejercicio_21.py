#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
import math
a=float(input("Introduce el valor de a: "))
b=float(input("Introduce el valor de b: "))
c=float(input("Introduce el valor de c: "))
discriminante=b**2-4*a*c
if discriminante<0:
    print("La raíz no puede ser un valor negativo.")
else:
    raiz1=(-b+math.sqrt(discriminante))/(2*a)
    raiz2=(-b-math.sqrt(discriminante))/(2*a)
    print(f"Las soluciones son {raiz1} y {raiz2}.")