diccionario = {}

diccionario = dict()

# {llave : el valor en el cual queremos asociar. }

diccionario = {"total": 55}
diccionario ={"total": 55, "descuento": True, "Subtotal": 15}

print(diccionario)



elemento = {}

elemento['casa'] ='cody' # crea la llave con su valor
elemento['aasa20'] ='codsas'
elemento[(1,2,3)] ='esto es una tupla'
elemento['casa'] ='codo' # actualiza la llave con su valor#print(elemento)

print(len(elemento))

valor = elemento['casa']
print(valor)

print('casa' in elemento)

# get por defaut retorna None
# setdefault 

valor = elemento.get('casas', 'la llave ') 
print(valor)


valor = elemento.setdefault('casas', 7) 
print(valor)