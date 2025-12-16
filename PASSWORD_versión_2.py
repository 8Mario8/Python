# Sistema de validación de contraseñas

## Introducir las instrucciones
print("\nINSTRUCCIONES")
print("La contraseña tiene que cumplir con los siguientes requisitos:")
print(" - Ha de tener como mínimo 2 números")
print("    - Uno de los números tiene que ser mayor o igual a 1 i menor o igual a 5")
print("    - El otro número tiene que ser diferente, es decir que tiene que ser mayor o igual a 6 i menor o igual a 9")
print(" - Ha de tener como mímino 2 letras mayúsculas")
print("    - Tienen que ser letras distintas")
print(" - Ha de tener como mínimo 2 letras minúsculas")
print("    - Tienen que ser letras distintas")
print(" - Ha de tener como mínimo 2 símbolos")
print("    - Tienen que ser smbolos diferentes\n")

## Inicializar variable
rep = 0

## Iniciar el bucle para los 3 intentos
while rep < 3:
    rep += 1
    print("--- INTENTO", rep, "---")
    password = input("Introduce una contraseña: ") # Pedir al usuario que introduzca la contraseña y dar valor a la variable

## Reiniciar contadores y variables para cada intento
    count_numeros_1_5 = 0
    count_numeros_6_9 = 0
    count_mayusculas = 0
    count_minusculas = 0
    count_simbolos = 0
    numeros_1_5 = ""
    numeros_6_9 = ""
    mayusculas = ""
    minusculas = ""
    simbolos = ""
    password_correcto = True

## Recorrer la contraseña carácter por carácter
    for j in password:

        if j.isdigit():
            numero = int(j)

            if numero >= 1 and numero <= 5:
                count_numeros_1_5 += 1
                numeros_1_5 += j
            else:
                count_numeros_6_9 += 1
                numeros_6_9 += j

        elif j.isupper():
            count_mayusculas += 1
            mayusculas += j

        elif j.islower():
            count_minusculas += 1
            minusculas += j

        else:
            count_simbolos += 1
            simbolos += j

## Validar la contraseña según los criterios establecidos
    if count_numeros_1_5 < 1:
        print("\n - La contraseña debe contener al menos un número entre 1 y 5.")
        password_correcto = False

    if count_numeros_6_9 < 1:
        print("\n - La contraseña debe contener al menos un número entre 6 y 9.")
        password_correcto = False

    if count_mayusculas < 2:
        print("\n - La contraseña debe contener al menos 2 letras mayúsculas.")
        password_correcto = False
    elif len(set(mayusculas)) < 2:
        print("\n - Las letras mayúsculas deben ser distintas.")
        password_correcto = False
    else:
        pass

    if count_minusculas < 2:
        print("\n - La contraseña debe contener al menos 2 letras minúsculas.")
        password_correcto = False
    elif len(set(minusculas)) < 2:
        print("\n - Las letras minúsculas deben ser distintas.")
        password_correcto = False
    else:
        pass

    if count_simbolos < 2:
        print("\n - La contraseña debe contener al menos 2 símbolos.")
        password_correcto = False
    elif len(set(simbolos)) < 2:
        print("\n - Los símbolos deben ser distintos.")
        password_correcto = False
    else:
        pass

## Mostrar el resultado final
    if password_correcto == True:
        print("\nLA CONTRASEÑA ES CORRECTA.\n")

    else:
        print("\nLA CONTRASEÑA ES INCORRECTA.\n")

## TESTEO DE CONTRASEÑAS:

## 1. gustavoAdolfo61&%@ - incorrecta (faltan mayúsculas)
## 2. gUSstavoAdolfo61&% - correcta
## 3. petermaTÍas149862#@~$ - correcta
## 4. castamanCA628# - incorrecta (faltan símbolos)
## 5. MarioRuópolo123456789#@#@ - correcta
## 6. mamalebisho1298#@ - incorrecta (faltan mayúsculas)
## 7. 28AAss@# - incorrecta (las letras mayúsculas y minúsculasdeben ser distintas)
## 8. 23ASas@# - incorrecta (debe contener al menos un número entre 6 y 9)
## 9. 67QWqw#@ - incorrecta (debe contener al menos un número entre 1 y 5)
##10. 1234567890qwertyQWERTY### - incorrecta (los símbolos deben ser distintos)