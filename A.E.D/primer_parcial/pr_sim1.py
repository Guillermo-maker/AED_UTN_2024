# Desarrolle un programa completo en Python que permita generar una sucesión de 20000 números enteros aleatorios, usando como semilla del generador el numero 49 (es decir random.seed(49)).
# Los valores de cada uno de esos 20000 números deben estar entre 1 y 45000 (incluidos ambos) (DEBE usar random.randint(1, 45000) para generar esos números).

# A modo de elemento de control, y para que cada estudiante sepa si la secuencia que está generando es la correcta, indicamos aquí cuánto debe valer la suma de todos los números generados con el mecanismo indicado:

#    Suma de todos los números generados: 451459554

# A partir de esa sucesión el programa debe:

#   Indicar cuantos números eran múltiplos de 5, cuántos eran múltiplos de 7 y cuántos eran múltiplos de 9.
#   Indicar el mayor entre todos aquellos números cuyo último dígito sea mayor o igual a 5 pero menor o igual a 8.
#   Indicar cuantos números generados son pares menores a 15000.
#   Indicar el porcentaje entero que representa el punto anterior sobre el total de números procesados.
#   Aclaración 1: NO se pide el porcentaje redondeado, sino el porcentaje truncado, sin decimales.
#   Aclaración 2: en el cálculo de este porcentaje, haga primero la multiplicación que corresponda, y luego la división.

# Cuando finalice, en las consignas que siguen en este mismo cuestionario, se le pedirá que informe cada uno de estos resultados,
# y también se le pedirá que suba el archivo de código fuente con el programa desarrollado (por lo que tenga muy presente en donde dejó ese archivo).
# Entienda: Si NO sube su código fuente, los profesores procederán a reprobar manualmente su parcial.
# Habrá también UNA pregunta de opciones múltiples referida a este mismo enunciado o a temas relacionados con él.


import random

random.seed(49)

lista_numeros = []

multiplo_de_5 = 0
multiplo_de_7 = 0
multiplo_de_9 = 0

numero_mayor = 0

numeros_pares = 0

porcentaje = 0

for i in range(20000):
    num = random.randint(1, 45000)
    lista_numeros.append(num)

    if num % 5 == 0:
        multiplo_de_5 += 1
    if num % 7 == 0:
        multiplo_de_7 += 1
    if num % 9 == 0:
        multiplo_de_9 += 1

    if numero_mayor is None:
        if 5 <= num % 10 <= 8:
            numero_mayor = num
    elif num > numero_mayor:
        numero_mayor = num

    if 5 <= num % 10 <= 8:
        numero_mayor = max(numero_mayor, num)

    if num % 2 == 0 and num < 15000:
        numeros_pares += 1

    porcentaje = (numeros_pares * 100) // 20000

print(f'Indicar cuantos números eran múltiplos de 5: {multiplo_de_5}')
print(f'Indicar cuantos números eran múltiplos de 7: {multiplo_de_7}')
print(f'Indicar cuantos números eran múltiplos de 9: {multiplo_de_9}')
print(f'Números cuyo último dígito sea mayor o igual a 5 pero menor o igual a 8: {numero_mayor}')
print(f'Indicar cuantos números generados son pares menores a 15000: {numeros_pares}')
print(f'El porcentaje entero que representa el punto anterior sobre el total de números procesados: {porcentaje}')
