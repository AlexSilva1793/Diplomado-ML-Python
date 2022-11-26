#Tipos de divisas
currencyTypesColombia={
    "USD":4865.57,
    "CLP":5.28,
    "ARS":29.43,
    "MEX":251.57
}

currencyTypesUsa={
    "COL":0.00020,
    "MEX":0.052,
    "ARS":0.0060,
    "CLP":0.0011
}

currencyTypesMexico={
    "USD":19.34,
    "COL":0.0039,
    "ARS":0.12,
    "CLP":0.021
}

currencyTypesChile={
    "USD":922.23,
    "COL":0.19,
    "MEX":47.68,
    "ARS":5.58
}

currencyTypesArgentina={
    "USD":165.31,
    "MEX":8.55,
    "COL":0.034,
    "CLP":0.18
}

def asignarMonedaCambiar(opcion):
    if opcion == 1:
        tmp = currencyTypesUsa
        tmp1 = "USA"
    elif opcion == 2:
        tmp = currencyTypesColombia
        tmp1 = "Colombia"
    elif opcion == 3:
        tmp = currencyTypesChile
        tmp1 = "Chile"
    elif opcion == 4:
        tmp = currencyTypesMexico
        tmp1 = "Mexico"
    else:        
        tmp = currencyTypesArgentina
        tmp1 = "Argentina"
    return tmp,tmp1