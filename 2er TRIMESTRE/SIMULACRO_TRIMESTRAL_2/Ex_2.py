contrasenya = "abc123-Password1-1234-Admin2024-test"

lista = contrasenya.split("-")

#Control seguridad
for x in lista:
    numletras = 0
    numnumeros = 0
    numcaracteres = 0

    for j in x:
        if j.isnumeric():
            numnumeros += 1
        elif j.isalpha():
            numletras += 1
        else:
            numcaracteres += 1

    if numcaracteres == 0 and len(x) >= 8 and numnumeros > 1 and numletras > 1:
        print("La contraseña ", x, "es segura")
    
    if numcaracteres == 0 and len(x) < 8 and (numnumeros >= 1 or numletras >= 1):
        print("La contraseña ", x, "es débil")
    
    if numcaracteres >= 1:
        print("La contraseña ", x, "es inválida")