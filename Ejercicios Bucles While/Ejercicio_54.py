#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el mensaje del acumulado es singular o plural.. . Con While
rep=True
while rep==True:
    num1=int(input("Introduce el primer número: "))
    num2=int(input("Introduce el segundo número: "))
    total=num1+num2
    print("El resultado de la suma:", total)
    rep=input("Deseas repetir la operación s/n: ")
    s=1
    n=-1
    if rep==s:
        rep==True
    else:
        rep==False