#Plantear un script (directamente en el shell de Python) que permita informar,
# para dos valores a y b el resultado de la división a/b y el resto de esa divisón.

a = int(input('ingresa un numero1: '))
b = int(input('ingresa un numero2: '))
div = a//b
resto = a % b

print('El resultado de la division es: ', div)

print('El resultado del resto es: ', resto)