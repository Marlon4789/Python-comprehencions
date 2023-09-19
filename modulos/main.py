import utils

# recurso importante => 
'''
import moduloconnombrelargo as m

m.función()  //Esto es igual a poner moduloconnombrelargo.función()
'''
# ejemplo 2

data = [
    {
        'Country': 'Bolivia',
        'Population': '500'
    },
    {
        'Country': 'Colombia',
        'Population': '300'
    }
]

def run():
    keys, values = utils.get_population()
    print(keys, values)

    country_name = input('Esocoge pais: ')

    result = utils.population_by_country(data, country_name)
    print(result)

# para ejecutar este archivo 'example.py' como un script para tener una dualidad y poderlo correr directamente.

# Se le llama: Entry point a esta ejecución.

if __name__ == '__main__':
    run()

