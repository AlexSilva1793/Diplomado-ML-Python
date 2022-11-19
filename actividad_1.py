#importamos librerias 
import random
import numpy as np

"""Basado en el código entregado de vectores que esta en el archivo de
inducción favor ajustar para que se determine el valor de ventas por
referencia y día teniendo en cuenta que las ventas son de una semana 
de lunes a viernes. Adicional determinar la venta mayor y la venta
menor indicando la referencia"""

diasReferencia = np.zeros(35, dtype=np.int64).reshape(7, 5)
referenciasPrecio = {'Papas Fritas Limón':1200,'Papas Fritas Pollo':1300, 'Papas Fritas BBQ':1000,'Papas Fritas Pizza':2000,'Papas Fritas Huevo Frito':2500,'Papas Fritas Chile':1400,'Papas Fritas Paprika':1600}
dias=['Lunes', 'Martes','Miercoles','Jueves','Viernes']
totalUnidadesDias=[]
referencias=list(referenciasPrecio.keys()) 


#ingresar ventas


for i in range(len(diasReferencia)):
  

    print(f"por favor ingresa las ventas para la refencia {referencias[i]} :")
    for t in range(5):
        print(f"del dia {dias[t]} :")
        diasReferencia[i,t]=random.randint(1, 10)
        print(diasReferencia[i,t])
   

#sumar ventas semanal por referencia unidad
p=0
sumatoriaUnidades=0
ventasTotales={}
for g in referencias:
    for t in range(5):
        sumatoriaUnidades=sumatoriaUnidades + diasReferencia[p,t]
    ventasTotales.update({g:sumatoriaUnidades})
    sumatoriaUnidades=0
    p=p+1

#Total de ventas por unidad cada dia
totalUnidadesDias=[]
totalUnidadesDias = np.sum(diasReferencia, axis=0)

#Total de ventas por valor cada dia



#sumar ventas semanal por referencia valor

#encontrar la venta mayor y menor durante la semana
print(f"\nVentas Totales de cada una de las referencias de papas \n{ventasTotales}")
print(diasReferencia)
print(f"\nTotal de ventas por unidad cada dia: {totalUnidadesDias}")
#print(f"\nTotal de ventas por valor cada dia: {totalValorDias}")

print("\nreferencia de papas mas vendida")
print([key for key, value in ventasTotales.items() if value == max(ventasTotales.values())]) #Max Ventas
print("\nreferencia de papas menos vendida")
print([key for key, value in ventasTotales.items() if value == min(ventasTotales.values())]) #Min Ventas

if __name__=='__main__':
    pass



