#Scope 
animal = 'Leon' # Variable Global -> Función, Condición o Cliclo

def imprimir_animal():
    global animal
    animal = 'Ballena'

    # animal = 'Ballena' # variable local

    tipo = 'mamifero' # variable local

    print(animal)
    print(id(animal))


imprimir_animal()

print(animal)
print(id(animal))
