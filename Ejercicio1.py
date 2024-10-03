import os

def cuadrados(n):
    """Función que imprime los cuadrados de los números menores o iguales a n"""
    print(f"Calculando los cuadrados de los números del 1 al {n}...")
    for i in range(1, n + 1):
        print(f"{i}^2 = {i ** 2}")

def tabla_multiplicar(n):
    """Función que imprime la tabla de multiplicar de n"""
    print(f"Mostrando la tabla de multiplicar del número {n}...")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

def main():
    # Solicitar el número de 1 a 10
    while True:
        try:
            numero = int(input("Ingresa un número del 1 al 10: "))
            if 1 <= numero <= 10:
                break
            else:
                print("Por favor, ingresa un número entre 1 y 10.")
        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")

    # Solicitar la elección del usuario
    print("Opciones disponibles:")
    print("1. Elevar al cuadrado los números menores o iguales al ingresado.")
    print("2. Mostrar la tabla de multiplicar del número ingresado.")
    print("3. Realizar ambos procesos.")

    while True:
        try:
            eleccion = int(input("¿Qué opción eliges? (1, 2 o 3): "))
            if eleccion in [1, 2, 3]:
                break
            else:
                print("Por favor, selecciona una opción válida (1, 2 o 3).")
        except ValueError:
            print("Entrada inválida. Ingresa 1, 2 o 3.")

    # Ejecutar los procesos según la elección del usuario
    if eleccion == 1:
        # Solo ejecutar el proceso de los cuadrados
        cuadrados(numero)

    elif eleccion == 2:
        # Solo ejecutar el proceso de la tabla de multiplicar
        tabla_multiplicar(numero)

    elif eleccion == 3:
        # Crear un proceso paralelo para ejecutar ambos procesos simultáneamente
        pid = os.fork()

        if pid == 0:
            # Proceso paralelo: realiza el cálculo de los cuadrados
            cuadrados(numero)
        else:
            # Proceso original: muestra la tabla de multiplicar
            tabla_multiplicar(numero)
            os.wait()  # Espera a que el proceso paralelo termine

if __name__ == "__main__":
 main()
