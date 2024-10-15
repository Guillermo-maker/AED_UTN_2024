class juicio:
    def __init__(self, cod, des, ti, no, imp ):
        self.codigo = cod
        self.descripcion = des
        self.tipo = ti
        self.nombre = no
        self.importe = imp

    def __str__(self):
        r = ""
        r = "{:<10}".format(" - Codigo Juicio: " + str(self.codigo))
        r += "{:<10}".format(" - Descripcion: " + self.descripcion)
        r += "{:<10}".format(" - Tipo: " + str(self.tipo))
        r += "{:<10}".format(" - Nombre del Cliente: " + self.nombre)
        r += "{:<10}".format(" - Monto: " + str(self.importe))
        return r