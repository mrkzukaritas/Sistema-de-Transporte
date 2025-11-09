import tkinter as tk
from tkinter import ttk, messagebox
from envios.envio_manager import EnvioManager


class InterfazEnvios:
    def __init__(self, root):
        self.manager = EnvioManager()
        self.root = root
        self.root.title("Gestión de Envíos (Factory Method)")
        self.root.geometry("750x450")
        self.root.configure(bg="#f4f4f4")

        # Variables
        self.tipo_seleccionado = tk.StringVar()
        self.destino = tk.StringVar()

        # ======== FRAME SUPERIOR ==========
        frame_form = tk.Frame(root, bg="#f4f4f4")
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Selecciona el tipo de envío:", bg="#f4f4f4", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=3, pady=5)

        # Botones de tipo
        tk.Button(frame_form, text="Terrestre", width=12, command=lambda: self.seleccionar_tipo("terrestre")).grid(row=1, column=0, padx=5)
        tk.Button(frame_form, text="Marítima", width=12, command=lambda: self.seleccionar_tipo("maritima")).grid(row=1, column=1, padx=5)
        tk.Button(frame_form, text="Aérea", width=12, command=lambda: self.seleccionar_tipo("aerea")).grid(row=1, column=2, padx=5)

        tk.Label(frame_form, text="Destino:", bg="#f4f4f4").grid(row=2, column=0, columnspan=3, pady=(10, 2))
        tk.Entry(frame_form, textvariable=self.destino, width=40).grid(row=3, column=0, columnspan=3)

        tk.Button(frame_form, text="Crear Envío", bg="#4CAF50", fg="white", width=20, command=self.crear_envio).grid(row=4, column=0, columnspan=3, pady=10)

        # ======== BOTONES CRUD ==========
        frame_botones = tk.Frame(root, bg="#f4f4f4")
        frame_botones.pack()

        tk.Button(frame_botones, text="Actualizar Estado", bg="#2196F3", fg="white", width=18, command=self.mostrar_botones_estado).grid(row=0, column=0, padx=10)
        tk.Button(frame_botones, text="Eliminar Envío", bg="#E53935", fg="white", width=18, command=self.eliminar_envio).grid(row=0, column=1, padx=10)
        tk.Button(frame_botones, text="Refrescar Lista", bg="#9E9E9E", fg="white", width=18, command=self.refrescar_tabla).grid(row=0, column=2, padx=10)

        # ======== TABLA ==========
        columnas = ("ID", "Tipo", "Destino", "Estado", "Costo", "Tiempo")
        self.tabla = ttk.Treeview(root, columns=columnas, show="headings")
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=100, anchor="center")
        self.tabla.pack(expand=True, fill="both", pady=10)

    # ===================== FUNCIONES =====================

    def seleccionar_tipo(self, tipo):
        """Guarda el tipo seleccionado y muestra un mensaje."""
        self.tipo_seleccionado.set(tipo)
        #messagebox.showinfo("Tipo seleccionado", f"Has seleccionado envío {tipo.capitalize()}")

    def crear_envio(self):
        """Crea un envío y limpia los campos."""
        tipo = self.tipo_seleccionado.get()
        destino = self.destino.get().strip()

        if not tipo or not destino:
            messagebox.showwarning("Error", "Debe seleccionar tipo y destino.")
            return

        self.manager.crear_envio(tipo, destino)
        #messagebox.showinfo("Éxito", f"Envío {tipo.capitalize()} creado correctamente.")
        self.refrescar_tabla()

        # Limpiar campos
        self.tipo_seleccionado.set("")
        self.destino.set("")

    def refrescar_tabla(self):
        """Actualiza la tabla con los envíos actuales."""
        for row in self.tabla.get_children():
            self.tabla.delete(row)
        for e in self.manager.envios:
            self.tabla.insert("", "end", values=(e.id_envio, e.tipo, e.destino, e.estado, e.costo, e.tiempo))

    def mostrar_botones_estado(self):
        """Muestra botones de actualización de estado dinámicos."""
        try:
            envio_seleccionado = self.tabla.item(self.tabla.selection())["values"]
            id_envio = int(envio_seleccionado[0])
            estado_actual = envio_seleccionado[3]
        except:
            messagebox.showwarning("Error", "Seleccione un envío para actualizar.")
            return

        ventana_estado = tk.Toplevel(self.root)
        ventana_estado.title("Actualizar Estado")
        ventana_estado.geometry("300x200")
        ventana_estado.config(bg="#f4f4f4")

        tk.Label(ventana_estado, text=f"Estado actual: {estado_actual}", bg="#f4f4f4", font=("Arial", 10, "bold")).pack(pady=10)
        tk.Label(ventana_estado, text="Seleccione nuevo estado:", bg="#f4f4f4").pack(pady=5)

        estados = ["Pendiente", "En tránsito", "Entregado"]
        for estado in estados:
            if estado != estado_actual:  # no mostrar el mismo estado actual
                tk.Button(
                    ventana_estado,
                    text=estado,
                    width=15,
                    command=lambda e=estado: self.actualizar_envio(id_envio, e, ventana_estado)
                ).pack(pady=5)

    def actualizar_envio(self, id_envio, nuevo_estado, ventana):
        """Actualiza el estado del envío y refresca la tabla."""
        self.manager.actualizar_envio(id_envio, nuevo_estado)
        self.refrescar_tabla()
        ventana.destroy()
        #messagebox.showinfo("Actualizado", f"Estado cambiado a {nuevo_estado}.")

    def eliminar_envio(self):
        """Elimina el envío seleccionado."""
        try:
            id_envio = int(self.tabla.item(self.tabla.selection())["values"][0])
        except:
            messagebox.showwarning("Error", "Seleccione un envío para eliminar.")
            return
        self.manager.eliminar_envio(id_envio)
        self.refrescar_tabla()
        #messagebox.showinfo("Eliminado", "Envío eliminado correctamente.")


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazEnvios(root)
    root.mainloop()
