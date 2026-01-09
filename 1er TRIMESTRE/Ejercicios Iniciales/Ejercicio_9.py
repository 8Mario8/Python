#9. Programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas
segundos=float(input("Introduce el número de segundos: "))
minutos=segundos/60
horas=segundos/3600
print(segundos, "segundos son equivalentes a", minutos, "minutos o", horas, "horas.")