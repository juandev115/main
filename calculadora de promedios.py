# Calculadora de promedios
import math
notas1 = []
cantidad_notas = int(input("ingrese la cantidad de notas a promediar del primer corte(debe ser un numero entero): "))
if cantidad_notas<= 0:
    print("La cantidad de notas debe ser un número positivo.")
    exit()

for i in range(cantidad_notas):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas1.append(nota)
promedio = sum(notas1) / cantidad_notas
print(f"El promedio de las notas del primer corte es : {promedio}")

notas2 = []
cantidad_notas2 = int(input("ingrese la cantidad de notas a promediar del segundo corte(debe ser un numero entero): "))
if cantidad_notas2<= 0:
    print("La cantidad de notas debe ser un número positivo.")
    exit()
for i in range(cantidad_notas2):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas2.append(nota)
promedio2 = sum(notas2) / cantidad_notas2
print(f"El promedio de las notas del segundo corte es : {promedio2}")
print(f"El promedio total es: {(promedio + promedio2) / 2}")
if (promedio + promedio2) / 2 >= 3.0:
    print("has aprobado el curso")
else:
    print("perdió")




    