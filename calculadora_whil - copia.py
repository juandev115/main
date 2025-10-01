# Sistema de Biblioteca Virtual

usuario_correcto = "Pepita24"  # ID válido
intentos = 0
autenticado = False


while intentos < 3 and autenticado == False:
    usuario = input("Ingrese su ID de usuario: ")
    if usuario == usuario_correcto:
        autenticado = True
        print("Autenticación exitosa.\n")
    else:
        intentos += 1
        print("ID incorrecto. Intento", intentos, "de 3\n")

if autenticado == False:
    print("Acceso bloqueado por exceder los intentos permitidos.")
else:
    # --- MENÚ PRINCIPAL ---
    opcion = ""
    while opcion != "d":
        print("---- Menú Biblioteca ----")
        print("a) Consultar libros disponibles")
        print("b) Realizar un préstamo")
        print("c) Devolver un libro")
        print("d) Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "a":
            print("Libros disponibles: \n- Butano\n- 207 Huesos\n- Siesta y rencor\n")
        elif opcion == "b":
            print("Ha realizado un préstamo. Costo: $10.000\n")
        elif opcion == "c":
            dias = int(input("Ingrese cantidad de días de retraso: "))
            if dias > 0:
                multa = dias * 200
                print("Debe pagar una multa de $", multa, "\n")
            else:
                print("Libro devuelto sin retrasos. No hay multa.\n")
        elif opcion == "d":
            print("Saliendo del sistema...")
        else:
            print("Opción no válida\n")
