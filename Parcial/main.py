# importaciones de programacion modular 
from catalogo import mostrar_catalogo, agregar_producto
from ventas import realizar_venta   
from factura import Factura

def menu():
    print("""
===================================
     SISTEMA DE FACTURACIÓN
        ELECTROMUNDO S.A.
===================================
1. Mostrar catálogo
2. Agregar nuevo producto
3. Realizar venta
4. Salir
""")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_catalogo()# catalogfo de catalogo.py
        elif opcion == "2":
            agregar_producto()# agregar producto de catalogo.py
        elif opcion == "3":
            mostrar_catalogo()# mostrar catalogo antes de vender
            cliente = input("\nIngrese el nombre del cliente: ") #el nombre se guarda en el txt
            carrito = realizar_venta()
            if not carrito:
                print("✖️ No se registraron productos.")
                continue
            factura = Factura(cliente, carrito)
            factura.mostrar_factura()#factura de factura.py
            factura.guardar_factura()# guardar factura de factura.py
        elif opcion == "4":
            print(" Saliendo del sistema...")#fin del programa
            break
        else:
            print("👋 Opción no válida, intente nuevamente.")#reset 

if __name__ == "__main__": 
    main() 
