import sqlite3
import os
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDIconButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField
from kivymd.uix.list import MDList, TwoLineAvatarIconListItem, IconLeftWidget
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp

DB_NAME = "finanzas_v2.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS billeteras (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT UNIQUE,
                        saldo REAL DEFAULT 0.0)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS movimientos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        billetera_id INTEGER,
                        tipo TEXT,
                        monto REAL,
                        descripcion TEXT,
                        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        FOREIGN KEY (billetera_id) REFERENCES billeteras(id))''')
    cursor.execute("SELECT COUNT(*) FROM billeteras")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO billeteras (nombre, saldo) VALUES ('Principal', 0.0)")
    conn.commit()
    conn.close()

class FinanzasScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id_billetera_actual = None
        self.dialog = None

    def on_enter(self):
        init_db()
        self.cargar_billeteras()

    def cargar_billeteras(self):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, saldo FROM billeteras")
        cuentas = cursor.fetchall()
        conn.close()

        lista_container = self.ids.lista_billeteras
        lista_container.clear_widgets()

        for id_b, nombre, saldo in cuentas:
            item = TwoLineAvatarIconListItem(
                text=nombre.upper(),
                secondary_text=f"$ {saldo:,.2f}",
                on_release=lambda x, b_id=id_b, b_nom=nombre: self.seleccionar_billetera(b_id, b_nom)
            )
            icon = IconLeftWidget(icon="wallet")
            item.add_widget(icon)
            lista_container.add_widget(item)

        if cuentas and self.id_billetera_actual is None:
            self.seleccionar_billetera(cuentas[0][0], cuentas[0][1])

    def seleccionar_billetera(self, b_id, b_nombre):
        self.id_billetera_actual = b_id
        self.ids.lbl_cuenta_actual.text = f"Cuenta: {b_nombre}"
        self.actualizar_saldo_ui()
        self.cargar_historial()

    def actualizar_saldo_ui(self):
        if not self.id_billetera_actual: return
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT saldo FROM billeteras WHERE id = ?", (self.id_billetera_actual,))
        res = cursor.fetchone()
        if res:
            self.ids.lbl_saldo.text = f"$ {res[0]:,.2f}"
        conn.close()

    def transaccion(self, tipo):
        if not self.id_billetera_actual: return
        try:
            monto_str = self.ids.txt_monto.text.replace(",", ".")
            if not monto_str: return
            monto = float(monto_str)
            desc = self.ids.txt_desc.text or "Sin descripción"

            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO movimientos (billetera_id, tipo, monto, descripcion) VALUES (?, ?, ?, ?)",
                          (self.id_billetera_actual, tipo, monto, desc))
            ajuste = monto if tipo == "Ingreso" else -monto
            cursor.execute("UPDATE billeteras SET saldo = saldo + ? WHERE id = ?", (ajuste, self.id_billetera_actual))
            conn.commit()
            conn.close()

            self.ids.txt_monto.text = ""
            self.ids.txt_desc.text = ""

            self.actualizar_saldo_ui()
            self.cargar_historial()
            self.cargar_billeteras()
        except ValueError:
            pass

    def cargar_historial(self):
        lista_historial = self.ids.lista_historial
        lista_historial.clear_widgets()

        if not self.id_billetera_actual: return

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT tipo, monto, descripcion, fecha FROM movimientos WHERE billetera_id = ? ORDER BY fecha DESC", (self.id_billetera_actual,))
        
        for row in cursor.fetchall():
            tipo, monto, desc, fecha = row
            es_ingreso = (tipo == "Ingreso")
            icono_str = "arrow-up-bold-circle" if es_ingreso else "arrow-down-bold-circle"
            
            item = TwoLineAvatarIconListItem(
                text=f"{'▲' if es_ingreso else '▼'} {tipo.upper()}: ${monto:,.2f} | {desc}",
                secondary_text=str(fecha)
            )
            icon = IconLeftWidget(icon=icono_str)
            item.add_widget(icon)
            lista_historial.add_widget(item)
            
        conn.close()

    def dialogo_nueva_billetera(self):
        self.input_nombre = MDTextField(hint_text="Nombre de la cuenta")
        self.dialog = MDDialog(
            title="Nueva Billetera",
            type="custom",
            content_cls=self.input_nombre,
            buttons=[
                MDFlatButton(text="CANCELAR", on_release=lambda x: self.dialog.dismiss()),
                MDRaisedButton(text="GUARDAR", on_release=lambda x: self.guardar_nueva_billetera())
            ],
        )
        self.dialog.open()

    def guardar_nueva_billetera(self):
        nombre = self.input_nombre.text.strip()
        if nombre:
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            try:
                cursor.execute("INSERT INTO billeteras (nombre, saldo) VALUES (?, 0.0)", (nombre,))
                conn.commit()
            except sqlite3.IntegrityError:
                pass
            conn.close()
            self.cargar_billeteras()
        self.dialog.dismiss()

    def eliminar_billetera(self):
        if not self.id_billetera_actual: return
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM billeteras")
        if cursor.fetchone()[0] > 1:
            cursor.execute("DELETE FROM movimientos WHERE billetera_id = ?", (self.id_billetera_actual,))
            cursor.execute("DELETE FROM billeteras WHERE id = ?", (self.id_billetera_actual,))
            conn.commit()
            self.id_billetera_actual = None
        conn.close()
        self.cargar_billeteras()
        self.cargar_historial()

    def abrir_resumen(self):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, saldo FROM billeteras")
        cuentas = cursor.fetchall()
        conn.close()

        box = MDBoxLayout(orientation="vertical", spacing=dp(10), size_hint_y=None)
        box.bind(minimum_height=box.setter('height'))

        self.checks_resumen = {}
        for id_b, nombre, saldo in cuentas:
            row = MDBoxLayout(orientation="horizontal", size_hint_y=None, height=dp(40))
            cb = MDCheckbox(active=True, size_hint_x=None, width=dp(40))
            cb.bind(active=self.recalcular_resumen)
            lbl = MDTextField(text=f"{nombre} (${saldo:,.2f})", readonly=True)
            row.add_widget(cb)
            row.add_widget(lbl)
            box.add_widget(row)
            self.checks_resumen[id_b] = (cb, saldo)

        scroll = ScrollView(size_hint=(1, None), height=dp(200))
        scroll.add_widget(box)

        self.lbl_total_resumen = MDTextField(text="Total: $ 0.00", readonly=True)

        layout = MDBoxLayout(orientation="vertical", spacing=dp(10), size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        layout.add_widget(scroll)
        layout.add_widget(self.lbl_total_resumen)

        self.recalcular_resumen()

        self.dialog_resumen = MDDialog(
            title="Resumen Consolidado",
            type="custom",
            content_cls=layout,
            buttons=[MDFlatButton(text="CERRAR", on_release=lambda x: self.dialog_resumen.dismiss())]
        )
        self.dialog_resumen.open()

    def recalcular_resumen(self, *args):
        total = sum(saldo for cb, saldo in self.checks_resumen.values() if cb.active)
        self.lbl_total_resumen.text = f"Total: $ {total:,.2f}"

class AppFinanzas(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        return FinanzasScreen()

    def cambiar_tema(self):
        if self.theme_cls.theme_style == "Light":
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

if __name__ == "__main__":
    AppFinanzas().run()