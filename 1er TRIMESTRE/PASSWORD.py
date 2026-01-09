# Sistema de validació de contrasenyes

## Introduir les instruccions
print("INSTRUCCIONS")
print("1. La longitud del password té que tenir entre 6 i 8 caràcters")
print("2. Forçar els següents valors segons la posició indicada:")
print("   Posició 1: Un número major o igual que 1 i menor o igual que 5")
print("   Posició 2: Una lletra minúscula")
print("   Posició 3: Una lletra majúscula")
print("   Posició 4: Un dels següents símbols *, _, @")
print("   Posició 5: Una lletra minúscula")
print("   Posició 6: Un número major o igual que 6 i menor o igual que 9")
print("   Posició 7: Un dels següents símbols &, /, #")
print("   Posició 8: Un número menor o igual que 5")

## Demanar a l'usuari que introdueixi la contrasenya y donar valor a la variable
password=input("Introdueix una contrasenya: ")

## Comprovar si la contrasenya compleix les instruccions

### Comprovar si la contrasenya compleix amb la longitud establerta
n = len(password)
if n < 6 or n > 8:
    print("Error, el password té una longitud de", n, "caràcters i no compleix els requisits")

### Comprovar si la contrasenya compleix amb els valors establerts per a cada posició
else:
    errors = []

    # Comprovar si la posició 1 compeix que ha de ser un número entre 1 i 5
    if n >= 1:
        c = password [0]
        if not (c.isdigit() and 1 <= int(c) <= 5):
            errors.append("Error en el caràcter 1")

    # Comprovar si la posició 2 compeix que ha de ser una lletra minúscula
    if n >= 2:
        c = password [1]
        if not (c.isalpha() and c.islower()):
            errors.append("Error en el caràcter 2")

    # Comprovar si la posició 3 compeix que ha de ser una lletra majúscula
    if n >= 3:
        c = password [2]
        if not (c.isalpha() and c.isupper()):
            errors.append("Error en el caràcter 3")

    # Comprovar si la posició 4 compeix que ha de ser un dels símbols *, _, @
    if n >= 4:
        c = password [3]
        if c not in ("*", "_", "@"):
            errors.append("Error en el caràcter 4")

    # Comprovar si la posició 5 compeix que ha de ser una lletra minúscula
    if n >= 5:
        c = password [4]
        if not (c.isalpha() and c.islower()):
            errors.append("Error en el caràcter 5")

    # Comprovar si la posició 6 compeix que ha de ser un número entre 6 i 9
    if n >= 6:
        c = password [5]
        if not (c.isdigit() and 6 <= int(c) <= 9):
            errors.append("Error en el caràcter 6")

    # Comprovar si la posició 7 compeix que ha de ser un dels símbols &, /, #
    if n >= 7:
        c = password [6]
        if c not in ("&", "/", "#"):
            errors.append("Error en el caràcter 7")

    # Comprovar si la posició 8 compeix que ha de ser un número menor o igual que 5
    if n >= 8:
        c = password [7]
        if not (c.isdigit() and 0 <= int(c) <= 5):
            errors.append("Error en el caràcter 8")
            
    # Mostrar els resultats
    if errors:
        for e in errors:
            print(e)
    else:
        print("El format del PASSWORD és correcte")