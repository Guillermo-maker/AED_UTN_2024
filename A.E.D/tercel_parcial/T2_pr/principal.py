import random
import Tikect


def validar(inf):
    n = int(input("Ingrese un valor mayor a " + str(inf) + " por favor: "))
    while n <= inf:
        n = int(input("ERROR...  se pidio un valor mayor a " + str(inf) + " Cargue de nuevo: "))
    return n


def cargar():
    n = validar(0)
    v = n * [None]
    nombres = ("AJ", "BC", "ZE", "RT", "PL", "HS", "UB", "KW", "LM")
    for i in range(n):
        cv = random.choice(nombres) + str(i)
        idp = random.randint(1, 150)
        pa = random.randint(1, 20)
        naa = random.randint(1, 200)
        imp = round(random.uniform(0, 20000), 2)
        v[i] = Tikect.ticket(cv, idp, pa, naa, imp)
    print("Ticket cargados")
    print()
    return v


def mostrar(v):
    n = len(v)
    # Lista v ordenada segun los vuelos
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].codigo_vuelo > v[j].codigo_vuelo:
                v[i], v[j] = v[j], v[i]

    num = int(input("Número de asiento (se mostrarán los tickets cuyo número de asiento sea mayor a este): "))
    print("listado de Listado de tikets con el numero mayor a ", num, ":")

    for i in range(n):
        if v[i].numero_asiento > num:
            print(v[i])
    print()


def acumular(v):
    n = len(v)
    c = 20 * [0]

    for i in range(n):
        # el numero de pais viene entre 1 y 20... restar uno para compatibilizar los indices del vector c...
        ind = v[i].pais - 1
        c[ind] += v[i].importe

    t = int(input("Importe (se mostraran los acumuladores mayores a este valor: "))
    print("importes acumulados por pais, mayores a ", t, ":")

    for k in range(20):
        if c[k] > t:
            # si al contar/acumular reste uno, entonces en pantalla, y SOLO EN PANTALLA, mostrar k+1...
            print("Pais destino:", k+1, "Importe acumulado:", round(c[k], 2))
    print()



def buscar(v):
    n = len(v)
    id = int(input("Numero de identificacion del pasajero a buscar: "))
    for i in range(n):
        if id == v[i].id_pasajero:
            print("ENCONTRADO:")
            print("Numero de asiento: ", v[i].numero_asiento, " - Pais destino: ", v[i].pais)
            return
    print("No estaba")
    print()


def principal():
    v = []
    op = -1

    while op != 5:
        print("1. Cargar el arreglo:")
        print("2. Mostrar los datos:")
        print("3. Acumular/Contar Tickects:")
        print("4. Buscar tikect segun id:")
        print("5. Salir:")
        print()
        op = int(input("Ingresar Opcion: "))

        if op == 1:
            v = cargar()
        elif op == 2:
            if v:
                mostrar(v)
            else:
                print("No ne cargaron los datos todavia")
        elif op == 3:
            if v:
                acumular(v)
            else:
                print("No ne cargaron los datos todavia")
        elif op == 4:
            if v:
                buscar(v)
            else:
                print("No ne cargaron los datos todavia")
        elif op == 5:
            print("Programa Terminado")
            print()


if __name__ == "__main__":
    principal()
