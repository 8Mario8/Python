#EJERCICIO DNI
dni = input("Introduce un valor de 8 dígitos para introducir en un DNI: ")

if not dni.isnumeric:
    print("El valor tiene que ser numérico")
elif not len(dni) == 8:
    print("El valor tiene que tener 8 dígitos")
else:
    