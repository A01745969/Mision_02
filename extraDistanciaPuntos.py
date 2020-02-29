# Autor: Paulina Mendoza Iglesias, A01745969
# Pide al usuario las coordenadas de dos puntos para imprimir la distancia

import math

x1 = int (input("Teclea la coordenada x1: "))
y1 = int (input("Teclea la coordenada y1: "))
x2 = int (input("Teclea la coordenada x2: "))
y2 = int (input("Teclea la coordenada y2: "))

x = (x1 - x2) ** 2
y = (y1 - y2) ** 2
d = math.sqrt (x + y) 

print ("Distancia: %.3f" % (d))