# r+ => para leer y escribir un archivo.
# w+ => escribir y leer un archivo pero lo sobre escribe.

with open('./texto.txt', 'w+') as file:
    for line in file:
        print(line)
    file.write('nueva linea añadida 1\n')
    file.write('nueva linea añadida 2\n')
    file.write('nueva linea añadida 3\n')
    file.write('nueva linea añadida 4\n')

