#13. Realiza un programa que, a partir introducir el lado de un cubo, presente por pantalla el área y para calcular el volumen utiliza el operador de exponente.
lado_cubo=float(input("Introduce el valor del lado del cubo: "))
área_cubo=6*lado_cubo**2
volumen_cubo=lado_cubo**3
print("El área del cubo es: ", área_cubo)
print("El volumen del cubo es: ", volumen_cubo)