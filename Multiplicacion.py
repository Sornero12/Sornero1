#Solicitar al usuario un número
n=int(input("Por favor digite un número para revisir su resultado: "))

#Muestra la tabla de multiplicar, del 1 al 10

for i in range(1,11):
    resultado=n*i
    print(f"{n} x {i} = {resultado}")