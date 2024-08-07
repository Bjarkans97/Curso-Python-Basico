mi_texto = 'Esto es una prueba'

resultado = mi_texto[9] #Busca el caracter que se encuentra en ese indice.
resultado = mi_texto.index('a') #Busca el primer indice que coincida con lo requerido
resultado = mi_texto.index('n',1,19)

print(resultado)