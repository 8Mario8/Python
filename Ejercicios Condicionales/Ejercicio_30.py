#30. Realiza un programa que controle si la longitud de una frase introducida por teclado es igual, menor o mayor de 11 caracteres. Utiliza elif
frase=input("Introduce una frase: ")
if len(frase)==11:
    print("La longitud de la frase es igual a 11 caracteres.")
elif len(frase)<11:
    print("La longitud de la frase es menor a 11 caracteres.")
else:
    print("La longitud de la frase es mayor a 11 caracteres.")
