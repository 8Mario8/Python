sumapositivos = 0
sumanegativos = 0
contadormayor100 = 0
for i in range(7):
    num=int(input("Introduce un número: "))
    if num>0:
        sumapositivos = sumapositivos + num
        if num>100:
            contadormayor100 +=1
    else:
        sumanegativos = sumanegativos + num


print("Suma positivos:", sumapositivos)
print("Suma negarivos:", sumanegativos)
print("Mayores de 100:", contadormayor100)