# EJERCICIO DNI
## Iniciar listas y variables
letras_dni = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
lista_intentos = []
dnis_correctos = []
dnis_incorrectos = []
continuar = "s"
opcion = 4
rep = 0
continuar_menu = "s"

## Pedir al usuario que introduzca el numero de DNI sin la letra
while continuar == "s":
    dni_input = input("\nIntroduce tu número de DNI (8 dígitos): ")

    ## Mirar si el DNI es erroneo o no
    if len(dni_input) != 8:
        print("Error: El DNI debe tener 8 dígitos.")
        lista_intentos.append(0)
        dnis_incorrectos.append(dni_input)

    elif not dni_input.isdigit():
        print("Error: El DNI debe ser numérico.")
        lista_intentos.append(1)
        dnis_incorrectos.append(dni_input)

    ## Si no es erroneo, calcular la letra
    else:
        dni_number = int(dni_input)
        resto = dni_number % 23

        ## Si el resto es valido, mostrar por pantalla el DNI completo
        if 0 <= resto < len(letras_dni):
            letra = letras_dni[resto]
            print("Tu DNI completo es: ", dni_input, "-", letra)
            lista_intentos.append(3)
            dnis_correctos.append(dni_input, "-", letra)

        ## Si el resto es invalido, mostrar por pantalla un mensaje de error
        else:
            print("Error: Resto no válido, DNI incorrecto.")
            lista_intentos.append(2)
            dnis_incorrectos.append(dni_input)
    
    ## Preguntar al usuario si quiere introducir otro DNI o no
    continuar = input("\n¿Deseas introducir otro DNI? (s/n) ").lower()

    ## Si la respuesta no es ni "s" ni "n" volver a preguntar
    while not continuar == "s" and not continuar == "n":
        continuar = input("¿s/n? ").lower()

# MENÚ
while opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5:
    ## Mostrar el menú
    if continuar_menu == "s" and rep == 0:
        print("\nMENÚ")
        print(" 1. DNIs correctos ordenados")
        print(" 2. DNIs incorrectos ordenados")
        print(" 3. Número total de errores")
        print(" 4. Número total de DNIs correctos")
        print(" 5. Porcentajes")
        print(" 6. Salir")

    ## Preguntar al usuario que opción quiere visualizar
    if rep == 0:
        opcion = int(input("\nIntroduce la opción que quieres visualizar: "))
    
    ## Si el usuario ya a introducido antes una o más opciones preguntar si quiere introducir otra opción
    if continuar_menu == "s" and rep > 0:
        continuar_menu = input("\n¿Deseas introducir otra opción? (s/n) ")

        ## Si la respuesta es "s", mostrar el menú y preguntar otra opción
        if continuar_menu == "s":
            print("\nMENÚ")
            print(" 1. DNIs correctos ordenados")
            print(" 2. DNIs incorrectos ordenados")
            print(" 3. Número total de errores")
            print(" 4. Número total de DNIs correctos")
            print(" 5. Porcentajes")
            print(" 6. Salir")

            opcion = int(input("\nIntroduce otra opción del menú: "))

    ## Dependiendo de la opción mostrar lo que pide
    ### Opción 1
    if opcion == 1:
        print("\nDNIs correctos ordenados:")

        for dni in sorted(dnis_correctos):
            print(  dni)

    ### Opción 2
    if opcion == 2:
        print("\nDNIs incorrectos ordenados:")

        for dni in sorted(dnis_incorrectos):
            print(  dni)

    ### Opción 3
    if opcion == 3:
        total_errores = lista_intentos.count(0) + lista_intentos.count(1) + lista_intentos.count(2)
        print("\nNúmero total de errores: ", total_errores)

    ### Opción 4
    if opcion == 4:
        total_correctos = lista_intentos.count(3)
        print("\nNúmero total de DNIs correctos: ", total_correctos)

    ### Opción 5
    if opcion == 5:
        total_intentos = len(lista_intentos)

        if total_intentos > 0:
            print("\n%")
            porcentaje_correctos = (lista_intentos.count(3) / total_intentos) * 100
            porcentaje_incorrectos = (lista_intentos.count(2) / total_intentos) * 100
            porcentaje_errores_longitud = (lista_intentos.count(0) / total_intentos) * 100
            porcentaje_errores_numericos = (lista_intentos.count(1) / total_intentos) * 100
            print(" % de DNI correctos: ", porcentaje_correctos)
            print(" % de DNI incorrectos: ", porcentaje_incorrectos)
            print(" % de errores de longitud: ", porcentaje_errores_longitud)
            print(" % de errores numéricos: ", porcentaje_errores_numericos)
    
    ## Si la opción no esta dentro del rango
    while not opcion == 1 and not opcion == 2 and not opcion == 3 and not opcion == 4 and not opcion == 5 and not opcion == 6:
        opcion = input("Perdona, que opción querias visualizar? ")
    
    ## Contar las repeticiones de las opciones del menú que ha introducido el usuario
    rep = rep + 1