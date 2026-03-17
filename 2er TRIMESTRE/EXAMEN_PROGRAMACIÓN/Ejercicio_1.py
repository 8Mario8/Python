import random

multiplicaciones = 0
respuestas = []
num_aciertos = 0

while multiplicaciones < 10:
    num1 = random.randint(0,10)
    num2 = random.randint(0,10)

    mult = num1, "x", num2, "= "
    multi = int(input(mult))

    if num1 * num2 == int(multi):
        num_aciertos += 1
    
    multiplicaciones += 1
    respuestas.append(str(num1*num2))

print("Has conseguido", num_aciertos, "puntos")
print("Las respuestas correctas eran:", respuestas)