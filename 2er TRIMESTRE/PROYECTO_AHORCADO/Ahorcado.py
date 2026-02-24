# JUEGO DEL AHORCADO

import random
import unicodedata
from datetime import datetime
import string

abecedario = string.ascii_lowercase

print("JUEGO DEL AHORCADO")

empezar = input("¿Quieres empezar a jugar? (s/n): ")

while empezar.lower() not in ["s", "n"]:
    empezar = input("Opción no válida. ¿Quieres empezar a jugar? (s/n): ")

if empezar.lower() == "s":
    print("\n MODOS DE JUEGO: ")
    print("   1. Modo fácil")
    print("   2. Modo difícil")
    print("   3. Modo contra reloj fácil (1 minuto por palabra)")
    print("   4. Modo contra reloj difícil (30 segundos por palabra)")

    modo_juego = input("\nSelecciona el modo de juego (1/2/3/4): ")

    while modo_juego not in ["1", "2", "3", "4"]:
        modo_juego = input("Opción no válida. Selecciona el modo de juego (1/2/3/4): ")

    print("\n CATEGORÍAS: ")
    print("   1. General")
    print("   2. Palabras con acentos")
    print("   3. Palabras compuestas")
    print("   4. Medicina")
    print("   5. Ciencia")
    print("   6. Deportes")
    print("   7. Madre Tierra")
    print("   8. Informática")
    print("   9. Literatura")
    print("  10. anglicismos")
    print("  11. Geografía")
    print("  12. Historia")
    print("  13. Derecho")
    print("  14. Economía")
    print("  15. Términos difíciles")

    categoria = input("\nSelecciona la categoría (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15): ")

    while categoria not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]:
        categoria = input("Opción no válida. Selecciona la categoría (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15): ")
    
    modos = {"1": "facil", "2": "dificil", "3": "contra_reloj_facil", "4": "contra_reloj_dificil"}
    categorias = {"1": "general", "2": "acentos", "3": "compuestas", "4": "medicina", "5": "ciencia", "6": "deportes", "7": "madre_tierra", "8": "informatica", "9": "literatura", "10": "anglicismos", "11": "geografia", "12": "historia", "13": "derecho", "14": "economia", "15": "dificiles"}

    nombre_modo = modos[modo_juego]
    nombre_categoria = categorias[categoria]
    
    nombre_fichero = "palabras_ahorcado_", nombre_categoria, "_", nombre_modo, ".txt"
    fichero_txt = open(nombre_fichero, "r", encoding="utf-8")

    lista_palabrasecreta = fichero_txt.read().splitlines()
    palabra_secreta = random.choice(lista_palabrasecreta)
    if categoria != "2":
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

    inicio_juego = datetime.now()
    fecha_inicio_juego = inicio_juego.strftime("%d-%m-%Y")
    hora_inicio_juego = inicio_juego.strftime("%H:%M:%S")

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
                
                cambio_modo = input("\n¿Quieres cambiar de modo de juego? (s/n): ")

                while cambio_modo.lower() not in ["s", "n"]:
                    cambio_modo = input("Opción no válida. ¿Quieres cambiar de modo de juego? (s/n): ")
                
                if cambio_modo.lower() == "s":

                    print("\n MODOS DE JUEGO: ")
                    print("   1. Modo fácil")
                    print("   2. Modo difícil")
                    print("   3. Modo contra reloj fácil (1 minuto por palabra)")
                    print("   4. Modo contra reloj difícil (30 segundos por palabra)")

                    modo_nuevapartida = input("\nSelecciona el modo de juego (1/2/3/4): ")

                    while modo_nuevapartida not in ["1", "2", "3", "4"]:
                        modo_nuevapartida = input("Opción no válida. Selecciona el modo de juego (1/2/3/4): ")
                    
                    while modo_nuevapartida == modo_juego:
                        print("Ya has seleccionado este modo de juego en la partida anterior. Por favor, selecciona un modo de juego diferente.")
                        modo_nuevapartida = input("Selecciona el modo de juego (1/2/3/4): ")

                    modos = {"1": "facil", "2": "dificil", "3": "contra_reloj_facil", "4": "contra_reloj_dificil"}

                    nombre_modo = modos[modo_nuevapartida]
                
                cambio_categoria = input("\n¿Quieres cambiar de categoría? (s/n): ")

                while cambio_categoria.lower() not in ["s", "n"]:
                    cambio_categoria = input("Opción no válida. ¿Quieres cambiar de categoría? (s/n): ")
                
                if cambio_categoria.lower() == "s":

                    print("\n CATEGORÍAS: ")
                    print("   1. General")
                    print("   2. Palabras con acentos")
                    print("   3. Palabras compuestas")
                    print("   4. Medicina")
                    print("   5. Ciencia")
                    print("   6. Deportes")
                    print("   7. Madre Tierra")
                    print("   8. Informática")
                    print("   9. Literatura")
                    print("  10. anglicismos")
                    print("  11. Geografía")
                    print("  12. Historia")
                    print("  13. Derecho")
                    print("  14. Economía")
                    print("  15. Términos difíciles")

                    categoria_nuevapartida = input("\nSelecciona la categoría (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15): ")

                    while categoria_nuevapartida not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]:
                        categoria_nuevapartida = input("Opción no válida. Selecciona la categoría (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15): ")
                    
                    while categoria_nuevapartida == categoria:
                        print("Ya has seleccionado esta categoría en la partida anterior. Por favor, selecciona una categoría diferente.")
                        categoria_nuevapartida = input("Selecciona la categoría (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15): ")

                    categorias = {"1": "general", "2": "acentos", "3": "compuestas", "4": "medicina", "5": "ciencia", "6": "deportes", "7": "madre_tierra", "8": "informatica", "9": "literatura", "10": "anglicismos", "11": "geografia", "12": "historia", "13": "derecho", "14": "economia", "15": "dificiles"}

                    nombre_categoria = categorias[categoria_nuevapartida]

                nombre_fichero = "palabras_ahorcado_", nombre_categoria, "_", nombre_modo, ".txt"
                fichero_txt = open(nombre_fichero, "r", encoding = "utf-8")
                
                errores = 0
                aciertos = 0
                lista_palabrasecreta_no_utilizadas = fichero_txt.read().splitlines()
                palabra_secreta = random.choice(lista_palabrasecreta_no_utilizadas)
                if cambio_categoria.lower() == "s":
                    if categoria_nuevapartida != "2":
                        palabra_secreta_sin_acentos = ''.join(c for c in unicodedata.normalize('NFD', palabra_secreta) if unicodedata.category(c) != 'Mn')
                    categoria = categoria_nuevapartida
                else:
                    if categoria != "2":
                        palabra_secreta_sin_acentos = ''.join(c for c in unicodedata.normalize('NFD', palabra_secreta) if unicodedata.category(c) != 'Mn')    
                lista_partida = []
                lista_ahorcado = []
        
        if nueva_partida.lower() == "s" or partidas == 0:
            inicio = datetime.now()
            fecha_inicio = inicio.strftime("%d-%m-%Y")
            hora_inicio = inicio.strftime("%H:%M:%S")

            partidas += 1

            while len(palabra_secreta) > len(lista_partida):
                lista_partida.append("_")
            
            if " " in palabra_secreta:

                for i in range(len(palabra_secreta)):

                    if palabra_secreta[i] == " ":
                        lista_partida[i] = " "

            while len(lista_ahorcado) < 8 and "_" in lista_partida:
                print("\nPalabra secreta: ", " ".join(lista_partida))

                adivinar_palabra = input("¿Quieres adivinar la palabra? (s/n): ")

                while adivinar_palabra.lower() not in ["s", "n"]:
                    adivinar_palabra = input("Opción no válida. ¿Quieres adivinar la palabra? (s/n): ")

                if adivinar_palabra.lower() == "s":
                    palabra_usuario = input("Introduce la palabra que crees que es: ")

                    if palabra_usuario.lower() == palabra_secreta.lower() or palabra_usuario.lower() == palabra_secreta_sin_acentos.lower():
                        aciertos += lista_partida.count("_")
                        lista_aciertos.append(palabra_usuario)

                        lista_partida = list(palabra_secreta)

                    else:
                        errores += lista_partida.count("_")

                        print("Palabra incorrecta")

                        letra_ahorcado = list("AHORCADO")

                        if len(lista_ahorcado) < len(letra_ahorcado):
                            lista_ahorcado.extend(letra_ahorcado[len(lista_ahorcado):])

                        print(" ".join(lista_ahorcado))

                        lista_errores.append(palabra_usuario)

                else:
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

                        print("Letra incorrecta")
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
                duracion = " ".join(map(str, duracion))

                print("\nPalabra secreta: ", " ".join(lista_partida))
                print("\n¡Felicidades, has adivinado la palabra!")
                print("\nNúmero de aciertos: ", aciertos)
                print("Número de errores: ", errores)
                print("\nDuración de la partida: ", duracion)

                linea = " -  | Inicio: ", fecha_inicio, " ", hora_inicio, " | Fin: ", fecha_fin, " ", hora_fin, " | Duración: ", duracion," | Palabra secreta: ", palabra_secreta, " | Número de aciertos: ", aciertos, " | Número de errores: ", errores,"\n"

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
                duracion = " ".join(map(str, duracion))

                print("\nHas perdido")
                print("\nLa palabra secreta era: ", palabra_secreta)
                print("\nNúmero de aciertos: ", aciertos)
                print("Número de errores: ", errores)
                print("\nDuración de la partida: ", duracion)

                linea = " -  | Inicio: ", fecha_inicio, " ", hora_inicio, " | Fin: ", fecha_fin, " ", hora_fin, " | Duración: ", duracion," | Palabra secreta: ", palabra_secreta, " | Número de aciertos: ", aciertos, " | Número de errores: ", errores,"\n"

                with open("partidas_ahorcado.txt", "a", encoding="utf-8") as fichero_txt:
                    fichero_txt.write("".join(map(str, linea)))

                print("\nREGISTRANDO PARTIDA...")
                print("Partida registrada correctamente en 'partidas_ahorcado.txt'.")

    if len(lista_palabrasecreta_no_utilizadas) == 0:
        print("\nNo quedan más palabras disponibles para seguir. Gracias por jugar al Ahorcado.")
    
    fichero_txt.close()
    
    fin_juego = datetime.now()
    fecha_fin_juego = fin_juego.strftime("%d-%m-%Y")
    hora_fin_juego = fin_juego.strftime("%H:%M:%S")

    total_segundos = int((fin_juego - inicio_juego).total_seconds())
    minutos = total_segundos // 60
    segundos = total_segundos % 60
    duracion = minutos, "minutos y ", segundos, "segundos"
    duracion = " ".join(map(str, duracion))
    
    print("\nREUMEN DEL JUEGO")
    print("\n Errores y Aciertos")
    print("    Errores: ", ", ".join(lista_errores))
    print("    Aciertos: ", ", ".join(lista_aciertos))
    print("\n Partidas")
    print("    Partidas jugadas: ", partidas)
    print("    Partidas ganadas: ", partidas_ganadas)
    print("    Partidas perdidas: ", partidas_perdidas)
    print("\n Tiempo")
    print("    Inicio del juego: ", fecha_inicio_juego, " ", hora_inicio_juego)
    print("    Fin del juego: ", fecha_fin_juego, " ", hora_fin_juego)
    print("    Duración total del juego: ", duracion)

    print("\nFIN DEL JUEGO")

else:
    print("FIN DEL JUEGO")