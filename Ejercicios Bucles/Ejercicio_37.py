#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.
num_notas = float(input("Introduce el número de notas que deseas introducir: "))
if num_notas < 0 or num_notas > 10 or num_notas != int(num_notas):
    print("Error")
else:
    for i in range(int(num_notas)):
        nota = float(input("Introduce la nota: "))
        if nota >= 5:
            print("Asignatura aprobada")
        else:
            print("Asignatura suspendida")