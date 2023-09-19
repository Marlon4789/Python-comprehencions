# Para controlar errores en python.

# assert => para verificar un error.

suma = lambda x,y: x + y
#assert suma(2,2) == 54 # AssertionError

print('hola')

# Raise Exception => controlar un error o levantar un error.

age = 10
if age < 18:
    raise Exception('No se permite menores de edad')
