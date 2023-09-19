# Es la manera de como podemos controlar la ejecución de un iterable manualmente, como si fuera un 'for' pero de 1 en 1

# range => para ietrar
# next => para la siguiente iteración.
# iter => como tipo de objeto.

# Esto nos ayudara a no consumir recursos de memoria.

for i in range(1,11):
    print(i)

my_iter = iter(range(1,11))
print(my_iter)
print(next(my_iter)) # 1
print(next(my_iter)) # 2
print(next(my_iter)) # 3
print(next(my_iter)) # 4

