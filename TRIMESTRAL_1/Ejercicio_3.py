# Nombrar las variables
suma_cifras=0
cifras=int(input("Introduce el número de cifras: "))
num=int(input("Introduce un número con ese mismo número de cifras: "))

# Comprovar si el número de cifras coincide y si coincide sumar las cifras
if len(str(num)) < cifras or len(str(num)) > cifras:
    print("Error, no coincide el número de cifras.")
else:
    for i in range(len(str(num))):
        suma_cifras=suma_cifras+i

    # Mostrar el resultado
    print("Resultado:", suma_cifras)