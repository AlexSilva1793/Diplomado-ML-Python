"""def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32

mi_funtion = centigrados_a_farhenheit

print(type(mi_funtion))

print(mi_funtion(20))


"""

# lambda <parámetros> : <Cuerpo de la funtion> el lambda se debe grabar en u a variable
funtion_grados = lambda grados : grados * 1.8 + 32

print(funtion_grados(10))



sin_parametos = lambda : True

Parametros_default = lambda p1=10, p2=20, p3=30 : p1 + p2 +p3

asterisco = lambda *args, **kwargs: len(args) + len(kwargs)