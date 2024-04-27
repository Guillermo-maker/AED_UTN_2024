#Un binomio al cuadrado (suma) es igual al cuadrado del primer término, 
#más el doble producto del primero por el segundo más el cuadrado del segundo.
# Plantear un script directamente en el shell de Python, que permita mostrar, para dos valores a y b, el valor del cuadrado del binomio. 

a = int(input('ingresa un numero a: '))
b = int(input('ingresa un numero b: '))

cuad = (a ** 2) + (a*b) + (a*b) + (b ** 2)


print('El cuadrado de un binomio es:', cuad)