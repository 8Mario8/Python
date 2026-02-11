letra = input()
vocales = "aeiou"
if letra.islower():
    print("minuscula")
else:
    print("majuscula")
if letra in vocales:
    print("vocal")
else:
    print("consonant")