__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


class Pantalon:
	def __init__(self, codigo, nombre, largo, cintura, tipo_tela, stock):
		self.codigo = codigo
		self.nombre = nombre
		self.largo = largo
		self.cintura = cintura
		self.tipo_tela = tipo_tela
		self.stock = stock

	def __str__(self):
		tela = ("Jean", "Gabardina", "Denim")
		r = ""
		r += "{:<20}".format("Codigo: " + str(self.codigo))
		r += "{:<30}".format("Nombre: " + str(self.nombre))
		r += "{:<20}".format("Largo: " + str(self.largo))
		r += "{:<20}".format("Cintura: " + str(self.cintura))
		r += "{:<50}".format("Tipo de Tela: (" + str(self.tipo_tela) + ") " + tela[self.tipo_tela - 1])
		r += "{:<20}".format("Stock:" + str(self.stock) )
		return r
