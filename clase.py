# Autor: Paulina Mendoza Iglesias, A01745969
# Descripcion: Programa que calcula el porcentaje de mujeres y hombres de una clase

# Escribe tu programa después de esta línea.


hombres = int(input("Teclea el número de hombres de una clase: "))
mujeres = int(input("Teclea el número de mujeres de una clase: "))

total = hombres + mujeres
porcentajeH = (hombres*100) / total
porcentajeM = (mujeres*100) / total

print("Total de inscritos: ", total)
print("Porcentaje de mujeres: %.1f" % (porcentajeM))
print("Porcentaje de hombres: %.1f" % (porcentajeH))
