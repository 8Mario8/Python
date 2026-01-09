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

count_pedido = 0
total_sin_iva = 0
precio_total = 0
precios_menu = 0
precios_acompanamientos = 0
precios_bebidas = 0
menu = 0
acompanamiento = 0
bebida = 0
repetir = 's'

while repetir == 's':
    print("MENÚ:")
    print("1. Bocadillo de calamares - 9 €")
    print("2. Bocadillo de chistorra - 4.5 €")
    print("3. Bikini de jamón - 2.5 €")

    menu = int(input("Selecciona el menú (1-3): "))

    print("ACOMPAÑAMIENTOS:")
    print("1. Patatas finas - 1.5 €")
    print("2. Patatas gruesas - 1.75 €")
    print("3. Patatas rústicas - 2 €")

    acompanamiento = int(input("Selecciona el acompañamiento (1-3): "))

    print("BEBIDAS:")
    print("1. Coca cola - 2 €")
    print("2. Acuarius - 1.5 €")
    print("3. Agua - 1 €")

    bebida = int(input("Selecciona la bebida (1-3): "))
    
### Precios
    if menu == 1:
        precios_menu += 9
    elif menu == 2:
        precios_menu += 4.5
    else:
        precios_menu += 2.5

    if acompanamiento == 1:
        precios_acompanamientos += 1.5
    elif acompanamiento == 2:
        precios_acompanamientos += 1.75
    else:
        precios_acompanamientos += 2

    if bebida == 1:
        precios_bebidas += 2
    elif bebida == 2:
        precios_bebidas += 1.5
    else:
        precios_bebidas += 1
    
    precio_total = precios_menu + precios_acompanamientos + precios_bebidas
    total_sin_iva = precio_total
    count_pedido += 1
    
    repetir = input("¿Deseas gestionar otro pedido? (s/n): ")

    if repetir.lower() == 'n':
        break

iva = total_sin_iva * 0.10
total_con_iva = total_sin_iva + iva

if total_con_iva > 30:
    descuento = total_con_iva * 0.15
elif total_con_iva >= 20 and total_con_iva <= 30:
    descuento = total_con_iva * 0.05
else:
    descuento = 0

total_con_descuento = total_con_iva - descuento

print("Número de pedidos realizados: ", count_pedido)
print("Total a pagar sin IVA:", total_sin_iva,"€")
print("Total con IVA (10%):", total_con_iva,"€")
print("Total con descuento aplicado:", total_con_descuento,"€")