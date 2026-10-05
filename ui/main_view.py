import os
import tkinter as tk
from tkinter import messagebox, ttk

from PIL import Image, ImageTk

from servicios.restaurante_servicio import RestauranteServicio


class MainView:
    def __init__(self, root, usuario_actual):
        self.root = root
        self.usuario_actual = usuario_actual
        self.servicio = RestauranteServicio()

        self.root.title(
            f"Restaurante App - Módulo de Gestión | Usuario: {self.usuario_actual.nombre} ({self.usuario_actual.rol})"
        )
        self.root.geometry("900x600")
        self.root.configure(bg="#ECF0F1")

        self.cargar_assets()
        self.crear_interfaz()

    def cargar_assets(self):
        """Carga de recursos visuales y escalado con Pillow respetando nombres de archivos"""
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        assets_dir = os.path.join(base_dir, "assets")
        self.iconos = {}

        # Diccionario con los nombres exactos que proveíste y colores opcionales si hiciera falta.
        archivos = {
            "logo": "logo.png",
            "registrar": "btn_registrar.png",
            "actualizar": "btn_actualizar.png",
            "eliminar": "btn_eliminar.png",
        }

        for clave, archivo in archivos.items():
            ruta = os.path.join(assets_dir, archivo)
            if os.path.exists(ruta):
                img = Image.open(ruta)
                # Logo más grande, botones más pequeños
                tamano = (100, 100) if clave == "logo" else (20, 20)
                img = img.resize(tamano, Image.Resampling.LANCZOS)
                self.iconos[clave] = ImageTk.PhotoImage(img)
            else:
                print(f"Advertencia: No se encontró {archivo} en assets/")
                self.iconos[clave] = None

    def crear_interfaz(self):
        # Frame Lateral (Menú)
        self.frame_menu = tk.Frame(self.root, bg="#2C3E50", width=200)
        self.frame_menu.pack(side="left", fill="y")

        # Logo del restaurante
        if self.iconos.get("logo"):
            lbl_logo = tk.Label(
                self.frame_menu, image=self.iconos["logo"], bg="#2C3E50"
            )
            lbl_logo.pack(pady=20)

        tk.Label(
            self.frame_menu,
            text=f"Hola,\n{self.usuario_actual.nombre}",
            bg="#2C3E50",
            fg="white",
            font=("Segoe UI", 12),
        ).pack(pady=10)

        # Solo el Administrador ve el botón de Usuarios
        if self.usuario_actual.rol == "Administrador":
            btn_usuarios = tk.Button(
                self.frame_menu,
                text=" Gestión Usuarios",
                bg="#34495E",
                fg="white",
                relief="flat",
                font=("Segoe UI", 11),
                cursor="hand2",
            )
            btn_usuarios.pack(fill="x", pady=5, ipady=10)

        # Frame Principal (Contenido)
        self.frame_contenido = tk.Frame(self.root, bg="#ECF0F1")
        self.frame_contenido.pack(side="right", fill="both", expand=True)

        if self.usuario_actual.rol == "Administrador":
            self.mostrar_gestion_usuarios()
        else:
            tk.Label(
                self.frame_contenido,
                text="Bienvenido al Sistema de Restaurante.\n(Solo administradores pueden gestionar usuarios)",
                font=("Segoe UI", 14),
                bg="#ECF0F1",
            ).pack(pady=100)

    def mostrar_gestion_usuarios(self):
        # Título
        tk.Label(
            self.frame_contenido,
            text="Gestión de Usuarios",
            font=("Segoe UI", 16, "bold"),
            bg="#ECF0F1",
            fg="#2C3E50",
        ).pack(pady=15)

        # Frame del Formulario
        frame_form = tk.Frame(self.frame_contenido, bg="#ECF0F1")
        frame_form.pack(fill="x", padx=20, pady=10)

        # Variables del formulario
        self.var_id = tk.StringVar()
        self.var_nombre = tk.StringVar()
        self.var_user = tk.StringVar()
        self.var_pass = tk.StringVar()
        self.var_rol = tk.StringVar()
        self.var_estado_label = tk.StringVar(
            value="Listo"
        )  # Para mostrar feedback de Combobox

        # Campos
        tk.Label(frame_form, text="ID Usuario:", bg="#ECF0F1").grid(
            row=0, column=0, padx=5, pady=5, sticky="e"
        )
        tk.Entry(frame_form, textvariable=self.var_id).grid(
            row=0, column=1, padx=5, pady=5
        )

        tk.Label(frame_form, text="Nombre:", bg="#ECF0F1").grid(
            row=0, column=2, padx=5, pady=5, sticky="e"
        )
        tk.Entry(frame_form, textvariable=self.var_nombre).grid(
            row=0, column=3, padx=5, pady=5
        )

        tk.Label(frame_form, text="Username:", bg="#ECF0F1").grid(
            row=1, column=0, padx=5, pady=5, sticky="e"
        )
        tk.Entry(frame_form, textvariable=self.var_user).grid(
            row=1, column=1, padx=5, pady=5
        )

        tk.Label(frame_form, text="Password:", bg="#ECF0F1").grid(
            row=1, column=2, padx=5, pady=5, sticky="e"
        )
        tk.Entry(frame_form, textvariable=self.var_pass, show="*").grid(
            row=1, column=3, padx=5, pady=5
        )

        tk.Label(frame_form, text="Rol:", bg="#ECF0F1").grid(
            row=2, column=0, padx=5, pady=5, sticky="e"
        )
        self.combo_rol = ttk.Combobox(
            frame_form,
            textvariable=self.var_rol,
            values=["Administrador", "Empleado", "Cliente"],
            state="readonly",
        )
        self.combo_rol.grid(row=2, column=1, padx=5, pady=5)

        lbl_estado = tk.Label(
            frame_form,
            textvariable=self.var_estado_label,
            bg="#ECF0F1",
            fg="#E67E22",
            font=("Segoe UI", 9, "italic"),
        )
        lbl_estado.grid(row=2, column=2, columnspan=2, sticky="w", padx=5)

        # Botones con Íconos (Manejo command=) - CORREGIDO
        frame_botones = tk.Frame(self.frame_contenido, bg="#ECF0F1")
        frame_botones.pack(pady=10)

        # Botón Registrar
        btn_registrar = tk.Button(
            frame_botones,
            text=" Registrar (Enter)",
            compound="left",
            bg="#27AE60",
            fg="white",
            relief="flat",
            cursor="hand2",
            command=self.registrar,
        )
        if self.iconos.get("registrar"):
            btn_registrar.config(image=self.iconos["registrar"])
        btn_registrar.grid(row=0, column=0, padx=10, ipady=3, ipadx=5)

        # Botón Actualizar
        btn_actualizar = tk.Button(
            frame_botones,
            text=" Actualizar",
            compound="left",
            bg="#F39C12",
            fg="white",
            relief="flat",
            cursor="hand2",
            command=self.actualizar,
        )
        if self.iconos.get("actualizar"):
            btn_actualizar.config(image=self.iconos["actualizar"])
        btn_actualizar.grid(row=0, column=1, padx=10, ipady=3, ipadx=5)

        # Botón Eliminar
        btn_eliminar = tk.Button(
            frame_botones,
            text=" Eliminar",
            compound="left",
            bg="#C0392B",
            fg="white",
            relief="flat",
            cursor="hand2",
            command=self.eliminar,
        )
        if self.iconos.get("eliminar"):
            btn_eliminar.config(image=self.iconos["eliminar"])
        btn_eliminar.grid(row=0, column=2, padx=10, ipady=3, ipadx=5)

        # Botón Limpiar (No lleva ícono, se mantiene igual)
        tk.Button(
            frame_botones,
            text=" Limpiar (Esc)",
            bg="#7F8C8D",
            fg="white",
            relief="flat",
            cursor="hand2",
            command=self.limpiar_form,
        ).grid(row=0, column=3, padx=10, ipady=3, ipadx=5)

        # Tabla Treeview
        columnas = ("ID", "Nombre", "Username", "Rol")
        self.tree = ttk.Treeview(
            self.frame_contenido, columns=columnas, show="headings", height=12
        )
        for col in columnas:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree.pack(fill="x", padx=20, pady=10)

        # ==========================================
        # SECCIÓN SEMANA 16: MANEJO DE EVENTOS (BIND)
        # ==========================================

        # 1. Evento <<TreeviewSelect>>: Cargar datos al seleccionar
        self.tree.bind("<<TreeviewSelect>>", self.cargar_datos_seleccionados)

        # 2. Evento <Return>: Ejecutar registro
        self.root.bind("<Return>", lambda event: self.registrar())

        # 3. Evento <Escape>: Limpiar formulario
        self.root.bind("<Escape>", lambda event: self.limpiar_form())

        # 4. Evento <<ComboboxSelected>>: Reaccionar al cambio de rol
        self.combo_rol.bind("<<ComboboxSelected>>", self.rol_seleccionado)

        self.actualizar_tabla()

    # --- Callbacks y Métodos de Acción ---

    def rol_seleccionado(self, event):
        """Callback para el evento <<ComboboxSelected>>"""
        rol = self.var_rol.get()
        self.var_estado_label.set(f"Nivel de acceso: {rol} seleccionado.")

    def cargar_datos_seleccionados(self, event):
        """Callback para el evento <<TreeviewSelect>>"""
        seleccion = self.tree.selection()
        if seleccion:
            item = self.tree.item(seleccion[0])
            id_usuario = item["values"][0]

            # Consultamos el servicio para evitar obtener la contraseña de la tabla (seguridad)
            usuarios = self.servicio.obtener_usuarios()
            usuario = next((u for u in usuarios if u.id_usuario == id_usuario), None)

            if usuario:
                self.var_id.set(usuario.id_usuario)
                self.var_nombre.set(usuario.nombre)
                self.var_user.set(usuario.username)
                self.var_pass.set(usuario.password)
                self.var_rol.set(usuario.rol)
                # Deshabilitar ID para evitar que lo modifiquen
                self.var_estado_label.set("Usuario cargado para edición.")

    def registrar(self):
        try:
            # Validaciones básicas de interfaz
            if not all(
                [
                    self.var_id.get(),
                    self.var_nombre.get(),
                    self.var_user.get(),
                    self.var_pass.get(),
                    self.var_rol.get(),
                ]
            ):
                messagebox.showwarning(
                    "Advertencia", "Todos los campos son obligatorios."
                )
                return

            self.servicio.registrar_usuario(
                self.var_id.get(),
                self.var_nombre.get(),
                self.var_user.get(),
                self.var_pass.get(),
                self.var_rol.get(),
            )
            messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
            self.limpiar_form()
            self.actualizar_tabla()
        except ValueError as e:
            messagebox.showerror("Error de Validación", str(e))

    def actualizar(self):
        try:
            self.servicio.actualizar_usuario(
                self.var_id.get(),
                self.var_nombre.get(),
                self.var_user.get(),
                self.var_pass.get(),
                self.var_rol.get(),
            )
            messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
            self.limpiar_form()
            self.actualizar_tabla()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def eliminar(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un usuario de la tabla.")
            return

        if messagebox.askyesno("Confirmar", "¿Está seguro de eliminar este usuario?"):
            try:
                self.servicio.eliminar_usuario(
                    self.var_id.get(), self.usuario_actual.id_usuario
                )
                messagebox.showinfo("Éxito", "Usuario eliminado.")
                self.limpiar_form()
                self.actualizar_tabla()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def limpiar_form(self):
        """Callback que también se activa con <Escape>"""
        self.var_id.set("")
        self.var_nombre.set("")
        self.var_user.set("")
        self.var_pass.set("")
        self.var_rol.set("")
        self.var_estado_label.set("Listo")
        for item in self.tree.selection():
            self.tree.selection_remove(item)

    def actualizar_tabla(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        usuarios = self.servicio.obtener_usuarios()
        for u in usuarios:
            self.tree.insert(
                "", "end", values=(u.id_usuario, u.nombre, u.username, u.rol)
            )
