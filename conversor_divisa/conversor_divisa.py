import currencyTypes as monedas

def limpiarCaracteres(origenPais, destinoPais):
    tmp1=origenPais.upper().replace(" ","").replace("Í","I").replace("Ú","U").replace("Á","A").replace("Ó","O").replace("É","E").replace("É","E")
    tmp2=destinoPais.upper().replace(" ","").replace("Í","I").replace("Ú","U").replace("Á","A").replace("Ó","O").replace("É","E").replace("É","E")
    if tmp1.isalpha() and tmp2.isalpha(): 
        print("si son letras")
    else:
        pass

def ingresarPais():
    origenPais = input("Ingresa el pais origen se encuentra=> ")
    siglaOrigenPais = monedas.encontrarSiglas(origenPais.upper().replace(" ","").replace("Í","I").replace("Ú","U").replace("Á","A").replace("Ó","O").replace("É","E").replace("É","E"))
    destinoPais = input("Ingresa el pais destino se encuentra=> ")
    siglaDestinoPais = monedas.encontrarSiglas(destinoPais.upper().replace(" ","").replace("Í","I").replace("Ú","U").replace("Á","A").replace("Ó","O").replace("É","E").replace("É","E"))
    print(f"origenPais--{origenPais}--{siglaOrigenPais}--destinoPais--{destinoPais}--{siglaDestinoPais}")


if __name__=='__main__':
    ingresarPais()
#print(f"Origen de la moneda: {tmpOrigenPais} para convertir a la moneda del pais {tmpDestinoPais}")

