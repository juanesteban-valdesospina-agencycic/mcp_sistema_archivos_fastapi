from pathlib import Path
from typing import List
from servicios.interfaces.obtener import Obtener


class ObtenerProyectos(Obtener):
    def obtener_proyectos(self, ruta: str = "/var/www") -> List[dict]:
        p = Path(ruta)
        if not p.exists() or not p.is_dir():
            return []
        return [
            {"nombre": f.name, "ruta": str(f.resolve())}
            for f in p.iterdir() if f.is_dir()
        ]
    
    def obtener_archivos_de_proyecto(self, proyecto: str, profundidad_maxima: int = 10, nivel: int = 0) -> List[dict]:
        if nivel > profundidad_maxima:
            return []
        p = Path(proyecto)
        if not p.exists() or not p.is_dir():
            return []
        resultado = []
        for f in p.iterdir():
            if f.is_file():
                resultado.append({
                    "nombre": f.name,
                    "ruta": str(f.resolve()),
                    "tipo": "archivo"
                })
            elif f.is_dir():
                resultado.append({
                    "nombre": f.name,
                    "ruta": str(f.resolve()),
                    "tipo": "carpeta",
                    "contenido": self.obtener_archivos_de_proyecto(str(f), profundidad_maxima, nivel + 1)
                })
        return resultado
    
    def leer_archivo(self, archivo: str) -> dict:
        p = Path(archivo)
        if not p.exists() or not p.is_file():
            return {"nombre": p.name, "ruta": str(p.resolve()), "contenido": None}
        return {"nombre": p.name, "ruta": str(p.resolve()), "contenido": p.read_text()}


