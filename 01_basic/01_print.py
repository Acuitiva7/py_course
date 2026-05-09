# el modulo print funciona para imprimir mensajes en la consola
# se puede usar con comillas dobles o con una sola comilla

print("hola mundo....")
print('hola mundo con una sola comilla')
#Ahora llamamos a la funcion print y le estamos pasando 3 valores que al ejecutarlo lo mostrará en consola. Lo ha separado
print("python", "es", "genial")

print("python", "es", "brutal", sep= "-")
# sep es para especificr con que separador quiero que se muestre mi texto, por defecto si no lo especificamos
# el separador será el espacio entre palabras

print("Esto se imprime", end = " ") #el end lo que hace es modificar el salto de línea que se pone de manera predeterminada y puedo cambierlo po respacio en blanco para que el siguiente print o texto que añada se ponga seguido y no debajo
print("en una línea")

# print con números
print(20)
