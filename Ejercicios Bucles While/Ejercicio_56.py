#56. Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se 
#compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El 
#dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se 
#visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la 
#realización de un pedido, si quiere gestionar otro. 
#El establecimiento contempla los siguientes descuentos:
##Si el total a pagar es entre 20 y 30 euros, se aplica un descuento del 5%
##Si el total a pagar es superior a 30 euros, se aplica un descuento del 15%
##Una vez se finaliza la introducción de todos los pedidos de un cliente, debe aparecer por pantalla:
###• El número de pedidos realizados
###• Total a pagar.
###• Total con IVA (10%)
###• Total con el descuento aplicado.
#MENÚ
##1. Bocadillo de calamares - 9 €"
##2. Bocadillo de chistorra - 4.5 €
##3. Bikini de jamón - 2.5 €"
#ACOMPAÑAMIENTO
##1. Patatas finas - 1.5 €
##2. Patatas gruesas - 1.75 €
##3. Patatas rústicas - 2 €
#BEBIDAS
##1. Coca cola - 2 €"
##2. Acuarius - 1.5 €
##3. Agua - 1 €"

coste_menu = 0
coste_acompañamiento = 0
coste_bebidas = 0

print("MENÚ")
print("1. Bocadillo de calamares - 9€")
print("2. Bocadillo de chistorra - 4.5€")
print("3. Bikini de jamón - 2.5€")

menu = int(input("Introduce el número del menú que quiere consumir: "))

if menu == 1:
    coste_menu = coste_menu + 9
elif menu == 2:
    coste_menu = coste_menu + 4.5
elif menu == 3:
    coste_menu = coste_menu + 2.5
else:
    print("Número de menú imcorrecto")

print("ACOMPAÑAMIENTO")
print("1. Patatas finas - 1.5€")
print("1. Patatas gruesas - 1.75€")
print("1. Patatas rústicas - 2€")

acompañamiento = int(input("Introduce el número del acompañamiento que quiere consumir: "))

if acompañamiento == 1:
    coste_acompañamiento = coste_acompañamiento + 1.5
elif acompañamiento == 2:
    coste_acompañamiento = coste_acompañamiento + 1.75
elif acompañamiento == 3:
    coste_acompañamiento == coste_acompañamiento + 2
else:
    print("Número de acompañamiento incorrecto")

print("BEBIDAS")
print("1. Coca cola - 2€")
print("2. Acuarius - 1.5€")
print("3. Agua - 1€")

bebidas = int(input("Introduce el número de la bebida que quiere consumir: "))

if bebidas == 1:
    coste_bebidas = coste_bebidas + 2
elif bebidas == 2:
    coste_bebidas = coste_bebidas + 1.5
elif bebidas == 3:
    coste_bebidas = coste_bebidas + 1
else:
    print("Número de bebida incorrecto")