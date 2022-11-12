import re


lista = [1,2,3,4,5,6]

tupla = (9,8,7,5,4,7)


resultado = zip(tupla, lista)
resultado1 =list(resultado)
print(resultado1)
resultado = zip(tupla, lista)
resultado2 =tuple(resultado)
print(resultado2)