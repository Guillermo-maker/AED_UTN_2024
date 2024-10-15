# Desarrolle un programa completo en Python que permita generar una sucesión de 20000 números enteros aleatorios, usando como semilla del generador el numero 49 (es decir random.seed(49)). Los valores de cada uno de esos 20000 números deben estar entre 1 y 45000 (incluidos ambos) (DEBE usar random.randint(1, 45000) para generar esos números).

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

# Importar el módulo random
import random

# Establecer la semilla del generador de números aleatorios a 49
random.seed(49)
# Inicializar una lista vacía para almacenar los números generados
x = []
# Variables para llevar la cuenta de los resultados solicitados
cant_nm5 = 0
cant_nm7 = 0
cant_nm9 = 0
nmayor = 0
cant_pares = 0
parporcentaje = 0

# Generar 20000 números aleatorios entre 1 y 45000 (ambos inclusive)
for i in range(20000):
    a = random.randint(1, 45000)
    x.append(a)

    # Contar los múltiplos de 5, 7 y 9
    if a % 5 == 0:
        cant_nm5 += 1
    if a % 7 == 0:
        cant_nm7 += 1
    if a % 9 == 0:
        cant_nm9 += 1

    # Contar los números pares menores a 15000
    if a % 2 == 0 and a < 15000:
        cant_pares += 1

# Calcular el porcentaje entero que representa los pares menores a 15000 respecto al total
parporcentaje = (cant_pares / len(x)) * 100
porcentaje_entero = int(parporcentaje)

# Encontrar el mayor número cuyo último dígito esté entre 5 y 8 (ambos inclusive) se puede hacer sin el for pero me gusta mas asi.
y = []
for z in x:
    if 5 <= z % 10 >= 8:
        y.append(z)
        nmayor = max(y)

print(f'la suma de todos los elementos de la la lista x es {sum(x)}')
print(f'hay {cant_nm5} numeros multiplo de 5 en la lista')
print(f'hay {cant_nm7} numeros multiplo de 7 en la lista')
print(f'hay {cant_nm9} numeros multiplo de 9 en la lista')
print(f'mayor con último dígito 5-8 es {nmayor}')
print(f'la cantidad de numeros pares menores a 15000 son {cant_pares}')
print(f'El porcentaje que representa la suma de los pares menores a 15000 respecto al total es {porcentaje_entero}%')
