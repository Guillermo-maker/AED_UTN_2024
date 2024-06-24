# Desarrollar un programa que permita procesar funciones de un complejo de cines. Por cada función se conoce: cantidad de espectadores y descuento (S/N).
# La carga termina cuando la cantidad de espectadores sea igual a 0 (cero).

# El programa deberá:

# a) Calcular la recaudación total del complejo, considerando que el valor de la entrada es de $50 en los días con descuento y $75 en los días sin descuento.

# b) Determinar cuántas funciones con descuento se efectuaron y qué porcentaje representan sobre el total de funciones.


recaudacion_total = 0
cant_funciones_descuento = 0
funciones_total = 0
recaudacion_funcion = 0
porcentaje_descuento = 0

while True:
    espectadores = int(input("Ingrese la cantidad de espectadores, ( si quiere terminar ingresar 0 ): "))
    if espectadores == 0:
        break

    descuento = input("hay descuento ( S/N ): ")

    if descuento == "S":
        recaudacion_funcion = espectadores * 50
        cant_funciones_descuento += 1
    if descuento == "N":
        recaudacion_funcion = espectadores * 75
    else:
        print("Ingresar bien los datos")

    recaudacion_total += recaudacion_funcion
    funciones_total += 1

    porcentaje_descuento = (cant_funciones_descuento / funciones_total) * 100

print(f"Recaudación total: ${recaudacion_total}")
print(f"Funciones con descuento: {cant_funciones_descuento} ({porcentaje_descuento:.2f}% del total)")
