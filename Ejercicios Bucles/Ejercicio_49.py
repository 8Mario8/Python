#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te indique en qué posición de la palabra se encuentra la letra.
secret=input("introduce la palabra 'secreta': ")
for i in range(len(secret)):
    letra=input("Introduce una letra: ")
    if letra in secret:
        for j in range(len(secret)):
            print("La letra se encuentra en la posición", j+1)
    else:
        print("La letra no existe")