

#Tipos de divisas
currencyTypesColombia={
    "USD":4948.00,
    "CLP":4948.00,
    "ARS":34.90,
    "MEX":3273.00
}

currencyTypesUsa={
    "COL":4948.00,
    "MEX":5077.54,
    "ARS":34.90,
    "CLP":3684.60,
}

currencyTypesMexico={
    "USD":4948.00,
    "COL":5077.54,
    "ARS":34.90,
    "CLP":3684.60,
}

currencyTypesChile={
    "USD":4948.00,
    "COL":5077.54,
    "MEX":34.90,
    "ARS":3684.60,
}

currencyTypesArgentina={
    "USD":4948.00,
    "MEX":5077.54,
    "COL":34.90,
    "ARS":3684.60,
}

#Tipos de nombre sobre los paises
paises= {
"COL":("COLOMBIA","COLOMBIANO","COLOMBIANA"),
"ARS":("ARGENTINA","ARGENTINO"),
"USA":("ESTADOS UNIDOS","USA"),
"CLP":("CHILENO","CHILE","CHILENA"),
"MEX":("MEXICANO","MEXICO","MEXICANA")
}

#encontrar las siglas del pais
def encontrarSiglas(siglaEncontrar):
    for i in paises.keys():
        if siglaEncontrar in paises[i]:
            siglaOrigen=i
            return siglaOrigen