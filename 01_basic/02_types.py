###
# 01 - types()
# Python tiene varios tipos de datos
# integer, float, string, boolean, list, tuple, dict, range, set ...

"""
asi puedes hacer una cadena de texto multilínea
y si no lo asignas a nada...
se trata como un comentario

"""

print("int...")
print(type(10))
print(type(0))
print(type(-5))
print(type(10161519851498451561))

# float
print("float...")
print(type(3.4))
print(type(1.0))
print(type(1e3)) # notación científica, es lo mismo que 1000.0

# numeros complejos
print("complex...")
print(type(1 + 2j))

#cadenas de texto
print("string...")
print(type("hola mundo"))
print(type(""))
print(type("year"))

# Booleanos
print("bool...")
print(type(True))
print(type(False))
# Tambien podemos obtener un booleano a partir de una comparación
# Ejemplo
print(10 > 5) # esto devuelve True
print(10 < 5) # esto devuelve False

# usencia de un valor
print("NoneType...")
print(type(None))