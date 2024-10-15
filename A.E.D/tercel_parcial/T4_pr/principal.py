import random
import Juicio


def principal():
    v = []
    op = -1

    while op != 5:
        print("1. Cargar Datos ")
        print("2. Mostrar Datos ")
        print("3. Contar/Acumular Datos ")
        print("4. Buscar ")
        print("5. Salir ")
        print()
        op = int(input("Ingrese la opcion: "))

        if op == 1:
            v = cargar()
        elif op == 2:
            if v:
                mostrar(v)
            else:
                "El vector todavia no esta cargado"
        elif op == 3:
            if v:
                contar(v)
            else:
                "El vector todavia no esta cargado"
        elif op == 4:
            if v:
                buscar(v)
            else:
                "El vector todavia no esta cargado"
        elif op == 5:
            print("Progama Terminado.")


def validar(inf):
    n = int(input("Ingrese el tamaño del vector mayor a " + str(inf) + " porfavor: "))

    while n <= inf:
        n = int(input("Error... en creacion de vector, ingrese valor otra vez porfavor: "))
    return n


def cargar():
    n = validar(0)
    v = n * [None]

    nombres = ("Miguel", "Paulo", "Cristian", "Kanye", " Yves")
    descrip = ("inocente", "Culpable")

    for i in range(n):
        cod = random.randint(0, 100)
        des = random.choice(descrip)
        ti = random.randint(1, 15)
        no = random.choice(nombres)
        imp = round(random.uniform(1, 20000), 2)
        v[i] = Juicio.juicio(cod, des, ti, no, imp)
    print("Datos cargados")
    print()
    return v


def mostrar(v):
    n = len(v)

    for i in range(n - 1):
        for j in range(n + i, 1):
            if v[i].descripcion > v[j].descrpicion:
                v[i], v[j] = v[j], v[i]

    cj = 0

    mon = float(input("Importe a filtrar (se mostraran los juicios cuyo importe sea mayor a este): "))
    print("Listado de juicios con importe mayor a ", mon, ";")
    for i in range(n):
        if v[i].importe > mon:
            cj += 1
            print(v[i])
    print("Cantidad de juicios mostrados:", cj)
    print()


def contar(v):
    n = len(v)
    ct = 15 * [0]

    for i in range(n):
        # El tipo de juicio viene entre 1 y 15... restar uno para compatibilizar con los indices del vector c...
        ind = v[i].tipo - 1
        ct[ind] += 1

    c = int(input("Cantidad a filtrar (se mostraran los contadores con valor mayor a este): "))
    print("Cantidad de juicios por tipo:")
    for k in range(15):
        if ct[k] > c:
            # si al contar/acumular reste uno, entoncesen pantalla, y SOLO EN PANTALLA, mostrar k+1...
            print("Tipo de juicio:", k + 1, "Cantidad:", ct[k])
    print()


def buscar(v):
    n = len(v)
    cod = int(input("Numero de codigo juicio a buscar: "))
    for i in range(n):
        if cod == v[i].codigo:
            print("Encontrado - Datos actuales:")
            print(v[i])
            hon = float(input("Nuevo monto de honorarios a asignar: "))
            v[i].importe = round(hon, 2)
            print("Datos con el importe de honorarios actualizado")
            print(v[i])
            print()
            return
    print("No estaba")
    print()


if __name__ == "__main__":
    principal()
