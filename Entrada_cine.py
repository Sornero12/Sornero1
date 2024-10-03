print("------- Menú Entradas a cine --------")
print("1. Comprar entrada")
print("2. Ver precios")
print("3. Salir")

opcion =int(input("Por favor seleccione una opción"))

print("Ingrese el día ")
print("1. Lunes")
print("2. Martes")
print("3. Miercoles")
print("4. Jueves")
print("5. Viernes")
print("6. Sabado")
print("7. Domingo")

if opcion==1:
    print("Seleccionaste la opcion comprar entrada")
    precio_entrada=16000

    dia= int(input("selecciona el día: "))

    if dia==2:  
        descuento=0.10
        precio_final=precio_entrada*(1-descuento)
        print ("El dia seleccionado es martes, tiene descuento del 10%")

    elif dia==3:
        descuento=0.15
        precio_final=precio_entrada*(1-descuento)
        print ("El dia seleccionado es miercoles, tiene descuento del 15%")

    elif dia==4:
        descuento=0.05
        precio_final=precio_entrada*(1-descuento)
        print ("El dia seleccionado es jueves, tiene descuento del 5%")

    else:
        precio_final=precio_entrada
        print ("No hay descuentos disponibles")

    cantidad=int(input("¿Cuantas entradas deseas comprar?"))
    total_compra=precio_final*cantidad

    print("----- Tiquete de compra -----")
    print("Dia de la semana: ", dia)
    print("Precio unitario: ", precio_final)
    print("Cantidad de entradas: ", cantidad)
    print("Valor total a pagar: ", total_compra)
    print("---------------------------------------------")

elif opcion==2:
    print("Has seleccionado la opcion verlista de  precios")
    print("El precio regular de la entrada es: 16.000")
    print("Descuentos disponibles")
    print("Martes: 10% de descuento")
    print("Miercoles: 15% de descuento")
    print("Jueves: 5% de descuento")

elif opcion==3:
    print("Gracias por visitarnos. Regresa pronto")

else:
    print("Opcion no valida")