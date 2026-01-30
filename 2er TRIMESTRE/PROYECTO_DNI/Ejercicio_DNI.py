#EJERCICIO DNI
letras_dni = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
lista_intentos = []
dnis_correctos = []
dnis_incorrectos = []
continuar = "s"
opcion = 4
rep = 0

while continuar == "s":
    dni_input = input("\nIntroduce tu número de DNI (8 dígitos): ")

    if len(dni_input) != 8:
        print("Error: El DNI debe tener 8 dígitos.")
        lista_intentos.append(0)
        dnis_incorrectos.append(dni_input)

    elif not dni_input.isdigit():
        print("Error: El DNI debe ser numérico.")
        lista_intentos.append(1)
        dnis_incorrectos.append(dni_input)

    else:
        dni_number = int(dni_input)
        resto = dni_number % 23

        if 0 <= resto < len(letras_dni):
            letra = letras_dni[resto]
            print(f"Tu DNI completo es: {dni_input}-{letra}")
            lista_intentos.append(3)
            dnis_correctos.append(f"{dni_input}-{letra}")

        else:
            print("Error: Resto no válido, DNI incorrecto.")
            lista_intentos.append(2)
            dnis_incorrectos.append(dni_input)
    
    continuar = input("\n¿Deseas introducir otro DNI? (s/n) ").lower()
    while not continuar == "s" and not continuar == "n":
        continuar = input("¿s/n? ").lower()

# MENÚ
while opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5:
    print("\nMENÚ")
    print(" 1. DNIs correctos ordenados")
    print(" 2. DNIs incorrectos ordenados")
    print(" 3. Número total de errores")
    print(" 4. Número total de DNIs correctos")
    print(" 5. Porcentajes")
    print(" 6. Salir")

    if rep == 0:
        opcion = int(input("\nIntroduce la opción que quieres visualizar: "))

    if opcion == 1:
        print("\nDNIs correctos ordenados:")

        for dni in sorted(dnis_correctos):
            print(  dni)

    if opcion == 2:
        print("\nDNIs incorrectos ordenados:")

        for dni in sorted(dnis_incorrectos):
            print(  dni)

    if opcion == 3:
        total_errores = lista_intentos.count(0) + lista_intentos.count(1) + lista_intentos.count(2)
        print("\nNúmero total de errores: ", total_errores)

    if opcion == 4:
        total_correctos = lista_intentos.count(3)
        print("\nNúmero total de DNIs correctos: ", total_correctos)

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
    
    while not opcion == 1 and not opcion == 2 and not opcion == 3 and not opcion == 4 and not opcion == 5 and not opcion == 6:
        opcion = input("Perdona, que opción querias visualizar? ")
    
    rep = rep + 1