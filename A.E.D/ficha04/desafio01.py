a = int(input("(1 si de SEGUNDOS a H:M:S) a (2 si de H:M:S a SEGUNDOS): "))

if a == 1:
    b = int(input("INGRESAR LOS SEGUNDOS: "))
    if b <= 86400:
        hora = b // 3600
        minuto = (b - (hora * 3600)) // 60
        segundo = b % 60
        print("%d segundos es igual a %d:%d:%d" % (b, hora, minuto, segundo))
    else:
        print("excedido")
elif a == 2:
    h = int(input("horas a segundos: "))
    m = int(input("minutos: "))
    s = int(input("segundos: "))
    totalsegundos = h*3600 + m*60 +s #Se suman todos los valores para obtener total de segundos.
    print(totalsegundos,"segundos")