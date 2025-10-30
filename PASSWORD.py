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
else:
    errors = []
    # Posició 1 (index 0): número entre 1 i 5
    if n >= 1:
        c = password [0]
        if not (c.isdigit() and 1 <= int(c) <= 5):
            errors.append("Error en el caràcter 1")
    # Posició 2 (index 1): lletra minúscula
    if n >= 2:
        c = password [1]
        if not (c.isalpha() and c.islower()):
            errors.append("Error en el caràcter 2")
    # Posició 3 (index 2): lletra majúscula
    if n >= 3:
        c = password [2]
        if not (c.isalpha() and c.isupper()):
            errors.append("Error en el caràcter 3")
    # Posició 4 (index 3): símbol *, _, @
    if n >= 4:
        c = password [3]
        if c not in ("*", "_", "@"):
            errors.append("Error en el caràcter 4")
    # Posició 5 (index 4): lletra minúscula
    if n >= 5:
        c = password [4]
        if not (c.isalpha() and c.islower()):
            errors.append("Error en el caràcter 5")
    # Posició 6 (index 5): número entre 6 i 9
    if n >= 6:
        c = password [5]
        if not (c.isdigit() and 6 <= int(c) <= 9):
            errors.append("Error en el caràcter 6")
    # Posició 7 (index 6): símbol &, /, #
    if n >= 7:
        c = password [6]
        if c not in ("&", "/", "#"):
            errors.append("Error en el caràcter 7")
    # Posició 8 (index 7): número menor o igual que 5 (0-5)
    if n >= 8:
        c = password [7]
        if not (c.isdigit() and 0 <= int(c) <= 5):
            errors.append("Error en el caràcter 8")
    # Mostrar resultats
    if errors:
        for e in errors:
            print(e)
    else:
        print("El format del PASSWORD és correcte")