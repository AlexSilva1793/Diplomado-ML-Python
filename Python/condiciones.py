resultado = 10

resultado = resultado == 10

if resultado:

    print("no diga mamadas merin yel")

else:
    print("callate parker")    



listado = []
nombre = 'cody'
casa = "corra"
"""
if listado:
    variable = listado
else:
    variable = nombre
"""
variable = listado or nombre or listado and casa

print(variable)