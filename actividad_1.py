#importamos librerias 
import random
import numpy as np

"""Basado en el código entregado de vectores que esta en el archivo de
inducción favor ajustar para que se determine el valor de ventas por
referencia y día teniendo en cuenta que las ventas son de una semana 
de lunes a viernes. Adicional determinar la venta mayor y la venta
menor indicando la referencia"""

diasReferencia = np.zeros(35, dtype=np.int64).reshape(7, 5)
diasReferenciaVentas = np.zeros(35, dtype=np.int64).reshape(7, 5)
referenciasPrecio = {
    'Papas Fritas Limón':1200,
    'Papas Fritas Pollo':1300,
    'Papas Fritas BBQ':1000,
    'Papas Fritas Pizza':2000,
    'Papas Fritas Huevo Frito':2500,
    'Papas Fritas Chile':1400,
    'Papas Fritas Paprika':1600
    }
dias=['Lunes', 'Martes','Miercoles','Jueves','Viernes']
totalUnidadesDias=[]

referencias=list(referenciasPrecio.keys())
#precios=list(referenciasPrecio.values())


#ingresar ventas


for i in range(len(diasReferencia)):
  

    print(f"por favor ingresa las ventas para la referencia {referencias[i]} :")
    for t in range(5):
        print(f"del dia {dias[t]} :")
        diasReferencia[i,t]=random.randint(1, 10)
        diasReferenciaVentas[i,t]=diasReferencia[i,t]*referenciasPrecio[referencias[i]] 
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

#Total de ventas de paquetes de papas cada dia: (colocar dias de la semana)
totalUnidadesDias=[]
totalUnidadesDias = np.sum(diasReferencia, axis=0)
totalUnidadesDiaNombres=""
for l in range(len(dias)):
    totalUnidadesDiaNombres+= f"\nEl dia {dias[l]} se vendieron {totalUnidadesDias[l]} paquetes de papas "


#Total valor venta diaria referencia

print(f"-----valor dia: {diasReferenciaVentas}")



#valor de ventas de cada referencia en la semana:
totalValorReferenciaSemana=""
#totalValorReferencia=[]
totalUnidadReferencia=np.sum(diasReferencia, axis=1)

for j in range(len(diasReferencia)):
   # totalValorReferencia.append(totalUnidadReferencia[j] * precios[j])

    totalValorReferenciaSemana+=f"unidades referencia {referencias[j]} :{totalUnidadReferencia[j]} precio referencia {referenciasPrecio[referencias[j]]} total = {totalUnidadReferencia[j]*referenciasPrecio[referencias[j]]} \n "



#encontrar la venta mayor y menor durante la semana
#print(f"\nVentas Totales de cada una de las referencias de papas \n{ventasTotales}")
print(f"\n Matriz ventas\n{diasReferencia}")
print(f"Total de unidades vendidas: {np.sum(diasReferencia)}")
print(f"Total Ventas en dinero {np.sum(diasReferenciaVentas)}")
print(f"\nTotal de ventas diario de papas: {totalUnidadesDiaNombres}")
#print(f"\nTotal de ventas por valor cada dia: {totalValorDias}")

#print(f"\nValor de ventas de cada referencia en la semana: {totalValorReferencia}")
print(f"\nValor total de ventas de cada referencia semanalmente:\n {totalValorReferenciaSemana}")
print("\nreferencia de papas mas vendida")
print([key for key, value in ventasTotales.items() if value == max(ventasTotales.values())]) #Max Ventas
print("\nreferencia de papas menos vendida")
print([key for key, value in ventasTotales.items() if value == min(ventasTotales.values())]) #Min Ventas

if __name__=='__main__':
    pass



