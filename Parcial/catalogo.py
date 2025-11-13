# catalogo.py

catalogo = {
    "Línea Blanca": {
        "LB001": {"nombre": "Refrigerador", "precio": 3200000},
        "LB002": {"nombre": "Lavadora", "precio": 2800000},
        "LB003": {"nombre": "Secadora", "precio": 2600000}
    },
    "Pequeños Electrodomésticos": {
        "PE001": {"nombre": "Licuadora", "precio": 450000},
        "PE002": {"nombre": "Cafetera", "precio": 380000},
        "PE003": {"nombre": "Tostadora", "precio": 250000}
    },
    "Entretenimiento": {
        "EN001": {"nombre": "Televisor", "precio": 4200000},
        "EN002": {"nombre": "Sistema de sonido", "precio": 1900000}
    },
    "Aires Acondicionados": {
        "AA001": {"nombre": "Aire 9000 BTU", "precio": 2700000},
        "AA002": {"nombre": "Aire 12000 BTU", "precio": 3100000}
    }
}

def mostrar_catalogo():
    print("\n=== Catálogo de ElectroMundo S.A. ===")
    for categoria, productos in catalogo.items():
        print(f"\n{categoria}:")
        for codigo, datos in productos.items():
            print(f"  {codigo} - {datos['nombre']} - ${datos['precio']:,}")

def buscar_producto_por_codigo(codigo):
    for categoria, productos in catalogo.items():
        if codigo in productos:
            producto = productos[codigo]
            producto["categoria"] = categoria
            return producto
    return None

def agregar_producto():
    categoria = input("\nIngrese la categoría del nuevo producto: ").title()
    codigo = input("Ingrese el código único del producto: ").upper()
    nombre = input("Ingrese el nombre del producto: ").title()
    precio = int(input("Ingrese el precio unitario: "))

    if categoria not in catalogo:
        catalogo[categoria] = {}
    catalogo[categoria][codigo] = {"nombre": nombre, "precio": precio}

    print(f"\n👍 Producto '{nombre}' agregado correctamente en {categoria}.")
