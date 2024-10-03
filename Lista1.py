colores={"red":"rojo","blue":"azul","white":"blanco","yellow":"amarillo"}
# Muestra tipo de dato
print (type(colores))
# Muestra los valores del diccionario
print(colores)
# Acceder al valor de una clave
print ("El color blue en Español es: ",colores["blue"])

# Agregar un elemento al diccionario
colores["black"]="negro"
print(colores)

#actualizar el valor de una clave en el diccionario
colores["green"]="verde"
print(colores)