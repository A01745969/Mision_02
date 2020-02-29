# : Paulina Mendoza Iglesias, A01745969
# Descripcion: Programa que calcula el costo total de una comida en un restaurante 

# Escribe tu programa después de esta línea.

PrecioComida = int(input("Teclea el precio de la comida: "))

propina = PrecioComida * .13 
IVA = PrecioComida * .16
PrecioTotal = PrecioComida + propina + IVA

print("Propina: %.2f $ " % (propina))
print("IVA: %.2f $ " % (IVA))
print("Total a pagar: %.2f $ " % (PrecioTotal))