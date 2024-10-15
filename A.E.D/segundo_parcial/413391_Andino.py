def digito_impar(archivo_leido):
    r1 = 0
    palabras = archivo_leido.split()  # Divide el contenido en palabras
    for car in palabras:
        if car[0] in "13579" and car[1:].islower():
            r1 += 1
    return r1


def palabra_mas_larga(archivo_leido):
    r2 = 0
    palabras = archivo_leido.split()
    for car in palabras:
        if car[0] in "AEIOUaeiou" and 'b' in car.lower():
            if len(car) > r2:
                r2 = len(car)
    return r2
def promedio_de_consonantes(archivo_leido):
    palabras = archivo_leido.split()
    total_caracteres = 0
    cantidad_palabras = 0

    for palabra in palabras:
        consonantes = sum(1 for letra in palabra if letra in "BCDFGHJKLMNPQRSTUVWXYZbcdfghjklmnpqrstvwxyz")
        vocales = sum(1 for letra in palabra if letra in "AEIOUaeiou")

        if consonantes > vocales and 'm' not in palabra.lower() and 'a' not in palabra.lower():
            total_caracteres += len(palabra)
            cantidad_palabras += 1

    if cantidad_palabras > 0:
        r3 = total_caracteres // cantidad_palabras
    else:
        r3 = 0

    return r3


def palabras_con_d_vocal(archivo_leido):
    palabras = archivo_leido.split()
    r4 = 0

    for car in palabras:
        d_count = 0
        tiene_vocal_final = False

        # Verificar si la palabra termina con una vocal
        if car[-1] in "AEIOUaeiou":
            tiene_vocal_final = True

        # Contar las ocurrencias de "d" seguida de una vocal
        i = 0
        while i < len(car) - 1:
            if car[i].lower() == 'd' and car[i + 1].lower() in "aeiou":
                d_count += 1
                i += 2  # Saltar al siguiente carácter después de la vocal
            else:
                i += 1

        # Si tiene más de una ocurrencia de "d" + vocal y termina con vocal, contarla
        if d_count >= 2 and tiene_vocal_final:
            r4 += 1

    return r4


def main():
    with open("entrada.txt", "r") as archivo_sin_leer:
        archivo_leido = archivo_sin_leer.read().strip()

    r1 = digito_impar(archivo_leido)
    r2 = palabra_mas_larga(archivo_leido)
    r3 = promedio_de_consonantes(archivo_leido)
    r4 = palabras_con_d_vocal(archivo_leido)
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == "__main__":
    main()
