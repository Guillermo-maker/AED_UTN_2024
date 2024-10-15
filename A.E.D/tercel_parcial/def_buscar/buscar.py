# TURNO 1

#Determinar si existe un empleo cuyo número de identificación sea igual num, siendo num un valor que se carga
#por teclado. Si existe, mostrar solo su descripción y el sueldo a pagar. Si no existe, informar con un mensaje. Si
#existe más de un registro que coincida con esos parámetros de búsqueda, debe mostrar sólo el primero que
#encuentre. La búsqueda debe detenerse al encontrar el prime objeto que coincida con el criterio pedido.

def buscar_T1(v):
    n = len(v)
    num = int(input("Número de identificación del empleo a buscar: "))
    for i in range(n):
        if num == v[i].identificador:
            print("Encontrado:")
            print("Desacripcion del empleo:", v[i].descripcion, " - Sueldo: ", v[i].importe)
            print()
            return
    print("No Estaba...")
    print()


# TURNO 2

#Determinar si existe un ticket cuyo número de identificación del pasajero sea igual a id. Si se encuentra,
#mostrar el número de asiento y el país de destino. Si no se encuentra, indicar con un mensaje que no existe.
#Debe mostrar los datos del primero que encuentre y detener en ese momento la búsqueda (sin importar si hay
#más de un registro con el mismo código).

def buscar_T2(v):
    n = len(v)
    id = int(input("Numero de identificacion del pasajero a buscar: "))
    for i in range(n):
        if id == v[i].pasajero:
            print("Encontrado:")
            print("Numero de asiento:", v[i].asiento, " - Pais destino:", v[i].pais)
            print()
            return
    print("No estaba...")
    print()

# TURNO 3

#Determinar si existe un servicio cuyo nombre de cliente sea igual a nom (cargar nom por teclado). Si lo
#encuentra, cambie el valor del atributo importe, sumando 2000 al valor anterior, y muestre todos los datos de
#ese objeto modificado. Si no lo encuentra, informe con un mensaje que no existe. Debe detener la búsqueda
#en el primero que encuentre (sin importar si hay más de un objeto que cumpla el criterio pedido).


def buscar_T3(v):
    n = len(v)
    nom = int("Nombre del cliente a Buscar: ")
    for i in range(n):
        if nom == v[i].nombre_cliente:
            print("Encontrado - Datos Actuales: ")
            print(v[i])
            v[i].importe += 2000
            print("Datos del importe actualizado: ")
            print(v[i])
            return
    print("No estaba... ")
    print()

# TURNO 4

#Determinar si existe un juicio cuyo código de expediente sea igual a cod. Si existe alguno, modificar el monto
#de honorarios de ese objeto tomando el nuevo valor por teclado, y mostrar los datos de ese juicio incluyendo
#esa modificación. Si no existe, informar con un mensaje. Debe mostrar los datos del primero que encuentre, y
#detener la búsqueda en el primero que encuentre (sin importar si hay más de un objeto que cumpla el criterio
#pedido).

def buscar_T4(v):
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
    print("No Estaba")
    print()

# TURNO E

#Buscar una publicacion cuyo título coincida con nom y cuyo tipo sea igual a t (los valores nom y t se cargan por
#teclado). Si existe, mostrar sus datos. Si no existe indicar con un mensaje. Debe mostrar los datos del primero
#que encuentre, y detener la búsqueda en ese momento (sin importar si hay más de un registro que cumpla el
#criterio pedido).

def buscar(v):
    n = len(v)
    nom = input("Titulo de la publicacion a buscar: ")
    t = int(input("Tipo de la publicacion a buscar (numero entre 1 y 30):"))
    for i in range(n):
        if nom == v[i].titulo and t == v[i].tipo:
            print("Encontrado:")
            print(v[i])
            print()
            return
    print("No Estaba")
    print()