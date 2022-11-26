from distutils.errors import CompileError


nombre = "camilo fabian"
apellido ="zapata"

completo = "Mr, "+nombre + " " + apellido

print(completo)

Completo2 = 'Mr, %s %s %s' %(nombre, apellido, "casa")
print(Completo2)

Completo3 = 'Mr {nombre} {apellido} {apellido2}'.format(nombre =nombre,
apellido =apellido,
apellido2 = 'juzman')


print(Completo3)

Completo4 = f"Mr, {nombre} {apellido} {20*40}"
print(Completo4)
print(type(Completo4))


