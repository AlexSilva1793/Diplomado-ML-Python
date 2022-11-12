
list_d = [10,45,54,15,56]
lista_f =["b","c","g"]
lista_z =["b","c","g"]
print(list_d[:])
lista_d = [10,45,54,15,56]


# [Stard:end:skip]
# [Stard:] -> Obtenemos los ultimos elementos (toma de la pocicion inicial)
# [:end] -> Obtenemos los primeros elementos (no toma la pocicion inicial)
# len cuanta los datos guardados
print(len(list_d))
# append agrega en el ultimo dato de la lista
list_d.append(15)

print(list_d[:])
# insert agrega y ubica en la posicion dada en el ultimo dato 
list_d.insert(1,30)
print(list_d[:])
# Extend combina las listas y con "+" puedde agragar mas de una
list_d.extend(lista_f+lista_z)

print(list_d[:])

# Sort ordena  de menor a mayor los int, float
lista_d.sort()
print(lista_d[:])
# Sort ordena  de mayor a menor los int, float
lista_d.sort(reverse=True)
print(lista_d)
# el operador in busca el dato y el not lo niega 

BUSCAR_C = 45 in lista_d

print(BUSCAR_C)





