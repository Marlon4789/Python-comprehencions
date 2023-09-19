
# Transformar una 'list' con map

# Creamos una list de dict para este ejercicio.

items = [
    {
        'product': 'camisa',
        'price': 100
    },
    {
        'product': 'pantalones',
        'price': 400
    },
    {
        'product': 'sombrero',
        'price': 600
    }
]

# Vamos a transformar esta list es una list de numeros.

# Que muestre en una list solo los numeros de los precios.

prices = list(map(lambda item: item['price'], items))

print(prices)

# Ahora agreguemos un nuevo atributo 'taxes' 'impuestos' a este list o 'array'

# copy() => para copiar el array y asi no tener que modificar el original.

def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19
    return new_item

new_items = list(map(add_taxes, items))

print(new_items)
print('Old items')
print(items)



# ejercicio
'''
group_music = [
    {
        'Grupo musical': 'blackpink',
        'cancion': 'savage',
        'pais': 'japon'
    },
    {
        'Grupo musical': 'taylor swift',
        'cancion': 'red',
        'pais': 'USA'
    },
    {
        'Grupo musical': 'Linkin Park',
        'cancion': 'crying',
        'pais': 'Britanico'
    }
]

def add_info(new_info):
    new_info['genero'] =  'rock'
    return new_info

add_new_info = list(map(add_info, group_music))
print(add_new_info)
'''