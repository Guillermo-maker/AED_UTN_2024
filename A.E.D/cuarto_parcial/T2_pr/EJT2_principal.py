import os.path
import random
import pickle
import clase


def add_in_order(v, libro):
    n = len(v)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if libro.isbn == v[c].isbn:
            pos = c
            break

        else:
            if libro.isbn < v[c].isbn:
                der = c - 1
            else:
                izq = c + 1

    if izq > der:
        pos = izq
    v[pos:pos] = [libro]


# carga y retorna un número, validando que sea mayor al valor inf que entra como parámetro.
def validar(inf):
    n = int(input('Valor (mayor a ' + str(inf) + ' por favor): '))
    while n <= inf:
        n = int(input('Error... Se pidio mayor a ' + str(inf) + '... Cargue de nuevo: '))
    return n


def cargar():
    n = validar(0)
    v = []
    tit1 = ("Guerra", "Espacio", "Abismo", "Fanatismo")
    tit2 = ("Oscuridad", "Tristeza", "Felicidad", "Honor")
    nombres = ("Carlos", "Ana", "José", "María", "Pedro", "Belén", "Martín", "Soledad")
    apellidos = ("Díaz", "Giuliani", "Trejo", "Masiero", "Duplesis", "Johnson", "Iriarte")
    for i in range(n):
        isb = random.randint(1, 100000000)
        tit = random.choice(tit1) + " y " + random.choice(tit2) + " " + str(i)
        aut = random.choice(nombres) + " " + random.choice(apellidos) + " " + random.choice(apellidos)
        idi = random.randint(1, 5)
        imp = round(random.uniform(10000, 20000), 2)
        libro = clase.Libro(isb, tit, aut, idi, imp)
        add_in_order(v, libro)
    print("Listo. El arreglo fue generado")
    print()
    return v


def mostrar(v):
    n = len(v)
    print("Listado de libros...")
    for i in range(n):
        print(v[i])
    print()


def binaria(v, isb):
    n = len(v)
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if isb == v[c].isbn:
            return c

        if isb < v[c].isbn:
            der = c - 1
        else:
            izq = c + 1

    return -1


def buscar(v):
    isb = int(input("ISBN a buscar: "))
    pos = binaria(v, isb)
    if pos != -1:
        print("Encontrado!")
        print(v[pos])
        if v[pos].idioma == 4:
            d = (22 * v[pos].importe) // 100
            v[pos].importe -= d
            print("Datos cambiados:")
            print(v[pos])
    else:
        print("No contamos con el libro", isb, "pero vuelva, please!!!!!")
    print()


def generar_archivo(v, fd):
    a = input("Autor a filtrar: ")
    p = float(input("Precio a filtrar: "))

    n = len(v)
    m = open(fd, "wb")
    for i in range(n):
        if v[i].autor == a and v[i].importe <= p:
            pickle.dump(v[i], m)
    m.close()
    print("Archivo generado...")
    print()


def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("No existe el archivo", fd, "...")
        print()
        return

    print("Listado de libros...")
    c = 0
    m = open(fd, "rb")
    t = os.path.getsize(fd)
    while m.tell() < t:
        r = pickle.load(m)
        c += 1
        print(r)
    m.close()

    print("Cantidad de libritos que te mostré:", c)
    print()


def principal():
    v = []
    fd = "libros.dat"
    op = -1
    while op != 6:
        print("1. Cargar arreglo")
        print("2. Mostrar contenido")
        print("3. Buscar y cambiar precio")
        print("4. Generar archivo")
        print("5. Mostrar archivo")
        print("6. Salir")
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
                buscar(v)
            else:
                print("el vector no fue cargado todavía...")
                print()

        elif op == 4:
            if v:
                generar_archivo(v, fd)
            else:
                print("el vector no fue cargado todavía...")
                print()

        elif op == 5:
            mostrar_archivo(fd)

        elif op == 6:
            print("Programa terminado... Hasta la vista baby...")
            print()


if __name__ == "__main__":
    principal()

