#importamos librerias 
import random
import numpy as np

"""Basado en el código entregado de vectores que esta en el archivo de
inducción favor ajustar para que se determine el valor de ventas por
referencia y día teniendo en cuenta que las ventas son de una semana 
de lunes a viernes. Adicional determinar la venta mayor y la venta
menor indicando la referencia"""

diasReferencia = np.zeros(35, dtype=np.int64).reshape(7, 5)
referencias = ['papas fritas','papas fritas 1', 'papas fritas 2','papa fritas 3','papa fritas 4','papa fritas 5','papa fritas 6']
dias=['Lunes', 'Martes','Miercoles','Jueves','Viernes']

#ingresar ventas
for i in range(len(diasReferencia)):
    for g in referencias:
        print(f"por favor ingresa las ventas para la refencia {g} :")
        for t in range(5):
            print(f"del dia {dias[t]} :")
            diasReferencia[i,t]=random.randint(1, 10)
            print(diasReferencia[i,t])

#sumar ventas semanal por referencia
p=0
sumatoria=0
ventasTotales={}
for g in referencias:
    for t in range(5):
        sumatoria=sumatoria + diasReferencia[p,t]
    ventasTotales.update({g:sumatoria})
    sumatoria=0
    p=p+1

#encontrar la venta mayor y menor durante la semana
print(ventasTotales)
print(max(ventasTotales, key=ventasTotales.get) )
print(min(ventasTotales, key=ventasTotales.get) )
print([key for key, value in ventasTotales.items() if value == max(ventasTotales.values())])
print([key for key, value in ventasTotales.items() if value == min(ventasTotales.values())])

if __name__=='__main__':
    pass



