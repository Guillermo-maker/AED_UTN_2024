import os.path
import pickle
import random

import EJT3_clase


def menu():
	cadena = 'Menu de Opciones:\n' + \
	         '===========================================\n' + \
	         '1 - Cargar un arreglo de registros\n' \
	         '2 - Mostrar todos los elementos del vector\n' \
	         '3 - Generar acumulacion por talle y cintura\n' \
	         '4 - Generar Archivo Binario\n' \
	         '5 - Mostrar Archivo Binario\n' \
	         '0 - Salir\n' \
	         'Ingrese su opcion: '
	return int(input(cadena))


def validar(minimo):
	n = int(input("Ingrese la cantidad de registros a cargar: "))
	while n <= minimo:
		n = int(input("Error!!!! Ingrese la cantidad de registros a cargar: "))
	return n


def add_in_order(v, reg):
	izq, der = 0, len(v) - 1
	pos = 0
	while izq <= der:
		med = (izq + der) // 2
		if v[med].codigo == reg.codigo:
			pos = med
			break

		if reg.codigo < v[med].codigo:
			der = med - 1
		else:
			izq = med + 1

	if izq > der:
		pos = izq
	v[pos:pos] = [reg]


def cargar_vector():
	n = validar(0)
	v = []
	for i in range(n):
		codigo = random.randint(100, 100000)
		nombre = "Pantalon " + str(random.randint(1500, 33450))
		largo = random.randint(30, 50)
		cintura = random.randint(30, 50)
		tela = random.randint(1, 3)
		stock = random.randint(1, 1500)
		reg = EJT3_clase.Pantalon(codigo, nombre, largo, cintura, tela, stock)
		add_in_order(v, reg)
	return v


def mostrar(v):
	print("Listado de Pantalones")
	n = len(v)
	for i in range(n):
		print(v[i])


def generar_matriz(v):
	m = [[0] * 21 for i in range(21)]
	n = len(v)
	for i in range(n):
		f = v[i].largo - 30
		c = v[i].cintura - 30
		m[f][c] += v[i].stock

	return m


def mostrar_matriz(mat, u):
	for f in range(len(mat)):
		for c in range(len(mat[f])):
			if mat[f][c] > u:
				print("Largo:", f + 30, " Cintura:", c + 30, " Stock:", mat[f][c])


def generar_archivo(fd, v, tela):
	n = len(v)
	m = open(fd, "wb")
	for i in range(n):
		if v[i].stock > 0 and v[i].tipo_tela == tela:
			pickle.dump(v[i], m)
	m.close()


def calcular_promedio(cantidad, total):
	promedio = 0
	if cantidad > 0:
		promedio = total / cantidad

	return promedio


def mostrar_archivo(fd):
	if not os.path.exists(fd):
		print("El archivo no existe!!!!")
		return

	size = os.path.getsize(fd)
	m = open(fd, "rb")
	acu = cont = 0
	while m.tell() < size:
		reg = pickle.load(m)
		acu += reg.stock
		cont += 1
		print(reg)

	m.close()
	prom = calcular_promedio(cont, acu)
	print("El Stock promedio disponible es", round(prom, 2), "unidades")


def principal():
	opcion = -1
	fd = "pantalones.dat"
	v = []

	while opcion != 0:
		opcion = menu()
		if opcion == 1:
			v = cargar_vector()

		elif v and len(v) > 0:
			if opcion == 2:
				mostrar(v)

			elif opcion == 3:
				mat = generar_matriz(v)
				u = int(input("Ingrese la cantidad de unidades minimas a mostrar: "))
				mostrar_matriz(mat, u)

			elif opcion == 4:
				tela = int(input("Ingrese el tipo de tela: "))
				generar_archivo(fd, v, tela)

			elif opcion == 5:
				mostrar_archivo(fd)
		else:
			print('Primero debe ejecutar la opcion 1')


if __name__ == '__main__':
	principal()
