import math
import math
#Solicitar datos del sistema 
base = float(input("Ingrese la base del terreno en metros: "))
altura = float(input("Ingrese la altura del terreno en metros: "))
Area_triangulo = (base * altura) / 2
Area_cuadrado = base * base 
Area_Total = (Area_triangulo + Area_cuadrado) 
precio_del_terreno = 4400000
Preco_total = Area_Total*precio_del_terreno
print("El area total del terreno es: ", Area_Total, "mts2")
print ("El precio total del terreno es: ", Preco_total, "pesos")
#error por escribir un string
