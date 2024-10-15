def palabras_comienzan_digito_impar(archivo_leido):
    palabras = archivo_leido.split()
    r1 = 0
    for palabra in palabras:
        empieza_digito = palabra[0] in "13579"
        minus_palabra = palabra[1:].islower()
        letra_palabra = palabra[-1].isalpha()
        if empieza_digito and minus_palabra and letra_palabra:
            r1 += 1

    return r1


def cant_car_palabra_mas_larga(archivo_leido):
    palabras = archivo_leido.split()
    r2 = 0
    for palabra in palabras:
        if palabra[0].lower() in "aeiou" and "b" in palabra.lower():
            if len(palabra) > r2:
                r2 = len(palabra)

    return r2


def promedio_caracteres_por_palabra_cons_que_vocales(archivo_leido):
    palabras = archivo_leido.split()
    cantidad_palabra = 0
    total_caracteres = 0
    r3 = 0
    for palabra in palabras:
        consonantes = sum(1 for letra in palabra if letra in "BCDFGHJKLMNPQRSTUVWXYZbcdfghjklmnpqrstvwxyz")
        vocales = sum(1 for letra in palabra if letra in "AEIOUaeiou")

        if consonantes > vocales and 'm' not in palabra.lower() and 'a' not in palabra.lower():
            cantidad_palabra += 1
            total_caracteres += len(palabra)

        if total_caracteres > 0:
            r3 = total_caracteres // cantidad_palabra
        else:
            r3 = 0

    return r3

def cant_palabras_d_mas_vocal_termina_vocal(archivo_leido):
    palabras = archivo_leido.split()
    r4 = 0
    for palabra in palabras:
        if palabra in "daeiou" and palabra[-1] in "aeiou":
            r4 += 1
    return r4

def main():
    with open("entrada.txt") as archivo_no_leido:
        archivo_leido = archivo_no_leido.read().strip(".")

        r1 = palabras_comienzan_digito_impar(archivo_leido)
        r2 = cant_car_palabra_mas_larga(archivo_leido)
        r3 = promedio_caracteres_por_palabra_cons_que_vocales(archivo_leido)
        r4 = cant_palabras_d_mas_vocal_termina_vocal(archivo_leido)

        print("Primer resultado:", r1)
        print("Segundo resultado:", r2)
        print("Tercer resultado:", r3)
        print("Cuarto resultado:", r4)



if __name__ == '__main__':
    main()
