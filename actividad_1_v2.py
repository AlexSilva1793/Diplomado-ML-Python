#importamos librerias a utilizar en el flujo
import random
import numpy as np
"""
Enunciado de la actividad:
Basado en el código entregado de vectores que esta en el archivo de inducción favor ajustar para que
se determine el valor de ventas por referencia y día teniendo en cuenta que las ventas son de una semana 
de lunes a viernes. Adicional determinar la venta mayor y la venta menor indicando la referencia
"""
#se crea una matriz 7*5 con 0, donde las filas seran para las referencias y columnas para los dias
diasReferencia = np.zeros(35, dtype=np.int64).reshape(7, 5)
diasReferenciaVentas = np.zeros(35, dtype=np.int64).reshape(7, 5)
dias=['Lunes', 'Martes','Miercoles','Jueves','Viernes']
referenciasPrecio = {
    'Papas Fritas Limón':1200,
    'Papas Fritas Pollo':1300,
    'Papas Fritas BBQ':1000,
    'Papas Fritas Pizza':2000,
    'Papas Fritas Huevo Frito':2500,
    'Papas Fritas Chile':1400,
    'Papas Fritas Paprika':1600
    }
referencias=list(referenciasPrecio.keys())

#ingresar ventas
def ingresarVentas(diasReferencia,referencias,dias):
    for i in range(len(diasReferencia)):
        print(f"Por favor ingresa las ventas para la refencia {referencias[i]} :")
        for t in range(5):
            print(f"Del dia {dias[t]}",end='=>')
            print()
            diasReferencia[i,t]=random.randint(10, 20)
            print(diasReferencia[i,t])
            #diasReferencia[i,t]=capturarUnidades(dias[t])
            diasReferenciaVentas[i,t]=diasReferencia[i,t]*referenciasPrecio[referencias[i]]
    return diasReferencia,diasReferenciaVentas
    
#Se crea funcion para en caso que sea vacio o letra no se rompa el codigo e inserte 0
def capturarUnidades(dia):
    entrada=input(f"Del dia {dia}=>")
    if not entrada or not entrada.isdigit():
        return 0
    return int(entrada)

#sumar ventas por dia sobre todas las referencias
def sumarVentasDiasP(diasReferenciaVentas):
    p=0
    sumatoria=0
    ventasDiasTotales={}
    for g in dias:
        for i in range(len(diasReferenciaVentas)):
            sumatoria=sumatoria + diasReferenciaVentas[i,p]
        ventasDiasTotales.update({g:sumatoria})
        sumatoria=0
        p=p+1
    return ventasDiasTotales

#sumar ventas por dia sobre todas las referencias
def sumarVentasDiasPU(diasReferencia):
    p=0
    sumatoria=0
    ventasDiasTotales={}
    for g in dias:
        for i in range(len(diasReferencia)):
            sumatoria=sumatoria + diasReferencia[i,p]
        ventasDiasTotales.update({g:sumatoria})
        sumatoria=0
        p=p+1
    return ventasDiasTotales

#Sumar las ventas por referencia de cada dia, se utilizaran variables auxiliares y se retorna un dict con las ventas
def sumarVentasDiasU(diasReferencia):
    p=0
    sumatoria=0
    ventasTotales={}
    for g in referencias:
        for t in range(5):
            sumatoria=sumatoria + diasReferencia[p,t]
        ventasTotales.update({g:sumatoria})
        sumatoria=0
        p=+1
    return ventasTotales

#sumar todas las ventas por unidad
def ventasTotalUnidades(diasReferencia):
    return np.sum(diasReferencia)

#sumar todas las ventas por valor
def ventasTotalValor(diasReferenciaVentas):
    return np.sum(diasReferenciaVentas)

#encontrar la venta mayor y menor durante la semana por referencia
def encontrarMayorMenor(ventasTotales):
    ventaMayor=[key for key, value in ventasTotales.items() if value == max(ventasTotales.values())]
    ventaMenor=[key for key, value in ventasTotales.items() if value == min(ventasTotales.values())]
    return ventaMayor,ventaMenor

#encontrar mayor y menor en las ventas
def encontrarMayorMenor():
    print(f"\nValor total de ventas de cada referencia semanalmente:\n {totalValorReferenciaSemana}")
    print("\nreferencia de papas mas vendida")
    print([key for key, value in ventasTotales.items() if value == max(ventasTotales.values())]) #Max Ventas
    print("\nreferencia de papas menos vendida")
    print([key for key, value in ventasTotales.items() if value == min(ventasTotales.values())]) #Min Ventas
    pass

#encontrar ventas de unidades por cada referencia en la semana
def sumarUnidadesReferencias():
    #valor de ventas de cada referencia en la semana:
    totalValorReferenciaSemana=""
    totalUnidadReferencia=np.sum(diasReferencia, axis=1)

    for j in range(len(diasReferencia)):
        totalValorReferenciaSemana+=f"unidades referencia {referencias[j]} :{totalUnidadReferencia[j]} precio referencia {referenciasPrecio[referencias[j]]} total = {totalUnidadReferencia[j]*referenciasPrecio[referencias[j]]} \n "

    return totalValorReferenciaSemana

#encontrar ventas de pesos por cada referencia en la semana

def run():
    ingresar=ingresarVentas(diasReferencia,referencias,dias)
    ventasPorValorDiaUnidades=sumarVentasDiasPU(ingresar[0])
    ventasPorValorDiaVentas=sumarVentasDiasP(ingresar[1])
    ventasTotalSemanaUnidades=ventasTotalUnidades(ingresar[0])
    ventasTotalSemanaPesos=ventasTotalValor(ingresar[1])
                                            
    print("Registro unidades por referencia")
    print(ingresar[0])
    print("Registro de valor por referencia")
    print(ingresar[1])
    print("Registro dias por total de unidades")
    print(ventasPorValorDiaUnidades)
    print("Registro dias por total de pesos")
    print(ventasPorValorDiaVentas)
    print("Total de unidades en la semana")
    print(ventasTotalSemanaUnidades)
    print("Total de Pesos en la semana")
    print(ventasTotalSemanaPesos)
    
    exit()

if __name__=='__main__':
    run()