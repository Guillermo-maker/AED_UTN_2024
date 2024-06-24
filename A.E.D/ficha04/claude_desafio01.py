def segundos_a_horas_minutos_segundos(segundos_totales):
    horas = segundos_totales // 3600
    minutos = (segundos_totales % 3600) // 60
    segundos = (segundos_totales % 3600) % 60

    if horas > 24:
        print("Excedido")
    else:
        print(f"El tiempo transcurrido fue de {horas} hora(s), {minutos} minuto(s) y {segundos} segundo(s).")

def horas_minutos_segundos_a_segundos(horas, minutos, segundos):
    segundos_totales = horas * 3600 + minutos * 60 + segundos
    return segundos_totales

# Solicitar segundos totales al usuario
segundos_totales = int(input("Ingrese la cantidad de segundos transcurridos: "))
segundos_a_horas_minutos_segundos(segundos_totales)

# Solicitar horas, minutos y segundos al usuario
horas = int(input("Ingrese la cantidad de horas transcurridas: "))
minutos = int(input("Ingrese la cantidad de minutos transcurridos: "))
segundos = int(input("Ingrese la cantidad de segundos transcurridos: "))

segundos_totales = horas_minutos_segundos_a_segundos(horas, minutos, segundos)
print(f"La cantidad total de segundos transcurridos es: {segundos_totales}")