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

random.seed(20220512)  # Se establece la semilla del generador de números aleatorios

num_lista = []
numeros_multiplos_3 = 0
numeros_multiplos_5 = 0
numeros_no_cumplen_condiciones = 0
max_num1 = 0
max_no_num1 = 0
num_par_multiplo_de_11 = 0
suma_par_multiplo_de_11 = 0
promedio = 0
porcentaje5_entero = 0
porcentaje3_entero = 0
porcentaje_no5_no3_entero = 0

for i in range(25000):  # Ciclo que se repite 25000 veces
    numeros = random.randint(1, 45000)  # Genera un número aleatorio entre 1 y 45000
    num_lista.append(numeros)  # Agrega el número generado a la lista

    # Verifica si el número es múltiplo de 3, 5 o no cumple ninguna condición
    if numeros % 3 == 0:
        numeros_multiplos_3 += 1
        porcentaje3 = (numeros_multiplos_3 / len(num_lista)) * 100
        porcentaje3_entero = int(porcentaje3)
    if numeros % 5 == 0 and not numeros % 3 == 0:
        numeros_multiplos_5 += 1
        porcentaje5 = (numeros_multiplos_5 / len(num_lista)) * 100
        porcentaje5_entero = int(porcentaje5)
    if not numeros % 5 == 0 and not numeros % 3 == 0:
        numeros_no_cumplen_condiciones += 1
        porcentaje_no5_no3 = (numeros_no_cumplen_condiciones / len(num_lista)) * 100
        porcentaje_no5_no3_entero = int(porcentaje_no5_no3)

    # Encuentra el mayor número que comienza con 1 y el mayor que no comienza con 1
    num_str = str(numeros)
    if num_str[0] == '1':
        max_num1 = max(max_num1, numeros)
    if not num_str[0] == '2':
        max_no_num1 = max(max_no_num1, numeros)

    # Verifica si el número es par y múltiplo de 11
    if numeros % 2 == 0 and numeros % 11 == 0:
        num_par_multiplo_de_11 += 1
        suma_par_multiplo_de_11 += numeros

# Calcula el promedio de los números pares y múltiplos de 11
promedio = suma_par_multiplo_de_11 // num_par_multiplo_de_11

# Imprime los resultados
print(f'La cantidad de numeros multiplos de 3 de la lista son: {numeros_multiplos_3}')
print(f'La cantidad numeros multiplos de 5 pero no de 3 de la lista son: {numeros_multiplos_5}')
print(f'La cantidad numeros que no cumplen ninguna de las 2 condiciones son: {numeros_no_cumplen_condiciones}')
print(f'El mayor de los numeros que comienzan con 1 es: {max_num1}')
print(f'El mayor de los numeros que NO comienzan con 1 es: {max_no_num1}')
print(f'El promedio entero truncado de los números generados que son pares y múltiplos de 11 es: {promedio}')
print(f'El porcentaje de numeros que son multiplos de 3 es: {porcentaje3_entero}')
print(f'El porcentaje de numeros que son multiplos de 5 y NO de 3 es: {porcentaje5_entero}')
print(f'El porcentaje de numeros que NO son multiplos de 5 NI de 3 es: {porcentaje_no5_no3_entero}')
