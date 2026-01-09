#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos  resultados de todo el proceso (raíz y división).
import math
var1=float(input("Introduce un número: "))
raíz_cuadrada=math.sqrt(var1)
división_raíz_cuadrada=int(raíz_cuadrada/2)
print("El resultado de la raíz es: ", raíz_cuadrada)
print("El resultado de dividir entre 2 la raíz es: ", división_raíz_cuadrada)