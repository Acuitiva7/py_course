###
# 03 - Casting de tipos
# A veces es necesario convertir un tipo de dato a otro, esto se llama casting
# En Python, podemos usar las funciones int(), float(), str(), bool() para hacer el casting de tipos

print("conversión de tipos")
print(type(int("100"))) 


# Solo se puede concatenar el mismo tipo de datos
print("100" + "2") # esto funciona porque ambos son strings
print(100 + 2) # esto funciona porque ambos son enteros
print("100" + str(2)) # esto funciona porque convertimos el entero a string
print(int("100") + 2) # esto funciona porque convertimos el string a entero

print((float("3.1416") + 2.0)) # esto convierte el string a float

print(2 + int("100"))
print("2" + str(100))
print("100" + str(2))

print("----")
print(int(3.1416)) # esto convierte el float a entero, pero pierde la parte decimal

print("-----")
# En el caso de los booleanos el único valor que se consiedera falso es el Cero
print(bool(3))
print(bool(0))
print(bool(-1))

print("-- Booleanos y Cadenas de texto---")
# En el caso de las cadenas de texto, cualquier cadena vacía se considera falsa
print(bool(""))
print(bool(" ")) # Aquí no marcara False pues hay un espacio en blanco en la cadena y se considera verdadero
print(bool("Hola Mundo"))


# También podemos redondear un número flotante a un número entero usando la función round()
print(round(3.1416)) # esto redondea a 3

# Banker's rounding o redondeo al par más cercano
# La función round() redondea al numero par mas cercano, 
# por lo que round(2.5) devuelve 2 y round(3.5) devuelve 4

print(round(2.5)) # esto redondea a 2
print(round(2.51)) # esto redondea a 3