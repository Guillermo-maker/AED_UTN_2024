# Desarrolle un programa completo en Python que permita generar una sucesión de 25000 números enteros aleatorios, usando como semilla del generador el número 20220512 (es decir random.seed(20220512)).
# Los valores de cada uno de esos 25000 números deben estar entre 1 y 45000 (incluidos ambos) (DEBE usar random.randint(1, 45000) para generar esos números).
# A partir de esa sucesión el programa debe:

#    Determinar la cantidad de números múltiplos de 3 y también la cantidad de números múltiplos de 5 pero no de 3 y finalmente la cantidad de números que no cumplen ninguna de las 2 condiciones.
#    Indicar el mayor entre todos los números comienzan con el dígito 1, es decir 1234 comienza con 1 y 2345 no comienza con 1.
#    Indicar el promedio entero truncado de los números generados que son pares y múltiplos de 11.
#    Indicar el porcentaje entero que representa cada contador del punto 1.
#    Aclaración 1: NO se pide el porcentaje redondeado, sino el porcentaje truncado, sin decimales.
#    Aclaración 2: en el cálculo de este porcentaje, haga primero la multiplicación que corresponda, y luego la división.

# Cuando finalice, en las consignas que siguen en este mismo cuestionario, se le pedirá que informe cada uno de estos resultados,
# y también se le pedirá que suba el archivo de código fuente con el programa desarrollado (por lo que tenga muy presente en donde dejó ese archivo).
# Habrá también UNA pregunta de opciones múltiples referida a este mismo enunciado o a temas relacionados con él.


import random

random.seed(20220512)


numeros_multiplos_3 = 0
numeros_multiplos_5 = 0
numeros_no_cumplen_condiciones = 0
promedio_pares = 0

mayor = 0

numeros_pares = 0
suma_de_los_numeros_pares = 0

porcentaje_multiplo_3 = 0
porcentaje_multiplo_5 = 0
porcentaje_numeros_no_cumplen_condiciones = 0

for i in range(25000):
    num = random.randint(1, 45000)

    if num % 3 == 0:
        numeros_multiplos_3 += 1
        porcentaje_multiplo_3 = (numeros_multiplos_3 * 100) / 25000
    if num % 5 == 0 and not num % 3 == 0:
        numeros_multiplos_5 += 1
        porcentaje_multiplo_5 = (numeros_multiplos_5 * 100) / 25000
    if not num % 5 == 0 and not num % 3 == 0:
        numeros_no_cumplen_condiciones += 1
        porcentaje_numeros_no_cumplen_condiciones = (numeros_no_cumplen_condiciones * 100) / 25000

    num_str = str(num)

    if num_str[0] == '1':
        mayor = max(mayor, num)

    if num % 2 == 0 and num % 11 == 0:
        numeros_pares += 1
        suma_de_los_numeros_pares += num

promedio_pares = (suma_de_los_numeros_pares // numeros_pares)

print(f'multiplos de 3: {numeros_multiplos_3}')
print(f'multiplos de 5: {numeros_multiplos_5}')
print(f'numeros que no cumplen ninguna de las dos condiciones: {numeros_no_cumplen_condiciones}')
print(f'el mayor de los numeros con digito 1 es: {mayor}')
print(f'promedio truncado de los números generados que son pares y múltiplos de 11: {promedio_pares}')
print(f'porcentaje numeros multiplos de 3: {int(porcentaje_multiplo_3)}')
print(f'porcentaje numeros multiplos de 5: {int(porcentaje_multiplo_5)}')
print(f'porcentaje que no cumplen ninguna de las dos condiciones: {int(porcentaje_numeros_no_cumplen_condiciones)}')
