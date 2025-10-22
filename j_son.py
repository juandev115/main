#Crear un diccionario
persona = {}
# Diccionario frutas
Programacion_1 = {
    "docente": "David Garcia",
    "estudiantes":[
        {
            "nombre": "Juan Gonzalez",
            "cedula": 1015434287,
            "correo": "juango@unisangil.edu.co",
            "edad": 20
        },
        {
            "nombre": "Camila Perez",
            "cedula": 1015434289,
            "correo": "camila@gmail.com",
            "edad": 19
        }
    ],
    "temas": [
        "Introducción a la programación",
        "Variables",
        "Estructuras de control",
        "Programación orientada a objetos"
    ],
    "creditos": 3,
    "cortes":[
        {
            "nombre": "Corte 1",
            "porcentaje": 50
        },
        {
            "nombre": "Corte 2",
            "porcentaje": 50
        }
    ]
}
#Imprimir diccionario

print(Programacion_1["estudiantes"][0]["nombre"])  
print(Programacion_1["temas"][2])
for temas in Programacion_1["temas"]:
    print(temas)
print(Programacion_1["cortes"][1]["nombre"])
print(Programacion_1["estudiantes"][0]["correo"])
print(Programacion_1["estudiantes"][1])
Programacion_1["estudiantes"][1]["edad"] = 18
Programacion_1["estudiantes"][1]["cedula"] = 1053332094
Programacion_1["estudiantes"][1]["correo"] = "juanhernandez@unisangil.edu.co"
Programacion_1["estudiantes"][1]["nombre"] = "Juan Hernandez"
print(Programacion_1["estudiantes"][1])
Programacion_1["uwu"] = True
print(Programacion_1)
del Programacion_1["uwu"]
print(Programacion_1)
for clave, valor in Programacion_1.items():
    print(f"{clave}: {valor}")
for clave in Programacion_1.keys():
    print(clave)
for clave in Programacion_1.get("temas"):
    print(clave)
Programacion_1.clear()
print(Programacion_1)