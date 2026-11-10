# Ejercicio integrador


def calculadora():
    """
    Calculadora de operaciones matemáticas básicas.
    """
    numero_1 = int(input("Introduzca el primer número: "))
    numero_2 = int(input("Introduzca el segundo número: "))

    # Operaciones con print-f().
    print(f"{numero_1} + {numero_2} = {numero_1 + numero_2}")
    print(f"{numero_1} - {numero_2} = {numero_1 - numero_2}")
    print(f"{numero_1} * {numero_2} = {numero_1 * numero_2}")
    print(f"{numero_1} / {numero_2} = {numero_1 / numero_2}")


calculadora()
