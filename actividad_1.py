#importamos numpy
import numpy as np
import random as ra
tablaVentas = np.zeros(35, dtype=np.int64).reshape(7, 5)
#variables
totalUnidades=[]
totalReferencias=[]
for j in range(7):
    totalUnidades.append(0)
    totalReferencias.append(0)

# Tablas ventas
for i in range(len(tablaVentas)):
    for t in range(5):
        tablaVentas[i, t]=ra.randint(0,30)
#       totalUnidades[i] += tablaVentas[i, t] 
        pass


totalUnidades = np.sum(tablaVentas, axis=0)  # suma por columnas Total unidades
totalReferencias = np.sum(tablaVentas, axis=1) # suma por filas Total ref


print(tablaVentas)
print(totalUnidades)
print(totalReferencias)










"""
for i in range(len(referencias)):
    for t in range(7):
        referencias[i, t]=0
        pass
"""

#if __name__=='__main__':
#   pass



#referencias = np.arange(35, dtype=np.int64).reshape(5, 7)
#tablaventas2 = np.full((7,5),2)
#tablasVentas3 = np.zeros((7,5)) 