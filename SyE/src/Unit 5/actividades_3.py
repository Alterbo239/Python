# Ejercicio 10

a = 10
b = a

print(id(a))
print(id(b))

# Ejercicio 11

edad = int(input("Edad: "))
tutor = False

if edad > 18 or tutor:
    print("Puede entrar.")

# Ejercicio 12

base = 10
altura = 5
area = base * altura
print(area)

# Ejercicio 13


def fahrenheit_a_celsius(f):
    """
    Convierte grados fahrenheit a grados celsius
    """

    # Formula de conversión
    return (f - 32) * 5 / 9


print(fahrenheit_a_celsius(64))
help(fahrenheit_a_celsius)
