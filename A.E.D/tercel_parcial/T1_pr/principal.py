"""
Una agencia de empleos necesita un programa para procesar los datos de los empleos que ofrece a los
interesados. Por cada Empleo se tienen los siguientes datos: el número de identificación del empleo, la descripción
del empleo, el tipo de empleo (un valor del 0 al 39) y el monto mensual del sueldo o retribución que se paga por
ese empleo. Se desea almacenar la información referida a los n empleos en un arreglo de objetos de tipo Empleo
(definir la clase Empleo y cargar n por teclado, validando que sea mayor a cero). Se pide desarrollar un programa
en Python controlado por un menú de opciones, que permita gestionar las siguientes tareas:

1. Cargar el arreglo pedido con los datos de los n empleos. Valide o asegure que los valores de cada campo sean
correctos. Puede hacer la carga en forma manual, o puede generar los datos en forma automática (con valores
aleatorios). Pero al menos una debe programar. Pero si hace carga automática, todos los campos deben ser
cargados así (no combine ambas técnicas en la carga de un registro).

2. Mostrar todos los datos de todos los empleos, a razón de uno por línea, en un listado ordenado de menor a
mayor según la descripción de los empleos. Al final del listado indique la suma de los sueldos a pagar por todos
los empleos que se mostraron.

3. Determinar la cantidad de empleos que hay en el arreglo por cada tipo de empleo posible (40 contadores en
total en un vector de conteo). Muestre solo los valores de los contadores cuyos valores finales sean mayores a
cero.

4. Determinar si existe un empleo cuyo número de identificación sea igual num, siendo num un valor que se carga
por teclado. Si existe, mostrar solo su descripción y el sueldo a pagar. Si no existe, informar con un mensaje. Si
existe más de un registro que coincida con esos parámetros de búsqueda, debe mostrar sólo el primero que
encuentre. La búsqueda debe detenerse al encontrar el prime objeto que coincida con el criterio pedido.
"""

import random
import Empleo

# carga y retorna un número, validando que sea mayor al valor inf que entra como parámetro.
def validar(inf):
    n = int(input("Valor (mayor a " + str(inf) + " por favor): "))
    while n <= inf:
        n = int(input("Error... se pidio mayor a " + str(inf) + "... Cargue de nuevo: "))
    return n

def cargar():
    n = validar(0)
    v = n * [None]
    nombres = ("Oficinista", "Mecanico", "Jardinero", "Programador", "Maestro")
    for i in range(n):
        id = random.randint(1, 25000)
        de = random.choice(nombres) + " " + str(i)
        ti = random.randint(0, 39)
        im = round(random.uniform(0, 20000), 2)
        v[i] = Empleo.empleo(id, de, ti, im)
    print("Listo. El arreglo fue generado")
    print()
    return v

def mostrar(v):
    n = len(v)

    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].descripcion > v[j].descripcion:
                v[i], v[j] = v[j], v[i]

    print("Listado de empleos...")
    ac = 0
    for i in range(n):
        ac += v[i].importe
        print(v[i])
    print("Suma de todos los sueldos pagados:", ac)
    print()



def contar(v):
    n = len(v)
    c = 40 * [0]

    for i in range(n):
        c[v[i].tipo] += 1

    print("Cantidad de empleos por tipo...")
    for k in range(40):
        if c[k] != 0:
            print("Tipo: ", k, "Cantidad: ", c[k])
    print()


def buscar(v):
    n = len(v)
    num = int(input("Numero de identificacion del empleo a buscar: "))
    for i in range(n):
        if num == v[i].identificador:
            print("Encontrado:")
            print("Descripcion del empleo:", v[i].descripcion, " - Sueldo: ", v[i].importe)
            print()
        print("No estaba...")
        print()


def principal():
    v = []  # CREO EL VECTOR
    op = -1  # inicializo variable opcion en -1
    while op != 5:
        print("1. Cargar arreglo")
        print("2. Mostrar ordenado")
        print("3. Conteo por tipo")
        print("4. Buscar")
        print("5. Salir")
        op = int(input("Ingrese numero de opcion: "))

        if op == 1:
            v = cargar()  # llamo a la funcion cargar
        elif op == 2:
            if v:
                mostrar(v)  # llamo a la funcion mostrar
            else:
                print("el vector no fue cargado todavia...")
                print()
        elif op == 3:
            if v:
                contar(v)  # llamo a la funcion contar
            else:
                print("el vector no fue cargado todavia...")
                print()
        elif op == 4:
            if v:
                buscar(v)  # llamo a la funcion buscar
            else:
                print("el vector no fue cargado todavia...")
                print()
        elif op == 5:
            print("Programa terminado... Hasta la vista baby...")
            print()


if __name__ == "__main__":
    principal()
