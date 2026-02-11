palabras = input().split()
if palabras[0] == palabras[1]:
    print(palabras[0], "=", palabras[1])
elif palabras[0] < palabras[1]:
    print(palabras[0], "<", palabras[1])
else:
    print(palabras[0], ">", palabras[1])