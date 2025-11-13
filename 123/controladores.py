usuario = "juanv117" 
contraseña = "12345" 
input_usuario = input("Ingrese su usuario: ")
input_contraseña = input("Ingrese su contraseña: ")
if input_usuario == usuario and input_contraseña == contraseña:
    print("Acceso concedido")
else:
    print("Acceso denegado")