# Paulina Mendoza Iglesias
# Calcula la cantidad de ingredientes que se necesitan
# para elaborar galletas

x = int(input("Teclea número de galletas: "))

azucar = x*.031
mantequilla = x*.020
harina = x*.057

print("Se necesitan %.2f tazas de azúcar" % (azucar))
print("Se necesitan %.2f tazas de mantequilla" % (mantequilla))
print("Se necesitan %.2f tazas de harina" % (harina))
