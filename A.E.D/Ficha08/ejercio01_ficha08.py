opciones = True

while opciones == True:
    menu = int(input("Selecionar opciones: ("
                     "'1' suma de cuadrados),"
                     " ('2' Ingresar texto y determinar cant vocales),"
                     " ('3' Ingresar numeros y saber pares e impares),"
                     " ('0' SALIR): "))
    if menu == 0:
        opciones = False

    if menu == 1:
        print("suma de cuadrados")
        n = int(input("Ingrese numeros: "))
        if n > 0:
            suma_cuadrados = 0
            for i in range(1, n + 1):
                suma_cuadrados += i ** 2

            print(suma_cuadrados)
        else:
            print("---n menor a cero---INGRESAR UN NUMERO MAYOR A CERO")
    if menu == 2:
        print("Ingresar texto y determinar cant vocales:")
        texto = input("ingresar un Texto (TERMINAR CON PUNTO) : ")
        cant_vocales = 0
        for car in texto:
            if car in "AEIOUaeiou":
                cant_vocales += 1
        if texto[-1] != ".":
            print("FALTA PUNTO")
        else:
            print(f"Cantidad de vocales: {cant_vocales}")
    if menu == 3:
        print("Ingresar numeros y saber pares e impares")
        lista_nums = []

        while True:
            num = int(input("Ingresar un número (0 para terminar): "))
            if num == 0:
                break
            lista_nums.append(num)

        print("Lista de números ingresados:", lista_nums)

        pares = [num for num in lista_nums if num % 2 == 0]
        impares = [num for num in lista_nums if num % 2 != 0]

        print("Números pares:", pares)
        print("Números impares:", impares)
