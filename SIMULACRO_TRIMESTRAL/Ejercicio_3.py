multiplicar = 1
contador_pares = 0

cantidad_cifras = int(input("Introduce la cantidad de cifras: "))
num = int(input("Introduce un número con esa cantidad de cifras: "))

longitud_num=len(str(num))

if longitud_num == cantidad_cifras:
    for i in str(num):
        multiplicar = multiplicar * int(i)
        if int(i)%2==0:
            contador_pares +=1
    print(multiplicar)
    print(contador_pares)
else:
    print("Longitud incorrecta")

