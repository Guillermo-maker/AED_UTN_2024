#Cargar un arreglo de objetos con los datos de n lotes (cargar n por teclado y validar que sea positivo), de manera
#que en todo momento el arreglo se mantenga ordenado por nombre del propietario. Para esto debe utilizar el
#algoritmo de inserción ordenada con búsqueda binaria (se considerará directamente incorrecta la solución
#basada en cargar el arreglo completo y ordenarlo al final, o aplicar el algoritmo de inserción ordenada pero con
#búsqueda secuencial). La carga de los lotes debe ser automática y con base aleatoria. Cada vez que se ingrese
#en esta opción, el arreglo debe ser creado desde cero y todo contenido anterior debe ser eliminado

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
            










#Cargar un arreglo de registros con los datos de n libros (cargar n por teclado y validar que sea positivo), de
#manera que en todo momento el arreglo se mantenga ordenado por ISBN. Para esto debe utilizar el algoritmo
#de inserción ordenada con búsqueda binaria (se considerará directamente incorrecta la solución basada en
#cargar el arreglo completo y ordenarlo al final, o aplicar el algoritmo de inserción ordenada pero con búsqueda
#secuencial). La carga de los libros debe ser automática y con base aleatoria. Cada vez que se ingrese en esta
#opción, el arreglo debe ser creado desde cero y todo contenido anterior debe ser eliminado






#Cargar un arreglo de registros con los datos de n pantalones (cargar n por teclado y validar que sea positivo),
#de manera que en todo momento el arreglo se mantenga ordenado por código de producto. Para esto debe
#utilizar el algoritmo de inserción ordenada con búsqueda binaria (se considerará directamente incorrecta la
#solución basada en cargar el arreglo completo y ordenarlo al final, o aplicar el algoritmo de inserción ordenada
#pero con búsqueda secuencial). La carga de los pantalones debe ser automática y con base aleatoria. Cada vez
#que se ingrese en esta opción, el arreglo debe ser creado desde cero y todo contenido anterior debe ser
#eliminado.






#Cargar un arreglo de registros con los datos de n piezas (cargar n por teclado y validar que sea positivo), de
#manera que en todo momento el arreglo se mantenga ordenado por código de identificación. Para esto debe
#utilizar el algoritmo de inserción ordenada con búsqueda binaria (se considerará directamente incorrecta la
#solución basada en cargar el arreglo completo y ordenarlo al final, o aplicar el algoritmo de inserción
#ordenada pero con búsqueda secuencial). La carga debe hacerse generando los datos en forma automática
#(con valores aleatorios). NO HAGA CARGA MANUAL.