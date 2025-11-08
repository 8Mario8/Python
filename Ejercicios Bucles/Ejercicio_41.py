#41. Imprime el siguiente patrón utilizando for:
#    54321
#    4321
#    321
#    21
#    1
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()