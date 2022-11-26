#import os 
#import time
import currencyTypes as monedas


menu_inicial=True
valor_suma_cambiar=0

def menuInicial():
    while (menu_inicial):
        opcion = input("Bienvenido a la divisa CUN:\n1) Quiero Dolares.\n2) Quiero Pesos Colombianos.\n3) Quiero Pesos Chilenos.\n4) Quiero Pesos Mexicanos.\n5) Quiero Pesos Argentinos.\n=> ")
        if opcion.isdigit() and int(opcion) in range(1,6):
            #os.system("cls")
            opcion=int(opcion)
            monedasHabilitadas=monedas.asignarMonedaCambiar(opcion)
            moneda_origen=monedasHabilitadas[0]
            tipo_pais=tuple(moneda_origen.keys())
            while (menu_inicial):
                opcion_1 = input(f"Por favor ingrese de donde es la monera con la que pagara:\n\n1) {tipo_pais[0]}.\n2) {tipo_pais[1]}.\n3) {tipo_pais[2]}.\n4) {tipo_pais[3]}.\n5) Volver al menú anterior.\n=> ")
                if opcion_1.isdigit() and int(opcion_1) in range(1,6):
                    if opcion_1 == "5":
                        break
                    else:
                        procedimientoCambiar={}
                        procedimientoCambiar.update({"DESTINO":monedasHabilitadas[1]})
                        procedimientoCambiar.update({"ORIGEN":tipo_pais[int(opcion_1) - 1]})
                        procedimientoCambiar.update({"ORIGEN_VALOR":moneda_origen[tipo_pais[int(opcion_1) - 1]][0]})
                        procedimientoCambiar.update({"ORIGEN_VALOR_PORCENTAJE":moneda_origen[tipo_pais[int(opcion_1) - 1]][1]})
                        procedimientoCambiar.update({"CANTIDAD":ingresarSumaCambiar(valor_suma_cambiar)})
                        #{'DESTINO': 'Colombia', 'ORIGEN': 'USD',
                        #'ORIGEN_VALOR': 4865.57, 'ORIGEN_VALOR_PORCENTAJE': 0.2, 'CANTIDAD': 1000000}
                        #os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
                        return procedimientoCambiar
                else:
                    print("Por favor seleciones una opción valida.")
                    #time.sleep(2.0)
                    #os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
                
        else:
            print("Por favor seleciones una opción valida.")
            #time.sleep(2.0)
            #os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear

def ingresarSumaCambiar(valor_suma_cambiar):
    while (menu_inicial):
        cantidad=input("Ingresa la cantidad que va a cambiar: ")
        if cantidad.isdigit():
            #os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
            return int(cantidad)+valor_suma_cambiar
        #else:
            #os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear

def realizarOperacion(datos_operacion_cambio):
    destino=datos_operacion_cambio["DESTINO"]
    valorOrigen=float(datos_operacion_cambio["ORIGEN_VALOR"])
    cantidad=datos_operacion_cambio["CANTIDAD"]
    porcentaSobreOperacion=float(datos_operacion_cambio["ORIGEN_VALOR_PORCENTAJE"])
    ganancia=round(valorOrigen*porcentaSobreOperacion,2)
    resultadoCliente=round((valorOrigen-ganancia)*cantidad, 2)
    precioOriginal=round(valorOrigen*cantidad,2)
    print(f"La ganancia sobre la transacción es de: {precioOriginal-resultadoCliente}, el precio neto es: {precioOriginal} y el cambio para el cliente es: {resultadoCliente}")

    return True

if __name__=='__main__':
    datos_operacion_cambio=menuInicial()
    realizarOperacion(datos_operacion_cambio)
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
    
    