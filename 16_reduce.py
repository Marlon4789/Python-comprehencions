# reduce => es un metodo para reducir los valores de una lista, tuple o set a un solo resultado.

import functools

numbers = [1,2,3,4]

# Explicandolo en una def normal
def accum(counter, item):
    print('counter => ', counter)
    print('item => ',item)
    return counter + item

result_v1 = functools.reduce(accum, numbers)

print(result_v1)
print('*********************')

result = functools.reduce(lambda counter, item: counter + item, numbers)

print(result)