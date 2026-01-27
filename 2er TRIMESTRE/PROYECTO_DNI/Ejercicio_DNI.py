#EJERCICIO DNI
letras_dni = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
lista_intentos = []
dnis_correctos = []
dnis_incorrectos = []
while True:
    dni_input = input("Introduce tu número de DNI (8 dígitos): ")
    if len(dni_input) != 8:
        print("Error: El DNI debe tener 8 dígitos.")
        lista_intentos.append(0)
    elif not dni_input.isdigit():
        print("Error: El DNI debe ser numérico.")
        lista_intentos.append(1)
    else:
        dni_number = int(dni_input)
        resto = dni_number % 23
        if 0 <= resto < len(letras_dni):
            letra = letras_dni[resto]
            print(f"Tu NIF completo es: {dni_input}-{letra}")
            lista_intentos.append(3)
            dnis_correctos.append(f"{dni_input}-{letra}")
        else:
            print("Error: Resto no válido, DNI incorrecto.")
            lista_intentos.append(2)
            dnis_incorrectos.append(dni_input)
    
    continuar = input("¿Deseas introducir otro DNI? (s/n): ").lower()
    if continuar == 'n':
        break
# MENÚ          
    for dni in sorted(dnis_correctos):
        print("DNI correctos ordenados:", dni)

    for dni in sorted(dnis_incorrectos):
        print("DNI incorrectos ordenados:", dni)

    total_errores = lista_intentos.count(0) + lista_intentos.count(1) + lista_intentos.count(2)
    print(f"Número total de errores: {total_errores}")

    total_correctos = lista_intentos.count(3)
    print(f"Número total de DNIs correctos: {total_correctos}")

    total_intentos = len(lista_intentos)
    if total_intentos > 0:
        porcentaje_correctos = (lista_intentos.count(3) / total_intentos) * 100
        porcentaje_incorrectos = (lista_intentos.count(2) / total_intentos) * 100
        porcentaje_errores_longitud = (lista_intentos.count(0) / total_intentos) * 100
        porcentaje_errores_numericos = (lista_intentos.count(1) / total_intentos) * 100
        print("% de DNI correctos: {porcentaje_correctos:.2%}")
        print(f"% de DNI incorrectos: {porcentaje_incorrectos:.2%}")
        print(f"% de errores de longitud: {porcentaje_errores_longitud:.2%}")
        print(f"% de errores numéricos: {porcentaje_errores_numericos:.2%}")