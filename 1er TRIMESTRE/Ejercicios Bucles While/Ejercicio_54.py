#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el mensaje del acumulado es singular o plural.. . Con While
repeticiones = 0
total_sumas = 0

while total_sumas <= 50:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    total = num1+num2
    print("El resultado de la suma es: ", total)
    repeticiones += 1
    total_sumas += total
    
    if total_sumas <= 50:
        print("El total acumulado hasta ahora es de: ", total_sumas)

print("Número de repeticiones: ", repeticiones)
print("Total de las sumas: ", total_sumas)
print("Finalizando programa...")