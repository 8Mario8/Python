#edad=int(input("Introduce la edad: "))

#while edad>130 or edad<=0:
    #print("Edad incorrecta")
    #edad=int(input("Introduce la edad: "))
#print("Edad correcta")


import random
num_secret=random.randint(1, 20)

num=int(input("Introduce un número del 1 al 20: "))

while num_secret!=num:
    print("Vaya, no has acertado. :(")
    num=int(input("Introduce un número del 1 al 20: "))
    if num<1 and num>20:
        print("Enorabuena, has acertado!!! :)")