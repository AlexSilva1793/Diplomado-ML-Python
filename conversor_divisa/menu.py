import os 
import time
import currencyTypes as monedas

menu_inicial=True

def asignarMonedaCambiar(opcion):
    if opcion == 1:
        tmp = monedas.currencyTypesUsa
        tmp1 = f"monedas.currencyTypesUsa"
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
    return tmp,tmp1

def menuInicial():
    while (menu_inicial):
        opcion = input("""
                    Bienvenido a la divisa CUN:
                    1) Para comprar Dolares.
                    2) Para comprar Pesos Colombianos.
                    3) Para comprar Pesos Chilenos.
                    4) Para comprar Pesos Mexicanos.
                    5) Para comprar Pesos Argentinos.
                    =>""")
        if opcion.isdigit() and int(opcion) in range(1,6):
            os.system("cls")
            opcion=int(opcion)
            monedasHabilitadas=asignarMonedaCambiar(opcion)
            moneda_origen=monedasHabilitadas[0]
            tipo_pais=tuple(moneda_origen.keys())
            while (menu_inicial):
                opcion_1 = input(f"""
                    Por favor ingrese de donde es la monera con la que pagara:
                    1) {tipo_pais[0]}.
                    2) {tipo_pais[1]}.
                    3) {tipo_pais[2]}.
                    4) {tipo_pais[3]}.
                    5) Volver al menú anterior.
                    =>""")
                os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
                if opcion_1.isdigit() and int(opcion_1) in range(1,6):
                    if opcion_1 == "5":
                        break
                    else:
                        procedimientoCambiar={}
                        procedimientoCambiar.update({"DESTINO":monedasHabilitadas[1]})
                        procedimientoCambiar.update({"ORIGEN":tipo_pais[int(opcion_1)]})
                        procedimientoCambiar.update({"CANTIDAD":ingresarSumaCambiar()})
                        os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
                        return procedimientoCambiar
                else:
                    print("""
                          Por favor seleciones una opción valida.""")
                    time.sleep(2.0)
                    os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
                
        else:
            print("""
                  Por favor seleciones una opción valida.""")
            time.sleep(2.0)
            os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear

def ingresarSumaCambiar():
    while (menu_inicial):
        cantidad=input("""
                       Ingresa la cantidad que va a cambiar: """)
        if cantidad.isdigit():
            os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear
            return cantidad
        else:
            os.system("cls") # Si estás en Unix (Mac o Linux) cambia cls por clear

if __name__=='__main__':
    print(menuInicial())
    print("Hola")