def impar(car):
    if car in "13579":
        return True

def promedio(cant, total):
    return (cant // total)


def main():
    # declaracion de contadores, flags, acumuladores
    r1 = r2 = r3 = r4 = 0

    # contador letras
    cLet = 0
    cPalabras = 0

    #r1
    cImpar = cMinuscula = 0

    #r2
    cVocal = cBb = 0

    #r3
    cPalabrasr3 = 0
    cLetrasr3 = 0
    cVocales = 0
    cConsonantes = 0
    cM = cA = 0

    #r4
    cDVocal = 0
    cD = False
    ulLetra = ""

    # manipulacion de archivo
    archivo = open("entrada.txt")
    archivoLeido = archivo.read()
    archivo.close()

    # procesamiento caracter por caracter
    for car in archivoLeido:
        ## afuera de la palabra
        if car in " .":
            if cImpar == 1 and (cLet - 1) == cMinuscula:
                r1 += 1
            if cVocal == 1 and cBb >= 1:
                if r2 == 0:
                    r2 = cLet
                else:
                    if cLet > r2:
                        r2 = cLet
            if cConsonantes > cVocales and cA == 0 and cM == 0:
                cPalabrasr3 += 1
                cLetrasr3 += cLet
            if cDVocal >= 2 and ulLetra in "aeiouAEIOU":
                r4 += 1
            cLet = cImpar = cMinuscula = cVocal = cBb = cConsonantes= cVocales= cM = cA= cDVocal = 0
        ## adentro de la palabra
        else:
            cLet += 1
            ulLetra = car

            if cLet == 1 and impar(car):
                cImpar += 1
            if car in "abcdefghijklmnopqrstuvwxyz":
                cMinuscula += 1
            if cLet == 1 and car in "aeiouAEIOU":
                cVocal += 1
            if car in "bB":
                cBb += 1
            if car in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
                cConsonantes += 1
            if car in "aeiouAEIOU":
                cVocales += 1
            if car in "mM":
                cM += 1
            if car in "aA":
                cA += 1
            if car in "dD":
                cD = True
            if car in "aeiouAEIOU":
                if cD:
                    cDVocal += 1
                    cD = False



    r3 = promedio(cLetrasr3, cPalabrasr3)
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == "__main__":
    main()
