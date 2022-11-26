

"""
def suma(n1,n2):
  

    resultado = n1 + n2
    print(resultado)

numero_uno = int(input("Ingresa el primer número entero: "))
numero_dos = int(input("Ingresa el primer número entero: "))

suma(numero_uno,numero_dos)

"""


def suma(n1,n2):
    #resultado = n1 + n2
    #return resultado

    
    return n1 + n2, "la funcion que mas"
    
numero_uno = int(input("Ingresa el primer número entero: "))
numero_dos = int(input("Ingresa el primer número entero: "))

resultado1, mensaje = suma(numero_uno,numero_dos)
print(resultado1)
print(mensaje)