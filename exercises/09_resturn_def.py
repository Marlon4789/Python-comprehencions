
name = input('Escribe tu nombre: ')

age = input('Escribe tu edad: ')

def info(name, age):
    set_resumen = []

    set_resumen.append(name)
    set_resumen.append(age)
    return 'info: ', set_resumen, len(set_resumen)

result = info(name, age)

print(result)