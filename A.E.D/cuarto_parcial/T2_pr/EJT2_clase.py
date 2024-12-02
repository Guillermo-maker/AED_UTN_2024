class Libro:
    def __init__(self, isb, tit, aut, idi, imp):
        self.isbn = isb
        self.titulo = tit
        self.autor = aut
        self.idioma = idi
        self.importe = imp

    def __str__(self):
        languajes = ("Español", "Inglés", "Portugués", "Francés", "Italiano")

        r = ""
        r = "{:<20}".format("ISBN: " + str(self.isbn))
        r += "{:<35}".format(" - Título: " + self.titulo)
        r += "{:<35}".format(" - Autor: " + self.autor)
        r += "{:<10}".format(" - Idioma: " + str(self.idioma))
        r += "{:<13}".format(" (" + languajes[self.idioma - 1] + ")")
        r += "{:<17}".format(" - Importe: " + str(self.importe))
        return r


# print(Libro(1919191, "Don Quijote", "Miguel de Cervantes", 1, 31674.86))
# print(Libro(1829811, "Ulises", "Joyce", 2, 245674.86))
