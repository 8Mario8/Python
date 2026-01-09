#14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.
import math
diámetro_círculo=float(input("Introduce el valor del diámetro del círculo: "))
radio_círculo=diámetro_círculo/2
perímetro_círculo=round(2*math.pi*radio_círculo, 1)
área_círculo=round(math.pi*radio_círculo**2, 1)
print("El perímetro del círculo es: ", perímetro_círculo)
print("El ára del círculo es: ", área_círculo)