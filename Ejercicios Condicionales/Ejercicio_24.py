#24. Corrige los errores del siguiente código y comprueba que se ejecuta correctamente
peso=float(input("Introduce tu peso en kg: "))
estatura=float(input("Introduce tu estatura en metros: "))
imc=peso/(estatura**2)
print("Si pesas", peso, "kilos y mides", estatura, ", tu IMC es: ", imc)
if imc>=25:
    print("Tienes sobrepeso.")
else:
    print("Estas dentro de los parámetros normales.")