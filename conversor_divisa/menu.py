import os 
import time
import currencyTypes as monedas

menu_inicial=True
valor_suma_cambiar=0

def asignarMonedaCambiar(opcion):
    if opcion == 1:
        tmp = monedas.currencyTypesUsa
        tmp1 = f"monedas.currencyTypesUsa"
        tmp2 = monedas.currencyTypesUsa["OPERADOR_REALIZAR"]
    elif opcion == 2:
        tmp = monedas.currencyTypesColombia
        tmp1 = f"monedas.currencyTypesColombia"
    elif opcion == 3:
        tmp = monedas.currencyTypesChile
        tmp1 = f"monedas.currencyTypesChile"
    elif opcion == 4:
        tmp = monedas.currencyTypesMexico
        tmp1 = f"monedas.currencyTypesMexico"
    else:
        
        tmp = monedas.currencyTypesArgentina
        tmp1 = f"monedas.currencyTypesArgentina"
    return tmp,tmp1,tmp2

def menuInicial():
    while (menu_inicial):
        opcion = input("Bienvenido a la divisa CUN:\n1) Para comprar Dolares.\n2) Para comprar Pesos Colombianos.\n3) Para comprar Pesos Chilenos.\n4) Para comprar Pesos Mexicanos.\n5) Para comprar Pesos Argentinos.\n=>")
        if opcion.isdigit() and int(opcion) in range(1,6):
            os.system("cls")
            opcion=int(opcion)
            monedasHabilitadas=asignarMonedaCambiar(opcion)
            moneda_origen=monedasHabilitadas[0]
            tipo_pais=tuple(moneda_origen.keys())
            while (menu_inicial):
                opcion_1 = input(f"Por favor ingrese de donde es la monera con la que pagara:\n\n1) {tipo_pais[0]}.\n2) {tipo_pais[1]}.\n3) {tipo_pais[2]}.\n4) {tipo_pais[3]}.\n5) Volver al menú anterior.\n=>")
                if opcion_1.isdigit() and int(opcion_1) in range(1,6):
                    if opcion_1 == "5":
                        break
                    else:
                        procedimientoCambiar={}
                        procedimientoCambiar.update({"DESTINO":monedasHabilitadas[1]})
                        procedimientoCambiar.update({"ORIGEN":tipo_pais[int(opcion_1) - 1]})
                        procedimientoCambiar.update({"ORIGEN_VALOR":moneda_origen[tipo_pais[int(opcion_1) - 1]]})
                        procedimientoCambiar.update({"CANTIDAD":ingresarSumaCambiar(valor_suma_cambiar)})
                        procedimientoCambiar.update({"OPERADOR":monedasHabilitadas[2]})
                        os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
                        return procedimientoCambiar
                else:
                    print("Por favor seleciones una opción valida.")
                    time.sleep(2.0)
                    os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
                
        else:
            print("Por favor seleciones una opción valida.")
            time.sleep(2.0)
            os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear

def ingresarSumaCambiar(valor_suma_cambiar):
    while (menu_inicial):
        cantidad=input("Ingresa la cantidad que va a cambiar: ")
        if cantidad.isdigit():
            os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
            return int(cantidad)+valor_suma_cambiar
        else:
            os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear

def realizarOperacion(datos_operacion_cambio):
    #{'DESTINO': 'monedas.currencyTypesUsa', 'ORIGEN': 'COL', 'ORIGEN_VALOR': 0.0002, 'CANTIDAD': 1, 'OPERADOR': '*'}
    
    valorOrigen=datos_operacion_cambio["ORIGEN_VALOR"]
    operador=datos_operacion_cambio["OPERADOR"]
    #print(f"valorOrigen--{valorOrigen}--operador--{operador}")
    
    if operador == "*":
        resultadoCambio=float(datos_operacion_cambio["CANTIDAD"])*float(valorOrigen)
    else:
        resultadoCambio=float(datos_operacion_cambio["CANTIDAD"])/float(valorOrigen)
    
    print(f"su cantidad ingresada a la moneda {operador} es : {resultadoCambio}")
    exit()

if __name__=='__main__':
    datos_operacion_cambio=menuInicial()
    print(datos_operacion_cambio)
    realizarOperacion(datos_operacion_cambio)
    
    