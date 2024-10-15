def promedio(total_caracteres, cant_palabras):
    if cant_palabras > 0:
        return total_caracteres // cant_palabras
    return 0


def main():
    with open("entrada.txt") as archivo_no_leido:
        r1 = 0
        r2 = 0
        r3 = 0
        r4 = 0
        total_caracteres = 0
        cant_palabras = 0
        palabra_mas_larga = ""

        palabra_actual = ""

        for caracter in archivo_no_leido.read():
            if caracter.isalpha():
                palabra_actual += caracter
            elif palabra_actual:

                palabra_actual = ""

        r3 = promedio(total_caracteres, cant_palabras)

        print("Primer resultado:", r1)
        print("Segundo resultado:", r2)
        print("Tercer resultado:", r3)
        print("Cuarto resultado:", r4)


if __name__ == '__main__':
    main()
