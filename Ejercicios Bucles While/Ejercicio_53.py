#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While
rep = True
repeticiones = 0
total_sumas = 0

while rep == True:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    total = num1+num2
    print("El resultado de la suma es: ", total)
    repetir=input("¿Deseas repetir la operación? (s/n): ")

    if repetir.lower() == 's':
        rep = True
        repeticiones += 1
        total_sumas += total

    elif repetir.lower() == 'n':
        rep = False
        repeticiones += 1
        total_sumas += total
        print("Número de repeticiones: ", repeticiones)
        print("Total de las sumas: ", total_sumas)
        print("Finalizando programa...")