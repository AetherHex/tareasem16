import sys
import tkinter as tk

from ui.login_view import LoginView


def configurar_dpi():
    """Habilita la alta resolución (DPI awareness) en Windows para evitar que Tkinter se vea borroso."""
    if sys.platform == "win32":
        try:
            import ctypes

            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception as e:
            print("DPI Awareness no soportado:", e)


if __name__ == "__main__":
    configurar_dpi()
    root = tk.Tk()

    # Aplicar un tema base estilizado si está disponible
    try:
        from tkinter import ttk

        style = ttk.Style(root)
        if "clam" in style.theme_names():
            style.theme_use("clam")

        # Estilizar el Treeview
        style.configure(
            "Treeview",
            background="#FFFFFF",
            fieldbackground="#FFFFFF",
            foreground="#2C3E50",
            rowheight=25,
        )
        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold"),
            background="#E67E22",
            foreground="white",
        )
        style.map(
            "Treeview",
            background=[("selected", "#3498DB")],
            foreground=[("selected", "white")],
        )
    except Exception:
        pass

    app = LoginView(root)
    root.mainloop()
