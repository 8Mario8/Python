#12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
lado=float(input("Introduce el lado del trapecio isósceles: "))
base_menor=float(input("Introduce la base menor del trapecio isósceles: "))
base_mayor=float(input("Introduce la base mayor del trapecio isósceles: "))
altura=float(input("Introduce la altura del trapecio isósceles: "))
perímetro=base_mayor+base_menor+2*lado
área=((base_mayor+base_menor)*altura)/2
print("El perímetro del trapecio isósceles es: ", perímetro)
print("El área del trapecio isósceles es: ", área)