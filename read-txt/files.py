# Para leer un archivo txt

# abre el archivo
file = open('./texto.txt')
print(file.read())

# leer linea por linea
print(file.readline())
print(file.readline())
print(file.readline())


# Iterar linea por linea y saber cuando termina.
for line in file:
    print(line)

# cerrar el archivo para dejar de consumir memoria.
file.close()

# Para abrir y cerrar el archivo automaticamente.
with open('./texto.txt') as file:
    for line in file:
        print(line)






