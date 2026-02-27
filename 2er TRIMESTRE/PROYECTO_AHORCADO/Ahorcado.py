# JUEGO DEL AHORCADO

# Importo las líbrerias necesarias para el programa
import random   # Para escoger de manera aleatoria la palabra secreta de la lista de palabras
import unicodedata   # Para eliminar los acentos de las palabras secretas y poder compararlas con las letras introducidas por el usuario sin que afecten los acentos
from datetime import datetime   # Para registrar la fecha y hora de inicio y fin de cada partida y poder calcular la duración de cada partida y del juego en general
import string   # Para crear una variable con el abecedario y poder comparar las letras introducidas por el usuario con el abecedario para evitar que introduzca caracteres no válidos
import time  # Para medir el tiempo transcurrido en los modos contra reloj y finalizar la partida si al usuario se le acaba el tiempo

abecedario = string.ascii_lowercase # Variable con el abecedario en minúscula para comparar las letras introducidas con la libreía string

# Empezar el juego
print("JUEGO DEL AHORCADO")

empezar = input("¿Quieres empezar a jugar? (s/n): ")    # Preguntar al usuario si quiere empezar a jugar

# Si la respuesta no es s ni n, evitar que le programa de error y volver a preguntar al usuario hasta que la respuesta sea válida
while empezar.lower() not in ["s", "n"]:
    empezar = input("Opción no válida. ¿Quieres empezar a jugar? (s/n): ")

# Si el usuario quiere empezar a jugar, empezar el juego y mostrar los diferentes modos de juego
if empezar.lower() == "s":
    print("\n MODOS DE JUEGO: ")
    print("   1. Modo fácil")
    print("   2. Modo difícil")
    print("   3. Modo contra reloj fácil (1 minuto por palabra)")
    print("   4. Modo contra reloj difícil (30 segundos por palabra)")

    modo_juego = input("\nSelecciona el modo de juego (1/2/3/4): ") # Preguntar al usuario por el modo de juego que quiere jugar

    # Si la respuesta no válida, evitar que le programa de error y volver a preguntar al usuario hasta que la respuesta sea válida
    while modo_juego not in ["1", "2", "3", "4"]:
        modo_juego = input("Opción no válida. Selecciona el modo de juego (1/2/3/4): ")
    
    # Mostrar las diferentes categorías de palabras para el juego
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

    categoria = input("\nSelecciona la categoría (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15): ")  # Preguntar al usuario por la categoría que quiere jugar

    # Si la respuesta no válida, evitar que le programa de error y volver a preguntar al usuario hasta que la respuesta sea válida
    while categoria not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]:
        categoria = input("Opción no válida. Selecciona la categoría (1/2/3/4/5/6/7/8/9/10/11/12/13/14/15): ")
    
    # Asignar a dos listas todos las opciones de modos de juego y categorias
    modos = {"1": "facil", "2": "dificil", "3": "contra_reloj_facil", "4": "contra_reloj_dificil"}
    categorias = {"1": "general", "2": "acentos", "3": "compuestas", "4": "medicina", "5": "ciencia", "6": "deportes", "7": "madre_tierra", "8": "informatica", "9": "literatura", "10": "anglicismos", "11": "geografia", "12": "historia", "13": "derecho", "14": "economia", "15": "dificiles"}

    # Utilizando las listas anteriores, asignar a dos variables el nombre del modo de juego y de la categoría seleccionados por el usuario
    nombre_modo = modos[modo_juego]
    nombre_categoria = categorias[categoria]
    
    # Con las variables anteriores, abrir el fichero de texto correspondiente al modo y categoría seleccionados para, aleatoriamente, asignar a la palabra secreta una palabra de ese fichero 
    nombre_fichero = "palabras_ahorcado_", nombre_categoria, "_", nombre_modo, ".txt"
    fichero_txt = open(nombre_fichero, "r", encoding="utf-8")

    lista_palabrasecreta = fichero_txt.read().splitlines()  # Asignar las palabras del fichero a la lista de palabras secretas
    palabra_secreta = random.choice(lista_palabrasecreta)   # Asignar de manera aleatoria una palabra de lsa lista a la palabra secreta
    if categoria != "2":    # Si la categoría seleccionada no es la de palabras con accentos, hacer que cuando el usuario introduce una vocal que en la palabra secreta va con accento, muestre en la lista_partida la vocal con accento
        palabra_secreta_sin_acentos = ''.join(c for c in unicodedata.normalize('NFD', palabra_secreta) if unicodedata.category(c) != 'Mn')
    lista_partida = []  # Lista donde se almacenan la longitud de la palabra secreta con sus respectivos espacios (_ _ _ _ _ _)
    lista_ahorcado = []    # Lista donde se almacenan las letras de la palabra ahorcado cada vez que cometes un error y se reinicia en cada palabra
    nueva_partida = "s"
    letra_ahorcado = ""
    partidas = 0
    partidas_ganadas = 0
    partidas_perdidas = 0
    errores = 0
    aciertos = 0
    lista_aciertos = []    # Lista donde se almacenan todas las letras acertadas
    lista_errores =[]   # Lista donde se almacenan todas las letras falladas
    lista_palabrasecreta_no_utilizadas = lista_palabrasecreta.copy()    # Copi

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

            if modo_juego in ["3", "4"]:

                if modo_juego == "3":
                    tiempo_limite = 60
                else:
                    tiempo_limite = 30

                print("\nTienes ", tiempo_limite, " segundos para adivinar la palabra")

                tiempo_inicio = time.time()

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

                    if categoria != "2" and categoria_nuevapartida != "2":

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
                    
                    else:

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

                                    print("Letra incorrecta")
                                    lista_ahorcado.append(letra_ahorcado)
                                    print(" ".join(lista_ahorcado))

                                    lista_errores.append(letra)
                
                tiempo_transcurrido = time.time() - tiempo_inicio

                if tiempo_transcurrido >= tiempo_limite:
                    print("\nSe ha acabado el tiempo")
                    break

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

                linea = " -  | Inicio: ", fecha_inicio, " ", hora_inicio, " | Fin: ", fecha_fin, " ", hora_fin, " | Duración: ", duracion, " | Modo de juego: ", modo_juego, " | Categoría: ", categoria, " | Palabra secreta: ", palabra_secreta, " | Número de aciertos: ", aciertos, " | Número de errores: ", errores,"\n"

                with open("partidas_ahorcado.txt", "a", encoding="utf-8") as fichero_txt:
                    fichero_txt.write("".join(map(str, linea)))

                print("\nREGISTRANDO PARTIDA...")
                print("Partida registrada correctamente en 'partidas_ahorcado.txt'")

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

                linea = " -  | Inicio: ", fecha_inicio, " ", hora_inicio, " | Fin: ", fecha_fin, " ", hora_fin, " | Duración: ", duracion, " | Modo de juego: ", modo_juego, " | Categoría: ", categoria, " | Palabra secreta: ", palabra_secreta, " | Número de aciertos: ", aciertos, " | Número de errores: ", errores,"\n"

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