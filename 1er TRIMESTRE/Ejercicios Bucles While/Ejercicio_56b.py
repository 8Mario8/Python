#56b.Opcional. Haz alguna o todas las mejoras en el programa anterior que a continuación se indican:
# - Cuando se pregunta “si desea realizar otro pedido”, el encargado puede introducir s ó n en mayúscula o minúscula.
# - Si el encargado introduce otro valor distinto a S o N, el programa debe repetir la pregunta e informar de que ha introducido un valor equivocado.
# - El lugar de almacenar los precios en variables, utiliza una biblioteca (busca información) e investiga como moverte por los índices.
# - Un pedido puede estar formado por 3, 2 o 1 componentes. Ej. Un usuario puede pedir únicamente una bebida.

menu = 0
acompanamiento = 0
bebida = 0
precios_menu = 0
precios_acompanamientos = 0
precios_bebidas = 0
total_sin_iva = 0
count_pedido = 0
precio_total = 0
repetir = 's'

while repetir == 's':
    print("MENÚ:")
    print("1. Bocadillo de calamares - 9 €")
    print("2. Bocadillo de chistorra - 4.5 €")
    print("3. Bikini de jamón - 2.5 €")

    menu = int(input("Selecciona el menú (1-3, 0 para omitir): "))

    if menu not in [0, 1, 2, 3]:
        print("Menú no válido. Por favor, inténtalo de nuevo.")
        continue

    print("ACOMPAÑAMIENTOS:")
    print("1. Patatas finas - 1.5 €")
    print("2. Patatas gruesas - 1.75 €")
    print("3. Patatas rústicas - 2 €")

    acompanamiento = int(input("Selecciona el acompañamiento (1-3, 0 para omitir): "))

    if acompanamiento not in [0, 1, 2, 3]:
        print("Acompañamiento no válido. Por favor, inténtalo de nuevo.")
        continue

    print("BEBIDAS:")
    print("1. Coca cola - 2 €")
    print("2. Acuarius - 1.5 €")
    print("3. Agua - 1 €")

    bebida = int(input("Selecciona la bebida (1-3, 0 para omitir): "))

    if bebida not in [0, 1, 2, 3]:
        print("Bebida no válida. Por favor, inténtalo de nuevo.")
        continue

    if bebida == 0 and acompanamiento == 0 and menu == 0:
        print("Debe seleccionar al menos un componente para el pedido.")
        continue

### Precios
    if menu == 1:
        precios_menu += 9
    elif menu == 2:
        precios_menu += 4.5
    elif menu == 3:
        precios_menu += 2.5
    else:
        precios_menu += 0

    if acompanamiento == 1:
        precios_acompanamientos += 1.5
    elif acompanamiento == 2:
        precios_acompanamientos += 1.75
    elif acompanamiento == 3:
        precios_acompanamientos += 2
    else:
        precios_acompanamientos += 0

    if bebida == 1:
        precios_bebidas += 2
    elif bebida == 2:
        precios_bebidas += 1.5
    elif bebida == 3:
        precios_bebidas += 1
    else:
        precios_bebidas += 0

    precio_total = precios_menu + precios_acompanamientos + precios_bebidas
    total_sin_iva = precio_total
    count_pedido += 1

    repetir = input("¿Deseas gestionar otro pedido? (s/n): ")

    while repetir.lower() not in ['s', 'n']:
        repetir = input("Valor incorrecto. Por favor, introduzca 's' para sí o 'n' para no: ")

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
print("Total sin IVA:", total_sin_iva,"€")
print("Total con IVA (10%):", total_con_iva,"€")
print("Total con descuento aplicado:", total_con_descuento,"€")