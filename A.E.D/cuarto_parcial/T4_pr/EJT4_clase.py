class Pieza:
    def __init__(self, cod, des, tip, sec, sto):
        self.codigo = cod
        self.descripcion = des
        self.tipo = tip
        self.sector = sec
        self.stock = sto

    def __str__(self):
        r = ""
        r = "{:<15}".format("Código: " + str(self.codigo))
        r += "{:<30}".format(" - Descripción: " + self.descripcion)
        r += "{:<13}".format(" - Tipo: " + str(self.tipo))
        r += "{:<13}".format(" - Sector: " + str(self.sector))
        r += "{:<15}".format(" - Stock: " + str(self.stock))
        return r
