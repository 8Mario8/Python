#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
import math
radio_cilindro=float(input("Introduce el valor del radio del cilindro: "))
altura_cilindro=float(input("Introduce el valor de la altura del cilindro: "))
área_cilindro=round(2*math.pi*radio_cilindro*(radio_cilindro+altura_cilindro), 2)
volumen_cilindro=round(math.pi*radio_cilindro**2*altura_cilindro, 2)
print("El área del cilindro es: ", área_cilindro)
print("El volumen del cilindro es: ", volumen_cilindro)