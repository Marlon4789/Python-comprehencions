# Lambdas => Son funciones anonimas que nos permite dar versatilidad y una sintaxis más corta.

def increment(x):
    return x + 1

result = increment(15)

print(result)

# Lambdas

increment_v2 = lambda x : x + 2

result_v2 = increment_v2(100)
print(result_v2)

# Ejemplo 2

full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}!!'

text = full_name('marlon', 'cuartas')
print(text)
