#importamos numpy
import random
import numpy as np

"""Basado en el código entregado de vectores que esta en el archivo de
inducción favor ajustar para que se determine el valor de ventas por
referencia y día teniendo en cuenta que las ventas son de una semana 
de lunes a viernes. Adicional determinar la venta mayor y la venta
menor indicando la referencia"""

ingresarVentas=True
dias = np.zeros(35, dtype=np.int64).reshape(7, 5)
referencias = ['papas fritas','papas fritas 1', 'papas fritas 2','papa fritas 3','papa fritas 4','papa fritas 5','papa fritas 6']
"""
0-luneas
1-martes
2-miercoles
3-jueves
4-viernes
"""
for i in range(len(dias)):
    for g in referencias:
        print(f"por favor ingresa un valor {g}:")
        while(ingresarVentas):
            for t in range(5):
               dias[i,t]=random.randint(1, 100)
            ventasTotales={g:np.sum(dias[t])}
            ingresarVentas=False
        #print(f"Las ventas para la referencia {referencias[i]} fueron en total {np.sum(dias[i])}")
        print(ventasTotales)
        ingresarVentas=True

    
def ventaMayorMenor(dias):
    mayor = dias[0][0]
    menor = dias[0][0]
    for fila in dias:
        for valor in fila:
            if valor > mayor:
                mayor = valor
            if valor < menor:
                menor = valor
    print("De la matriz: ")
    print(dias)
    print(f"El menor es {menor} y el mayor es {mayor}")    
        
def ingresar():
    pass
    

if __name__=='__main__':
    ventaMayorMenor(dias)



