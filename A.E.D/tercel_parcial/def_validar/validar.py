# TODOS LOS TURNOS SON IGUALES

def validar(inf):
    n = int(input("INGRESAR VALOR DEL ARREGLO " + str(inf) + " Porfavor"))
    while n <= inf:
        n = int(input("Error... Ingrese un valor mayor a " + str(inf)))
    return n

def validar_2(inf):
    n = int(input("INGRESAR VALOR DEL ARREGLO " + str(inf) + " Porfavor"))
    while n <= inf:
        n = int(input("Error... porfavor un valor mayor a" + str(inf)))
    return n
