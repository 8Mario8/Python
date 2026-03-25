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

# Listas de los diferentes grupos de palabras correspondientes a las diferentes opciones de modo y categoria
general_facil = ["achiperres", "almagre", "cacofonía", "despulpar", "ecletordomésticos", "exhumación ilegal", "fulgido", "hipopotamofobia", "pícaro", "quijotesco"]
general_dificil = ["antidesintegracionistarevolucionario", "desintegracionparticularelativista", "fototransistor semiconductor", "hipopotamonstruosesquipedaliofobico", "inconstitucionalidad democrática", "oxicloruro ferroso", "otorrinolaringólogo", "quimioprofilaxispreventivamedica", "paralelepipedogeometriaanalitica", "supercalifragilisticexpialidoso"]
general_contra_reloj_facil = ["achiperres", "almagre", "cacofonía", "despulpar", "ecletordomésticos", "exhumación ilegal", "fulgido", "hipopotamofobia", "pícaro", "quijotesco"]
general_contra_reloj_dificil = ["antidesintegracionistarevolucionario", "desintegracionparticularelativista", "fototransistor semiconductor", "hipopotamonstruosesquipedaliofobico", "inconstitucionalidad democrática", "oxicloruro ferroso", "otorrinolaringólogo", "quimioprofilaxispreventivamedica", "paralelepipedogeometriaanalitica", "supercalifragilisticexpialidoso"]
acentos_facil = ["menú", "bolígrafo", "miércoles", "exámenes", "química", "matemáticas", "economía", "magnífico", "depósito", "analíticamente"]
acentos_dificil = ["proposición", "expresión", "impresión", "depresión", "profesión", "televisión", "comunicación", "información", "explicación", "murciélago"]
acentos_contra_reloj_facil = ["menú", "bolígrafo", "miércoles", "exámenes", "química", "matemáticas", "economía", "magnífico", "depósito", "analíticamente"]
acentos_contra_reloj_dificil = ["proposición", "expresión", "impresión", "depresión", "profesión", "televisión", "comunicación", "información", "explicación", "murciélago"]
compuestas_facil = ["paraguas", "parasol", "sacapuntas", "abrelatas", "sacacorchos", "cortaplumas", "lavaplatos", "limpiacristales", "quitamanchas", "cortacésped"]
compuestas_dificil = ["permanganato potásico", "celulosa poliglucosa", "noradrenalina norepinefrina", "testosterona andrógeno", "aspirina ácidoacetilsalicílico", "atropina alcaloide", "fenobarbital barbitúrico", "carbamazepina antiepiléptico", "estreptokinasa fibrinolítico", "montelukast antileucotrieno"]
compuestas_contra_reloj_facil = ["paraguas", "parasol", "sacapuntas", "abrelatas", "sacacorchos", "cortaplumas", "lavaplatos", "limpiacristales", "quitamanchas", "cortacésped"]
compuestas_contra_reloj_dificil = ["permanganato potásico", "celulosa poliglucosa", "noradrenalina norepinefrina", "testosterona andrógeno", "aspirina ácidoacetilsalicílico", "atropina alcaloide", "fenobarbital barbitúrico", "carbamazepina antiepiléptico", "estreptokinasa fibrinolítico", "montelukast antileucotrieno"]
medicina_facil = ["estetoscopio", "articulación", "yodo", "alcohol", "aspirina", "suero", "oxígeno", "quirófano", "convulsión", "parálisis"]
medicina_dificil = ["otorrinolaringología"]

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

    categoria = input("\nSelecciona la categoría (1/2/3/4/5): ")  # Preguntar al usuario por la categoría que quiere jugar

    # Si la respuesta no válida, evitar que le programa de error y volver a preguntar al usuario hasta que la respuesta sea válida
    while categoria not in ["1", "2", "3", "4", "5"]:
        categoria = input("Opción no válida. Selecciona la categoría (1/2/3/4/5): ")
    
    # Con las variables anteriores, utilizar la lista correspondiente al modo y categoría seleccionados para, aleatoriamente, asignar a la palabra secreta una palabra de esa lista
    if modo_juego == 1:

        if categoria == 1:
            lista_palabrasecreta = general_facil

        if categoria == 2:
            lista_palabrasecreta = acentos_facil

        if categoria == 3:
            lista_palabrasecreta = compuestas_facil

        if categoria == 4:
            lista_palabrasecreta = medicina_facil

        if categoria == 5:
            lista_palabrasecreta = ciencia_facil
        
    if modo_juego == 2:

        if categoria == 1:
            lista_palabrasecreta = general_dificil

        if categoria == 2:
            lista_palabrasecreta = acentos_dificil

        if categoria == 3:
            lista_palabrasecreta = compuestas_dificil

        if categoria == 4:
            lista_palabrasecreta = medicina_dificil
            
        if categoria == 5:
            lista_palabrasecreta = ciencia_dificil

    if modo_juego == 3:

        if categoria == 1:
            lista_palabrasecreta = general_contra_reloj_facil

        if categoria == 2:
            lista_palabrasecreta = acentos_contra_reloj_facil

        if categoria == 3:
            lista_palabrasecreta = compuestas_contra_reloj_facil

        if categoria == 4:
            lista_palabrasecreta = medicina_contra_reloj_facil
            
        if categoria == 5:
            lista_palabrasecreta = ciencia_contra_reloj_facil

    if modo_juego == 4:

        if categoria == 1:
            lista_palabrasecreta = general_contra_reloj_dificil

        if categoria == 2:
            lista_palabrasecreta = acentos_contra_reloj_dificil

        if categoria == 3:
            lista_palabrasecreta = compuestas_contra_reloj_dificil

        if categoria == 4:
            lista_palabrasecreta = medicina_contra_reloj_dificil
            
        if categoria == 5:
            lista_palabrasecreta = ciencia_contra_reloj_dificil

    lista_palabrasecreta_no_utilizadas = lista_palabrasecreta.copy()    # Copia de la lista de palabras secretas para quitar la palabra ya utilizada
    palabra_secreta = random.choice(lista_palabrasecreta_no_utilizadas)   # Asignar de manera aleatoria una palabra de lsa lista a la palabra secreta
    lista_palabrasecreta_no_utilizadas = lista_palabrasecreta_no_utilizadas.remove(palabra_secreta)    # Quitar la palabra secreta para que no se repita en las siguientes partidas
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
    lista_letras_partida = []    # Lista donde se almacenan las letras utilizadas durante la partida y se reinicia en cada partida
    lista_errores =[]   # Lista donde se almacenan todas las letras falladas
    letras_con_acento = ["á", "é", "í", "ó", "ú"]   # Lista con las vocales con acento

    if categoria != "2":    # Si la categoría seleccionada no es la de palabras con accentos, hacer que cuando el usuario introduce una vocal que en la palabra secreta va con accento, muestre en la lista_partida la vocal con accento
        palabra_secreta_sin_acentos = ''.join(c for c in unicodedata.normalize('NFD', palabra_secreta) if unicodedata.category(c) != 'Mn')
        
    # Marcar el incio del juego (tiempo)
    inicio_juego = datetime.now()
    fecha_inicio_juego = inicio_juego.strftime("%d-%m-%Y")  # Fecha de inicio
    hora_inicio_juego = inicio_juego.strftime("%H:%M:%S")   # Hora de inicio

    # Bucle while donde si el usuario quiere jugar otra partida siga jugando pero siempre que la lista de palabras no utilizadas no este vacia
    while nueva_partida.lower() == "s" or len(lista_palabrasecreta_no_utilizadas) == 0:

        # Si el usuario ya ha jugado una partida (como mínimo) preguntar si quiere jugar otra partida
        if partidas > 0:
            nueva_partida = input("\n¿Quieres jugar otra vez? (s/n): ")

            while nueva_partida.lower() not in ["s", "n"]:  # Bucle while para evitar errores si la respuesta no es válida
                nueva_partida = input("Opción no válida. ¿Quieres jugar otra vez? (s/n): ")
        
            if nueva_partida.lower() == "s":    # Si el usuario quiere jugar otra vez preguntar si quiere añadir una nueva palabra al juego
                nueva_palabra = input("\n¿Quieres añadir una nueva palabra al juego? (s/n): ")

                while nueva_palabra.lower() not in ["s", "n"]:  # Bucle while para evitar errores si la respuesta no es válida
                    nueva_palabra = input("Opción no válida. ¿Quieres añadir una nueva palabra al juego? (s/n): ")

                # Si el usuario quiere añadir una nueva palabra hacer que introduzca la palbra que quiere añadir
                if nueva_palabra.lower() == "s":
                    nueva_palabra = input("Introduce la nueva palabra: ")

                    while nueva_palabra in lista_palabrasecreta_no_utilizadas:  # Bucle while para que si la palabra introducida ya esta en la lista de palabras no utilizadas vuelva a introducir una palabra
                        nueva_palabra = input("La palabra ya esta en el juego. Introduce la palabra: ")

                    lista_palabrasecreta_no_utilizadas.append(nueva_palabra)    # Añadir la palabra introducida por el usuario a la lista de palabras no utilizadas
                else:
                    print("No se añadirá una nueva palabra al juego")   # Si el usuario no quiere introducir una nueva palabra mostrar un mensaje que diga que no se añadirá una nueva palabra
                
                cambio_modo = input("\n¿Quieres cambiar de modo de juego? (s/n): ")    # Preguntar al usuario si quiere cambiar el modo de juego

                while cambio_modo.lower() not in ["s", "n"]:    # Bucle while para evitar errores si la respuesta no es válida
                    cambio_modo = input("Opción no válida. ¿Quieres cambiar de modo de juego? (s/n): ")
                
                # Si el usuario quiere cambiar de modo de juego mostrar de nuevo los diferentes modos
                if cambio_modo.lower() == "s":

                    print("\n MODOS DE JUEGO: ")
                    print("   1. Modo fácil")
                    print("   2. Modo difícil")
                    print("   3. Modo contra reloj fácil (1 minuto por palabra)")
                    print("   4. Modo contra reloj difícil (30 segundos por palabra)")

                    modo_nuevapartida = input("\nSelecciona el modo de juego (1/2/3/4): ")  # Preguntar al usuario por el modo que quiere jugar

                    while modo_nuevapartida not in ["1", "2", "3", "4"]:    # Bucle while para evitar errores si la respuesta no es válida
                        modo_nuevapartida = input("Opción no válida. Selecciona el modo de juego (1/2/3/4): ")
                    
                    while modo_nuevapartida == modo_juego:  # Bucle while para que si el modo seleccionado es igual al modo que ya ha jugado le diga al usuario que ya ha jugado ese modo y que le pida seleccionar otro modo
                        print("Ya has seleccionado este modo de juego en la partida anterior. Por favor, selecciona un modo de juego diferente.")
                        modo_nuevapartida = input("Selecciona el modo de juego (1/2/3/4): ")

                    modo_juego = modo_nuevapartida  # Asignar el modo seleccionado de la nueva partida a la variable modo de juego para que, si el usuario decide despues volver a jugar, que el modo utilizado anteriormente sea el de la nueva partida y no el de la primera
                
                cambio_categoria = input("\n¿Quieres cambiar de categoría? (s/n): ")    # Preguntar al usuario si quiere cambiar la categoria

                while cambio_categoria.lower() not in ["s", "n"]:   # Bucle while para evitar errores si la respuesta no es válida
                    cambio_categoria = input("Opción no válida. ¿Quieres cambiar de categoría? (s/n): ")
                
                # Si el usuario quiere cambiar de categoria mostrar de nuevo las diferentes categorias
                if cambio_categoria.lower() == "s":

                    print("\n CATEGORÍAS: ")
                    print("   1. General")
                    print("   2. Palabras con acentos")
                    print("   3. Palabras compuestas")
                    print("   4. Medicina")
                    print("   5. Ciencia")

                    categoria_nuevapartida = input("\nSelecciona la categoría (1/2/3/4/5): ")    # Preguntar al usuario por la categoria com la que quiere jugar

                    while categoria_nuevapartida not in ["1", "2", "3", "4", "5"]:  # Bucle while para evitar errores si la respuesta no es válida
                        categoria_nuevapartida = input("Opción no válida. Selecciona la categoría (1/2/3/4/5): ")
                    
                    while categoria_nuevapartida == categoria:
                        print("Ya has seleccionado esta categoría en la partida anterior. Por favor, selecciona una categoría diferente.")  # Bucle while para que si la categoria seleccionada es igual a la categoria que ya ha jugado le diga al usuario que ya ha jugado esa categoria y que le pida seleccionar otra categoria
                        categoria_nuevapartida = input("Selecciona la categoría (1/2/3/4/5): ")
                    
                if cambio_modo == "s" or cambio_categoria == "s":

                    if modo_juego == 1:
                    
                        if categoria == 1:
                            lista_palabrasecreta = general_facil

                        if categoria == 2:
                            lista_palabrasecreta = acentos_facil

                        if categoria == 3:
                            lista_palabrasecreta = compuestas_facil

                        if categoria == 4:
                            lista_palabrasecreta = medicina_facil

                        if categoria == 5:
                            lista_palabrasecreta = ciencia_facil

                    if modo_juego == 2:
                    
                        if categoria == 1:
                            lista_palabrasecreta = general_dificil

                        if categoria == 2:
                            lista_palabrasecreta = acentos_dificil

                        if categoria == 3:
                            lista_palabrasecreta = compuestas_dificil

                        if categoria == 4:
                            lista_palabrasecreta = medicina_dificil

                        if categoria == 5:
                            lista_palabrasecreta = ciencia_dificil

                    if modo_juego == 3:
                    
                        if categoria == 1:
                            lista_palabrasecreta = general_contra_reloj_facil

                        if categoria == 2:
                            lista_palabrasecreta = acentos_contra_reloj_facil

                        if categoria == 3:
                            lista_palabrasecreta = compuestas_contra_reloj_facil

                        if categoria == 4:
                            lista_palabrasecreta = medicina_contra_reloj_facil

                        if categoria == 5:
                            lista_palabrasecreta = ciencia_contra_reloj_facil

                    if modo_juego == 4:
                    
                        if categoria == 1:
                            lista_palabrasecreta = general_contra_reloj_dificil

                        if categoria == 2:
                            lista_palabrasecreta = acentos_contra_reloj_dificil

                        if categoria == 3:
                            lista_palabrasecreta = compuestas_contra_reloj_dificil

                        if categoria == 4:
                            lista_palabrasecreta = medicina_contra_reloj_dificil

                        if categoria == 5:
                            lista_palabrasecreta = ciencia_contra_reloj_dificil
                    
                    lista_palabrasecreta_no_utilizadas = lista_palabrasecreta.copy()
                
                # Iniciar las variables para la nueva partida
                errores = 0
                aciertos = 0
                palabra_secreta = random.choice(lista_palabrasecreta_no_utilizadas)
                lista_palabrasecreta_no_utilizadas = lista_palabrasecreta_no_utilizadas.remove(palabra_secreta)
                lista_partida = []
                lista_ahorcado = []
                lista_letras_partida = []

                if cambio_categoria.lower() == "s":    # Si el usuario ha cambiado la categoria ver si la nueva es la categoria de palabras con accentos

                    if categoria_nuevapartida != "2":   # Ver si la categoria de la nueva partida es la de palabras con accentos
                        palabra_secreta_sin_acentos = ''.join(c for c in unicodedata.normalize('NFD', palabra_secreta) if unicodedata.category(c) != 'Mn')
                    
                    categoria = categoria_nuevapartida  # Asignar la categoria seleccionada de la nueva partida a la variable categoria para que, si el usuario decide despues volver a jugar, que la categoria utilizada anteriormente sea la de la nueva partida y no la de la primera (esto lo aplico aquí para que no afecte al if anterior)

                else:   # Si el usuario no ha cambiado la categoria ver si la categoria es la de palabras con accentos

                    if categoria != "2":    # Ver si la categoria es la de palabras con accentos
                        palabra_secreta_sin_acentos = ''.join(c for c in unicodedata.normalize('NFD', palabra_secreta) if unicodedata.category(c) != 'Mn')
        
        # Iniciar la partida
        if nueva_partida.lower() == "s" or partidas == 0:

            # Marcar el inicio de la partida (tiempo de duración de la partida)
            inicio = datetime.now()
            fecha_inicio = inicio.strftime("%d-%m-%Y")  # Fecha de inicio
            hora_inicio = inicio.strftime("%H:%M:%S")   # Hora de inicio

            partidas += 1   # Sumar uno al número de partidas jugadas

            # Ver si el modo de juego seleccionado es de contra reloj (3 o 4)
            if modo_juego in ["3", "4"]:

                if modo_juego == "3":   # Si el modo es el 3, poner un tiempo límite de 60 segundos
                    tiempo_limite = 60
                else:   # Si el modo es el 4, poner un tiempo límite de 30 segundos
                    tiempo_limite = 30

                print("\nTienes ", tiempo_limite, " segundos para adivinar la palabra")    # Mostrar al usuario el tiempo límite

                tiempo_inicio = time.time()    # Marcar el tiempo de inicio para ver si al usuario se le acaba el tiempo límite

            while len(palabra_secreta) > len(lista_partida):
                lista_partida.append("_")   # Poner en la lista partida tantos _ como el número de carácteres de la palabra secreta
            
            # Mirar si hay espacios en la palabra secreta para cambiar la posición del espacio en la lista partida por un espacio
            if " " in palabra_secreta:

                for i in range(len(palabra_secreta)):

                    if palabra_secreta[i] == " ":
                        lista_partida[i] = " "

            # Bucle mientras el usuario no haya acertado la palabra o no haya cometido 8 errores y no haya completado la lista con la palabra ahorcado
            while len(lista_ahorcado) < 8 and "_" in lista_partida:

                # Si el usuario està jugando a alguno de los modos de contrareloj, ver si se le ha acabado el tiempo
                if modo_juego in ["3", "4"]:
                    tiempo_restante = tiempo_limite - (time.time() - tiempo_inicio)

                    if tiempo_restante <= 0:
                        print("\nSe ha acabado el tiempo")
                        break

                    print("\n", int(tiempo_restante), "segundos restantes")  # El usuario ve el tiempo que le falta

                print("\nPalabra secreta: ", " ".join(lista_partida))   # Print la lista partida con las letras acertadas

                adivinar_palabra = input("¿Quieres adivinar la palabra? (s/n): ")   # Preguntar al usuario si quiere adivinar la palabra

                while adivinar_palabra.lower() not in ["s", "n"]:   # Bucle while para evitar errores si la respuesta no es válida
                    adivinar_palabra = input("Opción no válida. ¿Quieres adivinar la palabra? (s/n): ")

                if adivinar_palabra.lower() == "s":    # Si el usuario quiere adivinar la palabra preguntarle por la palabra
                    palabra_usuario = input("Introduce la palabra que crees que es: ")

                    # Si la palabra introducida por el usuario es igual a la palabra secreta, contar los aciertos y añadir a la lista de aciertos la palabra del usuario
                    if palabra_usuario.lower() == palabra_secreta.lower() or palabra_usuario.lower() == palabra_secreta_sin_acentos.lower():
                        aciertos += lista_partida.count("_")
                        lista_aciertos.append(palabra_usuario)

                        lista_partida = list(palabra_secreta)

                    else:   # Si no es igual, entonces, contar los aciertos, mostrar un mensaje diciendo que la palabra es incorrecta y mostrar la lista ahorcado con todas las letras
                        errores += lista_partida.count("_")

                        print("Palabra incorrecta")

                        letra_ahorcado = list("AHORCADO")

                        if len(lista_ahorcado) < len(letra_ahorcado):
                            lista_ahorcado.extend(letra_ahorcado[len(lista_ahorcado):])

                        print(" ".join(lista_ahorcado))

                        lista_errores.append(palabra_usuario)   # Añadir a la lista de errores la palabra del usuario

                else:   # Si el usuario no quiere adivinar la palabra, preguntar por una letra
                    letra = input("Introduce una letra: ").lower()

                    while letra in lista_letras_partida:    # Evitar errores si la respuesta no es una letra
                        letra = input("Letra ya introducida. Introduce una letra: ").lower()

                    if letra not in letras_con_acento:

                        if letra not in abecedario:

                            while letra not in abecedario:    # Comprovar que la letra introducida este en el abecedario o sea una letra con acento, si no lo es preguntar por otra letra
                                letra = input("Tienes que introducuir una letra. Introduce una letra: ").lower()
                    
                    # Normalizar la letra del usuario (quitar acentos si no es la categoría 2)
                    letra_normalizada = letra
                    if letra in letras_con_acento and categoria != "2":
                        letra_normalizada = unicodedata.normalize("NFD", letra)[0].lower()

                    # Normalizar la palabra secreta para comparar
                    if categoria != "2":
                        palabra_para_comparar = palabra_secreta_sin_acentos.lower()

                    else:
                        palabra_para_comparar = palabra_secreta.lower()

                    # Comprobar si la letra está en la palabra
                    if letra_normalizada in palabra_para_comparar:
                        
                        for i in range(len(palabra_secreta)):   # Reemplazar todas las ocurrencias de la letra
                            
                            if palabra_para_comparar[i] == letra_normalizada:
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

                    lista_letras_partida.append(letra)

            # Si el usuario ha acertado la palabra, sumar uno a las partidas ganadas
            if "_" not in lista_partida:
                partidas_ganadas += 1

                # Marcar el tiempo final de la partida
                fin = datetime.now()
                fecha_fin = fin.strftime("%d-%m-%Y")
                hora_fin = fin.strftime("%H:%M:%S")

                total_segundos = int((fin - inicio).total_seconds())
                minutos = total_segundos // 60
                segundos = total_segundos % 60
                duracion = minutos, "minutos y ", segundos, "segundos"
                duracion = " ".join(map(str, duracion))

                # Mostrar al usuario la palabra secreta, un mensaje dando la enhorabuena, el numero de aciertos y errores y la duración de la partida
                print("\nPalabra secreta: ", " ".join(lista_partida))
                print("\n¡Felicidades, has adivinado la palabra!")
                print("\nNúmero de aciertos: ", aciertos)
                print("Número de errores: ", errores)
                print("\nDuración de la partida: ", duracion)

                # Registrar la partida
                linea = "\n -  | Inicio: ", fecha_inicio, " ", hora_inicio, " | Fin: ", fecha_fin, " ", hora_fin, " | Duración: ", duracion, " | Modo de juego: ", modo_juego, " | Categoría: ", categoria, " | Palabra secreta: ", palabra_secreta, " | Número de aciertos: ", aciertos, " | Número de errores: ", errores,"\n"

                with open("partidas_ahorcado.txt", "a", encoding="utf-8") as fichero_txt:
                    fichero_txt.write("".join(map(str, linea)))

                print("\nREGISTRANDO PARTIDA...")
                print("Partida registrada correctamente en 'partidas_ahorcado.txt'")

            # Si el usuario no ha acertado la palabra, sumar uno a las partidas perdidas
            else:
                partidas_perdidas += 1

                # Marcar el tiempo final de la partida
                fin = datetime.now()
                fecha_fin = fin.strftime("%d-%m-%Y")
                hora_fin = fin.strftime("%H:%M:%S")

                total_segundos = int((fin - inicio).total_seconds())
                minutos = total_segundos // 60
                segundos = total_segundos % 60
                duracion = minutos, "minutos y ", segundos, "segundos"
                duracion = " ".join(map(str, duracion))

                # Mostrar al usuario un mensaje diciendo que ha perdido, la palabra secreta, el numero de aciertos y errores y la duración de la partida
                print("\nHas perdido")
                print("\nLa palabra secreta era: ", palabra_secreta)
                print("\nNúmero de aciertos: ", aciertos)
                print("Número de errores: ", errores)
                print("\nDuración de la partida: ", duracion)

                # Registrar la partida
                linea = "\n -  | Inicio: ", fecha_inicio, " ", hora_inicio, " | Fin: ", fecha_fin, " ", hora_fin, " | Duración: ", duracion, " | Modo de juego: ", modo_juego, " | Categoría: ", categoria, " | Palabra secreta: ", palabra_secreta, " | Número de aciertos: ", aciertos, " | Número de errores: ", errores,"\n"

                with open("partidas_ahorcado.txt", "a", encoding="utf-8") as fichero_txt:
                    fichero_txt.write("".join(map(str, linea)))

                print("\nREGISTRANDO PARTIDA...")
                print("Partida registrada correctamente en 'partidas_ahorcado.txt'.")
    
    # Al finalizar el juego cerrar el fichero txt
    fichero_txt.close()
    
    # Marcar el tiempo final del juego
    fin_juego = datetime.now()
    fecha_fin_juego = fin_juego.strftime("%d-%m-%Y")
    hora_fin_juego = fin_juego.strftime("%H:%M:%S")

    total_segundos = int((fin_juego - inicio_juego).total_seconds())
    minutos = total_segundos // 60
    segundos = total_segundos % 60
    duracion = minutos, "minutos y ", segundos, "segundos"
    duracion = " ".join(map(str, duracion))
    
    # Mostrar al usuario un resumen del juego
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

else:   # Si el usuario no quiere empezar a jugar, finalizar el juego
    print("FIN DEL JUEGO")