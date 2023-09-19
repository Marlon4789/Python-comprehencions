# Try - Except => para probar el codigo y capturas si existe algun error.

try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)

# podemos usar distintas logicas en un mismo 'try except'.

try:
    # 1
    print(0/0)
    # 2
    assert 1 != 1, 'Uno no es igual a uno.'

    # 3
    age = 10
    if age < 18:
        raise Exception('No se permite menores de edad')

except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)

print('hello')

