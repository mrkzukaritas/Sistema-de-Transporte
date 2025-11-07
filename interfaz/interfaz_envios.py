import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from envios.envio_manager import EnvioManager

class InterfazEnvios:
    def __init__(self, root):
        self.manager = EnvioManager()
        self.root = root
        self.root.title("Gestión de Envíos (Factory Method)")
        self.root.geometry("700x400")

        # Formulario
        tk.Label(root, text="Tipo (terrestre/maritima/aerea):").pack()
        self.tipo = tk.Entry(root)
        self.tipo.pack()

        tk.Label(root, text="Destino:").pack()
        self.destino = tk.Entry(root)
        self.destino.pack()

        tk.Button(root, text="Crear Envío", command=self.crear_envio).pack(pady=5)
        tk.Button(root, text="Actualizar Estado", command=self.actualizar_envio).pack(pady=5)
        tk.Button(root, text="Eliminar Envío", command=self.eliminar_envio).pack(pady=5)

        # Tabla
        self.tabla = ttk.Treeview(root, columns=("ID", "Tipo", "Destino", "Estado", "Costo", "Tiempo"), show="headings")
        for col in self.tabla["columns"]:
            self.tabla.heading(col, text=col)
        self.tabla.pack(expand=True, fill="both", pady=10)

        tk.Button(root, text="Refrescar Lista", command=self.refrescar_tabla).pack()

    def crear_envio(self):
        tipo = self.tipo.get().lower()
        destino = self.destino.get()
        if not tipo or not destino:
            messagebox.showwarning("Error", "Debe llenar todos los campos.")
            return
        self.manager.crear_envio(tipo, destino)
        self.refrescar_tabla()

    def refrescar_tabla(self):
        for row in self.tabla.get_children():
            self.tabla.delete(row)
        for e in self.manager.envios:
            self.tabla.insert("", "end", values=(e.id_envio, e.tipo, e.destino, e.estado, e.costo, e.tiempo))

    def actualizar_envio(self):
        try:
            id_envio = int(self.tabla.item(self.tabla.selection())["values"][0])
        except:
            messagebox.showwarning("Error", "Seleccione un envío para actualizar.")
            return
        nuevo_estado = simpledialog.askstring("Actualizar", "Nuevo estado (Pendiente/En tránsito/Entregado):")
        if nuevo_estado:
            self.manager.actualizar_envio(id_envio, nuevo_estado)
            self.refrescar_tabla()

    def eliminar_envio(self):
        try:
            id_envio = int(self.tabla.item(self.tabla.selection())["values"][0])
        except:
            messagebox.showwarning("Error", "Seleccione un envío para eliminar.")
            return
        self.manager.eliminar_envio(id_envio)
        self.refrescar_tabla()


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazEnvios(root)
    root.mainloop()
