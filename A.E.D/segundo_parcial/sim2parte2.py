def ejercicios(text):
    import re

    words = text.split()
    count_digito_impar = 0
    max_length_vocal_b = 0
    valid_words_lengths = []
    count_d_y_vocal = 0
    pattern = re.compile(r"(d[aeiouAEIOU])")

    for word in words:
        # Digito impar palabra minúscula
        if word[0] in "13579" and word[1:].islower():
            count_digito_impar += 1

        # Palabra más larga con vocal y "b"
        if word[0].lower() in "aeiou" and ("b" in word.lower()):
            max_length_vocal_b = max(max_length_vocal_b, len(word))

        # Promedio caracteres palabra consonantes
        vowels = sum(1 for char in word if char.lower() in "aeiou")
        consonants = sum(
            1 for char in word if char.isalpha() and char.lower() not in "aeiou"
        )
        if consonants > vowels and "m" not in word.lower() and "a" not in word.lower():
            valid_words_lengths.append(len(word))

        # Contar palabras con "d" y vocal
        if len(pattern.findall(word)) >= 2 and word[-1].lower() in "aeiou":
            count_d_y_vocal += 1

    promedio_caracteres = (
        (sum(valid_words_lengths) // len(valid_words_lengths))
        if valid_words_lengths
        else 0
    )

    return count_digito_impar, max_length_vocal_b, promedio_caracteres, count_d_y_vocal


def main():
    with open("entrada.txt", "r") as file:
        text = file.read().strip(".")

    r1, r2, r3, r4 = ejercicios(text)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == "__main__":
    main()
