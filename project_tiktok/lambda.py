
# Lambda => se usa como funciones anónimas para crear funciones cortas y simples.

# También son útiles cuando se requieren funciones de orden superior (funciones que toman otras funciones como argumentos).

# o trabajar con métodos como => map, reduce, filter, sorted


# déjame un comentario si quieres saber más acerca de estos métodos.

# Función normal
def sum(x,y):
    return x + y

result = sum(2, 4)

print(result) # 6

# Función lambda

sum_v2 = lambda x, y: x + y

result_v2 = sum_v2(2,4)

print(result_v2) # 6


