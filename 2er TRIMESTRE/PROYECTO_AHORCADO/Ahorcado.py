# JUEGO DEL AHORCADO

import random
import unicodedata
from datetime import datetime

lista_palabrasecreta = ["Quijotesco", "Anticonstitucional", "Cacofonía", "Lixivia", "Yunque", "Níquel", "Bucelario", "Cicuta", "Yuxtaposición", "Fulgido", "Guillotina", "Arado"]
palabra_secreta = random.choice(lista_palabrasecreta)
palabra_secreta_sin_acentos = ''.join(c for c in unicodedata.normalize('NFD', palabra_secreta) if unicodedata.category(c) != 'Mn')
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

print("JUEGO DEL AHORCADO")

empezar = input("¿Quieres empezar a jugar? (s/n): ")

while empezar.lower() not in ["s", "n"]:
    empezar = input("Opción no válida. ¿Quieres empezar a jugar? (s/n): ")

if empezar.lower() == "s":

    while nueva_partida.lower() == "s" and len(lista_palabrasecreta_no_utilizadas) > 0:

        if partidas > 0:

            nueva_partida = input("\n¿Quieres jugar otra vez? (s/n): ")

            while nueva_partida.lower() not in ["s", "n"]:
                nueva_partida = input("Opción no válida. ¿Quieres jugar otra vez? (s/n): ")
        
            if nueva_partida.lower() == "s":        
                nueva_palabra = input("\n¿Quieres añadir una nueva palabra al juego? (s/n): ")

                while nueva_palabra.lower() not in ["s", "n"]:
                    nueva_palabra = input("Opción no válida. ¿Quieres añadir una nueva palabra al juego? (s/n): ")

                if nueva_palabra.lower() == "s":
                    nueva_palabra = input("Introduce la nueva palabra: ")
                    lista_palabrasecreta.append(nueva_palabra)
                    lista_palabrasecreta_no_utilizadas.append(nueva_palabra)
                else:
                    print("No se añadirá una nueva palabra al juego")
                
                errores = 0
                aciertos = 0
                lista_palabrasecreta_no_utilizadas.remove(palabra_secreta)
                palabra_secreta = random.choice(lista_palabrasecreta_no_utilizadas)
                palabra_secreta_sin_acentos = ''.join(c for c in unicodedata.normalize('NFD', palabra_secreta) if unicodedata.category(c) != 'Mn')
                lista_partida = []
                lista_ahorcado = []

        inicio = datetime.now()
        fecha_inicio = inicio.strftime("%d-%m-%Y")
        hora_inicio = inicio.strftime("%H:%M:%S")

        partidas += 1

        while len(palabra_secreta) > len(lista_partida):
            lista_partida.append("_")

        while len(lista_ahorcado) < 8 and "_" in lista_partida:
            print("\nPalabra secreta: ", " ".join(lista_partida))
            letra = input("Introduce una letra: ").lower()

            if letra in palabra_secreta_sin_acentos.lower():

                for i in range(len(palabra_secreta_sin_acentos)):

                    if palabra_secreta_sin_acentos[i].lower() == letra:
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
            partidas_ganadas += 1

            fin = datetime.now()
            fecha_fin = fin.strftime("%d-%m-%Y")
            hora_fin = fin.strftime("%H:%M:%S")

            total_segundos = int((fin - inicio).total_seconds())
            minutos = total_segundos // 60
            segundos = total_segundos % 60
            duracion = minutos, "minutos y ", segundos, "segundos"
            duracion = "".join(map(str, duracion))

            print("\nPalabra secreta: ", " ".join(lista_partida))
            print("\n¡Felicidades, has adivinado la palabra!")
            print("\nNúmero de aciertos: ", aciertos)
            print("Número de errores: ", errores)
            print("\nDuración de la partida: ", duracion)

            linea = " -  | Inicio: ", fecha_inicio, "_", hora_inicio, " | Fin: ", fecha_fin, "_", hora_fin, " | Duración: ", duracion," | Palabra secreta: ", palabra_secreta, " | Número de aciertos: ", aciertos, " | Número de errores: ", errores,"\n"

            with open("partidas_ahorcado.txt", "a", encoding="utf-8") as fichero_txt:
                fichero_txt.write("".join(map(str, linea)))

            print("\nREGISTRANDO PARTIDA...")
            print("Partida registrada correctamente en 'partidas_ahorcado.txt'.")

        else:
            partidas_perdidas += 1

            fin = datetime.now()
            fecha_fin = fin.strftime("%d-%m-%Y")
            hora_fin = fin.strftime("%H:%M:%S")

            total_segundos = int((fin - inicio).total_seconds())
            minutos = total_segundos // 60
            segundos = total_segundos % 60
            duracion = minutos, "minutos y ", segundos, "segundos"
            duracion = "".join(map(str, duracion))

            print("\nHas perdido")
            print("\nLa palabra secreta era: ", " ".join(lista_partida))
            print("\nNúmero de aciertos: ", aciertos)
            print("Número de errores: ", errores)
            print("\nDuración de la partida: ", duracion)

            linea = " -  | Inicio: ", fecha_inicio, "_", hora_inicio, " | Fin: ", fecha_fin, "_", hora_fin, " | Duración: ", duracion," | Palabra secreta: ", palabra_secreta, " | Número de aciertos: ", aciertos, " | Número de errores: ", errores,"\n"

            with open("partidas_ahorcado.txt", "a", encoding="utf-8") as fichero_txt:
                fichero_txt.write("".join(map(str, linea)))

            print("\nREGISTRANDO PARTIDA...")
            print("Partida registrada correctamente en 'partidas_ahorcado.txt'.")

    if len(lista_palabrasecreta_no_utilizadas) == 0:
        print("\nNo quedan más palabras disponibles para jugar. Gracias por jugar al Ahorcado.")
    
    print("\nREUMEN DEL JUEGO")
    print("\n Errores y Aciertos")
    print("    Errores: ", ", ".join(lista_errores))
    print("    Aciertos: ", ", ".join(lista_aciertos))
    print("\n Partidas")
    print("    Partidas jugadas: ", partidas)
    print("    Partidas ganadas: ", partidas_ganadas)
    print("    Partidas perdidas: ", partidas_perdidas)

    print("\nFIN DEL JUEGO")

else:
    print("FIN DEL JUEGO")