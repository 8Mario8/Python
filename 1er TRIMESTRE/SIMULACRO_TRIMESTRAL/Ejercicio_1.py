concatenar = ""
inicio = int(input("Introduce el número de inicio: "))
fin = int(input("Introduce el número de final: "))
incremento = int(input("Introduce el incremento entre los números: "))

for i in range(inicio,fin,incremento):
    if not i % 4 == 0:
        if i % 6 == 0:
            concatenar = concatenar + "*" + str(i) + "*" ","
        else:
            concatenar = concatenar + str(i) + ","

concatenar = concatenar[:-1]
print(concatenar)