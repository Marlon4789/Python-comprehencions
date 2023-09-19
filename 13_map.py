# map => es ua función predefinida por python para hacer transformaciones y cumple con el concepto 'hof'

# Podemos usar el concepto 'hof' y 'lambda' 

numbers = [1, 2, 3, 4]
numbers_v2 = []
for i in numbers:
    numbers_v2.append(i * 2)

# función 'map'
numbers_v3 = list(map(lambda i: i * 2, numbers))

print(numbers)
print(numbers_v2)
print(numbers_v3)

# ejemplo con dos listas de diferente dimenciones.

number_1 = [1,2,3,4]
number_2 = [4,5,6]

result = list(map(lambda x, y: x + y, number_1, number_2))

print(result)

# ejercicio
