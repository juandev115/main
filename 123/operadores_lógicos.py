#operadores lógicos
a = 5
b = 10
print (a < 15 and b > 5) #true
print (a < 10 and 10 < 5 ) #false
print (a < 10 and 10 < 5 )#false
print (a > 10 and b <5) #false

usuario = "Juandiddy"
contraseña = "1234"
#solicitar nobre usuario y contraseña
nombre_usuario = input("Ingrese su nombre de usuario: ")
contraseña_usuario = input("Ingrese su contraseña: ")
if usuario == nombre_usuario and contraseña == contraseña_usuario:
    print ("Acceso concedido")
else:
    print ("Acceso denegado")
#or
print (a < 5 or b > 5) #true
print (a < 10 or 10 < 5 ) #true
print (a > 10 or b <5) #false
print (a > 10 or b >5) #true
#not
print (not(a<10)) #false
print (not(a>10)) #true