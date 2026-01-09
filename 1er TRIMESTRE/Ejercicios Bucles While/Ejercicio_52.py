#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While
rep = True

while rep == True:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    total = num1+num2
    print("El resultado de la suma es: ", total)
    repetir=input("¿Deseas repetir la operación? (s/n): ")

    if repetir.lower() == 's':
        rep = True

    elif repetir.lower() == 'n':
        rep = False
        print("Finalizando programa...")