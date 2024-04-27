# Solicitar el monto total recaudado
total_recaudado = float(input("Ingresar el monto que recaudó la película: $"))

# Lista de tuplas con los datos de los actores y sus porcentajes de pago
actores = [
    ("Guillermo Andino", 50),
    ("Tom Cruise",50),
]

# Calcular y mostrar la cantidad que cada actor va a ganar
for actor, porcentaje_pago in actores:
    monto_a_pagar = total_recaudado * (porcentaje_pago / 100)
    print(f"El actor {actor} va a ganar ${monto_a_pagar:.2f}")
