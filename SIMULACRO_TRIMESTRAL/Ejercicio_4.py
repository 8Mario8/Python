valor=100
num=int(input("Introduce un número: "))

while num>0 and 50<=valor<=150:
    if num%2==0:
        valor=valor/2
    else:
        valor=valor + num

    if num%3==0:
        valor=valor-5

    print(valor)

    if valor >= 50 and valor <= 150:
        num=int("Introduce un número: ")