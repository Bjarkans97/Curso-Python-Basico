nom = input('¿Cual es su nombre?')
monto = input('¿Cuales fueron sus ventas?')

comision = round((int(monto)*0.13),2)

print(f'Hola {nom}, su comision es de ${comision}')