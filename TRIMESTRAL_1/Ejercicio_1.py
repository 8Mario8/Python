# Nombrar variables
concatenar=""
var_min=int(input("Introduce el valor minimo del intervalo: "))
var_max=int(input("Introduce el valor maximo del intervalo: "))
var_intervalo=int(input("Introduce el valor del intervalo entre los numeros: "))

# Concatenar el intervalo
for i in range(var_min, var_max, var_intervalo):
    concatenar=concatenar+str(i)+","

# Mostrar la solución
concatenar=concatenar [:-1]
print(concatenar)