class Usuario:
    def __init__(self, id_usuario, nombre, username, password, rol):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.username = username
        self.password = password
        self.rol = rol  # Administrador, Empleado, Cliente

    def to_dict(self):
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "username": self.username,
            "password": self.password,
            "rol": self.rol,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id_usuario=data["id_usuario"],
            nombre=data["nombre"],
            username=data["username"],
            password=data["password"],
            rol=data.get("rol", "Cliente"),  # Cliente por defecto si no existe
        )
