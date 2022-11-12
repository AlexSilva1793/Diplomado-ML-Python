

"""
print("....CONVERTIDOR DE DOLARES....")
texto = "...... Menu ......" 
texto = texto.center(30)
print(texto)
print(" 1. Pesos Argentinos \n 2. Pesos Colombianos \n 3. Pesos mexicanos")

codigo = int(input("favor ingrese el codigo de la moneda desea que convertir tus dolares: "))
#money = float(input("Ingresa el monto a convertir:  "))
########################################favor haces solo un menu en una vairable en comentario menu#############################################

if codigo == 1:
    money = float(input("Ingresa el monto a convertir argentino:  "))
    dolar_arg = 128.23
    Valor_Final = money / dolar_arg
    Valor_Final = round(Valor_Final, 2)
    Valor_Final = str(Valor_Final)

    print("ceuntas con $" + Valor_Final + " Dolares" )

# mejorar variables a convenir mas si es en casos con resultados de una sola variable o varias

elif codigo == 2:
    money = float(input("Ingresa el monto a convertir colombiano:  "))
    dolar_col = 4411.18
    Valor_Final = money / dolar_col
    Valor_Final = round(Valor_Final, 2)
    Valor_Final = str(Valor_Final)

    print("ceuntas con $" + Valor_Final + " Dolares" )
    
elif codigo == 3:
    money = float(input("Ingresa el monto a convertir mexicano:  "))
    dolar_mex = 20.53
    money = float(money) #error cometido en dodas las opciones
    Valor_Final = money / dolar_mex
    Valor_Final = round(Valor_Final, 2)
    Valor_Final = str(Valor_Final)

    print("ceuntas con $" + Valor_Final + " Dolares" )
    
else: 
    print("usted no sabe leer o es que no ve bien")


# ljust -> justificar a la izquierda
# rjust -> justificar a la derecha
# center -> centrar


dolar_mex = 20.53
dolar_col = 4411.18
dolar_arg = 128.23




menu = 
----------------------convierte y mira-----------------------
..................no todo es dinero chico dinero.............

"""


def convertidor_multiple(pais,monto):

  

# precio del dolar segun pais   
    
# que pais escogio el usuario
#diccionario = {"total": 55}


   # Argentina = {"Precio_Dolar": 128.23}
   # Colombia = {"Precio_Dolar": 4411.18}
   # Mexico = {"Precio_Dolar": 20.53}




    if pais == 1:
        Precio_Dolar = 128.23
        pais = "Argentina"
    elif pais == 2:
        Precio_Dolar = 4411.18
        pais = "Colombia"
    elif pais == 3:
        Precio_Dolar = 20.53
        pais = "Mexico"
    else:
        pais = False
        Convercion = "no se pudo"

    if pais == False:
        pass 
    else:    
        pais = pais
        #Proceso
        monto = float(monto)
        Convercion = monto / Precio_Dolar 
        Convercion = round(Convercion, 2)
        Convercion = str(Convercion)

    return print(Convercion)


menu = """
----------------------convierte y mira-----------------------
..................no todo es dinero chico dinero.............
 1. Pesos Argentinos \n 2. Pesos Colombianos \n 3. Pesos mexicanos
"""
print(menu)
pais_en = int(input("ingrese codigo de pais: "))
monto_en = float(input("cuanta plata: "))
convertidor_multiple(pais_en,monto_en)

"""

def suma(n1,n2):
  

    resultado = n1 + n2
    print(resultado)

numero_uno = int(input("Ingresa el primer número entero: "))
numero_dos = int(input("Ingresa el primer número entero: "))

suma(numero_uno,numero_dos)




def suma(n1,n2):
    #resultado = n1 + n2
    #return resultado

    
    return n1 + n2, "la funcion que mas"
    
numero_uno = int(input("Ingresa el primer número entero: "))
numero_dos = int(input("Ingresa el primer número entero: "))

resultado1, mensaje = suma(numero_uno,numero_dos)
print(resultado1)
print(mensaje)
"""