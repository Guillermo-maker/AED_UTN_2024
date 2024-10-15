def main():
    with open("entrada.txt") as archivo_no_leido:
        r1 = 0
        r2 = 0
        r3 = 0
        r4 = 0
        cantidad_palabra = 0
        total_caracteres = 0
        palabra_mas_larga = ""

        palabra_actual = ""  # Variable para construir la palabra actual

        # Iterar sobre cada caracter del archivo
        for caracter in archivo_no_leido.read():
            if caracter.isalnum():  # Si el caracter es alfanumérico (letra o número)
                palabra_actual += caracter
            elif palabra_actual:  # Si hay una palabra construida
                # Procesar la palabra actual
                empieza_vocal = palabra_actual[0].lower() in "aeiou"  # Comprueba si la palabra empieza con una vocal
                tiene_b = 'b' in palabra_actual.lower()  # Comprueba si la palabra contiene al menos una letra 'b'

                if empieza_vocal and tiene_b:
                    if len(palabra_actual) > len(palabra_mas_larga):
                        palabra_mas_larga = palabra_actual

                    r1 += 1  # Incrementa el contador r1 si la palabra cumple las condiciones

                consonantes = sum(1 for letra in palabra_actual if letra in "BCDFGHJKLMNPQRSTUVWXYZbcdfghjklmnpqrstvwxyz")

                vocales = sum(1 for letra in palabra_actual if letra in "AEIOUaeiou")

                if consonantes > vocales and 'm' not in palabra_actual.lower() and 'a' not in palabra_actual.lower():
                    cantidad_palabra += 1
                    total_caracteres += len(palabra_actual)

                if palabra_actual in ["d", "a", "e", "i", "o", "u"] and palabra_actual[-1] in "aeiou":
                    r4 += 1

                palabra_actual = ""  # Reiniciar la palabra actual después de procesarla

        # Calcular r3 si hay palabras que cumplen las condiciones
        if cantidad_palabra > 0:
            r3 = total_caracteres // cantidad_palabra

        if palabra_mas_larga:
            r2 = len(palabra_mas_larga)

        print("Primer resultado:", r1)
        print("Segundo resultado:", r2)
        print("Tercer resultado:", r3)
        print("Cuarto resultado:", r4)


if __name__ == '__main__':
    main()
