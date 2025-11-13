# guardar_factura.py
import os

def guardar_factura_txt(nombre_archivo, empresa, nit, cliente, fecha, carrito, subtotal, iva, total):
    # Creamos una carpeta para guardar las facturas si no existe
    carpeta = "Facturas"
    os.makedirs(carpeta, exist_ok=True)

    # Ruta completa del archivo
    ruta = os.path.join(carpeta, f"{nombre_archivo}.txt")

    # Crear y escribir la factura
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("===================================\n")
        f.write(f"        {empresa}\n")
        f.write(f"          NIT: {nit}\n")
        f.write("       FACTURA ELECTRÓNICA\n")
        f.write("===================================\n")
        f.write(f"Cliente: {cliente}\n")
        f.write(f"Fecha: {fecha}\n\n")
        f.write("Detalle de productos:\n")

        for codigo, datos in carrito.items():
            subtotal_producto = datos["precio"] * datos["cantidad"]
            f.write(f"{codigo} - {datos['nombre']} x{datos['cantidad']} = ${subtotal_producto:,}\n")

        f.write("\n-----------------------------------\n")
        f.write(f"Subtotal: ${subtotal:,.0f}\n")
        f.write(f"IVA (19%): ${iva:,.0f}\n")
        f.write(f"TOTAL: ${total:,.0f}\n")
        f.write("===================================\n")
        f.write("¡Gracias por su compra en ElectroMundo S.A.! 💡\n")

    print(f"\n✅ Factura guardada en '{ruta}' correctamente.")