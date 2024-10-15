def cant_palabras_seis_vocal_digito(archivo_leido):
    palabras = archivo_leido.split()
    r1 = 0
    for palabra in palabras:  # CREO UN FOR QUE RECORRA TODAS LA LISTA
        if len(palabra) == 6:  # SI LA LONGITUD DE LA PALABRA ES 6,
            tiene_vocal = False  # SE CREAN LAS FLAGS PARA VOCAL Y DIGITO
            tiene_digito = False
            for car in palabra:  # CREO OTRO FOR QUE RECORRE LAS PALABRAS DE LONGITUD 6
                if car.lower() in "aeiou":  # VERIFICO QUE TENGAN VOCALES
                    tiene_vocal = True  # SI CUMPLE SE ACTUALIZA A TRUE
                if car.isdigit():  # VERIFICO QUE TENGAN DIGITOS
                    tiene_digito = True  # SI CUMPLE SE ACTUALIZA A TRUE
            if tiene_vocal and tiene_digito:  # CONDICION SI CUMPLE LAS DOS SE SUMA A R1
                r1 += 1
    return r1


def promedio_caracteres_palabra(archivo_leido):
    palabras = archivo_leido.split()
    cant_palabras_r_e = 0
    cant_caracteres_total = 0
    for palabra in palabras:
        cuenta_r = palabra.lower().count('r')
        cuenta_e = palabra.lower().count('e')

        if cuenta_r == 1 and cuenta_e >= 2:
            cant_palabras_r_e += 1
            cant_caracteres_total += len(palabra)

    if cant_palabras_r_e > 0:
        r2 = cant_caracteres_total // cant_palabras_r_e
    else:
        r2 = 0
    return r2


def cant_empieza_termina_vocal_distinta(archivo_leido):
    palabras = archivo_leido.split()
    r3 = 0
    for palabra in palabras:
        inicio = palabra[0].lower()  # Primer carácter convertido a minúscula
        fin = palabra[-1].lower()  # Último carácter convertido a minúscula

        if inicio in "aeiou" and fin in "aeiou" and inicio != fin:
            r3 += 1
    return r3


def cuantas_palabras_expresion_fi_con_n_t(archivo_leido):
    palabras = archivo_leido.split()
    r4 = 0
    for palabra in palabras:
        contiene_fi = 'fi' in palabra.lower()
        contiene_n = 'n' in palabra.lower()
        contiene_t = 't' in palabra.lower()

        if contiene_fi:
            if contiene_n or contiene_t:
                r4 += 1
    return r4


def main():
    with open("entrada.txt") as archivo_sin_leer:
        archivo_leido = archivo_sin_leer.read()

    r1 = cant_palabras_seis_vocal_digito(archivo_leido)
    r2 = promedio_caracteres_palabra(archivo_leido)
    r3 = cant_empieza_termina_vocal_distinta(archivo_leido)
    r4 = cuantas_palabras_expresion_fi_con_n_t(archivo_leido)
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == "__main__":
    main()
