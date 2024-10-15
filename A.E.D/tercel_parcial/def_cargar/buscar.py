import random


def validar(inf):
    n = int(input("INGRESAR VALOR DEL ARREGLO " + str(inf) + " Porfavor"))
    while n <= inf:
        n = int(input("Error... Ingrese un valor mayor a " + str(inf)))
    return n

def cargar():
    n = validar(0)
    v = n * [None]
    descripcion = ("Alto", "Bajo", "Blanco", "Negro")
    for i in range(n):
        cid = random.randint(0, 20000)
        des = random.choice(descripcion)
        tip = random.randint(0, 39)
        imp = round(random.uniform(0, 20000), 2)
        v[i] = Clase.empleo(cid, des, tip, imp)
    return v
    print("Datos cargados")

