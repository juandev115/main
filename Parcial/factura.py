# factura.py
from datetime import datetime
from guardar_factura import guardar_factura_txt

class Factura:
    def __init__(self, cliente, carrito):
        self.cliente = cliente
        self.carrito = carrito
        self.fecha = datetime.now().strftime("%Y-%m-%d %H-%M")
        self.subtotal = sum(p["precio"] * p["cantidad"] for p in carrito.values())
        self.iva = self.subtotal * 0.19
        self.total = self.subtotal + self.iva
        self.nit = "900123456-7"
        self.empresa = "ElectroMundo S.A."

    def mostrar_factura(self):
        print("\n===================================")
        print(f"        {self.empresa}")
        print(f"          NIT: {self.nit}")
        print("       FACTURA ELECTRÓNICA")
        print("===================================")
        print(f"Cliente: {self.cliente}")
        print(f"Fecha: {self.fecha}")
        print("\nDetalle de productos:")
        for codigo, datos in self.carrito.items():
            subtotal = datos["precio"] * datos["cantidad"]
            print(f" {codigo} - {datos['nombre']:<25} x{datos['cantidad']:<3} ${subtotal:,}")
        print("-----------------------------------")
        print(f"SUBTOTAL: ${self.subtotal:,.0f}")
        print(f"IVA (19%): ${self.iva:,.0f}")
        print(f"TOTAL: ${self.total:,.0f}")
        print("===================================")
        print(" ¡Gracias por su compra en ElectroMundo S.A.! ")

    def guardar_factura(self):
        nombre_archivo = f"Factura_{self.cliente.replace(' ', '_')}_{self.fecha}"
        guardar_factura_txt(
            nombre_archivo,
            self.empresa,
            self.nit,
            self.cliente,
            self.fecha,
            self.carrito,
            self.subtotal,
            self.iva,
            self.total
        )
