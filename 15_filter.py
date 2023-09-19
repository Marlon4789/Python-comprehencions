# filter => para filtrar elementos de una lista.

# recuerda que con filter se crea una nueva lista y no modifica el array original.

# Para saber cual numero es par.

numbers = [1,2,3,4,5,6]

new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers)