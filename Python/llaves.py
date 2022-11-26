from this import d


diccionario = {'a': 25, 'b': 35, 'c':52}

# keys
# values
# items

llaves = tuple(diccionario.keys())
print(llaves)

valores = tuple(diccionario.values())
print(valores)

elementos = tuple(diccionario.items())
print(elementos)



del diccionario['a']
valor = diccionario.pop('c') #1

diccionario.clear() # 2
print(diccionario) # 3