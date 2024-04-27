#Desarrolle un programa o script Python que permita cargar por teclado un número entero que representa la  cantidad de segundos que pasaron desde un evento dado.
#El programa debe convertir esa cantidad de segundos  a la cantidad de horas, minutos y segundos que transcurrieron. Por ejemplo, si la cantidad de segundos
# ingresada es 4452 deberá mostrar un mensaje que informe que el tiempo transcurrido fue de 1 hora, 14 minutos  y 12 segundos.
#Pero la conversión solo debe mostrarse si la cantidad de horas totales obtenida es menor o igual a 24. Si esa cantidad de horas totales es mayor a 24, el programa debe mostrar un mensaje de la forma "Excedido".
# Se le pedirá comprobar su programa para cuatro cantidades de segundos, que deberá cargar por teclado.
#Además, el desafío incluye una consigna adicional, en la cual se le pedirá que haga el proceso inverso: deberá tomar tres datos, que serán el valor en horas,
# el valor en minutos y el valor en segundos transcurridos desde un evento dado, y su programa deberá calcular la cantidad total de segundos a partir de esos datos. Por ejemplo,
# si los datos ingresados fuesen: horas = 4, minutos = 36 y segundos = 8 entonces el resultado a obtener es que la cantidad total de segundos es 16568.

y = int(input("seleccione si desea convertir de segundos a horas (1) o de  horas a segundos (2): ")) #Seleccionamos la opcion del usuario

#si la opcion es uno (1)  se convierte de segundos a horas
if y == 1:
    x = int(input("Ingrese la cantidad de segundos que desee convertir en horas: ")) #Tomamos el input del usuario
    if x < 86400:                    #Si el tiempo ingresado no supera los 86400 segundos, que son 24horas, prosigue con el ejercicio
        hour = x // 3600   # Total de segundos  por una hora es 3600
        minute = (x - (hour * 3600)) // 60    # Restamos las horas y obtenemos los minutos
        second = x % 60     # Conseguir el resto de los segundos si no es divisible por 3600 o por 60
        print("%d segundos es igual a %d:%d:%d" % (x , hour, minute, second))
    else:                #Si la opción es mayor a un dia, da un mensaje de error
        print("excedido")
#si la opcion es dos (2)  se convierte de hroas a segundos
elif y == 2:
            h = int(input("ingrese la cantidad de horas que desea convertir a segundos: ")) #Se le pide al usuario ingresar la cantidad de horas a convertir
            m = int(input("Ahora los  minutos: "))  #Ahora los minutos
            s = int(input("Por ultimo los segundos: ")) #Y por ultimo los segundos
            totalsegundos = h*3600 + m*60 +s #Se suman todos los valores para obtener total de segundos.
            print(totalsegundos,"segundos")