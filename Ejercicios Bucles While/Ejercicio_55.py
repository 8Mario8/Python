#55. Última vez que reutilizamos el mismo código.. lo prometo. A partir del programa anterior haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While
repeticiones = 0
total_sumas = 0

while total_sumas <= 50 and total_sumas % 2 != 0 or total_sumas == 0:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    total = num1+num2
    print("El resultado de la suma es: ", total)
    repeticiones += 1
    total_sumas += total
    if total_sumas <= 50:
        print("El total acumulado hasta ahora es de: ", total_sumas)

print("Total de las sumas: ", total_sumas)
print("Número de repeticiones: ", repeticiones)
print("Finalizando programa...")