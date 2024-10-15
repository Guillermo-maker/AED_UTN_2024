# TURNO 1

#Mostrar todos los datos de todos los empleos, a razón de uno por línea, en un listado ordenado de menor a
#mayor según la descripción de los empleos. Al final del listado indique la suma de los sueldos a pagar por todos
#los empleos que se mostraron.

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

def mostrar(v):
    n = len(v)

    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].descripcion > v[j].descripcion:
                v[i], v[j] = v[j], v[i]

    print("listadp de empleos")
    ac = 0
    for i in range(n):
        ac += v[i].importe
        print(v[i])
    print(" la suma de los sueldos:", ac)




# TURNO 2

#Mostrar los datos de todos los tickets cuyo número de asiento sea mayor a un valor num que se carga por
#teclado, ordenados por código de vuelo de menor a mayor. Los tickets se deben mostrar a razón de uno por
#línea (no más de una línea por ticket en la pantalla).

def mostrar_t2(v):
    n = len(v)
    # Lista v ordenada segun los vuelos
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].codigo_vuelo > v[j].codigo_vuelo:
                v[i], v[j] = v[j], v[i]

    num = int(input("Número de asiento (se mostrarán los tickets cuyo número de asiento sea mayor a este): "))
    print("listado de Listado de tikets con el numero mayor a ", num, ":")

    for i in range(n):
        if v[i].numero_asiento > num:
            print(v[i])
    print()

# TURNO 3

#Mostrar los datos de todos los servicios cuyo importe esté entre los valores i1 e i2 (ambos incluidos) que se
#cargan por teclado, y ordenados de menor a mayor por código identificatario. Muestre al final una línea
#adicional con la cantidad de servicios mostrados en este listado.


def mostrar_t3(v):
    n = len(v)

    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].id_cliente > v[j].id_cliente :
                v[i], v[j] = v[j], v[i]

    cs = 0
    # PARAMENTRO I1
    i1 = int(input("Ingrese el primer parametro:"))
    # PARAMENTRO I2
    i2 = int(input("Ingrese el segundo parametro:"))

    for i in range(n):
        if i1 <= v[i].importe >= i2:
            cs += 1
            print(v[i])
    print()
    print("La cantiad de servicios mostrados: ", cs)
    print()

# TURNO 4

#Mostrar datos de todos los juicios cuyo monto de honorarios sea mayor a mon (que se carga por teclado), en
#un listado ordenado de menor a mayor según la descripción o carátula, a razón de un juicio por línea. Al final
#del listado, indique cuántos objetos se mostraron.

def mostrar_t4(v):
    n = len(v)

    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].descripcion > v[j].descripcion:
                v[i], v[j] = v[j], v[i]

    mon = int(input("Ingresar un monto para comparar"))
    co = 0
    print("Listado de juicios con importe mayor a ", mon, ";")
    for i in range(n):
        if v[i].importe > mon:
            co += 1
            print(v[i])
    print()
    print("La cantidad de objetos que se mostraron: ", co)

# TURNO E

#Mostrar los datos de todas los publicaciones cuyo costo sea mayor al valor cos que se carga por teclado. El
#listado debe salir ordenado alfabéticamente por el código de identificación de las publicaciones. Mostrar a
#razón de un registro por línea. Al final del listado, muestre el costo promedio de las publicaciones que se
#mostraron.


def mostrar_TE(v):
    n = len(v)

    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].codigo > v[j].codigo:
                v[i], v[j] = v[j], v[i]

    p = cp = ac = 0
    cos = float(input("Costo a filtrar (se mostrarán los registros cuyo costo sea mayor a este): "))
    print("Listado de publicaciones con costo mayor a", cos, ":" )
    for i in range(n):
        if v[i].costo > cos:
            cp += 1
            ac += v[i].costo
            print(v[i])
    if cp != 0:
        p = ac // cp
    print("Costo promedio de las publicaciones mostradas:", round(p, 2))
    print()


