# Nombrar variable
var_total=50

# Sumar o restar valor introducido por pantalla
while var_total<=60:
    num=int(input("Introduce un número: "))
    if num%2==0:
        var_total=var_total+num
    else:
        var_total=var_total-num
    print(var_total)
print("Fin de programa")