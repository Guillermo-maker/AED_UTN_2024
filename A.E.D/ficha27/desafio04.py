import csv
import math

# Definimos la clase Point con un método para calcular la distancia
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# Leemos el archivo y creamos la lista de puntos
points = []
with open('puntos.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        x, y = int(row[0]), int(row[1])
        points.append(Point(x, y))

# Inicializamos las variables de distancia mínima y máxima
dmin = points[0].distance(points[1])
dmax = 0

# Algoritmo de fuerza bruta para encontrar las distancias mínima y máxima
n = len(points)
for i in range(n - 1):
    for j in range(i + 1, n):
        d = points[i].distance(points[j])
        if d < dmin:
            dmin = d
        if d > dmax:
            dmax = d

# Redondeamos los resultados
dmin = round(dmin)
dmax = round(dmax)

# Mostramos los resultados
print("Distancia mínima:", dmin)
print("Distancia máxima:", dmax)
