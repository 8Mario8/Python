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

print("MENÚ")
print("1. Bocadillo de calamares - 9€")
print("2. Bocadillo de chistorra - 4.5€")
print("3. Bikini de jamón - 2.5€")

menu=int(input("Introduce el numero del menu que quiere consumir: "))