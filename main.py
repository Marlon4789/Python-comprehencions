# Este archivo es para importar modulos y funciones.

# Todo lo que se ejcute pasa por primero '__init__'
'''
from package.mod_1 import func_1, func_2 
from package.mod_2 import func_3, func_4

print(func_1())
print(func_2())
print(func_3())
print(func_4())
'''

# importar de forma directa 'package'

import package
print(package.URL)

print(package.mod_1.func_1())

