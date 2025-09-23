#17. Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.
peso=float(input("Introduce tu peso en kg: "))
estatura=float(input("Introduce tu estatura en metros: "))
imc=peso/(estatura**2)
print("Tu índice de masa corporal (IMC) es de: ", imc)
if imc>=25:
    print("Tienes sobrepeso.")
else:
    print("No tienes sobrepeso.")