import json

def cargar_datos():
        archivo = open("mascotas.json", "r")
        datos = json.load(archivo)
        archivo.close()
        return datos


def guardar_datos(lista_mascotas):
    
    archivo = open("mascotas.json", "w")
    json.dump(lista_mascotas, archivo)
    archivo.close()

def agregar_mascota(lista_mascotas):

    nombre = input("Ingrese el nombre: ")
    especie = input("Ingrese la especie: ")
    edad = int(input("Ingrese la edad: "))
    tamano = input("Ingrese el tamaño: ")
    cuidados = []
    print("Ingrese los cuidados (escriba 'fin' para terminar):")
    while True:
        cuidado = input("Cuidado: ")
        if cuidado.lower() == "fin":
            break
        cuidados.append(cuidado)
    nueva_mascota = {"nombre": nombre,"especie": especie,"edad": edad,"tamano": tamano,"cuidados": cuidados
    }

    lista_mascotas.append(nueva_mascota)
    guardar_datos(lista_mascotas)

def eliminar_mascota(lista_mascotas):
   
    nombre_buscar = input("Ingrese el nombre de la mascota a eliminar: ")
    encontrado = False
    
    for i in range(len(lista_mascotas)):
        if lista_mascotas[i]["nombre"].lower() == nombre_buscar.lower():
            lista_mascotas.pop(i)
            
            
    if encontrado:
        guardar_datos(lista_mascotas)
        print("Mascota eliminada correctamente.")
    else:
        print("No se encontró ninguna mascota con ese nombre.")

def modificar_mascota(lista_mascotas):
    nombre_buscar = input("Ingrese el nombre de la mascota a modificar: ")
    encontrado = False
    
    for mascota in lista_mascotas:
        if mascota["nombre"].lower() == nombre_buscar.lower():
            mascota["edad"] = int(input(f"Nueva edad [{mascota['edad']}]: "))
            mascota["tamano"] = input(f"Nuevo tamaño [{mascota['tamano']}]: ")
            encontrado = True
            break
    if encontrado:
        guardar_datos(lista_mascotas)
        print("mascota modificada con éxito")
    else:
        print("no se encontro ninguna mascota con ese nombre.")

def ver_lista(lista_mascotas):
    print("\nLISTA DE MASCOTAS")
    print(lista_mascotas)

def menu():
    mascotas = cargar_datos()
    seleccion = 0
    
    while seleccion != 5:

        print("   SISTEMA GESTIÓN DE MASCOTAS")
        print("1. Agregar mascota")
        print("2. Eliminar mascota")
        print("3. Modificar mascota")
        print("4. Ver lista")
        print("5. Salir")
        
        seleccion = int(input("Ingrese una selección: "))
        
        if seleccion == 1:
            agregar_mascota(mascotas)
        elif seleccion == 2:
            eliminar_mascota(mascotas)
        elif seleccion == 3:
            modificar_mascota(mascotas)
        elif seleccion == 4:
            ver_lista(mascotas)
        elif seleccion == 5:
            print("Saliendo del programa...")
        else:
            print("Opción no válida, intente de nuevo.")


menu()