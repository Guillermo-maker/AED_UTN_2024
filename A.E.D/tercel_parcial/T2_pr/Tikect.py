class ticket:
    def __init__(self, cv, idp, pa, naa, imp):
        self.codigo_vuelo = cv
        self.id_pasajero = idp
        self.pais = pa
        self.numero_asiento = naa
        self.importe = imp


    def __str__(self):
        r = ""
        r =  "{:<15}".format(" - Codigo de vuelo: " + self.codigo_vuelo)
        r += "{:<15}".format(" - id del pasajero: " + str(self.id_pasajero))
        r += "{:<15}".format(" - Pais: " + str(self.pais))
        r += "{:<15}".format(" - Numero de asiento: " + str(self.numero_asiento))
        r += "{:<15}".format(" - Importe: " + str(self.importe))
        return r
