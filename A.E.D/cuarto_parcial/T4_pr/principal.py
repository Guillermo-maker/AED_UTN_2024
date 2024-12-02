import random
import Pieza
import os.path
import pickle

def principal():
    v = []
    fd = "PIEZAS.dat"
    op = -1
    while op != 6:
        print("1. Cargar Arreglo ")
        print("2. Mostrar todos las Piezas")
        print("3. Acumular")
        print("4. Generar Archivo")
        print("5. Mostrar Archivo")
        print("6. Salir")
        print()
        op = int(input("INGRESAR OPCION: "))

        if op == 1:
            v = cargar()
        elif op == 2:
            if v:
                mostrar(v)
            else:
                "No estan cargados los datos..."
                print()
        elif op == 3:
            if v:
                acumular(v)
            else:
                "No estan cargados los datos..."
                print()
        elif op == 4:
            if v:
                generar_archivo(v, fd)
            else:
                "No estan cargados los datos..."
                print()
        elif op == 5:
            if v:
                mostrar_archivo(fd)
            else:
                "No estan cargados los datos..."
                print()
        elif op == 6:
                "ADIOS"


def add_in_order(v, pieza):
    n = len(v)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if pieza.codigo == v[c].codigo:
            pos = c
            break

        else:
            if pieza.codigo < v[c].codigo:
                der = c - 1
            else:
                izq = c + 1

    if izq > der:
        pos = izq
    v[pos:pos] = [pieza]

def validar(inf):
    n = int(input("Valor mayor a " + str(inf) + " por favor: "))
    while n <= inf:
        n = int(input("Error... se pidio un valor mayor a " + str(inf)+ "... Cargue de nuevo"))
    return n


def cargar():
    n = validar(0)
    v = []
    descripciones = ("TURBO", "LLantas", "INTERCOOLER", "SUSPENSION", "Diferencial", "Asiento", "Bujía")
    for i in range(n):
        cod = random.randint(1, 100000)
        des = random.choice(descripciones) + " " + str(i)
        tip = random.randint(0, 19)
        sec = random.randint(10, 25)
        sto = random.randint(0, 200)
        pieza = Pieza.pieza(cod, des, tip, sec, sto)
        add_in_order(v,pieza)
        print()
    return v

def mostrar(v):
    n = len(v)
    x = int(input("Nivel de stock  de referencia: "))
    print("Listado de piezas...")
    for i in range(n):
        print(v[i], end="")
        if v[i].stock < x:
            print(" - Observación: Stock reducido (menor que ", x, ")", sep="")
        else:
            print()
    print()

def binaria(v, isb):
    n = len(v)
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if isb == v[c].codigo:
            return c

        if isb < v[c].codigo:
            der = c - 1
        else:
            izq = c + 1
    return -1

def acumular(v):
    n = len(v)

    #proceso de acumulacion...
    ac = [[0] * 16 for f in range(20)]
    for i in range(n):
        f = v[i].tipo
        c = v[i].sector -10
        ac[f][c] += v[i].stock

    # mostrar resultado distinto a cero
    print("Resultados...")
    for f in range(20):
        for c in range(16):
            if ac[f][c] != 0:
                print("Tipo: ", f, "Sector: ", c+10, "Stock acumulado: ", ac[f][c])
    print()


def generar_archivo(v, fd):
    n = len(v)
    m = open(fd, "wb")
    for i in range(n):
        if v[i].sector >= 15:
            pickle.dump(v[i], m)
    m.close()
    print("Archivo generado...")
    print()

def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("No existe el archivo", fd, "...")
        print()
        return
    print("Listado de piezas...")
    c = ac = 0
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        r = pickle.load(m)
        c += 1
        ac += r.stock
        print(r)
    m.close()

    p = 0
    if c != 0:
        p = ac / c
    print("Stock promedio de todas las piezas:", round(p, 2))
    print()



















if __name__ == "__main__":
    principal()