# JUEGO DEL AHORCADO

import random

lista_palabrasecreta = ["Jirafa", "Lixivia", "Yunque", "Niquel", "Bucelario", "Cicuta", "Yuxtaposición", "Fulgido", "Guillotina", "Arado"]
palabra_secreta = random.choice(lista_palabrasecreta)
lista_partida = []
lista_ahorcado = []
nueva_partida = "s"
letra_ahorcado = ""

while len(palabra_secreta) > len(lista_partida):
    lista_partida.append("_")

print("---- JUEGO DEL AHORCADO ----")

empezar = input("¿Quieres empezar a jugar? (s/n): ")

while empezar.lower() not in ["s", "n"]:
    empezar = input("Opción no válida. ¿Quieres empezar a jugar? (s/n): ")

if empezar.lower() == "s":
    while len(lista_ahorcado) < 6 and "_" in lista_partida:
        print("\nPalabra secreta: ", " ".join(lista_partida))
        letra = input("Introduce una letra: ").lower()

        if letra in palabra_secreta.lower():
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i].lower() == letra:
                    lista_partida[i] = palabra_secreta[i]

        else:
            print("Letra incorrecta.")
            print(lista_ahorcado.append(letra_ahorcado))

    if "_" not in lista_partida:
        print("\nPalabra secreta: ", palabra_secreta)
        print("¡Felicidades, has adivinado la palabra!")
        
    else:
        print("\nHas perdido. La palabra secreta era: ", palabra_secreta)

else:
    print("---- FIN DEL JUEGO ----")

while nueva_partida.lower() == "s":

    nueva_partida = input("¿Quieres jugar otra vez? (s/n): ")

    while nueva_partida.lower() not in ["s", "n"]:
        nueva_partida = input("Opción no válida. ¿Quieres jugar otra vez? (s/n): ")

    if nueva_partida.lower() == "s":
        palabra_secreta = random.choice(lista_palabrasecreta)
        lista_partida = []
        lista_ahorcado = []

        while len(palabra_secreta) > len(lista_partida):
            lista_partida.append("_")
        
        while len(lista_ahorcado) < 6 and "_" in lista_partida:
            print("\nPalabra secreta: ", " ".join(lista_partida))
            letra = input("Introduce una letra: ").lower()

            if letra in palabra_secreta.lower():
                for i in range(len(palabra_secreta)):
                    if palabra_secreta[i].lower() == letra:
                        lista_partida[i] = palabra_secreta[i]

            else:
                lista_ahorcado.append(letra)
                print("Letra incorrecta")
                print(lista_ahorcado.append(letra_ahorcado))

        if "_" not in lista_partida:
            print("\nPalabra secreta: ", palabra_secreta)
            print("¡Felicidades, has adivinado la palabra!")
        
        else:
            print("\nHas perdido. La palabra secreta era: ", palabra_secreta)
    else:
        print("---- FIN DEL JUEGO ----")