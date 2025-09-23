#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.
menores=int(input("Introduce el número de menores de 18 años que asisitiran al cine: "))
adultos=int(input("Introduce el número de adultos (mayores de 18 años) que asistiran al cine: "))
precio=12
descuento_menores=50
descuento_adultos=10
precio_final_menores=(precio-(precio*descuento_menores/100))*menores
precio_final_adultos=(precio-(precio*descuento_adultos/100))*adultos
print("Apicando un descuento del 50% a los menores de 18 años y un 10% a los adultos el precio total del cine para", menores, "menor/es es", precio_final_menores,"€ y para", adultos, "adulto/s es", precio_final_adultos,"€.")