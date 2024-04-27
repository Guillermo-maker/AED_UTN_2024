

rojo = 0
negro = 0

while (True):
    voto = input("INGRESAR VOTO: (SI) ROJO (NO) NEGR0: ")
    
    if voto == "stop":
        break    

    if voto == "si":
        rojo +=1
        porcentaje_rojo = rojo / (rojo + negro) * 100
        print ("votos de rojo:", porcentaje_rojo)
    elif voto == "no":
        negro += 1
        porcentaje_negro = negro / (rojo + negro) * 100
        print ("votos de negro :", porcentaje_negro)
    else:
        print ("ingresaste mal los datos")

 

