#Tipos de divisas
currencyTypesColombia={
    "USD":[4865.57,0.2],
    "CLP":[5.28,0.12],
    "ARS":[29.43,0.15],
    "MEX":[251.57,0.1]
}

currencyTypesUsa={
    "COL":[0.00020,0.1],
    "MEX":[0.052,0.12],
    "ARS":[0.0060,0.19],
    "CLP":[0.0011,0.2]
}

currencyTypesMexico={
    "USD":[19.34,0.2],
    "COL":[0.0039,0.2],
    "ARS":[0.12,0.2],
    "CLP":[0.021,0.2]
}

currencyTypesChile={
    "USD":[922.23,0.05],
    "COL":[0.19,0.15],
    "MEX":[47.68,0.11],
    "ARS":[5.58,0.12]
}

currencyTypesArgentina={
    "USD":[165.31,0.2],
    "MEX":[8.55,0.15],
    "COL":[0.034,0.1],
    "CLP":[0.18,0.2]
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