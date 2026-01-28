#EJERCICIO DNI
letras_dni = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
lista_intentos = []
dnis_correctos = []
dnis_incorrectos = []
continuar = "s"

while continuar == "s":
    dni_input = input("Introduce tu número de DNI (8 dígitos): ")

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
            print(f"\nTu DNI completo es: {dni_input}-{letra}")
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
while opción ==
print("\nMENÚ")
print(" 1. DNIs correctos ordenados")
print(" 2. DNIs incorrectos ordenados")
print(" 3. Número total de errores")
print(" 4. Número total de DNIs correctos")
print(" 5. Porcentajes")
print(" 6. Salir")

opción = input("Introduce la opción que quieres visualizar: ")

if opción == 1:
    for dni in sorted(dnis_correctos):
        print("\nDNIs correctos ordenados:")
        print(  dni)

for dni in sorted(dnis_incorrectos):
    print("\nDNIs incorrectos ordenados:")
    print(  dni)

total_errores = lista_intentos.count(0) + lista_intentos.count(1) + lista_intentos.count(2)
print("\nNúmero total de errores: ", total_errores)

total_correctos = lista_intentos.count(3)
print("\nNúmero total de DNIs correctos: ", total_correctos)

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