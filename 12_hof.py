# Higher order function => es una funcion que puede recibir otra función.

# Funciones de orden superior.
'''
def increment(x):
    return x + 1

def high_ord_func(x, func):
    return x + func(x)

result = high_ord_func(2, increment)

print(result)

# ejemplo con Lambdas

increment_v2 = lambda x: x + 1

high_ord_func_v2 = lambda x, func: x + func(x)

result_v2 = high_ord_func_v2(2, increment_v2)

print(result_v2)

# Tambien se puede hacer esto.

result_v2 = high_ord_func_v2(2, lambda x: x + 2)
print(result_v2)

result_v2 = high_ord_func_v2(2, lambda x: x * 50)
print(result_v2)
'''
# ejercicio 

full_name = lambda name, last_name: f'{name} {last_name}'
result_1 = full_name('marlon', 'cuartas')


full_direction = lambda city, avenue: f'{city} {avenue}'
result_2 = full_direction('La Celia', 'Av. Las Americas')

high_ord_func = lambda full_name, full_direction: f'My names is {full_name} and I am live in {full_direction} and I am so happy for this!!'

sum_up = high_ord_func(result_1, result_2)
print(sum_up)



