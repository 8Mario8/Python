#35. Programa que al introducir un número por teclado permita mostrar ese número de veces tu nombre
nombre=input("Introduce tu nombre: ")
rep=int(input("Introduce el número de veces que quieres que se repita tu nombre: "))
for i in range(rep):
    print(nombre)