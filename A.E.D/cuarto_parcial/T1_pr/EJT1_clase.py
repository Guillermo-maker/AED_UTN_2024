class Lote:
    def __init__(self, nom, man, lot, ori, sup, imp):
        self.nombre = nom
        self.manzana = man
        self.lote = lot
        self.orientacion = ori
        self.superficie = sup
        self.importe = imp

    def __str__(self):
        puntos = ("Norte", "Sur", "Este", "Oeste")

        r = ""
        r = "{:<35}".format("Cliente: " + self.nombre)
        r += "{:<15}".format(" - Manzana: " + str(self.manzana))
        r += "{:<12}".format(" - Lote: " + str(self.lote))
        r += "{:<15}".format(" - Orientación: " + str(self.orientacion))
        r += "{:<10}".format(" (" + puntos[self.orientacion - 1] + ")")
        r += "{:<25}".format(" - Superficie: " + str(self.superficie))
        r += "{:<17}".format(" - Importe: " + str(self.importe))
        return r
