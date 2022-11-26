"""
e = 'e' # variable Global

def funtion_principal():
    a = 'a' # variable Local
    b = 'b'

    def funtion_aninada():
        c = 'c' # variable local

        nonlocal b 
        b = 'cambio de valor'

        print(a)
        print(b)
        print(id(b))

        print(e)

    funtion_aninada()
    print(b)
    print(id(b))
funtion_principal()




def saludar():
    
    def mostrar_mensaje():
        print('esta es la manera de infrigir')

    return mostrar_mensaje


respuesta = saludar()

respuesta()
"""



def saludar(username):
    mensaje = f'hola {username}' # variable Local

    def mostrar_mensaje(): # anidada
        print(mensaje)

    return mostrar_mensaje

username = 'cody'
respuesta = saludar(username)

respuesta()
