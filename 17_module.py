# module => Nos ayuda a modularizar archivos, metodos y mas.

# Importar la información del sistema.
import sys
print(sys.path)

# Expresiones regulares
# Vamos a traer del texto solo los nuemros.
import re
text = 'Mi numero telefonico es 456 6456 4654 5464 654 6 y my codigo del pais es 67'
result = re.findall('[0-9]+', text)

print(result)

# fechas
import time
timestamp = time.time() # fecha computadora
print(timestamp)


local = time.localtime() # fecha para humanos
result = time.asctime(local)
print(result)


# Para saber la frecuencia de un numero en una lista.
import collections
numbers = [1,2,3,23,43,4,12,1,2,23,4,45,5,44,4,4,4,4,4,4]
counter = collections.Counter(numbers)
print(counter)