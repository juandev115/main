import math

while True:

    print("calculadora")
    print("1. suma")
    print("2. resta")
    print("3. multiplicacion")
    print("4. division")
    print("5. potencia ")
    print("6. raíz cuadrada")
    print("7. raiz cúbica")
    print("8. seno en radianes")
    print("9. seno")    
    print("10. salir")
    
    opcion = int(input("elija una opcion entre 1-10: "))
    if opcion == 1:
        num1 = int(input("ingrese el numero 1: "))
        num2 = int(input("ingrese el numero 2 : "))
        resultado = num1 + num2
        print(f"el resultado de la suma es: {resultado}")
    elif opcion == 2:
        num1 = int(input("ingrese el numero 1: "))
        num2 = int(input("ingrese el numero 2 : "))
        resultado = num1 - num2
        print(f"el resultado de la resta es: {resultado}")
    elif opcion == 3:
        num1 = int(input("ingrese el numero 1: "))
        num2 = int(input("ingrese el numero 2 : "))
        resultado = num1 * num2
        print(f"el resultado de multiplicacion: {resultado}")
    elif opcion == 4:
        num1 = int(input("ingrese el numero 1: "))
        num2 = int(input("ingrese el numero 2 : "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"el resultado de division es: {resultado}")
        else:
            print("error no se puede dividir entre 0")
    elif opcion == 5:
        num1 = int(input("ingrese el numero 1: "))
        num2 = int(input("ingrese el numero 2 : "))
        resultado = num1 ** num2
        print(f"el resultado de potencia es: {resultado}")
    elif opcion == 6:
        num1 = int(input("ingrese el numero 1: "))
        if num1 >= 0:
            resultado = math.sqrt(num1)
            print(f"el resultado de la raiz cuadrada es: {resultado}")
        else:
            print("error no se puede sacar la raiz cuadrada de un numero negativo")
    elif opcion == 7:
        num1 = int(input("ingrese el numero 1: "))
        if num1 >= 0:
            resultado = 3* math.sqrt(num1)
            print(f"el resultado de la raiz cubica es: {resultado}")
        else:
            print("error no se puede sacar la raiz cubica de un numero negativo")
    elif opcion == 8:
        num1 = int(input("ingrese el numero : "))
        resultado = math.sin(num1)
        print(f"el resultado del seno es: {resultado}") 
    elif opcion == 9:
        num1 = int(input("ingrese el numero : "))
        resultado = math.radians(num1)
        resultado = math.sin(resultado)
        print(f"el resultado del seno en radianes es: {resultado}")       
        
    elif opcion == 10:
        print("gracias por usar la calculadora")
        break
    