"""

def promedio(p1,*args,p2):
    return sum(args) / len(args)

    print(p1)
    print(args)
    print(ps)

resultado = promedio(12,50,45,48,75,65,215,554,5,24,4)
print(resultado)


def promedio(p1,*args): # tupla
    #return sum(args) / len(args)

    print(p1)
    print(args)
    #print(p2)

promedio(12,50,45,48,75,65,215,554,5,24,4)


def usuarios(**kwargs): # Dict
    print(kwargs)
    print(type(kwargs))
"""
def combinacion(p1, p2,*args,**kwargs):
    print(args) 
    print(kwargs)
    

combinacion(1,2,3,4, cody=True, curso="python")        
    


# entre funciones debe haber dos saltos de lineas