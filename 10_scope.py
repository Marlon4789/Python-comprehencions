# el escope 

# Global => funciona en todas partes.
# Local => funciona solo en el bloque de codigo.

my_global = 100

def my_local():
    my_global = 255
    print(200 + my_global)

my_local()

