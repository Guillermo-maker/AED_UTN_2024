def es_consonante(letra):
    vocales = 'aeiouáéíóúü'
    return letra.isalpha() and letra.lower() not in vocales


def cant_palabras_digito_consonante(archivo_leido):
    palabras = archivo_leido.split()
    r1 = 0
    for palabra in palabras:
        if len(palabra) >= 4:
            # Verificar si hay un dígito en la segunda o tercera posición
            if (palabra[1].isdigit() or (len(palabra) > 2 and palabra[2].isdigit())):
                # Contar las consonantes a partir de la cuarta posición
                consonantes_desde_cuarta = [letra for letra in palabra[3:] if es_consonante(letra)]
                if len(consonantes_desde_cuarta) >= 2:
                    r1 += 1
    return r1


def es_vocal(letra):
    vocales = 'aeiouáéíóúü'
    return letra.isalpha() and letra.lower() in vocales


def promedio_palabras_vocal(archivo_leido):
    palabras = archivo_leido.split()
    cant_palabras_vocales = 0
    cant_palabras_totales = len(palabras)
    r2 = 0
    for palabra in palabras:
        palabra_con_vocales = any(es_vocal(letra) for letra in palabra)
        digito_final = palabra[-1].isdigit()
        if palabra_con_vocales and digito_final:
            cant_palabras_vocales += 1
    if palabra_con_vocales > 0:
        r2 = (cant_palabras_vocales * 100) // cant_palabras_totales
    else:
        r2 = 0

    return r2


def cuantas_tres_vocales(archivo_leido):
    palabras = archivo_leido.split()
    r3 = 0
    for palabra in palabras:
        if len(palabra) >= 4:
            # Verificar si las primeras tres posiciones contienen solo vocales
            if all(es_vocal(letra) for letra in palabra[:3]):
                r3 += 1
        return r3


def cantida_de_palabra(archivo_leido):
    palabras = archivo_leido.split()
    r4 = 0
    for palabra in palabras:
        palabra = palabra.lower()  # Convertir la palabra a minúsculas para hacer la búsqueda insensible a mayúsculas
        if 'de' in palabra and 't' in palabra[palabra.index('de') + 2:]:
            r4 += 1
    return r4


def main():
    with open("entrada.txt") as archivo_sin_leer:
        archivo_leido = archivo_sin_leer.read()
    r1 = cant_palabras_digito_consonante(archivo_leido)
    r2 = promedio_palabras_vocal(archivo_leido)
    r3 = cuantas_tres_vocales(archivo_leido)
    r4 = cantida_de_palabra(archivo_leido)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == '__main__':
    main()
