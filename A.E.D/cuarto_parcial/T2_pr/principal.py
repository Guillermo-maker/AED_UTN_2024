import os.path
import pickle
import random
import Libro

def principal():
    v = []
    fd = "libros.dat"
    op = -1

    while op != 6:
        print("1. Cargar Datos ")
        print("2. Mostrar Datos")
        print("3. Buscar ")
        print("4. Generar Archivo")
        print("5. Mostrar Archivo")
        print("6. Salir ")
        op = int(input("Ingrese numero de opcion: "))
        if op == 1:
            v = cargar()

        elif op == 2:
            if v:
                mostrar(v)
            else:
                print("Todavia no se cargaron los datos")

        elif op == 3:
            if v:
                buscar(v)
            else:
                print("Todavia no se cargaron los datos")

        elif op == 4:
            if v:
                generar(v, fd)
            else:
                print("Todavia no se cargaron los datos")

        elif op == 5:
            if v:
                mostrar_archivo(fd)

        elif op == 6:
                print("ADIOS PERRA")


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

def validar(inf):
    n = int(input("Ingresar un numero mayor a " + str(inf) + " porfavor: "))
    while n < inf:
        n = int(input("Numero ingresado es menor a  " + str(inf) + " porfavor... ingrese de nuevo"))
    return n


def cargar():
    n = validar(0)
    v = []
    tit1 = ("LATE", "Espacio", "Abismo", "Fanatismo")
    tit2 = ("REGISTRATION", "Tristeza", "Felicidad", "Honor")
    nombres = ("KANYE", "Ana", "José", "María", "Pedro", "Belén", "Martín", "Soledad")
    apellidos = ("WEST", "Giuliani", "Trejo", "Masiero", "Duplesis", "Johnson", "Iriarte")
    for i in range(n):
        isbn = random.randint(1, 10000)
        tit = random.choice(tit1) + " y " + random.choice(tit2) + " " + str(i)
        au = random.choice(nombres) + " " + random.choice(apellidos)
        idi = random.randint(1, 5)
        pr = round(random.uniform(10000, 20000,), 2)
        libro = Libro.libro(isbn, tit, au, idi, pr)
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

def binaria(v, isbn):
    n = len(v)
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der) // 2
        if isbn == v[c].isbn:
            return c

        if isbn < v[c].isbn:
            der = c - 1
        else:
            izq = c + 1

    return -1

def buscar(v):
    isbn = int(input("ISBN a buscar: "))
    pos = binaria(v, isbn)
    if pos != -1:
        print("Encontrado!")
        print(v[pos])
        if v[pos].idioma == 4:
            d = (22 * v[pos].precio) // 100
            v[pos].precio -= d
            print("Datos Cambiados:")
            print(v[pos])
    else:
        print("No contamos con el libro", isbn, "SIGA BUSCANDO MAN")
    print()

def generar(v, fd):
    a = input("Autor a filtrar: ")
    p = float(input("Precio a filtrar: "))

    n = len(v)
    m = open(fd, "wb")
    for i in range(n):
        if v[i].autor == a and v[i].importe <= p:
            pickle.dump(v[i], m)
    m.close()
    print("Archivo Generado.")
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

    print("Cantidad de libros mostrados: ", c)
    print()

if __name__ == "__main__":
    principal()