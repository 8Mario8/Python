#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While
rep=True
while rep==True:
    num1=int(input("Introduce el primer número: "))
    num2=int(input("Introduce el segundo número: "))
    total=num1+num2
    print("El resultado de la suma:", total)
    rep=input("Deseas repetir la operación s/n: ")
    s=1
    n=-1
    if rep==s:
        rep==True
    else:
        rep==False