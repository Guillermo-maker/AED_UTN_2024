import os.path
import pickle
import random
import Pants

def principal():
    v = []
    op = -1
    fd = "PANTALONES.dat"
    while op != 6:
        print("1. Cargar Arreglo")
        print("2. Mostrar todo los elementos")
        print("3. Generar acumulacion por talle y cintura")
        print("4. Generar Archivo Binario")
        print("5. Mostrar Archivo Binario")
        print("6. SALIR")
        print()
        op = int(input("INGRESAR OPCION: "))

        if op == 1:
            v = cargar_vector()

        elif op == 2:
            if v:
                mostrar(v)
            else:
                print("Archivo no Cargado Todavia")
        elif op == 3:
            if v:
                mat = generar_matriz(v)
                u = int(input("Ingrese la cantidad de unidades minimas a mostrar: "))
                mostrar_matriz(mat, u)
            else:
                print("Archivo no Cargado Todavia")
        elif op == 4:
            if v:
                tela = int(input("Ingrese el tipo de tela: "))
                generar_archivo(fd, v, tela)
            else:
                print("Archivo no Cargado Todavia")
        elif op == 5:
            if v:
                mostrar_archivo(fd)
            else:
                print("Archivo no Cargado Todavia")

        elif op == 6:
            print("CHAITOO!!")



def validar(inf):
    n = int(input("Ingrese la cantidad (mayor a Cero) de registros a cargar: "))
    while n < inf:
        n = int(input("error... INGRESAR la cantidad (mayor a Cero) de registros a cargar: "))
    return n

def add_in_order(v, pantalones):
    izq, der = 0, len(v) - 1
    pos = 0
    while izq <= der:
        med = (izq + der) // 2
        if v[med]. codigo == pantalones.codigo:
            pos = med
            break

        if pantalones.codigo < v[med].codigo:
            der = med - 1
        else:
            izq = med + 1

    if izq > der:
        pos = izq
    v[pos:pos] = [pantalones]

def cargar_vector():
    n = validar(0)
    v = []
    for i in range(n):
        codigo = random.randint(1, 1000)
        nombre = "YZY PNTS" + str(random.randint(1, 10))
        largo = random.randint(30, 50)
        cintura = random.randint(30, 50)
        tela = random.randint(1,3)
        stock = random.randint(1, 1500)
        pantalones = Pants.Pantalon(codigo, nombre, largo, cintura, tela, stock)
        add_in_order(v, pantalones)
    return v

def mostrar(v):
    print("Listado de Pantalones: ")
    n = len(v)
    for i in range(n):
        print(v[i])
        print()


def generar_matriz(v):
    m = [[0] * 21 for i in range(21)]
    n = len(v)
    for i in range(n):
        f = v[i].largo - 30
        c = v[i].cintura - 30
        m[f][c] += v[i].stock
    return m

def mostrar_matriz(mat, u):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            if mat[f][c] > u:
                print("LARGO:", f + 30, " CINTURA: ", c + 30, " STOCK: ", mat[f][c])

def generar_archivo(fd, v, tela):
    n = len(v)
    m = open(fd, "wb")
    for i in range(n):
        if v[i].stock > 0 and v[i].tipo_tela == tela:
            pickle.dump(v[i], m)
    m.close()

def calcular_promedio(cantidad, total):
    promedio = 0
    if cantidad > 0:
        promedio = total / cantidad
    return  promedio

def mostrar_archivo(fd):
    if not os.path.exists(fd):
        print("El archivo no existe o no ha sido encontrado...")
        return

    size = os.path.getsize(fd)
    m = open(fd, "rb")
    acu = cont = 0
    while m.tell() < size:
        reg = pickle.load(m)
        acu += reg.stock
        cont += 1
        print(reg)

    m.close()
    prom = calcular_promedio(cont, acu)
    print("El stock es: ", round(prom, 2), " unidades")
    print()




if __name__ == '__main__':
    principal()