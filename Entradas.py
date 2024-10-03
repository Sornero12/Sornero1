#Diccionario lleno de nombres y edades

edades={"Juan":25,
        "Luis":15,
        "Maria":30,
        "Luz":40
        }


#Usar un for para recorrer el diccionario y mostrar las claves y valores
for nombre, edad in edades.items():
    print(f"{nombre} tiene {edad} años")
    
#Inicializar un diccionario vacío
edades={}

#Solicitamos al usuario cuantas entradas desea solicitar
cantidad=int (input("¿Cuántas personas desean ingresa?"))

#Usar un for para que se llene el diccionario con nombre y edades

for i in range(cantidad):
    nombre= input(f"Por favor ingrese el nombre de la persona {i+1}:")
    edad=int (input(f"Digite la edad de {nombre} :"))
    edades[nombre]=edad

#Mostrar la información de los pares clave y valor del diccionario

print("")