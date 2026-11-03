import math
import random

## U2_01


def main_U2_01():
    print("Ejercicio 1:")
    fizzbuzz()


FIZZ = "fizz"
BUZZ = "buzz"


def fizzbuzz():
    for i in range(100):
        num = i + 1
        if num % 3 == 0 and num % 5 == 0:
            print(FIZZ + BUZZ)
        elif num % 3 == 0:
            print(FIZZ)
        elif num % 5 == 0:
            print(BUZZ)
        else:
            print(num)


## Fin U2_01


## U2_02


def main_U2_02():
    nombre = "Alberto Zamora Landete"
    calle_tipo = "C/"
    calle = "Ruzafa"
    calle_num = "78"
    calle_puerta = "8"
    codigo_psotal = "46006"
    localidad = "Valencia"
    pais = "España"

    print("Ejercicio 2:")
    direccion_postal(
        nombre,
        calle_tipo,
        calle,
        calle_num,
        calle_puerta,
        codigo_psotal,
        localidad,
        pais,
    )


def direccion_postal(
    nombre, calle_tipo, calle, calle_num, calle_puerta, codigo_psotal, localidad, pais
):
    print(nombre)
    print(calle_tipo, calle + ",", "numero", calle_num + ",", "puerta", calle_puerta)
    print("CP", codigo_psotal, "(" + localidad + ", " + pais + ")")


## Fin U2_02

## U2_03


def main_U2_03():
    print("Ejercicio 3:")
    saludo_personalizado()
    print()


def saludo_personalizado():
    nombre = input("Por favor, introduzca su nombre: ")
    print(f"¡Hola, {nombre}!")


## Fin U2_03

## U2_04


def main_U2_04():
    print("Ejercicio 4:")
    importe_cuenta()


def importe_cuenta():
    importe_inicial = float(input("Introduzca el importe de la comida: "))
    porcentaje_impuesto = int(is_porcentaje_impuesto_real(-1))

    impuesto_calculado = impuesto_precio(importe_inicial, porcentaje_impuesto)
    propina = impuesto_precio(importe_inicial, 18)

    precio_total = importe_inicial + impuesto_calculado + propina

    print("Precio inicial: ", round(importe_inicial, 2), "€")
    print("Impuesto: ", round(impuesto_calculado, 2), "€")
    print("Propina: ", round(propina, 2), "€")
    print("Total a pagar: ", round(precio_total, 2), "€")


def is_porcentaje_impuesto_real(impuesto):
    num = int(impuesto)
    if num < 0 or num > 100:
        num = is_porcentaje_impuesto_real(
            input("Introduzca el porcentaje de impuesto: ")
        )
    else:
        num = impuesto

    return num


def impuesto_precio(importe, porcentaje):
    return importe * porcentaje / 100


## Fin U2_04

## U2_05


def main_U2_05():
    print("Ejercicio 5:")
    n = int(input("Introduzca un numero entero: "))
    print("Suma iterativa:", suma_iteratva(n))
    print("Suma recursiva:", suma_recursiva(n))
    print("Expresión:", n * (n + 1) / 2)


def suma_iteratva(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i

    return sum


def suma_recursiva(n):
    if n <= 1:
        return n
    else:
        return n + suma_recursiva(n - 1)


## Fin U2_05

## U2_06


def main_U2_06():
    print("Ejercicio 6:")
    n = int(introducir_numero(-1))
    calc_interes(n)


INTERES_ANUAL = 4


def introducir_numero(n):
    num = int(n)
    if num < 0:
        num = introducir_numero(input("Introduce un numero entero: "))

    return num


def calc_interes(n):
    for i in range(3):
        interes = n * INTERES_ANUAL / 100
        n += interes
        print("Interes del año", i + 1, "=", round(interes, 2))
        print("Año", i + 1, "=", round(n, 2))


## Fin U2_06

## U2_07


def main_U2_07():
    print("Ejercicio 7:")

    latitud1 = int(introducir_valores(200, "latitud", -90, 90))
    longitud1 = int(introducir_valores(200, "longitud", -180, 180))
    latitud2 = int(introducir_valores(200, "latitud", -90, 90))
    longitud2 = int(introducir_valores(200, "longitud", -180, 180))

    print(distancia_tierra(latitud1, longitud1, latitud2, longitud2))


R_TERRESTE = 6371.01


def introducir_valores(n, tipo, g, g2):
    valor = float(n)
    if g < valor < g2:
        valor = n
    else:
        print("Introduzca una", tipo, "que esté comprendida entre ", g, "y", g2)
        valor = introducir_valores(input(), tipo, g, g2)

    return valor


def distancia_tierra(latitud1, longitud1, latitud2, longitud2):
    grados_lat1 = math.radians(latitud1)
    grados_long1 = math.radians(longitud1)
    grados_lat2 = math.radians(latitud2)
    grados_long2 = math.radians(longitud2)

    math.acos(max(-1.0, min(grados_lat1, 1.0)))

    return R_TERRESTE * math.acos(
        math.sin(grados_lat1) * math.sin(grados_lat2)
        + math.cos(grados_lat1)
        * math.cos(grados_lat2)
        * math.cos(grados_long1 - grados_long2)
    )


## Fin U2_07

## U2_08


def main_U2_08():
    print("Ejercicio 8:")
    grados = float(input("Introduzca una temperatura en grados Celsius: "))
    print(grados, "º ->", celsius_a_fahrenheit(grados), "Fahrenheit.")
    print(grados, "º ->", celsius_a_kelvin(grados), "Kelvin.")


def celsius_a_fahrenheit(cel):
    return round(cel * 9 / 5 + 32, 2)


def celsius_a_kelvin(cel):
    return round(cel + 273.15, 2)


## Fin U2_08

## U2_09


def main_U2_09():
    print("Ejercicio 9:")
    num = introduce_numeros(-1)
    print(calcular_valores(num))


def introduce_numeros(n):
    valor = int(n)
    if 1000 <= valor <= 9999:
        valor = n
    else:
        valor = introduce_numeros(
            input("Introduzca un valor entero de 4 cifras (1000 - 9999): ")
        )

    return valor


def calcular_valores(n):
    suma = 0
    for i in range(4):
        suma += int(n[i])

    return suma


## Fin U2_09

## U2_010


def main_U2_10():
    print("Ejercicio 10:")
    edad = int(input("Introduzca su edad: "))
    print("Su edad en edad canina es: ", edad_humana_a_canina(edad))


HUMANO_A_CANINO_DOS_PRIMEROS_ANYOS = 10.5
HUMANO_A_CANINO = 4


def edad_humana_a_canina(n):
    edad = 0
    if n <= 0:
        edad = "Error, no se puede convertir una edad negativa"
    else:
        if n > 2:
            n -= 2
            edad += HUMANO_A_CANINO_DOS_PRIMEROS_ANYOS * 2
            edad += HUMANO_A_CANINO * n
        else:
            edad += HUMANO_A_CANINO_DOS_PRIMEROS_ANYOS * n

    return round(edad)


## Fin U2_10

## U2_011


def main_U2_11():
    print("Ejercicio 11:")
    columna = input("Introduzca la columna (a-h): ")
    fila = int(input("Introduzca la fila (1-8): "))
    color_cuadro = is_black_or_white(columna, fila)

    print("El cuadro de esa posición es de color", color_cuadro)


def is_black_or_white(c, f):
    color = None
    if f % 2 == 1:
        if c == "a" or c == "c" or c == "e" or c == "g":
            color = "negro"
        else:
            color = "blanco"
    else:
        if c == "a" or c == "c" or c == "e" or c == "g":
            color = "blanco"
        else:
            color = "negro"

    return color


## Fin U2_11

## U2_012


def main_U2_12():
    print("Ejercicio 12:")
    dia = int(input("Introduzca un numero de dia: "))
    mes = int(input("Introduzca un numero de mes: "))
    signo_zodiacal = calcular_signo(dia, mes)
    if signo_zodiacal != None:
        print("Tu signo es", signo_zodiacal)


def calcular_signo(d, m):
    signo = None
    if (
        (d == 31 and (m == 2 or m == 4 or m == 6 or m == 9 or m == 11))
        or (d == 30 and m == 2)
        or (d > 31 or d < 1)
        or (m < 1 or m > 12)
    ):
        print("Esa fecha no es válida.")

    if 22 <= d <= 31 and m == 12 or 1 <= d <= 19 and m == 1:
        signo = "Capricornio"
    elif 20 <= d <= 31 and m == 1 or 1 <= d <= 19 and m == 2:
        signo = "Acuario"
    elif 19 <= d <= 29 and m == 2 or 1 <= d <= 20 and m == 3:
        signo = "Piscis"
    elif 21 <= d <= 31 and m == 3 or 1 <= d <= 19 and m == 4:
        signo = "Aries"
    elif 20 <= d <= 30 and m == 4 or 1 <= d <= 20 and m == 5:
        signo = "Tauro"
    elif 21 <= d <= 31 and m == 5 or 1 <= d <= 20 and m == 6:
        signo = "Géminis"
    elif 21 <= d <= 30 and m == 6 or 1 <= d <= 22 and m == 7:
        signo = "Cáncer"
    elif 23 <= d <= 31 and m == 7 or 1 <= d <= 22 and m == 8:
        signo = "Leo"
    elif 23 <= d <= 31 and m == 8 or 1 <= d <= 22 and m == 9:
        signo = "Virgo"
    elif 23 <= d <= 30 and m == 9 or 1 <= d <= 22 and m == 10:
        signo = "Libra"
    elif 23 <= d <= 31 and m == 10 or 1 <= d <= 21 and m == 11:
        signo = "Escorpio"
    elif 22 <= d <= 30 and m == 11 or 1 <= d <= 21 and m == 12:
        signo = "Libra"

    return signo


## Fin U2_12

## U2_013


def main_U2_13():
    print("Ejercicio 13:")
    luz = float(input("Introduzca la longitud de onda: "))
    color_onda = longitud_onda(luz)

    if color_onda != None:
        print("El color que corresponde a esa onda es el", color_onda)


def longitud_onda(l):
    color = None
    if 380 <= l < 450:
        color = "Violeta"
    elif 450 <= l < 495:
        color = "Azul"
    elif 495 <= l < 570:
        color = "Verde"
    elif 570 <= l < 590:
        color = "Amarillo"
    elif 590 <= l < 620:
        color = "Naranja"
    elif 620 <= l < 750:
        color = "Rojo"
    else:
        print("Esa longitud no es visible en estos momentos.")

    return color


## Fin U2_13

## U2_014


def main_U2_14():
    print("Ejercicio 14:")
    anyo = int(input("Introduzca un año: "))

    if es_bisiesto(anyo):
        print("Ese año es bisiesto.")
    else:
        print("Ese año no es bisiesto.")


def es_bisiesto(a):
    resultado = False
    if a % 400 == 0:
        resultado = True
    elif a % 100 == 0:
        resultado = False
    elif a % 4 == 0:
        resultado = True

    return resultado


## Fin U2_14

## U2_015


def main_U2_15():
    print("Ejercicio 15:")
    print(generar_contrasena())


def generar_contrasena():
    contrasena_generada = ""
    cant_caracteres = random.randint(7, 10)

    for i in range(cant_caracteres):
        char_generado = random.randint(33, 126)
        contrasena_generada += chr(char_generado)

    return contrasena_generada


## Fin U2_15

## U2_016


def main_U2_16():
    print("Ejercicio 16:")
    if es_contrasena_valida(input("Introduzca una contraseña: ")):
        print("Enhorabuena, su contraseña está establecida.")
    else:
        print(
            "Lo sentimos, esa contraseña es muy débil. Debe tener 8 carácteres o más, al menos una letra mayúsucla y minúscula y un número."
        )


def es_contrasena_valida(contrasena: str):
    is_longitud = len(contrasena) >= 8
    have_mayuscula = False
    have_minuscula = False
    have_numero = False

    if is_longitud:
        for i in range(len(contrasena)):
            if contrasena[i].isdigit() and not have_numero:
                have_numero = True

            if contrasena[i].isupper() and not have_mayuscula:
                have_mayuscula = True

            if contrasena[i].islower() and not have_minuscula:
                have_minuscula = True

    return is_longitud and have_mayuscula and have_minuscula and have_numero


## Fin U2_16

## U2_017


def main_U2_17():
    print("Ejercicio 17:")
    comprobar_contrasena_valida()


def comprobar_contrasena_valida(intento: int = 1):
    contrasena = generar_contrasena()

    if not es_contrasena_valida(contrasena):
        comprobar_contrasena_valida(intento + 1)
    else:
        print("La contraseña generada ha sido:", contrasena)
        print("Cantidad de intentos:", intento)


## Fin U2_17

## U2_018


def main_U2_18():
    print("Ejercicio 18:")
    numero = int(input("Introduzca un número: "))
    primo_encontrado = siguiente_primo(numero + 1)
    print("El siguiente numero primo es:", primo_encontrado)


def es_primo(num):
    resultado = None
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                resultado = False
        if resultado == None:
            resultado = True
    else:
        resultado = False

    return resultado


def siguiente_primo(num):
    resultado = 0
    if es_primo(num):
        resultado = num
    else:
        resultado = siguiente_primo(num + 1)

    return resultado


## Fin U2_18

## U2_019


def main_U2_19():
    print("Ejercicio 19:")
    mes_pedido = int(input("Introduzca un mes: "))
    anyo_pedido = input("Introduzca un año: ")

    dia = dia_del_mes(mes_pedido, anyo_pedido)

    if dia == 0:
        print("Esa fecha no es válida.")
        print("(El mes debe ser válido y el año de cuatro cifras.)")
    else:
        print("El número de días de ese mes es de", dia)


def dia_del_mes(mes, anyo):
    dias = 0
    if mes > 12 or mes < 0 or len(anyo) != 4:
        dias = 0
    else:
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            dias = 30
        elif (
            mes == 1
            or mes == 3
            or mes == 5
            or mes == 7
            or mes == 8
            or mes == 10
            or mes == 12
        ):
            dias = 31
        elif mes == 2:
            if es_bisiesto(int(anyo)):
                dias = 29
            else:
                dias = 28

    return dias


## Fin U2_19

## U2_019


def main_U2_20():
    print("Ejercicio 20:")
    bucle_fecha_magica()


def bucle_fecha_magica(dia: int = 1, mes: int = 1, anyo: int = 1901):
    for i in range(anyo, 2001):
        for j in range(mes, 13):
            dias_totales = dia_del_mes(mes, str(anyo))
            for k in range(dia, dias_totales + 1):
                if es_fecha_magica(k, j, i):
                    print(f"La fecha {k}/{j}/{i} es mágica.")


def es_fecha_magica(dia, mes, anyo):
    ultimas_cifras = anyo % 100
    resultado = None

    if dia * mes == ultimas_cifras:
        resultado = True
    else:
        resultado = False

    return resultado


## Fin U2_20


# main_U2_01()
# main_U2_02()
# main_U2_03()
# main_U2_04()
# main_U2_05()
# main_U2_06()
# main_U2_07()
# main_U2_08()
# main_U2_09()
# main_U2_10()
# main_U2_11()
# main_U2_12()
# main_U2_13()
# main_U2_14()
# main_U2_15()
# main_U2_16()
# main_U2_17()
# main_U2_18()
# main_U2_19()
main_U2_20()
