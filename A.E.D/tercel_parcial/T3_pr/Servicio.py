class servicio:
    def __init__(self, id, nom, ti, imp):
        self.id_cliente = id
        self.nombre_cliente = nom
        self.tipo = ti
        self.importe = imp


    def __str__(self):
        r = ""
        r = "{:<10}".format(" -Id Cliente: " + str(self.id_cliente))
        r += "{:<10}".format(" -Nombre de Cliente: " + self.nombre_cliente)
        r += "{:<10}".format(" -Tipo: " + str(self.tipo))
        r += "{:<10}".format(" -Importe:" + str(self.importe))
        return r
