#77. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.
lista_1 = ["a", "b", "D", "x", "r", "X", "3", "h", "w", "2", "i"]
numeros = []
letras = []

for x in lista_1:
    if x.isnumeric():
        numeros.append(int(x))
    
    if x.isalpha():
        letras.append(x)

orden = input("Introduce 1 para visualizar en orden ascendente o 2 descendente: ")

if int(orden) == 1:
    numeros.sort()
    letras.sort(key=str.lower)

if int(orden) == 2:
    numeros.sort(reverse = True)
    letras.sort(key=str.lower, reverse = True)

print(numeros)
print(letras)