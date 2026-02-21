# JUEGO DEL AHORCADO

import random

lista_palabrasecreta = ["Quijotesco", "Anticonstitucional", "Cacofonía", "Lixivia", "Yunque", "Níquel", "Bucelario", "Cicuta", "Yuxtaposición", "Fulgido", "Guillotina", "Arado"]
palabra_secreta = random.choice(lista_palabrasecreta)
lista_partida = []
lista_ahorcado = []
nueva_partida = "s"
letra_ahorcado = ""
partidas = 0
partidas_ganadas = 0
partidas_perdidas = 0
errores = 0
aciertos = 0
lista_aciertos = []
lista_errores =[]
lista_palabrasecreta_no_utilizadas = lista_palabrasecreta.copy()

while len(palabra_secreta) > len(lista_partida):
    lista_partida.append("_")

print("JUEGO DEL AHORCADO")

empezar = input("¿Quieres empezar a jugar? (s/n): ")

while empezar.lower() not in ["s", "n"]:
    empezar = input("Opción no válida. ¿Quieres empezar a jugar? (s/n): ")

if empezar.lower() == "s":
    while len(lista_ahorcado) < 8 and "_" in lista_partida:
        print("\nPalabra secreta: ", " ".join(lista_partida))
        letra = input("Introduce una letra: ").lower()

        if letra in palabra_secreta.lower():

            for i in range(len(palabra_secreta)):

                if palabra_secreta[i].lower() == letra:
                    lista_partida[i] = palabra_secreta[i]
                    aciertos += 1
                    lista_aciertos.append(letra)

        else:
            errores += 1
            if errores == 1:
                letra_ahorcado = "A"
            elif errores == 2:
                letra_ahorcado = "H"
            elif errores == 3:
                letra_ahorcado = "O"
            elif errores == 4:
                letra_ahorcado = "R"
            elif errores == 5:
                letra_ahorcado = "C"
            elif errores == 6:
                letra_ahorcado = "A"
            elif errores == 7:
                letra_ahorcado = "D"
            elif errores == 8:
                letra_ahorcado = "O"

            print("Letra incorrecta.")
            lista_ahorcado.append(letra_ahorcado)
            print(" ".join(lista_ahorcado))

            lista_errores.append(letra)

    if "_" not in lista_partida:
        print("\nPalabra secreta: ", " ".join(lista_partida))
        print("\nNúmero de aciertos: ", aciertos)
        print("Número de errores: ", errores)
        print("\n¡Felicidades, has adivinado la palabra!")
        
    else:
        print("\nLa palabra secreta era: ", palabra_secreta)
        print("\nNúmero de aciertos: ", aciertos)
        print("Número de errores: ", errores)
        print("\nHas perdido")

    while nueva_partida.lower() == "s":

        nueva_partida = input("\n¿Quieres jugar otra vez? (s/n): ")

        while nueva_partida.lower() not in ["s", "n"]:
            nueva_partida = input("Opción no válida. ¿Quieres jugar otra vez? (s/n): ")

        if nueva_partida.lower() == "s":
            partidas += 1
            lista_palabrasecreta_no_utilizadas.remove(palabra_secreta)
            palabra_secreta = random.choice(lista_palabrasecreta_no_utilizadas)
            lista_partida = []
            lista_ahorcado = []

            while len(palabra_secreta) > len(lista_partida):
                lista_partida.append("_")

            while len(lista_ahorcado) < 8 and "_" in lista_partida:
                    print("\nPalabra secreta: ", " ".join(lista_partida))
                    letra = input("Introduce una letra: ").lower()

                    if letra in palabra_secreta.lower():
                    
                        for i in range(len(palabra_secreta)):
                        
                            if palabra_secreta[i].lower() == letra:
                                lista_partida[i] = palabra_secreta[i]
                                aciertos += 1
                                lista_aciertos.append(letra)

                    else:
                        errores += 1
                        if errores == 1:
                            letra_ahorcado = "A"
                        elif errores == 2:
                            letra_ahorcado = "H"
                        elif errores == 3:
                            letra_ahorcado = "O"
                        elif errores == 4:
                            letra_ahorcado = "R"
                        elif errores == 5:
                            letra_ahorcado = "C"
                        elif errores == 6:
                            letra_ahorcado = "A"
                        elif errores == 7:
                            letra_ahorcado = "D"
                        elif errores == 8:
                            letra_ahorcado = "O"

                        print("Letra incorrecta.")
                        lista_ahorcado.append(letra_ahorcado)
                        print(" ".join(lista_ahorcado))

                        lista_errores.append(letra)

            if "_" not in lista_partida:
                print("\nPalabra secreta: ", " ".join(lista_partida))
                print("\nNúmero de aciertos: ", aciertos)
                print("Número de errores: ", errores)
                print("\n¡Felicidades, has adivinado la palabra!")
                
                partidas_ganadas += 1

            else:
                print("\nLa palabra secreta era: ", palabra_secreta)
                print("\nNúmero de aciertos: ", aciertos)
                print("Número de errores: ", errores)
                print("\nHas perdido")

                partidas_perdidas += 1
    
    print("\nREUMEN DEL JUEGO")
    print(" Errores y Aciertos")
    print("     Errores: ", lista_errores)
    print("     Aciertos: ", lista_aciertos)
    print(" Partidas")
    print("     Partidas jugadas: ", partidas)
    print("     Partidas ganadas: ", partidas_ganadas)
    print("     Partidas perdidas: ", partidas_perdidas)
    print("\nFIN DEL JUEGO")

else:
    print("FIN DEL JUEGO")