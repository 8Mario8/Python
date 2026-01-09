# Inicializo listas
milista = [1, 2, 3, 4, 5, 6]
milistapor2 = []
milistapro = []
milistapor2pro = []

# Inicializo variables
maximo = max(milista)
minimo = min(milista)
suma = sum(milista)

# Muestro por pantalla la lista, su máximo, su mínimo y su suma
print(milista)
print("maximo:", maximo)
print("minimo:", minimo)
print("Suma total", suma)

# Hago que todos los valores de la lista se multipliquen por 2 y los muestro en otra lista de tres maneras distintas:

## Primera (la opción más sencilla)

for x in range(len(milista)):
    calculo = milista[x] * 2
    milistapor2.append(calculo)

print(milistapor2)

## Segunda (la opción un poco más dificil)

for x in milista:
    milistapro.append(x * 2)

print(milistapro)

## Tercera (la opción pro)

milistapor2pro = [n * 2 for n in milista]

print(milistapor2pro)