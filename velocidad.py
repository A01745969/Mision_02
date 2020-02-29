# Autor: Paulina Mendoza Iglesias, A01745969
# Descripcion: Programa que pregunta la velocidad que viaja un auto para imprimir distancia y tiempo 

# Escribe tu programa después de esta línea.

velocidad = int(input("Teclea la velocidad del auto: "))

distancia1 = velocidad * 6
distancia2 = velocidad * 3.5
tiempo = 485 / velocidad

print("Distancia recorrida en 6 hrs: %.1f " % (distancia1))
print("Distancia recorrida en 3.5 hrs: %.1f " % (distancia2))
print("Tiempo para recorrer 485 km: %.1f " % (tiempo))
