class Venta:
    def __init__(self, id_venta, cliente, total, fecha):
        self.id_venta = id_venta
        self.cliente = cliente
        self.total = total
        self.fecha = fecha

    def to_dict(self):
        return {
            "id_venta": self.id_venta,
            "cliente": self.cliente,
            "total": self.total,
            "fecha": self.fecha,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id_venta=data["id_venta"],
            cliente=data["cliente"],
            total=data["total"],
            fecha=data["fecha"],
        )
