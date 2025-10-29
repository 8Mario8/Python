# Sistema de validació de contrasenyes
## Introduir les instruccions
print("INSTRUCCIONS")
print("1. La longitud del password té que tenir entre 6 i 8 caràcters")
print("2. Forçar els següents valors segons la posició indicada:")
print("Posició 1: Un número major o igual que 1 i menor o igual que 5")
print("Posició 2: Una lletra minúscula")
print("Posició 3: Una lletra majúscula")
print("Posició 4: Un dels següents símbols *, _, @")
print("Posició 5: Una lletra minúscula")
print("Posició 6: Un número major o igual que 6 i menor o igual que 9")
print("Posició 7: Un dels següents símbols &, /, #")
print("Posició 8: Un número menor o igual que 5")
## Demanar a l'usuari que introdueixi la contrasenya y donar valor a la variable
password=input("Introdueix una contrasenya: ")
## Comprovar si la contrasenya compleix les instruccions
### Comprovar si la contrasenya compleix amb la longitud establerta
if not int(len(password)) <=8 and not int(len(password)) >=6:
    print("Error, el password té una longitud de", int(len(password)), "caràcters i no compleix els requisits")
    