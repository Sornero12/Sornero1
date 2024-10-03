frutas=["mora","lulo","manzana","Fresa","banano"]
#muestra el tipo de dato
print (type(frutas))
#muestre la lista completa
print ("La lista de frutas es:" , frutas)
#agregar un elemento
frutas.append("kiwi")
print (frutas)
#acceder a un elemento de la lista
print ("La tercera fruta es " , frutas[2])
#eliminar el ultimo elemento de la lista
frutas.pop()
print(frutas)
#contar la cantidad de elementos
print ("la cantidad de frutas en la lista es: " ,len(frutas))
#ordernas la lista alfabeticamente
frutas.sort
print(frutas)
#eliminar un elemento especifico
frutas.remove("manzana")
print(frutas)