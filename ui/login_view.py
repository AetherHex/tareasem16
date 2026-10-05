import tkinter as tk
from tkinter import messagebox

from servicios.restaurante_servicio import RestauranteServicio
from ui.main_view import MainView


class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurante App - Iniciar Sesión")
        self.root.geometry("400x350")
        self.root.configure(bg="#2C3E50")
        self.servicio = RestauranteServicio()

        # Estilo
        lbl_titulo = tk.Label(
            root,
            text="Iniciar Sesión",
            font=("Segoe UI", 18, "bold"),
            bg="#2C3E50",
            fg="white",
        )
        lbl_titulo.pack(pady=30)

        tk.Label(
            root, text="Usuario:", bg="#2C3E50", fg="white", font=("Segoe UI", 10)
        ).pack()
        self.entry_user = tk.Entry(root, font=("Segoe UI", 12), justify="center")
        self.entry_user.pack(pady=5, ipadx=5, ipady=3)

        tk.Label(
            root, text="Contraseña:", bg="#2C3E50", fg="white", font=("Segoe UI", 10)
        ).pack()
        self.entry_pass = tk.Entry(
            root, show="*", font=("Segoe UI", 12), justify="center"
        )
        self.entry_pass.pack(pady=5, ipadx=5, ipady=3)

        # Botón con color Naranja de acento
        btn_login = tk.Button(
            root,
            text="Ingresar",
            bg="#E67E22",
            fg="white",
            font=("Segoe UI", 12, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.iniciar_sesion,
        )
        btn_login.pack(pady=30, ipadx=20, ipady=5)

        # Evento Enter para login
        self.root.bind("<Return>", lambda event: self.iniciar_sesion())

    def iniciar_sesion(self):
        user = self.entry_user.get()
        password = self.entry_pass.get()
        usuario = self.servicio.autenticar(user, password)

        if usuario:
            self.root.destroy()
            root_main = tk.Tk()
            app = MainView(root_main, usuario)
            root_main.mainloop()
        else:
            messagebox.showerror("Error", "Credenciales incorrectas")
