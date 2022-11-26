import os 
import time
import currencyTypes as monedas

menu_inicial=True
valor_suma_cambiar=0

def asignarMonedaCambiar(opcion):
    if opcion == 1:
        tmp = monedas.currencyTypesUsa
        tmp1 = "USA"
    elif opcion == 2:
        tmp = monedas.currencyTypesColombia
        tmp1 = "Colombia"
    elif opcion == 3:
        tmp = monedas.currencyTypesChile
        tmp1 = "Chile"
    elif opcion == 4:
        tmp = monedas.currencyTypesMexico
        tmp1 = "Mexico"
    else:        
        tmp = monedas.currencyTypesArgentina
        tmp1 = "Argentina"
    return tmp,tmp1

def menuInicial():
    while (menu_inicial):
        opcion = input("Bienvenido a la divisa CUN:\n1) Para comprar Dolares.\n2) Para comprar Pesos Colombianos.\n3) Para comprar Pesos Chilenos.\n4) Para comprar Pesos Mexicanos.\n5) Para comprar Pesos Argentinos.\n=> ")
        if opcion.isdigit() and int(opcion) in range(1,6):
            os.system("cls")
            opcion=int(opcion)
            monedasHabilitadas=asignarMonedaCambiar(opcion)
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
                        procedimientoCambiar.update({"ORIGEN_VALOR":moneda_origen[tipo_pais[int(opcion_1) - 1]]})
                        procedimientoCambiar.update({"CANTIDAD":ingresarSumaCambiar(valor_suma_cambiar)})
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
    os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
    destino=datos_operacion_cambio["DESTINO"]
    valorOrigen=float(datos_operacion_cambio["ORIGEN_VALOR"])
    cantidad=float(datos_operacion_cambio["CANTIDAD"])
    resultadoCambio=cantidad*valorOrigen 
    print(f"su cantidad ingresada a la moneda {destino} es : {resultadoCambio}")
    exit()

if __name__=='__main__':
    datos_operacion_cambio=menuInicial()
    print(datos_operacion_cambio)
    realizarOperacion(datos_operacion_cambio)
    
    