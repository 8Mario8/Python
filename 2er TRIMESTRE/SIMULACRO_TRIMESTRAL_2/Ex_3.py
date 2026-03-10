listaproductos = []
listaprecio = []
listastock = []

var1 = "laptop:800:5-raton:25:10-teclado:50:0-monitor:200:3-raton:25:10"
lista1 = var1.split("-")
for x in lista1:
    lista2 = x.split(":")
    listaproductos.append(lista2[0])
    listaprecio.append(lista2[1])
    listastock.append(lista2[2])
listaprecio = [int(x) for x in listaprecio]
listastock = [int(x) for x in listastock]

for j in range(len(listaprecio)):
    precio_total = precio_total + (listaprecio[j] * listaprecio[j])
print(precio_total)

mascaro = max(listaprecio)
posicion = listaprecio.index(mascaro)

print("El producto mas caro es: ", listaproductos)