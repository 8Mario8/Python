# JUEGO DEL AHORCADO

#import random
#import unicodedata
#from datetime import datetime
#import string
#
#fichero_txt = open("palabras_ahorcado.txt", "r", encoding = "utf-8")
#lista_palabrasecreta = fichero_txt.read().splitlines()
#palabra_secreta = random.choice(lista_palabrasecreta)
#palabra_secreta_sin_acentos = ''.join(c for c in unicodedata.normalize('NFD', palabra_secreta) if unicodedata.category(c) != 'Mn')
#lista_partida = []
#lista_ahorcado = []
#nueva_partida = "s"
#letra_ahorcado = ""
#partidas = 0
#partidas_ganadas = 0
#partidas_perdidas = 0
#errores = 0
#aciertos = 0
#lista_aciertos = []
#lista_errores =[]
#lista_palabrasecreta_no_utilizadas = lista_palabrasecreta.copy()
#abecedario = string.ascii_lowercase
#
#print("JUEGO DEL AHORCADO")
#
#empezar = input("¿Quieres empezar a jugar? (s/n): ")
#
#while empezar.lower() not in ["s", "n"]:
#    empezar = input("Opción no válida. ¿Quieres empezar a jugar? (s/n): ")
#
#if empezar.lower() == "s":
#    inicio_juego = datetime.now()
#    fecha_inicio_juego = inicio_juego.strftime("%d-%m-%Y")
#    hora_inicio_juego = inicio_juego.strftime("%H:%M:%S")
#
#    while nueva_partida.lower() == "s" and len(lista_palabrasecreta_no_utilizadas) > 0:
#
#        if partidas > 0:
#            nueva_partida = input("\n¿Quieres jugar otra vez? (s/n): ")
#
#            while nueva_partida.lower() not in ["s", "n"]:
#                nueva_partida = input("Opción no válida. ¿Quieres jugar otra vez? (s/n): ")
#        
#            if nueva_partida.lower() == "s":        
#                nueva_palabra = input("\n¿Quieres añadir una nueva palabra al juego? (s/n): ")
#
#                while nueva_palabra.lower() not in ["s", "n"]:
#                    nueva_palabra = input("Opción no válida. ¿Quieres añadir una nueva palabra al juego? (s/n): ")
#
#                if nueva_palabra.lower() == "s":
#                    nueva_palabra = input("Introduce la nueva palabra: ")
#                    lista_palabrasecreta.append(nueva_palabra)
#                    lista_palabrasecreta_no_utilizadas.append(nueva_palabra)
#                else:
#                    print("No se añadirá una nueva palabra al juego")
#                
#                errores = 0
#                aciertos = 0
#                lista_palabrasecreta_no_utilizadas.remove(palabra_secreta)
#                palabra_secreta = random.choice(lista_palabrasecreta_no_utilizadas)
#                palabra_secreta_sin_acentos = ''.join(c for c in unicodedata.normalize('NFD', palabra_secreta) if unicodedata.category(c) != 'Mn')
#                lista_partida = []
#                lista_ahorcado = []
#        
#        if nueva_partida.lower() == "s" or partidas == 0:
#            inicio = datetime.now()
#            fecha_inicio = inicio.strftime("%d-%m-%Y")
#            hora_inicio = inicio.strftime("%H:%M:%S")
#
#            partidas += 1
#
#            while len(palabra_secreta) > len(lista_partida):
#                lista_partida.append("_")
#            
#            if " " in palabra_secreta:
#
#                for i in range(len(palabra_secreta)):
#
#                    if palabra_secreta[i] == " ":
#                        lista_partida[i] = " "
#
#            while len(lista_ahorcado) < 8 and "_" in lista_partida:
#                print("\nPalabra secreta: ", " ".join(lista_partida))
#
#                adivinar_palabra = input("¿Quieres adivinar la palabra? (s/n): ")
#
#                while adivinar_palabra.lower() not in ["s", "n"]:
#                    adivinar_palabra = input("Opción no válida. ¿Quieres adivinar la palabra? (s/n): ")
#
#                if adivinar_palabra.lower() == "s":
#                    palabra_usuario = input("Introduce la palabra que crees que es: ")
#
#                    if palabra_usuario.lower() == palabra_secreta.lower() or palabra_usuario.lower() == palabra_secreta_sin_acentos.lower():
#                        aciertos += lista_partida.count("_")
#                        lista_aciertos.append(palabra_usuario)
#
#                        lista_partida = list(palabra_secreta)
#
#                    else:
#                        errores += lista_partida.count("_")
#
#                        print("Palabra incorrecta")
#
#                        letra_ahorcado = list("AHORCADO")
#
#                        if len(lista_ahorcado) < len(letra_ahorcado):
#                            lista_ahorcado.extend(letra_ahorcado[len(lista_ahorcado):])
#
#                        print(" ".join(lista_ahorcado))
#
#                        lista_errores.append(palabra_usuario)
#
#                else:
#                    letra = input("Introduce una letra: ").lower()
#
#                    if letra in palabra_secreta_sin_acentos.lower():
#
#                        for i in range(len(palabra_secreta_sin_acentos)):
#
#                            if palabra_secreta_sin_acentos[i].lower() == letra:
#                                lista_partida[i] = palabra_secreta[i]
#                                aciertos += 1
#
#                                lista_aciertos.append(letra)
#
#                    else:
#                        errores += 1
#
#                        if errores == 1:
#                            letra_ahorcado = "A"
#
#                        elif errores == 2:
#                            letra_ahorcado = "H"
#
#                        elif errores == 3:
#                            letra_ahorcado = "O"
#
#                        elif errores == 4:
#                            letra_ahorcado = "R"
#
#                        elif errores == 5:
#                            letra_ahorcado = "C"
#
#                        elif errores == 6:
#                            letra_ahorcado = "A"
#
#                        elif errores == 7:
#                            letra_ahorcado = "D"
#
#                        elif errores == 8:
#                            letra_ahorcado = "O"
#
#                        print("Letra incorrecta")
#                        lista_ahorcado.append(letra_ahorcado)
#                        print(" ".join(lista_ahorcado))
#
#                        lista_errores.append(letra)
#
#            if "_" not in lista_partida:
#                partidas_ganadas += 1
#
#                fin = datetime.now()
#                fecha_fin = fin.strftime("%d-%m-%Y")
#                hora_fin = fin.strftime("%H:%M:%S")
#
#                total_segundos = int((fin - inicio).total_seconds())
#                minutos = total_segundos // 60
#                segundos = total_segundos % 60
#                duracion = minutos, "minutos y ", segundos, "segundos"
#                duracion = " ".join(map(str, duracion))
#
#                print("\nPalabra secreta: ", " ".join(lista_partida))
#                print("\n¡Felicidades, has adivinado la palabra!")
#                print("\nNúmero de aciertos: ", aciertos)
#                print("Número de errores: ", errores)
#                print("\nDuración de la partida: ", duracion)
#
#                linea = " -  | Inicio: ", fecha_inicio, " ", hora_inicio, " | Fin: ", fecha_fin, " ", hora_fin, " | Duración: ", duracion," | Palabra secreta: ", palabra_secreta, " | Número de aciertos: ", aciertos, " | Número de errores: ", errores,"\n"
#
#                with open("partidas_ahorcado.txt", "a", encoding="utf-8") as fichero_txt:
#                    fichero_txt.write("".join(map(str, linea)))
#
#                print("\nREGISTRANDO PARTIDA...")
#                print("Partida registrada correctamente en 'partidas_ahorcado.txt'.")
#
#            else:
#                partidas_perdidas += 1
#
#                fin = datetime.now()
#                fecha_fin = fin.strftime("%d-%m-%Y")
#                hora_fin = fin.strftime("%H:%M:%S")
#
#                total_segundos = int((fin - inicio).total_seconds())
#                minutos = total_segundos // 60
#                segundos = total_segundos % 60
#                duracion = minutos, "minutos y ", segundos, "segundos"
#                duracion = " ".join(map(str, duracion))
#
#                print("\nHas perdido")
#                print("\nLa palabra secreta era: ", palabra_secreta)
#                print("\nNúmero de aciertos: ", aciertos)
#                print("Número de errores: ", errores)
#                print("\nDuración de la partida: ", duracion)
#
#                linea = " -  | Inicio: ", fecha_inicio, " ", hora_inicio, " | Fin: ", fecha_fin, " ", hora_fin, " | Duración: ", duracion," | Palabra secreta: ", palabra_secreta, " | Número de aciertos: ", aciertos, " | Número de errores: ", errores,"\n"
#
#                with open("partidas_ahorcado.txt", "a", encoding="utf-8") as fichero_txt:
#                    fichero_txt.write("".join(map(str, linea)))
#
#                print("\nREGISTRANDO PARTIDA...")
#                print("Partida registrada correctamente en 'partidas_ahorcado.txt'.")
#
#    if len(lista_palabrasecreta_no_utilizadas) == 0:
#        print("\nNo quedan más palabras disponibles para seguir. Gracias por jugar al Ahorcado.")
#    
#    fichero_txt.close()
#    
#    fin_juego = datetime.now()
#    fecha_fin_juego = fin_juego.strftime("%d-%m-%Y")
#    hora_fin_juego = fin_juego.strftime("%H:%M:%S")
#
#    total_segundos = int((fin_juego - inicio_juego).total_seconds())
#    minutos = total_segundos // 60
#    segundos = total_segundos % 60
#    duracion = minutos, "minutos y ", segundos, "segundos"
#    duracion = " ".join(map(str, duracion))
#    
#    print("\nREUMEN DEL JUEGO")
#    print("\n Errores y Aciertos")
#    print("    Errores: ", ", ".join(lista_errores))
#    print("    Aciertos: ", ", ".join(lista_aciertos))
#    print("\n Partidas")
#    print("    Partidas jugadas: ", partidas)
#    print("    Partidas ganadas: ", partidas_ganadas)
#    print("    Partidas perdidas: ", partidas_perdidas)
#    print("\n Tiempo")
#    print("    Inicio del juego: ", fecha_inicio_juego, " ", hora_inicio_juego)
#    print("    Fin del juego: ", fecha_fin_juego, " ", hora_fin_juego)
#    print("    Duración total del juego: ", duracion)
#
#    print("\nFIN DEL JUEGO")
#
#else:
#    print("FIN DEL JUEGO")

import random
import time

palabras = ["python", "ordenador", "ahorcado", "barcelona", "cataluna"]
palabra_j1 = random.choice(palabras)
palabra_j2 = random.choice(palabras)

jugador1 = {'palabra': palabra_j1, 'tablero': ['_'] * len(palabra_j1), 'errores': 0, 'letras': [], 'puntos': 0}
jugador2 = {'palabra': palabra_j2, 'tablero': ['_'] * len(palabra_j2), 'errores': 0, 'letras': [], 'puntos': 0}

abc = list('abcdefghijklmnñopqrstuvwxyz')
inicio = time.time()

print(f"J1: {len(palabra_j1)} letras | J2: {len(palabra_j2)} letras")
print("¡300 SEGUNDOS! Escribe letras:")

for ronda in range(30):
    if time.time() - inicio > 300: 
        break
        
    print(f"\nRonda {ronda+1} - Tiempo: {int(300-(time.time()-inicio))}s")
    print(f"J1: {' '.join(jugador1['tablero'])} ({jugador1['errores']}/6)")
    print(f"J2: {' '.join(jugador2['tablero'])} ({jugador2['errores']}/6)")
    
    # J1 turno
    l1 = input("J1 letra: ").lower().strip()
    if len(l1) == 1 and l1 in abc and l1 not in jugador1['letras']:
        jugador1['letras'].append(l1)
        if l1 in jugador1['palabra']:
            for i in range(len(jugador1['palabra'])):
                if jugador1['palabra'][i] == l1:
                    jugador1['tablero'][i] = l1
            if '_' not in jugador1['tablero']:
                jugador1['puntos'] += 50
        else:
            jugador1['errores'] += 1
            jugador1['puntos'] -= 10
    
    # J2 turno
    l2 = input("J2 letra: ").lower().strip()
    if len(l2) == 1 and l2 in abc and l2 not in jugador2['letras']:
        jugador2['letras'].append(l2)
        if l2 in jugador2['palabra']:
            for i in range(len(jugador2['palabra'])):
                if jugador2['palabra'][i] == l2:
                    jugador2['tablero'][i] = l2
            if '_' not in jugador2['tablero']:
                jugador2['puntos'] += 50
        else:
            jugador2['errores'] += 1
            jugador2['puntos'] -= 10
    
    if (jugador1['errores'] >= 6 or '_' not in jugador1['tablero']) and \
       (jugador2['errores'] >= 6 or '_' not in jugador2['tablero']):
        break

print("\n🏆 RESULTADO FINAL")
print(f"J1: {jugador1['puntos']} pts {'✅' if jugador1['errores']<6 else '❌'}")
print(f"J2: {jugador2['puntos']} pts {'✅' if jugador2['errores']<6 else '❌'}")

if jugador1['puntos'] > jugador2['puntos']:
    print("👑 ¡JUGADOR 1 GANA!")
elif jugador2['puntos'] > jugador1['puntos']:
    print("👑 ¡JUGADOR 2 GANA!")
else:
    print("🤝 ¡EMPATE!")
