import  os.path
import random
import pickle
import Lote


def principal():
    v = []
    fd = "lotes.dat"
    op = -1
    while op != 6:
        print("1. Cargar Arreglo")
        print("2. Mostrar Contenido")
        print("3. Acumulación por manzana y orientación")
        print("4. Generar Archivo")
        print("5. Mostrar Archivo")
        print("6. Salir")
        op = int(input("Ingrese numero de opcion: "))

        if op == 1:
            v = cargar()

        elif op == 2:
            if v:
                mostrar(v)
            else:
                print("El vector no fue cargado todavia...")
                print()

        elif op == 3:
            if v:
                contar(v)
            else:
                print("el vector no fue cargado todavía...")
                print()

        elif op == 4:
            if v:
                generar_archivo(v, fd)
            else:
                print("El vector no fue cargado todavia...")
                print()
        elif op == 5:
            mostrar_archivo(fd)

        elif op == 6:
            print("Programa terminado... Hasta la vista baby...")
            print()



def add_in_order(v, lote):
    n = len(v)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if lote.nombre == v[c].nombre:
            pos = c
            break

        else:
            if lote.nombre < v[c].nombre:
                der = c - 1
            else:
                izq = c + 1

    if izq > der:
        pos = izq
    v[pos:pos] = [lote]

def validar(inf):
    n = int(input('Valor mayor a '+ str(inf) + ' porfavor: '))
    while n <= inf:
        n = int(input('Error... Se pidio un valor mayor a '+ str(inf) + ' Cargue de nuevo porfavor: '))
    return n

def cargar():
    n = validar(0)
    v = []
    nombres = ("Kanye", "Tyler", "Alicia", "María", "Pedro", "Belén", "Martín", "Soledad")
    apellidos = ("West", "The Creator", "Keys", "Masiero", "Duplesis", "Johnson", "Iriarte")
    for i in range(n):
        nom = random.choice(nombres) + " " + random.choice(apellidos) + " " + random.choice(apellidos)
        man = random.randint(1, 35)
        lot = random.randint(1, 20)
        ori = random.randint(1, 4)
        sup =  round(random.uniform(200, 4000), 2)
        imp = round(random.uniform(10000, 200000), 2)
        lote = Lote.lote(nom, man, lot, ori, sup, imp)
        add_in_order(v, lote)
    print("Listo. EL arreglo fue generado")
    print()
    return v

def mostrar(v):
    n = len(v)
    print("Listado de lotes...")
    for i in range(n):
        print(v[i])
    print()

def contar(v):
    n = len(v)

    #proceso de acumulacion...
    ac = [[0] * 4 for f in range(35)]
    for i in range(n):
        f = v[i].manzana - 1
        c = v[i].orientacion - 1
        ac[f][c] += v[i].superficie

    #mostrar resultados (diferentes a cero...)
    print("Resultados...")
    for f in range(35):
        for c in range(4):
            if ac[f][c] != 0:
                print("Manzana:", f+1, "Orientacion:", c+1, "Superficie:", ac[f][c])
    print()

    m = int(input("Manzana que desea acumular (entre 1 y 35)?: "))
    sa = 0
    f = m - 1
    for c in range(4):
        sa += ac[f][c]
    print("La superficie total para la manzana", m, "es:", sa)
    print()

def generar_archivo(v, fd):
    l1 = int(input("Valor de l1: "))
    l2 = int(input("Valor de l2: "))

    n = len(v)
    m = open(fd, "wb")
    for i in range(n):
        if l1 <= v[i].lote <= l2:
            pickle.dump(v[i], m)
    m.close()
    print("Archivo generado...")
    print()

def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("No existe el archivo", fd, "...")
        print()
        return

    print("Listado de lotes...")
    c = ac = 0
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        r = pickle.load(m)
        c += 1
        ac += r.importe
        print(r)
    m.close()

    p = 0
    if c != 0:
        p = ac / c
    print("Importe promedio de venta:", round(p, 2))
    print()


if __name__ == "__main__":
    principal()