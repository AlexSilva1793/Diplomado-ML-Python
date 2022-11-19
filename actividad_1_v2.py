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
    'Papas Fritas Limón':2000,
    'Papas Fritas Pollo':2000,
    'Papas Fritas BBQ':2000,
    'Papas Fritas Pizza':2000,
    'Papas Fritas Frito':2000,
    'Papas Fritas Chile':2000,
    'Papas Fritas Paprika':2000
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
def sumarVentasDiasU(diasReferenciaVentas):
    p=0
    sumatoria=0
    ventasDiasU={}
    for g in dias:
        for i in range(len(diasReferenciaVentas)):
            sumatoria=sumatoria + diasReferenciaVentas[i,p]
        ventasDiasU.update({g:sumatoria})
        sumatoria=0
        p+=1
    return ventasDiasU

#sumar ventas por dia sobre todas las referencias
def sumarVentasDiasP(diasReferencia):
    p=0
    sumatoria=0
    ventasDiasP={}
    for g in dias:
        for i in range(len(diasReferencia)):
            sumatoria=sumatoria + diasReferencia[i,p]
        ventasDiasP.update({g:sumatoria})
        sumatoria=0
        p+=1
    return ventasDiasP

#Sumar las ventas por referencia de cada dia, se utilizaran variables auxiliares y se retorna un dict con las ventas
def sumarVentasReferenciasU(diasReferencia):
    p=0
    sumatoria=0
    ventasReferenciasU={}
    for g in referencias:
        for t in range(5):
            sumatoria=sumatoria + diasReferencia[p,t]
        ventasReferenciasU.update({g:sumatoria})
        sumatoria=0
        p+=1
    return ventasReferenciasU

#Sumar las ventas por referencia de cada dia, se utilizaran variables auxiliares y se retorna un dict con las ventas
def sumarVentasReferenciasP(diasReferenciaVentas):
    p=0
    sumatoria=0
    ventasReferenciasP={}
    for g in referencias:
        for t in range(5):
            sumatoria=sumatoria + diasReferenciaVentas[p,t]
        ventasReferenciasP.update({g:sumatoria})
        sumatoria=0
        p+=1
    return ventasReferenciasP

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
    return ventaMenor,ventaMayor

def mostrarMenorMayorReferecia(ventaMenorMayor,ventasPorValorReferenciaVentas):
    menor=ventaMenorMayor[0]
    mayor=ventaMenorMayor[1]
    print("+--------------------+----------+")
    print("|         Ventas Menores        |")
    print("+--------------------+----------+")
    print("|Referencia          |Valor     |")
    print("+--------------------+----------+")
    for t in range(len(menor)):
        menorTmp=ventasPorValorReferenciaVentas[menor[t]]
        Referencia=menor[t]
        cadena = "|{:<20}|{:>10}|".format(Referencia, menorTmp)
        print(cadena)
        print("+--------------------+----------+")
        
    print("+--------------------+----------+")
    print("|         Ventas Mayores        |")
    print("+--------------------+----------+")
    print("|Referencia          |Valor     |")
    print("+--------------------+----------+")
    for t in range(len(mayor)):
        mayorTmp=ventasPorValorReferenciaVentas[mayor[t]]
        Referencia=mayor[t]
        cadena = "|{:<20}|{:>10}|".format(Referencia, mayorTmp)
        print(cadena)
        print("+--------------------+----------+")
    return "Gracias"

def run():
    ingresar=ingresarVentas(diasReferencia,referencias,dias)
    ventasPorValorReferenciaUnidades=sumarVentasReferenciasU(ingresar[0])
    ventasPorValorReferenciaVentas=sumarVentasReferenciasP(ingresar[1])
    ventasPorValorDiaUnidades=sumarVentasDiasU(ingresar[0])
    ventasPorValorDiaVentas=sumarVentasDiasP(ingresar[1])
    ventasTotalSemanaUnidades=ventasTotalUnidades(ingresar[0])
    ventasTotalSemanaPesos=ventasTotalValor(ingresar[1])
    ventaMenorMayor=encontrarMayorMenor(ventasPorValorReferenciaVentas)
    print("Registro unidades por referencia")
    print(ingresar[0])
    print("******************************************")
    print("Registro de valor por referencia")
    print(ingresar[1])
    print("******************************************")
    print("Registro dias por total de unidades",end="=>")
    print(ventasPorValorDiaUnidades)
    print("******************************************")
    print("Registro dias por total de pesos",end="=>")
    print(ventasPorValorDiaVentas)
    print("******************************************")
    print("Registro referencias por total de unidades",end="=>")
    print(ventasPorValorReferenciaUnidades)
    print("******************************************")
    print("Registro referencias por total de pesos",end="=>")
    print(ventasPorValorReferenciaVentas)
    print("******************************************")
    print("Total de unidades en la semana",end="=>")
    print(ventasTotalSemanaUnidades)
    print("******************************************")
    print("Total de Pesos en la semana",end="=>")
    print(ventasTotalSemanaPesos)
    print("******************************************")
    mostrarMenorMayorReferecia(ventaMenorMayor,ventasPorValorReferenciaVentas)
    print("""
          *******************************
          |Integrantes:                 |
          |Santiago Mancera Guerrero    |
          |Yamith Andres Lopez Palacio  |
          |Diego Fernando Cuellar Alviz |
          |Sonia Milena Melo Garcia     |
          |Eivar Alexander Silva Gaitan |
          *******************************
          """)
    exit()
    
if __name__=='__main__':
    run()