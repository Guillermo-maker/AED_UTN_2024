# TURNO 1



#Determinar la cantidad de empleos que hay en el arreglo por cada tipo de empleo posible (40 contadores en
#total en un vector de conteo). Muestre solo los valores de los contadores cuyos valores finales sean mayores a
#cero.

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

# TURNO 2

#Determine el importe acumulado que se cobró por cada posible país de destino (20 acumuladores en un vector
#de acumulación). Muestre solo aquellos acumuladores cuyo valor sea mayor un valor t que se carga por
#teclado.

def acumular(v):
    n = len(v)
    c = 20 * [0]

    for i in range(n):
        # el numero de pais viene entre 1 y 20... restar uno para compatibilizar los indices del vector c ...
        ind = v[i].pais - 1
    t = int(input("Importe ( se mostraran los acumuladores mayores a este valor: "))
    print("importadores acumulados por pais, mayores a ", t, ":")

    for k in range(20):
        if c[k] > t:
            #si al contar/acumular reste, entonces en pantalla, Y SOLO EN PANTALLA, mostrar k+1...
            print("Pais destino:", k+1, "Importe acumulado: ", round(c[k], 2))
    print()

# TURNO 3

#Determinar cuántos servicios hay para uno de los tipos posibles (10 contadores). Mostrar todos los conteos
#que sean diferentes de cero.

def contar_T3(v):
    n = len(v)
    c = 10 * [0]

    for i in range(n):
        ind = v[i].tipo - 1
        c[ind] += 1

    print("Cantidad de servicios por tipo: ")
    for k in range(10):
        if c[k] > 0:
            print("Tipo de servicio: ", k+1, " Cantidad: ", c[k])
    print()

# TURNO 4

#Determinar y mostrar la cantidad de juicios que hay por cada posible tipo (15 contadores en un vector de
#conteo). Mostrar sólo aquellos contadores que sean mayores a una cantidad c ingresada por teclado.

def contar_T4(v):
    n = len(v)
    ct = 15 * [0]

    for i in range(n):
        # El tipo de juicio viene entre 1 y 15... restar uno para compatibilizar con los indices del vector c...
        ind = v[i].tipo - 1
        ct[ind] += 1

    c = int(input("Cantidad a filtrar ( se mostraran los contadores con un valor mayor a este): "))
    print("Cantidad de juicios por tipo:")
    for k in range(15):
        if ct[k] > c:
            print("Tipo de juicio: ", k+1, " Cantidad:,", ct[k] )
    print()

# TURNO E

#Determine la cantidad de publicaciones que hay por cada tipo posible (30 contadores en un vector de conteo).
#Muestre aquellos cuyo valor final sea mayor al valor x que se carga por teclado.

def contar_TE(v):
    n = len(v)
    ct = 30 * [0]

    for i in range(n):
        ind = v[i].tipo - 1
        ct[ind] += 1

    x = int(input("Ingrese cantidad a filtrar ( Se mostraran los contadores con el valor mayor a este): "))
    print("Cantidad de publicaciones por tipo: ")
    for k in range(30):
        if ct[k] > x:
            print("Tipo de publicaciones: ", k+1, " Cantidad:", ct[k])
    print()