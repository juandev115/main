def mensaje():
        """
        basic coding message
        """
        print ("hola mundo")
        
mensaje()

#funcion con retorno 

def suma():
        rta = 5+3
        return rta
print(suma()) 

def resta(a, b):
        rta= a-b
        print ("resta",rta)

resta(10,4)
# función simple con valores de retorno 
def solicitud_datos():
    """
    función de solicitud de información
    """
    num1 = int(input("Ingrese su información x: "))
    num2 = int(input("Ingrese su otra info x: "))
    return num1, num2

def multiplicacion(num1, num2):
    """
    función para multiplicación de 2 números
    """
    rta = num1 * num2
    return rta

# llamada a la función
num1, num2 = solicitud_datos()
print("Multiplicación:", multiplicacion(num1, num2))
