# JUEGO DEL AHORCADO

import random

lista_palabrasecreta = ["Jirafa", "Lixivia", "Yunque", "Niquel", "Bucelario", "Cicuta", "Yuxtaposición", "Fulgido", "Guillotina", "Arado"]
palabra_secreta = random.choice(lista_palabrasecreta)
lista_partida = []
lista_ahorcado = []

while len(palabra_secreta) > len(lista_partida):
    lista_partida.append("_")

palabra_introducida = input("")