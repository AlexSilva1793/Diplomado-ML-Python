def funtion_a(funtion_b):

    def funtion_c():
        print('nos encontramos en la funcion c')

    return funtion_c

@funtion_a
def saludar():
    print('Hola, nos encontramos en una funcion')

saludar()

