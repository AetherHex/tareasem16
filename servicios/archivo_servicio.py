import json
import os


class ArchivoServicio:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATOS_DIR = os.path.join(BASE_DIR, "datos")

    @classmethod
    def leer_json(cls, nombre_archivo):
        ruta = os.path.join(cls.DATOS_DIR, nombre_archivo)
        if not os.path.exists(ruta):
            return []
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)

    @classmethod
    def escribir_json(cls, nombre_archivo, datos):
        os.makedirs(cls.DATOS_DIR, exist_ok=True)
        ruta = os.path.join(cls.DATOS_DIR, nombre_archivo)
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)
