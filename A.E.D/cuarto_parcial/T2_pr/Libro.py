class libro():
    def __init__(self,isbn, tit, au, idi, pr):
        self.isbn = isbn
        self.titulo = tit
        self.autor = au
        self.idioma = idi
        self.precio = pr

    def __str__(self):
        idiomas = ("Español", "Inglés", "Portugués", "Francés", "Italiano")

        r = ""
        r = "{:<10}".format("ISBN: " + str(self.isbn))
        r += "{:<10}".format(" - Titulo: " + self.titulo)
        r += "{:<10}".format(" - Autor: " + self.autor)
        r += "{:<10}".format(" (" + idiomas[self.idioma - 1] + ") ")
        r += "{:<10}".format(" - Precio: " + str(self.precio))
        return r
