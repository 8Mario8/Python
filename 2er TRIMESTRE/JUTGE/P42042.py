letra = input()
vocales = "aeiou"
if letra.islower():
    print("minuscula")
else:
    print("majuscula")
if letra.lower in vocales:
    print("vocal")
else:
    print("consonant")