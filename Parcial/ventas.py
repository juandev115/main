# ventas.py
from catalogo import buscar_producto_por_codigo, agregar_producto

def realizar_venta():
    carrito = {}
    print("\nIngrese los códigos de los productos a vender (escriba 'fin' para terminar)")
    while True:
        codigo = input("Código del producto: ").upper()
        if codigo.lower() == "fin": 
            break
        producto = buscar_producto_por_codigo(codigo)
        if producto is None:
            print("✖️ Código no encontrado. ¿Desea agregar este producto? (s/n)")
            if input().lower() == "s":
                agregar_producto()
            else:
                continue
        else:
            cantidad = int(input(f"Cantidad de {producto['nombre']}: "))
            carrito[codigo] = {
                "nombre": producto["nombre"],
                "precio": producto["precio"],
                "cantidad": cantidad
            }
    return carrito
