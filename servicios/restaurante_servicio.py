from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    ARCHIVO_USUARIOS = "usuarios.json"

    def obtener_usuarios(self):
        datos = ArchivoServicio.leer_json(self.ARCHIVO_USUARIOS)
        return [Usuario.from_dict(d) for d in datos]

    def guardar_usuarios(self, usuarios):
        datos = [u.to_dict() for u in usuarios]
        ArchivoServicio.escribir_json(self.ARCHIVO_USUARIOS, datos)

    def autenticar(self, username, password):
        usuarios = self.obtener_usuarios()
        for u in usuarios:
            if u.username == username and u.password == password:
                return u
        return None

    def registrar_usuario(self, id_usuario, nombre, username, password, rol):
        usuarios = self.obtener_usuarios()
        if any(u.id_usuario == id_usuario for u in usuarios):
            raise ValueError("El ID de usuario ya existe.")
        if any(u.username == username for u in usuarios):
            raise ValueError("El nombre de usuario (username) ya está en uso.")

        nuevo_usuario = Usuario(id_usuario, nombre, username, password, rol)
        usuarios.append(nuevo_usuario)
        self.guardar_usuarios(usuarios)

    def actualizar_usuario(self, id_usuario, nombre, username, password, rol):
        usuarios = self.obtener_usuarios()
        for u in usuarios:
            if u.id_usuario == id_usuario:
                u.nombre = nombre
                u.username = username
                u.password = password
                u.rol = rol
                self.guardar_usuarios(usuarios)
                return
        raise ValueError("Usuario no encontrado.")

    def eliminar_usuario(self, id_usuario, id_usuario_actual):
        if id_usuario == id_usuario_actual:
            raise ValueError(
                "No puedes eliminar tu propia cuenta mientras estás en sesión."
            )

        usuarios = self.obtener_usuarios()
        usuarios_filtrados = [u for u in usuarios if u.id_usuario != id_usuario]

        if len(usuarios) == len(usuarios_filtrados):
            raise ValueError("Usuario no encontrado.")

        self.guardar_usuarios(usuarios_filtrados)
