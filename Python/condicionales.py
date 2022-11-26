
edad = int(input("escribe tu edad:  "))
# edad int(edad)



if edad > 18:
    texto = "ya esatas viejo cuentame que es de ti"
    texto = texto.rjust(40)
    print(texto)

elif edad == 18:

    print("mejor espera el otro año")

else:
    print("ja valla que le cambien el pañal")    


"""
listado = [1]
nombre = 'cody'

if listado:
    variable = listado
else:
    variable = nombre

variable = listado or nombre 

print(variable)









texto = "ya esatas viejo cuentame que es de ti"
print(type(texto))

print(texto)
"""