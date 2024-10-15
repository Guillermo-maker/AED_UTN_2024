import random
import Servicio


def principal():
    v = []
    op = -1
    while op != 5:
        print("1. Cargar arreglo")
        print("2. Mostrar ordenado")
        print("3. Contar por tipo")
        print("4. Buscar")
        print("5. Salir")
        op = int(input("Ingrese número de opción: "))

        if op == 1:
            v = cargar()

        elif op == 2:
            if v:
                mostrar(v)
            else:
                print("el vector no fue cargado todavía...")
                print()

        elif op == 3:
            if v:
                contar(v)
            else:
                print("el vector no fue cargado todavía...")
                print()

        elif op == 4:
            if v:
                buscar(v)
            else:
                print("el vector no fue cargado todavía...")
                print()

        elif op == 5:
            print("Programa terminado... Hasta la vista baby...")
            print()


def validar(inf):
    n = int(input("Ingrese la cantidad de datos, tiene que ser un valor mayor " + str(inf) + " Porfavor: "))
    while n <= inf:
        n = int(input("Porfavor de nuevo: "))
    return n


def cargar():
    n = validar(0)
    v = n * [None]
    nombres = ("Kanye", "Michael", "Abel", "Luis", "Dua")
    apellidos = ("West", "Jackson", "Telasefaye", "Miguel", "Lipa")
    for i in range(n):
        id = random.randint(1, 50000)
        nom = random.choice(nombres) + " " + random.choice(apellidos)
        ti = random.randint(1, 10)
        imp = round(random.uniform(0, 20000), 2)
        v[i] = Servicio.servicio(id, nom, ti, imp)
    print("Datos Cargados")
    print()
    return v


def mostrar(v):
    n = len(v)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].id_cliente > v[j].id_cliente:
                v[i], v[j] = v[j], v[i]

    cs = 0
    # MOSTRAR TODOS LOS DATOS ENTRE I1 Y I2:
    i1 = int(input("Ingrese el primer parametro de comparacion: "))
    i2 = int(input("Ingrese el segundo parametro de comparacion: "))
    print("Listado de Importe entre ", i1, " y ", i2, ":")
    for i in range(n):
        if i1 <= v[i].importe <= i2:
            cs += 1
            print(v[i])
    print()
    print("La cantidad de servicios mostrados: ", cs)
    print()


def contar(v):
    n = len(v)
    c = 10 * [0]

    for i in range(n):
        # el tipo de servicio viene entre 1 y 10... restar uno para compatibilizar con los indices del vector c...
        ind = v[i].tipo - 1
        c[ind] += 1

    print("Cantidad de servicios por tipo: ")
    for k in range(10):
        if c[k] > 0:
            # si al contar/acumular reste uno, entonces en pantalla, Y SOLO EN PANTALLA, mostrar k+1...
            print("Tipo de servicio:", k+1, " Cantidad: ", c[k])
    print()


def buscar(v):
    n = len(v)
    nom = input("Nombre del cliente a Buscar: ")
    for i in range(n):
        if nom == v[i].nombre_cliente:
            print("Encontrado - Datos actuales: ")
            print(v[i])
            v[i].importe += 2000
            print("Datos con el importe actualizado: ")
            print(v[i])
            return
    print("No Estaba...")
    print()



if __name__ == "__main__":
    principal()
